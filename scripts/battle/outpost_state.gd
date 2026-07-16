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
var capture_progress := 0.0
var construction_locked := false
var existing_buildings_enabled := true
var prior_building_ruined := false
var capture_revision := 0

var _hold_remaining := 0.0
var _phase_remaining := 0.0
var _is_reverting := false
var _previous_owner_team_id: StringName
var _previous_existing_buildings_enabled := true
var _previous_prior_building_ruined := false


func _init(initial_owner_team_id: StringName = &"", has_existing_building: bool = false) -> void:
	owner_team_id = initial_owner_team_id
	existing_buildings_enabled = has_existing_building


func begin_capture(team_id: StringName, power: float) -> bool:
	if team_id == &"" or team_id == owner_team_id or state == STABILIZING:
		return false
	capturing_team_id = team_id
	capture_power = _normalize_capture_power(power)
	capture_progress = 0.0
	_previous_owner_team_id = owner_team_id
	_previous_existing_buildings_enabled = existing_buildings_enabled
	_previous_prior_building_ruined = prior_building_ruined
	construction_locked = true
	existing_buildings_enabled = false
	state = NEUTRALIZING
	_phase_remaining = NEUTRALIZE_SECONDS
	_hold_remaining = 0.0
	_is_reverting = false
	return true


func lose_capture_power(delta: float) -> void:
	if state != NEUTRALIZING and state != CAPTURING:
		return
	set_capture_power(capture_power - CAPTURE_POWER_REVERT_PER_SECOND * delta)


func set_capture_power(power: float) -> void:
	var previous_power := capture_power
	capture_power = _normalize_capture_power(power)
	if previous_power > 0.0 and capture_power <= 0.0:
		_hold_remaining = HOLD_SECONDS
		_is_reverting = false
	elif capture_power > 0.0:
		_hold_remaining = 0.0
		_is_reverting = false


func advance(delta: float) -> void:
	var remaining := maxf(0.0, delta)
	while remaining > 0.0:
		if state == STABILIZING:
			var stabilized := minf(remaining, _phase_remaining)
			_phase_remaining -= stabilized
			remaining -= stabilized
			if _phase_remaining <= 0.0:
				state = STABLE
				construction_locked = false
			continue
		if capture_power > 0.0:
			var capture_seconds := (2.0 - capture_progress) * NEUTRALIZE_SECONDS / capture_power
			var captured := minf(remaining, capture_seconds)
			capture_progress += captured * capture_power / NEUTRALIZE_SECONDS
			remaining -= captured
			if capture_progress >= 2.0 - 0.000001:
				_complete_capture()
				continue
			_sync_capture_phase()
			continue
		if _hold_remaining > 0.0:
			var held := minf(remaining, _hold_remaining)
			_hold_remaining -= held
			remaining -= held
			if _hold_remaining <= 0.000001:
				_hold_remaining = 0.0
				_is_reverting = true
			continue
		if _is_reverting:
			var reversion_seconds := capture_progress / CAPTURE_POWER_REVERT_PER_SECOND
			var reverted := minf(remaining, reversion_seconds)
			capture_progress -= reverted * CAPTURE_POWER_REVERT_PER_SECOND
			remaining -= reverted
			if capture_progress <= 0.000001:
				_restore_previous_stable_state()
				return
			_sync_capture_phase()
			continue
		return


func _complete_capture() -> void:
	capture_progress = 2.0
	owner_team_id = capturing_team_id
	capturing_team_id = &""
	capture_power = 0.0
	prior_building_ruined = true
	capture_revision += 1
	existing_buildings_enabled = false
	state = STABILIZING
	_phase_remaining = STABILIZE_SECONDS
	_hold_remaining = 0.0
	_is_reverting = false


func _restore_previous_stable_state() -> void:
	owner_team_id = _previous_owner_team_id
	capturing_team_id = &""
	capture_power = 0.0
	capture_progress = 0.0
	construction_locked = false
	existing_buildings_enabled = _previous_existing_buildings_enabled
	prior_building_ruined = _previous_prior_building_ruined
	state = STABLE
	_hold_remaining = 0.0
	_phase_remaining = 0.0
	_is_reverting = false


func _sync_capture_phase() -> void:
	if capture_progress < 1.0:
		state = NEUTRALIZING
		_phase_remaining = (1.0 - capture_progress) * NEUTRALIZE_SECONDS
		return
	state = CAPTURING
	_phase_remaining = (2.0 - capture_progress) * CAPTURE_SECONDS


func _normalize_capture_power(power: float) -> float:
	if power == 0.0 or power == 1.0 or power == MAX_CAPTURE_POWER:
		return power
	return 0.0


func snapshot() -> Dictionary:
	return {
		"owner_team_id": str(owner_team_id),
		"capturing_team_id": str(capturing_team_id),
		"state": state,
		"capture_power": capture_power,
		"capture_progress": capture_progress,
		"construction_locked": construction_locked,
		"existing_buildings_enabled": existing_buildings_enabled,
		"prior_building_ruined": prior_building_ruined,
		"capture_revision": capture_revision,
		"hold_remaining": _hold_remaining,
		"phase_remaining": _phase_remaining,
	}
