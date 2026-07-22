from __future__ import annotations

import pathlib
import shutil

ROOT = pathlib.Path(__file__).resolve().parents[1]


def write(relative: str, content: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.lstrip("\n"), encoding="utf-8", newline="\n")


write("tests/headless/battle_simulation_test.gd", r'''
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
''')

write("tests/headless/c2_battle_objective_test.gd", r'''
extends SceneTree

const DataRegistry = preload("res://scripts/core/data_registry.gd")
const StageManifest = preload("res://scripts/core/stage_manifest.gd")
const StageEconomy = preload("res://scripts/core/stage_economy.gd")
const BuildingService = preload("res://scripts/buildings/building_service.gd")
const BattleSimulator = preload("res://scripts/battle/battle_simulator.gd")
const UnitSpawnDefinition = preload("res://scripts/data/unit_spawn_definition.gd")

const BOOTSTRAP_CATALOG_PATH := "res://data/bootstrap_catalog.tres"


func _init() -> void:
	var failures := PackedStringArray()
	_test_shared_objective_profiles(failures)
	_test_objective_sequence_and_lane_gate_isolation(failures)
	_test_contested_clash_and_economy(failures)
	_test_outpost_building_effect_lifecycle(failures)
	_test_natural_base_result(failures)
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
	var giant: Variant = battle.spawn_unit(_spawn(&"lumern", &"top", &"giant"))
	giant.lane_position = battle.CLASH_POSITION
	battle.advance(20.0)
	_expect(battle.clash_zones[&"top"].outpost.is_stable_for(&"lumern"), "an uncontested giant captures the top clash", failures)
	giant.lane_position = float(battle.OUTPOST_POSITIONS[&"veil"])
	battle.advance(10.0)
	_expect(battle.outposts[&"veil"][&"top"].is_stable_for(&"lumern"), "the same lane force captures the enemy top outpost", failures)
	giant.lane_position = float(battle.GATE_POSITIONS[&"veil"])
	battle.gates[&"veil"][&"top"].apply_damage(100000.0, true)
	battle.advance(2.0)
	_expect(battle.gates[&"veil"][&"top"].is_collapsed(), "the top enemy gate collapses independently", failures)
	_expect(not battle.gates[&"veil"][&"middle"].is_collapsed() and not battle.gates[&"veil"][&"bottom"].is_collapsed(), "other lane gates remain standing", failures)
	giant.lane_position = float(battle.BASE_POSITIONS[&"veil"])
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
''')

# Keep stage progression coverage isolated from the new natural battle result while retaining its C1/C2 storage checks.
stage_test = ROOT / "tests/headless/stage_run_test.gd"
stage_text = stage_test.read_text(encoding="utf-8")
stage_text = stage_text.replace(
    "run.start(tutorial, 1001)\n\t_expect(run.result_state == &\"running\"",
    "run.start(tutorial, 1001)\n\trun.battle.objectives_enabled = false\n\t_expect(run.result_state == &\"running\"",
    1,
)
stage_text = stage_text.replace(
    "run.start(regular, 1001)\n\t_advance_waves(run, 15)",
    "run.start(regular, 1001)\n\trun.battle.objectives_enabled = false\n\t_advance_waves(run, 15)",
    1,
)
stage_test.write_text(stage_text, encoding="utf-8", newline="\n")

