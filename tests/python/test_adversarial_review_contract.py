from __future__ import annotations

import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
REGISTRY = json.loads((ROOT / "docs" / "base" / "SKILL_REGISTRY.json").read_text(encoding="utf-8"))


class AdversarialReviewContractTests(unittest.TestCase):
    def test_review_skill_contains_all_three_methods(self) -> None:
        path = ROOT / next(
            skill["path"]
            for skill in REGISTRY["skills"]
            if skill["id"] == "foundation.validation-review"
        )
        text = path.read_text(encoding="utf-8")
        for required in ("Adversarial Review", "Red Teaming", "Critique–Refine"):
            self.assertIn(required, text)

    def test_shared_contract_blocks_false_completion(self) -> None:
        text = (ROOT / "skills" / "SHARED_EXECUTION_CONTRACT.md").read_text(encoding="utf-8")
        self.assertIn("P0·P1이 남으면 완료하지 않는다", text)
        self.assertIn("NOT_RUN", text)
        self.assertIn("문서에 테스트 이름이 존재한다는 사실은 `PROVEN`이 아니다", text)

    def test_review_stack_uses_active_validation_and_freshness_skills(self) -> None:
        stack = REGISTRY["routing"]["review_stack"]
        self.assertEqual(
            stack,
            ["foundation.validation-review", "specialist.canonical-freshness"],
        )
        self.assertNotIn("discipline.integration-review", stack)

    def test_shared_contract_matches_registry_routing_limits(self) -> None:
        text = (ROOT / "skills" / "SHARED_EXECUTION_CONTRACT.md").read_text(encoding="utf-8")
        self.assertIn("`routing.always_on`은 비워", text)
        self.assertIn("지원 Discipline은 최대 1개", text)
        for skill_id in REGISTRY["routing"]["review_stack"]:
            self.assertIn(f"`{skill_id}`", text)


if __name__ == "__main__":
    unittest.main()
