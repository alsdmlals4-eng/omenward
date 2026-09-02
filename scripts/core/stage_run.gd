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
const COMMAND_LANE_IDS := [&"front"]
const TAB_DOMESTIC := &"domestic"
const TAB_ROULETTE := &"roulette"
const TAB_FRONT := &"front"
const TAB_IDS := [TAB_DOMESTIC, TAB_ROULETTE, TAB_FRONT]
const FRONT_MAP_LOCKED := &"locked"
const FRONT_MAP_CURRENT := &"current"
const FRONT_MAP_CLEARED := &"cleared"
const FRONT_MAP_AVAILABLE := &"available"
const FRONT_MAP_RESULT_NONE := &""
const FRONT_MAP_RESULT_CLEARED := &"cleared"
const TUTORIAL_FRONT_MAP := {
	"map_id": "ward_citadel",
	"display_name": "수호 성채",
	"terrain_id": "ward_citadel",
	"wave_first": 1,
	"wave_last": 4,
}

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
var active_tab: StringName = TAB_DOMESTIC
var roulette_session := {}
var roulette_moves_remaining := 0
var pending_deployment_assignments := {}
var front_map_index := 0
var front_map_result: StringName = FRONT_MAP_RESULT_NONE

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
	active_tab = TAB_DOMESTIC
	roulette_session = {}
	roulette_moves_remaining = 0
	pending_deployment_assignments = {}
	front_map_index = 0
	front_map_result = FRONT_MAP_RESULT_NONE
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
	buildings.set_roster_mutation_allowed(not manifest.tutorial_stage)
	if manifest.tutorial_stage:
		buildings.install_prebuilt(&"barracks")
	roulette = RouletteServiceScript.new(economy, buildings, manifest, &"lumern")
	deployment = DeploymentServiceScript.new(economy, manifest)
	battle = BattleSimulatorScript.new(_registry, seed, manifest.base_max_health)
	wave_director = WaveDirectorScript.new(stage, _waves_for_current_front_map())
	_sync_building_roster_capacity()
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
	active_tab = TAB_ROULETTE
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
	active_tab = TAB_FRONT
	return true


func assign_pending_reward(reward_index: int, lane_id: StringName = &"front") -> bool:
	if command_phase != COMMIT or reward_index < 0 or reward_index >= pending_roulette_rewards.size() or lane_id != &"front":
		return false
	pending_deployment_assignments[reward_index] = &"front"
	return true


func confirm_pending_deployment() -> bool:
	if command_phase != COMMIT or pending_roulette_rewards.is_empty():
		return false
	var cards: Array[UnitSpawnDefinition] = []
	for reward_index in pending_roulette_rewards.size():
		if not pending_deployment_assignments.has(reward_index):
			if not assign_pending_reward(reward_index):
				return false
		var card := pending_roulette_rewards[reward_index].duplicate() as UnitSpawnDefinition
		if card == null:
			return false
		card.lane_id = &"front"
		if battle == null or not battle.accepts_front_id(card.lane_id) or not battle.can_spawn_unit(card):
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
	active_tab = TAB_FRONT
	return true


func begin_battle() -> bool:
	if command_phase == PREPARE and pending_roulette_rewards.is_empty() and roulette_session.is_empty():
		command_phase = BATTLE
		active_tab = TAB_FRONT
		return true
	if command_phase == COMMIT and pending_roulette_rewards.is_empty():
		command_phase = BATTLE
		active_tab = TAB_FRONT
		return true
	return false


func store_roulette_result(result: RouletteSpinResult) -> bool:
	if result == null or not result.accepted or result.rewards.is_empty():
		return false
	for reward in result.rewards:
		pending_roulette_rewards.append(reward.duplicate() as UnitSpawnDefinition)
	return true


func install_building(building_id: StringName) -> bool:
	if command_phase != PREPARE:
		return false
	_sync_building_roster_capacity()
	return buildings != null and buildings.try_install(building_id)


func move_building_roster_entry(from_slot_index: int, to_slot_index: int) -> bool:
	if command_phase != PREPARE:
		return false
	_sync_building_roster_capacity()
	return buildings != null and buildings.move_roster_entry(from_slot_index, to_slot_index)


func building_roster_snapshot() -> Array[Dictionary]:
	_sync_building_roster_capacity()
	return buildings.roster_snapshot() if buildings != null else []


func front_slot_capacity() -> int:
	_sync_building_roster_capacity()
	return buildings.unlocked_slot_capacity() if buildings != null else 0


func current_front_map() -> Dictionary:
	if not _uses_sequential_front_maps():
		var tutorial_map := TUTORIAL_FRONT_MAP.duplicate(true)
		tutorial_map["wave_last"] = stage.waves.size() if stage != null else 0
		return tutorial_map
	var definition: Variant = stage.front_map_at(front_map_index)
	return definition.to_dictionary() if definition != null else {}


func front_map_snapshot() -> Array:
	var result: Array = []
	if not _uses_sequential_front_maps():
		var tutorial_map := current_front_map()
		tutorial_map["state"] = FRONT_MAP_CURRENT
		tutorial_map["selectable"] = false
		result.append(tutorial_map)
		return result
	for index in stage.front_maps.size():
		var definition: Variant = stage.front_map_at(index)
		if definition == null:
			continue
		var entry: Dictionary = definition.to_dictionary()
		entry["state"] = _front_map_state_at(index)
		entry["selectable"] = false
		result.append(entry)
	return result


