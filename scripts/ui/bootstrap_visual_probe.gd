class_name BootstrapVisualProbe
extends Node2D

func _draw() -> void:
	var lane_colors := [Color("315c87"), Color("4a6f94"), Color("315c87")]
	for index in lane_colors.size():
		var y := 110.0 + index * 150.0
		draw_rect(Rect2(80.0, y, 800.0, 96.0), lane_colors[index], true)
		draw_line(Vector2(120.0, y + 48.0), Vector2(840.0, y + 48.0), Color("d4b46c"), 2.0)
		draw_circle(Vector2(480.0, y + 48.0), 18.0, Color("d7dfe8"))
