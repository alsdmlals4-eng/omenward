from __future__ import annotations

import unittest

from tools.validate_runtime_transition_scope import (
    APPROVED_RUNTIME_FILES,
    validate_runtime_transition,
)

EXPECTED_CURRENT_RUNTIME_FILES = {
    ".gitattributes",
    ".github/workflows/validate-active-integrated-contract-v4-4.yml",
    ".github/workflows/validate-base-v9-adoption.yml",
    ".github/workflows/validate-project-base-adapter.yml",
    "scripts/battle/battle_simulator.gd",
    "scripts/battle/lane_state.gd",
    "scripts/battle/unit_instance.gd",
    "tests/gut/test_barracks_role_output.gd",
    "tests/gut/test_barracks_role_output.gd.uid",
    "tests/headless/barracks_role_output_fv_test.gd",
    "tests/headless/barracks_role_output_fv_test.gd.uid",
    "tests/python/test_barracks_functional_value_combat_numerics_review.py",
    "tests/python/test_barracks_godot_471_preflight.py",
    "tests/python/test_barracks_role_output_runtime_implementation_package.py",
    "tests/python/test_base_recovery_map.py",
    "tests/python/test_runtime_transition_scope.py",
    "tools/invoke_barracks_role_output_executor.ps1",
    "tools/reconcile_and_invoke_barracks_role_output_executor.ps1",
    "tools/validate_runtime_transition_scope.py",
}


def approved_state() -> dict:
    return {
        "entry_gate": {
            "allowed_next_actions": ["BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE"]
        }
    }


class RuntimeTransitionScopeTest(unittest.TestCase):
    def test_current_approved_runtime_surface_is_exact(self) -> None:
        self.assertEqual(APPROVED_RUNTIME_FILES, EXPECTED_CURRENT_RUNTIME_FILES)
        self.assertEqual(len(APPROVED_RUNTIME_FILES), 19)
        self.assertEqual(
            validate_runtime_transition(approved_state(), APPROVED_RUNTIME_FILES),
            [],
        )

    def test_stale_adapter_generated_views_are_not_runtime_scope(self) -> None:
        stale = {
            "docs/PROJECT_OPERATING_DASHBOARD.html",
            "docs/PROJECT_OPERATING_HEALTH.json",
            "docs/operations/PROJECT_BASE_ADAPTER_SHEET_SYNC_EVIDENCE_2026-08-09.json",
            "skills/BASE_V9_ADAPTER.json",
            "skills/PROJECT_BASE_ADAPTER.json",
            "skills/PROJECT_BASE_SKILL_ADAPTER.json",
            "skills/PROJECT_SKILL_SNAPSHOT.json",
            "tests/python/test_project_base_adapter_freshness.py",
        }
        self.assertTrue(stale.isdisjoint(APPROVED_RUNTIME_FILES))

    def test_missing_active_authorization_fails_closed(self) -> None:
        errors = validate_runtime_transition(
            {"entry_gate": {"allowed_next_actions": []}},
            {"scripts/battle/lane_state.gd"},
        )
        self.assertTrue(any("does not authorize" in item for item in errors))

    def test_extra_protected_path_fails_closed(self) -> None:
        errors = validate_runtime_transition(
            approved_state(),
            {"scripts/battle/lane_state.gd", "data/units/priest.tres"},
        )
        self.assertTrue(any("unapproved protected paths" in item for item in errors))

    def test_unrelated_nonprotected_file_fails_closed(self) -> None:
        errors = validate_runtime_transition(
            approved_state(),
            {"scripts/battle/lane_state.gd", "README.md"},
        )
        self.assertTrue(any("unapproved files" in item for item in errors))

    def test_runtime_claim_without_runtime_protected_change_fails(self) -> None:
        errors = validate_runtime_transition(
            approved_state(),
            {"tests/python/test_runtime_transition_scope.py"},
        )
        self.assertTrue(any("does not contain" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
