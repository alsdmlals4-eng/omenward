extends SceneTree

const DataRegistry = preload("res://scripts/core/data_registry.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"
const BATTLE_SIMULATOR_PATH := "res://scripts/battle/battle_simulator.gd"
const GATE_STATE_PATH := "res://scripts/battle/gate_state.gd"
const OUTPOST_STATE_PATH := "res://scripts/battle/outpost_state.gd"


func _init() -> void:
	var failures := PackedStringArray()
	var simulator_script: GDScript = load(BATTLE_SIMULATOR_PATH) as GDScript
	var gate_script: GDScript = load(GATE_STATE_PATH) as GDScript
	var outpost_script: GDScript = load(OUTPOST_STATE_PATH) as GDScript
	var simulator_ready := simulator_script != null and simulator_script.can_instantiate()
	var gate_ready := gate_script != null and gate_script.can_instantiate()
	var outpost_ready := outpost_script != null and outpost_script.can_instantiate()
	_expect(simulator_ready, "battle simulator script loads and can instantiate", failures)
	_expect(gate_ready, "gate state script loads and can instantiate", failures)
	_expect(outpost_ready, "outpost state script loads and can instantiate", failures)
	if simulator_ready:
		_test_shared_stats_and_lane_isolation(simulator_script, failures)
		_test_fixed_seed_snapshot_repeatability(simulator_script, failures)
	if gate_ready:
		_test_gate_multipliers_and_collapse(gate_script, failures)
	if outpost_ready:
		_test_outpost_capture_sequence(outpost_script, failures)
		_test_outpost_capture_power_scaling(outpost_script, failures)
		_test_fractional_capture_power_is_preserved(outpost_script, failures)
		_test_outpost_contested_freeze(outpost_script, failures)
		_test_outpost_exit_hold_and_reversion(outpost_script, failures)
	_finish(failures)


func _test_shared_stats_and_lane_isolation(simulator_script: GDScript, failures: PackedStringArray) -> void:
	var simulator: Variant = simulator_script.new(_registry(), 91)
	simulator.objectives_enabled = false
	var registry: Variant = _registry()
	for archetype in registry.catalog.archetypes:
		var public_stats: Variant = archetype.get("base_stats")
		_expect(public_stats is Dictionary and not public_stats.is_empty(), "%s exposes public base combat stats" % archetype.archetype_id, failures)
		var lumern: Variant = simulator.spawn_unit(_spawn(&"lumern", &"top", archetype.archetype_id))
		var veil: Variant = simulator.spawn_unit(_spawn(&"veil", &"top", archetype.archetype_id))
		_expect(lumern.combat_stats() == veil.combat_stats(), "%s visual faction does not alter combat stats" % archetype.archetype_id, failures)
		if public_stats is Dictionary:
			_expect(lumern.combat_stats() == public_stats, "%s unit stats derive from public profile data" % archetype.archetype_id, failures)
	var lumern: Variant = simulator.lanes[&"top"].units[0]
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
	_expect(outpost.construction_locked and outpost.existing_buildings_enabled, "capture start locks construction while existing buildings remain active", failures)
	outpost.advance(5.0)
	_expect(outpost.state == outpost.CAPTURING and outpost.owner_team_id == &"", "power two neutralizes an outpost in five seconds", failures)
	_expect(not outpost.existing_buildings_enabled, "neutralization disables the previous buildings", failures)
	outpost.advance(5.0)
	_expect(outpost.owner_team_id == &"lumern", "capture completion assigns the new owner", failures)
	_expect(outpost.prior_building_ruined, "capture completion ruins the prior building", failures)
	_expect(outpost.state == outpost.STABILIZING, "capture completion begins stabilization", failures)
	outpost.advance(5.0)
	_expect(outpost.state == outpost.STABLE and not outpost.construction_locked, "five-second stabilization unlocks new-owner construction", failures)


func _test_outpost_capture_power_scaling(outpost_script: GDScript, failures: PackedStringArray) -> void:
	var one_power: Variant = outpost_script.new(&"veil")
	one_power.begin_capture(&"lumern", 1.0)
	one_power.advance(9.9)
	_expect(one_power.state == one_power.NEUTRALIZING, "capture power one has not neutralized before ten seconds", failures)
	one_power.advance(0.1)
	_expect(one_power.state == one_power.CAPTURING, "capture power one neutralizes in ten seconds", failures)
	var two_power: Variant = outpost_script.new(&"veil")
	two_power.begin_capture(&"lumern", 2.0)
	two_power.advance(4.9)
	_expect(two_power.state == two_power.NEUTRALIZING, "capture power two has not neutralized before five seconds", failures)
	two_power.advance(0.1)
	_expect(two_power.state == two_power.CAPTURING, "capture power two neutralizes in five seconds", failures)


func _test_fractional_capture_power_is_preserved(outpost_script: GDScript, failures: PackedStringArray) -> void:
	var half_power: Variant = outpost_script.new(&"veil")
	_expect(half_power.begin_capture(&"lumern", 0.5), "approved ranged capture power 0.5 starts capture", failures)
	half_power.advance(10.0)
	_expect(is_equal_approx(float(half_power.capture_progress), 0.5), "capture power 0.5 advances half a neutralization phase in ten seconds", failures)
	var guard_power: Variant = outpost_script.new(&"veil")
	_expect(guard_power.begin_capture(&"lumern", 1.25), "approved shield capture power 1.25 starts capture", failures)
	guard_power.advance(8.0)
	_expect(guard_power.state == guard_power.CAPTURING, "capture power 1.25 neutralizes in eight seconds", failures)
	var clamped: Variant = outpost_script.new(&"veil")
	clamped.begin_capture(&"lumern", 9.0)
	_expect(is_equal_approx(float(clamped.capture_power), 2.0), "capture power is capped at the approved maximum two", failures)


func _test_outpost_contested_freeze(outpost_script: GDScript, failures: PackedStringArray) -> void:
	var outpost: Variant = outpost_script.new(&"veil")
	outpost.begin_capture(&"lumern", 1.0)
	outpost.advance(4.0)
	var before: float = outpost.capture_progress
	outpost.set_contested()
	outpost.advance(10.0)
	_expect(is_equal_approx(float(outpost.capture_progress), before), "contested capture freezes without hold or reversion", failures)
	outpost.set_capture_power(1.0)
	outpost.advance(1.0)
	_expect(outpost.capture_progress > before, "capture resumes when only the capturing team remains", failures)


func _test_outpost_exit_hold_and_reversion(outpost_script: GDScript, failures: PackedStringArray) -> void:
	var outpost: Variant = outpost_script.new(&"veil", true)
	outpost.begin_capture(&"lumern", 2.0)
	outpost.advance(5.0)
	outpost.clear_capture_presence()
	_expect(outpost.state == outpost.CAPTURING, "capturer exit does not immediately discard capture progress", failures)
	_expect(is_equal_approx(float(outpost.capture_progress), 1.0), "capturer exit preserves capture progress during the hold", failures)
	outpost.advance(3.0)
	_expect(is_equal_approx(float(outpost.capture_progress), 1.0), "capture progress remains frozen for the three-second exit hold", failures)
	outpost.advance(1.0)
	_expect(is_equal_approx(float(outpost.capture_progress), 0.9), "capture progress reverts at ten percent per second after the hold", failures)
	outpost.advance(9.0)
	_expect(outpost.state == outpost.STABLE and outpost.owner_team_id == &"veil", "fully reverted capture restores the previous stable owner", failures)
	_expect(not outpost.construction_locked and outpost.existing_buildings_enabled, "fully reverted capture restores the previous stable building state", failures)


func _test_fixed_seed_snapshot_repeatability(simulator_script: GDScript, failures: PackedStringArray) -> void:
	var first: Variant = simulator_script.new(_registry(), 314159)
	var second: Variant = simulator_script.new(_registry(), 314159)
	for simulator in [first, second]:
		simulator.objectives_enabled = false
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
