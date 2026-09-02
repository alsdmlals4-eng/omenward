extends SceneTree

const RUN_COMMAND_SCREEN_PATH := "res://scenes/ui/run_command_screen.tscn"
const MarchMinimapView = preload("res://scripts/ui/march_minimap_view.gd")
const BattleFocusView = preload("res://scripts/ui/battle_focus_view.gd")
const BattlefieldView = preload("res://scripts/battle/battlefield_view.gd")
const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")

const REGULAR_STAGE_PATH := "res://data/stages/regular_stage.tres"


func _init() -> void:
	call_deferred("_run")


func _run() -> void:
	var failures: Array[String] = []
	var screen := (load(RUN_COMMAND_SCREEN_PATH) as PackedScene).instantiate()
	var battle_focus := screen.get_node_or_null("BattleFocusViewport")
	var march_minimap := screen.get_node_or_null("MarchMinimap")
	_expect(battle_focus is Control, "Run Command exposes a primary battle focus viewport", failures)
	_expect(march_minimap is Control, "Run Command exposes a compact march minimap", failures)
	_expect(screen.get_node_or_null("StrategicMap") == null, "wide strategic map is not retained as the player-facing surface", failures)
	_expect(screen.get_node_or_null("Fronts") == null, "legacy three-card front hierarchy is absent", failures)
	if battle_focus != null:
		_expect(battle_focus.has_method("bind_run"), "battle focus reads StageRun state", failures)
	if march_minimap != null:
		_expect(march_minimap.has_method("bind_run"), "minimap reads StageRun state", failures)
	screen.free()
	_test_single_route_projection(failures)
	await _test_review_next_map_cta(failures)
	_test_battlefield_alignment(failures)
	_finish(failures)


func _test_single_route_projection(failures: Array[String]) -> void:
	var map := MarchMinimapView.new()
	var run: Variant = _new_run(4101)
	map.bind_run(run)
	_expect(map.front_count() == 1, "minimap exposes exactly one active front", failures)
	_expect(map.fixed_tower_count() == 1, "minimap exposes exactly one fixed tower", failures)
	_expect(map.is_read_only(), "minimap cannot become a second interactive battlefield", failures)
	_expect(map.route_state_for(&"top").is_empty(), "legacy top route is not projected", failures)
	var route := map.route_state_for(&"front")
	_expect(route.has_all(["ward_forward", "clash", "veil_forward"]), "front projection retains the three capturable anchors", failures)
	_expect(map.has_method("current_sector_id"), "minimap exposes the currently emphasized route sector", failures)
	_expect(map.has_method("front_map_entry_for"), "minimap exposes read-only sequential map state", failures)
	if map.has_method("current_sector_id"):
		_expect(map.current_sector_id() == &"ward_citadel", "opening sector emphasizes the first active battlefield map", failures)
	if map.has_method("front_map_entry_for"):
		_expect(StringName(map.front_map_entry_for(&"ward_citadel").get("state", &"")) == &"current", "opening map is current", failures)
		_expect(StringName(map.front_map_entry_for(&"ward_forward").get("state", &"")) == &"locked", "second map starts locked", failures)
	var battle_focus := BattleFocusView.new()
	battle_focus.bind_run(run)
	_expect(battle_focus.current_sector_id() == &"ward_citadel", "battle focus and minimap start at the same active battlefield map", failures)
	_expect(battle_focus.has_method("current_terrain_id"), "battle focus resolves a terrain consumer key from the active map package", failures)
	if battle_focus.has_method("current_terrain_id"):
		_expect(battle_focus.current_terrain_id() == &"ward_citadel", "opening battle focus resolves Ward Citadel terrain rather than a guessed capture sector", failures)
	_expect(battle_focus.has_method("displayed_unit_count"), "battle focus exposes its bounded live formation projection", failures)
	battle_focus.free()
	map.free()


func _test_review_next_map_cta(failures: Array[String]) -> void:
	var screen := (load(RUN_COMMAND_SCREEN_PATH) as PackedScene).instantiate()
	var run: Variant = _new_run(4103)
	root.add_child(screen)
	await process_frame
	screen.bind_run(run)
	run.submit_command({"action": "stage_victory"})
	screen.call("_refresh")
	var next_button := screen.get_node_or_null("LowerDeck/ReviewPanel/NextFrontMapButton") as Button
	var retry_button := screen.get_node_or_null("LowerDeck/ReviewPanel/RetryButton") as Button
	_expect(next_button != null and next_button.visible, "non-final map review shows the explicit next-front CTA", failures)
	_expect(retry_button != null and not retry_button.visible, "non-final map review does not mislabel progression as a full Stage retry", failures)
	screen.call("_on_next_front_map_pressed")
	_expect(run.front_map_index == 1 and run.command_phase == run.PREPARE, "review CTA performs the one-way next-map handoff", failures)
	screen.free()
	await process_frame


func _test_battlefield_alignment(failures: Array[String]) -> void:
	var battlefield_view := BattlefieldView.new()
	_expect(battlefield_view.has_method("world_position_for"), "battlefield exposes one route position transform", failures)
	if battlefield_view.has_method("world_position_for"):
		var clash: Vector2 = battlefield_view.world_position_for(&"front", 50.0)
		_expect(absf(clash.x - 480.0) < 8.0, "single clash is centered in the battle focus route", failures)
		_expect(battlefield_view.world_position_for(&"top", 50.0) == clash, "legacy front IDs have no separate world row", failures)
	battlefield_view.free()


func _new_run(seed: int) -> Variant:
	var progression := StageProgression.new()
	progression.regular_unlocked = true
	var run := StageRun.new(progression)
	run.start(ResourceLoader.load(REGULAR_STAGE_PATH), seed)
	return run


func _expect(condition: bool, message: String, failures: Array[String]) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("PASS: battle focus and march minimap contract")
		quit(0)
	else:
		printerr("FAIL: battle focus and march minimap contract\n- " + "\n- ".join(failures))
		quit(1)
