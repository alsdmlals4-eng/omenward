class_name StageManifest
extends RefCounted

var stage_id: String
var seed: int
var archetype_ids: Array[String] = []
var random_roll: int
var input_log: Array[Dictionary] = []

func to_json() -> String:
	return JSON.stringify({
		"archetype_ids": archetype_ids,
		"input_log": input_log,
		"random_roll": random_roll,
		"seed": seed,
		"stage_id": stage_id,
	})
