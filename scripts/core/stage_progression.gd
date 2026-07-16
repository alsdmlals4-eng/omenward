class_name StageProgression
extends RefCounted

var tutorial_completed := false
var regular_unlocked := false


func can_start(stage: Variant) -> bool:
	return bool(stage.tutorial_stage) or regular_unlocked


func record_victory(stage: Variant) -> void:
	if stage.tutorial_stage:
		tutorial_completed = true
		regular_unlocked = true
