class_name FrontMapDefinition
extends Resource

@export var map_id: StringName
@export var display_name := ""
@export var terrain_id: StringName
@export var wave_first := 0
@export var wave_last := 0


func is_valid() -> bool:
	return map_id != &"" and not display_name.is_empty() and terrain_id != &"" and wave_first > 0 and wave_last >= wave_first


func owns_wave(wave_number: int) -> bool:
	return wave_number >= wave_first and wave_number <= wave_last


func to_dictionary() -> Dictionary:
	return {
		"map_id": str(map_id),
		"display_name": display_name,
		"terrain_id": str(terrain_id),
		"wave_first": wave_first,
		"wave_last": wave_last,
	}
