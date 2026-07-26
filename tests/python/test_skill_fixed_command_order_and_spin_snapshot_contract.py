from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "design" / "APPROVED_V2_FIXED_COMMAND_ORDER_AND_SPIN_SNAPSHOT_2026-07-26.md"
REVIEW = ROOT / "docs" / "reviews" / "2026-07-26-v2-fixed-command-order-and-spin-snapshot-review.md"
OUTPUT_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PRODUCER_OUTPUT_FINGERPRINT_CASCADE_2026-07-26.md"
DEPENDENCY_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md"
RESUME_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_SPIN_SESSION_TACTICAL_RESUME_GATE_2026-07-26.md"
REVALIDATION_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md"


class FixedCommandOrderAndSpinSnapshotContractTests(unittest.TestCase):
    def test_contract_is_routed_to_current_parent_policies(self) -> None:
        self.assertTrue(POLICY.is_file())
        self.assertTrue(REVIEW.is_file())
        text = POLICY.read_text(encoding="utf-8")
        for parent in (
            OUTPUT_POLICY.name,
            DEPENDENCY_POLICY.name,
            RESUME_POLICY.name,
            REVALIDATION_POLICY.name,
        ):
            self.assertIn(parent, text)

    def test_fixed_order_and_no_preconfirm_mutation_markers(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "COMMAND_REORDER_UI: NOT_SUPPORTED",
            "COMMAND_EXECUTION_ORDER: SYSTEM_ASSIGNED_CREATION_SEQUENCE",
            "RESERVATION_SEQUENCE_USER_MUTATION: FORBIDDEN",
            "AUTHORITATIVE_MUTATION_BEFORE_CONFIRM: FORBIDDEN",
            "SIMULATION_TIME_ADVANCE_BEFORE_CONFIRM: FORBIDDEN",
            "PLANNING_EDIT_SCOPE: PLAN_DATA_ONLY",
            "DEPENDENCY_REORDER_POLICY: RESOLVED_NOT_SUPPORTED",
        ):
            self.assertIn(marker, text)

    def test_spin_snapshot_and_pending_reward_are_immutable(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "ROULETTE_REWARD_BASIS: IMMUTABLE_SPIN_SNAPSHOT",
            "PLANNING_QUEUE_MUTATION_RECOMPUTES_ROULETTE_RESULT: FORBIDDEN",
            "CONFIRMED_PENDING_REWARD_IDENTITY: IMMUTABLE",
            "immutable SpinSnapshot",
            "accepted movement history",
            "확정된 `PendingReward`의 정체성",
        ):
            self.assertIn(marker, text)

    def test_sequence_lifecycle_is_explicit(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("새 명령은 기존 명령 뒤의 새 sequence", text)
        self.assertIn("명령 수정은 기존 command ID와 sequence를 유지", text)
        self.assertIn("삭제 뒤 남은 sequence를", text)
        self.assertIn("재번호화하지 않는다", text)
        self.assertIn("삭제된 sequence를 같은 session에서 새 명령에 재사용하지 않는다", text)
        self.assertIn("미래 producer를 참조하는 명령 생성은 거부", text)

    def test_review_records_resolution_without_product_authorization(self) -> None:
        review = REVIEW.read_text(encoding="utf-8")
        output_policy = OUTPUT_POLICY.read_text(encoding="utf-8")
        self.assertIn("F-19: RESOLVED", review)
        self.assertIn("FIXED_CREATION_ORDER_NO_REORDER_AND_IMMUTABLE_SPIN_SNAPSHOT", review)
        self.assertIn("DEPENDENCY_REORDER_POLICY: REVIEW_PENDING", output_policy)
        self.assertIn("명시적으로 대체", POLICY.read_text(encoding="utf-8"))
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", review)


if __name__ == "__main__":
    unittest.main()
