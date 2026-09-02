from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "docs/CURRENT_CONFIRMED_DECISIONS.md"
ACTIVE_CONTEXT = ROOT / "docs/ACTIVE_CONTEXT.md"
OWNER = ROOT / "docs/design/APPROVED_OMENWARD_GLOBAL_BUILDING_ROSTER_AND_OCCUPATION_SLOTS_2026-08-30.md"

DECISION_ID = "OMW-PLAN-20260830-GLOBAL-BUILDING-ROSTER-OCCUPATION-SLOTS-01"


class GlobalBuildingRosterDecisionContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.index = INDEX.read_text(encoding="utf-8")
        cls.active_context = ACTIVE_CONTEXT.read_text(encoding="utf-8")
        cls.owner = OWNER.read_text(encoding="utf-8")

    def test_owner_locks_global_roster_rules(self) -> None:
        for marker in (
            DECISION_ID,
            "BASE_BUILDING_SLOT_CAPACITY = 6",
            "BUILDING_MAP_PLACEMENT = FORBIDDEN",
            "FIXED_TOWER_COUNT_PER_SHARED_FRONT = 1",
            "TEST_STAGE1_REJECTS_ROSTER_MUTATION",
        ):
            self.assertIn(marker, self.owner)

    def test_current_index_routes_to_global_roster_owner(self) -> None:
        self.assertIn(DECISION_ID, self.index)
        self.assertIn("APPROVED_OMENWARD_GLOBAL_BUILDING_ROSTER_AND_OCCUPATION_SLOTS_2026-08-30.md", self.index)

    def test_active_context_exposes_the_new_phase_two_route(self) -> None:
        self.assertIn(DECISION_ID, self.active_context)
        self.assertIn("GLOBAL_BUILDING_ROSTER", self.active_context)


if __name__ == "__main__":
    unittest.main()
