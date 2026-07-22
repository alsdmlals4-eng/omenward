extends SceneTree

const DataRegistry = preload("res://scripts/core/data_registry.gd")
const StageManifest = preload("res://scripts/core/stage_manifest.gd")
const StageEconomy = preload("res://scripts/core/stage_economy.gd")
const BuildingService = preload("res://scripts/buildings/building_service.gd")
const BattleSimulator = preload("res://scripts/battle/battle_simulator.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")
const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const TUTORIAL_STAGE_PATH := "res://data/stages/tutorial_stage.tres"
const REGULAR_STAGE_PATH := "res://data/stages/regular_stage.tres"


func _init() -> void:
	var failures := PackedStringArray()
	_test_shared_objective_profiles(failures)
	_test_objective_sequence_and_lane_gate_isolation(failures)
	_test_contested_clash_and_economy(failures)
	_test_outpost_building_effect_lifecycle(failures)
	_test_natural_base_result(failures)
	_test_stage_natural_results(failures)
	_finish(failures)


func _test_shared_objective_profiles(failures: PackedStringArray) -> void:
	var registry: Variant = _registry()
	var expected := {
		&"shield_guard": 1.25,
		&"greatsword_warrior": 1.0,
		&"assassin": 0.0,
		&"spear_guard": 1.0,
		&"archer": 0.5,
		&"cavalry": 1.0,
		&"priest": 0.5,
		&"mage": 0.5,
		&"flier": 0.0,
		&"giant": 0.5,
	}
	for archetype_id in expected:
		var profile: Variant = registry.archetypes[str(archetype_id)]
		_expect(is_equal_approx(float(profile.capture_power), float(expected[archetype_id])), "%s uses the approved shared capture power" % archetype_id, failures)
		var is_siege: bool = profile.structure_damage_tags.has("siege")
		_expect(is_siege == (archetype_id == &"giant"), "%s uses the shared structure damage tag" % archetype_id, failures)


func _test_objective_sequence_and_lane_gate_isolation(failures: PackedStringArray) -> void:
	var battle := BattleSimulator.new(_registry(), 101)
	var giants: Array = []
	for _index in 4:
		var giant: Variant = battle.spawn_unit(_spawn(&"lumern", &"top", &"giant"))
		giant.lane_position = battle.CLASH_POSITION
		giants.append(giant)
	battle.advance(10.0)
	_expect(battle.clash_zones[&"top"].outpost.is_stable_for(&"lumern"), "an uncontested giant squad captures the top clash", failures)
	for giant in giants:
		giant.lane_position = float(battle.OUTPOST_POSITIONS[&"veil"])
	battle.advance(15.0)
	_expect(battle.outposts[&"veil"][&"top"].is_stable_for(&"lumern"), "the same lane force captures the enemy top outpost", failures)
	for giant in giants:
		giant.lane_position = float(battle.GATE_POSITIONS[&"veil"])
	var giant: Variant = giants[0]
	battle.gates[&"veil"][&"top"].apply_damage(100000.0, true)
	battle.advance(2.0)
	_expect(battle.gates[&"veil"][&"top"].is_collapsed(), "the top enemy gate collapses independently", failures)
	_expect(not battle.gates[&"veil"][&"middle"].is_collapsed() and not battle.gates[&"veil"][&"bottom"].is_collapsed(), "other lane gates remain standing", failures)
	for attacker in giants:
		attacker.lane_position = float(battle.BASE_POSITIONS[&"veil"])
	battle.bases[&"veil"].apply_damage(100000.0, true)
	battle.advance(0.1)
	_expect(battle.result_state == battle.LUMERN_VICTORY, "enemy base destruction produces a natural battle victory", failures)


func _test_contested_clash_and_economy(failures: PackedStringArray) -> void:
	var battle := BattleSimulator.new(_registry(), 202)
	var lumern: Variant = battle.spawn_unit(_spawn(&"lumern", &"middle", &"shield_guard"))
	var veil: Variant = battle.spawn_unit(_spawn(&"veil", &"middle", &"shield_guard"))
	lumern.lane_position = battle.CLASH_POSITION
	veil.lane_position = battle.CLASH_POSITION
	battle.advance(5.0)
	_expect(battle.clash_zones[&"middle"].outpost.contested, "both teams on one clash freeze it as contested", failures)
	_expect(is_equal_approx(float(battle.clash_zones[&"middle"].outpost.capture_progress), 0.0), "contested clash does not progress", failures)
	veil.health = 0.0
	battle.advance(8.0)
	_expect(battle.clash_zones[&"middle"].outpost.state != battle.clash_zones[&"middle"].outpost.STABLE, "capture begins after one team remains", failures)
	battle.clash_zones[&"middle"].outpost.owner_team_id = &"lumern"
	battle.clash_zones[&"middle"].outpost.state = battle.clash_zones[&"middle"].outpost.STABLE
	var manifest := StageManifest.new()
	manifest.starting_gold = 0
	manifest.starting_food_cap = 12
	var economy := StageEconomy.new(manifest)
	economy.advance(60.0, battle.controlled_clash_count(&"lumern"), battle.stable_owned_outpost_count(&"lumern"))
	_expect(economy.gold == 31, "sixty seconds pays 15 base, 4 clash, and 12 for three stable home outposts", failures)


