extends SceneTree

const RUN_COMMAND_SCREEN_PATH := "res://scenes/ui/run_command_screen.tscn"
const BATTLEFIELD_SCENE_PATH := "res://scenes/battle/battlefield.tscn"
const WIDE_CONNECTED_TERRAIN_PATH := "res://assets/art/battlefield/wide_connected_strategic_front_terrain_v1.png"
const StrategicMapView = preload("res://scripts/ui/strategic_map_view.gd")
const BattlefieldView = preload("res://scripts/battle/battlefield_view.gd")
const UnitView = preload("res://scripts/units/unit_view.gd")
const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")
const REGULAR_STAGE_PATH := "res://data/stages/regular_stage.tres"


func _init() -> void:
	var failures: Array[String] = []
	var screen := (load(RUN_COMMAND_SCREEN_PATH) as PackedScene).instantiate()
	var strategic_map := screen.get_node_or_null("StrategicMap")
	_expect(strategic_map is Control, "Run Command exposes one primary strategic map", failures)
	_expect(screen.get_node_or_null("Fronts") == null, "three per-front progress-card minimaps are removed", failures)
	if strategic_map != null:
		_expect(strategic_map.has_method("bind_run"), "strategic map reads existing StageRun state", failures)
		_expect(strategic_map.get_node_or_null("BuildingRoster") == null, "strategic map contains no building roster control", failures)
	screen.free()
	_test_read_only_state_projection(failures)
	_test_battlefield_alignment(failures)
	_test_unit_readability_scale(failures)
	_test_approved_terrain_consumer(failures)
	_finish(failures)


func _test_read_only_state_projection(failures: Array[String]) -> void:
	var progression := StageProgression.new()
	progression.regular_unlocked = true
	var run := StageRun.new(progression)
	run.start(ResourceLoader.load(REGULAR_STAGE_PATH), 4101)
	var map := StrategicMapView.new()
	map.bind_run(run)
	_expect(map.front_count() == 3, "strategic map retains exactly three shared fronts", failures)
	_expect(map.fixed_tower_count() == 3, "strategic map presents one fixed tower per shared front", failures)
	var before_gold: int = int(run.economy.gold)
	var top_state := map.route_state_for(&"top")
	_expect(top_state.get("tower_owner_team_id", &"") == &"lumern" and bool(top_state.get("tower_active", false)), "top route reports its Ward-owned active tower", failures)
	_expect(top_state.has("ward_forward") and top_state.has("clash") and top_state.has("veil_forward"), "route projection exposes forward and clash ownership anchors", failures)
	_expect(int(run.economy.gold) == before_gold, "route inspection does not mutate economy or battle state", failures)
	map.free()


func _test_battlefield_alignment(failures: Array[String]) -> void:
	var battlefield_view := BattlefieldView.new()
	_expect(battlefield_view.has_method("world_position_for"), "battlefield exposes one strategic-map position transform", failures)
	if not battlefield_view.has_method("world_position_for"):
		battlefield_view.free()
		return
	var clash: Vector2 = battlefield_view.world_position_for(&"middle", 50.0)
	_expect(absf(clash.x - 480.0) < 8.0 and absf(clash.y - 186.0) < 8.0, "middle clash is centered in the strategic map", failures)
	_expect(battlefield_view.world_position_for(&"top", 30.0).y < clash.y, "top route remains above the middle route", failures)
	_expect(battlefield_view.world_position_for(&"bottom", 30.0).y > clash.y, "bottom route remains below the middle route", failures)
	battlefield_view.free()


func _test_unit_readability_scale(failures: Array[String]) -> void:
	_expect(
		UnitView.IDLE_DISPLAY_HEIGHT >= 68.0,
		"battlefield unit sprites are large enough to remain silhouette-readable against the wide terrain",
		failures,
	)


func _test_approved_terrain_consumer(failures: Array[String]) -> void:
	var battlefield := (load(BATTLEFIELD_SCENE_PATH) as PackedScene).instantiate()
	var backdrop := battlefield.get_node_or_null("Backdrop") as Sprite2D
	_expect(backdrop != null and backdrop.texture != null, "battlefield has a terrain backdrop texture", failures)
	if backdrop != null and backdrop.texture != null:
		_expect(
			backdrop.texture.resource_path == WIDE_CONNECTED_TERRAIN_PATH,
			"battlefield uses the approved wide connected terrain rather than the legacy baked backdrop",
			failures,
		)
	battlefield.free()


func _expect(condition: bool, message: String, failures: Array[String]) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("PASS: strategic-map UI contract")
		quit(0)
	else:
		printerr("FAIL: strategic-map UI contract\n- " + "\n- ".join(failures))
		quit(1)
