# 메인 진입은 준비가 끝난 뒤 실제 튜토리얼만 시작하며, 존재하지 않는 메뉴 기능을 약속하지 않는다.
extends SceneTree

const MAIN_SCENE_PATH := "res://scenes/main/main.tscn"
const TITLE_SCENE_PATH := "res://scenes/ui/title_screen.tscn"


func _init() -> void:
	var failures := PackedStringArray()
	var main_scene_text := FileAccess.get_file_as_string(MAIN_SCENE_PATH)
	_expect(FileAccess.file_exists(TITLE_SCENE_PATH), "main entry owns a dedicated title screen scene", failures)
	_expect(main_scene_text.contains('res://scenes/ui/title_screen.tscn'), "main scene references the dedicated title screen", failures)
	_expect(main_scene_text.contains('[node name="RunCommandScreen" parent="UI" instance=ExtResource("5_command")]\nvisible = false'), "Run Command stays hidden before the title action", failures)
	if FileAccess.file_exists(TITLE_SCENE_PATH):
		var title_packed := load(TITLE_SCENE_PATH) as PackedScene
		_expect(title_packed != null, "title screen scene loads", failures)
		if title_packed != null:
			var title_screen := title_packed.instantiate()
			_expect(title_screen.get_node_or_null("Panel/StartExpeditionButton") is Button, "title exposes one actual expedition action", failures)
			title_screen.free()
		var title_scene_text := FileAccess.get_file_as_string(TITLE_SCENE_PATH)
		_expect(title_scene_text.contains('text = "원정 시작"'), "title start action is labeled for the real expedition", failures)
		_expect(not title_scene_text.contains("계속하기"), "title does not claim an unimplemented save continuation", failures)
		_expect(not title_scene_text.contains("설정"), "title does not claim an unimplemented settings surface", failures)
	_finish(failures)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Title entry contracts passed")
		quit(0)
	else:
		printerr("Title entry contract failures:\n%s" % "\n".join(failures))
		quit(1)
