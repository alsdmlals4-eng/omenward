# 룰렛 선택 UI가 게임 규칙과 분리된 표시 상태를 유지하는지 검증한다.
extends SceneTree

const RUN_COMMAND_SCREEN_PATH := "res://scenes/ui/run_command_screen.tscn"
const BATTLEFIELD_SCENE_PATH := "res://scenes/battle/battlefield.tscn"


func _init() -> void:
	var failures := PackedStringArray()
	var battlefield := (load(BATTLEFIELD_SCENE_PATH) as PackedScene).instantiate()
	var backdrop := battlefield.get_node_or_null("Backdrop") as Sprite2D
	_expect(backdrop != null, "battlefield owns a project backdrop node", failures)
	if backdrop != null:
		_expect(backdrop.scale.x >= 0.64 and backdrop.scale.y >= 0.64, "battlefield backdrop is enlarged beyond a distant-map scale", failures)
	battlefield.queue_free()
	var screen := (load(RUN_COMMAND_SCREEN_PATH) as PackedScene).instantiate()
	var result_list := screen.get_node_or_null("LowerDeck/RoulettePanel/ResultList")
	_expect(result_list is GridContainer, "roulette exposes all nine inspected results as a compact grid", failures)
	if result_list is GridContainer:
		_expect(result_list.columns == 3, "roulette inspection grid keeps three visible columns", failures)
	var front_panel := screen.get_node_or_null("Fronts/Top") as Panel
	var front_style := front_panel.get_theme_stylebox("panel") if front_panel != null else null
	_expect(front_style is StyleBoxFlat and (front_style as StyleBoxFlat).bg_color.a <= 0.45, "front cards remain translucent so the battlefield is primary", failures)
	_expect(screen.has_method("select_roulette_tile"), "roulette screen exposes UI-only tile selection", failures)
	_expect(screen.has_method("selected_roulette_tile_index"), "roulette screen exposes current selected tile index", failures)
	if screen.has_method("select_roulette_tile"):
		screen.select_roulette_tile(4)
	if screen.has_method("selected_roulette_tile_index"):
		_expect(screen.selected_roulette_tile_index() == 4, "roulette selection stores the inspected tile only", failures)
	screen.queue_free()
	_finish(failures)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Roulette picker UI checks passed")
		quit(0)
	else:
		printerr("Roulette picker UI failures:\n%s" % "\n".join(failures))
		quit(1)
