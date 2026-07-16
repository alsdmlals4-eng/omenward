class_name LaneState
extends RefCounted

var lane_id: StringName
var units: Array = []


func _init(assigned_lane_id: StringName) -> void:
	lane_id = assigned_lane_id


func add_unit(unit: Variant) -> bool:
	if unit.lane_id != lane_id:
		return false
	units.append(unit)
	return true


func find_target(attacker: Variant) -> Variant:
	var candidates: Array = []
	for unit in units:
		if unit.is_alive() and unit.owner_team_id != attacker.owner_team_id:
			candidates.append(unit)
	candidates.sort_custom(func(left: Variant, right: Variant) -> bool:
		var left_distance: float = attacker.distance_to(left)
		var right_distance: float = attacker.distance_to(right)
		return left.unit_id < right.unit_id if is_equal_approx(left_distance, right_distance) else left_distance < right_distance
	)
	return candidates[0] if not candidates.is_empty() else null


func remove_dead_units() -> void:
	units = units.filter(func(unit: Variant) -> bool: return unit.is_alive())


func ordered_units() -> Array:
	var ordered := units.duplicate()
	ordered.sort_custom(func(left: Variant, right: Variant) -> bool: return left.unit_id < right.unit_id)
	return ordered


func snapshot() -> Dictionary:
	var unit_snapshots: Array = []
	for unit in ordered_units():
		unit_snapshots.append(unit.to_snapshot())
	return {"lane_id": str(lane_id), "units": unit_snapshots}
