extends SceneTree

const TUTORIAL_STAGE_PATH := "res://data/stages/tutorial_stage.tres"
const REGULAR_STAGE_PATH := "res://data/stages/regular_stage.tres"


func _init() -> void:
	var failures := PackedStringArray()
	var tutorial := ResourceLoader.load(TUTORIAL_STAGE_PATH)
	var regular := ResourceLoader.load(REGULAR_STAGE_PATH)

	_expect(tutorial != null, "tutorial stage resource must load", failures)
	_expect(regular != null, "regular stage resource must load", failures)
	if tutorial != null:
		_expect(_waves(tutorial).size() == 4, "tutorial has four waves", failures)
	if regular != null:
		var waves := _waves(regular)
		_expect(waves.size() == 20, "regular stage has W1 through W20", failures)
		if waves.size() >= 20:
			_expect(waves[14].boss_kind == &"legendary", "W15 is legendary", failures)
			_expect(waves[19].boss_kind == &"mythic", "W20 is mythic", failures)

	if failures.is_empty():
		print("Stage data contract checks passed")
		quit(0)
	else:
		printerr("Stage data contract failures:\n%s" % "\n".join(failures))
		quit(1)


func _waves(stage: Resource) -> Array:
	return stage.get("waves") as Array


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)
