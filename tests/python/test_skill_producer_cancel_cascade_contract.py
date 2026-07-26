from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PRODUCER_CANCEL_CASCADE_2026-07-26.md"
REVIEW = ROOT / "docs" / "reviews" / "2026-07-26-v2-producer-cancel-cascade-review.md"
DEPENDENCY_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md"
REVALIDATION_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md"
TRANSACTION_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md"


class ProducerCancelCascadeContractTests(unittest.TestCase):
    def test_contract_is_routed_to_current_parent_policies(self) -> None:
        self.assertTrue(POLICY.is_file())
        self.assertTrue(REVIEW.is_file())
        text = POLICY.read_text(encoding="utf-8")
        for parent in (
            DEPENDENCY_POLICY.name,
            REVALIDATION_POLICY.name,
            TRANSACTION_POLICY.name,
        ):
            self.assertIn(parent, text)

    def test_cascade_contract_markers(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "PRODUCER_CANCEL_DEPENDENT_UX_POLICY: EXPLICIT_PREVIEW_THEN_ATOMIC_CASCADE",
            "TRANSITIVE_DEPENDENT_CLOSURE: REQUIRED",
            "SILENT_DEPENDENT_AUTO_DELETE: FORBIDDEN",
            "AUTO_REBIND_TO_OTHER_PRODUCER: FORBIDDEN",
            "DANGLING_DEPENDENT_AFTER_CANCEL: FORBIDDEN",
            "CASCADE_CONFIRMATION: REQUIRED_WHEN_DEPENDENTS_EXIST",
            "CASCADE_CONFIRMATION_BASIS_HASH: REQUIRED",
            "STALE_CASCADE_CONFIRMATION: REJECT_WITH_ZERO_MUTATION",
            "CASCADE_QUEUE_MUTATION: ATOMIC",
            "QUEUE_REVISION_INCREMENT_PER_CASCADE: EXACTLY_ONCE",
            "POST_CASCADE_FULL_QUEUE_REVALIDATION: REQUIRED",
            "ProducerCancelImpactPreview",
            "cascade_confirmation_basis_hash",
            "QueueMutationReceipt",
            "queue_mutation_transaction_id",
        ):
            self.assertIn(marker, text)

    def test_transitive_shared_and_stale_cases_are_explicit(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("reverse_reachable_dependents", text)
        self.assertIn("모든 transitive dependent", text)
        self.assertIn("dependent가 여러 producer를 요구하더라도", text)
        self.assertIn("STALE_CASCADE_PREVIEW", text)
        self.assertIn("상태 변경 0", text)
        self.assertIn("과거 동의로 새 dependent를 조용히 삭제해서는 안 된다", text)
        self.assertIn("부분 삭제는 금지", text)
        self.assertIn("queue_revision 정확히 1 증가", text)

    def test_parent_pending_is_superseded_without_scope_expansion(self) -> None:
        policy = POLICY.read_text(encoding="utf-8")
        parent = DEPENDENCY_POLICY.read_text(encoding="utf-8")
        revalidation = REVALIDATION_POLICY.read_text(encoding="utf-8")
        review = REVIEW.read_text(encoding="utf-8")
        self.assertIn("PRODUCER_CANCEL_DEPENDENT_UX_POLICY: REVIEW_PENDING", parent)
        self.assertIn("명시적으로 대체", policy)
        self.assertIn("PLANNING_BATCH_COMMIT: ATOMIC_ALL_OR_NOTHING", revalidation)
        self.assertIn("dependent를 유지하려면 취소 전에 별도 큐 mutation", policy)
        self.assertIn("producer 예약 전체 취소", review)
        self.assertIn("F-17: RESOLVED", review)
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", policy)

    def test_idempotency_and_full_revalidation_are_preserved(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("동일 `queue_mutation_transaction_id` 재요청", text)
        self.assertIn("`queue_revision` 추가 증가", text)
        self.assertIn("과거 provisional-to-tentative-actual mapping", text)
        self.assertIn("남은 예약은 새 `queue_revision`에서 전체 dependency graph", text)
        self.assertIn("전체 제거 성공 + QueueMutationReceipt", text)
        self.assertIn("전체 상태 변경 0", text)


if __name__ == "__main__":
    unittest.main()
