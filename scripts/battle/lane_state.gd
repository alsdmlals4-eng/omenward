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


func remove_unit(unit: Variant) -> bool:
	var index := units.find(unit)
	if index < 0:
		return false
	units.remove_at(index)
	return true


func find_target(attacker: Variant) -> Variant:
	var candidates: Array = _enemy_candidates(attacker)
	if candidates.is_empty():
		return null
	for priority in attacker.target_priority_tags:
		var selected: Variant = _select_priority(attacker, candidates, StringName(priority))
		if selected != null:
			return selected
	return candidates[0]


func find_lowest_health_ally(supporter: Variant) -> Variant:
	var selected: Variant = null
	for unit in units:
		if not unit.is_alive() or unit.owner_team_id != supporter.owner_team_id or unit == supporter:
			continue
		var maximum := float(unit.combat_stats().get("max_health", 0.0))
		if unit.health >= maximum:
			continue
		if selected == null or unit.health < selected.health or (is_equal_approx(unit.health, selected.health) and unit.unit_id < selected.unit_id):
			selected = unit
	return selected


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


func _enemy_candidates(attacker: Variant) -> Array:
	var candidates: Array = []
	for unit in units:
		if not unit.is_alive() or unit.owner_team_id == attacker.owner_team_id:
			continue
		if unit.role == "air" and not attacker.target_priority_tags.has("flying"):
			continue
		candidates.append(unit)
	candidates.sort_custom(func(left: Variant, right: Variant) -> bool:
		var left_distance: float = attacker.distance_to(left)
		var right_distance: float = attacker.distance_to(right)
		return left.unit_id < right.unit_id if is_equal_approx(left_distance, right_distance) else left_distance < right_distance
	)
	return candidates


func _select_priority(attacker: Variant, candidates: Array, priority: StringName) -> Variant:
	if priority == &"flying":
		for candidate in candidates:
			if candidate.role == "air":
				return candidate
		return null
	if priority == &"backline":
		var selected: Variant = null
		for candidate in candidates:
			if selected == null:
				selected = candidate
				continue
			var is_deeper: bool = candidate.lane_position > selected.lane_position if attacker.owner_team_id == &"lumern" else candidate.lane_position < selected.lane_position
			if is_deeper or (is_equal_approx(candidate.lane_position, selected.lane_position) and candidate.unit_id < selected.unit_id):
				selected = candidate
		return selected
	if priority == &"cluster":
		var selected: Variant = null
		var selected_count := -1
		for candidate in candidates:
			var count := 0
			for neighbor in candidates:
				if candidate.distance_to(neighbor) <= 3.0:
					count += 1
			if count > selected_count:
				selected = candidate
				selected_count = count
		return selected
	return null
