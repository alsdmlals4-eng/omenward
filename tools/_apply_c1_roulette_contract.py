from __future__ import annotations

import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def write(relative: str, content: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def replace_once(relative: str, old: str, new: str) -> None:
    text = read(relative)
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{relative}: expected one literal match, found {count}: {old[:120]!r}")
    write(relative, text.replace(old, new, 1))


def replace_regex(relative: str, pattern: str, replacement: str) -> None:
    text = read(relative)
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"{relative}: expected one regex match, found {count}: {pattern!r}")
    write(relative, updated)


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


write(
    "scripts/data/roulette_spin_result.gd",
    '''class_name RouletteSpinResult
extends RefCounted

var accepted := false
var failure_reason: StringName = &""
var board: Array[StringName] = []
var judging_symbol: StringName = &""
var completed_line_count := 0
var rank_id: StringName = &""
var outcome_type: StringName = &"none"
var rewards: Array[UnitSpawnDefinition] = []
var gold_reward := 0
var paid_cost := 0
var spin_seed := 0
var source_building_id: StringName = &""
var source_tier_id: StringName = &""
var legendary_converted_to_heroes := false
var template_resolution: StringName = &""


func to_dictionary() -> Dictionary:
	var reward_dictionaries: Array[Dictionary] = []
	for reward in rewards:
		reward_dictionaries.append(reward.to_dictionary())
	return {
		"accepted": accepted,
		"failure_reason": str(failure_reason),
		"board": board.map(func(symbol: StringName) -> String: return str(symbol)),
		"judging_symbol": str(judging_symbol),
		"completed_line_count": completed_line_count,
		"rank_id": str(rank_id),
		"outcome_type": str(outcome_type),
		"rewards": reward_dictionaries,
		"gold_reward": gold_reward,
		"paid_cost": paid_cost,
		"spin_seed": spin_seed,
		"source_building_id": str(source_building_id),
		"source_tier_id": str(source_tier_id),
		"legendary_converted_to_heroes": legendary_converted_to_heroes,
		"template_resolution": str(template_resolution),
	}
''',
)

write(
    "scripts/data/building_definition.gd",
    '''class_name BuildingDefinition
extends Resource

@export var building_id: StringName
@export var gold_cost: int
@export var food_cap_bonus: int
@export var roulette_symbol_id: StringName
@export var roulette_reward_archetype_id: StringName
@export var roulette_board_weight: int
@export var roulette_source_tier_id: StringName = &"tier_1"
@export var roulette_source_weight: int = 1
''',
)

write(
    "scripts/buildings/building_service.gd",
    '''class_name BuildingService
extends RefCounted

const PLAYER_TEAM_ID := &"lumern"
const BuildingDefinitionScript = preload("res://scripts/data/building_definition.gd")
const BuildingStateScript = preload("res://scripts/buildings/building_state.gd")

var economy: Variant
var manifest: Variant
var definitions := {}
var _outposts := {}
var _nodes := {}
var _buildings := {}


func _init(assigned_economy: Variant, assigned_manifest: Variant) -> void:
	economy = assigned_economy
	manifest = assigned_manifest
	definitions = {
		&"barracks": _definition(&"barracks", 40, 0, &"warrior", &"shield_guard", 3, &"tier_1", 1),
		&"tower": _definition(&"tower", 35, 0, &"", &"", 0, &"tier_1", 0),
		&"farm": _definition(&"farm", 35, 6, &"", &"", 0, &"tier_1", 0),
	}


func register_outpost(outpost_id: StringName, outpost: Variant, node_ids: Array) -> void:
	_outposts[outpost_id] = outpost
	_nodes[outpost_id] = node_ids.duplicate()


func try_construct(outpost_id: StringName, node_id: StringName, building_id: StringName) -> bool:
	if not definitions.has(building_id) or not _node_is_available(outpost_id, node_id):
		return false
	var definition: Variant = definitions[building_id]
	if not economy.try_spend_gold(definition.gold_cost):
		return false
	var outpost: Variant = _outposts[outpost_id]
	var state: Variant = BuildingStateScript.new(outpost_id, node_id, definition, outpost.capture_revision)
	_buildings[_key(outpost_id, node_id)] = state
	if definition.food_cap_bonus > 0:
		economy.add_food_cap(definition.food_cap_bonus)
	manifest.input_log.append({
		"action": "build",
		"outpost_id": str(outpost_id),
		"node_id": str(node_id),
		"building_id": str(building_id),
	})
	return true


func roulette_token_sources() -> Array[Dictionary]:
	var sources: Array[Dictionary] = []
	var keys: Array = _buildings.keys()
	keys.sort()
	for key in keys:
		var state: Variant = _buildings[key]
		var definition: BuildingDefinition = state.definition
		if not _outpost_is_active_for_player(state.outpost_id) or not _building_matches_current_capture(state):
			continue
		if definition.roulette_symbol_id == &"" or definition.roulette_board_weight <= 0:
			continue
		sources.append({
			"symbol_id": definition.roulette_symbol_id,
			"reward_archetype_id": definition.roulette_reward_archetype_id,
			"board_weight": definition.roulette_board_weight,
			"source_tier_id": definition.roulette_source_tier_id,
			"source_weight": definition.roulette_source_weight,
			"source_building_id": StringName(str(key)),
		})
	return sources


func _node_is_available(outpost_id: StringName, node_id: StringName) -> bool:
	if not _nodes.has(outpost_id) or not (_nodes[outpost_id] as Array).has(node_id):
		return false
	var key := _key(outpost_id, node_id)
	if _buildings.has(key):
		var state: Variant = _buildings[key]
		if _building_matches_current_capture(state):
			return false
		_buildings.erase(key)
	return _outpost_is_active_for_player(outpost_id)


func _outpost_is_active_for_player(outpost_id: StringName) -> bool:
	if not _outposts.has(outpost_id):
		return false
	var outpost: Variant = _outposts[outpost_id]
	return outpost.owner_team_id == PLAYER_TEAM_ID and outpost.state == outpost.STABLE and not outpost.construction_locked


func _building_matches_current_capture(state: Variant) -> bool:
	if not _outposts.has(state.outpost_id):
		return false
	var outpost: Variant = _outposts[state.outpost_id]
	return state.capture_revision == outpost.capture_revision


func _definition(
	building_id: StringName,
	gold_cost: int,
	food_cap_bonus: int,
	symbol_id: StringName,
	reward_archetype_id: StringName,
	board_weight: int,
	source_tier_id: StringName,
	source_weight: int,
) -> BuildingDefinition:
	var definition := BuildingDefinitionScript.new() as BuildingDefinition
	definition.building_id = building_id
	definition.gold_cost = gold_cost
	definition.food_cap_bonus = food_cap_bonus
	definition.roulette_symbol_id = symbol_id
	definition.roulette_reward_archetype_id = reward_archetype_id
	definition.roulette_board_weight = board_weight
	definition.roulette_source_tier_id = source_tier_id
	definition.roulette_source_weight = source_weight
	return definition


func _key(outpost_id: StringName, node_id: StringName) -> String:
	return "%s:%s" % [outpost_id, node_id]
''',
)

write(
    "scripts/roulette/roulette_service.gd",
    '''class_name RouletteService
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
''',
)

replace_once(
    "scripts/core/stage_economy.gd",
    "func add_food_cap(amount: int) -> void:\n\tfood_cap += maxi(0, amount)\n",
    "func add_gold(amount: int) -> void:\n\tgold += maxi(0, amount)\n\n\nfunc add_food_cap(amount: int) -> void:\n\tfood_cap += maxi(0, amount)\n",
)

