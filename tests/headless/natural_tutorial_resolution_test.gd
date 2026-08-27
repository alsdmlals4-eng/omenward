# 병력 없이 시작한 튜토리얼 전투가 실제 전투 결과로 REVIEW에 도달하는지를 검증한다.
extends SceneTree

const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")
const TUTORIAL_STAGE_PATH := "res://data/stages/tutorial_stage.tres"
const MAX_SIMULATED_SECONDS := 2400.0


func _init() -> void:
	var failures := PackedStringArray()
	var tutorial := ResourceLoader.load(TUTORIAL_STAGE_PATH)
	var run: Variant = StageRun.new(StageProgression.new())
	run.start(tutorial, 8601)
	_expect(run.begin_battle(), "empty-reward tutorial can enter BATTLE", failures)
	var simulated_seconds := 0.0
	while run.result_state == run.RUNNING and simulated_seconds < MAX_SIMULATED_SECONDS:
		run.advance(1.0)
		simulated_seconds += 1.0
	_expect(run.current_wave == 4, "the live tutorial schedule emits all four declared waves", failures)
	_expect(run.result_state == run.DEFEAT, "an undefended tutorial resolves through the real base-destruction defeat path", failures)
	_expect(run.command_phase == run.REVIEW, "a natural battle result transitions to REVIEW", failures)
	_expect(simulated_seconds < MAX_SIMULATED_SECONDS, "natural resolution completes within the bounded simulation window", failures)
	_finish(failures)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Natural tutorial resolution passed")
		quit(0)
	else:
		printerr("Natural tutorial resolution failures:\n%s" % "\n".join(failures))
		quit(1)
