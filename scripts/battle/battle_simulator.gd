class_name BattleSimulator
extends RefCounted

const UnitInstanceScript = preload("res://scripts/battle/unit_instance.gd")
const LaneStateScript = preload("res://scripts/battle/lane_state.gd")
const GateStateScript = preload("res://scripts/battle/gate_state.gd")
const BaseStateScript = preload("res://scripts/battle/base_state.gd")
const ClashZoneStateScript = preload("res://scripts/battle/clash_zone_state.gd")
const OutpostStateScript = preload("res://scripts/battle/outpost_state.gd")
const AssassinBypassStateScript = preload("res://scripts/battle/assassin_bypass_state.gd")

const FIXED_STEP_SECONDS := 0.1
const LANE_IDS := [&"top", &"middle", &"bottom"]
const TEAM_IDS := [&"lumern", &"veil"]
const RUNNING := &"running"
const LUMERN_VICTORY := &"lumern_victory"
const VEIL_VICTORY := &"veil_victory"
const MUTUAL_DESTRUCTION := &"mutual_destruction"

const BLOCKED_RUNTIME_OUTPUT := "BLOCKED_RUNTIME_OUTPUT"
const PRIEST_COOLDOWN_SECONDS := 8.0
const PRIEST_BUFF_SECONDS := 5.0
const MAGE_COOLDOWN_SECONDS := 7.0
const MAGE_PRIMARY_DAMAGE := 60.0
const MAGE_COLLATERAL_DAMAGE := 45.0
const MAGE_AOE_RADIUS := 3.0
const MAGE_MAX_TARGETS := 5
const FLIER_DIVE_DAMAGE := 70.0
const GIANT_MAX_SLAM_TARGETS := 6
const GIANT_OUTER_SLAM_MULTIPLIER := 0.75
const GIANT_SLAM_RADIUS := 3.0

# Deterministic simulation coordinates only. They are not visual world-scale values.
const BASE_POSITIONS := {&"lumern": 0.0, &"veil": 100.0}
const GATE_POSITIONS := {&"lumern": 15.0, &"veil": 85.0}
const OUTPOST_POSITIONS := {&"lumern": 30.0, &"veil": 70.0}
const CLASH_POSITION := 50.0
const OBJECTIVE_RADIUS := 1.0

var registry: DataRegistry
var seed := 0
var lanes := {}
var gates := {}
var bases := {}
var outposts := {}
var clash_zones := {}
var bypasses: Array = []
var result_state: StringName = RUNNING
var objectives_enabled := true

var _rng := RandomNumberGenerator.new()
var _accumulator := 0.0
var _tick := 0
var _next_unit_id := 1
var _events: Array[Dictionary] = []
var _elapsed_seconds := 0.0
var _role_ready_at: Dictionary = {}
var _active_buffs: Dictionary = {}
var _flier_contacted: Dictionary = {}
var _flier_route_targets: Dictionary = {}
var _role_metrics: Dictionary = {
	"EFFECTIVE_HEALING_HP": 0.0,
	"OVERHEAL_WASTE": 0.0,
	"SUPPORTED_TARGET_SECONDS": 0.0,
	"BUFF_UPTIME": 0.0,
	"PRIMARY_TARGET_DAMAGE": 0.0,
	"COLLATERAL_AOE_DAMAGE": 0.0,
	"TARGETS_HIT_PER_CAST": 0.0,
	"TIME_TO_BACKLINE_CONTACT": 0.0,
	"FRONTLINE_BYPASS_DISTANCE_OR_TIME": 0.0,
	"DIVE_DAMAGE": 0.0,
	"BACKLINE_PRESSURE_SECONDS": 0.0,
	"SLAM_TARGETS_HIT": 0.0,
	"SLAM_TOTAL_DAMAGE": 0.0,
	"CONTROL_TARGET_SECONDS": BLOCKED_RUNTIME_OUTPUT,
	"AIR_TARGETABILITY_EXPOSURE": BLOCKED_RUNTIME_OUTPUT,
}