write(
    "scripts/core/stage_run.gd",
    '''class_name StageRun
extends RefCounted

const DataRegistryScript = preload("res://scripts/core/data_registry.gd")
const CombatClockScript = preload("res://scripts/core/combat_clock.gd")
const StageEconomyScript = preload("res://scripts/core/stage_economy.gd")
const BuildingServiceScript = preload("res://scripts/buildings/building_service.gd")
const RouletteServiceScript = preload("res://scripts/roulette/roulette_service.gd")
const RouletteSpinResultScript = preload("res://scripts/data/roulette_spin_result.gd")
const DeploymentServiceScript = preload("res://scripts/units/deployment_service.gd")
const WaveDirectorScript = preload("res://scripts/waves/wave_director.gd")
const BattleSimulatorScript = preload("res://scripts/battle/battle_simulator.gd")
const StageProgressionScript = preload("res://scripts/core/stage_progression.gd")
const OutpostStateScript = preload("res://scripts/battle/outpost_state.gd")

const RUNNING := &"running"
const VICTORY := &"victory"
const DEFEAT := &"defeat"

var progression: Variant
var stage: Variant
var manifest: Variant
var clock: Variant
var economy: Variant
var buildings: Variant
var roulette: Variant
var deployment: Variant
var wave_director: Variant
var battle: Variant
var current_wave := 0
var result_state: StringName = &""
var pending_roulette_rewards: Array[UnitSpawnDefinition] = []
var last_roulette_result: RouletteSpinResult

var _registry: Variant
var _home_outpost: Variant


func _init(assigned_progression: Variant = null) -> void:
	progression = assigned_progression if assigned_progression != null else StageProgressionScript.new()


func start(assigned_stage: Variant, seed: int) -> void:
	stage = assigned_stage
	current_wave = 0
	result_state = &""
	pending_roulette_rewards.clear()
	last_roulette_result = null
	if stage == null or not progression.can_start(stage):
		return
	_registry = DataRegistryScript.new()
	var errors: PackedStringArray = _registry.load_bootstrap_catalog("res://data/bootstrap_catalog.tres")
	if not errors.is_empty():
		result_state = DEFEAT
		return
	manifest = stage.build_manifest(seed)
	clock = CombatClockScript.new()
	clock.is_planning = false
	economy = StageEconomyScript.new(manifest)
	buildings = BuildingServiceScript.new(economy, manifest)
	_home_outpost = OutpostStateScript.new(&"lumern")
	buildings.register_outpost(&"home", _home_outpost, [&"front_a", &"front_b", &"rear"])
	roulette = RouletteServiceScript.new(economy, buildings, manifest, &"lumern")
	deployment = DeploymentServiceScript.new(economy, manifest)
	wave_director = WaveDirectorScript.new(stage)
	battle = BattleSimulatorScript.new(_registry, seed)
	result_state = RUNNING


func spin_roulette(seed_input: Dictionary) -> RouletteSpinResult:
	if roulette == null:
		var unavailable := RouletteSpinResultScript.new() as RouletteSpinResult
		unavailable.failure_reason = &"service_not_ready"
		return unavailable
	if not pending_roulette_rewards.is_empty():
		var blocked := RouletteSpinResultScript.new() as RouletteSpinResult
		blocked.failure_reason = &"pending_reward"
		last_roulette_result = blocked
		return blocked
	var result: RouletteSpinResult = roulette.spin(seed_input)
	last_roulette_result = result
	store_roulette_result(result)
	return result


func store_roulette_result(result: RouletteSpinResult) -> bool:
	if result == null or not result.accepted:
		return false
	for reward in result.rewards:
		pending_roulette_rewards.append(reward.duplicate() as UnitSpawnDefinition)
	return true


func construct_home(building_id: StringName) -> bool:
	if buildings == null:
		return false
	var node_by_building := {
		&"tower": &"front_a",
		&"farm": &"front_b",
		&"barracks": &"rear",
	}
	if not node_by_building.has(building_id):
		return false
	return buildings.try_construct(&"home", node_by_building[building_id], building_id)


func deploy_next_roulette_reward(lane_id: StringName) -> bool:
	if pending_roulette_rewards.is_empty():
		return false
	var reward := pending_roulette_rewards.front()
	if not deploy_card(reward, lane_id):
		return false
	pending_roulette_rewards.pop_front()
	return true


func deploy_card(card: UnitSpawnDefinition, lane_id: StringName) -> bool:
	if deployment == null or battle == null or not deployment.deploy(card, lane_id, 10.0):
		return false
	var deployed := card.duplicate() as UnitSpawnDefinition
	deployed.lane_id = lane_id
	return battle.spawn_unit(deployed) != null


func submit_command(command: Dictionary) -> bool:
	if result_state != RUNNING:
		return false
	match command.get("action", ""):
		"stage_victory":
			result_state = VICTORY
			progression.record_victory(stage)
		"stage_defeat":
			result_state = DEFEAT
		_:
			return false
	manifest.input_log.append(command.duplicate(true))
	return true


func advance(delta: float) -> void:
	if result_state != RUNNING:
		return
	clock.advance(delta)
	economy.advance(delta, 0, _stable_owned_outpost_count())
	for wave in wave_director.advance(delta):
		current_wave = wave.wave_number
		for spawn in wave.spawns:
			battle.spawn_unit(spawn.duplicate() as UnitSpawnDefinition)
		manifest.input_log.append({"action": "wave", "wave_number": current_wave})
	battle.advance(delta)


func _stable_owned_outpost_count() -> int:
	if battle == null:
		return 0
	var count := 0
	for lane_id in battle.LANE_IDS:
		var outpost: Variant = battle.clash_zones[lane_id].outpost
		if outpost.owner_team_id == &"lumern" and outpost.state == outpost.STABLE:
			count += 1
	return count
''',
)

write(
    "scripts/ui/stage_hud.gd",
    '''class_name StageHud
extends Control

@onready var _resource_label: Label = $ResourceLabel
@onready var _wave_label: Label = $WaveLabel
@onready var _omen_label: Label = $OmenLabel
@onready var _cards_label: Label = $CardsLabel
@onready var _result_label: Label = $ResultLabel
@onready var _retry_button: Button = $RetryButton

var run: Variant
var _spin_index := 0


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	_update_display()


func _process(_delta: float) -> void:
	_update_display()


func _on_spin_pressed() -> void:
	if run == null:
		return
	_spin_index += 1
	run.spin_roulette({"seed": _spin_index})
	_update_display()


func _on_barracks_pressed() -> void:
	if run != null:
		run.construct_home(&"barracks")
	_update_display()


func _on_tower_pressed() -> void:
	if run != null:
		run.construct_home(&"tower")
	_update_display()


func _on_farm_pressed() -> void:
	if run != null:
		run.construct_home(&"farm")
	_update_display()


func _on_deploy_pressed(lane_id: StringName) -> void:
	if run != null:
		run.deploy_next_roulette_reward(lane_id)
	_update_display()


func _on_retry_pressed() -> void:
	var session := get_node_or_null("../../GameSession")
	if session != null:
		session.retry_stage()


func _update_display() -> void:
	if run == null or run.economy == null:
		return
	_resource_label.text = "Gold %d   Food %d/%d" % [run.economy.gold, run.economy.food_used, run.economy.food_cap]
	_wave_label.text = "Wave %d" % run.current_wave
	var omen: float = float(run.wave_director.omen_seconds_remaining()) if run.wave_director != null else 0.0
	_omen_label.text = "Next omen %.0fs" % omen
	var result: Variant = run.last_roulette_result
	var board_text := "-"
	var outcome_text := "none"
	if result != null:
		board_text = ",".join(result.board.map(func(symbol: StringName) -> String: return str(symbol)))
		outcome_text = "%s %s lines=%d gold=%d" % [str(result.outcome_type), str(result.rank_id), result.completed_line_count, result.gold_reward]
		if not result.accepted and result.failure_reason != &"":
			outcome_text = "blocked: %s" % str(result.failure_reason)
	_cards_label.text = "Board [%s] | %s | Pending %d" % [board_text, outcome_text, run.pending_roulette_rewards.size()]
	_result_label.visible = run.result_state != run.RUNNING
	_result_label.text = "Stage %s" % str(run.result_state).capitalize()
	_retry_button.visible = run.result_state != run.RUNNING
''',
)

scene = read("scenes/ui/stage_hud.tscn")
scene = scene.replace(
    '[node name="TowerButton" type="Button" parent="."]\nlayout_mode = 0\noffset_left = 144.0\noffset_top = 450.0\noffset_right = 232.0\noffset_bottom = 486.0\ntext = "Tower"\n',
    '[node name="BarracksButton" type="Button" parent="."]\nlayout_mode = 0\noffset_left = 144.0\noffset_top = 450.0\noffset_right = 242.0\noffset_bottom = 486.0\ntext = "Barracks"\n\n[node name="TowerButton" type="Button" parent="."]\nlayout_mode = 0\noffset_left = 252.0\noffset_top = 450.0\noffset_right = 330.0\noffset_bottom = 486.0\ntext = "Tower"\n',
    1,
)
scene = scene.replace(
    'offset_left = 242.0\noffset_top = 450.0\noffset_right = 330.0\noffset_bottom = 486.0\ntext = "Farm"',
    'offset_left = 340.0\noffset_top = 450.0\noffset_right = 418.0\noffset_bottom = 486.0\ntext = "Farm"',
    1,
)
scene = scene.replace('offset_left = 344.0\noffset_top = 450.0\noffset_right = 700.0', 'offset_left = 428.0\noffset_top = 450.0\noffset_right = 704.0', 1)
scene = scene.replace('[connection signal="pressed" from="TowerButton"', '[connection signal="pressed" from="BarracksButton" to="." method="_on_barracks_pressed"]\n[connection signal="pressed" from="TowerButton"', 1)
write("scenes/ui/stage_hud.tscn", scene)

