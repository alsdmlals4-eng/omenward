extends SceneTree

func _initialize() -> void:
	call_deferred("verify")

func verify() -> void:
	var screen = load("res://scenes/replan/front_slice.tscn").instantiate()
	screen.save_path = "user://replan-screen-test-v1.json"
	root.add_child(screen)
	await process_frame
	var failed := false
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
	DirAccess.remove_absolute(screen.save_path)
	screen.queue_free()
	await process_frame
	quit(1 if failed else 0)
