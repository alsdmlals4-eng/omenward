from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROOF_HEAD = "1976c5355124b2ce7d7ef77b8835df0c95710038"
PROOF_RUN = "29965348284"
FINAL_WORKFLOW = ".github/workflows/validate-omenward-core.yml"


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def write(relative: str, text: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def transition(relative: str, old: str, new: str) -> None:
    text = read(relative)
    if new in text:
        return
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{relative}: expected one old or existing new value; old count={count}: {old[:120]!r}")
    write(relative, text.replace(old, new, 1))


def replace_all(relative: str, old: str, new: str, minimum: int = 1) -> None:
    text = read(relative)
    if old not in text:
        if new in text:
            return
        raise RuntimeError(f"{relative}: neither old nor new value found: {old!r}")
    if text.count(old) < minimum:
        raise RuntimeError(f"{relative}: replacement count below minimum for {old!r}")
    write(relative, text.replace(old, new))


# README
transition(
    "README.md",
    "> 현재 상태: **C1 룰렛 REMOTE_PROVEN / C2 전투 목적 루프 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기 / 사람 플레이 미완결**",
    "> 현재 상태: **C1 룰렛 REMOTE_PROVEN / C2 전투 목적 루프 REMOTE_PROVEN / C3 코어 UX AUTOMATED_CONTRACTS_PROVEN / 사람 플레이 미완결**",
)
transition(
    "README.md",
    "→ C3 승인 코어 UX 6종 구현 완료·원격 통합 검증 대기\n→ [다음 실행] 10~15분 사람 플레이와 1080p·720p 가독성 검증",
    "→ C3 승인 코어 UX 6종 자동 계약 검증 완료\n→ [다음 실행] 10~15분 사람 플레이와 1080p·720p 가독성 검증",
)
transition(
    "README.md",
    "C3는 확률 미리보기·토큰 장부·단계형 징조·전술 오버레이·웨이브 원인 보고·건설 비교를 실제 도메인 snapshot과 HUD에 연결했으며 최신 원격 통합 검증을 기다린다. 현재 판정은 `C1_ROULETTE_CORE_REMOTE_PROVEN`, `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`, `C3_IMPLEMENTED`, `CORE_VERTICAL_SLICE_PARTIAL`, `CORE_LOOP_NOT_PROVEN`, `HUMAN_QA_NOT_RUN`이다.",
    f"C3는 확률 미리보기·토큰 장부·단계형 징조·전술 오버레이·웨이브 원인 보고·건설 비교를 실제 도메인 snapshot과 HUD에 연결했고 자동 계약 원격 검증을 완료했다 (head `{PROOF_HEAD}`, run `{PROOF_RUN}`). 현재 판정은 `C1_ROULETTE_CORE_REMOTE_PROVEN`, `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`, `C3_AUTOMATED_CONTRACTS_PROVEN`, `CORE_VERTICAL_SLICE_PARTIAL`, `CORE_LOOP_NOT_PROVEN`, `HUMAN_QA_NOT_RUN`이다.",
)

# Current implementation status
transition(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "- C3 작업 브랜치: `agent/c3-core-ux-minimum`\n- C3 상태: `C3_IMPLEMENTED / REMOTE_VALIDATION_PENDING / HUMAN_QA_PENDING`",
    f"- C3 자동 계약 검증 head: `{PROOF_HEAD}`\n- C3 자동 계약 검증 run: `{PROOF_RUN}` (`Validate Core Contracts`)\n- C3 통합 PR: `#51` — 병합 결과는 GitHub PR 상태가 원본\n- C3 상태: `C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING`",
)
transition("docs/CURRENT_IMPLEMENTATION_STATUS.md", "  - `C3_IMPLEMENTED`", "  - `C3_AUTOMATED_CONTRACTS_PROVEN`")
transition(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "| 테스트 | C1·C2 원격 검증, C3 정상·경계·결정론 headless 및 Python mutation 계약 | `C3_REMOTE_VALIDATION_PENDING` |",
    "| 테스트 | C1·C2·C3 Godot 4.7.1, 4환경 Python·문서·Skill·mutation 계약 | `REMOTE_PROVEN` |",
)
transition(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "## 5. C3 코어 UX 6종 — 구현 완료, 최신 원격 검증 대기",
    "## 5. C3 코어 UX 6종 — 자동 계약 검증 완료, 사람 QA 대기",
)
transition(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "현재 판정: `C3_IMPLEMENTED / REMOTE_VALIDATION_PENDING / HUMAN_QA_PENDING`.",
    f"현재 판정: `C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING` — head `{PROOF_HEAD}`, run `{PROOF_RUN}`에서 4환경 계약과 Godot 전체 회귀가 통과했다.",
)
transition(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "1. C3 최신 영구 Core Contracts 원격 검증과 PR #51 병합\n2. 10~15분 사람 플레이·1080p·720p 가독성 QA\n3. C1U 이동권·럭키·상위 템플릿 사용자 결정 게이트",
    "1. 10~15분 사람 플레이·1080p·720p 가독성 QA\n2. C1U 이동권·럭키·상위 템플릿 사용자 결정 게이트\n3. 밸런스 안정화",
)
transition(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "4. 밸런스 안정화\n5. 콘텐츠·아트 확장",
    "4. 콘텐츠·아트 확장\n5. 캠페인·데모 통합",
)
transition(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "C3 자동 검증과 사람 플레이 완료 전에는 전체 코어 루프를 `PROVEN`으로 부르지 않는다.",
    "사람 플레이 완료 전에는 전체 코어 루프를 `PROVEN`으로 부르지 않는다.",
)

# C3 audit
transition(
    "docs/C3_CORE_UX_AUDIT_2026-07-23.md",
    "- 현재 상태: `C3_IMPLEMENTED / REMOTE_VALIDATION_PENDING / HUMAN_QA_PENDING`",
    f"- 현재 상태: `C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING`\n- 자동 검증 head: `{PROOF_HEAD}`\n- 자동 검증 run: `{PROOF_RUN}` (`Validate Core Contracts`, 5 jobs success)",
)
transition(
    "docs/C3_CORE_UX_AUDIT_2026-07-23.md",
    "- 최신 영구 `Validate Core Contracts`에서 Godot 4.7.1 editor import, 모든 headless, runtime smoke를 통과해야 한다.\n- Ubuntu/Windows × Python 3.12/3.13에서 C1·C2·C3 계약, mutation tests, 프로젝트 코어·Skill·whitespace를 통과해야 한다.\n- 원격 자동 검증 완료 뒤 상태는 `C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING`으로 승격한다.",
    f"- head `{PROOF_HEAD}`, run `{PROOF_RUN}`에서 Godot 4.7.1 editor import, 모든 headless, runtime smoke가 통과했다.\n- 같은 run에서 Ubuntu/Windows × Python 3.12/3.13의 C1·C2·C3 계약, mutation tests, 프로젝트 코어·Skill·whitespace가 모두 통과했다.\n- 따라서 상태를 `C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING`으로 승격한다.",
)

# Active context
transition(
    "docs/ACTIVE_CONTEXT.md",
    "- 저장소 상태: **C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기 / 사람 플레이 미검증**",
    "- 저장소 상태: **C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX AUTOMATED_CONTRACTS_PROVEN / 사람 플레이 미검증**",
)
transition("docs/ACTIVE_CONTEXT.md", "+ C3_IMPLEMENTED", "+ C3_AUTOMATED_CONTRACTS_PROVEN")
transition(
    "docs/ACTIVE_CONTEXT.md",
    "C3 코어 UX 6종은 실제 snapshot과 HUD에 구현됐고 최신 영구 CI 검증을 기다리며, 사람 플레이는 아직 완료되지 않았다.",
    f"C3 코어 UX 6종은 실제 snapshot과 HUD에 구현됐고 head `{PROOF_HEAD}`, run `{PROOF_RUN}`에서 자동 계약 원격 검증을 완료했으며, 사람 플레이는 아직 완료되지 않았다.",
)
transition(
    "docs/ACTIVE_CONTEXT.md",
    "→ C3 승인 코어 UX 6종 구현 완료·원격 통합 검증 대기",
    "→ C3 승인 코어 UX 6종 자동 계약 검증 완료",
)
transition(
    "docs/ACTIVE_CONTEXT.md",
    "- PR #49와 PR #50은 main에 병합됐다. PR #51은 C3 코어 UX 6종의 구현·문서·검증을 통합하는 현재 작업이다.",
    "- PR #49와 PR #50은 main에 병합됐다. PR #51은 C3 코어 UX 6종의 구현·문서·자동 계약 증거를 통합한 변경 집합이며 병합 결과는 GitHub PR 상태를 따른다.",
)

# Handoff
transition(
    "docs/HANDOFF_CONTEXT.md",
    "- 현재 상태: **CORE_LOCKED / C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기 / C1U·사람 플레이 미검증**",
    "- 현재 상태: **CORE_LOCKED / C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3_AUTOMATED_CONTRACTS_PROVEN / C1U·사람 플레이 미검증**",
)
transition(
    "docs/HANDOFF_CONTEXT.md",
    "C3 최신 원격 통합 검증, C1U 유틸리티 결정과 사람 플레이가 남아 있다.",
    "C3 자동 계약 검증은 완료됐고 C1U 유틸리티 결정과 사람 플레이가 남아 있다.",
)
transition("docs/HANDOFF_CONTEXT.md", "+ C3_IMPLEMENTED", "+ C3_AUTOMATED_CONTRACTS_PROVEN")
transition(
    "docs/HANDOFF_CONTEXT.md",
    "C3 승인 UX 6종은 실제 도메인 snapshot과 HUD에 구현됐고 최신 영구 CI 검증을 기다린다.",
    f"C3 승인 UX 6종은 실제 도메인 snapshot과 HUD에 구현됐고 head `{PROOF_HEAD}`, run `{PROOF_RUN}`에서 자동 계약 검증을 완료했다.",
)
transition(
    "docs/HANDOFF_CONTEXT.md",
    "다음 순서는 C3 원격 통합 검증과 PR #51 병합, 10~15분 사람 플레이·1080p·720p 가독성 검증, C1U 사용자 결정 게이트다.",
    "다음 순서는 10~15분 사람 플레이·1080p·720p 가독성 검증, C1U 사용자 결정 게이트다. PR #51 병합 결과는 GitHub PR 상태가 원본이다.",
)

# GDD
transition(
    "docs/OMENWARD_GAME_DESIGN.md",
    "- 상태: **프리프로덕션 계약 승인 / C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기 / 사람 플레이 미검증**",
    "- 상태: **프리프로덕션 계약 승인 / C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3_AUTOMATED_CONTRACTS_PROVEN / 사람 플레이 미검증**",
)
transition("docs/OMENWARD_GAME_DESIGN.md", "+ C3_IMPLEMENTED", "+ C3_AUTOMATED_CONTRACTS_PROVEN")
transition(
    "docs/OMENWARD_GAME_DESIGN.md",
    "- C3는 건설 전 확률 미리보기, 토큰 장부, T-30/T-15/T-5 징조, 상성·사거리·현재 타기팅, 라인별 원인 보고, 건설 비교를 실제 도메인 snapshot과 HUD에 연결했다.",
    f"- C3는 건설 전 확률 미리보기, 토큰 장부, T-30/T-15/T-5 징조, 상성·사거리·현재 타기팅, 라인별 원인 보고, 건설 비교를 실제 도메인 snapshot과 HUD에 연결했고 head `{PROOF_HEAD}`, run `{PROOF_RUN}`에서 자동 계약 검증을 완료했다.",
)
transition(
    "docs/OMENWARD_GAME_DESIGN.md",
    "- C3 최신 영구 CI 증거와 PR #51 병합.\n- 이동권 완성선 보상량과 럭키 규칙 통합.",
    "- 이동권 완성선 보상량과 럭키 규칙 통합.",
)
transition(
    "docs/OMENWARD_GAME_DESIGN.md",
    "→ C3 코어 UX 6종 IMPLEMENTED·원격 검증 대기\n→ C4 10~15분 사람 플레이·1080p·720p 가독성 QA",
    "→ C3 코어 UX 6종 AUTOMATED_CONTRACTS_PROVEN\n→ C4 10~15분 사람 플레이·1080p·720p 가독성 QA",
)

# Roadmap
transition(
    "docs/OMENWARD_ROADMAP.md",
    "- 현재 상태: **C0·C1·C2 REMOTE_PROVEN / C3 IMPLEMENTED·원격 검증 대기 / C1U 사용자 결정 대기 / 사람 QA 다음**",
    "- 현재 상태: **C0·C1·C2 REMOTE_PROVEN / C3 AUTOMATED_CONTRACTS_PROVEN / C1U 사용자 결정 대기 / 사람 QA 현재**",
)
transition(
    "docs/OMENWARD_ROADMAP.md",
    "→ C3 승인 코어 UX 6종 구현 완료·원격 통합 검증 대기",
    "→ C3 승인 코어 UX 6종 자동 계약 검증 완료",
)
transition(
    "docs/OMENWARD_ROADMAP.md",
    "| C3 코어 UX | 승인 UX 6종을 실제 데이터와 연결 | **IMPLEMENTED / REMOTE_VALIDATION_PENDING** | 영구 CI·사람 가독성 기준 |",
    "| C3 코어 UX | 승인 UX 6종을 실제 데이터와 연결 | **AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING** | 사람 가독성 기준 |",
)
transition(
    "docs/OMENWARD_ROADMAP.md",
    "C3 승인 코어 UX 6종 최신 영구 CI 검증과 PR #51 병합\n→ 10~15분 사람 플레이·1080p·720p 가독성 QA",
    "10~15분 사람 플레이·1080p·720p 가독성 QA",
)
transition(
    "docs/OMENWARD_ROADMAP.md",
    "C3는 PR #51에서 실제 snapshot·HUD·정상/경계/결정론 회귀를 구현했으며 최신 영구 CI 검증을 기다린다.",
    f"C3는 실제 snapshot·HUD·정상/경계/결정론·비변경 회귀를 구현했고 head `{PROOF_HEAD}`, run `{PROOF_RUN}`에서 자동 계약 검증을 완료했다. PR #51 병합 결과는 GitHub PR 상태가 원본이다.",
)

# Decisions
transition(
    "docs/DECISIONS_PENDING.md",
    "- 현재 작업: PR #51 C3 코어 UX 원격 검증·병합 / 다음 사용자 결정: C1U 이동권·럭키·분포",
    "- 현재 작업: C3 자동 계약 검증 완료·사람 QA 준비 / 다음 사용자 결정: C1U 이동권·럭키·분포",
)
transition(
    "docs/DECISIONS_PENDING.md",
    "- [ ] 최신 영구 `Validate Core Contracts` 원격 증거 기록과 PR #51 병합.",
    f"- [x] C3 자동 계약 원격 검증 — head `{PROOF_HEAD}`, run `{PROOF_RUN}`, 5 jobs success.\n- PR #51 병합 결과는 GitHub PR 상태가 원본이다.",
)
transition(
    "docs/DECISIONS_PENDING.md",
    "- [x] C3 코어 UX 6종 구현과 정상·경계·결정론 계약 추가. 최신 영구 원격 run은 병합 전 기록.",
    f"- [x] C3 코어 UX 6종·정상·경계·결정론·비변경 계약 원격 검증 — head `{PROOF_HEAD}`, run `{PROOF_RUN}`.",
)
transition(
    "docs/DECISIONS_PENDING.md",
    "| headless 테스트 | Godot 4.7.1 전체 suite 원격 통과 (C1 `29926598807`, 통합 C1·C2 `29938742864`); C3 최신 통합 run 대기 |",
    f"| headless 테스트 | Godot 4.7.1 전체 suite 원격 통과 (C1 `29926598807`, C1·C2 `29938742864`, C3 `{PROOF_RUN}`) |",
)
transition(
    "docs/DECISIONS_PENDING.md",
    "1. C3 최신 영구 Core Contracts 원격 검증과 PR #51 병합\n2. 10~15분 사람 플레이와 1080p·720p QA\n3. C1U 이동권·럭키 정본 통합과 100,000시드 사용자 결정",
    "1. 10~15분 사람 플레이와 1080p·720p QA\n2. C1U 이동권·럭키 정본 통합과 100,000시드 사용자 결정\n3. 밸런스 안정화",
)
transition(
    "docs/DECISIONS_PENDING.md",
    "4. 밸런스 안정화\n5. 콘텐츠·아트 확장",
    "4. 콘텐츠·아트 확장\n5. 캠페인·데모 통합",
)

# Godot structure and validation evidence
transition(
    "docs/GODOT_PROJECT_STRUCTURE.md",
    "- 상태: **기술 기준선·C1 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기**",
    "- 상태: **기술 기준선·C1 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX AUTOMATED_CONTRACTS_PROVEN**",
)
transition(
    "docs/GODOT_PROJECT_STRUCTURE.md",
    "현재 UI는 자동 계약을 위한 텍스트 중심 PoC다.",
    f"현재 UI는 자동 계약을 위한 텍스트 중심 PoC이며 head `{PROOF_HEAD}`, run `{PROOF_RUN}`에서 전체 계약을 통과했다.",
)
transition(
    "docs/VERTICAL_SLICE_VALIDATION.md",
    "# Vertical Slice Validation\n",
    f"# Vertical Slice Validation\n\n## C3 automated evidence\n\n- 검증 head: `{PROOF_HEAD}`\n- `Validate Core Contracts` run: `{PROOF_RUN}`\n- 결과: Ubuntu/Windows × Python 3.12/3.13 네 계약 작업과 Godot 4.7.1 작업, 총 5 jobs success.\n- 범위: C1·C2·C3·프로젝트 코어·Skill·전체 mutation·whitespace, editor import·모든 headless·runtime smoke.\n- 사람 플레이·1080p·720p 가독성은 아직 실행하지 않았다.\n",
)

# Finalize the permanent C3 validator and mutation tests.
validator = "tools/validate_c3_core_ux.py"
replace_all(validator, ".github/workflows/validate-core-contracts.yml", FINAL_WORKFLOW)
transition(
    validator,
    '    "tools/sync_c3_canonical_docs.py",\n)',
    '    "tools/sync_c3_canonical_docs.py",\n    ".github/workflows/core-contracts.yml",\n    ".github/workflows/validate-core-contracts.yml",\n    ".github/workflows/finalize-c3-proof.yml",\n    "tools/finalize_c3_proof.py",\n)',
)
transition(
    validator,
    '    "현재 C3 시작점은",\n)',
    '    "현재 C3 시작점은",\n    "C3 코어 UX IMPLEMENTED·원격 검증 대기",\n    "C3 IMPLEMENTED·원격 검증 대기",\n    "REMOTE_VALIDATION_PENDING",\n    "C3 승인 코어 UX 6종 최신 영구 CI 검증과 PR #51 병합",\n)',
)
transition(
    validator,
    '            "C3_IMPLEMENTED",\n            "REMOTE_VALIDATION_PENDING",\n            "HUMAN_QA_PENDING",',
    f'            "C3_AUTOMATED_CONTRACTS_PROVEN",\n            "HUMAN_QA_PENDING",\n            "{PROOF_RUN}",',
)
replace_all(validator, "C3 코어 UX IMPLEMENTED·원격 검증 대기", "C3 코어 UX AUTOMATED_CONTRACTS_PROVEN")
replace_all(validator, "C3_IMPLEMENTED / REMOTE_VALIDATION_PENDING / HUMAN_QA_PENDING", "C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING")
replace_all(validator, '            "C3_IMPLEMENTED",', '            "C3_AUTOMATED_CONTRACTS_PROVEN",')
replace_all(validator, "C3 IMPLEMENTED·원격 검증 대기", "C3 AUTOMATED_CONTRACTS_PROVEN")
replace_all(validator, "IMPLEMENTED / REMOTE_VALIDATION_PENDING", "AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING")
replace_all(validator, '            "C3 승인 코어 UX 6종 최신 영구 CI 검증과 PR #51 병합",', '            "10~15분 사람 플레이·1080p·720p 가독성 QA",')

mutation = "tests/python/test_c3_core_ux_contract.py"
replace_all(mutation, ".github/workflows/validate-core-contracts.yml", FINAL_WORKFLOW)
replace_all(mutation, ".github/workflows/core-contracts.yml", FINAL_WORKFLOW, minimum=0)
replace_all(mutation, "C3_IMPLEMENTED / REMOTE_VALIDATION_PENDING / HUMAN_QA_PENDING", "C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING")

# Create exactly one permanent workflow.
workflow = r'''name: Validate Omenward Core

on:
  pull_request:
    branches:
      - main
    paths:
      - "scripts/**"
      - "scenes/**"
      - "data/**"
      - "tests/**"
      - "docs/**"
      - "README.md"
      - "tools/validate_*.py"
      - ".github/workflows/validate-omenward-core.yml"
  workflow_dispatch:

permissions:
  contents: read

jobs:
  contracts:
    timeout-minutes: 15
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest]
        python-version: ["3.12", "3.13"]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - name: Compile Python contracts
        run: python -m py_compile tools/validate_c1_roulette.py tools/validate_c2_battle_objective.py tools/validate_c3_core_ux.py tools/validate_project_core_docs.py tests/python/test_c1_roulette_contract.py tests/python/test_c2_battle_objective_contract.py tests/python/test_c3_core_ux_contract.py
      - name: Validate C1 roulette contract
        run: python tools/validate_c1_roulette.py
      - name: Validate C2 battle objective contract
        run: python tools/validate_c2_battle_objective.py
      - name: Validate C3 core UX contract
        run: python tools/validate_c3_core_ux.py
      - name: Run all Python repository tests
        run: python -m unittest discover -s tests/python -v
      - name: Validate project core documents
        run: python tools/validate_project_core_docs.py
      - name: Validate Skill system when present
        shell: bash
        run: |
          if [ -f tools/validate_skill_system.py ]; then python tools/validate_skill_system.py; fi
      - name: Check whitespace
        run: git diff --check

  godot:
    timeout-minutes: 20
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Reject temporary C3 artifacts
        shell: bash
        run: |
          set -euo pipefail
          test ! -e docs/_C3_HEADLESS_DIAGNOSTIC.log
          test ! -e tools/_repair_c3_stage_run_types.py
          test ! -e tools/sync_c3_canonical_docs.py
          test ! -e tools/finalize_c3_proof.py
          test ! -e .github/workflows/diagnose-c3-headless.yml
          test ! -e .github/workflows/sync-c3-canonical-docs.yml
          test ! -e .github/workflows/core-contracts.yml
          test ! -e .github/workflows/validate-core-contracts.yml
          test ! -e .github/workflows/finalize-c3-proof.yml
      - name: Install Godot 4.7.1 Standard
        shell: bash
        run: |
          curl -fL "https://github.com/godotengine/godot-builds/releases/download/4.7.1-stable/Godot_v4.7.1-stable_linux.x86_64.zip" -o godot.zip
          unzip -q godot.zip
          chmod +x Godot_v4.7.1-stable_linux.x86_64
          ./Godot_v4.7.1-stable_linux.x86_64 --version
      - name: Import project
        shell: bash
        run: timeout 120s ./Godot_v4.7.1-stable_linux.x86_64 --headless --path . --editor --quit
      - name: Run all headless contract tests
        shell: bash
        run: |
          set -euo pipefail
          for test_file in tests/headless/*_test.gd; do
            echo "Running ${test_file}"
            timeout 60s ./Godot_v4.7.1-stable_linux.x86_64 --headless --path . -s "res://${test_file}"
          done
      - name: Runtime smoke
        shell: bash
        run: timeout 60s ./Godot_v4.7.1-stable_linux.x86_64 --headless --path . --quit-after 1
'''
write(FINAL_WORKFLOW, workflow)

# Remove all temporary/obsolete C3 transition artifacts before validation.
for relative in (
    ".github/workflows/core-contracts.yml",
    ".github/workflows/validate-core-contracts.yml",
    ".github/workflows/finalize-c3-proof.yml",
    "tools/finalize_c3_proof.py",
):
    path = ROOT / relative
    if path.exists():
        path.unlink()

print("C3 proof transition completed")
