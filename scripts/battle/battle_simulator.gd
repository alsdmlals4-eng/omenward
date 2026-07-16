class_name BattleSimulator
extends RefCounted

const UnitInstanceScript = preload("res://scripts/battle/unit_instance.gd")
const LaneStateScript = preload("res://scripts/battle/lane_state.gd")
const GateStateScript = preload("res://scripts/battle/gate_state.gd")
const ClashZoneStateScript = preload("res://scripts/battle/clash_zone_state.gd")

const FIXED_STEP_SECONDS := 0.1
const LANE_IDS := [&"top", &"middle", &"bottom"]

var registry: DataRegistry
var seed := 0
var lanes := {}
var gates := {}
var clash_zones := {}

var _rng := RandomNumberGenerator.new()
var _accumulator := 0.0
var _tick := 0
var _next_unit_id := 1


func _init(assigned_registry: DataRegistry, seed_value: int = 0) -> void:
	registry = assigned_registry
	seed = seed_value
	_rng.seed = seed
	for lane_id in LANE_IDS:
		lanes[lane_id] = LaneStateScript.new(lane_id)
		clash_zones[lane_id] = ClashZoneStateScript.new(lane_id)
	gates = {
		"lumern": {"top": GateStateScript.new(), "middle": GateStateScript.new(), "bottom": GateStateScript.new()},
		"veil": {"top": GateStateScript.new(), "middle": GateStateScript.new(), "bottom": GateStateScript.new()},
	}


func spawn_unit(spawn: UnitSpawnDefinition) -> Variant:
	if spawn == null or not registry.archetypes.has(str(spawn.archetype_id)) or not lanes.has(spawn.lane_id):
		return null
	var unit: Variant = UnitInstanceScript.new(spawn, registry, _next_unit_id, _rng.randi_range(0, 9999))
	_next_unit_id += 1
	if not lanes[spawn.lane_id].add_unit(unit):
		return null
	return unit


func request_lane_move(unit: Variant, requested_lane_id: StringName) -> bool:
	return unit != null and unit.lane_id == requested_lane_id


func advance(delta: float) -> void:
	_accumulator += maxf(0.0, delta)
	while _accumulator + 0.000001 >= FIXED_STEP_SECONDS:
		_accumulator -= FIXED_STEP_SECONDS
		_advance_fixed_step()


func snapshot() -> Dictionary:
	var lane_snapshots: Array = []
	var unit_snapshots: Array = []
	var zone_snapshots: Array = []
	var gate_snapshots := {}
	for lane_id in LANE_IDS:
		var lane: Variant = lanes[lane_id]
		lane_snapshots.append(lane.snapshot())
		for unit in lane.ordered_units():
			unit_snapshots.append(unit.to_snapshot())
		zone_snapshots.append(clash_zones[lane_id].snapshot())
	for team_id in [&"lumern", &"veil"]:
		var team_gates := {}
		for lane_id in LANE_IDS:
			team_gates[str(lane_id)] = gates[str(team_id)][str(lane_id)].snapshot()
		gate_snapshots[str(team_id)] = team_gates
	return {
		"seed": seed,
		"tick": _tick,
		"accumulator": _accumulator,
		"lanes": lane_snapshots,
		"units": unit_snapshots,
		"gates": gate_snapshots,
		"clash_zones": zone_snapshots,
	}


func _advance_fixed_step() -> void:
	_tick += 1
	for lane_id in LANE_IDS:
		var lane: Variant = lanes[lane_id]
		for unit in lane.ordered_units():
			if not unit.is_alive():
				continue
			var target: Variant = lane.find_target(unit)
			unit.target_unit_id = target.unit_id if target != null else -1
			if target == null:
				unit.state = "idle"
				continue
			if unit.distance_to(target) > float(unit.combat_stats()["attack_range"]):
				unit.move_toward(target, FIXED_STEP_SECONDS)
				continue
			var damage: float = unit.advance_attack(FIXED_STEP_SECONDS)
			if damage > 0.0:
				target.receive_damage(damage)
		lane.remove_dead_units()
		clash_zones[lane_id].advance(FIXED_STEP_SECONDS)
	for team_id in [&"lumern", &"veil"]:
		for lane_id in LANE_IDS:
			gates[str(team_id)][str(lane_id)].advance(FIXED_STEP_SECONDS)
