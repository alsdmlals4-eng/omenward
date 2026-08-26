# Run Command UI 파생 이미지의 로컬 경로·규격·알파를 검증한다.
extends SceneTree

const EXPECTED_ASSETS := {

	"roulette_board_frame": {"path": "res://assets/art/ui/run_command/roulette_board_frame.png", "size": Vector2i(180, 180)},
	"roulette_arrow": {"path": "res://assets/art/ui/run_command/roulette_arrow.png", "size": Vector2i(28, 28)},
	"omen_device": {"path": "res://assets/art/ui/run_command/omen_device.png", "size": Vector2i(72, 76)},
	"token_x": {"path": "res://assets/art/ui/run_command/token_x.png", "size": Vector2i(34, 34)},
	"token_gold": {"path": "res://assets/art/ui/run_command/token_gold.png", "size": Vector2i(34, 34)},
	"token_frame": {"path": "res://assets/art/ui/run_command/token_frame.png", "size": Vector2i(34, 34)},
	"token_state": {"path": "res://assets/art/ui/run_command/token_state.png", "size": Vector2i(34, 34)},
}


func _init() -> void:
	var failures := PackedStringArray()
	for asset_id in EXPECTED_ASSETS:
		var contract: Dictionary = EXPECTED_ASSETS[asset_id]
		var path := str(contract["path"])
		_expect(ResourceLoader.exists(path), "%s runtime derivative exists" % asset_id, failures)
		if not ResourceLoader.exists(path):
			continue
		var image := Image.load_from_file(path)
		_expect(not image.is_empty(), "%s runtime derivative loads" % asset_id, failures)
		_expect(image.get_size() == contract["size"], "%s has the approved runtime size" % asset_id, failures)
		_expect(image.get_format() in [Image.FORMAT_RGBA8, Image.FORMAT_RGBA4444], "%s preserves RGBA data" % asset_id, failures)
		_expect(image.get_pixel(0, 0).a <= 0.01, "%s keeps a transparent corner" % asset_id, failures)
	_finish(failures)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Run Command visual asset checks passed")
		quit(0)
	else:
		printerr("Run Command visual asset failures:\n%s" % "\n".join(failures))
		quit(1)
