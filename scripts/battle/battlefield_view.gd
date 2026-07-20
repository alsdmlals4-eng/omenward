class_name BattlefieldView
extends Node2D

const UNIT_SCENE := preload("res://scenes/units/unit.tscn")
const LANE_IDS := [&"top", &"middle", &"bottom"]
const LANE_Y := {&"top": 165.0, &"middle": 270.0, &"bottom": 375.0}
const FRIENDLY_OUTPOST_X := 300.0
const CENTER_CLASH_X := 480.0
const ENEMY_OUTPOST_X := 660.0
const LUMEN := Color(0.31, 0.66, 0.96, 1.0)
const VEIL := Color(0.76, 0.3, 0.54, 1.0)
const PATH_LIGHT := Color(0.69, 0.76, 0.68, 0.82)
const PATH_SHADOW := Color(0.25, 0.38, 0.34, 0.94)
const FRIENDLY_NODE_IDS := [&"front_a", &"front_b", &"rear"]

signal construction_node_selected(outpost_id: StringName, node_id: StringName)

var run: Variant
var _unit_views := {}
var _selected_outpost_id: StringName = &""
var _selected_node_id: StringName = &""


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	queue_redraw()


func _process(_delta: float) -> void:
	_sync_unit_views()
	queue_redraw()


func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
		for lane_id in LANE_IDS:
			var outpost_id := StringName("home_%s" % lane_id)
			for node_id in FRIENDLY_NODE_IDS:
				if event.position.distance_to(_friendly_node_position(lane_id, node_id)) <= 14.0:
					_selected_outpost_id = outpost_id
					_selected_node_id = node_id
					construction_node_selected.emit(outpost_id, node_id)
					queue_redraw()
					var viewport := get_viewport()
					if viewport != null:
						viewport.set_input_as_handled()
					return


func set_selected_construction_node(outpost_id: StringName, node_id: StringName) -> void:
	_selected_outpost_id = outpost_id
	_selected_node_id = node_id
	queue_redraw()


func _draw() -> void:
	draw_rect(Rect2(24, 92, 912, 332), Color(0.08, 0.15, 0.16, 0.98), true)
	draw_rect(Rect2(28, 96, 904, 324), Color(0.12, 0.24, 0.2, 0.92), true)
	draw_string(ThemeDB.fallback_font, Vector2(38, 72), "경계의 초원 · 독립 3레인 전장", HORIZONTAL_ALIGNMENT_LEFT, -1, 15, Color(0.87, 0.94, 0.9))
	draw_string(ThemeDB.fallback_font, Vector2(700, 72), "루멘  ←  점령선  →  베일", HORIZONTAL_ALIGNMENT_LEFT, -1, 12, Color(0.72, 0.8, 0.82))
	for lane_id in LANE_IDS:
		var y: float = LANE_Y[lane_id]
		_draw_lane_ground(lane_id, y)
		_draw_gate(Vector2(76, y), LUMEN, false)
		_draw_gate(Vector2(884, y), VEIL, true)
		_draw_outpost(Vector2(FRIENDLY_OUTPOST_X, y), LUMEN, false, StringName("home_%s" % lane_id))
		_draw_outpost(Vector2(ENEMY_OUTPOST_X, y), VEIL, true)
		_draw_clash_zone(Vector2(CENTER_CLASH_X, y))
		if run != null and run.battle != null:
			var bypasses: Array = run.battle.bypasses
			if bypasses.any(func(entry: Dictionary) -> bool: return entry["state"].lane_id == lane_id and entry["state"].warning_active):
				draw_string(ThemeDB.fallback_font, Vector2(CENTER_CLASH_X - 38.0, y - 31.0), "우회 경고", HORIZONTAL_ALIGNMENT_LEFT, -1, 12, Color(1.0, 0.76, 0.24))


func _draw_lane_ground(lane_id: StringName, y: float) -> void:
	var lane_color := Color(0.2, 0.37, 0.28, 0.9) if lane_id != &"middle" else Color(0.22, 0.4, 0.31, 0.9)
	draw_rect(Rect2(40, y - 43, 880, 86), lane_color, true)
	draw_line(Vector2(96, y), Vector2(864, y), PATH_SHADOW, 28.0)
	draw_line(Vector2(96, y), Vector2(864, y), PATH_LIGHT, 18.0)
	draw_line(Vector2(96, y - 5), Vector2(864, y - 5), Color(0.88, 0.9, 0.76, 0.7), 1.0)
	draw_line(Vector2(96, y + 5), Vector2(864, y + 5), Color(0.88, 0.9, 0.76, 0.55), 1.0)
	var lane_name := "상단" if lane_id == &"top" else ("중단" if lane_id == &"middle" else "하단")
	draw_rect(Rect2(38, y - 15, 42, 30), Color(0.06, 0.1, 0.12, 0.92), true)
	draw_string(ThemeDB.fallback_font, Vector2(46, y + 5), lane_name, HORIZONTAL_ALIGNMENT_LEFT, -1, 11, Color(0.86, 0.93, 0.9))


