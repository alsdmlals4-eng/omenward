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
	_advance_bypasses(FIXED_STEP_SECONDS)
	for lane_id in LANE_IDS:
		var lane: LaneState = lanes[lane_id]
		for unit in lane.ordered_units():
			if not unit.is_alive():
				continue
			var target: Variant = lane.find_target(unit)
			unit.target_unit_id = target.unit_id if target != null else -1
			if target != null:
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
