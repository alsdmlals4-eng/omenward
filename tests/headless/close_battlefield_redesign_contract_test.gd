# 새 단일 전장 자산과 통행-안전 지형 배치를 정적·기하 계약으로 검증한다.
extends SceneTree

const BattleFocusView = preload("res://scripts/ui/battle_focus_view.gd")

const BATTLE_FOCUS_SOURCE_PATH := "res://scripts/ui/battle_focus_view.gd"
const RUN_COMMAND_SCENE_PATH := "res://scenes/ui/run_command_screen.tscn"
const MAIN_SCENE_PATH := "res://scenes/main/main.tscn"
const SCENE_BINDER_SOURCE_PATH := "res://scripts/presentation/scene_binder.gd"
const FOUNDATION_PATH := "res://assets/art/battlefield/omenward_close_single_front_foundation_v1.png"
const TERRAIN_PROP_PATHS := [
	"res://assets/art/battlefield/props/omenward_lumern_low_slab_cluster_v1.png",
	"res://assets/art/battlefield/props/omenward_lumern_meadow_bank_v1.png",
	"res://assets/art/battlefield/props/omenward_lumern_blue_flower_bank_v1.png",
	"res://assets/art/battlefield/props/omenward_veil_rubble_v1.png",
	"res://assets/art/battlefield/props/omenward_veil_crystal_cluster_v1.png",
	"res://assets/art/battlefield/props/omenward_veil_thorn_brush_v1.png",
]
const UNIT_TRAVEL_Y_MIN_RATIO := 0.36
const UNIT_TRAVEL_Y_MAX_RATIO := 0.80


func _init() -> void:
	var failures := PackedStringArray()
	var source := FileAccess.get_file_as_string(BATTLE_FOCUS_SOURCE_PATH)
	_expect(not source.contains("ward_veil_three_lane_backdrop_v1.png"), "battle focus stops sampling the legacy three-front backdrop", failures)
	_expect(not source.contains("_draw_clash_focus"), "battle focus draws no standalone clash-circle marker over the unit travel field", failures)
	_expect(source.contains("omenward_close_single_front_foundation_v1.png"), "battle focus preloads the approved neutral foundation", failures)
	_expect(source.contains("omenward_lumern_low_slab_cluster_v1.png"), "battle focus preloads an independent Lumern terrain prop", failures)
	_expect(source.contains("omenward_veil_crystal_cluster_v1.png"), "battle focus preloads an independent Veil terrain prop", failures)
	_expect(source.contains("LUMERN_PROP_MAX_X_RATIO := 0.36"), "Lumern terrain stays before the Lumern territory threshold", failures)
	_expect(source.contains("VEIL_PROP_MIN_X_RATIO := 0.64"), "Veil terrain stays after the Veil territory threshold", failures)
	_expect(source.contains("UNIT_TRAVEL_Y_MIN_RATIO := 0.36"), "battle focus declares the top edge of the unit-travel corridor", failures)
	_expect(source.contains("UNIT_TRAVEL_Y_MAX_RATIO := 0.80"), "battle focus declares the bottom edge of the unit-travel corridor", failures)
	_expect(FileAccess.file_exists(FOUNDATION_PATH), "approved foundation is copied into the project runtime path", failures)
	for terrain_prop_path in TERRAIN_PROP_PATHS:
		_expect(FileAccess.file_exists(terrain_prop_path), "%s is copied into the project runtime path" % terrain_prop_path, failures)
	_test_single_active_battle_renderer(failures)
	_test_scene_layout(failures)
	_test_prop_geometry(failures)
	_finish(failures)


func _test_scene_layout(failures: PackedStringArray) -> void:
	var scene_text := FileAccess.get_file_as_string(RUN_COMMAND_SCENE_PATH)
	_expect(scene_text.contains("offset_left = 16.0\noffset_top = 62.0\noffset_right = 702.0"), "battle focus uses the full 686px-wide left battle surface", failures)
	_expect(scene_text.contains('[node name="TopTabRail" type="HBoxContainer" parent="TopBar"]'), "three work-surface tabs live inside the top command rail", failures)
	_expect(not scene_text.contains('[node name="TabRail" type="VBoxContainer" parent="."]'), "vertical tab rail no longer steals battle width", failures)
	_expect(scene_text.contains('[node name="MarchMinimap" type="Control" parent="."]'), "the narrow march minimap remains a separate right-side surface", failures)