write(
    "tests/headless/roulette_contract_test.gd",
    '''extends SceneTree

const StageManifest = preload("res://scripts/core/stage_manifest.gd")


func _init() -> void:
	var failures := PackedStringArray()
	var roulette_script := load("res://scripts/roulette/roulette_service.gd")
	_expect(roulette_script != null, "roulette service loads", failures)
	if roulette_script != null:
		_test_judgment_line_gate(roulette_script, failures)
		_test_grade_mapping(roulette_script, failures)
		_test_gold_payout(roulette_script, failures)
		_test_legendary_limit(roulette_script, failures)
	_finish(failures)


func _test_judgment_line_gate(roulette_script: GDScript, failures: PackedStringArray) -> void:
	var service: Variant = roulette_script.new(null, null, _manifest(), &"lumern")
	var result: Variant = service.resolve_board_snapshot([
		&"warrior", &"warrior", &"warrior",
		&"warrior", &"warrior", &"x",
		&"x", &"gold", &"x",
	], _sources(), 1, 20, false)
	_expect(result.accepted, "a valid board snapshot is accepted", failures)
	_expect(result.outcome_type == &"none" and result.rewards.is_empty(), "other completed lines are ignored when the middle judgment line fails", failures)
	var x_result: Variant = service.resolve_board_snapshot([
		&"x", &"x", &"x",
		&"x", &"x", &"x",
		&"x", &"x", &"x",
	], _sources(), 2, 20, false)
	_expect(x_result.outcome_type == &"none", "X never produces a reward", failures)


func _test_grade_mapping(roulette_script: GDScript, failures: PackedStringArray) -> void:
	var service: Variant = roulette_script.new(null, null, _manifest(), &"lumern")
	var common: Variant = service.resolve_board_snapshot([
		&"x", &"gold", &"x",
		&"warrior", &"warrior", &"warrior",
		&"gold", &"x", &"gold",
	], _sources(), 3, 20, false)
	_expect(common.completed_line_count == 1 and common.rank_id == &"common" and common.rewards.size() == 1, "one matching line produces one common reward", failures)
	var elite: Variant = service.resolve_board_snapshot([
		&"warrior", &"warrior", &"warrior",
		&"warrior", &"warrior", &"warrior",
		&"x", &"gold", &"x",
	], _sources(), 4, 20, false)
	_expect(elite.completed_line_count == 2 and elite.rank_id == &"elite", "two matching lines produce elite", failures)
	var hero: Variant = service.resolve_board_snapshot([
		&"warrior", &"warrior", &"x",
		&"warrior", &"warrior", &"warrior",
		&"warrior", &"warrior", &"x",
	], _sources(), 5, 20, false)
	_expect(hero.completed_line_count == 3 and hero.rank_id == &"hero", "three matching lines produce hero", failures)
	_expect(hero.template_resolution == &"source_archetype_rank_fallback", "unresolved fixed upper-grade templates use an explicit provisional fallback", failures)


func _test_gold_payout(roulette_script: GDScript, failures: PackedStringArray) -> void:
	var service: Variant = roulette_script.new(null, null, _manifest(), &"lumern")
	var one_line: Variant = service.resolve_board_snapshot([
		&"x", &"warrior", &"x",
		&"gold", &"gold", &"gold",
		&"x", &"warrior", &"x",
	], _sources(), 6, 20, false)
	_expect(one_line.gold_reward == 15, "one gold line pays 75 percent of the paid spin cost", failures)
	var two_lines: Variant = service.resolve_board_snapshot([
		&"gold", &"gold", &"gold",
		&"gold", &"gold", &"gold",
		&"x", &"warrior", &"x",
	], _sources(), 7, 20, false)
	_expect(two_lines.gold_reward == 40, "two gold lines pay 200 percent", failures)
	var three_lines: Variant = service.resolve_board_snapshot([
		&"gold", &"gold", &"x",
		&"gold", &"gold", &"gold",
		&"gold", &"gold", &"x",
	], _sources(), 8, 20, false)
	_expect(three_lines.gold_reward == 100, "three or more gold lines pay 500 percent", failures)


func _test_legendary_limit(roulette_script: GDScript, failures: PackedStringArray) -> void:
	var service: Variant = roulette_script.new(null, null, _manifest(), &"lumern")
	var board := [
		&"warrior", &"warrior", &"warrior",
		&"warrior", &"warrior", &"warrior",
		&"warrior", &"warrior", &"warrior",
	]
	var first: Variant = service.resolve_board_snapshot(board, _sources(), 9, 20, true)
	_expect(first.completed_line_count == 8 and first.rank_id == &"legendary" and first.rewards.size() == 1, "the first all-nine board produces one legendary", failures)
	var repeat: Variant = service.resolve_board_snapshot(board, _sources(), 10, 20, true)
	_expect(repeat.rank_id == &"hero" and repeat.rewards.size() == 2 and repeat.legendary_converted_to_heroes, "later all-nine boards convert to two heroes", failures)


func _sources() -> Array[Dictionary]:
	return [{
		"symbol_id": &"warrior",
		"reward_archetype_id": &"shield_guard",
		"board_weight": 3,
		"source_tier_id": &"tier_1",
		"source_weight": 1,
		"source_building_id": &"home:rear",
	}]


func _manifest() -> StageManifest:
	var manifest := StageManifest.new()
	manifest.stage_id = "roulette_contract"
	manifest.seed = 20260722
	manifest.starting_gold = 160
	manifest.starting_food_cap = 12
	return manifest


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Approved roulette contract checks passed")
		quit(0)
	else:
		printerr("Approved roulette contract failures:\n%s" % "\n".join(failures))
		quit(1)
''',
)