func _draw_gate(center: Vector2, color: Color, mirrored: bool) -> void:
	var direction := -1.0 if mirrored else 1.0
	draw_circle(center, 25.0, Color(color.r, color.g, color.b, 0.18))
	draw_rect(Rect2(center.x - 10, center.y - 22, 20, 44), Color(0.11, 0.15, 0.18, 1.0), true)
	draw_rect(Rect2(center.x - 6, center.y - 18, 12, 36), color, true)
	draw_colored_polygon(PackedVector2Array([
		Vector2(center.x - 15 * direction, center.y - 22),
		Vector2(center.x + 15 * direction, center.y - 22),
		Vector2(center.x, center.y - 38),
	]), color)
	draw_line(Vector2(center.x + 20 * direction, center.y - 30), Vector2(center.x + 20 * direction, center.y + 30), Color(color.r, color.g, color.b, 0.55), 2.0)


func _draw_outpost(center: Vector2, color: Color, mirrored: bool, outpost_id: StringName = &"") -> void:
	var direction := -1.0 if mirrored else 1.0
	draw_circle(center, 38.0, Color(0.03, 0.06, 0.08, 0.48))
	draw_circle(center, 30.0, Color(color.r, color.g, color.b, 0.14))
	draw_rect(Rect2(center.x - 18, center.y - 16, 36, 32), Color(0.13, 0.18, 0.2, 1.0), true)
	draw_rect(Rect2(center.x - 13, center.y - 23, 26, 12), color, true)
	draw_colored_polygon(PackedVector2Array([
		Vector2(center.x - 20, center.y - 16),
		Vector2(center.x + 20, center.y - 16),
		Vector2(center.x, center.y - 34),
	]), Color(color.r, color.g, color.b, 0.88))
	_draw_outpost_nodes(center, color, direction, outpost_id)


func _draw_outpost_nodes(center: Vector2, color: Color, direction: float, outpost_id: StringName = &"") -> void:
	var offsets := [Vector2(-28, -23), Vector2(-28, 23), Vector2(29, 0)]
	for index in offsets.size():
		var offset: Vector2 = offsets[index]
		var node_position := center + Vector2(offset.x * direction, offset.y)
		var node_id: StringName = FRIENDLY_NODE_IDS[index] if not outpost_id.is_empty() else &""
		var status: StringName = run.construction_status(outpost_id, node_id) if run != null and not outpost_id.is_empty() else &""
		var node_color := Color(0.91, 0.76, 0.35, 1.0) if status == &"occupied" else color
		if status == &"locked" or status == &"enemy":
			node_color = Color(0.43, 0.45, 0.5, 1.0)
		draw_circle(node_position, 8.0, Color(0.04, 0.07, 0.08, 0.9))
		draw_arc(node_position, 8.0, 0.0, TAU, 12, Color(node_color.r, node_color.g, node_color.b, 0.9), 1.5)
		draw_circle(node_position, 3.0, Color(node_color.r, node_color.g, node_color.b, 0.62))
		if outpost_id == _selected_outpost_id and node_id == _selected_node_id:
			draw_arc(node_position, 12.0, 0.0, TAU, 16, Color(1.0, 0.92, 0.55, 1.0), 2.0)


func _friendly_node_position(lane_id: StringName, node_id: StringName) -> Vector2:
	var y: float = LANE_Y[lane_id]
	var offsets := {&"front_a": Vector2(-28, -23), &"front_b": Vector2(-28, 23), &"rear": Vector2(29, 0)}
	return Vector2(FRIENDLY_OUTPOST_X, y) + offsets.get(node_id, Vector2.ZERO)


func _draw_clash_zone(center: Vector2) -> void:
	draw_circle(center, 31.0, Color(0.75, 0.66, 0.37, 0.12))
	draw_arc(center, 28.0, 0.0, TAU, 20, Color(0.86, 0.72, 0.38, 0.7), 1.0)
	draw_line(center + Vector2(-20, 0), center + Vector2(20, 0), Color(0.92, 0.8, 0.48, 0.75), 1.5)
	draw_line(center + Vector2(0, -20), center + Vector2(0, 20), Color(0.92, 0.8, 0.48, 0.75), 1.5)


func _sync_unit_views() -> void:
	if run == null or run.battle == null:
		return
	var visible_ids := {}
	for lane_id in LANE_IDS:
		var lane: Variant = run.battle.lanes[lane_id]
		for unit in lane.ordered_units():
			visible_ids[unit.unit_id] = true
			var view: Variant = _unit_views.get(unit.unit_id)
			if view == null:
				view = UNIT_SCENE.instantiate()
				_unit_views[unit.unit_id] = view
				add_child(view)
			view.bind_unit(unit, _visual_profile_for(unit))
			view.position = Vector2(110.0 + unit.lane_position * 7.4, float(LANE_Y[lane_id]))
	for unit_id in _unit_views.keys():
		if not visible_ids.has(unit_id):
			_unit_views[unit_id].queue_free()
			_unit_views.erase(unit_id)


func _visual_profile_for(unit: Variant) -> Variant:
	if run == null or run.battle == null or run.battle.registry == null:
		return null
	for profile in run.battle.registry.faction_visuals:
		if profile.archetype_id == unit.archetype_id and profile.visual_faction_id == unit.visual_faction_id:
			return profile
	return null
