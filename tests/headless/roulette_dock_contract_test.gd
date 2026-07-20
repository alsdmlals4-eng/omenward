# 하단 전술 도크와 3×3 룰렛 UI 계약을 검증한다.
extends SceneTree

const STAGE_HUD_SCENE_PATH := "res://scenes/ui/stage_hud.tscn"
const TUTORIAL_STAGE_PATH := "res://data/stages/tutorial_stage.tres"


func _init() -> void:
	call_deferred("_run")


func _run() -> void:
	var failures := PackedStringArray()
	var packed := load(STAGE_HUD_SCENE_PATH) as PackedScene
	_expect(packed != null, "stage HUD scene loads", failures)
	if packed != null:
		var hud := packed.instantiate()
		_expect(hud.get_node_or_null("BottomDock/RoulettePanel") != null, "bottom dock includes a roulette panel", failures)
		_expect(hud.get_node_or_null("BottomDock/TacticalPanel") != null, "bottom dock includes tactical skills", failures)
		_expect(hud.get_node_or_null("BottomDock/ShopPanel") != null, "bottom dock includes a shop section", failures)
		_expect(hud.get_node_or_null("BottomDock/BelluGuide") != null, "bottom dock includes Bellu guidance", failures)
		_expect(hud.get_node_or_null("BottomDock/RoulettePanel/Board/Cell0") != null, "roulette board includes its first cell", failures)
		_expect(hud.get_node_or_null("BottomDock/RoulettePanel/Board/Cell8") != null, "roulette board includes all nine cells", failures)
		_expect(hud.get_node_or_null("BottomDock/RoulettePanel/RowStatusLabel") != null, "roulette panel explains center-row matching and completed lines", failures)
		_expect(hud.get_node_or_null("NodeBuildPanel") != null, "HUD provides a contextual selected-node building panel", failures)
		_expect(hud.get_node_or_null("NodeBuildPanel/TowerButton") != null and hud.get_node_or_null("NodeBuildPanel/FarmButton") != null, "selected-node panel lists available building actions", failures)
		_expect(hud.get_node_or_null("TowerButton") == null and hud.get_node_or_null("FarmButton") == null, "raw immediate building buttons are removed", failures)
		_expect(hud.has_method("_refresh_roulette_dock"), "stage HUD refreshes the roulette dock", failures)
		await _assert_runtime_roulette_flow(hud, failures)
		hud.queue_free()
	_finish(failures)


func _assert_runtime_roulette_flow(hud: Control, failures: PackedStringArray) -> void:
	var stage_run_script := load("res://scripts/core/stage_run.gd") as GDScript
	var tutorial := load(TUTORIAL_STAGE_PATH) as Resource
	_expect(stage_run_script != null and tutorial != null, "roulette HUD runtime dependencies load", failures)
	if stage_run_script == null or tutorial == null:
		return
	var run: Variant = stage_run_script.new()
	run.start(tutorial, 1001)
	get_root().add_child(hud)
	await process_frame
	hud.bind_run(run)
	hud._on_spin_pressed()
	_expect(hud._pending_cards.size() == 9, "one roulette press fills all nine result cells", failures)
	_expect(hud.get_node("BottomDock/RoulettePanel/ReserveLabel").text.contains("9"), "roulette reserve displays nine stored results", failures)
	_expect(hud.get_node("BottomDock/RoulettePanel/RowStatusLabel").text.contains("중앙 적중"), "roulette HUD reports the center-line match", failures)
	hud._on_deploy_pressed(&"top")
	_expect(hud._pending_cards.size() == 8, "one lane deploy consumes exactly one stored result", failures)
	hud._on_construction_node_selected(&"home_top", &"front_a")
	_expect(hud.get_node("NodeBuildPanel").visible, "selecting a node opens the contextual build panel", failures)
	_expect(not hud.get_node("NodeBuildPanel/TowerButton").disabled, "available node enables its permitted building", failures)
	hud._on_building_pressed(&"tower")
	_expect(hud.get_node("NodeBuildPanel/TowerButton").disabled, "installed node disables repeat building", failures)
	hud.get_parent().remove_child(hud)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Roulette dock contracts passed")
		quit(0)
	else:
		printerr("Roulette dock contract failures:\n%s" % "\n".join(failures))
		quit(1)
