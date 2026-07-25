from __future__ import annotations

import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs" / "design" / "APPROVED_V2_TACTICAL_LEGENDARY_RESERVATION_ORDER_2026-07-26.md"
PARENT_POLICY = ROOT / "docs" / "design" / "APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md"
MAPRUN_POLICY = ROOT / "docs" / "design" / "APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md"


class TacticalLegendaryReservationContractTests(unittest.TestCase):
    def test_contract_file_and_parent_routes_exist(self) -> None:
        self.assertTrue(POLICY.is_file())
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn(PARENT_POLICY.name, text)
        self.assertIn(MAPRUN_POLICY.name, text)

    def test_ordered_virtual_reservation_markers_are_present(self) -> None:
        text = POLICY.read_text(encoding="utf-8")
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

    def test_parent_and_maprun_contracts_remain_available(self) -> None:
        parent = PARENT_POLICY.read_text(encoding="utf-8")
        maprun = MAPRUN_POLICY.read_text(encoding="utf-8")
        self.assertIn("PLAYER_ALIVE_LEGENDARY_BATTLEFIELD_CAP: 1", parent)
        self.assertIn("AUTO_DOWNGRADE_WITHOUT_CONSENT: FORBIDDEN", parent)
        self.assertIn("TACTICAL_PLANNING", maprun)
        self.assertIn("[전투 재개]", maprun)
        self.assertIn("비용을 일괄 차감한 뒤 동시에 적용", maprun)


if __name__ == "__main__":
    unittest.main()
