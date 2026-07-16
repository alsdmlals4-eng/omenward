class_name ClashZoneState
extends RefCounted

const OutpostStateScript = preload("res://scripts/battle/outpost_state.gd")

var lane_id: StringName
var outpost: Variant


func _init(assigned_lane_id: StringName) -> void:
	lane_id = assigned_lane_id
	outpost = OutpostStateScript.new()


func advance(delta: float) -> void:
	outpost.advance(delta)


func snapshot() -> Dictionary:
	return {"lane_id": str(lane_id), "outpost": outpost.snapshot()}