write(
    "tests/headless/economy_roulette_test.gd",
    '''extends SceneTree

const StageManifest = preload("res://scripts/core/stage_manifest.gd")
const OutpostState = preload("res://scripts/battle/outpost_state.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")


func _init() -> void:
	var failures := PackedStringArray()
	var economy_script := load("res://scripts/core/stage_economy.gd")
	var building_service_script := load("res://scripts/buildings/building_service.gd")
	var roulette_script := load("res://scripts/roulette/roulette_service.gd")
	var deployment_script := load("res://scripts/units/deployment_service.gd")
	_expect(economy_script != null, "stage economy service exists", failures)
	_expect(building_service_script != null, "building service exists", failures)
	_expect(roulette_script != null, "roulette service exists", failures)
	_expect(deployment_script != null, "deployment service exists", failures)
	if economy_script != null:
		_test_stage_economy(economy_script, failures)
	if economy_script != null and building_service_script != null:
		_test_building_ownership_and_capture_lock(economy_script, building_service_script, failures)
		_test_stabilized_capture_allows_rebuilding(economy_script, building_service_script, failures)
	if economy_script != null and building_service_script != null and roulette_script != null:
		_test_deterministic_approved_roulette(economy_script, building_service_script, roulette_script, failures)
	if economy_script != null and deployment_script != null:
		_test_deployment_food_limit(economy_script, deployment_script, failures)
	_finish(failures)


func _test_stage_economy(economy_script: GDScript, failures: PackedStringArray) -> void:
	var economy: Variant = economy_script.new(_manifest())
	_expect(economy.gold == 160, "regular stage starts at 160 gold", failures)
	_expect(economy.food_cap == 12, "regular stage starts with 12 food", failures)
	economy.advance(60.0, 1, 1)
	_expect(economy.gold == 183, "active combat grants base, controlled clash, and stable outpost income on their exact intervals", failures)


func _test_building_ownership_and_capture_lock(economy_script: GDScript, building_service_script: GDScript, failures: PackedStringArray) -> void:
	var economy: Variant = economy_script.new(_manifest())
	var buildings: Variant = building_service_script.new(economy, _manifest())
	var enemy_outpost := OutpostState.new(&"veil")
	var player_outpost := OutpostState.new(&"lumern")
	buildings.register_outpost(&"enemy_top", enemy_outpost, [&"front_a"])
	buildings.register_outpost(&"player_top", player_outpost, [&"front_a", &"front_b"])
	_expect(not buildings.try_construct(&"enemy_top", &"front_a", &"tower"), "enemy-owned node rejects player building", failures)
	_expect(buildings.try_construct(&"player_top", &"front_a", &"tower"), "owned stabilized outpost accepts a tower", failures)
	player_outpost.begin_capture(&"veil", 1.0)
	_expect(not buildings.try_construct(&"player_top", &"front_b", &"farm"), "capture locks construction nodes", failures)


func _test_stabilized_capture_allows_rebuilding(economy_script: GDScript, building_service_script: GDScript, failures: PackedStringArray) -> void:
	var economy: Variant = economy_script.new(_manifest())
	var buildings: Variant = building_service_script.new(economy, _manifest())
	var outpost := OutpostState.new(&"veil", true)
	buildings.register_outpost(&"captured_top", outpost, [&"front_a"])
	outpost.begin_capture(&"lumern", 1.0)
	outpost.advance(20.0)
	outpost.advance(5.0)
	_expect(buildings.try_construct(&"captured_top", &"front_a", &"farm"), "a captured outpost accepts new construction after stabilization", failures)


func _test_deterministic_approved_roulette(economy_script: GDScript, building_service_script: GDScript, roulette_script: GDScript, failures: PackedStringArray) -> void:
	var first_manifest := _manifest()
	var first_economy: Variant = economy_script.new(first_manifest)
	var first_buildings: Variant = building_service_script.new(first_economy, first_manifest)
	var outpost := OutpostState.new(&"lumern")
	first_buildings.register_outpost(&"player_top", outpost, [&"front_a", &"front_b", &"rear"])
	_expect(first_buildings.try_construct(&"player_top", &"front_a", &"tower"), "tower construction succeeds", failures)
	_expect(first_buildings.try_construct(&"player_top", &"front_b", &"farm"), "farm construction succeeds", failures)
	_expect(first_buildings.roulette_token_sources().is_empty(), "tower and farm do not create unit roulette tokens", failures)
	_expect(first_buildings.try_construct(&"player_top", &"rear", &"barracks"), "barracks construction succeeds", failures)
	_expect(first_buildings.roulette_token_sources().size() == 1, "one completed barracks contributes one source token entry", failures)
	var first_roulette: Variant = roulette_script.new(first_economy, first_buildings, first_manifest, &"lumern")
	var first_result: Variant = first_roulette.spin({"seed": 12})
	_expect(first_result.accepted and first_result.board.size() == 9, "a paid spin resolves one deterministic 3x3 board result", failures)
	_expect(first_economy.gold >= 30, "construction and roulette charge approved costs before any possible gold payout", failures)
	var second_manifest := _manifest()
	var second_economy: Variant = economy_script.new(second_manifest)
	var second_buildings: Variant = building_service_script.new(second_economy, second_manifest)
	var second_outpost := OutpostState.new(&"lumern")
	second_buildings.register_outpost(&"player_top", second_outpost, [&"front_a", &"front_b", &"rear"])
	second_buildings.try_construct(&"player_top", &"front_a", &"tower")
	second_buildings.try_construct(&"player_top", &"front_b", &"farm")
	second_buildings.try_construct(&"player_top", &"rear", &"barracks")
	var second_roulette: Variant = roulette_script.new(second_economy, second_buildings, second_manifest, &"lumern")
	var second_result: Variant = second_roulette.spin({"seed": 12})
	_expect(JSON.stringify(first_result.to_dictionary()) == JSON.stringify(second_result.to_dictionary()), "identical seed and building snapshot reproduce the same roulette result", failures)
	_expect(first_manifest.input_log.size() == 4, "three constructions and the roulette result are recorded", failures)


func _test_deployment_food_limit(economy_script: GDScript, deployment_script: GDScript, failures: PackedStringArray) -> void:
	var manifest := _manifest()
	var economy: Variant = economy_script.new(manifest)
	var deployment: Variant = deployment_script.new(economy, manifest)
	var card := UnitSpawnDefinition.new()
	card.archetype_id = &"shield_guard"
	card.owner_team_id = &"lumern"
	card.visual_faction_id = &"lumern"
	card.food_cost = 12
	_expect(deployment.deploy(card, &"top", 10.0), "deployment reserves available food", failures)
	_expect(not deployment.deploy(card, &"top", 20.0), "deployment rejects cards that exceed the food cap", failures)
	_expect(economy.food_used == 12, "rejected deployment does not spend additional food", failures)
	_expect(manifest.input_log.size() == 1, "only accepted deployment commands are recorded", failures)


func _manifest() -> StageManifest:
	var manifest := StageManifest.new()
	manifest.stage_id = "regular_stage"
	manifest.seed = 101
	manifest.starting_gold = 160
	manifest.starting_food_cap = 12
	return manifest


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Economy, construction, approved roulette, and deployment checks passed")
		quit(0)
	else:
		printerr("Economy, construction, roulette, and deployment failures:\n%s" % "\n".join(failures))
		quit(1)
''',
)

replace_once(
    "tests/headless/stage_run_test.gd",
    "\tif bypass_script != null:\n\t\t_test_assassin_bypass_timing(bypass_script, failures)",
    "\tif stage_run_script != null and progression_script != null:\n\t\t_test_roulette_storage_and_deployment(stage_run_script, progression_script, failures)\n\tif bypass_script != null:\n\t\t_test_assassin_bypass_timing(bypass_script, failures)",
)
replace_once(
    "tests/headless/stage_run_test.gd",
    "func _test_assassin_bypass_timing(bypass_script: GDScript, failures: PackedStringArray) -> void:",
    '''func _test_roulette_storage_and_deployment(stage_run_script: GDScript, progression_script: GDScript, failures: PackedStringArray) -> void:
	var tutorial: Resource = ResourceLoader.load(TUTORIAL_STAGE_PATH)
	var run: Variant = stage_run_script.new(progression_script.new())
	run.start(tutorial, 2002)
	_expect(run.construct_home(&"barracks"), "the stage can build the approved basic barracks", failures)
	var result: Variant = run.roulette.resolve_board_snapshot([
		&"x", &"gold", &"x",
		&"warrior", &"warrior", &"warrior",
		&"gold", &"x", &"gold",
	], run.buildings.roulette_token_sources(), 17, 20, false)
	_expect(run.store_roulette_result(result), "a unit roulette result enters stage-owned storage", failures)
	_expect(run.pending_roulette_rewards.size() == 1, "one unit reward remains pending without consuming food", failures)
	var blocked: Variant = run.spin_roulette({"seed": 1})
	_expect(not blocked.accepted and blocked.failure_reason == &"pending_reward", "pending storage blocks only the next roulette spin", failures)
	_expect(run.deploy_next_roulette_reward(&"top"), "the stored reward can be committed to one lane", failures)
	_expect(run.pending_roulette_rewards.is_empty(), "successful deployment clears the stored reward", failures)


func _test_assassin_bypass_timing(bypass_script: GDScript, failures: PackedStringArray) -> void:''',
)

write(
    "tools/validate_c1_roulette.py",
    '''#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "scripts/data/roulette_spin_result.gd",
    "scripts/roulette/roulette_service.gd",
    "scripts/buildings/building_service.gd",
    "tests/headless/roulette_contract_test.gd",
    "docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md",
)
FORBIDDEN_ACTIVE_REFERENCES = (
    "docs/work_orders/0001-phase-0-codex-plan-mode.md",
    "work_orders/0001-phase-0-codex-plan-mode.md",
    "docs/work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md",
    "work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md",
    "docs/design/proposals/0001-phase-0-godot-bootstrap.md",
    "design/proposals/0001-phase-0-godot-bootstrap.md",
    "docs/goals/0001-engine-selection-and-bootstrap.md",
    "goals/0001-engine-selection-and-bootstrap.md",
    "docs/goals/0002-core-vertical-slice.md",
    "goals/0002-core-vertical-slice.md",
)
EXCLUDED_DOC_PARTS = {"archive", "work_orders", "proposals", "issues", "goals"}


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def active_markdown_files(root: pathlib.Path = ROOT) -> list[pathlib.Path]:
    result: list[pathlib.Path] = []
    for path in (root / "docs").rglob("*.md"):
        relative_parts = path.relative_to(root / "docs").parts
        if any(part in EXCLUDED_DOC_PARTS for part in relative_parts):
            continue
        result.append(path)
    result.append(root / "README.md")
    result.append(root / "AGENTS.md")
    return sorted(set(result))


def validate(root: pathlib.Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing C1 file: {relative}")
    if errors:
        return errors

    roulette = (root / "scripts/roulette/roulette_service.gd").read_text(encoding="utf-8")
    buildings = (root / "scripts/buildings/building_service.gd").read_text(encoding="utf-8")
    stage_run = (root / "scripts/core/stage_run.gd").read_text(encoding="utf-8")
    economy_test = (root / "tests/headless/economy_roulette_test.gd").read_text(encoding="utf-8")
    contract_test = (root / "tests/headless/roulette_contract_test.gd").read_text(encoding="utf-8")

    roulette_terms = (
        "LINE_INDEXES",
        "resolve_board_snapshot",
        "_completed_line_count",
        "_rank_for_lines",
        "legendary_generated",
        "_gold_reward",
        "source_archetype_rank_fallback",
    )
    for term in roulette_terms:
        if term not in roulette:
            errors.append(f"roulette service missing contract term: {term}")
    if "return cards" in roulette or "Array[UnitSpawnDefinition]" in re.search(r"func spin.*", roulette).group(0):
        errors.append("roulette service still exposes the direct nine-card placeholder API")
    if "roulette_archetype_ids" in buildings or "roulette_archetype_ids" in economy_test:
        errors.append("legacy roulette_archetype_ids consumer remains")
    if "first_result.size() == 9" in economy_test:
        errors.append("placeholder nine-card assertion remains")
    if '&"barracks"' not in buildings or '&"warrior"' not in buildings:
        errors.append("approved barracks warrior token source is missing")
    if 'pending_roulette_rewards' not in stage_run or 'pending_reward' not in stage_run:
        errors.append("stage-owned reward storage contract is missing")
    for phrase in (
        "middle judgment line fails",
        "one matching line produces one common reward",
        "two matching lines produce elite",
        "three matching lines produce hero",
        "first all-nine board produces one legendary",
        "later all-nine boards convert to two heroes",
    ):
        if phrase not in contract_test:
            errors.append(f"roulette regression test missing: {phrase}")

    for path in active_markdown_files(root):
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root).as_posix()
        for forbidden in FORBIDDEN_ACTIVE_REFERENCES:
            if forbidden in text:
                errors.append(f"active document references retired execution input: {relative} -> {forbidden}")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            clean = target.split("#", 1)[0].strip()
            if not clean or "://" in clean or clean.startswith(("#", "mailto:")):
                continue
            resolved = (path.parent / clean).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                continue
            if not resolved.exists():
                errors.append(f"broken active Markdown link: {relative} -> {clean}")

    for path in root.rglob("*"):
        if path.is_file() and path.name.startswith("_C1_"):
            errors.append(f"temporary C1 audit file remains: {path.relative_to(root).as_posix()}")
    for path in root.rglob("*"):
        if path.is_file() and ("_apply_c1_" in path.name or "-once" in path.name and "c1" in path.name.lower()):
            errors.append(f"temporary C1 bootstrap remains: {path.relative_to(root).as_posix()}")

    gdd = (root / "docs/OMENWARD_GAME_DESIGN.md").read_text(encoding="utf-8")
    if "문서 버전: **v0.21**" not in gdd:
        errors.append("GDD was not advanced to v0.21")
    for stale in ("### 구현 전 미확정", "Issue #1 Phase 0 Codex Plan Mode", "현재 실제 Godot 코드, Scene, Resource, 테스트는 생성·수정하지 않는다"):
        if stale in gdd:
            errors.append(f"GDD retains stale implementation state: {stale}")
    baseline = (root / "docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md").read_text(encoding="utf-8")
    if "Phase 0 Plan Mode 대기 / 구현 전" in baseline:
        errors.append("active preproduction baseline still claims implementation has not started")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("C1 roulette validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("C1 roulette validation PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
''',
)

