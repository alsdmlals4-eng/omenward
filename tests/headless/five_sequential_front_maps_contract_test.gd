# 다섯 전선 맵은 병렬 전선이나 선택 메뉴가 아니라 한 방향 순차 진행이어야 한다.
extends SceneTree

const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")

const REGULAR_STAGE_PATH := "res://data/stages/regular_stage.tres"
const FRONT_MAP_IDS := [&"ward_citadel", &"ward_forward", &"clash", &"veil_forward", &"veil_citadel"]


func _init() -> void:
	var failures := PackedStringArray()
	var progression := StageProgression.new()
	progression.regular_unlocked = true
	var run := StageRun.new(progression)
	run.start(ResourceLoader.load(REGULAR_STAGE_PATH), 9301)
	_expect(run.has_method(&"front_map_snapshot"), "StageRun exposes a read-only five-map progress snapshot", failures)
	_expect(run.has_method(&"current_front_map"), "StageRun exposes the one active map package", failures)
	_expect(run.has_method(&"can_enter_next_front_map"), "StageRun exposes an explicit next-map availability query", failures)
	_expect(run.has_method(&"enter_next_front_map"), "StageRun owns the explicit next-map transition", failures)
	if run.has_method(&"front_map_snapshot"):
		_assert_initial_map_state(run, failures)
		_assert_sequential_transition(run, failures)
		_assert_final_map_only_victory(run, failures)
	_assert_natural_victory_requires_full_wave_package_and_preserves_survivor(failures)
	_assert_veil_bypass_blocks_natural_map_clear(failures)
	_finish(failures)


func _assert_initial_map_state(run: Variant, failures: PackedStringArray) -> void:
	var maps: Array = run.front_map_snapshot()
	_expect(maps.size() == 5, "regular Stage exposes exactly five front map packages", failures)
	if maps.size() != 5:
		return
	for index in maps.size():
		var entry: Dictionary = maps[index] as Dictionary
		_expect(StringName(entry.get("map_id", &"")) == FRONT_MAP_IDS[index], "map order matches the one-way Ward-to-Veil route", failures)
		_expect(StringName(entry.get("state", &"")) == (&"current" if index == 0 else &"locked"), "only the first map is current at start", failures)
		_expect(not bool(entry.get("selectable", true)), "the top progress ribbon never becomes a map selection control", failures)
	var current: Dictionary = run.current_front_map()
	_expect(StringName(current.get("map_id", &"")) == &"ward_citadel", "the active battle opens at Ward Citadel", failures)
	_expect(current.get("wave_first", 0) == 1 and current.get("wave_last", 0) == 4, "Ward Citadel owns W1 through W4", failures)


func _assert_sequential_transition(run: Variant, failures: PackedStringArray) -> void:
	_expect(run.install_building(&"barracks"), "global roster can be prepared before the first map", failures)
	var roster_before: Array = run.building_roster_snapshot().duplicate(true)
	var gold_before := int(run.economy.gold)
	run.submit_command({"action": "stage_victory"})
	_expect(run.result_state == run.RUNNING, "a non-final map victory does not finish the StageRun", failures)
	_expect(run.command_phase == run.REVIEW, "a non-final map victory enters REVIEW", failures)
	_expect(run.can_enter_next_front_map(), "only a cleared non-final map enables the next-map action", failures)
	var cleared: Array = run.front_map_snapshot()
	if cleared.size() == 5:
		_expect(StringName((cleared[0] as Dictionary).get("state", &"")) == &"cleared", "the completed map is marked cleared", failures)
		_expect(StringName((cleared[1] as Dictionary).get("state", &"")) == &"available", "exactly the next map becomes available", failures)
		_expect(StringName((cleared[2] as Dictionary).get("state", &"")) == &"locked", "later maps remain locked", failures)
	_expect(run.enter_next_front_map(), "Review explicitly enters the next front map", failures)
	_expect(run.command_phase == run.PREPARE, "a next-map handoff reopens PREPARE", failures)
	_expect(run.result_state == run.RUNNING, "a next-map handoff retains the overall running state", failures)
	_expect(run.front_map_index == 1, "the second map is the only active map after handoff", failures)
	_expect(run.building_roster_snapshot() == roster_before, "global building roster persists across a front-map handoff", failures)
	_expect(int(run.economy.gold) == gold_before, "map handoff does not reset global gold", failures)
	var current: Dictionary = run.current_front_map()
	_expect(StringName(current.get("map_id", &"")) == &"ward_forward", "handoff changes the battle package to Ward Forward", failures)
	_expect(current.get("wave_first", 0) == 5 and current.get("wave_last", 0) == 8, "Ward Forward owns W5 through W8", failures)


func _assert_final_map_only_victory(run: Variant, failures: PackedStringArray) -> void:
	while run.front_map_index < 4:
		run.submit_command({"action": "stage_victory"})
		_expect(run.result_state == run.RUNNING, "maps before Veil Citadel cannot resolve final victory", failures)
		_expect(run.enter_next_front_map(), "every cleared non-final map hands off to exactly one next map", failures)
	run.submit_command({"action": "stage_victory"})
	_expect(run.result_state == run.VICTORY, "Veil Citadel victory is the only final StageRun victory", failures)
	_expect(not run.can_enter_next_front_map(), "final victory exposes no sixth map", failures)
	var completed_maps: Array = run.front_map_snapshot()
	if completed_maps.size() == 5:
		_expect(completed_maps.all(func(entry: Dictionary) -> bool: return StringName(entry.get("state", &"")) == &"cleared"), "final victory marks all five maps cleared", failures)


