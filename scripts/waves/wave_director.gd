class_name WaveDirector
extends RefCounted

const WAVE_INTERVAL_SECONDS := 60.0

var stage: Variant
var active_combat_seconds := 0.0
var current_wave_number := 0
var _next_wave_index := 0


func _init(assigned_stage: Variant) -> void:
	stage = assigned_stage


func advance(delta: float) -> Array:
	active_combat_seconds += maxf(0.0, delta)
	var emitted: Array = []
	while _next_wave_index < stage.waves.size():
		var wave: Variant = stage.waves[_next_wave_index]
		if active_combat_seconds + 0.000001 < float(wave.wave_number) * WAVE_INTERVAL_SECONDS:
			break
		current_wave_number = wave.wave_number
		emitted.append(wave)
		_next_wave_index += 1
	return emitted


func current_wave() -> Variant:
	return wave_at(current_wave_number)


func wave_at(wave_number: int) -> Variant:
	for wave in stage.waves:
		if wave.wave_number == wave_number:
			return wave
	return null


func omen_seconds_remaining() -> float:
	if _next_wave_index >= stage.waves.size():
		return 0.0
	var next_wave: Variant = stage.waves[_next_wave_index]
	return maxf(0.0, float(next_wave.wave_number) * WAVE_INTERVAL_SECONDS - float(next_wave.omen_lead_seconds) - active_combat_seconds)
