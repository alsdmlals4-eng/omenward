from __future__ import annotations

import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]


class R54OperatingContractReconciliationTest(unittest.TestCase):
    def test_project_adapter_uses_fresh_base_and_sheet_compatibility_only(self) -> None:
        adapter = json.loads((ROOT / "skills" / "PROJECT_BASE_ADAPTER.json").read_text(encoding="utf-8"))
        current_base = adapter["current_base_authority"]
        self.assertEqual(current_base["repository"], "alsdmlals4-eng/Base")
        self.assertEqual(current_base["resolution"], "LATEST_COMPLETED_MAIN")
        self.assertEqual(current_base["loading_policy"], "BASE_OWNER_PROGRESSIVE_LOAD")
        sheet = adapter["gdd_sheet"]
        self.assertEqual(sheet["role"], "COMPATIBILITY_ONLY_MIGRATION_SOURCE")
        self.assertEqual(sheet["sync_status"], "COMPATIBILITY_ONLY")
        self.assertEqual(sheet["write_policy"], "NO_NEW_ACTIVE_WORKSPACE_WRITES")

    def test_project_router_does_not_require_pinned_base_checkout(self) -> None:
        router = (ROOT / ".agents" / "skills" / "omenward-workflow-router" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("latest completed Base main", router)
        self.assertIn("Project Notion Home", router)
        self.assertNotIn("pinned Base checkout", router)

    def test_shared_execution_contract_routes_base_freshly(self) -> None:
        contract = (ROOT / "skills" / "SHARED_EXECUTION_CONTRACT.md").read_text(encoding="utf-8")
        self.assertIn("fresh Base current authority", contract)
        self.assertIn("Notion", contract)
        self.assertIn("Google Sheet", contract)
        self.assertNotIn("`docs/BASE_RULES_VERSION.md`가 고정한 Base 원칙", contract)

    def test_base_rules_version_is_historical_adoption_record_not_current_router(self) -> None:
        text = (ROOT / "docs" / "BASE_RULES_VERSION.md").read_text(encoding="utf-8")
        self.assertIn("HISTORICAL_ADOPTION_RECORD", text)
        self.assertIn("ALWAYS_REFETCH_CURRENT_COMPLETED_MAIN", text)
        self.assertIn("COMPATIBILITY_ONLY", text)

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


if __name__ == "__main__":
    unittest.main()