func _test_single_active_battle_renderer(failures: PackedStringArray) -> void:
	var main_scene := FileAccess.get_file_as_string(MAIN_SCENE_PATH)
	var scene_binder := FileAccess.get_file_as_string(SCENE_BINDER_SOURCE_PATH)
	_expect(main_scene.contains('[node name="Battlefield" parent="." unique_id=617805723 instance=ExtResource("2_battlefield")]\nvisible = false'), "legacy root battlefield renderer is hidden behind the close battle surface", failures)
	_expect(not scene_binder.contains("battlefield.bind_run(run)"), "scene binder does not activate the legacy battlefield renderer for the current run", failures)


func _test_prop_geometry(failures: PackedStringArray) -> void:
	var battle_focus := BattleFocusView.new()
	_expect(battle_focus.has_method("terrain_prop_layout"), "battle focus exposes a deterministic terrain-prop layout", failures)
	_expect(battle_focus.has_method("is_terrain_prop_placement_allowed"), "battle focus validates territory-side and travel-corridor safety before drawing a prop", failures)
	if not battle_focus.has_method("terrain_prop_layout") or not battle_focus.has_method("is_terrain_prop_placement_allowed"):
		battle_focus.free()
		return
	var combat_rect := Rect2(Vector2.ZERO, Vector2(686.0, 292.0))
	var travel_rect := Rect2(
		Vector2(0.0, combat_rect.size.y * UNIT_TRAVEL_Y_MIN_RATIO),
		Vector2(combat_rect.size.x, combat_rect.size.y * (UNIT_TRAVEL_Y_MAX_RATIO - UNIT_TRAVEL_Y_MIN_RATIO))
	)
	var layout: Array = battle_focus.terrain_prop_layout(combat_rect)
	_expect(layout.size() == TERRAIN_PROP_PATHS.size(), "all six locked terrain props receive a deterministic edge placement", failures)
	for placement in layout:
		var prop_rect: Rect2 = placement.get("rect", Rect2())
		var x_ratio := float(placement.get("x_ratio", -1.0))
		_expect(not prop_rect.intersects(travel_rect), "%s stays outside the unit-travel corridor" % str(placement.get("id", "terrain prop")), failures)
		_expect(x_ratio <= 0.36 or x_ratio >= 0.64, "%s stays in a faction territory band, not the clash center" % str(placement.get("id", "terrain prop")), failures)
		_expect(battle_focus.is_terrain_prop_placement_allowed(placement, combat_rect), "%s is accepted only in its approved faction edge band" % str(placement.get("id", "terrain prop")), failures)
	var wrong_side: Dictionary = layout[0].duplicate(true)
	wrong_side["x_ratio"] = 0.50
	_expect(not battle_focus.is_terrain_prop_placement_allowed(wrong_side, combat_rect), "a Lumern prop is rejected from the neutral central band", failures)
	var corridor_intrusion: Dictionary = layout[0].duplicate(true)
	corridor_intrusion["rect"] = Rect2(Vector2(120.0, travel_rect.position.y + 8.0), Vector2(80.0, 40.0))
	_expect(not battle_focus.is_terrain_prop_placement_allowed(corridor_intrusion, combat_rect), "a prop that enters the soldier travel corridor is rejected", failures)
	var lumern_rect_crosses_center: Dictionary = layout[0].duplicate(true)
	lumern_rect_crosses_center["rect"] = Rect2(
		combat_rect.position + Vector2(combat_rect.size.x * 0.08, combat_rect.size.y * 0.05),
		Vector2(combat_rect.size.x * 0.40, combat_rect.size.y * 0.16)
	)
	_expect(not battle_focus.is_terrain_prop_placement_allowed(lumern_rect_crosses_center, combat_rect), "a Lumern prop rectangle that crosses into the neutral center is rejected", failures)
	var veil_rect_crosses_center: Dictionary = layout[3].duplicate(true)
	veil_rect_crosses_center["rect"] = Rect2(
		combat_rect.position + Vector2(combat_rect.size.x * 0.55, combat_rect.size.y * 0.05),
		Vector2(combat_rect.size.x * 0.32, combat_rect.size.y * 0.16)
	)
	_expect(not battle_focus.is_terrain_prop_placement_allowed(veil_rect_crosses_center, combat_rect), "a Veil prop rectangle that crosses into the neutral center is rejected", failures)
	battle_focus.free()


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Close battlefield redesign contract passed")
		quit(0)
	else:
		printerr("Close battlefield redesign contract failures:\n%s" % "\n".join(failures))
		quit(1)
