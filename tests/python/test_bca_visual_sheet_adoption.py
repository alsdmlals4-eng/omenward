from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE_SHA = "c987647d01ad2baa028a16e03d85ddfc1572a727"
SHEET_ID = "1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw"
C1_HEAD = "19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9"
C1_RUN = "29926598807"


class OmenwardGddSheetTests(unittest.TestCase):
    def test_legacy_sheet_contract_remains_traceable(self) -> None:
        registry = json.loads((ROOT / "docs/base/SKILL_REGISTRY.json").read_text(encoding="utf-8"))
        self.assertEqual(registry["base_source"]["commit"], BASE_SHA)
        self.assertEqual(registry["bca_visual_sheet"]["spreadsheet_id"], SHEET_ID)
        self.assertIn("05_GDD_요약", registry["bca_visual_sheet"]["required_tabs"])
        self.assertIn("15_조작_게임규칙", registry["bca_visual_sheet"]["required_tabs"])
        workbook = (ROOT / "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md").read_text(encoding="utf-8")
        for token in ("PROJECT_SHEET_CONFIGURED", SHEET_ID):
            self.assertIn(token, workbook)
        current_map = (ROOT / "docs/DOCUMENTATION_MAP.md").read_text(encoding="utf-8")
        self.assertIn("Google Sheet", current_map)
        self.assertIn("current human authority", current_map)

    def test_c1_exact_proof_lives_in_historical_evidence_owner(self) -> None:
        report = (ROOT / "docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md").read_text(encoding="utf-8")
        self.assertIn(f"구현 검증 head: `{C1_HEAD}`", report)
        self.assertIn(f"GitHub Actions run: `{C1_RUN}`", report)
        status = (ROOT / "docs/CURRENT_IMPLEMENTATION_STATUS.md").read_text(encoding="utf-8")
        self.assertIn("LEGACY_C1_C2_C3_PROVEN", status)
        self.assertIn("CURRENT_GODOT_RUNTIME = PARTIAL__BATTLE_PRIMARY_MACHINE_VERIFIED__RUNTIME_NOT_RUN", status)
        self.assertNotIn(f"C1 구현 검증 head: `{C1_HEAD}`", status)
        self.assertNotIn(f"C1 최종 검증 run: `{C1_RUN}`", status)


if __name__ == "__main__":
    unittest.main()
