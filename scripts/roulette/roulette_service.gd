class_name RouletteService
extends RefCounted

const SPIN_COST := 20
const BOARD_SIZE := 9
const X_WEIGHT := 6
const GOLD_WEIGHT := 2
const X_SYMBOL := &"x"
const GOLD_SYMBOL := &"gold"
const LINE_INDEXES := [
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8],
	[0, 3, 6],
	[1, 4, 7],
	[2, 5, 8],
	[0, 4, 8],
	[2, 4, 6],
]
const UnitSpawnDefinitionScript = preload("res://scripts/data/unit_spawn_definition.gd")
const RouletteSpinResultScript = preload("res://scripts/data/roulette_spin_result.gd")
const DeterminismServiceScript = preload("res://scripts/core/determinism_service.gd")

var economy: Variant
var buildings: Variant
var manifest: Variant
var player_team_id: StringName
var legendary_generated := false


func _init(assigned_economy: Variant, assigned_buildings: Variant, assigned_manifest: Variant, assigned_player_team_id: StringName) -> void:
	economy = assigned_economy
	buildings = assigned_buildings
	manifest = assigned_manifest
	player_team_id = assigned_player_team_id


func spin(seed_input: Dictionary) -> RouletteSpinResult:
	var session := begin_paid_spin(seed_input, false)
	if not bool(session.get("accepted", false)):
		var rejected := RouletteSpinResultScript.new() as RouletteSpinResult
		rejected.failure_reason = StringName(session.get("failure_reason", &"service_not_ready"))
		return rejected
	return resolve_paid_board(
		session.get("board", []),
		int(session.get("resolution_seed", 0)),
		int(session.get("spin_seed", manifest.seed)),
	)


func begin_paid_spin(seed_input: Dictionary, record_stopped_board: bool = true) -> Dictionary:
	var session := {"accepted": false, "failure_reason": &"service_not_ready", "board": []}
	if economy == null or buildings == null or manifest == null:
		return session
	if not economy.try_spend_gold(SPIN_COST):
		session["failure_reason"] = &"insufficient_gold"
		return session
	var requested_seed := int(seed_input.get("seed", manifest.seed))
	var rng: RandomNumberGenerator = DeterminismServiceScript.new(manifest.seed).create_roulette_rng(requested_seed)
	var sources: Array[Dictionary] = buildings.roulette_token_sources()
	session = {
		"accepted": true,
		"failure_reason": &"",
		"board": _generate_board(rng, sources),
		"resolution_seed": rng.randi(),
		"spin_seed": requested_seed,
		"paid_cost": SPIN_COST,
	}
	if record_stopped_board:
		manifest.input_log.append({
			"action": "roulette_stopped",
			"spin_seed": requested_seed,
			"paid_cost": SPIN_COST,
			"board": (session["board"] as Array).map(func(symbol: StringName) -> String: return str(symbol)),
		})
	return session


func preview_paid_board(board: Array, resolution_seed: int) -> RouletteSpinResult:
	var sources: Array[Dictionary] = buildings.roulette_token_sources() if buildings != null else []
	return resolve_board_snapshot(board, sources, resolution_seed, SPIN_COST, false)


func resolve_paid_board(board: Array, resolution_seed: int, spin_seed: int) -> RouletteSpinResult:
	var sources: Array[Dictionary] = buildings.roulette_token_sources() if buildings != null else []
	var result := resolve_board_snapshot(board, sources, resolution_seed, SPIN_COST, true)
	result.spin_seed = spin_seed
	if result.gold_reward > 0 and economy != null:
		economy.add_gold(result.gold_reward)
	if manifest != null:
		manifest.input_log.append({
			"action": "roulette",
			"result": result.to_dictionary(),
		})
	return result


