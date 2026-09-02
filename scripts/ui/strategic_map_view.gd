# Run Command의 단일 행군 전선을 읽기 전용으로 투영한다.
class_name StrategicMapView
extends Control

const FRONT_ID := &"front"
const WARD_COLOR := Color(0.46, 0.68, 0.98, 1.0)
const VEIL_COLOR := Color(0.72, 0.38, 0.78, 1.0)
const CLASH_COLOR := Color(0.94, 0.68, 0.26, 1.0)
const LUMERN_SHIELD_GUARD_TEXTURE := preload("res://assets/art/units/lumern_shield_guard_storybook_idle_v1.png")
const VEIL_SHIELD_GUARD_TEXTURE := preload("res://assets/art/units/veil_shield_guard_storybook_idle_v1.png")
const UNIT_MARKER_SIZE := Vector2(84.0, 84.0)

var run: Variant


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	queue_redraw()


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
	var frame := StyleBoxFlat.new()
	frame.bg_color = Color(0.025, 0.052, 0.078, 0.44)
	frame.border_width_left = 1
	frame.border_width_top = 1
	frame.border_width_right = 1
	frame.border_width_bottom = 1
	frame.border_color = Color(0.54, 0.65, 0.78, 0.72)
	frame.corner_radius_top_left = 6
	frame.corner_radius_top_right = 6
	frame.corner_radius_bottom_left = 6
	frame.corner_radius_bottom_right = 6
	draw_style_box(frame, Rect2(Vector2.ZERO, size))
	var route := route_state_for(FRONT_ID)
	var points := _route_points()
	draw_polyline(points, Color(0.015, 0.026, 0.044, 0.84), 44.0, true)
	draw_polyline(points, Color(0.63, 0.52, 0.31, 0.82), 33.0, true)
	draw_polyline(points, Color(0.96, 0.88, 0.64, 0.42), 2.0, true)
	_draw_root(_ward_root(), "WARD", WARD_COLOR, HORIZONTAL_ALIGNMENT_LEFT)
	_draw_root(_veil_root(), "VEIL", VEIL_COLOR, HORIZONTAL_ALIGNMENT_RIGHT)
	_draw_objective(_ward_forward(), route.get("ward_forward", {}), WARD_COLOR, "전진기지")
	_draw_clash(_clash(), route.get("clash", {}))
	_draw_objective(_veil_forward(), route.get("veil_forward", {}), VEIL_COLOR, "장막 전진기지")
	_draw_fixed_tower(_ward_forward() + Vector2(-30.0, 0.0), route)
	_draw_sector_focus(current_sector_id())
	_draw_front_unit_markers()
	var count_text := "%d : %d" % [int(route.get("friendly_count", 0)), int(route.get("enemy_count", 0))]
	draw_string(ThemeDB.fallback_font, _clash() + Vector2(-15.0, 34.0), count_text, HORIZONTAL_ALIGNMENT_LEFT, -1, 11, Color(0.92, 0.94, 0.98, 0.94))


func _route_points() -> PackedVector2Array:
	return PackedVector2Array([_ward_root(), _ward_forward(), _clash(), _veil_forward(), _veil_root()])


func unit_marker_texture_for(owner_team_id: StringName, archetype_id: StringName) -> Texture2D:
	if archetype_id == &"":
		return null
	return VEIL_SHIELD_GUARD_TEXTURE if owner_team_id == &"veil" else LUMERN_SHIELD_GUARD_TEXTURE


func front_unit_marker_offset_for(index: int) -> Vector2:
	var formation_offsets := PackedVector2Array([
		Vector2.ZERO,
		Vector2(48.0, -8.0),
		Vector2(-48.0, -8.0),
		Vector2(24.0, -46.0),
		Vector2(-24.0, -46.0),
	])
	if index < formation_offsets.size():
		return formation_offsets[index]
	var overflow_index := index - formation_offsets.size()
	return Vector2(float((overflow_index % 3) - 1) * 44.0, -76.0 - float(overflow_index / 3) * 34.0)


func _draw_front_unit_markers() -> void:
	if run == null or run.battle == null:
		return
	var index := 0
	for unit in run.battle.front_units(FRONT_ID):
		var texture := unit_marker_texture_for(unit.owner_team_id, unit.archetype_id)
		if texture == null:
			continue
		var lane_position: float = clampf(unit.lane_position, 4.0, 96.0)
		var formation_offset := front_unit_marker_offset_for(index)
		var center := Vector2(lerpf(_ward_root().x, _veil_root().x, lane_position / 100.0), size.y * 0.5) + formation_offset
		var faction_color := _owner_color(unit.owner_team_id, Color.WHITE)
		draw_circle(center + Vector2(0.0, 13.0), 28.0, Color(0.01, 0.02, 0.04, 0.76))
		draw_circle(center + Vector2(0.0, 5.0), 35.0, Color(faction_color.r, faction_color.g, faction_color.b, 0.34))
		draw_arc(center + Vector2(0.0, 5.0), 36.0, 0.0, TAU, 24, Color(0.96, 0.88, 0.64, 0.9), 2.0)
		draw_texture_rect(texture, Rect2(center - Vector2(UNIT_MARKER_SIZE.x * 0.5, UNIT_MARKER_SIZE.y - 18.0), UNIT_MARKER_SIZE), false, Color.WHITE)
		draw_string(ThemeDB.fallback_font, center + Vector2(-42.0, 38.0), _unit_marker_label(unit.owner_team_id, unit.archetype_id), HORIZONTAL_ALIGNMENT_CENTER, 84.0, 10, Color(0.98, 0.96, 0.88, 0.98))
		index += 1


