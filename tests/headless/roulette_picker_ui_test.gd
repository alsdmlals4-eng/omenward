# 룰렛 선택 UI가 게임 규칙과 분리된 표시 상태를 유지하는지 검증한다.
extends SceneTree

const RUN_COMMAND_SCREEN_PATH := "res://scenes/ui/run_command_screen.tscn"
const BATTLEFIELD_SCENE_PATH := "res://scenes/battle/battlefield.tscn"
const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")
const REGULAR_STAGE_PATH := "res://data/stages/regular_stage.tres"

var failures: Array[String] = []


func _init() -> void:
	call_deferred("_run")


func _run() -> void:
	var battlefield := (load(BATTLEFIELD_SCENE_PATH) as PackedScene).instantiate()
	var backdrop := battlefield.get_node_or_null("Backdrop") as Sprite2D
	_expect(backdrop != null, "battlefield owns a project backdrop node", failures)
	if backdrop != null:
		_expect(backdrop.scale.x >= 0.64 and backdrop.scale.y >= 0.64, "battlefield backdrop is enlarged beyond a distant-map scale", failures)
	battlefield.queue_free()
	var screen := (load(RUN_COMMAND_SCREEN_PATH) as PackedScene).instantiate()
	var result_list := screen.get_node_or_null("LowerDeck/RoulettePanel/ResultList")
	_expect(result_list is GridContainer, "roulette exposes all nine inspected results as a compact grid", failures)
	if result_list is GridContainer:
		_expect(result_list.columns == 5, "roulette result inspection compresses into two visible rows", failures)
	var battle_focus := screen.get_node_or_null("BattleFocusViewport") as Control
	var march_minimap := screen.get_node_or_null("MarchMinimap") as Control
	_expect(battle_focus != null, "battle focus is the primary visual surface", failures)
	_expect(march_minimap != null, "march minimap retains route context", failures)
	_expect(screen.get_node_or_null("StrategicMap") == null, "wide strategic map is removed from the screen", failures)
	if march_minimap != null:
		_expect(march_minimap.has_method("route_state_for"), "minimap owns a read-only route-state projection", failures)
		_expect(march_minimap.get_rect().size.x < 360.0, "minimap is compact rather than another wide battlefield", failures)
	if battle_focus != null and march_minimap != null:
		_expect(battle_focus.get_rect().size.x > march_minimap.get_rect().size.x * 1.5, "battle focus remains visually dominant", failures)
	_expect(screen.get_node_or_null("Fronts") == null, "legacy three-card front hierarchy is not retained", failures)
	_expect(screen.has_method("select_roulette_tile"), "roulette screen exposes UI-only tile selection", failures)
	_expect(screen.has_method("selected_roulette_tile_index"), "roulette screen exposes current selected tile index", failures)
	if screen.has_method("select_roulette_tile"):
		screen.select_roulette_tile(4)
	if screen.has_method("selected_roulette_tile_index"):
		_expect(screen.selected_roulette_tile_index() == 4, "roulette selection stores the inspected tile only", failures)
	var run: Variant = _new_run()
	root.add_child(screen)
	await process_frame
	screen.bind_run(run)
	_expect(run.set_active_tab(&"roulette"), "roulette tab accepts the compact inspection surface", failures)
	run.begin_roulette_session({"seed": 2})
	screen.call("_refresh")
	await process_frame
	var viewport_bottom := 540.0
	for path in [
		NodePath("LowerDeck/RoulettePanel/BoardFrame"),
		NodePath("LowerDeck/RoulettePanel/BoardGrid"),
		NodePath("LowerDeck/RoulettePanel/ArrowControls"),
		NodePath("LowerDeck/RoulettePanel/ResultList"),
		NodePath("LowerDeck/RoulettePanel/LockResultButton"),
		NodePath("LowerDeck/RoulettePanel/ConfirmResultButton"),
	]:
		var control := screen.get_node_or_null(path) as Control
		_expect(control != null, "roulette owns required compact control %s" % path, failures)
		if control != null:
			_expect(control.get_global_rect().end.y <= viewport_bottom, "roulette control remains inside the 960×540 viewport: %s" % path, failures)
	if result_list is GridContainer:
		_expect(result_list.get_child_count() == 9, "roulette renders all nine inspection choices", failures)
		for entry in result_list.get_children():
			if entry is Control:
				_expect((entry as Control).get_global_rect().end.y <= viewport_bottom, "each roulette result choice stays clickable inside the viewport", failures)
	screen.queue_free()
	await process_frame
	_finish(failures)


func _new_run() -> Variant:
	var progression := StageProgression.new()
	progression.regular_unlocked = true
	var run := StageRun.new(progression)
	run.start(ResourceLoader.load(REGULAR_STAGE_PATH), 4202)
	return run


func _expect(condition: bool, message: String, failures: Array[String]) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("Roulette picker UI checks passed")
		quit(0)
	else:
		printerr("Roulette picker UI failures:\n%s" % "\n".join(failures))
		quit(1)
