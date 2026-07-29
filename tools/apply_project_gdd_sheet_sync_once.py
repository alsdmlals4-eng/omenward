from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_SHA = "c987647d01ad2baa028a16e03d85ddfc1572a727"
SHEET_ID = "1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit"
REGISTRY_PATH = "docs/base/SKILL_REGISTRY.json"
TEST_PATH = "tests/python/test_bca_visual_sheet_adoption.py"
TABS = [
    "00_프로젝트_허브", "01_작업순서", "02_현재_확정결정", "03_근거_라이브러리",
    "04_누락_충돌_감사", "05_GDD_요약", "10_제품방향", "11_세계관", "12_핵심루프",
    "13_주요인물", "14_조연_세력_관계", "15_조작_게임규칙", "20_코어경험_데모목표",
    "30_데모범위_품질기준_제작기반", "40_핵심시스템_메인콘텐츠", "41_성장_경제",
    "50_메인콘텐츠", "60_UX_UI_접근성", "70_아트_오디오_에셋", "71_이미지기획_생성목록",
    "72_이미지검수_승인로그", "80_데모_버티컬슬라이스_플레이테스트", "90_본제작_출시_사업",
    "98_Base_반영후보", "99_변경이력",
]


def update_active_text(path: str) -> None:
    file = ROOT / path
    if not file.exists():
        return
    text = file.read_text(encoding="utf-8")
    for old_sha in (
        "7072b9e2742a60d7548fd39df3328ad76a8dbad1",
        "6a224e450f9420223c00921f3c56e051612f92ad",
        "41a20584dd2ee51d917e5c9d7cab6838e1ceba7e",
    ):
        text = text.replace(old_sha, BASE_SHA)
    text = text.replace("NOT_CONFIGURED", "PROJECT_SHEET_CONFIGURED")
    text = text.replace(
        "정확한 URL·권한을 확인하기 전에는 새 Sheet를 추정 생성하지 않는다.",
        "검증된 URL·ID·탭을 사용하고 사용자 Sheet 수정은 `PROPOSED_SHEET_CHANGE`로 보존한다.",
    )
    text = text.replace(
        "실제 Google Sheet URL·권한과 실제 생성 이미지·런타임 검수",
        "실제 생성 이미지·런타임·사용자 시각 검수",
    )
    if path == "docs/BASE_RULES_VERSION.md":
        text = text.replace("코어 25개 Skill 집합", "전체 ACTIVE 27개 Skill 집합")
        text = text.replace("Base 활성 Skill 25개", "Base 활성 Skill 27개")
        text = text.replace("코어 25개 Skill 동기화", "전체 ACTIVE 27개 Skill 동기화")
        anchor = "25. `diagnosing-game-engine-runtime-failures`"
        if anchor in text and "26. `governing-legacy-retention-and-archives`" not in text:
            text = text.replace(
                anchor,
                anchor
                + "\n26. `governing-legacy-retention-and-archives`"
                + "\n27. `evaluating-godot-assets-and-plugins-before-creation`",
            )
    file.write_text(text, encoding="utf-8")


for path in (
    "README.md",
    "AGENTS.md",
    "docs/BASE_RULES_VERSION.md",
    "docs/BCA_VISUAL_SHEET_ADOPTION_AUDIT.md",
    "docs/GPT_IMAGE_GENERATION_AND_REVIEW_WORKFLOW.md",
):
    update_active_text(path)

workbook = [
    "# OMENWARD 프로젝트 Google Sheets Workbook",
    "",
    "```yaml",
    "project: omenward",
    "sheet_status: PROJECT_SHEET_CONFIGURED",
    f"spreadsheet_url: {SHEET_URL}",
    f"spreadsheet_id: {SHEET_ID}",
    "workbook_role: USER_FACING_GDD_WORKSPACE",
    "sheet_edit_policy: PROPOSED_SHEET_CHANGE",
    f"base_commit: {BASE_SHA}",
    "last_verified_at: 2026-07-29",
    "```",
    "",
    "Google Sheets는 3릴·3전선·건물·경제·플레이테스트의 전체 흐름을 사용자가 확인·수정하고 AI가 GitHub 정본·실제 구현과 함께 읽는 GDD 작업면이다.",
    "",
    "## 검증된 탭",
]
workbook.extend(f"- `{tab}`" for tab in TABS)
workbook.extend(
    [
        "",
        "## 프로젝트 책임 매핑",
        "",
        "| 의미 구조 | 프로젝트 책임 원본 |",
        "|---|---|",
        "| 핵심루프 | 룰렛 구조 설계→TokenSource→전선 커밋→자동전투→전술 계획 |",
        "| 핵심시스템 | 승인된 전체 Vertical Slice 계약, 건물 작업·F-30 정본 |",
        "| 성장·경제 | 금고·골드·토큰·건설·수리·환급 정본 |",
        "| UX·검증 | 룰렛 통제감 Evidence Pack과 사람 검증 Artifact |",
        "| 이미지 계획·검수 | `docs/GPT_IMAGE_GENERATION_AND_REVIEW_WORKFLOW.md` |",
        "",
        "GitHub에 없는 사용자 수정은 `PROPOSED_SHEET_CHANGE`로 보존하고 승인 후 양쪽을 재조회한다.",
    ]
)
(ROOT / "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md").write_text(
    "\n".join(workbook) + "\n", encoding="utf-8"
)

registry_path = ROOT / REGISTRY_PATH
registry = json.loads(registry_path.read_text(encoding="utf-8"))
base = registry.setdefault("base_source", {})
base["commit"] = BASE_SHA
base.update(
    {
        "project_sheet_status": "PROJECT_SHEET_CONFIGURED",
        "project_sheet_url": SHEET_URL,
        "project_sheet_id": SHEET_ID,
        "project_sheet_role": "USER_FACING_GDD_WORKSPACE",
        "project_sheet_edit_policy": "PROPOSED_SHEET_CHANGE",
        "project_sheet_last_verified_at": "2026-07-29",
    }
)
registry["bca_visual_sheet"] = {
    "sheet_status": "PROJECT_SHEET_CONFIGURED",
    "spreadsheet_url": SHEET_URL,
    "spreadsheet_id": SHEET_ID,
    "workbook_role": "USER_FACING_GDD_WORKSPACE",
    "sheet_edit_policy": "PROPOSED_SHEET_CHANGE",
    "last_verified_at": "2026-07-29",
    "required_tabs": TABS,
}
registry_path.write_text(
    json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

test = f'''from __future__ import annotations
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
BASE_SHA = "{BASE_SHA}"
SHEET_ID = "{SHEET_ID}"
REGISTRY_PATH = "{REGISTRY_PATH}"
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
'''
(ROOT / TEST_PATH).write_text(test, encoding="utf-8")
