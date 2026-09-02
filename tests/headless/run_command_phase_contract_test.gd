# Run Command의 단계 전이와 원자적 커밋 경계를 검증한다.
extends SceneTree

const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")
const TUTORIAL_STAGE_PATH := "res://data/stages/tutorial_stage.tres"


func _init() -> void:
	var failures := PackedStringArray()
	var tutorial := ResourceLoader.load(TUTORIAL_STAGE_PATH)
	var run: Variant = StageRun.new(StageProgression.new())
	run.start(tutorial, 8101)
	_expect(run.command_phase == &"prepare", "a new run begins in PREPARE", failures)
	_expect(run.has_method("begin_roulette_session"), "StageRun exposes a stopped-board roulette entry", failures)
	_expect(run.has_method("lock_roulette_result"), "StageRun exposes a separate result review action", failures)
	_expect(run.has_method("confirm_pending_deployment"), "StageRun exposes atomic deployment confirmation", failures)
	var wave_before := int(run.current_wave)
	run.advance(60.0)
	_expect(int(run.current_wave) == wave_before, "PREPARE does not advance wave, combat, or economy time", failures)
	_expect(not run.install_building(&"barracks"), "Stage 1 PREPARE keeps the global roster read-only", failures)
	var gold_before_spin := int(run.economy.gold)
	_expect(run.begin_roulette_session({"seed": 8102}), "PREPARE starts one paid stopped-board session", failures)
	_expect(run.command_phase == &"stopped_3x3", "paid spin reaches STOPPED_3X3", failures)
	_expect(int(run.economy.gold) == gold_before_spin - 20, "paid stopped-board session spends gold exactly once", failures)
	var gold_before_preview := int(run.economy.gold)
	run.preview_roulette_result()
	_expect(int(run.economy.gold) == gold_before_preview, "result preview does not spend gold", failures)
	_expect(run.move_roulette_row(1, 1), "one direct row arrow executes a move", failures)
	_expect(run.command_phase == &"manipulate" and int(run.roulette_moves_remaining) == 2, "executed move enters MANIPULATE and consumes one move", failures)
	_expect(str((run.manifest.input_log.back() as Dictionary).get("action", "")) == "roulette_move", "executed move records the irreversible session action", failures)
	_expect(run.lock_roulette_result(), "stopped board enters a separate result confirmation", failures)
	_expect(run.command_phase == &"result_confirm", "result review uses RESULT_CONFIRM", failures)
	_expect(run.confirm_roulette_result(), "confirmed roulette result resolves through the canonical service", failures)
	_expect(run.command_phase == &"commit", "confirmed result enters COMMIT without auto-deploy", failures)
	if run.pending_roulette_rewards.is_empty():
		_expect(run.begin_battle(), "empty reward result can still enter BATTLE", failures)
	else:
		_expect(run.confirm_pending_deployment(), "COMMIT applies the pending rewards to the single irreversible front and enters BATTLE", failures)
	_expect(run.command_phase == &"battle", "the valid command path reaches BATTLE", failures)
	run.advance(60.0)
	_expect(int(run.current_wave) > wave_before, "BATTLE advances wave time", failures)
	run.submit_command({"action": "stage_victory"})
	_expect(run.command_phase == &"review", "an actual stage outcome enters REVIEW", failures)
	_test_reward_commit_path(tutorial, failures)
	_finish(failures)


func _test_reward_commit_path(tutorial: Resource, failures: PackedStringArray) -> void:
	var run: Variant = StageRun.new(StageProgression.new())
	run.start(tutorial, 8103)
	var reward := UnitSpawnDefinition.new()
	reward.archetype_id = &"shield_guard"
	reward.owner_team_id = &"lumern"
	reward.visual_faction_id = &"lumern"
	reward.food_cost = 1
	run.pending_roulette_rewards.append(reward)
	run.command_phase = run.COMMIT
	_expect(not run.assign_pending_reward(0, &"top"), "reward COMMIT rejects removed three-front identifiers", failures)
	_expect(run.assign_pending_reward(0, &"front"), "reward COMMIT accepts the one irreversible front", failures)
	_expect(run.confirm_pending_deployment(), "reward COMMIT atomically reserves, spawns, logs, and enters BATTLE", failures)
	_expect(int(run.economy.food_used) == 1, "reward COMMIT reserves food once", failures)
	_expect(run.battle.front_units(&"front").size() == 1, "reward COMMIT spawns on the one front", failures)
	_expect(str((run.manifest.input_log.back() as Dictionary).get("action", "")) == "commit_deployment", "reward COMMIT writes one aggregate command", failures)


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Run Command phase contracts passed")
		quit(0)
	else:
		printerr("Run Command phase contract failures:\n%s" % "\n".join(failures))
		quit(1)
