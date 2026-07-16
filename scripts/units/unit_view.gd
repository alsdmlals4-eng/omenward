class_name UnitView
extends Node2D

var unit: Variant
var visual_profile: Variant


func bind_unit(assigned_unit: Variant, assigned_visual_profile: Variant = null) -> void:
	unit = assigned_unit
	visual_profile = assigned_visual_profile
	queue_redraw()


func _process(_delta: float) -> void:
	queue_redraw()


func _draw() -> void:
	if unit == null:
		return
	var color := Color.WHITE
	if visual_profile != null:
		color = visual_profile.palette_color
	var state_name := str(unit.state)
	var radius := 7.0
	if state_name == "structure_attack":
		radius = 10.0
	elif state_name == "dead":
		color.a = 0.3
		draw_line(Vector2(-7, 0), Vector2(7, 0), color, 3.0)
		return
	if state_name.begins_with("bypass"):
		draw_colored_polygon(PackedVector2Array([Vector2(0, -8), Vector2(8, 0), Vector2(0, 8), Vector2(-8, 0)]), color)
	else:
		draw_circle(Vector2.ZERO, radius, color)
	if state_name.begins_with("attack"):
		var direction := 1.0 if unit.owner_team_id == &"lumern" else -1.0
		draw_line(Vector2.ZERO, Vector2(direction * 12.0, -4.0), Color.WHITE, 2.0)
	if state_name == "hit_light":
		draw_arc(Vector2.ZERO, radius + 3.0, 0.0, TAU, 12, Color.WHITE, 1.0)
	if state_name == "capture":
		draw_arc(Vector2.ZERO, radius + 4.0, 0.0, TAU, 12, Color(1.0, 0.85, 0.35), 2.0)
	if state_name == "victory":
		draw_line(Vector2(0, -radius), Vector2(0, -radius - 8.0), Color(1.0, 0.9, 0.4), 2.0)
