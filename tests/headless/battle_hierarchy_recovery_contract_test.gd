# 전투 우선 블루프린트 V2가 BATTLE에서만 화면 질량을 전투로 옮기는지 검증한다.
extends SceneTree

const RUN_COMMAND_SCREEN_PATH := "res://scenes/ui/run_command_screen.tscn"
const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")
const REGULAR_STAGE_PATH := "res://data/stages/regular_stage.tres"

var failures: Array[String] = []


func _init() -> void:
	call_deferred("_run")


func _run() -> void:
	var screen := (load(RUN_COMMAND_SCREEN_PATH) as PackedScene).instantiate()
	var battle_focus := screen.get_node_or_null("BattleFocusViewport") as Control
	var march_minimap := screen.get_node_or_null("MarchMinimap") as Control
	var lower_deck := screen.get_node_or_null("LowerDeck") as Control
	_expect(battle_focus != null, "V2 needs the existing BattleFocus viewport", failures)
	_expect(march_minimap != null, "V2 needs the existing MarchMinimap", failures)
	_expect(lower_deck != null, "V2 needs the phase-appropriate LowerDeck", failures)
	root.add_child(screen)
	await process_frame
	var run: Variant = _new_run()
	screen.bind_run(run)
	await process_frame
	if lower_deck != null:
		_expect(lower_deck.size == Vector2(928, 164), "non-BATTLE retains the existing 928x164 work deck", failures)
	if battle_focus != null:
		_expect(battle_focus.has_method("role_display_cell_size"), "battle focus declares its V2 readable role cell", failures)
		if battle_focus.has_method("role_display_cell_size"):
			_expect(battle_focus.call("role_display_cell_size") == Vector2(104, 104), "role art renders in the V2 104px display cell", failures)
	if march_minimap != null:
		_expect(march_minimap.has_method("presentation_contract"), "march minimap declares its V2 context-ribbon contract", failures)
		if march_minimap.has_method("presentation_contract"):
			_expect(
				march_minimap.call("presentation_contract") == {
					"front_count": 1,
					"sector_count": 5,
					"top_single_row": true,
					"read_only": true,
					"unit_replication": false,
				},
				"march minimap remains a five-sector read-only context ribbon",
				failures
			)
	_enter_battle(run)
	screen.call("_refresh")
	await process_frame
	if battle_focus != null:
		_expect(battle_focus.visible, "BATTLE shows the close battle view", failures)
		_expect(battle_focus.get_rect().position == Vector2(16, 110), "BATTLE places the battle focus below the top ribbon", failures)
		_expect(battle_focus.size == Vector2(926, 304), "BATTLE grants the close battle the recovered visual height", failures)
	if march_minimap != null:
		_expect(march_minimap.visible, "BATTLE shows the top march ribbon", failures)
		_expect(march_minimap.get_rect().position == Vector2(16, 62), "march ribbon keeps its top context position", failures)
		_expect(march_minimap.size == Vector2(926, 40), "march ribbon remains a single compact row", failures)
	if lower_deck != null:
		_expect(lower_deck.get_rect().position == Vector2(16, 422), "BATTLE moves the action deck below the enlarged combat frame", failures)
		_expect(lower_deck.size == Vector2(928, 106), "BATTLE compresses the explanatory deck", failures)
	screen.queue_free()
	await process_frame
	_finish(failures)


func _enter_battle(run: Variant) -> void:
	_expect(run.install_building(&"barracks"), "fixture installs a token source", failures)
	_expect(run.begin_roulette_session({"seed": 2}), "fixture opens the roulette session", failures)
	run.roulette_session["board"] = [&"x", &"x", &"x", &"warrior", &"warrior", &"warrior", &"gold", &"warrior", &"x"]
	_expect(run.lock_roulette_result(), "fixture locks a unit-producing roulette result", failures)
	_expect(run.confirm_roulette_result(), "fixture confirms the roulette result", failures)
	_expect(run.confirm_pending_deployment(), "fixture commits the earned unit to the only active front", failures)


func _new_run() -> Variant:
	var progression := StageProgression.new()
	progression.regular_unlocked = true
	var run := StageRun.new(progression)
	run.start(ResourceLoader.load(REGULAR_STAGE_PATH), 4103)
	return run


func _expect(condition: bool, message: String, failures: Array[String]) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("PASS: battle-primary hierarchy recovery contract")
		quit(0)
	else:
		printerr("FAIL: battle-primary hierarchy recovery contract\n- " + "\n- ".join(failures))
		quit(1)
