from __future__ import annotations

import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
REGISTRY = json.loads((ROOT / "docs" / "base" / "SKILL_REGISTRY.json").read_text(encoding="utf-8"))
TACTICAL_LEGENDARY_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_TACTICAL_LEGENDARY_RESERVATION_ORDER_2026-07-26.md"
LEGENDARY_PARENT_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md"
MAPRUN_POLICY = ROOT / "docs" / "design" / "APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md"


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

    def test_tactical_legendary_reservation_contract_is_routed(self) -> None:
        self.assertTrue(TACTICAL_LEGENDARY_POLICY.is_file())
        text = TACTICAL_LEGENDARY_POLICY.read_text(encoding="utf-8")
        self.assertIn(LEGENDARY_PARENT_POLICY.name, text)
        self.assertIn(MAPRUN_POLICY.name, text)

    def test_tactical_legendary_reservation_contract_markers(self) -> None:
        text = TACTICAL_LEGENDARY_POLICY.read_text(encoding="utf-8")
        for marker in (
            "TACTICAL_PLANNING_LEGENDARY_RESERVATION: ORDERED_VIRTUAL_SIMULATION",
            "QUEUE_MUTATION_REEVALUATION: REQUIRED",
            "CONSENT_BASIS_HASH: REQUIRED",
            "TACTICAL_RESUME_REVALIDATION: REQUIRED",
            "TACTICAL_BATCH_APPLY: ATOMIC",
            "AUTO_DOWNGRADE_WITH_STALE_CONSENT: FORBIDDEN",
            "reservation_sequence",
            "PlanningCommitPlan",
            "PlanningCommitReceipt",
        ):
            self.assertIn(marker, text)

    def test_tactical_legendary_reservation_preserves_parent_contracts(self) -> None:
        parent = LEGENDARY_PARENT_POLICY.read_text(encoding="utf-8")
        maprun = MAPRUN_POLICY.read_text(encoding="utf-8")
        self.assertIn("PLAYER_ALIVE_LEGENDARY_BATTLEFIELD_CAP: 1", parent)
        self.assertIn("AUTO_DOWNGRADE_WITHOUT_CONSENT: FORBIDDEN", parent)
        self.assertIn("TACTICAL_PLANNING", maprun)
        self.assertIn("[전투 재개]", maprun)
        self.assertIn("비용을 일괄 차감한 뒤 동시에 적용", maprun)


if __name__ == "__main__":
    unittest.main()
