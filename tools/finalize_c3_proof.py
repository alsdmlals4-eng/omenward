from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROOF_HEAD = "1976c5355124b2ce7d7ef77b8835df0c95710038"
PROOF_RUN = "29965348284"
FINAL_WORKFLOW = ".github/workflows/validate-omenward-core.yml"


def replace_once(relative: str, old: str, new: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{relative}: expected one match, found {count}: {old[:100]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


def replace_required(relative: str, old: str, new: str, minimum: int = 1) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count < minimum:
        raise RuntimeError(f"{relative}: expected at least {minimum} matches, found {count}: {old!r}")
    path.write_text(text.replace(old, new), encoding="utf-8", newline="\n")


def regex_once(relative: str, pattern: str, replacement: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE | re.DOTALL)
    if count != 1:
        raise RuntimeError(f"{relative}: expected one regex match, found {count}: {pattern[:100]!r}")
    path.write_text(updated, encoding="utf-8", newline="\n")


# README
replace_once(
    "README.md",
    "> 현재 상태: **C1 룰렛 REMOTE_PROVEN / C2 전투 목적 루프 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기 / 사람 플레이 미완결**",
    "> 현재 상태: **C1 룰렛 REMOTE_PROVEN / C2 전투 목적 루프 REMOTE_PROVEN / C3 코어 UX AUTOMATED_CONTRACTS_PROVEN / 사람 플레이 미완결**",
)
replace_once(
    "README.md",
    "→ C3 승인 코어 UX 6종 구현 완료·원격 통합 검증 대기\n→ [다음 실행] 10~15분 사람 플레이와 1080p·720p 가독성 검증",
    "→ C3 승인 코어 UX 6종 자동 계약 검증 완료\n→ [다음 실행] 10~15분 사람 플레이와 1080p·720p 가독성 검증",
)
replace_once(
    "README.md",
    "C3는 확률 미리보기·토큰 장부·단계형 징조·전술 오버레이·웨이브 원인 보고·건설 비교를 실제 도메인 snapshot과 HUD에 연결했으며 최신 원격 통합 검증을 기다린다. 현재 판정은 `C1_ROULETTE_CORE_REMOTE_PROVEN`, `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`, `C3_IMPLEMENTED`, `CORE_VERTICAL_SLICE_PARTIAL`, `CORE_LOOP_NOT_PROVEN`, `HUMAN_QA_NOT_RUN`이다.",
    f"C3는 확률 미리보기·토큰 장부·단계형 징조·전술 오버레이·웨이브 원인 보고·건설 비교를 실제 도메인 snapshot과 HUD에 연결했고 자동 계약 원격 검증을 완료했다 (head `{PROOF_HEAD}`, run `{PROOF_RUN}`). 현재 판정은 `C1_ROULETTE_CORE_REMOTE_PROVEN`, `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`, `C3_AUTOMATED_CONTRACTS_PROVEN`, `CORE_VERTICAL_SLICE_PARTIAL`, `CORE_LOOP_NOT_PROVEN`, `HUMAN_QA_NOT_RUN`이다.",
)

# Current status
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "- C3 작업 브랜치: `agent/c3-core-ux-minimum`\n- C3 상태: `C3_IMPLEMENTED / REMOTE_VALIDATION_PENDING / HUMAN_QA_PENDING`",
    f"- C3 자동 계약 검증 head: `{PROOF_HEAD}`\n- C3 자동 계약 검증 run: `{PROOF_RUN}` (`Validate Core Contracts`)\n- C3 통합 PR: `#51` — 병합 결과는 GitHub PR 상태가 원본\n- C3 상태: `C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING`",
)
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "  - `C3_IMPLEMENTED`",
    "  - `C3_AUTOMATED_CONTRACTS_PROVEN`",
)
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "| 테스트 | C1·C2 원격 검증, C3 정상·경계·결정론 headless 및 Python mutation 계약 | `C3_REMOTE_VALIDATION_PENDING` |",
    "| 테스트 | C1·C2·C3 Godot 4.7.1, 4환경 Python·문서·Skill·mutation 계약 | `REMOTE_PROVEN` |",
)
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "## 5. C3 코어 UX 6종 — 구현 완료, 최신 원격 검증 대기",
    "## 5. C3 코어 UX 6종 — 자동 계약 검증 완료, 사람 QA 대기",
)
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "현재 판정: `C3_IMPLEMENTED / REMOTE_VALIDATION_PENDING / HUMAN_QA_PENDING`.",
    f"현재 판정: `C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING` — head `{PROOF_HEAD}`, run `{PROOF_RUN}`에서 4환경 계약과 Godot 전체 회귀가 통과했다.",
)
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "1. C3 최신 영구 Core Contracts 원격 검증과 PR #51 병합\n2. 10~15분 사람 플레이·1080p·720p 가독성 QA\n3. C1U 이동권·럭키·상위 템플릿 사용자 결정 게이트",
    "1. 10~15분 사람 플레이·1080p·720p 가독성 QA\n2. C1U 이동권·럭키·상위 템플릿 사용자 결정 게이트\n3. 밸런스 안정화",
)
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "4. 밸런스 안정화\n5. 콘텐츠·아트 확장",
    "4. 콘텐츠·아트 확장\n5. 캠페인·데모 통합",
)
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "C3 자동 검증과 사람 플레이 완료 전에는 전체 코어 루프를 `PROVEN`으로 부르지 않는다.",
    "사람 플레이 완료 전에는 전체 코어 루프를 `PROVEN`으로 부르지 않는다.",
)

