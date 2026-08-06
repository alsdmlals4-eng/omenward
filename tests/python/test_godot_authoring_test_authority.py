from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "tools/validate_godot_authoring_test_authority.py"
ADOPTION = ROOT / "docs/operations/GUT_ADOPTION_RECORD.v1.json"
ENTRY_STATE = ROOT / "docs/operations/WORK_ENTRY_GATE_STATE.v1.json"
SPEC = ROOT / "docs/design/PROPOSED_OMENWARD_HIGODOT_GUT_AUTHORITY_AND_GUT_9_7_1_ADOPTION_2026-08-06.md"


def load_validator():
    spec = importlib.util.spec_from_file_location("authority_validator", VALIDATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError("validator import spec unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GodotAuthoringTestAuthorityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = load_validator()
        cls.adoption = json.loads(ADOPTION.read_text(encoding="utf-8"))
        cls.entry = json.loads(ENTRY_STATE.read_text(encoding="utf-8"))
        cls.spec_text = SPEC.read_text(encoding="utf-8")

    def test_contract_accepts_truthful_blocked_bootstrap_state(self) -> None:
        errors = self.validator.validate_contract(ROOT)
        self.assertEqual(errors, [])
        decision = self.validator.evaluate_entry(self.entry, changed_files=self.validator.BOOTSTRAP_ALLOWLIST)
        self.assertTrue(decision.allowed)
        self.assertEqual(decision.status, "BOOTSTRAP_ONLY_ALLOWED_WHILE_ENTRY_BLOCKED")
        self.assertIn("CANON_LEDGER_STALE", decision.blockers)
        self.assertIn("GUT_VENDOR_TREE_MISMATCH", decision.blockers)

    def test_higodot_and_gut_cannot_share_mutation_authority(self) -> None:
        mutated = copy.deepcopy(self.adoption)
        mutated["authorities"]["gut"]["may_mutate_project_files"] = True
        errors = self.validator.validate_adoption(mutated)
        self.assertIn("GUT must not mutate project authoring files", errors)

    def test_activation_cannot_be_ready_with_vendor_mismatch_or_runtime_not_run(self) -> None:
        mutated = copy.deepcopy(self.adoption)
        mutated["adoption_status"] = "ACTIVATION_READY"
        errors = self.validator.validate_adoption(mutated)
        self.assertIn("ACTIVATION_READY requires exact upstream vendor tree match", errors)
        self.assertIn("ACTIVATION_READY requires Godot import and GUT CLI smoke PASS", errors)

    def test_rejected_images_cannot_be_promoted_to_ready_or_awaiting(self) -> None:
        for forbidden in ("READY", "AWAITING", "APPROVED"):
            mutated = copy.deepcopy(self.entry)
            mutated["image_review_readback"]["rejected_image_ids"][0]["status"] = forbidden
            errors = self.validator.validate_entry_state(mutated)
            self.assertIn("rejected image cannot be READY/AWAITING/APPROVED", errors)

    def test_non_bootstrap_work_is_blocked_until_all_entry_surfaces_are_current(self) -> None:
        decision = self.validator.evaluate_entry(
            self.entry,
            changed_files=("src/domain/example.gd",),
        )
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.status, "WORK_ENTRY_BLOCKED")
        self.assertIn("CANON_LEDGER_STALE", decision.blockers)
        self.assertIn("IMAGE_APPROVAL_NONE_AVAILABLE", decision.blockers)

    def test_ready_claim_is_rejected_while_blockers_remain(self) -> None:
        mutated = copy.deepcopy(self.entry)
        mutated["gate_status"] = "READY"
        errors = self.validator.validate_entry_state(mutated)
        self.assertIn("gate cannot claim READY while blockers remain", errors)

    def test_spec_declares_non_overlapping_roles_and_removal_path(self) -> None:
        for marker in (
            "HIGODOT_AUTHORING_AUTHORITY",
            "GUT_TEST_AUTHORITY",
            "MUTATION_AUTHORITY_OVERLAP = FORBIDDEN",
            "VENDOR_TREE_MISMATCH",
            "REMOVAL_AND_ROLLBACK_PROCEDURE",
            "WORK_ENTRY_GATE = FAIL_CLOSED",
        ):
            self.assertIn(marker, self.spec_text)


if __name__ == "__main__":
    unittest.main()
