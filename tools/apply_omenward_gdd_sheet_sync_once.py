from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_SHA = "c987647d01ad2baa028a16e03d85ddfc1572a727"
SHEET_ID = "1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit"
C1_HEAD = "19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9"
C1_RUN = "29926598807"
TABS = [
    "00_프로젝트_허브", "01_작업순서", "02_현재_확정결정", "03_근거_라이브러리",
    "04_누락_충돌_감사", "05_GDD_요약", "10_제품방향", "11_세계관", "12_핵심루프",
    "13_주요인물", "14_조연_세력_관계", "15_조작_게임규칙", "20_코어경험_데모목표",
    "30_데모범위_품질기준_제작기반", "40_핵심시스템_메인콘텐츠", "41_성장_경제",
    "50_메인콘텐츠", "60_UX_UI_접근성", "70_아트_오디오_에셋", "71_이미지기획_생성목록",
    "72_이미지검수_승인로그", "80_데모_버티컬슬라이스_플레이테스트", "90_본제작_출시_사업",
    "98_Base_반영후보", "99_변경이력",
]


def append_once(path: str, marker: str, block: str) -> None:
    file = ROOT / path
    text = file.read_text(encoding="utf-8")
    if marker not in text:
        text = text.rstrip() + "\n\n" + block.strip() + "\n"
        file.write_text(text, encoding="utf-8")


registry_path = ROOT / "docs/base/SKILL_REGISTRY.json"
registry = json.loads(registry_path.read_text(encoding="utf-8"))
base = registry.setdefault("base_source", {})
base.update({
    "repository": "alsdmlals4-eng/Base",
    "commit": BASE_SHA,
    "synced_on": "2026-07-29",
    "policy": "project_canon_first_explicit_adoption_no_auto_overwrite",
    "integrated_execution_prompt": "templates/prompts/VERTICAL_SLICE_INTEGRATED_EXECUTION_PROMPT_v8.md",
    "project_sheet_status": "PROJECT_SHEET_CONFIGURED",
    "project_sheet_url": SHEET_URL,
    "project_sheet_id": SHEET_ID,
    "project_sheet_role": "USER_FACING_GDD_WORKSPACE",
    "project_sheet_edit_policy": "PROPOSED_SHEET_CHANGE",
    "project_sheet_last_verified_at": "2026-07-29",
})
registry["bca_visual_sheet"] = {
    "status": "ADOPTED",
    "sheet_status": "PROJECT_SHEET_CONFIGURED",
    "spreadsheet_url": SHEET_URL,
    "spreadsheet_id": SHEET_ID,
    "workbook_role": "USER_FACING_GDD_WORKSPACE",
    "sheet_edit_policy": "PROPOSED_SHEET_CHANGE",
    "last_verified_at": "2026-07-29",
    "required_tabs": TABS,
    "image_modes": ["planning-visualization", "final-visual-candidate", "visual-qa-and-approval"],
    "adversarial_mode": "repository-wide-audit",
}
for skill in registry.get("skills", []):
    if skill.get("id") == "foundation.validation-review":
        for trigger in ("sheet-structure", "stale-prompt", "repository-wide-audit", "visual-qa-and-approval"):
            if trigger not in skill["triggers"]:
                skill["triggers"].append(trigger)
    if skill.get("id") == "discipline.omenward-core-design":
        for trigger in ("worldbuilding", "core-loop", "main-characters", "supporting-characters", "core-systems", "main-content"):
            if trigger not in skill["triggers"]:
                skill["triggers"].append(trigger)
    if skill.get("id") == "discipline.omenward-art-assets":
        for trigger in ("planning-visualization", "final-visual-candidate", "image-mockup", "image-approval"):
            if trigger not in skill["triggers"]:
                skill["triggers"].append(trigger)
registry_path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

