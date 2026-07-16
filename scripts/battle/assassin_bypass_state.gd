class_name AssassinBypassState
extends RefCounted

const ENTRY_WINDUP := 1.0
const TRAVEL_DURATION := 9.0
const WARNING_LEAD := 2.5
const ARRIVAL_RECOVERY := 0.6
const EXIT_OFFSET := 120.0

var lane_id: StringName
var exit_position: float
var capture_power := 0.0
var state: StringName = &"windup"
var warning_active := false

var _windup_remaining := ENTRY_WINDUP
var _travel_elapsed := 0.0
var _recovery_remaining := ARRIVAL_RECOVERY


func _init(assigned_lane_id: StringName, enemy_outpost_position: float) -> void:
	lane_id = assigned_lane_id
	exit_position = enemy_outpost_position + EXIT_OFFSET


func advance(delta: float) -> void:
	var remaining := maxf(0.0, delta)
	while remaining > 0.0 and not is_complete():
		if state == &"windup":
			var windup := minf(remaining, _windup_remaining)
			_windup_remaining -= windup
			remaining -= windup
			if _windup_remaining <= 0.000001:
				state = &"travel"
			continue
		if state == &"travel":
			var travel := minf(remaining, TRAVEL_DURATION - _travel_elapsed)
			_travel_elapsed += travel
			remaining -= travel
			if _travel_elapsed + 0.000001 >= TRAVEL_DURATION - WARNING_LEAD:
				warning_active = true
			if _travel_elapsed + 0.000001 >= TRAVEL_DURATION:
				state = &"recovery"
			continue
		if state == &"recovery":
			var recovery := minf(remaining, _recovery_remaining)
			_recovery_remaining -= recovery
			remaining -= recovery
			if _recovery_remaining <= 0.000001:
				state = &"complete"


func is_complete() -> bool:
	return state == &"complete"


func snapshot() -> Dictionary:
	return {
		"lane_id": str(lane_id),
		"exit_position": exit_position,
		"capture_power": capture_power,
		"state": str(state),
		"warning_active": warning_active,
	}
