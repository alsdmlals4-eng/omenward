from __future__ import annotations

import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
CANDIDATE_RECORD = ROOT / "docs" / "images" / "planning" / "OMENWARD_WIDE_CONNECTED_STRATEGIC_FRONT_TERRAIN_CANDIDATE_2026-08-30.md"
APPROVED_RECORD = ROOT / "docs" / "images" / "approved" / "OMENWARD_WIDE_CONNECTED_STRATEGIC_FRONT_TERRAIN_V1.md"


class WideConnectedStrategicMapContractTest(unittest.TestCase):
    def test_approved_candidate_is_retained_after_the_battle_primary_override(self) -> None:
        text = CANDIDATE_RECORD.read_text(encoding="utf-8")
        self.assertIn("status: USER_APPROVED__CANON_REGISTERED__SUPERSEDED_RUNTIME_CONSUMER__RUNTIME_NOT_RUN", text)
        self.assertIn("runtime_asset: assets/art/battlefield/wide_connected_strategic_front_terrain_v1.png", text)
        self.assertIn("Issue #235", text)
        self.assertIn("NO_RIVER", text)
        self.assertIn("BATTLEFIELD_VISIBLE_EXCLUDES = CONSTRUCTION_PADS + PRODUCTION_BUILDINGS + MAP_BUILDING_POPUPS", text)
        self.assertIn("current_runtime_binding: NONE__SUPERSEDED_BY_OMW-PLAN-20260830-BATTLE-PRIMARY-MARCH-MINIMAP-01", text)
        approved = APPROVED_RECORD.read_text(encoding="utf-8")
        self.assertIn("asset_id: OMW-IMG-20260830-WIDE-CONNECTED-STRATEGIC-FRONT-TERRAIN-V1", approved)
        self.assertIn("sha256: 1E56ACBD1B75394ADC7A7D059D0C3AB4AFCECA3B7CAF39F294886B7714768FA8", approved)
        self.assertIn("user_asset_lock: USER_APPROVED_EXACT_CANDIDATE", approved)
        self.assertIn("current_runtime_binding: NONE__SUPERSEDED_BY_OMW-PLAN-20260830-BATTLE-PRIMARY-MARCH-MINIMAP-01", approved)
        self.assertIn("runtime: NOT_RUN", approved)
        self.assertIn("human_readability: NOT_RUN", approved)


if __name__ == "__main__":
    unittest.main()