workbook = [
    "# OMENWARD 프로젝트 Google Sheets Workbook", "", "```yaml", "project: omenward",
    "sheet_status: PROJECT_SHEET_CONFIGURED", f"spreadsheet_url: {SHEET_URL}",
    f"spreadsheet_id: {SHEET_ID}", "workbook_role: USER_FACING_GDD_WORKSPACE",
    "sheet_edit_policy: PROPOSED_SHEET_CHANGE", f"base_commit: {BASE_SHA}",
    "last_verified_at: 2026-07-29", "```", "",
    "Google Sheets는 3릴·3전선·건물·경제·플레이테스트의 전체 흐름을 사용자가 확인·수정하고 AI가 GitHub 정본·실제 구현과 함께 읽는 GDD 작업면이다.",
    "", "## 검증된 탭",
]
workbook.extend(f"- `{tab}`" for tab in TABS)
workbook.extend([
    "", "## 프로젝트 책임 매핑", "", "| 의미 구조 | 프로젝트 책임 원본 |", "|---|---|",
    "| 핵심루프 | 룰렛 구조 설계→TokenSource→전선 커밋→자동전투→전술 계획 |",
    "| 핵심시스템 | 승인된 전체 Vertical Slice 계약, 건물 작업·F-30 정본 |",
    "| 성장·경제 | 금고·골드·토큰·건설·수리·환급 정본 |",
    "| UX·검증 | 룰렛 통제감 Evidence Pack과 사람 검증 Artifact |",
    "| 이미지 계획·검수 | `docs/GPT_IMAGE_GENERATION_AND_REVIEW_WORKFLOW.md` |", "",
    "GitHub에 없는 사용자 수정은 `PROPOSED_SHEET_CHANGE`로 보존하고 승인 후 양쪽을 재조회한다.",
])
(ROOT / "docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md").write_text("\n".join(workbook) + "\n", encoding="utf-8")

(ROOT / "docs/BCA_VISUAL_SHEET_ADOPTION_AUDIT.md").write_text(
    "# OMENWARD BCA Visual Sheet Adoption Audit\n\n"
    f"- Base: `{BASE_SHA}`\n- Sheet: `PROJECT_SHEET_CONFIGURED`\n"
    "- 제품 코드·데이터·Scene·Resource·자산 변경: 없음\n\n"
    "## 판정\n\n"
    "- `05_GDD_요약`과 `15_조작_게임규칙` 포함 25개 의미 탭을 연결한다.\n"
    "- 생성 이미지·목업·최종 자산·런타임 승인 상태를 구분한다.\n"
    "- 실제 전장 가독성·사람 검증은 실행 전 `NOT_RUN`으로 남긴다.\n"
    "- C1 legacy 원격 증거와 V2 구현 미시작 상태를 혼동하지 않는다.\n",
    encoding="utf-8",
)
(ROOT / "docs/GPT_IMAGE_GENERATION_AND_REVIEW_WORKFLOW.md").write_text(
    "# OMENWARD GPT 이미지 생성·검수 Workflow\n\n"
    "```text\n현재 확정 결정 확인\n→ planning-visualization\n→ 브리프·구도·금지 요소 검토\n"
    "→ final-visual-candidate\n→ 실제 화면·권리·오류·일관성 검수\n→ visual-qa-and-approval\n"
    "→ PROJECT_ASSET_APPROVED\n→ Godot 적용·런타임 확인 뒤 APPLIED_AND_RUNTIME_VERIFIED\n```\n\n"
    "생성 결과는 자동 최종 자산이 아니며, 전장·릴·HUD 이미지는 1920×1080과 1280×720 가독성을 별도로 확인한다.\n",
    encoding="utf-8",
)

append_once("README.md", "## GDD Google Sheets 운영", f"""
## GDD Google Sheets 운영

- Base·GDD 기준: `{BASE_SHA}`
- Sheet: `PROJECT_SHEET_CONFIGURED`
- Workbook: `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`
- 역할: `USER_FACING_GDD_WORKSPACE`
- 사용자 편집: `PROPOSED_SHEET_CHANGE`
- UX/UI 전용 Base content commit은 `docs/UX_UI_SYSTEM.md`가 별도로 소유한다.
""")
append_once("AGENTS.md", "## GDD Google Sheets 계약", """
## GDD Google Sheets 계약

- `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`와 실제 Sheet를 GitHub 정본과 함께 읽는다.
- Sheet는 `USER_FACING_GDD_WORKSPACE`이며 독립 정본이 아니다.
- GitHub에 없는 편집은 `PROPOSED_SHEET_CHANGE`로 보존한다.
- 승인 후 GitHub와 Sheet를 모두 재조회한 경우에만 `SYNCED`로 판정한다.
- 생성 이미지와 실제 적용·런타임 승인 상태를 구분한다.
""")
append_once("skills/disciplines/governing-omenward-art-animation-and-assets/SKILL.md", "## BCA image modes", """
## BCA image modes

- `planning-visualization`: 3릴·3전선·건물·HUD의 기획 모순을 비교한다.
- `final-visual-candidate`: Demo·스토어·인게임 후보를 만든다.
- `visual-qa-and-approval`: 실제 화면 가독성·권리·오류·일관성·승인 상태를 판정한다.
""")