write(
    "tests/python/test_c1_roulette_contract.py",
    '''from __future__ import annotations

import pathlib
import shutil
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from validate_c1_roulette import REQUIRED_FILES, validate  # noqa: E402


class C1RouletteValidationTests(unittest.TestCase):
    def _copy_contract_files(self, destination: pathlib.Path) -> None:
        for relative in REQUIRED_FILES:
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        for relative in (
            "scripts/core/stage_run.gd",
            "tests/headless/economy_roulette_test.gd",
            "docs/OMENWARD_GAME_DESIGN.md",
            "docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md",
            "README.md",
            "AGENTS.md",
        ):
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    def test_current_tree_passes(self) -> None:
        self.assertEqual(validate(ROOT), [])

    def test_direct_nine_card_placeholder_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            roulette = root / "scripts" / "roulette" / "roulette_service.gd"
            roulette.write_text(roulette.read_text(encoding="utf-8") + "\n# return cards\n", encoding="utf-8")
            self.assertTrue(any("nine-card placeholder" in error for error in validate(root)))

    def test_retired_work_order_reference_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            readme = root / "README.md"
            readme.write_text(readme.read_text(encoding="utf-8") + "\n`docs/work_orders/0001-phase-0-codex-plan-mode.md`\n", encoding="utf-8")
            self.assertTrue(any("retired execution input" in error for error in validate(root)))

    def test_missing_judgment_line_regression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            test_file = root / "tests" / "headless" / "roulette_contract_test.gd"
            test_file.write_text(test_file.read_text(encoding="utf-8").replace("middle judgment line fails", "middle line omitted"), encoding="utf-8")
            self.assertTrue(any("middle judgment line fails" in error for error in validate(root)))


if __name__ == "__main__":
    unittest.main()
''',
)

# Canonical roulette documentation and permanent recovery report.
replace_once(
    "docs/design/APPROVED_ROULETTE_CORE_RULES.md",
    "- 상태: **핵심 구조·등급 생성·병영 출처 추첨 승인됨 / 세부 확률 일부 미확정**",
    "- 상태: **핵심 구조 승인 / C1 중앙 판정·완성선·등급·보상·보관 구현 후보 / 유틸리티 세부 일부 미확정**",
)
replace_once(
    "docs/design/APPROVED_ROULETTE_CORE_RULES.md",
    "## 17. 미확정 세부",
    '''## 17. C1 구현 경계

C1은 다음 인과를 구현한다.

```text
중앙 가로줄 확정
→ 비-X 동일 심벌 3개 선행 조건
→ 전체 8개 줄 중 판정 심벌 완성선 계산
→ 일반·엘리트·영웅·전설 등급
→ 훈련 출처 선택
→ 실제 보상 생성
→ StageRun 소유 보관함
→ 한 라인 배치
```

- X 6, 금화 2, 활성 기본 병영 토큰 3의 릴 가중치를 사용한다.
- 기본 병영은 전사 토큰과 현재 공용 아키타입 `shield_guard`를 첫 일반 보상 fallback으로 제공한다.
- 농장·포탑은 유닛 룰렛 토큰을 제공하지 않는다.
- 고정 상위 등급 템플릿 ID가 확정되기 전에는 선택 출처 아키타입에 Rank를 적용하는 `source_archetype_rank_fallback`을 명시적으로 기록한다.
- 이동권 심벌의 완성선 보상량과 럭키의 이동·한 칸 교체 상충은 임의 구현하지 않고 `DECISIONS_PENDING.md`에서 분리한다.

## 18. 미확정 세부''',
)
replace_once(
    "docs/design/APPROVED_ROULETTE_CORE_RULES.md",
    "Godot 구현은 별도 Codex Plan Mode 제안서와 사용자 승인을 거쳐야 한다.",
    "Godot 변경은 최신 Roadmap의 C1 범위와 별도 PR 검증을 따른다. 과거 Phase 0 작업 입력은 현재 구현 근거로 사용하지 않는다.",
)
replace_once(
    "docs/design/APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md",
    "- 상태: **확률 구조·목표 분포 승인 / 릴 가중치는 첫 시뮬레이션 가설**",
    "- 상태: **확률 구조·목표 분포 승인 / C1 기본 릴 가중치 구현 후보 / 100,000시드 검증·이동권 보상·럭키 해석 대기**",
)
replace_once(
    "docs/design/APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md",
    "## 9. 시뮬레이션 검증",
    '''## 9. C1 유틸리티 보류 경계

- 이동권의 릴 가중치 1은 승인돼 있으나 이동권 심벌 완성선의 지급량은 명시되지 않았다.
- 룰렛 핵심 규칙은 자연 럭키를 무료 이동 1회로, 이 문서는 실패 보드를 한 칸 교체해 최소 일반 1줄로 만드는 것으로 설명한다.
- 두 항목은 다음 C1 유틸리티 결정에서 하나의 정본으로 통합하기 전까지 런타임 생성 풀에서 제외한다.
- 제외는 승인 취소가 아니라 상충 규칙을 임의 구현하지 않기 위한 가역적 경계다.

## 10. 시뮬레이션 검증''',
)