func can_enter_next_front_map() -> bool:
	return _uses_sequential_front_maps() and front_map_result == FRONT_MAP_RESULT_CLEARED and front_map_index < stage.front_maps.size() - 1 and result_state == RUNNING and command_phase == REVIEW


func enter_next_front_map() -> bool:
	if not can_enter_next_front_map():
		return false
	front_map_index += 1
	front_map_result = FRONT_MAP_RESULT_NONE
	current_wave = 0
	legendary_boss_unit_id = -1
	if battle != null:
		battle.reset_for_next_front_map()
	wave_director = WaveDirectorScript.new(stage, _waves_for_current_front_map())
	command_phase = PREPARE
	active_tab = TAB_DOMESTIC
	manifest.input_log.append({
		"action": "enter_front_map",
		"map_index": front_map_index,
		"map_id": current_front_map().get("map_id", ""),
	})
	_sync_building_roster_capacity()
	return true


func set_active_tab(tab_id: StringName) -> bool:
	if not TAB_IDS.has(tab_id):
		return false
	active_tab = tab_id
	return true


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
			_finish_current_front_map_victory(&"debug_command")
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
					"front_id": unit.lane_id,
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
	_sync_building_roster_capacity()
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


func _sync_building_roster_capacity() -> void:
	if buildings == null or battle == null:
		return
	buildings.sync_occupation_capacity(
		battle.stable_player_forward_base_count(),
		1 if battle.clash_is_stable_for(&"lumern") else 0,
	)


func _resolve_natural_result() -> void:
	if battle.result_state == battle.LUMERN_VICTORY:
		if not _uses_sequential_front_maps() or _current_front_map_wave_package_resolved():
			_finish_current_front_map_victory(&"enemy_base_destroyed")
		return
	if battle.result_state == battle.VEIL_VICTORY or battle.result_state == battle.MUTUAL_DESTRUCTION:
		_finish_defeat(&"player_base_destroyed")
		return
	if _uses_sequential_front_maps() and _current_front_map_wave_package_resolved():
		_finish_current_front_map_victory(&"wave_package_cleared")
		return
	if not _uses_sequential_front_maps() and current_wave >= 15 and legendary_boss_unit_id > 0 and not battle.is_unit_alive(legendary_boss_unit_id):
		_finish_victory(&"wave_15_legendary_boss_defeated")


func _finish_current_front_map_victory(reason: StringName) -> void:
	if result_state != RUNNING:
		return
	if not _uses_sequential_front_maps():
		_finish_victory(reason)
		return
	front_map_result = FRONT_MAP_RESULT_CLEARED
	if front_map_index >= stage.front_maps.size() - 1:
		_finish_victory(reason)
		return
	command_phase = REVIEW
	active_tab = TAB_FRONT
	manifest.input_log.append({
		"action": "front_map_result",
		"map_index": front_map_index,
		"map_id": current_front_map().get("map_id", ""),
		"result": "victory",
		"reason": str(reason),
	})


func _finish_victory(reason: StringName) -> void:
	if result_state != RUNNING:
		return
	result_state = VICTORY
	command_phase = REVIEW
	active_tab = TAB_FRONT
	progression.record_victory(stage)
	manifest.input_log.append({"action": "stage_result", "result": "victory", "reason": str(reason)})


func _finish_defeat(reason: StringName) -> void:
	if result_state != RUNNING:
		return
	result_state = DEFEAT
	command_phase = REVIEW
	active_tab = TAB_FRONT
	manifest.input_log.append({"action": "stage_result", "result": "defeat", "reason": str(reason)})


func _uses_sequential_front_maps() -> bool:
	return stage != null and not bool(stage.tutorial_stage) and stage.front_maps.size() == 5


func _waves_for_current_front_map() -> Array:
	if stage == null:
		return []
	if not _uses_sequential_front_maps():
		return stage.waves.duplicate()
	var current := current_front_map()
	var waves: Array = []
	for wave in stage.waves:
		if int(wave.wave_number) >= int(current.get("wave_first", 0)) and int(wave.wave_number) <= int(current.get("wave_last", -1)):
			waves.append(wave)
	return waves


func _front_map_state_at(index: int) -> StringName:
	if index < front_map_index:
		return FRONT_MAP_CLEARED
	if index == front_map_index:
		return FRONT_MAP_CLEARED if front_map_result == FRONT_MAP_RESULT_CLEARED else FRONT_MAP_CURRENT
	if index == front_map_index + 1 and front_map_result == FRONT_MAP_RESULT_CLEARED:
		return FRONT_MAP_AVAILABLE
	return FRONT_MAP_LOCKED


func _all_veil_units_defeated() -> bool:
	return battle != null and not battle.has_living_units_for(&"veil")


func _current_front_map_wave_package_resolved() -> bool:
	return wave_director != null and wave_director.is_exhausted() and _all_veil_units_defeated()


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
