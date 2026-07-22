extends SceneTree

const DataRegistry = preload("res://scripts/core/data_registry.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const TUTORIAL_STAGE_PATH := "res://data/stages/tutorial_stage.tres"
const REGULAR_STAGE_PATH := "res://data/stages/regular_stage.tres"


func _init() -> void:
	var failures := PackedStringArray()
	var stage_run_script := load("res://scripts/core/stage_run.gd")
	var progression_script := load("res://scripts/core/stage_progression.gd")
	var wave_director_script := load("res://scripts/waves/wave_director.gd")
	var bypass_script := load("res://scripts/battle/assassin_bypass_state.gd")
	var battle_script := load("res://scripts/battle/battle_simulator.gd")
	_expect(stage_run_script != null, "stage run service exists", failures)
	_expect(progression_script != null, "stage progression service exists", failures)
	_expect(wave_director_script != null, "wave director service exists", failures)
	_expect(bypass_script != null, "assassin bypass state exists", failures)
	if stage_run_script != null and progression_script != null:
		_test_tutorial_unlock_and_regular_wave_progression(stage_run_script, progression_script, failures)
	if stage_run_script != null and progression_script != null:
		_test_roulette_storage_and_deployment(stage_run_script, progression_script, failures)
	if bypass_script != null:
		_test_assassin_bypass_timing(bypass_script, failures)
	if bypass_script != null and battle_script != null:
		_test_assassin_bypass_leaves_and_returns_to_same_lane(battle_script, failures)
	_finish(failures)


func _test_tutorial_unlock_and_regular_wave_progression(stage_run_script: GDScript, progression_script: GDScript, failures: PackedStringArray) -> void:
	var tutorial: Resource = ResourceLoader.load(TUTORIAL_STAGE_PATH)
	var regular: Resource = ResourceLoader.load(REGULAR_STAGE_PATH)
	var progression: Variant = progression_script.new()
	var run: Variant = stage_run_script.new(progression)
	run.start(tutorial, 1001)
	_expect(run.result_state == &"running", "stage run begins with the tutorial", failures)
	_advance_waves(run, 4)
	_expect(run.current_wave == 4, "tutorial reaches W4 from its declared data", failures)
	run.submit_command({"action": "stage_victory"})
	_expect(progression.regular_unlocked, "tutorial victory unlocks the regular stage for this session", failures)
	run.start(regular, 1001)
	_advance_waves(run, 15)
	_expect(run.current_wave == 15, "regular progression reaches W15", failures)
	_expect(run.wave_director.current_wave().boss_kind == &"legendary", "W15 uses the existing legendary wave definition", failures)
	_advance_waves(run, 16)
	for wave_number in range(16, 20):
		_expect(run.wave_director.wave_at(wave_number).is_overtime, "W%s is marked as overtime" % wave_number, failures)
	_advance_waves(run, 20)
	_expect(run.current_wave == 20, "regular progression reaches W20", failures)
	_expect(run.wave_director.current_wave().boss_kind == &"mythic", "W20 uses the existing mythic wave definition", failures)


func _test_roulette_storage_and_deployment(stage_run_script: GDScript, progression_script: GDScript, failures: PackedStringArray) -> void:
	var tutorial: Resource = ResourceLoader.load(TUTORIAL_STAGE_PATH)
	var run: Variant = stage_run_script.new(progression_script.new())
	run.start(tutorial, 2002)
	_expect(run.construct_home(&"barracks"), "the stage can build the approved basic barracks", failures)
	var result: Variant = run.roulette.resolve_board_snapshot([
		&"x", &"gold", &"x",
		&"warrior", &"warrior", &"warrior",
		&"gold", &"x", &"gold",
	], run.buildings.roulette_token_sources(), 17, 20, false)
	_expect(run.store_roulette_result(result), "a unit roulette result enters stage-owned storage", failures)
	_expect(run.pending_roulette_rewards.size() == 1, "one unit reward remains pending without consuming food", failures)
	var blocked: Variant = run.spin_roulette({"seed": 1})
	_expect(not blocked.accepted and blocked.failure_reason == &"pending_reward", "pending storage blocks only the next roulette spin", failures)
	_expect(run.deploy_next_roulette_reward(&"top"), "the stored reward can be committed to one lane", failures)
	_expect(run.pending_roulette_rewards.is_empty(), "successful deployment clears the stored reward", failures)


func _test_assassin_bypass_timing(bypass_script: GDScript, failures: PackedStringArray) -> void:
	var bypass: Variant = bypass_script.new(&"middle", 500.0)
	_expect(bypass.capture_power == 0.0, "assassin bypass never contributes capture power", failures)
	bypass.advance(1.0)
	_expect(bypass.state == &"travel", "assassin enters travel after one second of windup", failures)
	bypass.advance(6.49)
	_expect(not bypass.warning_active, "warning remains hidden until 2.5 seconds before arrival", failures)
	bypass.advance(0.01)
	_expect(bypass.warning_active, "warning activates exactly 2.5 seconds before arrival", failures)
	bypass.advance(2.5)
	_expect(bypass.state == &"recovery" and bypass.exit_position == 620.0, "assassin arrives in the same lane 120 units behind the enemy outpost", failures)
	bypass.advance(0.6)
	_expect(bypass.is_complete(), "assassin completes the required 0.6 second arrival recovery", failures)


func _test_assassin_bypass_leaves_and_returns_to_same_lane(battle_script: GDScript, failures: PackedStringArray) -> void:
	var battle: Variant = battle_script.new(_registry(), 11)
	var assassin := UnitSpawnDefinition.new()
	assassin.archetype_id = &"assassin"
	assassin.owner_team_id = &"lumern"
	assassin.visual_faction_id = &"lumern"
	assassin.lane_id = &"bottom"
	var unit: Variant = battle.spawn_unit(assassin)
	_expect(battle.request_assassin_bypass(unit, 100.0), "assassin can start its same-lane bypass", failures)
	battle.advance(1.0)
	_expect(battle.lanes[&"bottom"].units.is_empty(), "assassin is removed from the lane during travel", failures)
	battle.advance(9.6)
	_expect(battle.lanes[&"bottom"].units.size() == 1, "assassin returns to its original lane after recovery", failures)
	_expect(is_equal_approx(float(battle.lanes[&"bottom"].units[0].lane_position), 220.0), "assassin returns behind the same lane enemy outpost", failures)


func _advance_waves(run: Variant, target_wave: int) -> void:
	while run.current_wave < target_wave:
		run.advance(60.0)


func _registry() -> Variant:
	var registry := DataRegistry.new()
	var errors: PackedStringArray = registry.load_bootstrap_catalog(BOOTSTRAP_CATALOG_PATH)
	if not errors.is_empty():
		push_error("stage run test registry failed to load: %s" % errors)
	return registry


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Stage run, wave, progression, and assassin bypass checks passed")
		quit(0)
	else:
		printerr("Stage run, wave, progression, and assassin bypass failures:\n%s" % "\n".join(failures))
		quit(1)