write(
    "docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md",
    '''# C1 승인 룰렛 계약 복구 보고서

- 기준 main: `ef9e66e3bc5be7711c36123e6c6d7fe8ec8dc9a2`
- 작업 상태: `IMPLEMENTED_CANDIDATE / REMOTE_VALIDATION_PENDING`
- 프로젝트 코어: `CORE_CONFIRMED / CORE_LOCKED`

## 1. 적용 Skill

- `foundation.project-intake` — 범위·보호 대상·검증·롤백 계약.
- `foundation.project-core` — 예측→확률 설계→전선 커밋 인과 보호.
- `foundation.pruning` — 구형 Work Order·Goal·Proposal의 활성 참조 차단과 Git 이력 보존.
- `discipline.game-design` — 중앙 판정·완성선·등급·보상 C1 경계.
- `discipline.engineering` — Godot 상태 소유·결정론·최소 데이터 변경.
- `discipline.qa` — 정상·실패·경계·결정론·저장·배치 테스트.
- `foundation.adversarial-review` — 9카드 placeholder·구형 참조·문서 상충 공격.
- `foundation.validation-review`, `discipline.integration-review` — 실제 diff·CI·정본 동기화.

## 2. 감사

기계 감사 입력에서 텍스트 242개, 룰렛 관련 105개, 구형 상태·명칭 후보 39개와 내부 Markdown 참조를 조사했다. 깨진 내부 링크는 수집 시점 0개였다.

확인된 핵심 결함:

1. 룰렛 서비스가 보드 9칸을 곧바로 9개 유닛 카드로 반환했다.
2. placeholder 테스트가 잘못된 API를 회귀 계약으로 고정했다.
3. 농장·포탑이 유닛 토큰을 만들고 기본 병영이 없었다.
4. 보상 저장이 HUD 로컬 배열에 있어 StageRun 책임이 아니었다.
5. GDD·통합 인덱스·문서 라우터가 Phase 0 이전 파일과 상태를 활성 기준으로 노출했다.

## 3. C1 구현

```text
3×3 결정론적 보드
→ 중앙 가로줄 선행 판정
→ 같은 판정 심벌의 8개 완성선 계산
→ common / elite / hero / legendary
→ 출처 병영 결정
→ 1개 유닛 보상 또는 금화 지급
→ StageRun 보관
→ 라인 배치
```

- X·금화·기본 병영 전사 토큰 가중치 적용.
- 금화 75%/200%/500% 지급.
- 전설 스테이지 1회와 이후 영웅 2기 변환.
- 농장·포탑의 유닛 토큰 제거.
- 병영 40금화·전사 토큰 추가.
- 결과 보관 중 다음 회전만 차단.
- 같은 시드·건물 스냅샷 재현 로그.

## 4. 의도적으로 보류

- 이동권 심벌의 완성선 지급량.
- 상충하는 럭키 규칙의 최종 해석.
- 계열별 고정 엘리트·영웅·전설 템플릿 ID.
- 100,000시드 확률·경제 분포 판정.

상위 등급 템플릿은 현재 공용 데이터에 확정 ID가 없어 `source_archetype_rank_fallback`으로 명시한다. 이는 숨은 최종 결정이 아니다.

## 5. 구형 참조 처리

- 과거 Work Order·Goal·Proposal은 활성 읽기·라우팅에서 제거한다.
- 고유 역사와 승인 근거는 Git 이력에 보존한다.
- 공식 명칭 교체표와 금지 예시는 구형 명칭을 설명하는 정본이므로 유지한다.
- mutation fixture의 구형 문자열은 Validator 공격 입력이므로 유지한다.

## 6. 검증 경계

영구 CI가 다음을 실행한다.

- Ubuntu/Windows × Python 3.12/3.13 정적 계약.
- Godot 4.7.1 editor import.
- 모든 `tests/headless/*_test.gd`.
- runtime smoke.
- 프로젝트 코어·Skill Validator와 whitespace.

사람 플레이·시각 QA·100,000시드 분포는 이번 자동 C1 계약과 별도다.
''',
)

# GDD and active state documents.
replace_once("docs/OMENWARD_GAME_DESIGN.md", "- 문서 버전: **v0.20**", "- 문서 버전: **v0.21**")
replace_once(
    "docs/OMENWARD_GAME_DESIGN.md",
    "- 3×3 보드.\n- 중앙 가로줄 기본 판정.\n- 같은 비-X 심벌 3개가 완성된 줄만 보상.",
    "- 3×3 결정론적 보드.\n- 중앙 가로줄의 동일 비-X 심벌 3개가 보상 판정의 선행 조건.\n- 선행 조건이 성립한 심벌만 전체 가로·세로·대각선 8개 완성선을 계산.\n- 결과는 보드 9칸이 아니라 최종 보상 1개를 기본으로 생성.",
)
replace_once(
    "docs/OMENWARD_GAME_DESIGN.md",
    "- 금화 장기 평균 지급 목표는 회전비의 30% 이하.",
    "- 금화 장기 평균 지급 목표는 회전비의 30% 이하.\n- 기본 병영은 전사 토큰을 제공하고 농장·포탑은 유닛 토큰을 제공하지 않는다.\n- 생성 유닛은 StageRun 보관함에 들어가며 보관 중에는 다음 룰렛 회전만 차단한다.\n- 이동권 보상량·럭키 최종 해석·고정 상위 등급 템플릿은 미확정 경계를 유지한다.",
)
replace_regex(
    "docs/OMENWARD_GAME_DESIGN.md",
    r"### 구현 전 미확정\n.*?(?=---\n\n## 23\.)",
    '''### 현재 구현·검증 경계

구현됨:

- Godot 4.7.1 Standard·Compatibility renderer.
- 960×540 논리 화면·1920×1080 출력·viewport stretch·keep aspect·integer scale.
- 실제 Scene·Script·Resource·Test 경로와 headless 테스트 러너.
- typed Resource·StageManifest·input log 데이터 경계.

미검증·미확정:

- C1 룰렛 영구 CI와 runtime smoke.
- 이동권 완성선 보상량과 럭키 규칙 통합.
- 100,000시드 확률·경제 시뮬레이션.
- 사람 플레이·1080p·720p 가독성.

''',
)
replace_regex(
    "docs/OMENWARD_GAME_DESIGN.md",
    r"## 23\. 구현 순서와 승인 게이트\n.*?(?=---\n\n## 24\.)",
    '''## 23. 구현 순서와 승인 게이트

```text
C0 프로젝트 코어·정본 복구 완료
→ [현재] C1 중앙 판정·완성선·등급·보상·보관 계약
→ C1 유틸리티 규칙 통합과 100,000시드 검증
→ C2 전투 목적 루프
→ C3 코어 UX
→ C4 사람 플레이
→ 밸런스·콘텐츠·아트 확장
```

각 단계는 최신 `PROJECT_CORE.md`, `CURRENT_IMPLEMENTATION_STATUS.md`, 관련 APPROVED 정본과 별도 PR 검증을 따른다. 과거 Phase 0 Work Order·Goal·Proposal은 구현 근거로 참조하지 않는다.

''',
)
replace_regex(
    "docs/OMENWARD_GAME_DESIGN.md",
    r"## 25\. 주요 책임 문서\n.*\Z",
    '''## 25. 주요 책임 문서

- 프로젝트 코어: `docs/PROJECT_CORE.md`
- 현재 구현 증거: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- 인수인계: `docs/HANDOFF_CONTEXT.md`
- 문서 라우팅: `docs/DOCUMENTATION_MAP.md`
- 통합 기준: `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`
- 룰렛 핵심: `docs/design/APPROVED_ROULETTE_CORE_RULES.md`
- 룰렛 확률: `docs/design/APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md`
- C1 복구 보고: `docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md`
- 전장: `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`
- 공용 병종 데이터·진영 이미지: `docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`
- W1~20 웨이브: `docs/design/APPROVED_SHARED_ARCHETYPE_WAVE_1_20_POC_V1.md`
- 성능·데이터·테스트: `docs/design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md`
- 개발 순서: `docs/OMENWARD_ROADMAP.md`
- 미확정: `docs/DECISIONS_PENDING.md`
''',
)

replace_once("README.md", "[현재] 정본·프로젝트 코어 복구\n→ 승인 룰렛 계약 복구", "정본·프로젝트 코어 확정·잠금 완료\n→ [현재] 승인 룰렛 핵심 계약 복구")
replace_once(
    "README.md",
    "세부 근거와 다음 게이트는 [`docs/CURRENT_IMPLEMENTATION_STATUS.md`](docs/CURRENT_IMPLEMENTATION_STATUS.md)를 따른다. 자동 검증 명령과 수동 QA 항목은 [`docs/VERTICAL_SLICE_VALIDATION.md`](docs/VERTICAL_SLICE_VALIDATION.md)와 [`docs/PHASE_0_VALIDATION.md`](docs/PHASE_0_VALIDATION.md)에 남아 있으며, 실제 재실행 전에는 완료로 보고하지 않는다.",
    "세부 근거와 다음 게이트는 [`docs/CURRENT_IMPLEMENTATION_STATUS.md`](docs/CURRENT_IMPLEMENTATION_STATUS.md)를 따른다. C1 변경과 증거 경계는 [`docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md`](docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md), 자동·수동 검증은 [`docs/VERTICAL_SLICE_VALIDATION.md`](docs/VERTICAL_SLICE_VALIDATION.md)를 따른다.",
)
replace_once("docs/ACTIVE_CONTEXT.md", "- 다음 게임 기능 변경은 승인 룰렛 계약 복구로 한정한다.", "- 현재 게임 기능 변경은 승인 룰렛 중앙 판정·완성선·등급·보상·보관 계약으로 한정한다.")
replace_once("docs/ACTIVE_CONTEXT.md", "정본·프로젝트 코어 복구\n→ 승인 룰렛 계약 복구", "정본·프로젝트 코어 확정·잠금 완료\n→ [현재] 승인 룰렛 핵심 계약 복구")
replace_once("docs/ACTIVE_CONTEXT.md", "- 다음 게임 기능 PR은 승인 룰렛 계약 복구만 포함한다.", "- 현재 C1 PR은 룰렛 핵심 계약과 구형 활성 참조 정리만 포함한다. 이동권·럭키·고정 상위 템플릿은 별도 결정 전 확정하지 않는다.")
replace_once("docs/HANDOFF_CONTEXT.md", "- 현재 상태: **기술 기준선 구현 / 핵심 수직 슬라이스 부분 구현 / 코어 루프·사람 플레이 미검증**", "- 현재 상태: **CORE_LOCKED / C1 승인 룰렛 핵심 계약 구현·원격 검증 진행 / 전투 목적 루프·사람 플레이 미검증**")
replace_once("docs/HANDOFF_CONTEXT.md", "2. 저장소에는 Phase 0 기술 기준선과 수직 슬라이스 구성요소가 존재하지만 승인 룰렛·전투 목적·코어 UX는 미완결이다.", "2. 저장소에는 기술 기준선과 수직 슬라이스 구성요소가 있으며, C1 룰렛 핵심 계약을 복구 중이다. 전투 목적·코어 UX는 아직 미완결이다.")

