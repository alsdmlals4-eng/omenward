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
	var rejected := RouletteSpinResultScript.new() as RouletteSpinResult
	if economy == null or buildings == null or manifest == null:
		rejected.failure_reason = &"service_not_ready"
		return rejected
	if not economy.try_spend_gold(SPIN_COST):
		rejected.failure_reason = &"insufficient_gold"
		return rejected
	var requested_seed := int(seed_input.get("seed", manifest.seed))
	var rng: RandomNumberGenerator = DeterminismServiceScript.new(manifest.seed).create_roulette_rng(requested_seed)
	var sources: Array[Dictionary] = buildings.roulette_token_sources()
	var board := _generate_board(rng, sources)
	var result := resolve_board_snapshot(board, sources, rng.randi(), SPIN_COST, true)
	result.spin_seed = requested_seed
	if result.gold_reward > 0:
		economy.add_gold(result.gold_reward)
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


func _generate_board(rng: RandomNumberGenerator, sources: Array[Dictionary]) -> Array[StringName]:
	var weights := {
		X_SYMBOL: X_WEIGHT,
		GOLD_SYMBOL: GOLD_WEIGHT,
	}
	for source in sources:
		var symbol := StringName(source.get("symbol_id", &""))
		var weight := maxi(0, int(source.get("board_weight", 0)))
		if symbol != &"" and weight > 0:
			weights[symbol] = int(weights.get(symbol, 0)) + weight
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
