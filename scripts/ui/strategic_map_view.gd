# Run Command의 세 전선을 한 장의 읽기 전용 전략 지도로 투영한다.
class_name StrategicMapView
extends Control

const LANE_IDS := [&"top", &"middle", &"bottom"]
const LANE_LABELS := {&"top": "상단", &"middle": "중앙", &"bottom": "하단"}
const WARD_ROOT := Vector2(92.0, 124.0)
const VEIL_ROOT := Vector2(832.0, 124.0)
const FRONT_Y := {&"top": 54.0, &"middle": 124.0, &"bottom": 194.0}
const ROUTE_LEFT_FORWARD_X := 314.0
const ROUTE_CLASH_X := 462.0
const ROUTE_RIGHT_FORWARD_X := 610.0

var run: Variant


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	queue_redraw()


func front_count() -> int:
	return LANE_IDS.size()


func fixed_tower_count() -> int:
	if run == null or run.battle == null:
		return 0
	return run.battle.fixed_towers.size()


func route_state_for(lane_id: StringName) -> Dictionary:
	if not LANE_IDS.has(lane_id) or run == null or run.battle == null:
		return {}
	var battle: Variant = run.battle
	var ward_forward: Variant = battle.outposts[&"lumern"][lane_id]
	var veil_forward: Variant = battle.outposts[&"veil"][lane_id]
	var clash: Variant = battle.clash_zones[lane_id].outpost
	var tower: Variant = battle.fixed_towers.get(lane_id)
	var friendly_count := 0
	var enemy_count := 0
	for unit in battle.lanes[lane_id].units:
		if unit.owner_team_id == &"lumern":
			friendly_count += 1
		else:
			enemy_count += 1
	return {
		"lane_id": lane_id,
		"ward_forward": _objective_snapshot(ward_forward),
		"clash": _objective_snapshot(clash),
		"veil_forward": _objective_snapshot(veil_forward),
		"tower_owner_team_id": tower.owner_team_id if tower != null else &"",
		"tower_active": tower.active if tower != null else false,
		"friendly_count": friendly_count,
		"enemy_count": enemy_count,
	}


func _process(_delta: float) -> void:
	queue_redraw()


func _draw() -> void:
	draw_style_box(_map_frame(), Rect2(Vector2.ZERO, size))
	for lane_id in LANE_IDS:
		_draw_route(lane_id)
	_draw_root(WARD_ROOT, "WARD", Color(0.46, 0.67, 0.96, 0.96), HORIZONTAL_ALIGNMENT_LEFT)
	_draw_root(VEIL_ROOT, "VEIL", Color(0.72, 0.38, 0.78, 0.96), HORIZONTAL_ALIGNMENT_RIGHT)


func _map_frame() -> StyleBoxFlat:
	var frame := StyleBoxFlat.new()
	frame.bg_color = Color(0.025, 0.052, 0.078, 0.42)
	frame.border_width_left = 1
	frame.border_width_top = 1
	frame.border_width_right = 1
	frame.border_width_bottom = 1
	frame.border_color = Color(0.54, 0.65, 0.78, 0.72)
	frame.corner_radius_top_left = 6
	frame.corner_radius_top_right = 6
	frame.corner_radius_bottom_right = 6
	frame.corner_radius_bottom_left = 6
	return frame


func _draw_route(lane_id: StringName) -> void:
	var points := _route_points(lane_id)
	draw_polyline(points, Color(0.015, 0.026, 0.044, 0.82), 34.0, true)
	draw_polyline(points, Color(0.78, 0.69, 0.43, 0.72), 25.0, true)
	draw_polyline(points, Color(0.95, 0.88, 0.64, 0.42), 2.0, true)
	var state := route_state_for(lane_id)
	_draw_objective_marker(Vector2(ROUTE_LEFT_FORWARD_X, FRONT_Y[lane_id]), state.get("ward_forward", {}), Color(0.48, 0.7, 0.98, 1.0))
	_draw_clash_marker(Vector2(ROUTE_CLASH_X, FRONT_Y[lane_id]), state.get("clash", {}))
	_draw_objective_marker(Vector2(ROUTE_RIGHT_FORWARD_X, FRONT_Y[lane_id]), state.get("veil_forward", {}), Color(0.72, 0.38, 0.78, 1.0))
	_draw_fixed_tower(lane_id, Vector2(ROUTE_LEFT_FORWARD_X - 30.0, FRONT_Y[lane_id]), state)
	var count_text := "%s  %d : %d" % [LANE_LABELS[lane_id], int(state.get("friendly_count", 0)), int(state.get("enemy_count", 0))]
	draw_string(ThemeDB.fallback_font, Vector2(ROUTE_CLASH_X - 34.0, FRONT_Y[lane_id] + 30.0), count_text, HORIZONTAL_ALIGNMENT_LEFT, -1, 11, Color(0.92, 0.94, 0.98, 0.94))


