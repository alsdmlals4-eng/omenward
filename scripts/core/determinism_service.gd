class_name DeterminismService
extends RefCounted

var seed: int
var _rng := RandomNumberGenerator.new()

func _init(seed_value: int) -> void:
	seed = seed_value
	_rng.seed = seed

func create_stage_manifest(stage_id: String, archetype_ids: Array[String]) -> StageManifest:
	var manifest := StageManifest.new()
	manifest.stage_id = stage_id
	manifest.seed = seed
	manifest.archetype_ids = archetype_ids.duplicate()
	manifest.archetype_ids.sort()
	manifest.random_roll = _rng.randi()
	return manifest