func _init(assigned_registry: DataRegistry, seed_value: int = 0, base_max_health: float = 0.0) -> void:
	registry = assigned_registry
	seed = seed_value
	_rng.seed = seed
	for lane_id in LANE_IDS:
		lanes[lane_id] = LaneStateScript.new(lane_id)
		clash_zones[lane_id] = ClashZoneStateScript.new(lane_id)
	gates = {
		&"lumern": {&"top": GateStateScript.new(), &"middle": GateStateScript.new(), &"bottom": GateStateScript.new()},
		&"veil": {&"top": GateStateScript.new(), &"middle": GateStateScript.new(), &"bottom": GateStateScript.new()},
	}
	bases = {
		&"lumern": BaseStateScript.new(base_max_health),
		&"veil": BaseStateScript.new(base_max_health),
	}
	outposts = {
		&"lumern": {
			&"top": OutpostStateScript.new(&"lumern", true),
			&"middle": OutpostStateScript.new(&"lumern", true),
			&"bottom": OutpostStateScript.new(&"lumern", true),
		},
		&"veil": {
			&"top": OutpostStateScript.new(&"veil", true),
			&"middle": OutpostStateScript.new(&"veil", true),
			&"bottom": OutpostStateScript.new(&"veil", true),
		},
	}


func spawn_unit(spawn: UnitSpawnDefinition) -> Variant:
	if spawn == null or not registry.archetypes.has(str(spawn.archetype_id)) or not lanes.has(spawn.lane_id):
		return null
	var unit: UnitInstance = UnitInstanceScript.new(spawn, registry, _next_unit_id, _rng.randi_range(0, 9999))
	_next_unit_id += 1
	if not lanes[spawn.lane_id].add_unit(unit):
		return null
	return unit


func request_lane_move(unit: Variant, requested_lane_id: StringName) -> bool:
	return unit != null and unit.lane_id == requested_lane_id


func request_assassin_bypass(unit: Variant, enemy_outpost_position: float) -> bool:
	if unit == null or unit.archetype_id != &"assassin" or not lanes.has(unit.lane_id):
		return false
	var lane: LaneState = lanes[unit.lane_id]
	if not lane.remove_unit(unit):
		return false
	bypasses.append({
		"unit": unit,
		"state": AssassinBypassStateScript.new(unit.lane_id, enemy_outpost_position),
	})
	return true


func advance(delta: float) -> void:
	_accumulator += maxf(0.0, delta)
	while _accumulator + 0.000001 >= FIXED_STEP_SECONDS:
		_accumulator -= FIXED_STEP_SECONDS
		_advance_fixed_step()


func controlled_clash_count(team_id: StringName) -> int:
	var count := 0
	for lane_id in LANE_IDS:
		var state: OutpostState = clash_zones[lane_id].outpost
		if state.is_stable_for(team_id):
			count += 1
	return count


func stable_owned_outpost_count(team_id: StringName) -> int:
	var count := 0
	for lane_id in LANE_IDS:
		for side_id in TEAM_IDS:
			var state: OutpostState = outposts[side_id][lane_id]
			if state.is_stable_for(team_id):
				count += 1
	return count


func get_unit_by_id(unit_id: int) -> Variant:
	for lane_id in LANE_IDS:
		for unit in lanes[lane_id].units:
			if int(unit.unit_id) == unit_id:
				return unit
	for entry: Dictionary in bypasses:
		var bypass_unit: Variant = entry.get("unit")
		if bypass_unit != null and int(bypass_unit.unit_id) == unit_id:
			return bypass_unit
	return null


func is_unit_alive(unit_id: int) -> bool:
	var unit: Variant = get_unit_by_id(unit_id)
	return unit != null and unit.is_alive()


func drain_events() -> Array[Dictionary]:
	var result: Array[Dictionary] = []
	for event in _events:
		result.append(event.duplicate(true))
	_events.clear()
	return result


func role_output_metrics() -> Dictionary:
	return _role_metrics.duplicate(true)


func snapshot() -> Dictionary:
	var lane_snapshots: Array = []
	var unit_snapshots: Array = []
	var zone_snapshots: Array = []
	var gate_snapshots := {}
	var outpost_snapshots := {}
	var base_snapshots := {}
	for lane_id in LANE_IDS:
		var lane: LaneState = lanes[lane_id]
		lane_snapshots.append(lane.snapshot())
		for unit in lane.ordered_units():
			unit_snapshots.append(unit.to_snapshot())
		zone_snapshots.append(clash_zones[lane_id].snapshot())
	for team_id in TEAM_IDS:
		var team_gates := {}
		var team_outposts := {}
		for lane_id in LANE_IDS:
			team_gates[str(lane_id)] = gates[team_id][lane_id].snapshot()
			team_outposts[str(lane_id)] = outposts[team_id][lane_id].snapshot()
		gate_snapshots[str(team_id)] = team_gates
		outpost_snapshots[str(team_id)] = team_outposts
		base_snapshots[str(team_id)] = bases[team_id].snapshot()
	return {
		"seed": seed,
		"tick": _tick,
		"accumulator": _accumulator,
		"result_state": str(result_state),
		"objectives_enabled": objectives_enabled,
		"lanes": lane_snapshots,
		"units": unit_snapshots,
		"gates": gate_snapshots,
		"bases": base_snapshots,
		"outposts": outpost_snapshots,
		"clash_zones": zone_snapshots,
		"bypasses": bypasses.map(func(entry: Dictionary) -> Dictionary: return entry["state"].snapshot()),
	}


