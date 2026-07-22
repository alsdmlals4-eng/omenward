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
const CAPTURE_PROGRESS_REVERT_PER_SECOND := 0.1

var owner_team_id: StringName
var capturing_team_id: StringName
var state := STABLE
var capture_power := 0.0
var capture_progress := 0.0
var construction_locked := false
var existing_buildings_enabled := true
var prior_building_ruined := false
var capture_revision := 0
var contested := false

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
	var normalized_power := _normalize_capture_power(power)
	if team_id == &"" or team_id == owner_team_id or state == STABILIZING or normalized_power <= 0.0:
		return false
	if (state == NEUTRALIZING or state == CAPTURING) and capturing_team_id == team_id:
		set_capture_power(normalized_power)
		return true
	if state != STABLE:
		return false
	capturing_team_id = team_id
	capture_power = normalized_power
	capture_progress = 1.0 if owner_team_id == &"" else 0.0
	_previous_owner_team_id = owner_team_id
	_previous_existing_buildings_enabled = existing_buildings_enabled
	_previous_prior_building_ruined = prior_building_ruined
	construction_locked = true
	contested = false
	_hold_remaining = 0.0
	_is_reverting = false
	_sync_capture_phase()
	return true


func set_capture_power(power: float) -> void:
	if state != NEUTRALIZING and state != CAPTURING:
		return
	var previous_power := capture_power
	capture_power = _normalize_capture_power(power)
	contested = false
	if previous_power > 0.0 and capture_power <= 0.0:
		_hold_remaining = HOLD_SECONDS
		_is_reverting = false
	elif capture_power > 0.0:
		_hold_remaining = 0.0
		_is_reverting = false


func set_contested() -> void:
	if state == STABILIZING:
		return
	capture_power = 0.0
	contested = true
	_hold_remaining = 0.0
	_is_reverting = false


func clear_capture_presence() -> void:
	if state == STABLE:
		contested = false
		return
	if state != NEUTRALIZING and state != CAPTURING:
		return
	var had_presence := capture_power > 0.0 or contested
	capture_power = 0.0
	contested = false
	if had_presence:
		_hold_remaining = HOLD_SECONDS
		_is_reverting = false


func advance(delta: float) -> void:
	var remaining := maxf(0.0, delta)
	while remaining > 0.000001:
		if state == STABILIZING:
			var stabilized := minf(remaining, _phase_remaining)
			_phase_remaining -= stabilized
			remaining -= stabilized
			if _phase_remaining <= 0.000001:
				_phase_remaining = 0.0
				state = STABLE
				construction_locked = false
			continue
		if contested:
			return
		if capture_power > 0.0:
			var boundary := 1.0 if capture_progress < 1.0 else 2.0
			var phase_seconds := NEUTRALIZE_SECONDS if capture_progress < 1.0 else CAPTURE_SECONDS
			var seconds_to_boundary := (boundary - capture_progress) * phase_seconds / capture_power
			var progressed := minf(remaining, seconds_to_boundary)
			capture_progress += progressed * capture_power / phase_seconds
			remaining -= progressed
			if capture_progress >= 2.0 - 0.000001:
				_complete_capture()
				continue
			if capture_progress >= boundary - 0.000001:
				capture_progress = boundary
				_sync_capture_phase()
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
			var reversion_seconds := capture_progress / CAPTURE_PROGRESS_REVERT_PER_SECOND
			var reverted := minf(remaining, reversion_seconds)
			capture_progress -= reverted * CAPTURE_PROGRESS_REVERT_PER_SECOND
			remaining -= reverted
			if capture_progress <= 0.000001:
				_restore_previous_stable_state()
				return
			_sync_capture_phase()
			continue
		return


func is_stable_for(team_id: StringName) -> bool:
	return state == STABLE and owner_team_id == team_id


func previous_owner_team_id() -> StringName:
	return _previous_owner_team_id


func _complete_capture() -> void:
	capture_progress = 2.0
	owner_team_id = capturing_team_id
	capturing_team_id = &""
	capture_power = 0.0
	prior_building_ruined = true
	capture_revision += 1
	existing_buildings_enabled = false
	contested = false
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
	contested = false
	state = STABLE
	_hold_remaining = 0.0
	_phase_remaining = 0.0
	_is_reverting = false


func _sync_capture_phase() -> void:
	if capture_progress < 1.0:
		state = NEUTRALIZING
		owner_team_id = _previous_owner_team_id
		existing_buildings_enabled = _previous_existing_buildings_enabled
		_phase_remaining = (1.0 - capture_progress) * NEUTRALIZE_SECONDS
		return
	state = CAPTURING
	owner_team_id = &""
	existing_buildings_enabled = false
	_phase_remaining = (2.0 - capture_progress) * CAPTURE_SECONDS


func _normalize_capture_power(power: float) -> float:
	return clampf(power, 0.0, MAX_CAPTURE_POWER)


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
		"contested": contested,
		"hold_remaining": _hold_remaining,
		"phase_remaining": _phase_remaining,
	}
