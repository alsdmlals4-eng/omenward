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
	var captured: Dictionary = {}
	for i in range(230):
		screen.run.advance(0.1)
		for actor in screen.run.units:
			if actor.side != 0 or actor.role != "shield_guard":
				continue
			var pose: int = screen.art.motion_frame(actor)
			if pose > 0 and not captured.has(pose):
				screen.queue_redraw()
				await process_frame
				await RenderingServer.frame_post_draw
				root.get_texture().get_image().save_png("res://output/front-shield-%s.png" % ["idle", "windup", "impact", "recover"][pose])
				captured[pose] = true
	screen.tab = "전선"
	screen._refresh_panel()
	await process_frame
	await RenderingServer.frame_post_draw
	root.get_texture().get_image().save_png("res://output/front-battle.png")
	root.size = Vector2i(1920, 1080)
	await process_frame
	await RenderingServer.frame_post_draw
	var hd := root.get_texture().get_image()
	hd.save_png("res://output/front-battle-1080.png")
	if hd.get_size() != Vector2i(1920, 1080):
		push_error("Full HD capture has wrong dimensions")
		quit(1)
		return
	print("REPLAN_RENDER: damage_events=", screen.run.damage_events, " units=", screen.run.units.size())
	print("SHIELD_RUNTIME_POSES: ", captured.size(), "/3")
	screen.queue_free()
	await process_frame
	quit(0 if captured.size() == 3 else 1)
