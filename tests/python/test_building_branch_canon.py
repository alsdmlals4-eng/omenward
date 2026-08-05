from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
OLD_DECISION_ID = "OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1"
NEW_DECISION_ID = "OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1"
OLD_SPEC = ROOT / "docs/superpowers/specs/2026-08-05-six-building-t2-t3-branches-design.md"
OLD_CANON = ROOT / "docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md"
OLD_REVIEW = ROOT / "docs/reviews/ADVERSARIAL_BUILDING_BRANCH_COUNTER_AND_OPPORTUNITY_COST_REVIEW_2026-08-05.md"
NEW_CANON = ROOT / "docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md"
PROCESS = ROOT / "docs/process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md"

PROCESS_MARKERS = (
    "BENCHMARK_REQUIRED",
    "INDUSTRY_COMPARISON_REQUIRED",
    "MAX_APPROVAL_BATCH: 10",
    "EARLY_CHECKPOINT_ON_HIGH_RISK_CONFLICT",
    "EARLY_CHECKPOINT_ON_SESSION_END",
    "EARLY_CHECKPOINT_ON_LARGE_CANON_IMPACT",
    "TDD_MANDATORY",
    "RED → GREEN → REFACTOR",
    "EXPLICIT_BRANCH_REQUIRED_FOR_GITHUB_MUTATION",
)


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


class BuildingBranchLifecycleTests(unittest.TestCase):
    def test_historical_evidence_and_new_authority_files_exist(self) -> None:
        for path in (OLD_SPEC, OLD_CANON, OLD_REVIEW, NEW_CANON, PROCESS):
            self.assertTrue(path.is_file(), f"missing authority file: {path.relative_to(ROOT)}")

    def test_old_decision_is_preserved_as_superseded_evidence(self) -> None:
        text = read(OLD_CANON)
        self.assertIn(OLD_DECISION_ID, text)
        self.assertIn(NEW_DECISION_ID, text)
        self.assertIn("SUPERSEDED", text)
        self.assertIn("IMPLEMENTATION_INPUT_FORBIDDEN", text)
        self.assertIn("HISTORICAL_EVIDENCE_ONLY", text)

    def test_rejected_universal_branch_grammar_is_not_current_input(self) -> None:
        text = read(OLD_CANON)
        self.assertIn("모든 6종 건물 공통 A/B 분기", text)
        self.assertIn("사용 금지", text)
        for marker in (
            "안정 금고 / 행운 금고",
            "징집 농장 / 예비 농장",
            "전열 병영 / 기동 병영",
            "연사탑 / 포격탑",
            "돌격 지휘소 / 수비 지휘소",
        ):
            self.assertIn(marker, text)

    def test_new_authority_owns_current_building_tier_grammar(self) -> None:
        text = read(NEW_CANON)
        self.assertIn(NEW_DECISION_ID, text)
        self.assertIn("CURRENT_BUILDING_TIER_AUTHORITY", text)
        self.assertIn("SPECIAL_T1_TOKEN_SOURCE = NONE", text)
        self.assertIn("LINEAR_T2_BRANCHING = FORBIDDEN", text)

    def test_process_policy_still_requires_benchmark_batch_checkpoint_and_tdd(self) -> None:
        text = read(PROCESS)
        for marker in PROCESS_MARKERS:
            self.assertIn(marker, text)

    def test_historical_review_does_not_authorize_product(self) -> None:
        text = read(OLD_REVIEW)
        self.assertIn("PRODUCT_CODE = UNCHANGED", text)
        self.assertIn("IMPLEMENTATION_READINESS = BLOCKED_BY_TROOP_AND_TACTICAL_DECISIONS", text)


if __name__ == "__main__":
    unittest.main()
