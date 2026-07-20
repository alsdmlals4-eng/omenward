class_name StageRun
extends RefCounted

const DataRegistryScript = preload("res://scripts/core/data_registry.gd")
const CombatClockScript = preload("res://scripts/core/combat_clock.gd")
const StageEconomyScript = preload("res://scripts/core/stage_economy.gd")
const BuildingServiceScript = preload("res://scripts/buildings/building_service.gd")
const RouletteServiceScript = preload("res://scripts/roulette/roulette_service.gd")
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
var last_roulette_resolution: Dictionary = {}
var current_wave := 0
var result_state: StringName = &""

var _registry: Variant
var _home_outposts := {}


func _init(assigned_progression: Variant = null) -> void:
	progression = assigned_progression if assigned_progression != null else StageProgressionScript.new()


func start(assigned_stage: Variant, seed: int) -> void:
	stage = assigned_stage
	current_wave = 0
	result_state = &""
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
	_home_outposts.clear()
	for lane_id in [&"top", &"middle", &"bottom"]:
		var outpost_id := StringName("home_%s" % lane_id)
		var outpost := OutpostStateScript.new(&"lumern")
		_home_outposts[outpost_id] = outpost
		buildings.register_outpost(outpost_id, outpost, [&"front_a", &"front_b", &"rear"])
	roulette = RouletteServiceScript.new(economy, buildings, manifest, &"lumern")
	deployment = DeploymentServiceScript.new(economy, manifest)
	wave_director = WaveDirectorScript.new(stage)
	battle = BattleSimulatorScript.new(_registry, seed)
	result_state = RUNNING


func spin_roulette(seed_input: Dictionary) -> Array:
	if roulette == null:
		last_roulette_resolution = {}
		return []
	var board: Array = roulette.spin(seed_input)
	last_roulette_resolution = roulette.last_resolution.duplicate(true)
	return board


func construct_home(building_id: StringName) -> bool:
	var node_id := &"front_a" if building_id == &"tower" else &"front_b"
	return construct_at_node(&"home_top", node_id, building_id)


func construction_status(outpost_id: StringName, node_id: StringName) -> StringName:
	return buildings.node_status(outpost_id, node_id) if buildings != null else &"unknown"


func available_buildings_for_node(outpost_id: StringName, node_id: StringName) -> Array[StringName]:
	return buildings.available_building_ids(outpost_id, node_id) if buildings != null else []


func construct_at_node(outpost_id: StringName, node_id: StringName, building_id: StringName) -> bool:
	return buildings.try_construct(outpost_id, node_id, building_id) if buildings != null else false


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
