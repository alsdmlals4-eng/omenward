extends SceneTree

func _initialize() -> void:
	call_deferred("verify")

func verify() -> void:
	var screen = load("res://scenes/replan/front_slice.tscn").instantiate()
	screen.save_path = "user://replan-screen-test-v1.json"
	root.add_child(screen)
	await process_frame
	var failed := false
	for role in screen.run.definitions:
		var veil: AtlasTexture = screen.art.unit(role, 1)
		var veil_image := veil.atlas.get_image()
		if veil_image.detect_alpha() == Image.ALPHA_NONE:
			push_error("Veil role still uses opaque atlas: " + role)
			failed = true
	var idle: AtlasTexture = screen.art.unit("shield_guard", 0)
	var source := idle.atlas.get_image()
	if source.detect_alpha() == Image.ALPHA_NONE or source.get_pixel(0, 0).a != 0:
		push_error("Shield idle must use genuine transparent pixels")
		failed = true
	if idle.region != Rect2(0, 0, 627, 627):
		push_error("Only the reviewed idle cell may be consumed")
		failed = true
	if not screen.has_method("phase_label"):
		push_error("Missing localized battle phase presentation")
		quit(1)
		return
	if screen.phase_label() != "출정 준비":
		failed = true
	for button in screen.find_children("*", "Button", true, false):
		if button.text == "전선":
			button.pressed.emit()
			if not button.button_pressed or screen.tab != "전선":
				failed = true
	screen.tab = "내정"
	screen._refresh_panel()
	screen.paused = true
	screen._process(0.0)
	if screen.pause_button.text != "계속 진행":
		failed = true
	screen.paused = false
	for node in screen.find_children("*", "TextureRect", true, false):
		if node.size.x > 130 or node.size.y > 130:
			push_error("Atlas picture exceeds its UI allocation: %s" % node.size)
			failed = true
	var found := false
	for button in screen.find_children("*", "Button", true, false):
		if button.text.begins_with("일반 병영"):
			button.pressed.emit()
			found = true
			break
	if not found or screen.run.buildings.size() != 1 or screen.run.gold != 80:
		failed = true
		push_error("Build button does not consume the real model")
	screen._save()
	screen.run.gold = 1
	screen._load_save()
	if screen.run.gold != 80:
		failed = true
		push_error("Save/load button path loses gold")
	print("REPLAN_SCREEN_TEST: ", "FAIL" if failed else "PASS")
	# User deletes disposable files manually; leave this deterministic test save for collection.
	screen.queue_free()
	await process_frame
	quit(1 if failed else 0)
