class_name FixedTowerState
extends RefCounted

const CAPTURE_POWER := 0.0

var lane_id: StringName
var owner_team_id: StringName = &""
var active := false
var capture_power := CAPTURE_POWER


func _init(assigned_lane_id: StringName) -> void:
	lane_id = assigned_lane_id


func sync_from_tower_bearing_objective(objective: OutpostState) -> void:
	active = objective != null and objective.state == objective.STABLE
	owner_team_id = objective.owner_team_id if active else &""


func snapshot() -> Dictionary:
	return {
		"lane_id": str(lane_id),
		"owner_team_id": str(owner_team_id),
		"active": active,
		"capture_power": capture_power,
	}
