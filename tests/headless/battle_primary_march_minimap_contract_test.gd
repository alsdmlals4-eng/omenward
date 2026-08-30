# 전투 우선 화면과 전진 미니맵이 동일한 단일 전선 상태를 읽는지 검증한다.
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
	_expect(battle_focus != null, "BATTLE presents a dedicated central battle focus viewport", failures)
	_expect(march_minimap != null, "BATTLE presents a compact march minimap", failures)
	_expect(screen.get_node_or_null("StrategicMap") == null, "the wide strategic map is no longer the player-facing battle surface", failures)
	if battle_focus != null:
		_expect(battle_focus.has_method("bind_run"), "battle focus reads the live run without writing combat state", failures)
	if march_minimap != null:
		_expect(march_minimap.has_method("bind_run"), "march minimap reads the live run", failures)
		_expect(march_minimap.has_method("front_count"), "march minimap exposes one active front", failures)
		_expect(march_minimap.has_method("fixed_tower_count"), "march minimap exposes the one fixed tower", failures)
		_expect(march_minimap.has_method("route_state_for"), "march minimap projects five-sector route state", failures)
		_expect(march_minimap.has_method("is_read_only"), "march minimap declares itself read-only", failures)
		_expect(march_minimap.get_rect().size.x < 360.0, "march minimap stays compact beside the battle focus", failures)
	if battle_focus != null and march_minimap != null:
		_expect(battle_focus.get_rect().size.x > march_minimap.get_rect().size.x * 1.5, "battle focus owns more visual width than the minimap", failures)
	var run: Variant = _new_run()
	root.add_child(screen)
	await process_frame
	screen.bind_run(run)
	_expect(not battle_focus.visible and not march_minimap.visible, "PREPARE does not pretend that the battle image is already live", failures)
	_expect(run.install_building(&"barracks"), "runtime fixture adds a unit-token source before spinning", failures)
	_expect(run.begin_roulette_session({"seed": 2}), "runtime fixture opens a paid roulette session", failures)
	run.roulette_session["board"] = [&"x", &"x", &"x", &"warrior", &"warrior", &"warrior", &"gold", &"warrior", &"x"]
	_expect(run.lock_roulette_result(), "runtime fixture locks a unit-producing result", failures)
	_expect(run.confirm_roulette_result(), "runtime fixture confirms the unit-producing result", failures)
	_expect(run.confirm_pending_deployment(), "runtime fixture commits the earned unit to the single front", failures)
	screen.call("_refresh")
	await process_frame
	_expect(battle_focus.visible and march_minimap.visible, "BATTLE shows the live battle focus and minimap together", failures)
	var front_units: Array = run.battle.front_units(&"front")
	_expect(front_units.size() == 1, "battle fixture has one deployed Shield Guard to render", failures)
	if battle_focus != null and front_units.size() == 1:
		_expect(is_equal_approx(battle_focus.unit_health_ratio(front_units[0]), 1.0), "battle focus reads UnitInstance health through its actual combat-stat schema", failures)
	screen.queue_free()
	await process_frame
	_finish(failures)


func _new_run() -> Variant:
	var progression := StageProgression.new()
	progression.regular_unlocked = true
	var run := StageRun.new(progression)
	run.start(ResourceLoader.load(REGULAR_STAGE_PATH), 4102)
	return run


func _expect(condition: bool, message: String, failures: Array[String]) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: Array[String]) -> void:
	if failures.is_empty():
		print("PASS: battle-primary march-minimap contract")
		quit(0)
	else:
		printerr("FAIL: battle-primary march-minimap contract\n- " + "\n- ".join(failures))
		quit(1)
