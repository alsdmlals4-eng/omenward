class_name BattlefieldView
extends Node2D

const UNIT_SCENE := preload("res://scenes/units/unit.tscn")
const LANE_IDS := [&"top", &"middle", &"bottom"]
const LANE_Y := {&"top": 116.0, &"middle": 186.0, &"bottom": 256.0}
const WORLD_X_ORIGIN := 110.0
const WORLD_X_PER_SIMULATION_POSITION := 7.4
const FIXED_TOWER_PRESENTATION_POSITION := 27.0

var run: Variant
var _unit_views := {}


func bind_run(assigned_run: Variant) -> void:
	run = assigned_run
	queue_redraw()


func _process(_delta: float) -> void:
	_sync_unit_views()
	queue_redraw()


func _draw() -> void:
	for lane_id in LANE_IDS:
		var y: float = LANE_Y[lane_id]
		var clash := world_position_for(lane_id, 50.0)
		draw_circle(clash, 27.0, Color(0.55, 0.2, 0.14, 0.26))
		draw_arc(clash, 27.0, 0.0, TAU, 24, Color(0.95, 0.68, 0.3, 0.7), 1.0)
		_draw_fixed_tower(lane_id, world_position_for(lane_id, FIXED_TOWER_PRESENTATION_POSITION))
		if run != null and run.battle != null:
			var bypasses: Array = run.battle.bypasses
			if bypasses.any(func(entry: Dictionary) -> bool: return entry["state"].lane_id == lane_id and entry["state"].warning_active):
				draw_string(ThemeDB.fallback_font, clash + Vector2(-20.0, -34.0), "BYPASS WARNING", HORIZONTAL_ALIGNMENT_LEFT, -1, 12, Color(1.0, 0.76, 0.24))
	draw_string(ThemeDB.fallback_font, Vector2(32, 28), "WARD CITADEL  ·  THREE FRONT CONFLICT  ·  VEIL RIFT", HORIZONTAL_ALIGNMENT_LEFT, -1, 13, Color(0.95, 0.88, 0.62, 0.9))


func _draw_fixed_tower(lane_id: StringName, center: Vector2) -> void:
	if run == null or run.battle == null or not run.battle.fixed_towers.has(lane_id):
		return
	var tower: Variant = run.battle.fixed_towers[lane_id]
	var color := Color(0.34, 0.4, 0.48, 0.9)
	if tower.active and tower.owner_team_id == &"lumern":
		color = Color(0.55, 0.72, 0.98, 0.9)
	elif tower.active and tower.owner_team_id == &"veil":
		color = Color(0.72, 0.36, 0.76, 0.9)
	draw_rect(Rect2(center - Vector2(7, 15), Vector2(14, 30)), color, true)
	draw_rect(Rect2(center - Vector2(9, 17), Vector2(18, 34)), Color(0.12, 0.14, 0.18, 0.78), false, 1.0)
	draw_circle(center + Vector2(0, -18), 5.0, color)


func world_position_for(lane_id: StringName, lane_position: float) -> Vector2:
	var lane_y: float = float(LANE_Y.get(lane_id, LANE_Y[&"middle"]))
	return Vector2(WORLD_X_ORIGIN + clampf(lane_position, 0.0, 100.0) * WORLD_X_PER_SIMULATION_POSITION, lane_y)


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
			view.position = world_position_for(lane_id, unit.lane_position)
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