func _advance_fixed_step() -> void:
	_tick += 1
	_elapsed_seconds += FIXED_STEP_SECONDS
	_update_active_buffs()
	_advance_bypasses(FIXED_STEP_SECONDS)
	for lane_id in LANE_IDS:
		var lane: LaneState = lanes[lane_id]
		for unit in lane.ordered_units():
			if not unit.is_alive():
				continue
			if unit.role == "support":
				_advance_priest(unit, lane)
				continue
			var target: Variant = lane.find_target(unit)
			if unit.archetype_id == &"flier":
				if not _flier_route_targets.has(unit.unit_id) and target != null:
					_flier_route_targets[unit.unit_id] = target.unit_id
				elif _flier_route_targets.has(unit.unit_id):
					var route_target: Variant = get_unit_by_id(int(_flier_route_targets[unit.unit_id]))
					target = route_target if route_target != null and route_target.is_alive() else target
			unit.target_unit_id = target.unit_id if target != null else -1
			if target != null:
				if unit.archetype_id == &"mage":
					_advance_mage(unit, target, lane, FIXED_STEP_SECONDS)
				elif unit.archetype_id == &"flier":
					_advance_flier(unit, target, FIXED_STEP_SECONDS)
				elif unit.archetype_id == &"giant":
					_advance_giant(unit, target, lane, FIXED_STEP_SECONDS)
				else:
					_advance_unit_combat(unit, target, FIXED_STEP_SECONDS)
			elif objectives_enabled and result_state == RUNNING:
				_advance_unit_objective(unit, FIXED_STEP_SECONDS)
			else:
				unit.state = "idle"
		lane.remove_dead_units()
	if objectives_enabled and result_state == RUNNING:
		_advance_capture_objectives(FIXED_STEP_SECONDS)
	for team_id in TEAM_IDS:
		for lane_id in LANE_IDS:
			var gate: GateState = gates[team_id][lane_id]
			var previous_state: String = gate.state
			gate.advance(FIXED_STEP_SECONDS)
			if previous_state != gate.state:
				_record_event(&"gate_state", {"team_id": str(team_id), "lane_id": str(lane_id), "state": gate.state})
	_check_base_result()


func _advance_unit_combat(unit: UnitInstance, target: UnitInstance, delta: float) -> void:
	if unit.distance_to(target) > float(unit.combat_stats().get("attack_range", 0.0)):
		unit.move_toward(target, delta)
		return
	var damage: float = unit.advance_attack(delta)
	if damage > 0.0:
		target.receive_damage(damage)


func _advance_unit_objective(unit: UnitInstance, delta: float) -> void:
	if unit.state == "bypass_exit":
		unit.state = "idle"
		return
	var objective := _next_objective(unit.owner_team_id, unit.lane_id)
	var kind: StringName = objective.get("kind", &"none")
	if kind == &"none":
		unit.state = "idle"
		return
	var position: float = float(objective.get("position", unit.lane_position))
	var attack_range: float = float(unit.combat_stats().get("attack_range", 0.0))
	var required_range := OBJECTIVE_RADIUS if kind == &"capture" else maxf(OBJECTIVE_RADIUS, attack_range)
	if unit.distance_to_position(position) > required_range:
		unit.move_toward_position(position, delta)
		return
	if kind == &"capture":
		unit.state = "capture"
		return
	var damage: float = unit.advance_attack(delta)
	if damage <= 0.0:
		return
	var defender_team: StringName = objective.get("defender_team", &"")
	if kind == &"gate":
		var gate: GateState = gates[defender_team][unit.lane_id]
		var previous_state: String = gate.state
		var applied: float = gate.apply_damage(damage, unit.is_siege_damage())
		if applied > 0.0:
			_record_event(&"gate_damage", {"attacker_team": str(unit.owner_team_id), "defender_team": str(defender_team), "lane_id": str(unit.lane_id), "damage": applied, "health": gate.health})
		if previous_state != gate.state:
			_record_event(&"gate_state", {"team_id": str(defender_team), "lane_id": str(unit.lane_id), "state": gate.state})
		return
	if kind == &"base":
		var base: BaseState = bases[defender_team]
		var previous_state: StringName = base.state
		var applied: float = base.apply_damage(damage, unit.is_siege_damage())
		if applied > 0.0:
			_record_event(&"base_damage", {"attacker_team": str(unit.owner_team_id), "defender_team": str(defender_team), "lane_id": str(unit.lane_id), "damage": applied, "health": base.health})
		if previous_state != base.state:
			_record_event(&"base_state", {"team_id": str(defender_team), "state": str(base.state)})


