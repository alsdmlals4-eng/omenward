# 내정·룰렛·전선 탭은 화면 상태이며 command phase를 우회하지 않는다.
extends SceneTree

const RUN_COMMAND_SCREEN_PATH := "res://scenes/ui/run_command_screen.tscn"
const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")

const REGULAR_STAGE_PATH := "res://data/stages/regular_stage.tres"


func _init() -> void:
	var failures := PackedStringArray()
	var screen := (load(RUN_COMMAND_SCREEN_PATH) as PackedScene).instantiate()
	_expect(screen.get_node_or_null("TabRail/DomesticTab") is Button, "domestic tab exists", failures)
	_expect(screen.get_node_or_null("TabRail/RouletteTab") is Button, "roulette tab exists", failures)
	_expect(screen.get_node_or_null("TabRail/FrontTab") is Button, "front tab exists", failures)
	_expect(screen.get_node_or_null("LowerDeck/RouletteReadyPanel/StartSpinButton") is Button, "roulette tab has a ready-state spin control before a board exists", failures)
	_expect(screen.get_node_or_null("LowerDeck/FrontReadyPanel/RouteSummary") is Label, "front tab has an always-readable route summary before deployment", failures)
	_expect(screen.has_method("visible_work_surface_id"), "screen exposes one active work surface", failures)
	_expect(screen.has_method("set_active_tab"), "screen can select a visible tab", failures)
	var run: Variant = _new_run()
	_expect(run.has_method("set_active_tab"), "StageRun owns tab state independently from command phase", failures)
	if run.has_method("set_active_tab"):
		var phase_before: StringName = run.command_phase
		_expect(run.set_active_tab(&"front"), "front tab can be selected for contextual inspection", failures)
		_expect(run.command_phase == phase_before, "tab selection does not alter command phase", failures)
		_expect(not run.set_active_tab(&"invalid"), "unknown tabs are rejected", failures)
	screen.free()
	_finish(failures)


func _new_run() -> Variant:
	var progression := StageProgression.new()
	progression.regular_unlocked = true
	var run := StageRun.new(progression)
	run.start(ResourceLoader.load(REGULAR_STAGE_PATH), 39003)
	return run


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Run Command tab contracts passed")
		quit(0)
	else:
		printerr("Run Command tab contract failures:\n%s" % "\n".join(failures))
		quit(1)
