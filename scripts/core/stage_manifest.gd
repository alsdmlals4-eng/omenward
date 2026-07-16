class_name StageManifest
extends RefCounted

var stage_id: String
var seed: int
var archetype_ids: Array[String] = []
var random_roll: int
var starting_gold: int
var starting_food_cap: int
var tutorial_stage := false
var wave_count: int
var waves: Array[Dictionary] = []
var input_log: Array[Dictionary] = []

func to_json() -> String:
	return JSON.stringify({
		"archetype_ids": archetype_ids,
		"input_log": input_log,
		"random_roll": random_roll,
		"seed": seed,
		"stage_id": stage_id,
		"starting_food_cap": starting_food_cap,
		"starting_gold": starting_gold,
		"tutorial_stage": tutorial_stage,
		"wave_count": wave_count,
		"waves": waves,
	})