func _next_objective(team_id: StringName, lane_id: StringName) -> Dictionary:
	var enemy_team := _enemy_team(team_id)
	var clash: OutpostState = clash_zones[lane_id].outpost
	if not clash.is_stable_for(team_id):
		return {"kind": &"capture", "position": CLASH_POSITION, "state": clash}
	var enemy_outpost: OutpostState = outposts[enemy_team][lane_id]
	if not enemy_outpost.is_stable_for(team_id):
		return {"kind": &"capture", "position": float(OUTPOST_POSITIONS[enemy_team]), "state": enemy_outpost}
	var gate: GateState = gates[enemy_team][lane_id]
	if not gate.is_collapsed():
		return {"kind": &"gate", "position": float(GATE_POSITIONS[enemy_team]), "defender_team": enemy_team}
	var base: BaseState = bases[enemy_team]
	if not base.is_destroyed():
		return {"kind": &"base", "position": float(BASE_POSITIONS[enemy_team]), "defender_team": enemy_team}
	return {"kind": &"none"}


func _advance_capture_objectives(delta: float) -> void:
	for lane_id in LANE_IDS:
		_update_capture_state(clash_zones[lane_id].outpost, CLASH_POSITION, lane_id, &"clash", delta)
		_update_capture_state(outposts[&"lumern"][lane_id], float(OUTPOST_POSITIONS[&"lumern"]), lane_id, &"outpost_lumern", delta)
		_update_capture_state(outposts[&"veil"][lane_id], float(OUTPOST_POSITIONS[&"veil"]), lane_id, &"outpost_veil", delta)


func _update_capture_state(state: OutpostState, position: float, lane_id: StringName, objective_id: StringName, delta: float) -> void:
	var power := {&"lumern": 0.0, &"veil": 0.0}
	for unit in lanes[lane_id].units:
		if not unit.is_alive() or unit.capture_power <= 0.0 or unit.distance_to_position(position) > OBJECTIVE_RADIUS:
			continue
		power[unit.owner_team_id] = minf(OutpostState.MAX_CAPTURE_POWER, float(power.get(unit.owner_team_id, 0.0)) + unit.capture_power)
	var lumern_power: float = float(power[&"lumern"])
	var veil_power: float = float(power[&"veil"])
	var before := state.snapshot()
	if lumern_power > 0.0 and veil_power > 0.0:
		state.set_contested()
	elif lumern_power > 0.0:
		_apply_capture_presence(state, &"lumern", lumern_power)
	elif veil_power > 0.0:
		_apply_capture_presence(state, &"veil", veil_power)
	else:
		state.clear_capture_presence()
	state.advance(delta)
	var after := state.snapshot()
	if before.get("state") != after.get("state") or before.get("owner_team_id") != after.get("owner_team_id") or before.get("contested") != after.get("contested"):
		_record_event(&"objective_state", {
			"objective_id": str(objective_id),
			"lane_id": str(lane_id),
			"state": after.get("state"),
			"owner_team_id": after.get("owner_team_id"),
			"capturing_team_id": after.get("capturing_team_id"),
			"contested": after.get("contested"),
		})


func _apply_capture_presence(state: OutpostState, team_id: StringName, power: float) -> void:
	if state.is_stable_for(team_id):
		state.contested = false
		return
	if state.capturing_team_id == team_id:
		state.set_capture_power(power)
		return
	if state.state == state.STABLE:
		state.begin_capture(team_id, power)
		return
	state.clear_capture_presence()


func _check_base_result() -> void:
	var lumern_destroyed: bool = bases[&"lumern"].is_destroyed()
	var veil_destroyed: bool = bases[&"veil"].is_destroyed()
	var next_state := RUNNING
	if lumern_destroyed and veil_destroyed:
		next_state = MUTUAL_DESTRUCTION
	elif veil_destroyed:
		next_state = LUMERN_VICTORY
	elif lumern_destroyed:
		next_state = VEIL_VICTORY
	if next_state != result_state:
		result_state = next_state
		_record_event(&"battle_result", {"result_state": str(result_state)})


