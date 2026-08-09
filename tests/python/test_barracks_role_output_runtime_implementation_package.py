from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
AUTHORITY = ROOT / "docs/design/APPROVED_OMENWARD_BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE_2026-08-09.md"
PLAN = ROOT / "docs/superpowers/plans/2026-08-09-barracks-role-output-runtime-implementation-package.md"
ACTIVE_STATE = ROOT / "docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json"
PACKAGE_STATE = ROOT / "docs/operations/BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE_STATE.v1.json"
UNIT_INSTANCE = ROOT / "scripts/battle/unit_instance.gd"
LANE_STATE = ROOT / "scripts/battle/lane_state.gd"
SIMULATOR = ROOT / "scripts/battle/battle_simulator.gd"
PROFILE = ROOT / "scripts/data/unit_archetype_profile.gd"

DECISION = "OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1"
PARENT = "OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-MEASUREMENT-SCENARIOS-DEFINITION-V1"


class BarracksRoleOutputRuntimeImplementationPackageTest(unittest.TestCase):
    def test_current_runtime_gap_is_reproducible(self) -> None:
        unit = UNIT_INSTANCE.read_text(encoding="utf-8")
        lane = LANE_STATE.read_text(encoding="utf-8")
        sim = SIMULATOR.read_text(encoding="utf-8")
        profile = PROFILE.read_text(encoding="utf-8")
        self.assertIn("magic_resistance", profile)
        self.assertIn("target_priority_tags", profile)
        self.assertIn('func receive_damage(raw_damage: float)', unit)
        self.assertNotIn('magic_resistance', unit.split('func receive_damage(raw_damage: float)', 1)[1].split('\n\n', 1)[0])
        self.assertIn("func find_target(attacker", lane)
        self.assertNotIn("target_priority_tags", lane)
        self.assertIn("func drain_events()", sim)
        self.assertIn("func _record_event(event_type", sim)

    def test_package_authority_exists_and_freezes_minimal_scope(self) -> None:
        self.assertTrue(AUTHORITY.is_file(), f"missing authority: {AUTHORITY.relative_to(ROOT)}")
        text = AUTHORITY.read_text(encoding="utf-8")
        for marker in (
            DECISION,
            PARENT,
            "PACKAGE_MODE = SPEC_ONLY_NO_PRODUCT_MUTATION",
            "GENERIC_ABILITY_SYSTEM = DEFERRED_NOT_REQUIRED",
            "TARGET_PRIORITY_SOURCE = EXISTING_TARGET_PRIORITY_TAGS",
            "ROLE_EVENT_SURFACE = EXTEND_EXISTING_RECORD_EVENT_DRAIN_EVENTS",
            "POC_NUMERICS = PROVISIONAL_POC_INPUT_NOT_FINAL_PRODUCT_AUTHORITY",
            "HIGODOT_AUTHORING = REQUIRED_FOR_PERSISTENT_GODOT_MUTATION",
            "GUT_TEST_AUTHORITY = REQUIRED_FOR_DETERMINISTIC_ACCEPTANCE",
            "HERA_ACCEPTANCE = LIVE_QA_SOURCE_DELTA_NONE",
            "FINAL_FUNCTIONAL_VALUE_INDEX = NOT_SELECTED",
            "FINAL_PARAMETER_VECTOR = NOT_SELECTED",
        ):
            self.assertIn(marker, text)

    def test_execution_plan_is_concrete_and_role_separated(self) -> None:
        self.assertTrue(PLAN.is_file(), f"missing plan: {PLAN.relative_to(ROOT)}")
        text = PLAN.read_text(encoding="utf-8")
        for marker in (
            "GUT RED",
            "HiGodot authoring manifest",
            "Priest",
            "Mage",
            "Flier",
            "Giant",
            "FV-PRIEST-01",
            "FV-MAGE-01",
            "FV-FLIER-01",
            "FV-GIANT-01",
            "tracked source delta NONE",
            "zero-test discovery",
        ):
            self.assertIn(marker, text)

    def test_package_state_defers_execution_without_falsely_closing_global_blocker(self) -> None:
        package = json.loads(PACKAGE_STATE.read_text(encoding="utf-8"))
        active = json.loads(ACTIVE_STATE.read_text(encoding="utf-8"))
        self.assertEqual(package["decision_id"], DECISION)
        self.assertEqual(package["parent_decision_id"], PARENT)
        self.assertEqual(package["package_mode"], "SPEC_ONLY_NO_PRODUCT_MUTATION")
        self.assertEqual(package["persistent_authoring_authority"], "HIGODOT_REQUIRED")
        self.assertEqual(package["execution_status"], "DEFERRED_EXTERNAL_EXECUTOR")
        self.assertEqual(package["global_entry_gate_transition"], "NONE_UNTIL_ACTUAL_HIGODOT_GUT_HERA_RUNTIME_GREEN")
        self.assertIsNone(package["final_functional_value_index"])
        self.assertIsNone(package["final_parameter_vector"])
        self.assertEqual(active["entry_gate"]["decision"], "BLOCK")
        self.assertIn("BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED", active["entry_gate"]["blocking_reasons"])
        self.assertEqual(active["entry_gate"]["allowed_next_actions"][0], "BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE")


if __name__ == "__main__":
    unittest.main()