# C3 audit
replace_once(
    "docs/C3_CORE_UX_AUDIT_2026-07-23.md",
    "- 현재 상태: `C3_IMPLEMENTED / REMOTE_VALIDATION_PENDING / HUMAN_QA_PENDING`",
    f"- 현재 상태: `C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING`\n- 자동 검증 head: `{PROOF_HEAD}`\n- 자동 검증 run: `{PROOF_RUN}` (`Validate Core Contracts`, 5 jobs success)",
)
replace_once(
    "docs/C3_CORE_UX_AUDIT_2026-07-23.md",
    "- 최신 영구 `Validate Core Contracts`에서 Godot 4.7.1 editor import, 모든 headless, runtime smoke를 통과해야 한다.\n- Ubuntu/Windows × Python 3.12/3.13에서 C1·C2·C3 계약, mutation tests, 프로젝트 코어·Skill·whitespace를 통과해야 한다.\n- 원격 자동 검증 완료 뒤 상태는 `C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING`으로 승격한다.",
    f"- head `{PROOF_HEAD}`, run `{PROOF_RUN}`에서 Godot 4.7.1 editor import, 모든 headless, runtime smoke가 통과했다.\n- 같은 run에서 Ubuntu/Windows × Python 3.12/3.13의 C1·C2·C3 계약, mutation tests, 프로젝트 코어·Skill·whitespace가 모두 통과했다.\n- 따라서 상태를 `C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING`으로 승격한다.",
)

# Active context
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "- 저장소 상태: **C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기 / 사람 플레이 미검증**",
    "- 저장소 상태: **C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX AUTOMATED_CONTRACTS_PROVEN / 사람 플레이 미검증**",
)
replace_once("docs/ACTIVE_CONTEXT.md", "+ C3_IMPLEMENTED", "+ C3_AUTOMATED_CONTRACTS_PROVEN")
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "C3 코어 UX 6종은 실제 snapshot과 HUD에 구현됐고 최신 영구 CI 검증을 기다리며, 사람 플레이는 아직 완료되지 않았다.",
    f"C3 코어 UX 6종은 실제 snapshot과 HUD에 구현됐고 head `{PROOF_HEAD}`, run `{PROOF_RUN}`에서 자동 계약 원격 검증을 완료했으며, 사람 플레이는 아직 완료되지 않았다.",
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "→ C3 승인 코어 UX 6종 구현 완료·원격 통합 검증 대기",
    "→ C3 승인 코어 UX 6종 자동 계약 검증 완료",
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "- PR #49와 PR #50은 main에 병합됐다. PR #51은 C3 코어 UX 6종의 구현·문서·검증을 통합하는 현재 작업이다.",
    "- PR #49와 PR #50은 main에 병합됐다. PR #51은 C3 코어 UX 6종의 구현·문서·자동 계약 증거를 통합한 변경 집합이며 병합 결과는 GitHub PR 상태를 따른다.",
)

