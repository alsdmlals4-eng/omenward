from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE_SHA="7072b9e2742a60d7548fd39df3328ad76a8dbad1"
TABS=["00_프로젝트_허브","01_작업순서","02_현재_확정결정","03_근거_라이브러리","04_누락_충돌_감사","10_제품방향","11_세계관","12_핵심루프","13_주요인물","14_조연_세력_관계","20_코어경험_데모목표","30_데모범위_품질기준_제작기반","40_핵심시스템_메인콘텐츠","41_성장_경제","50_메인콘텐츠","60_UX_UI_접근성","70_아트_오디오_에셋","71_이미지기획_생성목록","72_이미지검수_승인로그","80_데모_버티컬슬라이스_플레이테스트","90_본제작_출시_사업","98_Base_반영후보","99_변경이력"]
def write(path,content):
 p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content.rstrip()+"\n",encoding="utf-8")
def append(path,marker,content):
 p=ROOT/path;t=p.read_text(encoding="utf-8")
 if marker not in t:p.write_text(t.rstrip()+"\n\n"+content.strip()+"\n",encoding="utf-8")
def main():
 tabs="\n".join(f"- `{x}`" for x in TABS)
 write("docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md",f"""# Omenward 프로젝트 Google Sheets Workbook

```yaml
sheet_status: NOT_CONFIGURED
base_commit: {BASE_SHA}
```

정확한 Sheet URL·권한을 확인하지 못했으므로 새 Sheet를 만들지 않는다. 연결 시 기존 값·수식·사용자 편집을 보존하고 다음 tab을 설치·병합한다.

{tabs}

| 의미 구조 | 책임 원본 |
|---|---|
| 세계관·인물·세력 | V2 core spec과 등록된 디자인 문서 |
| 핵심루프 | 3원형 릴 선택·예측·확정 → 3전선 자동전투 → 보상·건설·재편 |
| 핵심시스템·메인콘텐츠 | 릴, Front, 유닛·건물 토큰, 예측/확정, 전선 결과, 캠페인 진행 |
| 이미지 계획·검수 | `docs/GPT_IMAGE_GENERATION_AND_REVIEW_WORKFLOW.md` |
""")
 write("docs/GPT_IMAGE_GENERATION_AND_REVIEW_WORKFLOW.md",f"""# Omenward GPT 이미지 생성·검수 워크플로

- Base: `alsdmlals4-eng/Base@{BASE_SHA}`
- Sheet: `NOT_CONFIGURED`
- Mode: `planning-visualization`, `final-visual-candidate`, `visual-qa-and-approval`

## 기획 중
1. 3개 원형 릴과 각 릴 결과·확률·예측 정보 구조.
2. 3개 전선의 위협·보상·유닛 상태·건물 토큰 원천 가독성.
3. 예측 → 선택 → 확정 → 자동전투 → 보상·건설 루프 목업.
4. 유닛·건물·위협·보상의 색·형태·아이콘 언어.
5. 1920×1080·1280×720 실제 HUD 비교.

## 기획 종료
1. Demo 키아트·Steam 캡슐·스크린샷 후보.
2. 릴/전선 HUD 고도화 목업.
3. 유닛·건물·상징·전장 환경 시트.
4. 캠페인 진행·보상·건설 선택 설명 이미지.

상태는 `PLANNED → GENERATED_EXPLORATION → IN_REVIEW → REVISION_REQUIRED/REJECTED/APPROVED_CANDIDATE → PROJECT_ASSET_APPROVED → APPLIED_AND_RUNTIME_VERIFIED`다. 전선 정보가 가려지거나 릴 결과·위협·보상·유닛 상태가 혼동되면 실패다. 특정 IP 유사성·원출처·라이선스·실제 Godot 적용을 검수한다. 생성 이미지는 자동 최종 자산이 아니다.
""")
 write("docs/BCA_VISUAL_SHEET_ADOPTION_AUDIT.md",f"""# Omenward BCA v8 적용 적대적 검토

```yaml
base_commit: {BASE_SHA}
sheet_status: NOT_CONFIGURED
product_paths_changed: false
final_status: CONFLICT_FIXED
```

- `MUST_FIX`: Base 2026-07-23 고정과 BCA adapter 부재 → v8로 갱신.
- `MUST_FIX`: art Skill에 기획 목업·최종 후보·승인 검수 mode 부재 → 통합.
- `SHOULD_FIX`: AGENTS의 과거 Core PoC 표현은 역사 범위로 명시.
- `BLOCKED_UNVERIFIED`: 실제 Sheet·생성 이미지·Godot 렌더·플레이테스트.
""")
 append("README.md","## BCA v8 기획·이미지·Sheet 운영",f"""## BCA v8 기획·이미지·Sheet 운영

- Base: `alsdmlals4-eng/Base@{BASE_SHA}`
- 통합 실행문: `VERTICAL_SLICE_INTEGRATED_EXECUTION_PROMPT_v8.md`
- Sheet: `NOT_CONFIGURED`; `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`
- 이미지 workflow: `docs/GPT_IMAGE_GENERATION_AND_REVIEW_WORKFLOW.md`
- 적대적 검토: `docs/BCA_VISUAL_SHEET_ADOPTION_AUDIT.md`
""")
 append("AGENTS.md","## BCA Sheet·GPT 이미지 생성·검수",f"""## BCA Sheet·GPT 이미지 생성·검수

- Base 기준은 `alsdmlals4-eng/Base@{BASE_SHA}`와 v8 통합 실행문이다.
- Sheet는 `NOT_CONFIGURED`; URL 확인 전 신규 Sheet를 추정 생성하지 않는다.
- GPT는 기획 중 릴·전선·토큰·HUD 목업과 기획 종료 Demo·상점 후보를 생성할 수 있다.
- 생성 결과는 자동 최종 자산이 아니며 실제 Godot 화면·구현·권리·오류·승인 원장 검수 뒤 사용한다.
- 과거 Core PoC 표현은 역사·호환 근거이며 현행 제품 Gate는 `DEMO_FIRST_VERTICAL_SLICE`다.
- 각 단계 뒤 `repository-wide-audit`를 실행한다.
""")
 p=ROOT/"docs/BASE_RULES_VERSION.md";t=p.read_text(encoding="utf-8").replace("41a20584dd2ee51d917e5c9d7cab6838e1ceba7e",BASE_SHA).replace("2026-07-23","2026-07-28")
 if "BCA v8" not in t:t=t.rstrip()+"\n\n## BCA v8\n\n- 활성 Prompt: `templates/prompts/VERTICAL_SLICE_INTEGRATED_EXECUTION_PROMPT_v8.md`.\n- Sheet: `NOT_CONFIGURED`.\n- 이미지 workflow: `docs/GPT_IMAGE_GENERATION_AND_REVIEW_WORKFLOW.md`.\n"
 p.write_text(t,encoding="utf-8")
 reg=ROOT/"docs/base/SKILL_REGISTRY.json";data=json.loads(reg.read_text(encoding="utf-8"));data["base_source"]["commit"]=BASE_SHA;data["base_source"]["synced_on"]="2026-07-28";data["base_source"]["integrated_execution_prompt"]="templates/prompts/VERTICAL_SLICE_INTEGRATED_EXECUTION_PROMPT_v8.md";data["bca_visual_sheet"]={"status":"ADOPTED","sheet_status":"NOT_CONFIGURED","required_tabs":TABS,"image_modes":["planning-visualization","final-visual-candidate","visual-qa-and-approval"],"adversarial_mode":"repository-wide-audit"}
 by={x["id"]:x for x in data["skills"]}
 for tag in ("세계관","핵심루프","주요인물","조연","핵심시스템","메인콘텐츠"): 
  if tag not in by["discipline.omenward-core-design"]["triggers"]:by["discipline.omenward-core-design"]["triggers"].append(tag)
 for tag in ("planning-visualization","final-visual-candidate","image-mockup","image-approval"):
  if tag not in by["discipline.omenward-art-assets"]["triggers"]:by["discipline.omenward-art-assets"]["triggers"].append(tag)
 for tag in ("visual-qa-and-approval","sheet-structure","stale-prompt","repository-wide-audit"):
  if tag not in by["foundation.validation-review"]["triggers"]:by["foundation.validation-review"]["triggers"].append(tag)
 reg.write_text(json.dumps(data,ensure_ascii=False,separators=(",",":")),encoding="utf-8")
 art=ROOT/"skills/disciplines/governing-omenward-art-animation-and-assets/SKILL.md";t=art.read_text(encoding="utf-8")
 if "## Skill Modes" not in t:t=t.replace("## 사용 조건","## Skill Modes\n\n- `asset-contract`: 에셋 규격·임포트·판정·연출 계약.\n- `planning-visualization`: 릴·전선·토큰·HUD 기획 목업.\n- `final-visual-candidate`: Demo·상점·키아트·UI·유닛 후보.\n- `visual-qa-and-approval`: 실제 화면·구현·권리·오류·승인 검수.\n\n## 사용 조건",1)
 if "자동 최종 자산" not in t:t=t.rstrip()+"\n\n생성 이미지·목업은 자동 최종 자산이 아니다. `APPROVED_CANDIDATE`와 `PROJECT_ASSET_APPROVED`를 분리하고 실제 전장 가독성과 Godot 적용을 검수한다.\n"
 art.write_text(t,encoding="utf-8")
 write("tests/python/test_bca_visual_sheet_adoption.py",f'''from __future__ import annotations
import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];BASE_SHA="{BASE_SHA}"
class TestBCA(unittest.TestCase):
 def test_pin(self):
  for p in ("README.md","AGENTS.md","docs/BASE_RULES_VERSION.md"):self.assertIn(BASE_SHA,(ROOT/p).read_text(encoding="utf-8"),p)
 def test_contracts(self):
  s=(ROOT/"docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md").read_text(encoding="utf-8");v=(ROOT/"docs/GPT_IMAGE_GENERATION_AND_REVIEW_WORKFLOW.md").read_text(encoding="utf-8")
  for x in ("11_세계관","12_핵심루프","13_주요인물","40_핵심시스템_메인콘텐츠","71_이미지기획_생성목록","72_이미지검수_승인로그","NOT_CONFIGURED"):self.assertIn(x,s)
  for x in ("planning-visualization","final-visual-candidate","visual-qa-and-approval","PROJECT_ASSET_APPROVED","자동 최종 자산"):self.assertIn(x,v)
 def test_registry(self):
  r=json.loads((ROOT/"docs/base/SKILL_REGISTRY.json").read_text(encoding="utf-8"));self.assertEqual(r["base_source"]["commit"],BASE_SHA);self.assertEqual(r["bca_visual_sheet"]["status"],"ADOPTED")
if __name__=="__main__":unittest.main()
''')
 write(".github/workflows/validate-bca-visual-sheet-adoption.yml",'''name: Validate Omenward BCA Adoption
on:
  pull_request:
    branches: [main]
    paths: ["README.md","AGENTS.md","docs/**","skills/**","tests/python/test_bca_visual_sheet_adoption.py",".github/workflows/validate-bca-visual-sheet-adoption.yml"]
permissions: {contents: read}
concurrency:
  group: omenward-bca-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true
jobs:
  contract:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: {python-version: "3.12"}
      - run: python -m unittest tests.python.test_bca_visual_sheet_adoption -v
      - run: git diff --check origin/main...HEAD
''')
if __name__=="__main__":main()
