class_name WaveDefinition
extends Resource

const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")

@export var wave_number: int
@export var omen_lead_seconds: float = 5.0
@export var spawns: Array[UnitSpawnDefinition] = []
@export var boss_kind: StringName
@export var is_overtime := false


func to_dictionary() -> Dictionary:
	return {
		"wave_number": wave_number,
		"omen_lead_seconds": omen_lead_seconds,
		"spawns": spawns.map(func(spawn): return spawn.to_dictionary()),
		"boss_kind": str(boss_kind),
		"is_overtime": is_overtime,
	}
