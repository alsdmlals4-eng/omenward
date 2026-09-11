extends SceneTree
## Reproducible real Godot rendering, no fabricated unit states or edited captures.
func _initialize() -> void:
	call_deferred("capture")

func capture() -> void:
	var screen = load("res://scenes/replan/front_slice.tscn").instantiate()
	root.add_child(screen)
	screen.paused = true
	screen.run.construct("barracks")
	screen._refresh_panel()
	await process_frame
	await RenderingServer.frame_post_draw
	root.get_texture().get_image().save_png("res://output/front-building.png")
	screen.run.spin()
	while screen.run.reserve.has("shield_guard"):
		if not screen.run.deploy("shield_guard"):
			break
	screen.run.begin_round()
	for i in range(230):
		screen.run.advance(0.1)
	screen.tab = "전선"
	screen._refresh_panel()
	await process_frame
	await RenderingServer.frame_post_draw
	root.get_texture().get_image().save_png("res://output/front-battle.png")
	print("REPLAN_RENDER: damage_events=", screen.run.damage_events, " units=", screen.run.units.size())
	screen.queue_free()
	await process_frame
	quit()
