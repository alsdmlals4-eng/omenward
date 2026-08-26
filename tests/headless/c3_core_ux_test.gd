extends SceneTree

const StageRun = preload("res://scripts/core/stage_run.gd")
const StageProgression = preload("res://scripts/core/stage_progression.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")
const CoreUxService = preload("res://scripts/core/core_ux_service.gd")
const RouletteService = preload("res://scripts/roulette/roulette_service.gd")
const WaveDirector = preload("res://scripts/waves/wave_director.gd")

const TUTORIAL_STAGE_PATH := "res://data/stages/tutorial_stage.tres"
const HUD_SCENE_PATH := "res://scenes/ui/stage_hud.tscn"


func _init() -> void:
	var failures := PackedStringArray()
	if not _test_script_instantiation(failures):
		_finish(failures)
		return
	_test_token_ledger_and_construction_preview(failures)
	_test_snapshot_is_read_only(failures)
	_test_boundary_snapshots(failures)
	_test_staged_omen_reveal(failures)
	_test_tactical_range_target_and_counter_overlay(failures)
	_test_wave_cause_report(failures)
	_test_snapshot_determinism(failures)
	_test_hud_contains_all_six_surfaces(failures)
	_finish(failures)


func _test_script_instantiation(failures: PackedStringArray) -> bool:
	var scripts := {
		"StageRun": StageRun,
		"CoreUxService": CoreUxService,
		"RouletteService": RouletteService,
		"WaveDirector": WaveDirector,
	}
	var valid := true
	for script_name in scripts:
		var script: Script = scripts[script_name]
		if not script.can_instantiate():
			failures.append("C3 dependency script cannot instantiate: %s" % script_name)
			valid = false
	return valid


func _new_run(seed: int) -> Variant:
	var stage: Resource = ResourceLoader.load(TUTORIAL_STAGE_PATH)
	var run := StageRun.new(StageProgression.new())
	run.start(stage, seed)
	return run


func _test_token_ledger_and_construction_preview(failures: PackedStringArray) -> void:
	var run: Variant = _new_run(701)
	var snapshot: Dictionary = run.core_ux_snapshot()
	var ledger: Array = snapshot.get("token_ledger", [])
	_expect(_ledger_entry(ledger, "x").get("weight", 0) == 6, "token ledger exposes the authoritative X weight", failures)
	_expect(_ledger_entry(ledger, "gold").get("weight", 0) == 2, "token ledger exposes the authoritative gold weight", failures)
	_expect(_ledger_entry(ledger, "warrior").is_empty(), "initial token ledger does not invent an inactive building source", failures)
	var barracks: Dictionary = _building_entry(snapshot.get("construction_comparison", []), "barracks")
	_expect(bool(barracks.get("can_construct", false)), "barracks comparison is available on the stable home node", failures)
	_expect(float(barracks.get("probability_after", 0.0)) > float(barracks.get("probability_before", 0.0)), "barracks preview increases the warrior probability before construction", failures)
	_expect(run.construct_home(&"barracks"), "barracks construction succeeds from the comparison state", failures)
	var after: Dictionary = run.core_ux_snapshot()
	var warrior: Dictionary = _ledger_entry(after.get("token_ledger", []), "warrior")
	_expect(int(warrior.get("source_count", 0)) == 1 and int(warrior.get("weight", 0)) == 3, "constructed barracks appears once in the token ledger", failures)
	_expect((warrior.get("source_building_ids", []) as Array).has("lumern_middle:rear"), "token ledger exposes the authoritative source building ID", failures)
	var occupied: Dictionary = _building_entry(after.get("construction_comparison", []), "barracks")
	_expect(not bool(occupied.get("can_construct", true)) and str(occupied.get("block_reason", "")) == "occupied", "building comparison exposes the occupied node reason", failures)