func _enemy_team(team_id: StringName) -> StringName:
	return &"veil" if team_id == &"lumern" else &"lumern"


func _advance_priest(unit: UnitInstance, lane: LaneState) -> void:
	if _elapsed_seconds < float(_role_ready_at.get(unit.unit_id, 0.0)):
		return
	var heal_target: Variant = lane.find_lowest_health_ally(unit)
	if heal_target != null:
		var raw_heal: float = float(heal_target.combat_stats().get("max_health", 0.0)) * 0.10 + 40.0
		var healing: Dictionary = heal_target.receive_heal(raw_heal)
		_role_metrics["EFFECTIVE_HEALING_HP"] = float(_role_metrics["EFFECTIVE_HEALING_HP"]) + float(healing["effective_heal"])
		_role_metrics["OVERHEAL_WASTE"] = float(_role_metrics["OVERHEAL_WASTE"]) + float(healing["overheal"])
		_record_event(&"role_heal", {
			"source": unit.unit_id,
			"target": heal_target.unit_id,
			"raw_heal": healing["raw_heal"],
			"effective_heal": healing["effective_heal"],
			"overheal": healing["overheal"],
		})
	else:
		var buff_target: Variant = _first_support_ally(unit, lane)
		if buff_target != null:
			_active_buffs[unit.unit_id] = {
				"target": buff_target.unit_id,
				"buff_id": "priest_encouragement",
				"ends_at": _elapsed_seconds + PRIEST_BUFF_SECONDS,
			}
			_record_event(&"role_buff_start", {
				"source": unit.unit_id,
				"target": buff_target.unit_id,
				"buff_id": "priest_encouragement",
				"duration": PRIEST_BUFF_SECONDS,
			})
	_role_ready_at[unit.unit_id] = _elapsed_seconds + PRIEST_COOLDOWN_SECONDS


func _advance_mage(unit: UnitInstance, target: UnitInstance, lane: LaneState, delta: float) -> void:
	if unit.distance_to(target) > float(unit.combat_stats().get("attack_range", 0.0)):
		unit.move_toward(target, delta)
		return
	if _elapsed_seconds < float(_role_ready_at.get(unit.unit_id, 0.0)):
		return
	var attack_marker: float = unit.advance_attack(delta)
	if attack_marker <= 0.0:
		return
	var primary_damage: float = target.receive_damage_with_channel(MAGE_PRIMARY_DAMAGE, &"magic")
	var affected_ids: Array[int] = [target.unit_id]
	var collateral_total := 0.0
	for candidate in lane.ordered_units():
		if affected_ids.size() >= MAGE_MAX_TARGETS:
			break
		if not candidate.is_alive() or candidate.owner_team_id == unit.owner_team_id or candidate == target:
			continue
		if target.distance_to(candidate) > MAGE_AOE_RADIUS:
			continue
		var applied: float = candidate.receive_damage_with_channel(MAGE_COLLATERAL_DAMAGE, &"magic")
		affected_ids.append(candidate.unit_id)
		collateral_total += applied
	_role_metrics["PRIMARY_TARGET_DAMAGE"] = float(_role_metrics["PRIMARY_TARGET_DAMAGE"]) + primary_damage
	_role_metrics["COLLATERAL_AOE_DAMAGE"] = float(_role_metrics["COLLATERAL_AOE_DAMAGE"]) + collateral_total
	_role_metrics["TARGETS_HIT_PER_CAST"] = float(_role_metrics["TARGETS_HIT_PER_CAST"]) + float(affected_ids.size())
	_record_event(&"role_aoe_hit", {
		"source": unit.unit_id,
		"primary_target": target.unit_id,
		"affected_unit_ids": affected_ids,
		"primary_damage": primary_damage,
		"collateral_damage": collateral_total,
	})
	_role_ready_at[unit.unit_id] = _elapsed_seconds + MAGE_COOLDOWN_SECONDS


func _update_active_buffs() -> void:
	var expired_sources: Array = []
	for source_id in _active_buffs:
		var buff: Dictionary = _active_buffs[source_id]
		if _elapsed_seconds >= float(buff["ends_at"]):
			_record_event(&"role_buff_end", {
				"source": source_id,
				"target": buff["target"],
				"buff_id": buff["buff_id"],
			})
			expired_sources.append(source_id)
			continue
		_role_metrics["BUFF_UPTIME"] = float(_role_metrics["BUFF_UPTIME"]) + FIXED_STEP_SECONDS
		_role_metrics["SUPPORTED_TARGET_SECONDS"] = float(_role_metrics["SUPPORTED_TARGET_SECONDS"]) + FIXED_STEP_SECONDS
	for source_id in expired_sources:
		_active_buffs.erase(source_id)


