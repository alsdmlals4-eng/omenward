class_name WaveDirector
extends RefCounted

const WAVE_INTERVAL_SECONDS := 60.0
const OMEN_T30_SECONDS := 30.0
const OMEN_T15_SECONDS := 15.0
const OMEN_T5_SECONDS := 5.0

var stage: Variant
var active_combat_seconds := 0.0
var current_wave_number := 0
var _next_wave_index := 0
var _waves: Array = []


func _init(assigned_stage: Variant, assigned_waves: Array = []) -> void:
	stage = assigned_stage
	_waves = assigned_waves.duplicate() if not assigned_waves.is_empty() else (stage.waves.duplicate() if stage != null else [])


func advance(delta: float) -> Array:
	active_combat_seconds += maxf(0.0, delta)
	var emitted: Array = []
	while _next_wave_index < _waves.size():
		var wave: Variant = _waves[_next_wave_index]
		if active_combat_seconds + 0.000001 < float(_next_wave_index + 1) * WAVE_INTERVAL_SECONDS:
			break
		current_wave_number = wave.wave_number
		emitted.append(wave)
		_next_wave_index += 1
	return emitted


func current_wave() -> Variant:
	return wave_at(current_wave_number)


func next_wave() -> Variant:
	if _next_wave_index >= _waves.size():
		return null
	return _waves[_next_wave_index]


func wave_at(wave_number: int) -> Variant:
	for wave in _waves:
		if wave.wave_number == wave_number:
			return wave
	return null


func seconds_until_next_wave() -> float:
	var wave: Variant = next_wave()
	if wave == null:
		return 0.0
	return maxf(0.0, float(_next_wave_index + 1) * WAVE_INTERVAL_SECONDS - active_combat_seconds)


func is_exhausted() -> bool:
	return _next_wave_index >= _waves.size()


func wave_package_snapshot() -> Array:
	return _waves.duplicate()


func omen_phase() -> StringName:
	if next_wave() == null:
		return &"complete"
	var remaining := seconds_until_next_wave()
	if remaining <= 0.000001:
		return &"now"
	if remaining <= OMEN_T5_SECONDS:
		return &"t5"
	if remaining <= OMEN_T15_SECONDS:
		return &"t15"
	if remaining <= OMEN_T30_SECONDS:
		return &"t30"
	return &"countdown"


func omen_seconds_remaining() -> float:
	var wave: Variant = next_wave()
	if wave == null:
		return 0.0
	return maxf(0.0, seconds_until_next_wave() - float(wave.omen_lead_seconds))
