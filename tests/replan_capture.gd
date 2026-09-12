extends SceneTree
## Natural battle first; explicitly labeled mixed-role stress fixture second.
func _initialize() -> void:
	call_deferred("capture")

func capture() -> void:
	root.gui_embed_subwindows = true
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
	root.size = Vector2i(1280, 720)
	screen.run = screen.Model.new()
	screen.run.units.clear()
	for side in range(2):
		for role in ["shield_guard", "archer", "mage", "priest", "spear_guard"]:
			screen.run.spawn(role, side, 46.0 if side == 0 else 54.0)
	screen.run.begin_round()
	screen.run.advance(0.6)
	screen.run.message = "혼합 병종 검증 편성 · 일반 획득 흐름 아님 · 병사 위에 마우스로 정보 확인"
	screen._refresh_panel()
	screen.queue_redraw()
	await process_frame
	var hover := InputEventMouseMotion.new()
	hover.position = screen.unit_draw_anchor(screen.run.units[1])
	hover.global_position = hover.position
	root.push_input(hover)
	await create_timer(0.8).timeout
	await RenderingServer.frame_post_draw
	root.get_texture().get_image().save_png("res://output/front-mixed.png")
	root.size = Vector2i(1920, 1080)
	await process_frame
	await RenderingServer.frame_post_draw
	root.get_texture().get_image().save_png("res://output/front-mixed-1080.png")
	print("MIXED_FIXTURE: units=", screen.run.units.size(), " damage_events=", screen.run.damage_events)
	screen.queue_free()
	await process_frame
	quit(0 if captured.size() == 3 else 1)