func _assert_natural_victory_requires_full_wave_package_and_preserves_survivor(failures: PackedStringArray) -> void:
	var progression := StageProgression.new()
	progression.regular_unlocked = true
	var run := StageRun.new(progression)
	run.start(ResourceLoader.load(REGULAR_STAGE_PATH), 9302)
	_prepare_first_map_base_result_before_wave_package(run, failures)
	if run.command_phase != run.BATTLE:
		return
	_finish_current_wave_package_without_veil_front_units(run)
	var survivor_spawn := UnitSpawnDefinition.new()
	survivor_spawn.archetype_id = &"assassin"
	survivor_spawn.owner_team_id = &"lumern"
	survivor_spawn.visual_faction_id = &"lumern"
	survivor_spawn.lane_id = &"front"
	var survivor: Variant = run.battle.spawn_unit(survivor_spawn)
	_expect(survivor != null, "fixture creates one living Lumern bypass survivor before the map result", failures)
	if survivor == null:
		return
	var survivor_id := int(survivor.unit_id)
	_expect(run.battle.request_assassin_bypass(survivor, 100.0), "fixture moves the Lumern assassin into an active bypass before handoff", failures)
	run.battle.advance(1.0)
	run.advance(0.1)
	_expect(run.result_state == run.RUNNING and run.command_phase == run.REVIEW, "real enemy-base destruction clears only the active non-final map after its full assigned Wave package", failures)
	_expect(run.can_enter_next_front_map(), "natural map victory exposes the explicit next-map action", failures)
	_expect(run.enter_next_front_map(), "natural-result review enters exactly the next map", failures)
	_expect(run.front_map_index == 1 and run.command_phase == run.PREPARE, "natural handoff reaches Ward Forward preparation", failures)
	_expect(run.battle.is_unit_alive(survivor_id), "a surviving Lumern bypass unit endures the local-map reset", failures)
	_expect(run.battle.get_unit_by_id(survivor_id) == survivor, "handoff preserves the bypass survivor instance rather than silently recreating it", failures)


func _assert_veil_bypass_blocks_natural_map_clear(failures: PackedStringArray) -> void:
	var progression := StageProgression.new()
	progression.regular_unlocked = true
	var run := StageRun.new(progression)
	run.start(ResourceLoader.load(REGULAR_STAGE_PATH), 9303)
	_prepare_first_map_base_result_before_wave_package(run, failures)
	if run.command_phase != run.BATTLE:
		return
	_finish_current_wave_package_without_veil_front_units(run)
	var veil_assassin_spawn := UnitSpawnDefinition.new()
	veil_assassin_spawn.archetype_id = &"assassin"
	veil_assassin_spawn.owner_team_id = &"veil"
	veil_assassin_spawn.visual_faction_id = &"veil"
	veil_assassin_spawn.lane_id = &"front"
	var veil_assassin: Variant = run.battle.spawn_unit(veil_assassin_spawn)
	_expect(veil_assassin != null, "fixture creates one living Veil bypass unit", failures)
	if veil_assassin == null:
		return
	_expect(run.battle.request_assassin_bypass(veil_assassin, 30.0), "fixture moves the Veil assassin into an active bypass", failures)
	run.battle.advance(1.0)
	run.advance(0.1)
	_expect(run.command_phase == run.BATTLE and not run.can_enter_next_front_map(), "a living Veil bypass blocks a package-clear map result", failures)
	veil_assassin.health = 0.0
	run.advance(0.1)
	_expect(run.command_phase == run.REVIEW and run.can_enter_next_front_map(), "removing the final Veil bypass allows the current map to clear", failures)


func _prepare_first_map_base_result_before_wave_package(run: Variant, failures: PackedStringArray) -> void:
	_expect(run.begin_battle(), "natural-result fixture enters the first map battle", failures)
	run.battle.objectives_enabled = false
	var veil_base: Variant = run.battle.bases.get(&"veil")
	_expect(veil_base != null, "fixture exposes the real Veil base state", failures)
	if veil_base == null:
		return
	veil_base.apply_damage(999999.0, true)
	run.advance(0.1)
	_expect(run.command_phase == run.BATTLE and not run.can_enter_next_front_map(), "enemy-base destruction before W1 through W4 cannot skip the assigned Wave package", failures)


func _finish_current_wave_package_without_veil_front_units(run: Variant) -> void:
	for _wave_index in 4:
		run.advance(60.0)
	for unit in run.battle.front_units(&"front"):
		if unit.owner_team_id == &"veil":
			unit.health = 0.0


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("PASS: five sequential front map contract")
		quit(0)
	else:
		printerr("FAIL: five sequential front map contract\n%s" % "\n".join(failures))
		quit(1)
