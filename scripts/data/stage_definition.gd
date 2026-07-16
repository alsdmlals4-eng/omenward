class_name StageDefinition
extends Resource

const StageManifest = preload("res://scripts/core/stage_manifest.gd")
const WaveDefinition = preload("res://scripts/data/wave_definition.gd")

@export var stage_id: StringName
@export var starting_gold := 160
@export var starting_food_cap := 12
@export var tutorial_stage := false
@export var waves: Array[WaveDefinition] = []


func build_manifest(seed: int) -> StageManifest:
	var manifest := StageManifest.new()
	manifest.stage_id = str(stage_id)
	manifest.seed = seed
	manifest.starting_gold = starting_gold
	manifest.starting_food_cap = starting_food_cap
	manifest.tutorial_stage = tutorial_stage
	manifest.wave_count = waves.size()
	manifest.waves = waves.map(func(wave): return wave.to_dictionary())
	return manifest
