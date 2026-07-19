# 기획된 독립 3레인 전장 표현이 회색 박스 표기를 대체했는지 검증한다.
extends SceneTree

const BATTLEFIELD_VIEW_PATH := "res://scripts/battle/battlefield_view.gd"


func _init() -> void:
	var failures := PackedStringArray()
	var source := FileAccess.get_file_as_string(BATTLEFIELD_VIEW_PATH)
	_expect(not source.contains("BATTLEFIELD GRAYBOX"), "battlefield no longer labels itself as a graybox", failures)
	_expect(source.contains("FRIENDLY_OUTPOST_X") and source.contains("ENEMY_OUTPOST_X"), "battlefield explicitly draws both independent-lane outposts", failures)
	_expect(source.contains("CENTER_CLASH_X"), "battlefield explicitly draws each lane clash zone", failures)
	if failures.is_empty():
		print("Battlefield visual contracts passed")
		quit(0)
	else:
		printerr("Battlefield visual contract failures:\n%s" % "\n".join(failures))
		quit(1)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)
