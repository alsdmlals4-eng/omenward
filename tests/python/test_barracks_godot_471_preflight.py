from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXECUTOR = ROOT / "tools/invoke_barracks_role_output_executor.ps1"


class BarracksGodot471PreflightContract(unittest.TestCase):
    def test_executor_requires_exact_live_godot_471_before_full_child(self) -> None:
        text = EXECUTOR.read_text(encoding="utf-8")

        self.assertIn("godot_version", text)
        self.assertIn("editor_pid", text)
        self.assertIn("4.7.1-stable", text)
        self.assertIn("HiGodot live session Godot version preflight PASS", text)
        self.assertIn("Parent HiGodot Godot version:", text)
        self.assertIn("Parent HiGodot editor PID:", text)
        self.assertLess(text.index("4.7.1-stable"), text.index("$issueBody ="))

    def test_executor_pins_verified_gut_single_test_entrypoint_for_child(self) -> None:
        text = EXECUTOR.read_text(encoding="utf-8")

        self.assertIn("-gtest=res://tests/gut/test_barracks_role_output.gd", text)
        self.assertIn("Do not use -gdir=res://tests/gut for Issue #176", text)
        self.assertIn("resolve the exact live editor executable from the parent-provided editor PID", text)


if __name__ == "__main__":
    unittest.main()