func resolve_board_snapshot(
	board_input: Array,
	sources: Array,
	resolution_seed: int,
	paid_cost: int = SPIN_COST,
	consume_legendary: bool = false,
) -> RouletteSpinResult:
	var result := RouletteSpinResultScript.new() as RouletteSpinResult
	result.paid_cost = paid_cost
	result.spin_seed = resolution_seed
	if board_input.size() != BOARD_SIZE:
		result.failure_reason = &"invalid_board"
		return result
	for value in board_input:
		result.board.append(StringName(value))
	result.accepted = true
	var judging_symbol := result.board[3]
	if judging_symbol == X_SYMBOL or result.board[4] != judging_symbol or result.board[5] != judging_symbol:
		return result
	result.judging_symbol = judging_symbol
	result.completed_line_count = _completed_line_count(result.board, judging_symbol)
	if result.completed_line_count <= 0:
		return result
	if judging_symbol == GOLD_SYMBOL:
		result.outcome_type = &"gold"
		result.gold_reward = _gold_reward(paid_cost, result.completed_line_count)
		return result
	var matching_sources := _matching_sources(sources, judging_symbol)
	if matching_sources.is_empty():
		result.accepted = false
		result.failure_reason = &"missing_reward_source"
		return result
	var source := _choose_source(matching_sources, resolution_seed)
	result.outcome_type = &"unit"
	result.rank_id = _rank_for_lines(result.completed_line_count)
	result.source_building_id = StringName(source.get("source_building_id", &""))
	result.source_tier_id = StringName(source.get("source_tier_id", &"tier_1"))
	var reward_count := 1
	if result.rank_id == &"legendary":
		if legendary_generated:
			result.rank_id = &"hero"
			result.legendary_converted_to_heroes = true
			reward_count = 2
		elif consume_legendary:
			legendary_generated = true
	if result.rank_id != &"common":
		result.template_resolution = &"source_archetype_rank_fallback"
	for _index in reward_count:
		result.rewards.append(_make_reward(source, result.rank_id))
	return result


func token_ledger(extra_sources: Array[Dictionary] = []) -> Array[Dictionary]:
	var sources: Array[Dictionary] = []
	if buildings != null:
		for source in buildings.roulette_token_sources():
			sources.append((source as Dictionary).duplicate(true))
	return token_ledger_from_sources(sources, extra_sources)


func token_ledger_from_sources(
	base_sources: Array[Dictionary],
	extra_sources: Array[Dictionary] = [],
) -> Array[Dictionary]:
	var sources: Array[Dictionary] = []
	for source in base_sources:
		sources.append(source.duplicate(true))
	for source in extra_sources:
		sources.append(source.duplicate(true))
	var weights := _weight_snapshot(sources)
	var total_weight := 0
	for weight in weights.values():
		total_weight += int(weight)
	var source_groups := {}
	for source in sources:
		var symbol := StringName(source.get("symbol_id", &""))
		if symbol == &"":
			continue
		if not source_groups.has(symbol):
			source_groups[symbol] = []
		(source_groups[symbol] as Array).append(source)
	var symbol_names: Array[String] = []
	for symbol in weights:
		symbol_names.append(str(symbol))
	symbol_names.sort()
	var ledger: Array[Dictionary] = []
	for symbol_name in symbol_names:
		var symbol := StringName(symbol_name)
		var grouped_sources: Array = source_groups.get(symbol, [])
		var source_ids: Array[String] = []
		var reward_ids: Array[String] = []
		for source in grouped_sources:
			source_ids.append(str(source.get("source_building_id", "")))
			reward_ids.append(str(source.get("reward_archetype_id", "")))
		source_ids.sort()
		reward_ids.sort()
		var weight := int(weights[symbol])
		ledger.append({
			"symbol_id": symbol_name,
			"weight": weight,
			"probability": float(weight) / float(total_weight) if total_weight > 0 else 0.0,
			"source_count": grouped_sources.size(),
			"source_building_ids": source_ids,
			"reward_archetype_ids": reward_ids,
			"total_weight": total_weight,
		})
	return ledger


func probability_for_symbol(symbol_id: StringName, extra_sources: Array[Dictionary] = []) -> float:
	for entry in token_ledger(extra_sources):
		if StringName(entry.get("symbol_id", &"")) == symbol_id:
			return float(entry.get("probability", 0.0))
	return 0.0