func _test_snapshot_is_read_only(failures: PackedStringArray) -> void:
	var run: Variant = _new_run(710)
	_expect(run.construct_home(&"farm"), "read-only snapshot setup constructs a farm", failures)
	var farm: Variant = run.buildings.building_state_snapshot(&"lumern_middle", &"front_b")
	var home: Variant = run.battle.outposts[&"lumern"][&"middle"]
	home.capture_revision += 1
	var gold_before := int(run.economy.gold)
	var food_cap_before := int(run.economy.food_cap)
	var state_before := StringName(farm.state)
	var effect_before := bool(farm.effect_active)
	var log_before := JSON.stringify(run.manifest.input_log)
	var first_snapshot := JSON.stringify(run.core_ux_snapshot())
	var second_snapshot := JSON.stringify(run.core_ux_snapshot())
	_expect(first_snapshot == second_snapshot, "repeated C3 reads return the same snapshot without a gameplay tick", failures)
	_expect(int(run.economy.gold) == gold_before, "C3 snapshot does not spend or grant gold", failures)
	_expect(int(run.economy.food_cap) == food_cap_before, "C3 snapshot does not change food capacity", failures)
	_expect(StringName(farm.state) == state_before and bool(farm.effect_active) == effect_before, "C3 snapshot does not synchronize or ruin a stale building", failures)
	_expect(JSON.stringify(run.manifest.input_log) == log_before, "C3 snapshot does not append gameplay input-log events", failures)


func _test_boundary_snapshots(failures: PackedStringArray) -> void:
	var poor: Variant = _new_run(706)
	poor.economy.gold = 0
	var poor_barracks: Dictionary = _building_entry(poor.core_ux_snapshot().get("construction_comparison", []), "barracks")
	_expect(not bool(poor_barracks.get("can_construct", true)) and str(poor_barracks.get("block_reason", "")) == "insufficient_gold", "construction comparison exposes insufficient gold without mutating state", failures)

	var contested: Variant = _new_run(707)
	var home: Variant = contested.battle.outposts[&"lumern"][&"middle"]
	_expect(home.begin_capture(&"veil", 1.0), "boundary setup begins an enemy capture", failures)
	home.set_contested()
	var contested_barracks: Dictionary = _building_entry(contested.core_ux_snapshot().get("construction_comparison", []), "barracks")
	_expect(not bool(contested_barracks.get("can_construct", true)) and str(contested_barracks.get("block_reason", "")).begins_with("outpost_"), "construction comparison safely blocks a contested capture state", failures)

	var no_target: Variant = _new_run(708)
	var lone_archer: Variant = no_target.battle.spawn_unit(_spawn(&"lumern", &"top", &"archer"))
	_expect(no_target.begin_battle(), "tactical overlay setup enters battle", failures)
	no_target.advance(0.1)
	var lone_entry: Dictionary = _unit_entry(no_target.core_ux_snapshot().get("tactical_overlay", []), int(lone_archer.unit_id))
	_expect(int(lone_entry.get("target_unit_id", 0)) == -1, "tactical overlay safely exposes a unit with no current target", failures)

	var unresolved: Variant = _new_run(709)
	_expect(unresolved.begin_battle(), "unresolved report setup enters battle", failures)
	unresolved.advance(60.0)
	_expect((unresolved.core_ux_snapshot().get("latest_wave_report", {}) as Dictionary).is_empty(), "wave report remains empty while a registered wave is unresolved", failures)


func _test_staged_omen_reveal(failures: PackedStringArray) -> void:
	var run: Variant = _new_run(702)
	var initial: Dictionary = run.core_ux_snapshot().get("omen", {})
	_expect(str(initial.get("phase", "")) == "countdown" and (initial.get("lanes", []) as Array).is_empty(), "omen hides composition outside T-30", failures)
	_expect(run.begin_battle(), "omen reveal setup enters battle", failures)
	run.advance(30.0)
	var t30: Dictionary = run.core_ux_snapshot().get("omen", {})
	_expect(str(t30.get("phase", "")) == "t30", "omen enters the T-30 phase", failures)
	var top_t30: Dictionary = _lane_entry(t30.get("lanes", []), "top")
	_expect(int(top_t30.get("count", 0)) == 1 and (top_t30.get("units", []) as Array).is_empty(), "T-30 reveals lane and role without exact unit details", failures)
	run.advance(15.0)
	var t15: Dictionary = run.core_ux_snapshot().get("omen", {})
	var top_t15: Dictionary = _lane_entry(t15.get("lanes", []), "top")
	_expect(str(t15.get("phase", "")) == "t15" and not (top_t15.get("units", []) as Array).is_empty(), "T-15 reveals exact shared archetype and counter hints", failures)
	run.advance(10.0)
	var t5: Dictionary = run.core_ux_snapshot().get("omen", {})
	_expect(str(t5.get("phase", "")) == "t5" and str(t5.get("danger_lane", "")) == "top", "T-5 highlights the highest-count danger lane", failures)


