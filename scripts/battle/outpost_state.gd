class_name OutpostState
extends RefCounted

const NEUTRALIZING := "neutralizing"
const CAPTURING := "capturing"
const STABILIZING := "stabilizing"
const STABLE := "stable"
const MAX_CAPTURE_POWER := 2.0
const HOLD_SECONDS := 3.0
const NEUTRALIZE_SECONDS := 10.0
const CAPTURE_SECONDS := 10.0
const STABILIZE_SECONDS := 5.0
const CAPTURE_POWER_REVERT_PER_SECOND := 0.1

var owner_team_id: StringName
var capturing_team_id: StringName
var state := STABLE
var capture_power := 0.0
var construction_locked := false
var existing_buildings_enabled := true
var prior_building_ruined := false

var _hold_remaining := 0.0
var _phase_remaining := 0.0


func _init(initial_owner_team_id: StringName = &"", has_existing_building: bool = false) -> void:
	owner_team_id = initial_owner_team_id
	existing_buildings_enabled = has_existing_building


func begin_capture(team_id: StringName, power: float) -> bool:
	if team_id == &"" or team_id == owner_team_id or state == STABILIZING:
		return false
	capturing_team_id = team_id
	capture_power = clampf(power, 0.0, MAX_CAPTURE_POWER)
	construction_locked = true
	existing_buildings_enabled = false
	state = NEUTRALIZING
	_hold_remaining = HOLD_SECONDS
	_phase_remaining = NEUTRALIZE_SECONDS
	return true


func lose_capture_power(delta: float) -> void:
	if state != NEUTRALIZING and state != CAPTURING:
		return
	capture_power = maxf(0.0, capture_power - CAPTURE_POWER_REVERT_PER_SECOND * delta)
	if capture_power <= 0.0:
		capturing_team_id = &""
		state = STABLE
		construction_locked = false
		existing_buildings_enabled = not prior_building_ruined


func advance(delta: float) -> void:
	var remaining := delta
	while remaining > 0.0:
		if state == NEUTRALIZING:
			if _hold_remaining > 0.0:
				var held := minf(remaining, _hold_remaining)
				_hold_remaining -= held
				remaining -= held
				continue
			var neutralized := minf(remaining, _phase_remaining)
			_phase_remaining -= neutralized
			remaining -= neutralized
			if _phase_remaining <= 0.0:
				state = CAPTURING
				_phase_remaining = CAPTURE_SECONDS
			continue
		if state == CAPTURING:
			var captured := minf(remaining, _phase_remaining)
			_phase_remaining -= captured
			remaining -= captured
			if _phase_remaining <= 0.0:
				owner_team_id = capturing_team_id
				capturing_team_id = &""
				prior_building_ruined = true
				existing_buildings_enabled = false
				state = STABILIZING
				_phase_remaining = STABILIZE_SECONDS
			continue
		if state == STABILIZING:
			var stabilized := minf(remaining, _phase_remaining)
			_phase_remaining -= stabilized
			remaining -= stabilized
			if _phase_remaining <= 0.0:
				state = STABLE
				construction_locked = false
			continue
		return


func snapshot() -> Dictionary:
	return {
		"owner_team_id": str(owner_team_id),
		"capturing_team_id": str(capturing_team_id),
		"state": state,
		"capture_power": capture_power,
		"construction_locked": construction_locked,
		"existing_buildings_enabled": existing_buildings_enabled,
		"prior_building_ruined": prior_building_ruined,
		"hold_remaining": _hold_remaining,
		"phase_remaining": _phase_remaining,
	}