replace_regex(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    r"### 3\.1 룰렛 — `DIVERGENT`\n.*?(?=### 3\.2)",
    '''### 3.1 룰렛 — `C1_IMPLEMENTED_CANDIDATE`

구현 후보:

```text
3×3 결정론적 보드
→ 중앙 가로줄 동일 비-X 선행 판정
→ 전체 8개 완성선
→ common / elite / hero / legendary
→ 출처 선택
→ 유닛 1개 또는 금화
→ StageRun 보관·라인 배치
```

- 기존 9개 직접 카드 API와 placeholder 테스트를 제거했다.
- 기본 병영 전사 토큰을 추가하고 농장·포탑의 유닛 토큰을 제거했다.
- 전설 1회 제한과 이후 영웅 2기 변환, 금화 75%/200%/500%를 구현했다.
- 고정 상위 등급 템플릿은 미확정이므로 `source_archetype_rank_fallback`을 명시한다.
- 이동권 지급량과 상충하는 럭키 규칙은 런타임 생성 풀에서 가역적으로 보류한다.

판정: `IMPLEMENTED_CANDIDATE / REMOTE_VALIDATION_PENDING`.

''',
)
replace_once("docs/CURRENT_IMPLEMENTATION_STATUS.md", "1. 승인 룰렛 계약 복구\n2. 전투 → 거점·성문·승패 목적 루프 연결", "1. C1 룰렛 핵심 계약 원격 검증\n2. C1 이동권·럭키 규칙 통합과 100,000시드 시뮬레이션\n3. 전투 → 거점·성문·승패 목적 루프 연결")

replace_once("docs/OMENWARD_ROADMAP.md", "- 현재 상태: **C0 정본·프로젝트 코어 확정·잠금 완료 / C1 승인 룰렛 계약 복구 착수**", "- 현재 상태: **C0 완료 / C1 승인 룰렛 핵심 계약 구현·원격 검증 진행**")
replace_once("docs/OMENWARD_ROADMAP.md", "→ [현재] 승인 룰렛 계약 복구\n→ 전투 목적 루프 연결", "→ [현재] 승인 룰렛 핵심 계약 복구\n→ C1 이동권·럭키 규칙 통합·100,000시드 검증\n→ 전투 목적 루프 연결")
replace_once("docs/OMENWARD_ROADMAP.md", "| C1 룰렛 계약 복구 | 중앙 판정 줄·완성선·등급·단일 보상 | **현재** | 승인 계약 테스트 PASS |", "| C1 룰렛 핵심 계약 | 중앙 판정 줄·완성선·등급·보상·보관 | **구현·원격 검증 진행** | Godot 계약 테스트 PASS |\n| C1U 룰렛 유틸리티 | 이동권·럭키 정본 통합·100,000시드 | 미시작 | 사용자 결정·분포 기준 |")
for old, new in (
    ("`docs/work_orders/0001-phase-0-codex-plan-mode.md`", "Git 이력의 Phase 0 작업 입력"),
    ("Issue #1.", "과거 Phase 0 계획 게이트."),
    ("Goal 0001.", "과거 Phase 0 목표."),
    ("Issue #32.", "과거 수직 슬라이스 계획 게이트."),
    ("Goal 0002.", "과거 수직 슬라이스 목표."),
):
    text = read("docs/OMENWARD_ROADMAP.md")
    write("docs/OMENWARD_ROADMAP.md", text.replace(old, new))
replace_regex(
    "docs/OMENWARD_ROADMAP.md",
    r"## 15\. 지금 실행할 단 하나의 작업\n.*\Z",
    '''## 15. 지금 실행할 단 하나의 작업

```text
C1 승인 룰렛 핵심 계약 구현
→ Godot 4.7.1 전체 headless 회귀
→ 구형 활성 참조 0건 검증
→ Adversarial Review·Validation Review·Integration Review
→ 사용자 검토
```

전투 목적 루프·코어 UX·신규 콘텐츠는 같은 PR에 섞지 않는다. 이동권·럭키 상충은 C1U 결정으로 분리한다.
''',
)

replace_regex(
    "docs/DECISIONS_PENDING.md",
    r"### B\. 다음 기능 작업 — 승인 룰렛 계약 복구\n.*?(?=### C\.)",
    '''### B. C1 승인 룰렛 핵심 계약

- [x] 9개 직접 카드 placeholder를 중앙 판정·완성선·등급·최종 보상 계약으로 교체.
- [x] X·금화·기본 병영 전사 토큰과 결정론적 보드 적용.
- [x] 전설 1회 제한과 이후 영웅 2기 변환.
- [x] StageRun 결과 보관과 라인 배치.
- [ ] Godot 4.7.1 원격 전체 회귀.

### B.1 C1U 별도 결정

- [ ] 이동권 심벌 완성선의 정확한 지급량.
- [ ] 자연 럭키를 무료 이동 1회로 볼지, 실패 보드 한 칸 교체로 볼지 정본 통합.
- [ ] 계열별 고정 엘리트·영웅·전설 템플릿 ID.
- [ ] 결과 보관함 3칸과 “유닛 보상은 사라지지 않음” 계약의 우선순위.
- [ ] 100,000시드 분포·금화 EV·첫 보상 시간 검증.

''',
)
replace_once("docs/DECISIONS_PENDING.md", "- 현재 작업: 정본·프로젝트 코어 복구 / 다음 기능 게이트: 승인 룰렛 계약 복구", "- 현재 작업: C1 승인 룰렛 핵심 계약 구현·원격 검증 / 다음 결정: C1U 이동권·럭키·분포")
replace_once("docs/DECISIONS_PENDING.md", "1. 프로젝트 코어 확정·잠금과 정본 복구 PR 병합\n2. 승인 룰렛 계약 복구 Plan\n3. 룰렛 계약 구현·자동 검증\n4. 전투 목적 루프 연결", "1. C1 승인 룰렛 핵심 계약 원격 검증\n2. C1U 이동권·럭키 정본 통합과 100,000시드 검증\n3. 전투 목적 루프 연결")

# Update active integration baseline and performance readiness in place.
replace_once("docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md", "- 상태: **프리프로덕션 구조 승인 완료 / 공용 10병종 데이터·진영 비주얼 분리 승인 / 전장·연출 초기값 승인 / Phase 0 Plan Mode 대기 / 구현 전**", "- 상태: **프리프로덕션 구조 승인 / 기술 기준선 구현 / C1 승인 룰렛 핵심 계약 구현·원격 검증 진행**")
replace_once("docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md", "- 최신 갱신일: 2026-07-16", "- 최신 갱신일: 2026-07-22")
replace_once("docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md", "- 룰렛: `docs/design/APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md`", "- 룰렛 핵심: `docs/design/APPROVED_ROULETTE_CORE_RULES.md`\n- 룰렛 확률: `docs/design/APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md`\n- C1 구현 증거: `docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md`")
replace_regex(
    "docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md",
    r"## 9\. 구현 전 남은 결정\n.*?(?=## 10\.)",
    '''## 9. 현재 기술·구현 경계

확인됨:

- Godot 4.7.1 Standard, Compatibility renderer.
- 960×540 논리 화면, 1920×1080 출력, viewport/keep/integer scale.
- 실제 Scene·Script·Resource·Test 경로.
- typed Resource·StageManifest·input log 경계.
- headless 테스트 명령과 GitHub Actions.

남은 결정·증거:

- C1 이동권·럭키 규칙 통합과 100,000시드 검증.
- 전투 목적 루프·코어 UX·사람 플레이.
- 최종 자산·VFX·오디오·성능 계측.

''',
)
replace_regex(
    "docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md",
    r"## 10\. 현재 실행 게이트\n.*?(?=\Z)",
    '''## 10. 현재 실행 게이트

```text
C0 프로젝트 코어·정본 복구 완료
→ [현재] C1 승인 룰렛 핵심 계약
→ C1U 이동권·럭키·분포
→ C2 전투 목적 루프
→ C3 코어 UX
→ C4 사람 플레이
```

- 현재 구현 근거는 `PROJECT_CORE.md`, `CURRENT_IMPLEMENTATION_STATUS.md`, 관련 APPROVED 문서와 실제 코드·테스트다.
- 과거 Work Order·Goal·Proposal은 활성 실행 입력으로 참조하지 않는다.
- 새로운 대형 시스템보다 잠긴 코어 인과의 구현·계측·검증을 우선한다.
''',
)
replace_regex(
    "docs/design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md",
    r"## 9\. Phase 0 Plan Mode 진입 조건\n.*?(?=## 11\.)",
    '''## 9. 현재 기술 기준선

확인된 구조:

1. Godot 4.7.1 프로젝트와 main Scene.
2. 공용 10병종·양 진영 Visual·AnimationContract.
3. 결정론·StageManifest·input log·DataRegistry.
4. 실제 Scene·Script·Resource·Test 경로.
5. headless 테스트와 CI.

## 10. 현재 C1 검증 조건

1. 중앙 판정 줄이 실패하면 다른 완성선을 무시한다.
2. 1/2/3~7/8줄 등급이 정확하다.
3. X는 보상하지 않고 금화는 75%/200%/500%를 지급한다.
4. 기본 병영만 유닛 토큰을 제공한다.
5. 같은 시드·건물 스냅샷·최종 보드가 같은 결과를 만든다.
6. 결과 보관 중 다음 회전만 차단하고 라인 배치가 가능하다.
7. 모든 기존 headless 테스트와 editor import가 통과한다.

''',
)

