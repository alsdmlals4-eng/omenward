# P0 HUD 자원 지표가 승인 아이콘과 숫자 라벨을 함께 제공하는지 검증한다.
extends SceneTree

const STAGE_HUD_SCENE_PATH := "res://scenes/ui/stage_hud.tscn"
const EXPECTED_ICON_PATHS := {
	&"GoldIcon": "res://assets/art/ui/gold_resource_indicator.png",
	&"CapacityIcon": "res://assets/art/ui/troop_capacity_resource_indicator.png",
}
const EXPECTED_LABELS := [&"GoldLabel", &"FoodLabel"]


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
		for icon_name in EXPECTED_ICON_PATHS:
			var icon := stage_hud.get_node_or_null(NodePath(icon_name)) as TextureRect
			var expected_path: String = EXPECTED_ICON_PATHS[icon_name]
			_expect(FileAccess.file_exists(expected_path), "%s runtime texture is available" % icon_name, failures)
			_expect(icon != null and icon.texture != null, "%s loads an approved runtime texture" % icon_name, failures)
			_expect(icon != null and icon.texture != null and icon.texture.resource_path == expected_path, "%s uses the mapped local texture" % icon_name, failures)
		for label_name in EXPECTED_LABELS:
			_expect(stage_hud.get_node_or_null(NodePath(label_name)) is Label, "%s preserves a numeric resource label" % label_name, failures)
		stage_hud.queue_free()
	_finish(failures)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("P0 HUD resource indicator icon contracts passed")
		quit(0)
	else:
		printerr("P0 HUD resource indicator icon contract failures:\n%s" % "\n".join(failures))
		quit(1)
