class_name BattlefieldView
extends Node2D

const UNIT_SCENE := preload("res://scenes/units/unit.tscn")
const LANE_IDS := [&"top", &"middle", &"bottom"]
const LANE_Y := {&"top": 165.0, &"middle": 270.0, &"bottom": 375.0}

var run: Variant
var _unit_views := {}


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	queue_redraw()


func _process(_delta: float) -> void:
	_sync_unit_views()
	queue_redraw()


func _draw() -> void:
	draw_rect(Rect2(24, 92, 912, 332), Color(0.08, 0.12, 0.16, 0.96), true)
	for lane_id in LANE_IDS:
		var y: float = LANE_Y[lane_id]
		draw_line(Vector2(88, y), Vector2(872, y), Color(0.31, 0.37, 0.43), 20.0)
		draw_line(Vector2(88, y), Vector2(872, y), Color(0.58, 0.63, 0.68), 2.0)
		draw_rect(Rect2(96, y - 23, 18, 46), Color(0.38, 0.66, 0.96), true)
		draw_rect(Rect2(846, y - 23, 18, 46), Color(0.76, 0.3, 0.54), true)
		draw_rect(Rect2(420, y - 20, 120, 40), Color(0.25, 0.28, 0.3), true)
		_draw_outpost_nodes(Vector2(330, y), Color(0.5, 0.55, 0.6))
		_draw_outpost_nodes(Vector2(630, y), Color(0.5, 0.55, 0.6))
		if run != null and run.battle != null:
			var bypasses: Array = run.battle.bypasses
			if bypasses.any(func(entry: Dictionary) -> bool: return entry["state"].lane_id == lane_id and entry["state"].warning_active):
				draw_string(ThemeDB.fallback_font, Vector2(460, y - 34), "BYPASS WARNING", HORIZONTAL_ALIGNMENT_LEFT, -1, 12, Color(1.0, 0.76, 0.24))
	draw_string(ThemeDB.fallback_font, Vector2(38, 72), "BATTLEFIELD GRAYBOX · THREE ISOLATED LANES", HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color(0.82, 0.88, 0.92))


func _draw_outpost_nodes(center: Vector2, color: Color) -> void:
	draw_circle(center + Vector2(-20, -14), 5.0, color)
	draw_circle(center + Vector2(-20, 14), 5.0, color)
	draw_circle(center + Vector2(20, 0), 5.0, color)


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
