# 다섯 구간의 단일 행군 전선만 요약하는 읽기 전용 미니맵이다.
class_name MarchMinimapView
extends Control

const FRONT_ID := &"front"
const WARD_COLOR := Color(0.46, 0.7, 0.98, 1.0)
const VEIL_COLOR := Color(0.72, 0.38, 0.8, 1.0)
const CLASH_COLOR := Color(0.96, 0.69, 0.28, 1.0)
const SECTOR_IDS := [&"ward_citadel", &"ward_forward", &"clash", &"veil_forward", &"veil_citadel"]

var run: Variant


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	queue_redraw()


func is_read_only() -> bool:
	return true


func front_count() -> int:
	return 1


func fixed_tower_count() -> int:
	if run == null or run.battle == null:
		return 0
	return 1 if run.battle.fixed_towers.has(FRONT_ID) else 0


func route_state_for(front_id: StringName) -> Dictionary:
	if front_id != FRONT_ID or run == null or run.battle == null:
		return {}
	return run.battle.route_state_for(FRONT_ID)


func current_sector_id() -> StringName:
	var route := route_state_for(FRONT_ID)
	if route.is_empty():
		return &"ward_forward"
	if StringName((route.get("ward_forward", {}) as Dictionary).get("owner_team_id", &"")) != &"lumern":
		return &"ward_forward"
	if StringName((route.get("clash", {}) as Dictionary).get("owner_team_id", &"")) != &"lumern":
		return &"clash"
	if StringName((route.get("veil_forward", {}) as Dictionary).get("owner_team_id", &"")) != &"lumern":
		return &"veil_forward"
	return &"veil_citadel"


func _process(_delta: float) -> void:
	queue_redraw()


func _draw() -> void:
	if size.x <= 0.0 or size.y <= 0.0:
		return
	var frame := StyleBoxFlat.new()
	frame.bg_color = Color(0.018, 0.04, 0.065, 0.96)
	frame.border_width_left = 1
	frame.border_width_top = 1
	frame.border_width_right = 1
	frame.border_width_bottom = 1
	frame.border_color = Color(0.56, 0.64, 0.78, 0.78)
	frame.corner_radius_top_left = 7
	frame.corner_radius_top_right = 7
	frame.corner_radius_bottom_left = 7
	frame.corner_radius_bottom_right = 7
	draw_style_box(frame, Rect2(Vector2.ZERO, size))
	draw_string(ThemeDB.fallback_font, Vector2(12.0, 19.0), "전진 미니맵", HORIZONTAL_ALIGNMENT_LEFT, -1, 12, Color(0.96, 0.9, 0.72, 1.0))
	var points := _route_points()
	draw_polyline(points, Color(0.01, 0.02, 0.04, 0.94), 15.0, true)
	draw_polyline(points, Color(0.54, 0.48, 0.3, 0.88), 9.0, true)
	var route := route_state_for(FRONT_ID)
	for index in SECTOR_IDS.size():
		_draw_sector(index, SECTOR_IDS[index], route)
	_draw_tower(route)
	_draw_strength_summary(route)


func _route_points() -> PackedVector2Array:
	var left := size.x * 0.28
	var right := size.x * 0.72
	return PackedVector2Array([
		Vector2(size.x * 0.5, 45.0),
		Vector2(left, size.y * 0.31),
		Vector2(size.x * 0.5, size.y * 0.5),
		Vector2(right, size.y * 0.69),
		Vector2(size.x * 0.5, size.y - 35.0),
	])


func _draw_sector(index: int, sector_id: StringName, route: Dictionary) -> void:
	var center := _route_points()[index]
	var color := _sector_color(sector_id, route)
	draw_circle(center, 10.0, Color(0.01, 0.02, 0.04, 0.96))
	draw_circle(center, 7.0, color)
	if current_sector_id() == sector_id:
		draw_arc(center, 15.0, 0.0, TAU, 18, Color(1.0, 0.84, 0.38, 0.96), 2.0, true)
	var label_position := center + Vector2(12.0, 4.0)
	draw_string(ThemeDB.fallback_font, label_position, _sector_label(sector_id), HORIZONTAL_ALIGNMENT_LEFT, 74.0, 9, Color(0.94, 0.94, 0.9, 0.95))


func _draw_tower(route: Dictionary) -> void:
	var center := _route_points()[1] + Vector2(-17.0, 0.0)
	var color := Color(0.38, 0.42, 0.5, 0.95)
	if bool(route.get("tower_active", false)):
		color = _owner_color(StringName(route.get("tower_owner_team_id", &"")), color)
	draw_rect(Rect2(center - Vector2(3.0, 7.0), Vector2(6.0, 14.0)), color, true)
	draw_circle(center + Vector2(0.0, -8.0), 3.0, color)


func _draw_strength_summary(route: Dictionary) -> void:
	var label := "수호 %d · 장막 %d" % [int(route.get("friendly_count", 0)), int(route.get("enemy_count", 0))]
	draw_string(ThemeDB.fallback_font, Vector2(12.0, size.y - 11.0), label, HORIZONTAL_ALIGNMENT_LEFT, -1, 10, Color(0.78, 0.86, 0.96, 0.96))


func _sector_color(sector_id: StringName, route: Dictionary) -> Color:
	if sector_id == &"ward_citadel":
		return WARD_COLOR
	if sector_id == &"veil_citadel":
		return VEIL_COLOR
	var state: Dictionary = route.get(String(sector_id), {})
	if bool(state.get("contested", false)):
		return CLASH_COLOR
	return _owner_color(StringName(state.get("owner_team_id", &"")), CLASH_COLOR)


func _owner_color(owner_team_id: StringName, fallback: Color) -> Color:
	if owner_team_id == &"lumern":
		return WARD_COLOR
	if owner_team_id == &"veil":
		return VEIL_COLOR
	return fallback


func _sector_label(sector_id: StringName) -> String:
	match sector_id:
		&"ward_citadel": return "수호"
		&"ward_forward": return "전진"
		&"clash": return "접전"
		&"veil_forward": return "장막"
	return "베일"