version_path = ROOT / "docs/BASE_RULES_VERSION.md"
version = version_path.read_text(encoding="utf-8")
for old in ("6a224e450f9420223c00921f3c56e051612f92ad", "7072b9e2742a60d7548fd39df3328ad76a8dbad1"):
    version = version.replace(old, BASE_SHA)
version = version.replace("`2026-07-25`", "`2026-07-29`")
if "## GDD Sheet 기준" not in version:
    version = version.rstrip() + f"\n\n## GDD Sheet 기준\n\n- GDD Sheet 의미 구조 기준: `{BASE_SHA}`\n- Workbook: `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`\n- UX/UI 전용 content commit은 `docs/UX_UI_SYSTEM.md`가 별도로 소유한다.\n"
version_path.write_text(version, encoding="utf-8")

append_once("docs/CURRENT_IMPLEMENTATION_STATUS.md", "C1 구현 검증 head:", f"""
## Legacy C1 원격 검증 증거

- `C1_ROULETTE_CORE_REMOTE_PROVEN`
- C1 구현 검증 head: `{C1_HEAD}`
- C1 최종 검증 run: `{C1_RUN}`
- 이 증거는 legacy C1 보존 seam의 원격 검증이며 V2 구현 완료를 뜻하지 않는다.
""")
append_once("docs/OMENWARD_ROADMAP.md", "C1 승인 룰렛 핵심 계약 원격 검증·병합 완료", """
## Legacy C1 증거 기준선

- C1 승인 룰렛 핵심 계약 원격 검증·병합 완료
- 판정: **REMOTE_PROVEN**
- V2 물리 릴·SpinSnapshot·SpinSession 구현은 별도 승인 패키지로 남는다.
""")
append_once("docs/design/APPROVED_ROULETTE_CORE_RULES.md", "C1 중앙 판정·완성선·등급·보상·보관 REMOTE_PROVEN", """
## Legacy C1 보존 증거

- C1 중앙 판정·완성선·등급·보상·보관 REMOTE_PROVEN
- 검증된 legacy resolver는 V2 migration에서 보존 seam으로만 사용한다.
""")

validator_path = ROOT / "tools/validate_c1_roulette.py"
validator = validator_path.read_text(encoding="utf-8")
old = '    if "문서 버전: **v0.23**" not in gdd:\n        errors.append("GDD was not advanced to v0.23")'
new = '    version_match = re.search(r"문서 버전:\\s*\\*\\*v(\\d+)\\.(\\d+)", gdd)\n    if version_match is None or tuple(map(int, version_match.groups())) < (0, 23):\n        errors.append("GDD was not advanced to v0.23 or later")'
if old in validator:
    validator = validator.replace(old, new)
validator_path.write_text(validator, encoding="utf-8")

test = f'''from __future__ import annotations
import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BASE_SHA="{BASE_SHA}"
SHEET_ID="{SHEET_ID}"
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
  self.assertIn("C1 구현 검증 head: `{C1_HEAD}`",status)
  self.assertIn("C1 최종 검증 run: `{C1_RUN}`",status)
  self.assertIn("V2 구현 완료를 뜻하지 않는다",status)
if __name__=="__main__": unittest.main()
'''
(ROOT / "tests/python/test_bca_visual_sheet_adoption.py").write_text(test, encoding="utf-8")

workflow = '''name: Validate Omenward GDD Sheet Adoption
on:
  pull_request:
    branches: [main]
    paths: ["README.md","AGENTS.md","docs/**","skills/**","tools/validate_c1_roulette.py","tests/python/test_bca_visual_sheet_adoption.py",".github/workflows/validate-bca-visual-sheet-adoption.yml"]
permissions: {contents: read}
concurrency:
  group: omenward-gdd-sheet-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true
jobs:
  contract:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: {fetch-depth: 0}
      - uses: actions/setup-python@v5
        with: {python-version: "3.12"}
      - run: python tests/python/test_bca_visual_sheet_adoption.py
      - run: python tools/validate_c1_roulette.py
      - run: git diff --check origin/main...HEAD
'''
(ROOT / ".github/workflows/validate-bca-visual-sheet-adoption.yml").write_text(workflow, encoding="utf-8")