write("tools/validate_c2_battle_objective.py", r'''
#!/usr/bin/env python3
from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "scripts/battle/base_state.gd",
    "scripts/battle/battle_simulator.gd",
    "scripts/battle/outpost_state.gd",
    "scripts/core/stage_run.gd",
    "scripts/buildings/building_service.gd",
    "tests/headless/c2_battle_objective_test.gd",
    "docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md",
)


def validate(root: pathlib.Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing C2 file: {relative}")
    if errors:
        return errors
    simulator = (root / "scripts/battle/battle_simulator.gd").read_text(encoding="utf-8")
    stage_run = (root / "scripts/core/stage_run.gd").read_text(encoding="utf-8")
    outpost = (root / "scripts/battle/outpost_state.gd").read_text(encoding="utf-8")
    building = (root / "scripts/buildings/building_service.gd").read_text(encoding="utf-8")
    unit_profile = (root / "scripts/data/unit_archetype_profile.gd").read_text(encoding="utf-8")
    contract_test = (root / "tests/headless/c2_battle_objective_test.gd").read_text(encoding="utf-8")
    for term in (
        "controlled_clash_count",
        "stable_owned_outpost_count",
        "_advance_capture_objectives",
        "_next_objective",
        "LUMERN_VICTORY",
        "VEIL_VICTORY",
        "BaseStateScript",
    ):
        if term not in simulator:
            errors.append(f"battle simulator missing C2 contract term: {term}")
    for term in ("legendary_boss_unit_id", "_resolve_natural_result", "enemy_base_destroyed", "wave_15_legendary_boss_defeated"):
        if term not in stage_run:
            errors.append(f"stage run missing natural result contract: {term}")
    for term in ("set_contested", "clear_capture_presence", "clampf(power, 0.0, MAX_CAPTURE_POWER)"):
        if term not in outpost:
            errors.append(f"outpost state missing approved capture contract: {term}")
    for term in ("sync_outpost_states", "remove_food_cap", "RUINED"):
        if term not in building and term not in (root / "scripts/core/stage_economy.gd").read_text(encoding="utf-8"):
            errors.append(f"building lifecycle missing contract term: {term}")
    for term in ("capture_power", "structure_damage_tags"):
        if term not in unit_profile:
            errors.append(f"shared archetype schema missing objective field: {term}")
    for phrase in (
        "an uncontested giant captures the top clash",
        "other lane gates remain standing",
        "both teams on one clash freeze it as contested",
        "farm food cap is removed when the outpost becomes neutral",
        "enemy base destruction produces a natural battle victory",
        "player base destruction produces a natural battle defeat",
    ):
        if phrase not in contract_test:
            errors.append(f"C2 regression test missing: {phrase}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("C2 battle objective validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("C2 battle objective validation PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
''')

write("tests/python/test_c2_battle_objective_contract.py", r'''
from __future__ import annotations

import pathlib
import shutil
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from validate_c2_battle_objective import REQUIRED_FILES, validate  # noqa: E402


class C2BattleObjectiveContractTests(unittest.TestCase):
    def _copy_contract_files(self, destination: pathlib.Path) -> None:
        for relative in REQUIRED_FILES:
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        for relative in (
            "scripts/data/unit_archetype_profile.gd",
            "scripts/core/stage_economy.gd",
            "scripts/buildings/building_state.gd",
        ):
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    def test_current_tree_passes(self) -> None:
        self.assertEqual([], validate(ROOT))

    def test_external_only_result_regression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            stage = root / "scripts/core/stage_run.gd"
            stage.write_text(stage.read_text(encoding="utf-8").replace("_resolve_natural_result()", "# natural result removed"), encoding="utf-8")
            self.assertTrue(any("natural result" in error for error in validate(root)))

    def test_fractional_capture_regression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            outpost = root / "scripts/battle/outpost_state.gd"
            outpost.write_text(outpost.read_text(encoding="utf-8").replace("clampf(power, 0.0, MAX_CAPTURE_POWER)", "0.0"), encoding="utf-8")
            self.assertTrue(any("capture contract" in error for error in validate(root)))

    def test_line_gate_isolation_regression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            test_file = root / "tests/headless/c2_battle_objective_test.gd"
            test_file.write_text(test_file.read_text(encoding="utf-8").replace("other lane gates remain standing", "gate isolation omitted"), encoding="utf-8")
            self.assertTrue(any("other lane gates remain standing" in error for error in validate(root)))


if __name__ == "__main__":
    unittest.main()
''')

# The audit payload is temporary evidence; the durable report preserves its findings.
audit_payload = ROOT / "docs/_C2_AUDIT_INPUT.md"
if audit_payload.exists():
    audit_payload.unlink()
self_path = ROOT / "tools/_apply_c2_tests.py"
if self_path.exists():
    self_path.unlink()