func _route_points(lane_id: StringName) -> PackedVector2Array:
	var y: float = FRONT_Y[lane_id]
	return PackedVector2Array([
		WARD_ROOT,
		Vector2(190.0, lerpf(WARD_ROOT.y, y, 0.58)),
		Vector2(ROUTE_LEFT_FORWARD_X, y),
		Vector2(ROUTE_CLASH_X, y),
		Vector2(ROUTE_RIGHT_FORWARD_X, y),
		Vector2(734.0, lerpf(VEIL_ROOT.y, y, 0.58)),
		VEIL_ROOT,
	])


func _objective_snapshot(objective: Variant) -> Dictionary:
	if objective == null:
		return {}
	return {
		"owner_team_id": objective.owner_team_id,
		"state": objective.state,
		"contested": objective.contested,
	}


func _draw_root(center: Vector2, label: String, color: Color, alignment: HorizontalAlignment) -> void:
	draw_circle(center, 18.0, Color(0.02, 0.04, 0.07, 0.9))
	draw_circle(center, 14.0, color)
	draw_arc(center, 19.0, 0.0, TAU, 20, Color(0.95, 0.88, 0.64, 0.84), 1.0)
	var label_position := center + Vector2(0.0, -25.0)
	draw_string(ThemeDB.fallback_font, label_position, label, alignment, 90.0, 11, Color(0.96, 0.92, 0.75, 0.96))


func _draw_objective_marker(center: Vector2, objective: Dictionary, fallback_color: Color) -> void:
	var color := _owner_color(StringName(objective.get("owner_team_id", &"")), fallback_color)
	if bool(objective.get("contested", false)):
		color = Color(0.96, 0.63, 0.26, 1.0)
	draw_circle(center, 11.0, Color(0.03, 0.05, 0.08, 0.9))
	draw_circle(center, 8.0, color)
	draw_arc(center, 12.0, 0.0, TAU, 16, Color(0.95, 0.88, 0.64, 0.92), 1.0)


func _draw_clash_marker(center: Vector2, objective: Dictionary) -> void:
	var color := Color(0.94, 0.68, 0.26, 1.0)
	if not bool(objective.get("contested", false)):
		color = _owner_color(StringName(objective.get("owner_team_id", &"")), color)
	draw_circle(center, 16.0, Color(0.15, 0.07, 0.06, 0.84))
	draw_arc(center, 16.0, 0.0, TAU, 20, color, 2.0)
	draw_line(center + Vector2(-6.0, -6.0), center + Vector2(6.0, 6.0), color, 2.0)
	draw_line(center + Vector2(-6.0, 6.0), center + Vector2(6.0, -6.0), color, 2.0)


func _draw_fixed_tower(lane_id: StringName, center: Vector2, state: Dictionary) -> void:
	var color := Color(0.3, 0.34, 0.4, 0.94)
	if bool(state.get("tower_active", false)):
		color = _owner_color(StringName(state.get("tower_owner_team_id", &"")), color)
	draw_rect(Rect2(center - Vector2(4.0, 10.0), Vector2(8.0, 20.0)), color, true)
	draw_rect(Rect2(center - Vector2(6.0, 12.0), Vector2(12.0, 24.0)), Color(0.01, 0.02, 0.04, 0.9), false, 1.0)
	draw_circle(center + Vector2(0.0, -12.0), 4.0, color)
	draw_string(ThemeDB.fallback_font, center + Vector2(-14.0, 29.0), "T", HORIZONTAL_ALIGNMENT_LEFT, -1, 9, Color(0.95, 0.88, 0.64, 0.9))


func _owner_color(owner_team_id: StringName, fallback: Color) -> Color:
	if owner_team_id == &"lumern":
		return Color(0.46, 0.68, 0.98, 1.0)
	if owner_team_id == &"veil":
		return Color(0.72, 0.38, 0.78, 1.0)
	return fallback
