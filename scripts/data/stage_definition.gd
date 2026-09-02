class_name StageDefinition
extends Resource

const StageManifest = preload("res://scripts/core/stage_manifest.gd")
const WaveDefinition = preload("res://scripts/data/wave_definition.gd")
const FrontMapDefinition = preload("res://scripts/data/front_map_definition.gd")

@export var stage_id: StringName
@export var starting_gold := 160
@export var starting_food_cap := 12
@export var base_max_health: float = 0.0
@export var tutorial_stage := false
@export var waves: Array[WaveDefinition] = []
@export var front_maps: Array[FrontMapDefinition] = []


func build_manifest(seed: int) -> StageManifest:
	var manifest := StageManifest.new()
	manifest.stage_id = str(stage_id)
	manifest.seed = seed
	manifest.starting_gold = starting_gold
	manifest.starting_food_cap = starting_food_cap
	manifest.base_max_health = base_max_health
	manifest.tutorial_stage = tutorial_stage
	manifest.wave_count = waves.size()
	for wave in waves:
		manifest.waves.append(wave.to_dictionary())
	for front_map in front_maps:
		manifest.front_maps.append(front_map.to_dictionary())
	return manifest


func front_map_at(index: int) -> FrontMapDefinition:
	if index < 0 or index >= front_maps.size():
		return null
	return front_maps[index]
