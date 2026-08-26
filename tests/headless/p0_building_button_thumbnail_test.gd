# P0 건물 행동 버튼이 승인된 썸네일을 읽는지 검증한다.
extends SceneTree

const STAGE_HUD_SCENE_PATH := "res://scenes/ui/stage_hud.tscn"
const EXPECTED_BUTTON_TEXTURES := {
	&"BarracksButton": "res://assets/art/buildings/general_barracks_t1_build_button.png",
	&"TowerButton": "res://assets/art/buildings/defense_tower_t1_build_button.png",
	&"FarmButton": "res://assets/art/buildings/farm_t1_build_button.png",
}
const EXPECTED_ICON_MAX_WIDTH := 22


func _init() -> void:
	call_deferred("_run")


func _run() -> void:
	var failures := PackedStringArray()
	var packed := load(STAGE_HUD_SCENE_PATH) as PackedScene
	_expect(packed != null, "Stage HUD scene loads", failures)
	if packed != null:
		var stage_hud := packed.instantiate()
		root.add_child(stage_hud)
		await process_frame
		for button_name in EXPECTED_BUTTON_TEXTURES:
			var button := stage_hud.get_node_or_null(NodePath(button_name)) as Button
			var expected_path: String = EXPECTED_BUTTON_TEXTURES[button_name]
			_expect(button != null, "%s exists" % button_name, failures)
			_expect(FileAccess.file_exists(expected_path), "%s thumbnail is available to Godot" % button_name, failures)
			if button != null:
				_expect(button.icon != null, "%s loads a building thumbnail" % button_name, failures)
				_expect(button.icon != null and button.icon.resource_path == expected_path, "%s uses its mapped approved building thumbnail" % button_name, failures)
				_expect(button.expand_icon, "%s uses the constrained thumbnail display mode" % button_name, failures)
				_expect(button.get_theme_constant(&"icon_max_width") == EXPECTED_ICON_MAX_WIDTH, "%s keeps the compact HUD icon width" % button_name, failures)
		stage_hud.queue_free()
	_finish(failures)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("P0 building button thumbnail contracts passed")
		quit(0)
	else:
		printerr("P0 building button thumbnail contract failures:\n%s" % "\n".join(failures))
		quit(1)
