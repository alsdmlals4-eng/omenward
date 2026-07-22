class_name StageRun
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
	if result == null or not result.accepted or result.rewards.is_empty():
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
	var reward: UnitSpawnDefinition = pending_roulette_rewards.front() as UnitSpawnDefinition
	if reward == null or not deploy_card(reward, lane_id):
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
