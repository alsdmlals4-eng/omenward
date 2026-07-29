from __future__ import annotations
import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BASE_SHA="c987647d01ad2baa028a16e03d85ddfc1572a727"
SHEET_ID="1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw"
class OmenwardGddSheetTests(unittest.TestCase):
 def test_sheet_contract(self):
  registry=json.loads((ROOT/"docs/base/SKILL_REGISTRY.json").read_text(encoding="utf-8"))
  self.assertEqual(registry["base_source"]["commit"],BASE_SHA)
  self.assertEqual(registry["bca_visual_sheet"]["spreadsheet_id"],SHEET_ID)
  self.assertIn("05_GDD_요약",registry["bca_visual_sheet"]["required_tabs"])
  self.assertIn("15_조작_게임규칙",registry["bca_visual_sheet"]["required_tabs"])
  workbook=(ROOT/"docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md").read_text(encoding="utf-8")
  for token in ("PROJECT_SHEET_CONFIGURED",SHEET_ID,"USER_FACING_GDD_WORKSPACE","PROPOSED_SHEET_CHANGE"):
   self.assertIn(token,workbook)
 def test_c1_evidence_boundary(self):
  status=(ROOT/"docs/CURRENT_IMPLEMENTATION_STATUS.md").read_text(encoding="utf-8")
  self.assertIn("C1 구현 검증 head: `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9`",status)
  self.assertIn("C1 최종 검증 run: `29926598807`",status)
  self.assertIn("V2 구현 완료를 뜻하지 않는다",status)
if __name__=="__main__": unittest.main()