# Handoff
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "- 현재 상태: **CORE_LOCKED / C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기 / C1U·사람 플레이 미검증**",
    "- 현재 상태: **CORE_LOCKED / C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3_AUTOMATED_CONTRACTS_PROVEN / C1U·사람 플레이 미검증**",
)
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "C3 최신 원격 통합 검증, C1U 유틸리티 결정과 사람 플레이가 남아 있다.",
    "C3 자동 계약 검증은 완료됐고 C1U 유틸리티 결정과 사람 플레이가 남아 있다.",
)
replace_once("docs/HANDOFF_CONTEXT.md", "+ C3_IMPLEMENTED", "+ C3_AUTOMATED_CONTRACTS_PROVEN")
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "C3 승인 UX 6종은 실제 도메인 snapshot과 HUD에 구현됐고 최신 영구 CI 검증을 기다린다.",
    f"C3 승인 UX 6종은 실제 도메인 snapshot과 HUD에 구현됐고 head `{PROOF_HEAD}`, run `{PROOF_RUN}`에서 자동 계약 검증을 완료했다.",
)
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "다음 순서는 C3 원격 통합 검증과 PR #51 병합, 10~15분 사람 플레이·1080p·720p 가독성 검증, C1U 사용자 결정 게이트다.",
    "다음 순서는 10~15분 사람 플레이·1080p·720p 가독성 검증, C1U 사용자 결정 게이트다. PR #51 병합 결과는 GitHub PR 상태가 원본이다.",
)

# GDD
replace_once(
    "docs/OMENWARD_GAME_DESIGN.md",
    "- 상태: **프리프로덕션 계약 승인 / C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기 / 사람 플레이 미검증**",
    "- 상태: **프리프로덕션 계약 승인 / C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3_AUTOMATED_CONTRACTS_PROVEN / 사람 플레이 미검증**",
)
replace_once("docs/OMENWARD_GAME_DESIGN.md", "+ C3_IMPLEMENTED", "+ C3_AUTOMATED_CONTRACTS_PROVEN")
replace_once(
    "docs/OMENWARD_GAME_DESIGN.md",
    "- C3는 건설 전 확률 미리보기, 토큰 장부, T-30/T-15/T-5 징조, 상성·사거리·현재 타기팅, 라인별 원인 보고, 건설 비교를 실제 도메인 snapshot과 HUD에 연결했다.",
    f"- C3는 건설 전 확률 미리보기, 토큰 장부, T-30/T-15/T-5 징조, 상성·사거리·현재 타기팅, 라인별 원인 보고, 건설 비교를 실제 도메인 snapshot과 HUD에 연결했고 head `{PROOF_HEAD}`, run `{PROOF_RUN}`에서 자동 계약 검증을 완료했다.",
)
replace_once(
    "docs/OMENWARD_GAME_DESIGN.md",
    "- C3 최신 영구 CI 증거와 PR #51 병합.\n- 이동권 완성선 보상량과 럭키 규칙 통합.",
    "- 이동권 완성선 보상량과 럭키 규칙 통합.",
)
replace_once(
    "docs/OMENWARD_GAME_DESIGN.md",
    "→ C3 코어 UX 6종 IMPLEMENTED·원격 검증 대기\n→ C4 10~15분 사람 플레이·1080p·720p 가독성 QA",
    "→ C3 코어 UX 6종 AUTOMATED_CONTRACTS_PROVEN\n→ C4 10~15분 사람 플레이·1080p·720p 가독성 QA",
)

# Roadmap
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "- 현재 상태: **C0·C1·C2 REMOTE_PROVEN / C3 IMPLEMENTED·원격 검증 대기 / C1U 사용자 결정 대기 / 사람 QA 다음**",
    "- 현재 상태: **C0·C1·C2 REMOTE_PROVEN / C3 AUTOMATED_CONTRACTS_PROVEN / C1U 사용자 결정 대기 / 사람 QA 현재**",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "→ C3 승인 코어 UX 6종 구현 완료·원격 통합 검증 대기",
    "→ C3 승인 코어 UX 6종 자동 계약 검증 완료",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "| C3 코어 UX | 승인 UX 6종을 실제 데이터와 연결 | **IMPLEMENTED / REMOTE_VALIDATION_PENDING** | 영구 CI·사람 가독성 기준 |",
    "| C3 코어 UX | 승인 UX 6종을 실제 데이터와 연결 | **AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING** | 사람 가독성 기준 |",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "C3 승인 코어 UX 6종 최신 영구 CI 검증과 PR #51 병합\n→ 10~15분 사람 플레이·1080p·720p 가독성 QA",
    "10~15분 사람 플레이·1080p·720p 가독성 QA",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "C3는 PR #51에서 실제 snapshot·HUD·정상/경계/결정론 회귀를 구현했으며 최신 영구 CI 검증을 기다린다.",
    f"C3는 실제 snapshot·HUD·정상/경계/결정론·비변경 회귀를 구현했고 head `{PROOF_HEAD}`, run `{PROOF_RUN}`에서 자동 계약 검증을 완료했다. PR #51 병합 결과는 GitHub PR 상태가 원본이다.",
)

