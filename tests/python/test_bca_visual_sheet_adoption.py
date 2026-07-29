from __future__ import annotations
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
BASE_SHA = "c987647d01ad2baa028a16e03d85ddfc1572a727"
SHEET_ID = "1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw"
REGISTRY_PATH = "docs/base/SKILL_REGISTRY.json"
class BCAAdoptionTests(unittest.TestCase):
    def test_contract(self):
        for path in ("README.md", "AGENTS.md", "docs/BASE_RULES_VERSION.md"):
            self.assertIn(BASE_SHA, (ROOT / path).read_text(encoding="utf-8"), path)
        sheet = (ROOT / "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md").read_text(encoding="utf-8")
        for token in ("PROJECT_SHEET_CONFIGURED", SHEET_ID, "USER_FACING_GDD_WORKSPACE", "PROPOSED_SHEET_CHANGE", "05_GDD_요약", "15_조작_게임규칙"):
            self.assertIn(token, sheet)
    def test_registry(self):
        registry = json.loads((ROOT / REGISTRY_PATH).read_text(encoding="utf-8"))
        self.assertEqual(registry["base_source"]["commit"], BASE_SHA)
        self.assertEqual(registry["bca_visual_sheet"]["spreadsheet_id"], SHEET_ID)
        self.assertIn("15_조작_게임규칙", registry["bca_visual_sheet"]["required_tabs"])
if __name__ == "__main__":
    unittest.main()
