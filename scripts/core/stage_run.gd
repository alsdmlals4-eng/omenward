class_name StageRun
extends RefCounted

const DataRegistryScript = preload("res://scripts/core/data_registry.gd")
const CombatClockScript = preload("res://scripts/core/combat_clock.gd")
const StageEconomyScript = preload("res://scripts/core/stage_economy.gd")
const BuildingServiceScript = preload("res://scripts/buildings/building_service.gd")
const RouletteServiceScript = preload("res://scripts/roulette/roulette_service.gd")
const RouletteSpinResultScript = preload("res://scripts/data/roulette_spin_result.gd")
const RouletteSpinResult = preload("res://scripts/data/roulette_spin_result.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")
const DeploymentServiceScript = preload("res://scripts/units/deployment_service.gd")
const WaveDirectorScript = preload("res://scripts/waves/wave_director.gd")
const BattleSimulatorScript = preload("res://scripts/battle/battle_simulator.gd")
const StageProgressionScript = preload("res://scripts/core/stage_progression.gd")
const CoreUxServiceScript = preload("res://scripts/core/core_ux_service.gd")

const RUNNING := &"running"
const VICTORY := &"victory"
const DEFEAT := &"defeat"
const PREPARE := &"prepare"
const STOPPED_3X3 := &"stopped_3x3"
const MANIPULATE := &"manipulate"
const RESULT_CONFIRM := &"result_confirm"
const COMMIT := &"commit"
const BATTLE := &"battle"
const REVIEW := &"review"
const COMMAND_LANE_IDS := [&"top", &"middle", &"bottom"]

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
var core_ux: Variant
var current_wave := 0
var result_state: StringName = &""
var pending_roulette_rewards: Array[UnitSpawnDefinition] = []
var last_roulette_result: RouletteSpinResult
var legendary_boss_unit_id := -1
var command_phase: StringName = PREPARE
var roulette_session := {}
var roulette_moves_remaining := 0
var pending_deployment_assignments := {}

var _registry: Variant


func _init(assigned_progression: Variant = null) -> void:
	progression = assigned_progression if assigned_progression != null else StageProgressionScript.new()


func start(assigned_stage: Variant, seed: int) -> void:
	stage = assigned_stage
	current_wave = 0
	result_state = &""
	legendary_boss_unit_id = -1
	pending_roulette_rewards.clear()
	last_roulette_result = null
	command_phase = PREPARE
	roulette_session = {}
	roulette_moves_remaining = 0
	pending_deployment_assignments = {}
	core_ux = null
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
	roulette = RouletteServiceScript.new(economy, buildings, manifest, &"lumern")
	deployment = DeploymentServiceScript.new(economy, manifest)
	wave_director = WaveDirectorScript.new(stage)
	battle = BattleSimulatorScript.new(_registry, seed, manifest.base_max_health)
	_register_battle_outposts()
	core_ux = CoreUxServiceScript.new(self, _registry)
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


func begin_roulette_session(seed_input: Dictionary) -> bool:
	if command_phase != PREPARE or roulette == null or not pending_roulette_rewards.is_empty():
		return false
	var session: Dictionary = roulette.begin_paid_spin(seed_input)
	if not bool(session.get("accepted", false)):
		var rejected := RouletteSpinResultScript.new() as RouletteSpinResult
		rejected.failure_reason = StringName(session.get("failure_reason", &"service_not_ready"))
		last_roulette_result = rejected
		return false
	roulette_session = session
	roulette_moves_remaining = 3
	command_phase = STOPPED_3X3
	return true


func preview_roulette_result() -> RouletteSpinResult:
	var unavailable := RouletteSpinResultScript.new() as RouletteSpinResult
	if roulette == null or roulette_session.is_empty():
		unavailable.failure_reason = &"session_not_ready"
		return unavailable
	return roulette.preview_paid_board(
		roulette_session.get("board", []),
		int(roulette_session.get("resolution_seed", 0)),
	)


func move_roulette_row(row_index: int, direction: int) -> bool:
	if row_index < 0 or row_index > 2:
		return false
	return _move_roulette_indexes([row_index * 3, row_index * 3 + 1, row_index * 3 + 2], direction)


