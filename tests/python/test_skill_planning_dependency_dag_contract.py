from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_DEPENDENCY_DAG_AND_PROVISIONAL_IDS_2026-07-26.md"
REVALIDATION_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_PLANNING_REVALIDATION_ALL_OR_NOTHING_2026-07-26.md"
RESUME_GATE_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_SPIN_SESSION_TACTICAL_RESUME_GATE_2026-07-26.md"
MAPRUN_POLICY = ROOT / "docs" / "design" / "APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md"
TRANSACTION_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md"


class PlanningDependencyDagContractTests(unittest.TestCase):
    def test_contract_is_routed_to_current_parent_policies(self) -> None:
        self.assertTrue(POLICY.is_file())
        text = POLICY.read_text(encoding="utf-8")
        for parent in (
            REVALIDATION_POLICY.name,
            RESUME_GATE_POLICY.name,
            MAPRUN_POLICY.name,
            TRANSACTION_POLICY.name,
        ):
            self.assertIn(parent, text)

    def test_dependency_dag_and_provisional_id_markers(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        for marker in (
            "PLANNING_DEPENDENCY_MODEL: EXPLICIT_DAG",
            "PROVISIONAL_ID_REQUIRED_FOR_INTRA_BATCH_REFERENCE: YES",
            "DEPENDENCY_EDGE_MUST_POINT_TO_EARLIER_SEQUENCE: YES",
            "IMPLICIT_INTRA_BATCH_REFERENCE: FORBIDDEN",
            "MISSING_PRODUCER: BLOCK_ENTIRE_PLAN",
            "FORWARD_REFERENCE: BLOCK_ENTIRE_PLAN",
            "DEPENDENCY_CYCLE: INVARIANT_VIOLATION",
            "TIME_ACCELERATION_IN_VIRTUAL_STATE: FORBIDDEN",
            "PROVISIONAL_TO_ACTUAL_ID_MAP_IN_RECEIPT: REQUIRED",
            "PLANNING_BATCH_COMMIT: ATOMIC_ALL_OR_NOTHING",
            "depends_on_reservation_ids",
            "provided_capabilities",
            "required_capabilities",
            "provisional_to_tentative_actual_id_map",
            "PlanningCommitReceipt",
        ):
            self.assertIn(marker, text)

    def test_lifecycle_does_not_accelerate_time(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("UNDER_CONSTRUCTION", text)
        self.assertIn("requires lifecycle = COMPLETED", text)
        self.assertIn("건설 시작 예약은 같은 batch에서 다음을 생산하지 않는다", text)
        self.assertIn("업그레이드 시작도 같은 batch 후속 예약에 완료 Tier를 제공하지 않는다", text)
        self.assertIn("전투 시간, 건설 시간, 업그레이드 시간, cooldown 시간이 흐른 것으로 간주하지 않는다", text)

    def test_parent_all_or_nothing_contract_is_preserved(self) -> None:
        dependency = POLICY.read_text(encoding="utf-8")
        revalidation = REVALIDATION_POLICY.read_text(encoding="utf-8")
        self.assertIn("PLANNING_BATCH_COMMIT: ATOMIC_ALL_OR_NOTHING", revalidation)
        self.assertIn("전체 예약 성공 + PlanningCommitReceipt", revalidation)
        self.assertIn("producer 생성 뒤 consumer mutation이 실패해도 producer 객체를 남기지 않는다", dependency)
        self.assertIn("provisional_id → actual_id", dependency)
        self.assertIn("동일 `planning_commit_transaction_id` 재요청", dependency)
        self.assertIn("dependent 예약을 자동으로 삭제하거나 다른 producer에 자동 연결하는 것은 금지", dependency)
        self.assertIn("PRODUCER_CANCEL_DEPENDENT_UX_POLICY: REVIEW_PENDING", dependency)
        self.assertIn("PRODUCT_CODE_AUTHORIZED: NO", dependency)


if __name__ == "__main__":
    unittest.main()