func _unit_marker_label(owner_team_id: StringName, archetype_id: StringName) -> String:
	var faction := "수호" if owner_team_id == &"lumern" else "장막"
	var role := "병사"
	match archetype_id:
		&"shield_guard": role = "수호병"
		&"archer": role = "궁수"
		&"assassin": role = "침투병"
		&"brute": role = "중보병"
	return "%s %s" % [faction, role]


func _ward_root() -> Vector2:
	return Vector2(52.0, size.y * 0.5)


func _veil_root() -> Vector2:
	return Vector2(maxf(52.0, size.x - 52.0), size.y * 0.5)


func _ward_forward() -> Vector2:
	return Vector2(lerpf(_ward_root().x, _veil_root().x, 0.28), size.y * 0.5)


func _clash() -> Vector2:
	return Vector2(size.x * 0.5, size.y * 0.5)


func _veil_forward() -> Vector2:
	return Vector2(lerpf(_ward_root().x, _veil_root().x, 0.72), size.y * 0.5)


func _draw_root(center: Vector2, label: String, color: Color, alignment: HorizontalAlignment) -> void:
	draw_circle(center, 19.0, Color(0.02, 0.04, 0.07, 0.92))
	draw_circle(center, 14.0, color)
	draw_arc(center, 20.0, 0.0, TAU, 20, Color(0.95, 0.88, 0.64, 0.84), 1.0)
	draw_string(ThemeDB.fallback_font, center + Vector2(0.0, -25.0), label, alignment, 92.0, 11, Color(0.96, 0.92, 0.75, 0.96))


func _draw_objective(center: Vector2, objective: Dictionary, fallback: Color, label: String) -> void:
	var color := _objective_color(objective, fallback)
	draw_circle(center, 12.0, Color(0.03, 0.05, 0.08, 0.9))
	draw_circle(center, 8.0, color)
	draw_arc(center, 13.0, 0.0, TAU, 16, Color(0.95, 0.88, 0.64, 0.92), 1.0)
	draw_string(ThemeDB.fallback_font, center + Vector2(-25.0, 31.0), label, HORIZONTAL_ALIGNMENT_LEFT, 70.0, 9, Color(0.91, 0.9, 0.8, 0.9))


func _draw_clash(center: Vector2, objective: Dictionary) -> void:
	var color := _objective_color(objective, CLASH_COLOR)
	draw_circle(center, 17.0, Color(0.15, 0.07, 0.06, 0.86))
	draw_arc(center, 17.0, 0.0, TAU, 20, color, 2.0)
	draw_line(center + Vector2(-6.0, -6.0), center + Vector2(6.0, 6.0), color, 2.0)
	draw_line(center + Vector2(-6.0, 6.0), center + Vector2(6.0, -6.0), color, 2.0)


func _draw_fixed_tower(center: Vector2, route: Dictionary) -> void:
	var color := Color(0.3, 0.34, 0.4, 0.94)
	if bool(route.get("tower_active", false)):
		color = _owner_color(StringName(route.get("tower_owner_team_id", &"")), color)
	draw_rect(Rect2(center - Vector2(4.0, 10.0), Vector2(8.0, 20.0)), color, true)
	draw_rect(Rect2(center - Vector2(6.0, 12.0), Vector2(12.0, 24.0)), Color(0.01, 0.02, 0.04, 0.9), false, 1.0)
	draw_circle(center + Vector2(0.0, -12.0), 4.0, color)


func _draw_sector_focus(sector_id: StringName) -> void:
	var center := _ward_forward()
	match sector_id:
		&"clash": center = _clash()
		&"veil_forward": center = _veil_forward()
		&"veil_citadel": center = _veil_root()
	draw_arc(center, 28.0, 0.0, TAU, 20, Color(1.0, 0.84, 0.38, 0.92), 2.0)


func _objective_color(objective: Dictionary, fallback: Color) -> Color:
	if bool(objective.get("contested", false)):
		return CLASH_COLOR
	return _owner_color(StringName(objective.get("owner_team_id", &"")), fallback)


func _owner_color(owner_team_id: StringName, fallback: Color) -> Color:
	if owner_team_id == &"lumern":
		return WARD_COLOR
	if owner_team_id == &"veil":
		return VEIL_COLOR
	return fallback