func move_roulette_column(column_index: int, direction: int) -> bool:
	if column_index < 0 or column_index > 2:
		return false
	return _move_roulette_indexes([column_index, column_index + 3, column_index + 6], direction)


func lock_roulette_result() -> bool:
	if command_phase != STOPPED_3X3 and command_phase != MANIPULATE:
		return false
	last_roulette_result = preview_roulette_result()
	if not last_roulette_result.accepted:
		return false
	command_phase = RESULT_CONFIRM
	return true


func confirm_roulette_result() -> bool:
	if command_phase != RESULT_CONFIRM or roulette == null or roulette_session.is_empty():
		return false
	var result: RouletteSpinResult = roulette.resolve_paid_board(
		roulette_session.get("board", []),
		int(roulette_session.get("resolution_seed", 0)),
		int(roulette_session.get("spin_seed", manifest.seed)),
	)
	if not result.accepted:
		last_roulette_result = result
		return false
	last_roulette_result = result
	store_roulette_result(result)
	roulette_session = {}
	roulette_moves_remaining = 0
	pending_deployment_assignments = {}
	command_phase = COMMIT
	return true


func assign_pending_reward(reward_index: int, lane_id: StringName) -> bool:
	if command_phase != COMMIT or reward_index < 0 or reward_index >= pending_roulette_rewards.size() or not COMMAND_LANE_IDS.has(lane_id):
		return false
	pending_deployment_assignments[reward_index] = lane_id
	return true


func confirm_pending_deployment() -> bool:
	if command_phase != COMMIT or pending_roulette_rewards.is_empty():
		return false
	var cards: Array[UnitSpawnDefinition] = []
	for reward_index in pending_roulette_rewards.size():
		if not pending_deployment_assignments.has(reward_index):
			return false
		var card := pending_roulette_rewards[reward_index].duplicate() as UnitSpawnDefinition
		if card == null:
			return false
		card.lane_id = StringName(pending_deployment_assignments[reward_index])
		if battle == null or not COMMAND_LANE_IDS.has(card.lane_id) or not battle.can_spawn_unit(card):
			return false
		cards.append(card)
	if deployment == null or not deployment.can_deploy_batch(cards):
		return false
	if not deployment.deploy_batch(cards, 10.0):
		return false
	for card in cards:
		if battle.spawn_unit(card) == null:
			return false
	manifest.input_log.append({
		"action": "commit_deployment",
		"assignments": cards.map(func(card: UnitSpawnDefinition) -> Dictionary: return card.to_dictionary()),
	})
	pending_roulette_rewards.clear()
	pending_deployment_assignments = {}
	command_phase = BATTLE
	return true


func begin_battle() -> bool:
	if command_phase == PREPARE and pending_roulette_rewards.is_empty() and roulette_session.is_empty():
		command_phase = BATTLE
		return true
	if command_phase == COMMIT and pending_roulette_rewards.is_empty():
		command_phase = BATTLE
		return true
	return false


func store_roulette_result(result: RouletteSpinResult) -> bool:
	if result == null or not result.accepted or result.rewards.is_empty():
		return false
	for reward in result.rewards:
		pending_roulette_rewards.append(reward.duplicate() as UnitSpawnDefinition)
	return true


func construct_home(building_id: StringName) -> bool:
	var node_by_building := {
		&"tower": &"front_a",
		&"farm": &"front_b",
		&"barracks": &"rear",
	}
	if not node_by_building.has(building_id):
		return false
	return construct_at_outpost(&"lumern_middle", node_by_building[building_id], building_id)


func construct_at_outpost(outpost_id: StringName, node_id: StringName, building_id: StringName) -> bool:
	return buildings != null and buildings.try_construct(outpost_id, node_id, building_id)


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
			_finish_victory(&"debug_command")
		"stage_defeat":
			_finish_defeat(&"debug_command")
		_:
			return false
	manifest.input_log.append(command.duplicate(true))
	return true


func core_ux_snapshot() -> Dictionary:
	if core_ux == null:
		return {
			"token_ledger": [],
			"construction_comparison": [],
			"omen": {"phase": "complete", "seconds_remaining": 0.0},
			"tactical_overlay": [],
			"latest_wave_report": {},
			"wave_reports": [],
		}
	return core_ux.snapshot()