func _test_outpost_building_effect_lifecycle(failures: PackedStringArray) -> void:
	var battle := BattleSimulator.new(_registry(), 303)
	var manifest := StageManifest.new()
	manifest.starting_gold = 200
	manifest.starting_food_cap = 12
	var economy := StageEconomy.new(manifest)
	var buildings := BuildingService.new(economy, manifest)
	var outpost: Variant = battle.outposts[&"lumern"][&"middle"]
	buildings.register_outpost(&"lumern_middle", outpost, [&"front_a", &"front_b", &"rear"])
	_expect(buildings.try_construct(&"lumern_middle", &"front_b", &"farm"), "a stable home outpost builds a farm", failures)
	_expect(economy.food_cap == 18, "active farm grants six food cap", failures)
	outpost.begin_capture(&"veil", 2.0)
	outpost.advance(5.0)
	buildings.sync_outpost_states()
	_expect(economy.food_cap == 12, "farm food cap is removed when the outpost becomes neutral", failures)
	outpost.advance(5.0)
	outpost.advance(5.0)
	buildings.sync_outpost_states()
	var ruined: Variant = buildings.building_state(&"lumern_middle", &"front_b")
	_expect(ruined != null and ruined.state == ruined.RUINED, "captured outpost ruins the previous building revision", failures)
	outpost.begin_capture(&"lumern", 2.0)
	outpost.advance(10.0)
	outpost.advance(5.0)
	_expect(buildings.try_construct(&"lumern_middle", &"front_b", &"farm"), "recapture allows a new building on the ruined node", failures)
	_expect(economy.food_cap == 18, "rebuilt farm restores food cap once", failures)


func _test_natural_base_result(failures: PackedStringArray) -> void:
	var battle := BattleSimulator.new(_registry(), 404)
	battle.clash_zones[&"bottom"].outpost.owner_team_id = &"veil"
	battle.clash_zones[&"bottom"].outpost.state = battle.clash_zones[&"bottom"].outpost.STABLE
	battle.outposts[&"lumern"][&"bottom"].owner_team_id = &"veil"
	battle.outposts[&"lumern"][&"bottom"].state = battle.outposts[&"lumern"][&"bottom"].STABLE
	battle.gates[&"lumern"][&"bottom"].apply_damage(100000.0, true)
	battle.gates[&"lumern"][&"bottom"].advance(2.0)
	battle.bases[&"lumern"].apply_damage(100000.0, true)
	battle.advance(0.1)
	_expect(battle.result_state == battle.VEIL_VICTORY, "player base destruction produces a natural battle defeat", failures)


func _test_stage_natural_results(failures: PackedStringArray) -> void:
	var tutorial: Resource = ResourceLoader.load(TUTORIAL_STAGE_PATH)
	var victory_progression := StageProgression.new()
	var victory_run := StageRun.new(victory_progression)
	victory_run.start(tutorial, 505)
	victory_run.battle.bases[&"veil"].apply_damage(100000.0, true)
	victory_run.advance(0.1)
	_expect(victory_run.result_state == victory_run.VICTORY and victory_progression.regular_unlocked, "enemy base destruction closes StageRun as victory", failures)
	var defeat_run := StageRun.new(StageProgression.new())
	defeat_run.start(tutorial, 506)
	defeat_run.battle.bases[&"lumern"].apply_damage(100000.0, true)
	defeat_run.advance(0.1)
	_expect(defeat_run.result_state == defeat_run.DEFEAT, "player base destruction closes StageRun as defeat", failures)
	var progression := StageProgression.new()
	progression.regular_unlocked = true
	var regular: Resource = ResourceLoader.load(REGULAR_STAGE_PATH)
	var boss_run := StageRun.new(progression)
	boss_run.start(regular, 507)
	boss_run.battle.objectives_enabled = false
	while boss_run.current_wave < 15:
		boss_run.advance(60.0)
	_expect(boss_run.legendary_boss_unit_id > 0, "W15 records the legendary boss runtime identity", failures)
	var boss: Variant = boss_run.battle.get_unit_by_id(boss_run.legendary_boss_unit_id)
	if boss != null:
		boss.health = 0.0
	boss_run.advance(0.1)
	_expect(boss_run.result_state == boss_run.VICTORY, "W15 legendary boss defeat produces standard victory", failures)


func _registry() -> Variant:
	var registry := DataRegistry.new()
	var errors: PackedStringArray = registry.load_bootstrap_catalog(BOOTSTRAP_CATALOG_PATH)
	if not errors.is_empty():
		push_error("C2 registry failed to load: %s" % errors)
	return registry


func _spawn(team_id: StringName, lane_id: StringName, archetype_id: StringName) -> UnitSpawnDefinition:
	var spawn := UnitSpawnDefinition.new()
	spawn.archetype_id = archetype_id
	spawn.owner_team_id = team_id
	spawn.visual_faction_id = team_id
	spawn.lane_id = lane_id
	return spawn


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("C2 battle objective checks passed")
		quit(0)
	else:
		printerr("C2 battle objective failures:\n%s" % "\n".join(failures))
		quit(1)
