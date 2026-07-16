extends SceneTree

const DataRegistry = preload("res://scripts/core/data_registry.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const BATTLE_SIMULATOR_PATH := "res://scripts/battle/battle_simulator.gd"
const GATE_STATE_PATH := "res://scripts/battle/gate_state.gd"
const OUTPOST_STATE_PATH := "res://scripts/battle/outpost_state.gd"


func _init() -> void:
	var failures := PackedStringArray()
	var simulator_script := load(BATTLE_SIMULATOR_PATH)
	var gate_script := load(GATE_STATE_PATH)
	var outpost_script := load(OUTPOST_STATE_PATH)
	_expect(simulator_script != null, "battle simulator script exists", failures)
	_expect(gate_script != null, "gate state script exists", failures)
	_expect(outpost_script != null, "outpost state script exists", failures)
	if simulator_script != null:
		_test_shared_stats_and_lane_isolation(simulator_script, failures)
		_test_fixed_seed_snapshot_repeatability(simulator_script, failures)
	if gate_script != null:
		_test_gate_multipliers_and_collapse(gate_script, failures)
	if outpost_script != null:
		_test_outpost_capture_sequence(outpost_script, failures)
	_finish(failures)


func _test_shared_stats_and_lane_isolation(simulator_script: GDScript, failures: PackedStringArray) -> void:
	var simulator: Variant = simulator_script.new(_registry(), 91)
	var lumern: Variant = simulator.spawn_unit(_spawn(&"lumern", &"top"))
	var veil: Variant = simulator.spawn_unit(_spawn(&"veil", &"top"))
	_expect(lumern.combat_stats() == veil.combat_stats(), "visual faction does not alter shared archetype combat stats", failures)
	_expect(not simulator.request_lane_move(lumern, &"middle"), "ordinary top lane units cannot move to middle", failures)
	_expect(lumern.lane_id == &"top", "rejected lane movement preserves the original lane", failures)
	_expect(simulator.lanes[&"middle"].units.is_empty(), "middle lane does not own top lane units", failures)


func _test_gate_multipliers_and_collapse(gate_script: GDScript, failures: PackedStringArray) -> void:
	var gate: Variant = gate_script.new()
	var expected_normal := 1000.0 * 0.4 * 100.0 / 180.0
	_expect(is_equal_approx(gate.apply_damage(1000.0, false), expected_normal), "normal damage uses the 0.4 structure multiplier and 80 resistance", failures)
	var expected_siege := 1000.0 * 2.0 * 100.0 / 180.0
	_expect(is_equal_approx(gate.apply_damage(1000.0, true), expected_siege), "siege damage uses the 2.0 structure multiplier and 80 resistance", failures)
	gate.apply_damage(100000.0, true)
	_expect(gate.is_collapsing(), "destroyed gate enters the two-second collapse state", failures)
	gate.advance(1.9)
	_expect(not gate.is_collapsed(), "gate does not collapse before two seconds", failures)
	gate.advance(0.1)
	_expect(gate.is_collapsed(), "gate collapses after two seconds", failures)


func _test_outpost_capture_sequence(outpost_script: GDScript, failures: PackedStringArray) -> void:
	var outpost: Variant = outpost_script.new(&"veil", true)
	outpost.begin_capture(&"lumern", 2.0)
	_expect(outpost.construction_locked and not outpost.existing_buildings_enabled, "capture start locks construction and disables existing buildings", failures)
	outpost.advance(13.0)
	_expect(outpost.state == outpost.CAPTURING, "three-second hold plus ten-second neutralization reaches capture", failures)
	outpost.advance(10.0)
	_expect(outpost.owner_team_id == &"lumern", "capture completion assigns the new owner", failures)
	_expect(outpost.prior_building_ruined, "capture completion ruins the prior building", failures)
	_expect(outpost.state == outpost.STABILIZING, "capture completion begins stabilization", failures)
	outpost.advance(5.0)
	_expect(outpost.state == outpost.STABLE and not outpost.construction_locked, "five-second stabilization unlocks new-owner construction", failures)


func _test_fixed_seed_snapshot_repeatability(simulator_script: GDScript, failures: PackedStringArray) -> void:
	var first: Variant = simulator_script.new(_registry(), 314159)
	var second: Variant = simulator_script.new(_registry(), 314159)
	for simulator in [first, second]:
		simulator.spawn_unit(_spawn(&"lumern", &"top"))
		simulator.spawn_unit(_spawn(&"veil", &"top"))
		simulator.spawn_unit(_spawn(&"lumern", &"bottom", &"archer"))
		for _step in 20:
			simulator.advance(0.1)
	_expect(JSON.stringify(first.snapshot()) == JSON.stringify(second.snapshot()), "identical seeds and inputs reproduce the same battle snapshot", failures)


func _registry() -> Variant:
	var registry: Variant = DataRegistry.new()
	var errors: PackedStringArray = registry.load_bootstrap_catalog(BOOTSTRAP_CATALOG_PATH)
	if not errors.is_empty():
		push_error("battle test registry failed to load: %s" % errors)
	return registry


func _spawn(visual_faction_id: StringName, lane_id: StringName, archetype_id: StringName = &"shield_guard") -> UnitSpawnDefinition:
	var spawn := UnitSpawnDefinition.new()
	spawn.archetype_id = archetype_id
	spawn.owner_team_id = visual_faction_id
	spawn.visual_faction_id = visual_faction_id
	spawn.lane_id = lane_id
	return spawn


func _expect(condition: bool, message: String, failures: PackedStringArray) -> void:
	if not condition:
		failures.append(message)


func _finish(failures: PackedStringArray) -> void:
	if failures.is_empty():
		print("Battle simulation checks passed")
		quit(0)
	else:
		printerr("Battle simulation failures:\n%s" % "\n".join(failures))
		quit(1)