func advance(delta: float) -> void:
	if result_state != RUNNING or command_phase != BATTLE:
		return
	clock.advance(delta)
	for wave in wave_director.advance(delta):
		current_wave = wave.wave_number
		var spawned_units: Array[Dictionary] = []
		for spawn in wave.spawns:
			var unit: Variant = battle.spawn_unit(spawn.duplicate() as UnitSpawnDefinition)
			if unit != null:
				spawned_units.append({
					"unit_id": int(unit.unit_id),
					"lane_id": unit.lane_id,
					"team_id": unit.owner_team_id,
				})
			if wave.wave_number == 15 and wave.boss_kind == &"legendary" and unit != null and spawn.rank_id == &"legendary":
				legendary_boss_unit_id = int(unit.unit_id)
		if core_ux != null:
			core_ux.register_wave(wave, spawned_units)
		manifest.input_log.append({"action": "wave", "wave_number": current_wave})
	var before_units: Array = (battle.snapshot().get("units", []) as Array).duplicate(true)
	battle.advance(delta)
	var after_units: Array = (battle.snapshot().get("units", []) as Array).duplicate(true)
	buildings.sync_outpost_states()
	var battle_events: Array[Dictionary] = battle.drain_events()
	for event in battle_events:
		manifest.input_log.append(event)
	if core_ux != null:
		core_ux.observe_unit_delta(before_units, after_units)
		core_ux.consume_battle_events(battle_events)
		core_ux.update_wave_reports()
	_resolve_natural_result()
	if result_state == RUNNING:
		economy.advance(delta, battle.controlled_clash_count(&"lumern"), battle.stable_owned_outpost_count(&"lumern"))


func _register_battle_outposts() -> void:
	for team_id in battle.TEAM_IDS:
		for lane_id in battle.LANE_IDS:
			var outpost_id := StringName("%s_%s" % [team_id, lane_id])
			buildings.register_outpost(outpost_id, battle.outposts[team_id][lane_id], [&"front_a", &"front_b", &"rear"])


func _resolve_natural_result() -> void:
	if battle.result_state == battle.LUMERN_VICTORY:
		_finish_victory(&"enemy_base_destroyed")
		return
	if battle.result_state == battle.VEIL_VICTORY or battle.result_state == battle.MUTUAL_DESTRUCTION:
		_finish_defeat(&"player_base_destroyed")
		return
	if current_wave >= 15 and legendary_boss_unit_id > 0 and not battle.is_unit_alive(legendary_boss_unit_id):
		_finish_victory(&"wave_15_legendary_boss_defeated")


func _finish_victory(reason: StringName) -> void:
	if result_state != RUNNING:
		return
	result_state = VICTORY
	command_phase = REVIEW
	progression.record_victory(stage)
	manifest.input_log.append({"action": "stage_result", "result": "victory", "reason": str(reason)})


func _finish_defeat(reason: StringName) -> void:
	if result_state != RUNNING:
		return
	result_state = DEFEAT
	command_phase = REVIEW
	manifest.input_log.append({"action": "stage_result", "result": "defeat", "reason": str(reason)})


func _move_roulette_indexes(indexes: Array, direction: int) -> bool:
	if (command_phase != STOPPED_3X3 and command_phase != MANIPULATE) or roulette_session.is_empty() or roulette_moves_remaining <= 0:
		return false
	if direction != -1 and direction != 1:
		return false
	var board: Array = roulette_session.get("board", [])
	if board.size() != 9:
		return false
	var values := []
	for index in indexes:
		values.append(board[index])
	for local_index in indexes.size():
		var source_index := posmod(local_index - direction, indexes.size())
		board[indexes[local_index]] = values[source_index]
	roulette_session["board"] = board
	roulette_moves_remaining -= 1
	command_phase = MANIPULATE
	manifest.input_log.append({
		"action": "roulette_move",
		"axis": "row" if indexes[1] - indexes[0] == 1 else "column",
		"index": indexes[0] / 3 if indexes[1] - indexes[0] == 1 else indexes[0],
		"direction": direction,
		"moves_remaining": roulette_moves_remaining,
	})
	return true
