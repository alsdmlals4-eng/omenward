from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "design" / "APPROVED_V2_DEMOLITION_CANCELS_PLANNED_WORK_2026-07-26.md"
REVIEW = ROOT / "docs" / "reviews" / "2026-07-26-v2-demolition-cancels-planned-work-review.md"
HEADSTART_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_ONE_SECOND_HEADSTART_2026-07-26.md"
CASCADE_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PRODUCER_CANCEL_CASCADE_2026-07-26.md"
REVALIDATION_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md"
TRANSACTION_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md"


class DemolitionCancelsPlannedWorkContractTests(unittest.TestCase):
    def test_contract_is_routed_to_current_parent_policies(self) -> None:
        self.assertTrue(POLICY.is_file())
        self.assertTrue(REVIEW.is_file())
        text = POLICY.read_text(encoding="utf-8")
        for parent in (
            HEADSTART_POLICY.name,
            CASCADE_POLICY.name,
            REVALIDATION_POLICY.name,
            TRANSACTION_POLICY.name,
        ):
            self.assertIn(parent, text)

    def test_required_policy_markers_are_present(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "DEMOLITION_WITH_PLANNED_WORK_POLICY: PREVIEW_CONFIRM_CANCEL_THEN_DEMOLISH",
            "PLANNED_WORK_IMPACT_PREVIEW: REQUIRED",
            "PLANNED_WORK_CANCEL_CONFIRMATION: REQUIRED",
            "PLANNED_WORK_VIRTUAL_COST_RELEASE: REQUIRED",
            "DEMOLITION_AND_WORK_CANCEL: ATOMIC_SINGLE_QUEUE_MUTATION",
            "SILENT_PLANNED_WORK_DISCARD: FORBIDDEN",
            "PLANNED_WORK_COST_WASTE: FORBIDDEN",
            "STALE_DEMOLITION_CONFIRMATION: REJECT_WITH_ZERO_MUTATION",
            "QUEUE_REVISION_INCREMENT_PER_DEMOLITION_OVERRIDE: EXACTLY_ONCE",
            "POST_DEMOLITION_FULL_REPLAY: REQUIRED",
            "LIVE_LEDGER_MUTATION_BEFORE_CONFIRM: FORBIDDEN",
            "DemolitionPlannedWorkImpactPreview",
            "demolition_override_basis_hash",
            "QueueMutationReceipt",
            "queue_mutation_transaction_id",
        ):
            self.assertIn(marker, text)

    def test_upgrade_cancel_cost_release_and_demolition_are_atomic(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("업그레이드 예약 제거", text)
        self.assertIn("업그레이드 1초 진행 상태 제거", text)
        self.assertIn("업그레이드 planned gold debit 제거", text)
        self.assertIn("building을 branch에서 REMOVED 처리", text)
        self.assertIn("node 점유 해제", text)
        self.assertIn("전체 성공", text)
        self.assertIn("전체 상태 변경 0", text)

    def test_provisional_construction_demolition_is_construction_cancel(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("승인된 의미는 `건설 예약 취소`", text)
        self.assertIn("provisional 건설 예약 제거", text)
        self.assertIn("건설 가상 비용 제거", text)
        self.assertIn("provisional output 제거", text)
        self.assertIn("별도의 live 철거 이벤트나 철거 비용을 만들지 않는다", text)

    def test_dependents_stale_confirmation_and_replay_are_explicit(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("transitive descendants of removed consumers", text)
        self.assertIn("직접 영향과 transitive 영향을 구분해 표시", text)
        self.assertIn("STALE_DEMOLITION_PLANNED_WORK_PREVIEW", text)
        self.assertIn("queue_revision 정확히 1 증가", text)
        self.assertIn("entry snapshot부터 전체 queue replay", text)
        self.assertIn("과거 업그레이드 1초가 누적되지 않음", text)

    def test_virtual_cost_release_is_not_live_refund(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("취소되는 미확정 작업의 비용은 live 환불이 아니다", text)
        self.assertIn("confirm 전 live 금화를 차감하거나 환불하지 않는다", text)
        self.assertIn("동일 비용을 두 번 해제하지 않는다", text)
        self.assertIn("업그레이드 비용을 소비한 뒤 철거하는 표현을 금지", text)

    def test_review_records_resolution_without_product_authorization(self) -> None:
        policy = POLICY.read_text(encoding="utf-8")
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("F-22: RESOLVED", review)
        self.assertIn("PREVIEW_CONFIRM_CANCEL_WORK_RELEASE_VIRTUAL_COST_THEN_DEMOLISH", review)
        self.assertIn("SHORT_DURATION_COMPLETION_BOUNDARY: REVIEW_PENDING", policy)
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", policy)
        self.assertIn("V2_IMPLEMENTATION: NOT_STARTED", policy)


if __name__ == "__main__":
    unittest.main()
