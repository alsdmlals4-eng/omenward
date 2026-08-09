from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
ROUTER = ROOT / ".agents" / "skills" / "omenward-workflow-router" / "SKILL.md"


class ExecutorPreflightRouterContractTest(unittest.TestCase):
    def test_verified_parent_preflight_can_satisfy_router_gate_without_recursive_reentry(self) -> None:
        text = ROUTER.read_text(encoding="utf-8")
        self.assertIn("verified parent executor preflight", text)
        self.assertIn("do not rerun the validator", text)
        self.assertIn("do not invoke the parent executor recursively", text)


if __name__ == "__main__":
    unittest.main()
