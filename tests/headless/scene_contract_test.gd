extends SceneTree

const MAIN_SCENE_PATH := "res://scenes/main/main.tscn"
const BATTLEFIELD_SCENE_PATH := "res://scenes/battle/battlefield.tscn"
const STAGE_HUD_SCENE_PATH := "res://scenes/ui/stage_hud.tscn"
const RUN_COMMAND_SCREEN_PATH := "res://scenes/ui/run_command_screen.tscn"
const STAGE_SELECT_SCENE_PATH := "res://scenes/ui/stage_select.tscn"
const UNIT_SCENE_PATH := "res://scenes/units/unit.tscn"


func _init() -> void:
	var failures := PackedStringArray()
	var main_packed := load(MAIN_SCENE_PATH) as PackedScene
	_expect(main_packed != null, "main scene loads", failures)
	if main_packed != null:
		var main := main_packed.instantiate()
		_expect(main.get_node_or_null("Battlefield") != null, "main includes battlefield", failures)
		_expect(main.get_node_or_null("UI/StageHud") != null, "main includes stage HUD", failures)
		_expect(main.get_node_or_null("UI/RunCommandScreen") != null, "main includes the player-facing Run Command screen", failures)
		_expect(main.get_node_or_null("UI/StageSelect") != null, "main includes stage select", failures)
		var session := main.get_node_or_null("GameSession")
		_expect(session != null and session.has_method("start_stage"), "game session can start a selected stage", failures)
		_expect(session != null and session.has_method("retry_stage"), "game session can retry the current stage", failures)
		main.queue_free()
	_assert_scene_contract(BATTLEFIELD_SCENE_PATH, "bind_run", "battlefield scene binds a stage run", failures)
	_assert_scene_contract(STAGE_HUD_SCENE_PATH, "bind_run", "stage HUD binds a stage run", failures)
	_assert_scene_contract(RUN_COMMAND_SCREEN_PATH, "bind_run", "Run Command screen binds a stage run", failures)
	_assert_global_roster_ui_contract(failures)
	_assert_strategic_map_ui_contract(failures)
	_assert_scene_contract(STAGE_SELECT_SCENE_PATH, "stage_requested", "stage select emits stage requests", failures)
	_assert_scene_contract(UNIT_SCENE_PATH, "bind_unit", "shared unit scene binds a unit instance", failures)
	_expect(not FileAccess.file_exists("res://scenes/units/enemy_unit.tscn"), "no enemy unit scene is created", failures)
	_finish(failures)


func _assert_scene_contract(scene_path: String, requirement: String, message: String, failures: PackedStringArray) -> void:
	var packed := load(scene_path) as PackedScene
	_expect(packed != null, "%s loads" % scene_path, failures)
	if packed == null:
		return
	var instance := packed.instantiate()
	var fulfilled := instance.has_method(requirement) if requirement.begins_with("bind_") else instance.has_signal(requirement)
	_expect(fulfilled, message, failures)
	instance.queue_free()


func _assert_global_roster_ui_contract(failures: PackedStringArray) -> void:
	var packed := load(RUN_COMMAND_SCREEN_PATH) as PackedScene
	if packed == null:
		return
	var screen := packed.instantiate()
	var roster := screen.get_node_or_null("LowerDeck/PreparePanel/BuildingRoster")
	_expect(roster is ItemList, "PREPARE exposes the global building roster as a selectable list", failures)
	_expect(screen.get_node_or_null("LowerDeck/PreparePanel/RosterMoveUpButton") is Button, "PREPARE exposes a roster priority-up action", failures)
	_expect(screen.get_node_or_null("LowerDeck/PreparePanel/RosterMoveDownButton") is Button, "PREPARE exposes a roster priority-down action", failures)
	screen.queue_free()


func _assert_strategic_map_ui_contract(failures: PackedStringArray) -> void:
	var packed := load(RUN_COMMAND_SCREEN_PATH) as PackedScene
	if packed == null:
		return
	var screen := packed.instantiate()
	var strategic_map := screen.get_node_or_null("StrategicMap") as Control
	_expect(strategic_map != null, "Run Command exposes one primary strategic map", failures)
	_expect(screen.get_node_or_null("Fronts") == null, "Run Command no longer exposes three progress-card minimaps", failures)
	if strategic_map != null:
		_expect(strategic_map.has_method("bind_run"), "strategic map consumes a stage run read-only", failures)
		_expect(strategic_map.has_method("fixed_tower_count"), "strategic map exposes fixed tower presentation count", failures)
	screen.queue_free()


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Playable scene contracts passed")
		quit(0)
	else:
		printerr("Playable scene contract failures:\n%s" % "\n".join(failures))
		quit(1)
