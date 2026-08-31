# 단일 행군 전선 계약: 공개 runtime은 하나의 front만 노출하고 세 전선 ID를 받지 않는다.
extends SceneTree

const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")

const REGULAR_STAGE_PATH := "res://data/stages/regular_stage.tres"


func _init() -> void:
	var failures := PackedStringArray()
	var run: Variant = _new_run(39001)
	_expect(run.battle != null, "regular run creates battle state", failures)
	if run.battle != null:
		_expect(run.battle.has_method("front_ids"), "battle exposes the active front collection", failures)
		_expect(run.battle.has_method("accepts_front_id"), "battle validates public front IDs", failures)
		_expect(run.battle.has_method("route_state_for"), "battle exposes one route state projection", failures)
		if run.battle.has_method("front_ids"):
			_expect(run.battle.front_ids() == [&"front"], "runtime exposes exactly one active front", failures)
		if run.battle.has_method("accepts_front_id"):
			_expect(run.battle.accepts_front_id(&"front"), "front is accepted", failures)
			_expect(not run.battle.accepts_front_id(&"top"), "legacy top ID is rejected", failures)
			_expect(not run.battle.accepts_front_id(&"middle"), "legacy middle ID is rejected", failures)
			_expect(not run.battle.accepts_front_id(&"bottom"), "legacy bottom ID is rejected", failures)
		if run.battle.has_method("route_state_for"):
			var route: Dictionary = run.battle.route_state_for(&"front")
			_expect(route.has_all(["ward_forward", "clash", "veil_forward"]), "front retains the route objectives", failures)
	_expect(run.has_method("front_slot_capacity"), "StageRun exposes single-front building capacity", failures)
	if run.has_method("front_slot_capacity"):
		_expect(run.front_slot_capacity() == 6, "opening capacity starts at six", failures)
	_expect(run.has_method("assign_pending_reward"), "StageRun exposes queued deployment assignment", failures)
	_test_legacy_spawn_rejection(run, failures)
	_test_ward_forward_first_capture(run, failures)
	_test_all_player_held_capture_points_expand_roster_capacity(run, failures)
	_test_pending_rewards_commit_without_front_selector(run, failures)
	_finish(failures)


func _test_legacy_spawn_rejection(run: Variant, failures: PackedStringArray) -> void:
	if run == null or run.battle == null or not run.battle.has_method("accepts_front_id"):
		return
	var legacy_spawn := UnitSpawnDefinition.new()
	legacy_spawn.archetype_id = &"shield_guard"
	legacy_spawn.owner_team_id = &"lumern"
	legacy_spawn.visual_faction_id = &"lumern"
	legacy_spawn.lane_id = &"top"
	_expect(not run.battle.can_spawn_unit(legacy_spawn), "legacy top spawn cannot enter the single front", failures)


func _test_ward_forward_first_capture(run: Variant, failures: PackedStringArray) -> void:
	if run == null or run.battle == null:
		return
	var battle: Variant = run.battle
	var ward_forward: Variant = battle.outposts[&"lumern"][&"front"]
	var tower: Variant = battle.fixed_towers[&"front"]
	_expect(not ward_forward.is_stable_for(&"lumern"), "Ward Forward starts unheld so it is the first occupation reward", failures)
	_expect(not tower.active, "the fixed tower is inactive until Ward Forward is stabilized", failures)
	var spawn := UnitSpawnDefinition.new()
	spawn.archetype_id = &"shield_guard"
	spawn.owner_team_id = &"lumern"
	spawn.visual_faction_id = &"lumern"
	spawn.lane_id = &"front"
	var unit: Variant = battle.spawn_unit(spawn)
	_expect(unit != null, "the active front accepts a Lumern capture unit", failures)
	if unit == null:
		return
	unit.lane_position = 30.0
	battle.advance(0.1)
	_expect(ward_forward.capturing_team_id == &"lumern", "first forward occupation begins before clash movement", failures)
	battle.advance(26.0)
	_expect(ward_forward.is_stable_for(&"lumern"), "Ward Forward stabilizes under sustained Lumern presence", failures)
	_expect(tower.active and tower.owner_team_id == &"lumern", "stabilized Ward Forward activates the one fixed tower", failures)


func _test_all_player_held_capture_points_expand_roster_capacity(run: Variant, failures: PackedStringArray) -> void:
	if run == null or run.battle == null or not run.has_method("front_slot_capacity"):
		return
	var battle: Variant = run.battle
	battle.outposts[&"lumern"][&"front"].owner_team_id = &"lumern"
	battle.outposts[&"lumern"][&"front"].state = battle.outposts[&"lumern"][&"front"].STABLE
	battle.clash_zones[&"front"].outpost.owner_team_id = &"lumern"
	battle.clash_zones[&"front"].outpost.state = battle.clash_zones[&"front"].outpost.STABLE
	battle.outposts[&"veil"][&"front"].owner_team_id = &"lumern"
	battle.outposts[&"veil"][&"front"].state = battle.outposts[&"veil"][&"front"].STABLE
	_expect(run.front_slot_capacity() == 9, "two player-held forward bases and the clash zone unlock six plus three roster slots", failures)
	battle.outposts[&"veil"][&"front"].owner_team_id = &"veil"
	battle.outposts[&"veil"][&"front"].state = battle.outposts[&"veil"][&"front"].STABLE
	_expect(run.front_slot_capacity() == 8, "losing one captured forward base immediately locks only its one bonus slot", failures)


func _test_pending_rewards_commit_without_front_selector(_run: Variant, failures: PackedStringArray) -> void:
	var run: Variant = _new_run(39002)
	var reward := UnitSpawnDefinition.new()
	reward.archetype_id = &"shield_guard"
	reward.owner_team_id = &"lumern"
	reward.visual_faction_id = &"lumern"
	reward.food_cost = 1
	run.pending_roulette_rewards.clear()
	run.pending_deployment_assignments = {}
	run.pending_roulette_rewards.append(reward)
	run.command_phase = run.COMMIT
	_expect(run.confirm_pending_deployment(), "single-front queue commits without a front selector", failures)
	_expect(run.command_phase == run.BATTLE, "queue commit enters battle", failures)
	_expect((run.battle.front_units(&"front") as Array).size() == 1, "queue commit spawns exactly one unit on front", failures)


func _new_run(seed: int) -> Variant:
	var progression := StageProgression.new()
	progression.regular_unlocked = true
	var run := StageRun.new(progression)
	run.start(ResourceLoader.load(REGULAR_STAGE_PATH), seed)
	return run


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Single march front contracts passed")
		quit(0)
	else:
		printerr("Single march front contract failures:\n%s" % "\n".join(failures))
		quit(1)