func probability_for_symbol_from_sources(
	symbol_id: StringName,
	base_sources: Array[Dictionary],
	extra_sources: Array[Dictionary] = [],
) -> float:
	for entry in token_ledger_from_sources(base_sources, extra_sources):
		if StringName(entry.get("symbol_id", &"")) == symbol_id:
			return float(entry.get("probability", 0.0))
	return 0.0


func _weight_snapshot(sources: Array[Dictionary]) -> Dictionary:
	var weights := {
		X_SYMBOL: X_WEIGHT,
		GOLD_SYMBOL: GOLD_WEIGHT,
	}
	for source in sources:
		var symbol := StringName(source.get("symbol_id", &""))
		var weight := maxi(0, int(source.get("board_weight", 0)))
		if symbol != &"" and weight > 0:
			weights[symbol] = int(weights.get(symbol, 0)) + weight
	return weights


func _generate_board(rng: RandomNumberGenerator, sources: Array[Dictionary]) -> Array[StringName]:
	var weights := _weight_snapshot(sources)
	var board: Array[StringName] = []
	for _index in BOARD_SIZE:
		board.append(_weighted_symbol(rng, weights))
	return board


func _weighted_symbol(rng: RandomNumberGenerator, weights: Dictionary) -> StringName:
	var names: Array[String] = []
	var total := 0
	for key in weights:
		var weight := maxi(0, int(weights[key]))
		if weight <= 0:
			continue
		names.append(str(key))
		total += weight
	names.sort()
	if total <= 0:
		return X_SYMBOL
	var roll := rng.randi_range(1, total)
	for name in names:
		var symbol := StringName(name)
		roll -= int(weights[symbol])
		if roll <= 0:
			return symbol
	return X_SYMBOL


func _completed_line_count(board: Array[StringName], symbol: StringName) -> int:
	var count := 0
	for line in LINE_INDEXES:
		var complete := true
		for index in line:
			if board[int(index)] != symbol:
				complete = false
				break
		if complete:
			count += 1
	return count


func _rank_for_lines(line_count: int) -> StringName:
	if line_count <= 1:
		return &"common"
	if line_count == 2:
		return &"elite"
	if line_count < 8:
		return &"hero"
	return &"legendary"


func _gold_reward(paid_cost: int, line_count: int) -> int:
	if line_count <= 1:
		return int(floor(float(paid_cost) * 0.75))
	if line_count == 2:
		return paid_cost * 2
	return paid_cost * 5


func _matching_sources(sources: Array, symbol: StringName) -> Array[Dictionary]:
	var matching: Array[Dictionary] = []
	for source in sources:
		if StringName(source.get("symbol_id", &"")) == symbol:
			matching.append((source as Dictionary).duplicate(true))
	matching.sort_custom(func(a: Dictionary, b: Dictionary) -> bool:
		return str(a.get("source_building_id", "")) < str(b.get("source_building_id", ""))
	)
	return matching


func _choose_source(sources: Array[Dictionary], resolution_seed: int) -> Dictionary:
	if sources.size() == 1:
		return sources[0]
	var rng: RandomNumberGenerator = DeterminismServiceScript.new(manifest.seed if manifest != null else 0).create_roulette_rng(resolution_seed)
	var total := 0
	for source in sources:
		total += maxi(1, int(source.get("source_weight", 1)))
	var roll := rng.randi_range(1, total)
	for source in sources:
		roll -= maxi(1, int(source.get("source_weight", 1)))
		if roll <= 0:
			return source
	return sources.back()


func _make_reward(source: Dictionary, rank_id: StringName) -> UnitSpawnDefinition:
	var reward := UnitSpawnDefinitionScript.new() as UnitSpawnDefinition
	reward.archetype_id = StringName(source.get("reward_archetype_id", &""))
	reward.tier_id = StringName(source.get("source_tier_id", &"tier_1"))
	reward.rank_id = rank_id
	reward.owner_team_id = player_team_id
	reward.visual_faction_id = player_team_id
	return reward
