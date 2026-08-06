from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = ROOT / "tools/validate_local_exact_head_fallback.py"
POLICY_PATH = ROOT / "docs/operations/LOCAL_EXACT_HEAD_FALLBACK_POLICY.v1.json"
EVIDENCE_PATH = ROOT / "docs/evidence/PR157_LOCAL_EXACT_HEAD_VERIFICATION_2026-08-07.json"


def load_validator():
    spec = importlib.util.spec_from_file_location("local_exact_head_fallback", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("validator import unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LocalExactHeadFallbackTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = load_validator()
        cls.policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
        cls.evidence = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))

    def test_truthful_policy_and_pr157_evidence_pass(self) -> None:
        self.assertEqual(self.validator.validate_policy(self.policy), [])
        self.assertEqual(self.validator.validate_evidence(self.evidence, self.policy), [])

    def test_actions_green_cannot_be_claimed(self) -> None:
        mutated = copy.deepcopy(self.policy)
        mutated["trigger"]["github_actions_green"] = True
        self.assertIn(
            "GitHub Actions Green must remain false",
            self.validator.validate_policy(mutated),
        )

    def test_runtime_surfaces_are_not_fallback_eligible(self) -> None:
        mutated = copy.deepcopy(self.policy)
        mutated["scope"]["eligible_pr_classes"].append("GODOT_RUNTIME")
        self.assertIn(
            "runtime or product class cannot be fallback-eligible",
            self.validator.validate_policy(mutated),
        )

    def test_repository_policy_bypass_is_forbidden(self) -> None:
        mutated = copy.deepcopy(self.policy)
        mutated["merge_policy"]["repository_policy_bypass"] = "ALLOWED"
        self.assertIn(
            "repository policy bypass must be FORBIDDEN",
            self.validator.validate_policy(mutated),
        )

    def test_exact_head_and_blob_readback_are_mandatory(self) -> None:
        mutated = copy.deepcopy(self.policy)
        mutated["verification_requirements"]["require_exact_head"] = False
        mutated["verification_requirements"]["require_git_blob_sha"] = False
        errors = self.validator.validate_policy(mutated)
        self.assertIn("exact HEAD verification must be required", errors)
        self.assertIn("Git blob SHA readback must be required", errors)

    def test_pr157_evidence_is_bound_to_current_exact_head(self) -> None:
        mutated = copy.deepcopy(self.evidence)
        mutated["subject"]["head_sha"] = "0" * 40
        self.assertIn(
            "PR157 exact head mismatch",
            self.validator.validate_evidence(mutated, self.policy),
        )

    def test_reconstructed_commands_must_all_exit_zero(self) -> None:
        mutated = copy.deepcopy(self.evidence)
        mutated["reconstructed_execution"]["commands"][1]["exit_code"] = 1
        self.assertIn(
            "reconstructed command failed",
            self.validator.validate_evidence(mutated, self.policy),
        )

    def test_runtime_is_not_silently_promoted_by_process_evidence(self) -> None:
        mutated = copy.deepcopy(self.evidence)
        mutated["limitations"]["godot_runtime"] = "PASS"
        self.assertIn(
            "Godot runtime must remain NOT_RUN or BLOCKED_UNVERIFIED",
            self.validator.validate_evidence(mutated, self.policy),
        )


if __name__ == "__main__":
    unittest.main()
