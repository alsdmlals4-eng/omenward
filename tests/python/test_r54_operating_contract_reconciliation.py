from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]


class R54RunCommandReconciliationTest(unittest.TestCase):
    def test_run_command_plan_consumes_current_front_state_minimap_decision(self) -> None:
        plan = (ROOT / "docs" / "superpowers" / "plans" / "2026-08-24-run-command-vertical-slice.md").read_text(encoding="utf-8")
        packet = (ROOT / "docs" / "implementation" / "OMENWARD_RUN_COMMAND_VERTICAL_SLICE_EXECUTION_PACKET_2026-08-24.md").read_text(encoding="utf-8")
        decision = "OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01"
        self.assertIn(decision, plan)
        self.assertIn(decision, packet)
        self.assertIn("PER_FRONT_MINIMAP = REQUIRED", plan)
        self.assertIn("FrontStateMinimapTop", plan)
        self.assertIn("FrontStateMinimapMiddle", plan)
        self.assertIn("FrontStateMinimapBottom", plan)
        self.assertIn("three contextual minimaps", plan)
        self.assertIn("latest completed `main`", packet)

    def test_execution_packet_routes_actual_godot_build_to_codex_handoff(self) -> None:
        packet = (ROOT / "docs" / "implementation" / "OMENWARD_RUN_COMMAND_VERTICAL_SLICE_EXECUTION_PACKET_2026-08-24.md").read_text(encoding="utf-8")
        self.assertIn("CODEX_GODOT_PRODUCT_IMPLEMENTATION_HANDOFF", packet)
        self.assertIn("independently fresh-reads OMENWARD GitHub + Notion", packet)
        self.assertIn("PRODUCT_RUNTIME_IMPLEMENTATION: NOT_RUN", packet)


if __name__ == "__main__":
    unittest.main()
