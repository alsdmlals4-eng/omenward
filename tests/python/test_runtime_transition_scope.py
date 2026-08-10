from __future__ import annotations

import unittest

from tools.validate_runtime_transition_scope import (
    APPROVED_RUNTIME_FILES,
    validate_runtime_transition,
)


def approved_state() -> dict:
    return {
        "entry_gate": {
            "allowed_next_actions": ["BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE"]
        }
    }


class RuntimeTransitionScopeTest(unittest.TestCase):
    def test_current_approved_runtime_surface_passes(self) -> None:
        self.assertEqual(
            validate_runtime_transition(approved_state(), APPROVED_RUNTIME_FILES),
            [],
        )

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