# Decisions
replace_once(
    "docs/DECISIONS_PENDING.md",
    "- 현재 작업: PR #51 C3 코어 UX 원격 검증·병합 / 다음 사용자 결정: C1U 이동권·럭키·분포",
    "- 현재 작업: C3 자동 계약 검증 완료·사람 QA 준비 / 다음 사용자 결정: C1U 이동권·럭키·분포",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "- [ ] 최신 영구 `Validate Core Contracts` 원격 증거 기록과 PR #51 병합.",
    f"- [x] C3 자동 계약 원격 검증 — head `{PROOF_HEAD}`, run `{PROOF_RUN}`, 5 jobs success.\n- PR #51 병합 결과는 GitHub PR 상태가 원본이다.",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "- [x] C3 코어 UX 6종 구현과 정상·경계·결정론 계약 추가. 최신 영구 원격 run은 병합 전 기록.",
    f"- [x] C3 코어 UX 6종·정상·경계·결정론·비변경 계약 원격 검증 — head `{PROOF_HEAD}`, run `{PROOF_RUN}`.",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "| headless 테스트 | Godot 4.7.1 전체 suite 원격 통과 (C1 `29926598807`, 통합 C1·C2 `29938742864`); C3 최신 통합 run 대기 |",
    f"| headless 테스트 | Godot 4.7.1 전체 suite 원격 통과 (C1 `29926598807`, C1·C2 `29938742864`, C3 `{PROOF_RUN}`) |",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "1. C3 최신 영구 Core Contracts 원격 검증과 PR #51 병합\n2. 10~15분 사람 플레이와 1080p·720p QA\n3. C1U 이동권·럭키 정본 통합과 100,000시드 사용자 결정",
    "1. 10~15분 사람 플레이와 1080p·720p QA\n2. C1U 이동권·럭키 정본 통합과 100,000시드 사용자 결정\n3. 밸런스 안정화",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "4. 밸런스 안정화\n5. 콘텐츠·아트 확장",
    "4. 콘텐츠·아트 확장\n5. 캠페인·데모 통합",
)

# Godot structure
replace_once(
    "docs/GODOT_PROJECT_STRUCTURE.md",
    "- 상태: **기술 기준선·C1 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기**",
    "- 상태: **기술 기준선·C1 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX AUTOMATED_CONTRACTS_PROVEN**",
)
replace_once(
    "docs/GODOT_PROJECT_STRUCTURE.md",
    "현재 UI는 자동 계약을 위한 텍스트 중심 PoC다.",
    f"현재 UI는 자동 계약을 위한 텍스트 중심 PoC이며 head `{PROOF_HEAD}`, run `{PROOF_RUN}`에서 전체 계약을 통과했다.",
)

# Validation evidence
replace_once(
    "docs/VERTICAL_SLICE_VALIDATION.md",
    "# Vertical Slice Validation\n",
    f"# Vertical Slice Validation\n\n## C3 automated evidence\n\n- 검증 head: `{PROOF_HEAD}`\n- `Validate Core Contracts` run: `{PROOF_RUN}`\n- 결과: Ubuntu/Windows × Python 3.12/3.13 네 계약 작업과 Godot 4.7.1 작업, 총 5 jobs success.\n- 범위: C1·C2·C3·프로젝트 코어·Skill·전체 mutation·whitespace, editor import·모든 headless·runtime smoke.\n- 사람 플레이·1080p·720p 가독성은 아직 실행하지 않았다.\n",
)

# Mutation test references the final workflow and proven audit state.
replace_required(
    "tests/python/test_c3_core_ux_contract.py",
    ".github/workflows/core-contracts.yml",
    FINAL_WORKFLOW,
)
replace_once(
    "tests/python/test_c3_core_ux_contract.py",
    "C3_IMPLEMENTED / REMOTE_VALIDATION_PENDING / HUMAN_QA_PENDING",
    "C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING",
)

print("C3 proof transition completed")
