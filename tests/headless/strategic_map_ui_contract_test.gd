extends SceneTree

const RUN_COMMAND_SCREEN_PATH := "res://scenes/ui/run_command_screen.tscn"
const StrategicMapView = preload("res://scripts/ui/strategic_map_view.gd")
const BattlefieldView = preload("res://scripts/battle/battlefield_view.gd")
const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")

const REGULAR_STAGE_PATH := "res://data/stages/regular_stage.tres"


func _init() -> void:
	var failures: Array[String] = []
	var screen := (load(RUN_COMMAND_SCREEN_PATH) as PackedScene).instantiate()
	var strategic_map := screen.get_node_or_null("StrategicMap")
	_expect(strategic_map is Control, "Run Command exposes one primary front map", failures)
	_expect(screen.get_node_or_null("Fronts") == null, "legacy three-card front hierarchy is absent", failures)
	if strategic_map != null:
		_expect(strategic_map.has_method("bind_run"), "map reads StageRun state", failures)
	screen.free()
	_test_single_route_projection(failures)
	_test_battlefield_alignment(failures)
	_finish(failures)


func _test_single_route_projection(failures: Array[String]) -> void:
	var map := StrategicMapView.new()
	var run: Variant = _new_run(4101)
	map.bind_run(run)
	_expect(map.front_count() == 1, "map exposes exactly one active front", failures)
	_expect(map.fixed_tower_count() == 1, "map exposes exactly one fixed tower", failures)
	_expect(map.route_state_for(&"top").is_empty(), "legacy top route is not projected", failures)
	var route := map.route_state_for(&"front")
	_expect(route.has_all(["ward_forward", "clash", "veil_forward"]), "front projection retains the three capturable anchors", failures)
	_expect(map.has_method("current_sector_id"), "map exposes the currently emphasized route sector", failures)
	if map.has_method("current_sector_id"):
		_expect(map.current_sector_id() == &"ward_forward", "opening sector emphasizes the unheld Ward Forward objective", failures)
	_expect(map.has_method("unit_marker_texture_for"), "strategic map exposes approved unit-art markers for live front readability", failures)
	if map.has_method("unit_marker_texture_for"):
		_expect(map.unit_marker_texture_for(&"lumern", &"shield_guard") != null, "Lumern Shield Guard marker uses approved runtime art", failures)
		_expect(map.unit_marker_texture_for(&"veil", &"shield_guard") != null, "Veil Shield Guard marker uses approved runtime art", failures)
		_expect(map.unit_marker_texture_for(&"veil", &"archer") != null, "Veil Archer marker reuses the approved unit-art family instead of a primitive", failures)
		_expect(map.unit_marker_texture_for(&"veil", &"assassin") != null, "Veil Assassin marker reuses the approved unit-art family instead of a primitive", failures)
	_expect(map.has_method("front_unit_marker_offset_for"), "strategic map arranges units that share one route position as a readable formation", failures)
	if map.has_method("front_unit_marker_offset_for"):
		_expect(map.front_unit_marker_offset_for(0) != map.front_unit_marker_offset_for(1), "formation offsets first and second units", failures)
		_expect(map.front_unit_marker_offset_for(1) != map.front_unit_marker_offset_for(2), "formation offsets second and third units", failures)
	map.free()


func _test_battlefield_alignment(failures: Array[String]) -> void:
	var battlefield_view := BattlefieldView.new()
	_expect(battlefield_view.has_method("world_position_for"), "battlefield exposes one route position transform", failures)
	if battlefield_view.has_method("world_position_for"):
		var clash: Vector2 = battlefield_view.world_position_for(&"front", 50.0)
		_expect(absf(clash.x - 480.0) < 8.0, "single clash is centered in the wide front", failures)
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
		print("PASS: single-front strategic map contract")
		quit(0)
	else:
		printerr("FAIL: single-front strategic map contract\n- " + "\n- ".join(failures))
		quit(1)