func _test_tactical_range_target_and_counter_overlay(failures: PackedStringArray) -> void:
	var run: Variant = _new_run(703)
	var archer: Variant = run.battle.spawn_unit(_spawn(&"lumern", &"top", &"archer"))
	var flier: Variant = run.battle.spawn_unit(_spawn(&"veil", &"top", &"flier"))
	archer.lane_position = 48.0
	flier.lane_position = 52.0
	_expect(run.begin_battle(), "target overlay setup enters battle", failures)
	run.advance(0.1)
	var overlay: Array = run.core_ux_snapshot().get("tactical_overlay", [])
	var archer_entry: Dictionary = _unit_entry(overlay, int(archer.unit_id))
	_expect(is_equal_approx(float(archer_entry.get("attack_range", 0.0)), 4.0), "tactical overlay uses the unit's actual attack range", failures)
	_expect((archer_entry.get("counter_tags", []) as Array).has("anti_air"), "tactical overlay exposes the approved anti-air hint", failures)
	_expect((archer_entry.get("target_priority_tags", []) as Array).has("flying"), "tactical overlay exposes the approved target-priority hint", failures)
	_expect(int(archer_entry.get("target_unit_id", -1)) == int(flier.unit_id), "tactical overlay exposes the current target identity", failures)


func _test_wave_cause_report(failures: PackedStringArray) -> void:
	var run: Variant = _new_run(704)
	run.battle.objectives_enabled = false
	_expect(run.begin_battle(), "wave report setup enters battle", failures)
	run.advance(60.0)
	var enemy: Variant = null
	for unit in run.battle.snapshot().get("units", []):
		if str(unit.get("owner_team_id", "")) == "veil":
			enemy = run.battle.get_unit_by_id(int(unit.get("unit_id", -1)))
			break
	_expect(enemy != null, "tutorial wave registers an enemy runtime unit", failures)
	if enemy != null:
		enemy.health = 0.0
	run.advance(0.1)
	var report: Dictionary = run.core_ux_snapshot().get("latest_wave_report", {})
	var top: Dictionary = _lane_entry(report.get("lanes", []), "top")
	_expect(int(report.get("wave_number", 0)) == 1, "resolved tutorial wave creates one wave report", failures)
	_expect(int(top.get("enemy_defeated", 0)) == 1, "wave report counts the actual defeated enemy in its lane", failures)
	_expect(str(top.get("cause_code", "")) == "clean_defense", "wave report derives a cause code from recorded metrics", failures)


func _test_snapshot_determinism(failures: PackedStringArray) -> void:
	var a: Variant = _new_run(705)
	var b: Variant = _new_run(705)
	_expect(JSON.stringify(a.core_ux_snapshot()) == JSON.stringify(b.core_ux_snapshot()), "identical stage state produces an identical core UX snapshot", failures)


func _test_hud_contains_all_six_surfaces(failures: PackedStringArray) -> void:
	var packed: PackedScene = ResourceLoader.load(HUD_SCENE_PATH)
	var hud: Node = packed.instantiate()
	var required_paths := [
		"OmenDetailLabel",
		"TokenLedgerLabel",
		"ConstructionComparisonLabel",
		"TacticalOverlayLabel",
		"WaveReportLabel",
	]
	for path in required_paths:
		_expect(hud.get_node_or_null(path) != null, "HUD contains C3 surface %s" % path, failures)
	hud.free()


func _spawn(team_id: StringName, lane_id: StringName, archetype_id: StringName) -> UnitSpawnDefinition:
	var spawn := UnitSpawnDefinition.new()
	spawn.archetype_id = archetype_id
	spawn.owner_team_id = team_id
	spawn.visual_faction_id = team_id
	spawn.lane_id = lane_id
	return spawn


func _ledger_entry(entries: Array, symbol_id: String) -> Dictionary:
	for entry in entries:
		if str(entry.get("symbol_id", "")) == symbol_id:
			return entry
	return {}


func _building_entry(entries: Array, building_id: String) -> Dictionary:
	for entry in entries:
		if str(entry.get("building_id", "")) == building_id:
			return entry
	return {}


func _lane_entry(entries: Array, lane_id: String) -> Dictionary:
	for entry in entries:
		if str(entry.get("lane_id", "")) == lane_id:
			return entry
	return {}


func _unit_entry(entries: Array, unit_id: int) -> Dictionary:
	for entry in entries:
		if int(entry.get("unit_id", -1)) == unit_id:
			return entry
	return {}


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("C3 core UX checks passed")
		quit(0)
	else:
		printerr("C3 core UX failures:\n%s" % "\n".join(failures))
		quit(1)
