# 다섯 구간의 단일 행군 전선만 요약하는 읽기 전용 미니맵이다.
class_name MarchMinimapView
extends Control

const FRONT_ID := &"front"
const WARD_COLOR := Color(0.46, 0.7, 0.98, 1.0)
const VEIL_COLOR := Color(0.72, 0.38, 0.8, 1.0)
const CLASH_COLOR := Color(0.96, 0.69, 0.28, 1.0)
const SECTOR_IDS := [&"ward_citadel", &"ward_forward", &"clash", &"veil_forward", &"veil_citadel"]
const SECTOR_MARGIN_LEFT := 70.0
const SECTOR_MARGIN_RIGHT := 16.0
const SECTOR_GAP := 8.0

var run: Variant


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	queue_redraw()


func is_read_only() -> bool:
	return true


func presentation_contract() -> Dictionary:
	return {
		"front_count": 1,
		"sector_count": 5,
		"top_single_row": true,
		"read_only": true,
		"unit_replication": false,
	}


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
	if run != null and run.has_method(&"current_front_map"):
		var current: Dictionary = run.current_front_map()
		var map_id := StringName(current.get("map_id", &""))
		if SECTOR_IDS.has(map_id):
			return map_id
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
	draw_string(ThemeDB.fallback_font, Vector2(12.0, size.y * 0.64), "전진", HORIZONTAL_ALIGNMENT_LEFT, 44.0, 11, Color(0.96, 0.9, 0.72, 1.0))
	_draw_route_connectors()
	var route := route_state_for(FRONT_ID)
	for index in SECTOR_IDS.size():
		_draw_sector(index, SECTOR_IDS[index], route)
	_draw_tower(route)


func _sector_rect(index: int) -> Rect2:
	var available_width := maxf(5.0, size.x - SECTOR_MARGIN_LEFT - SECTOR_MARGIN_RIGHT - SECTOR_GAP * float(SECTOR_IDS.size() - 1))
	var sector_width := available_width / float(SECTOR_IDS.size())
	return Rect2(
		Vector2(SECTOR_MARGIN_LEFT + float(index) * (sector_width + SECTOR_GAP), 6.0),
		Vector2(sector_width, maxf(1.0, size.y - 12.0))
	)


func _draw_route_connectors() -> void:
	for index in range(SECTOR_IDS.size() - 1):
		var left_rect := _sector_rect(index)
		var right_rect := _sector_rect(index + 1)
		var y := size.y * 0.5
		draw_line(Vector2(left_rect.end.x, y), Vector2(right_rect.position.x, y), Color(0.52, 0.47, 0.3, 0.9), 3.0, true)


func _draw_sector(index: int, sector_id: StringName, route: Dictionary) -> void:
	var rect := _sector_rect(index)
	var map_entry := front_map_entry_for(sector_id)
	var state := StringName(map_entry.get("state", &"locked"))
	var color := _sector_color(sector_id, route, state)
	var cell := StyleBoxFlat.new()
	cell.bg_color = Color(color.r, color.g, color.b, 0.28 if state == &"current" else 0.14)
	cell.border_width_left = 1
	cell.border_width_top = 1
	cell.border_width_right = 1
	cell.border_width_bottom = 1
	cell.border_color = Color(1.0, 0.84, 0.38, 0.96) if state == &"current" else Color(color.r, color.g, color.b, 0.72)
	cell.corner_radius_top_left = 4
	cell.corner_radius_top_right = 4
	cell.corner_radius_bottom_left = 4
	cell.corner_radius_bottom_right = 4
	draw_style_box(cell, rect)
	draw_circle(rect.position + Vector2(10.0, rect.size.y * 0.5), 3.5, color)
	if state == &"current":
		draw_arc(rect.get_center(), minf(rect.size.y * 0.5 + 3.0, 14.0), 0.0, TAU, 18, Color(1.0, 0.84, 0.38, 0.96), 1.25, true)
	var label_color := Color(0.94, 0.94, 0.9, 0.98) if state != &"locked" else Color(0.58, 0.59, 0.65, 0.92)
	draw_string(ThemeDB.fallback_font, rect.position + Vector2(18.0, rect.size.y * 0.64), _sector_label(sector_id), HORIZONTAL_ALIGNMENT_LEFT, rect.size.x - 24.0, 10, label_color)
	if state == &"cleared":
		draw_string(ThemeDB.fallback_font, rect.position + Vector2(rect.size.x - 26.0, rect.size.y * 0.64), "완료", HORIZONTAL_ALIGNMENT_RIGHT, 22.0, 8, Color(0.72, 0.93, 0.78, 0.96))
	elif state == &"available":
		draw_string(ThemeDB.fallback_font, rect.position + Vector2(rect.size.x - 26.0, rect.size.y * 0.64), "다음", HORIZONTAL_ALIGNMENT_RIGHT, 22.0, 8, Color(1.0, 0.84, 0.38, 0.96))
	elif state == &"locked":
		draw_string(ThemeDB.fallback_font, rect.position + Vector2(rect.size.x - 22.0, rect.size.y * 0.64), "잠김", HORIZONTAL_ALIGNMENT_RIGHT, 18.0, 8, Color(0.55, 0.56, 0.62, 0.92))


func _draw_tower(route: Dictionary) -> void:
	if fixed_tower_count() == 0:
		return
	var index := maxi(0, SECTOR_IDS.find(current_sector_id()))
	var rect := _sector_rect(index)
	var center := rect.position + Vector2(rect.size.x - 14.0, rect.size.y * 0.5)
	var color := Color(0.38, 0.42, 0.5, 0.95)
	if bool(route.get("tower_active", false)):
		color = _owner_color(StringName(route.get("tower_owner_team_id", &"")), color)
	draw_rect(Rect2(center - Vector2(2.0, 5.0), Vector2(4.0, 10.0)), color, true)
	draw_circle(center + Vector2(0.0, -5.0), 2.0, color)


func _sector_color(sector_id: StringName, route: Dictionary, map_state: StringName = &"") -> Color:
	if map_state == &"locked":
		return Color(0.38, 0.38, 0.46, 1.0)
	if map_state == &"cleared":
		return WARD_COLOR
	if map_state == &"available":
		return CLASH_COLOR
	if sector_id == &"ward_citadel":
		return WARD_COLOR
	if sector_id == &"veil_citadel":
		return VEIL_COLOR
	var state: Dictionary = route.get(String(sector_id), {})
	if bool(state.get("contested", false)):
		return CLASH_COLOR
	return _owner_color(StringName(state.get("owner_team_id", &"")), CLASH_COLOR)


func front_map_entry_for(sector_id: StringName) -> Dictionary:
	if run != null and run.has_method(&"front_map_snapshot"):
		for entry in run.front_map_snapshot():
			if StringName((entry as Dictionary).get("map_id", &"")) == sector_id:
				return (entry as Dictionary).duplicate(true)
	return {
		"map_id": str(sector_id),
		"state": &"current" if sector_id == current_sector_id() else &"locked",
		"selectable": false,
	}


func _owner_color(owner_team_id: StringName, fallback: Color) -> Color:
	if owner_team_id == &"lumern":
		return WARD_COLOR
	if owner_team_id == &"veil":
		return VEIL_COLOR
	return fallback


func _sector_label(sector_id: StringName) -> String:
	match sector_id:
		&"ward_citadel": return "수호 성채"
		&"ward_forward": return "수호 전진"
		&"clash": return "접전"
		&"veil_forward": return "장막 전진"
	return "베일 성채"