# Documentation map: remove task-specific legacy files from active routing.
replace_regex(
    "docs/DOCUMENTATION_MAP.md",
    r"## 현재 Codex 시작 문서\n.*?(?=## 항상 확인할 공식 문서)",
    '''## 현재 작업 시작점

새 작업은 고정된 과거 Work Order가 아니라 다음 정본에서 시작한다.

```text
PROJECT_CORE.md
→ CURRENT_IMPLEMENTATION_STATUS.md
→ 관련 APPROVED 책임 문서
→ OMENWARD_ROADMAP.md
→ 최신 PR·Issue와 실제 코드·테스트
```

현재 C1 시작 문서는 `C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md`와 룰렛 APPROVED 정본이다. 과거 Work Order·Goal·Proposal은 Git 이력에서만 추적한다.

''',
)
for exact in (
    '| `work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md` | 현재 새 Codex 채팅 작업 요청·복사 프롬프트 |\n',
    '| `work_orders/0001-phase-0-codex-plan-mode.md` | Phase 0 이전에 사용한 과거 작업 요청 |\n',
    '| `design/proposals/0001-phase-0-godot-bootstrap.md` | Phase 0 사전 기술 추천안·변경 이력 |\n',
):
    text = read("docs/DOCUMENTATION_MAP.md")
    write("docs/DOCUMENTATION_MAP.md", text.replace(exact, ""))
replace_once("docs/DOCUMENTATION_MAP.md", "| 새 Codex 채팅·현재 main 조사 | `PROJECT_CORE.md`, `CURRENT_IMPLEMENTATION_STATUS.md`, `work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md`, `PROPOSAL_WORKFLOW.md`, 현재 Issue·PR·Goal |", "| 새 작업·현재 main 조사 | `PROJECT_CORE.md`, `CURRENT_IMPLEMENTATION_STATUS.md`, 관련 APPROVED 문서, 최신 PR·Issue, 실제 파일·테스트 |")
replace_once("docs/DOCUMENTATION_MAP.md", "| 과거 Phase 0 결정 추적 | `work_orders/0001-phase-0-codex-plan-mode.md`, `design/proposals/0001-phase-0-godot-bootstrap.md`, Goal 0001 |", "| 과거 단계 결정 추적 | Git 커밋·병합 PR 이력 |")
replace_once("docs/DOCUMENTATION_MAP.md", "| 현재 Codex 작업 요청 | `work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md` |", "| 현재 C1 구현·증거 | `C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md` |")
replace_once("docs/DOCUMENTATION_MAP.md", "→ 현재 Codex 작업이면 work_orders 문서", "→ 현재 PR·Issue와 관련 승인 보고서")

write(
    "docs/VERTICAL_SLICE_VALIDATION.md",
    '''# Vertical Slice Validation

## Automated

Godot 4.7.1 Standard editor binary로 저장소 루트에서 실행한다.

```powershell
Get-ChildItem tests/headless/*_test.gd | ForEach-Object { & Godot_v4.7.1-stable_win64_console.exe --headless --path . -s ("res://tests/headless/" + $_.Name) }
Godot_v4.7.1-stable_win64_console.exe --headless --path . --editor --quit
Godot_v4.7.1-stable_win64_console.exe --headless --path . --quit-after 1
python tools/validate_project_core_docs.py
python tools/validate_c1_roulette.py
python -m unittest discover -s tests/python -v
git diff --check
```

GitHub Actions의 `Validate C1 Roulette Contract`가 Linux Godot runtime과 Ubuntu/Windows Python 계약을 재검증한다.

현재 자동 범위:

- 공용 병종·양 진영 데이터.
- 3라인·성문·거점·경제·건설·웨이브·암살자 우회.
- C1 중앙 판정·8개 완성선·등급·금화·전설 제한·결과 보관·배치.
- 구형 활성 파일 참조와 깨진 내부 링크.

## Manual QA still required

1. 튜토리얼과 정규 스테이지를 실행한다.
2. 1920×1080에서 병영 건설→룰렛→결과 보관→라인 배치를 확인한다.
3. 1280×720에서 보드·등급·보관 상태와 세 라인이 읽히는지 확인한다.
4. 이동권·럭키는 C1U 결정 전 최종 동작으로 판정하지 않는다.
5. W1~W20 연속 플레이와 재미·밸런스는 C2 이후 별도 실행한다.
''',
)

write(
    ".github/workflows/validate-c1-roulette.yml",
    '''name: Validate C1 Roulette Contract

on:
  pull_request:
    paths:
      - "scripts/**"
      - "scenes/**"
      - "tests/**"
      - "docs/**"
      - "README.md"
      - "tools/validate_c1_roulette.py"
      - ".github/workflows/validate-c1-roulette.yml"
  workflow_dispatch:

permissions:
  contents: read

jobs:
  contracts:
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest]
        python-version: ["3.12", "3.13"]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - name: Compile Python contracts
        run: python -m py_compile tools/validate_c1_roulette.py tests/python/test_c1_roulette_contract.py tools/validate_project_core_docs.py
      - name: Validate C1 roulette and active references
        run: python tools/validate_c1_roulette.py
      - name: Run all Python repository tests
        run: python -m unittest discover -s tests/python -v
      - name: Validate project core documents
        run: python tools/validate_project_core_docs.py
      - name: Validate Skill system when present
        shell: bash
        run: |
          if [ -f tools/validate_skill_system.py ]; then python tools/validate_skill_system.py; fi
      - name: Check whitespace
        run: git diff --check

  godot:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Godot 4.7.1 Standard
        shell: bash
        run: |
          curl -fL "https://github.com/godotengine/godot-builds/releases/download/4.7.1-stable/Godot_v4.7.1-stable_linux.x86_64.zip" -o godot.zip
          unzip -q godot.zip
          chmod +x Godot_v4.7.1-stable_linux.x86_64
          ./Godot_v4.7.1-stable_linux.x86_64 --version
      - name: Import project
        run: ./Godot_v4.7.1-stable_linux.x86_64 --headless --path . --editor --quit
      - name: Run all headless contract tests
        shell: bash
        run: |
          set -euo pipefail
          for test_file in tests/headless/*_test.gd; do
            echo "Running ${test_file}"
            ./Godot_v4.7.1-stable_linux.x86_64 --headless --path . -s "res://${test_file}"
          done
      - name: Runtime smoke
        run: ./Godot_v4.7.1-stable_linux.x86_64 --headless --path . --quit-after 1
''',
)

# Delete temporary audit payloads and bootstrap files.
for relative in (
    "docs/_C1_ROULETTE_AUDIT_INPUT.md",
    "docs/_C1_ROULETTE_AUDIT_INPUT.json",
    "docs/_C1_ROULETTE_SHORTLIST.md",
    "docs/_C1_SHORTLIST_FAILURE.log",
    "tools/_apply_c1_roulette_contract.py",
    ".github/workflows/apply-c1-roulette-contract-once.yml",
):
    path = ROOT / relative
    if path.exists():
        path.unlink()

run("python", "-m", "py_compile", "tools/validate_c1_roulette.py", "tests/python/test_c1_roulette_contract.py", "tools/validate_project_core_docs.py")
run("python", "tools/validate_c1_roulette.py")
run("python", "-m", "unittest", "discover", "-s", "tests/python", "-v")
run("python", "tools/validate_project_core_docs.py")
if (ROOT / "tools/validate_skill_system.py").exists():
    run("python", "tools/validate_skill_system.py")
run("git", "diff", "--check")
run("git", "config", "user.name", "github-actions[bot]")
run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
run("git", "add", "-A")
run("git", "commit", "-m", "implement C1 approved roulette core contract")
run("git", "push", "origin", "HEAD:agent/c1-approved-roulette-contract-recovery")