func _first_support_ally(unit: UnitInstance, lane: LaneState) -> Variant:
	for candidate in lane.ordered_units():
		if candidate.is_alive() and candidate.owner_team_id == unit.owner_team_id and candidate != unit:
			return candidate
	return null


func _advance_flier(unit: UnitInstance, target: UnitInstance, delta: float) -> void:
	if unit.distance_to(target) > float(unit.combat_stats().get("attack_range", 0.0)):
		unit.move_toward(target, delta)
		return
	if not _flier_contacted.has(unit.unit_id):
		_flier_contacted[unit.unit_id] = true
		_role_metrics["TIME_TO_BACKLINE_CONTACT"] = _elapsed_seconds
		_role_metrics["FRONTLINE_BYPASS_DISTANCE_OR_TIME"] = _elapsed_seconds
		_record_event(&"role_backline_contact", {
			"source": unit.unit_id,
			"target": target.unit_id,
			"time_to_contact": _elapsed_seconds,
		})
		var dive_damage: float = target.receive_damage_with_channel(FLIER_DIVE_DAMAGE, &"physical")
		_role_metrics["DIVE_DAMAGE"] = float(_role_metrics["DIVE_DAMAGE"]) + dive_damage
		_record_event(&"role_dive", {"source": unit.unit_id, "target": target.unit_id, "damage": dive_damage})
	_role_metrics["BACKLINE_PRESSURE_SECONDS"] = float(_role_metrics["BACKLINE_PRESSURE_SECONDS"]) + delta
	var damage: float = unit.advance_attack(delta)
	if damage > 0.0:
		target.receive_damage_with_channel(damage, &"physical")


func _advance_giant(unit: UnitInstance, target: UnitInstance, lane: LaneState, delta: float) -> void:
	if unit.distance_to(target) > float(unit.combat_stats().get("attack_range", 0.0)):
		unit.move_toward(target, delta)
		return
	var center_damage: float = unit.advance_attack(delta)
	if center_damage <= 0.0 or target.role == "air":
		return
	var affected_ids: Array[int] = []
	var damage_by_target: Dictionary = {}
	for candidate in lane.ordered_units():
		if affected_ids.size() >= GIANT_MAX_SLAM_TARGETS:
			break
		if not candidate.is_alive() or candidate.owner_team_id == unit.owner_team_id or candidate.role == "air":
			continue
		if target.distance_to(candidate) > GIANT_SLAM_RADIUS:
			continue
		var raw_damage: float = center_damage if candidate == target else center_damage * GIANT_OUTER_SLAM_MULTIPLIER
		var applied: float = candidate.receive_damage_with_channel(raw_damage, &"physical")
		affected_ids.append(candidate.unit_id)
		damage_by_target[str(candidate.unit_id)] = applied
	if affected_ids.is_empty():
		return
	var total_damage := 0.0
	for applied_damage in damage_by_target.values():
		total_damage += float(applied_damage)
	_role_metrics["SLAM_TARGETS_HIT"] = float(_role_metrics["SLAM_TARGETS_HIT"]) + float(affected_ids.size())
	_role_metrics["SLAM_TOTAL_DAMAGE"] = float(_role_metrics["SLAM_TOTAL_DAMAGE"]) + total_damage
	_record_event(&"role_slam", {
		"source": unit.unit_id,
		"affected_unit_ids": affected_ids,
		"damage_by_target": damage_by_target,
	})


func _record_event(event_type: StringName, payload: Dictionary) -> void:
	var event := payload.duplicate(true)
	event["event_type"] = str(event_type)
	event["tick"] = _tick
	_events.append(event)


func _advance_bypasses(delta: float) -> void:
	var active_bypasses: Array = []
	for entry: Dictionary in bypasses:
		var bypass: Variant = entry["state"]
		bypass.advance(delta)
		if not bypass.is_complete():
			active_bypasses.append(entry)
			continue
		var unit: UnitInstance = entry["unit"] as UnitInstance
		unit.lane_position = bypass.exit_position
		unit.state = "bypass_exit"
		lanes[unit.lane_id].add_unit(unit)
	bypasses = active_bypasses
