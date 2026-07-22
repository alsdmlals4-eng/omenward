from __future__ import annotations

import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
RUN_ID = "29919925777"
VALIDATED_HEAD = "237d07cd59a9553a28725b0e173231bd0e660492"
BASE_MAIN = "ef9e66e3bc5be7711c36123e6c6d7fe8ec8dc9a2"


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def write(relative: str, content: str) -> None:
    (ROOT / relative).write_text(content, encoding="utf-8", newline="\n")


def replace_once(relative: str, old: str, new: str) -> None:
    text = read(relative)
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{relative}: expected one match, found {count}: {old[:120]!r}")
    write(relative, text.replace(old, new, 1))


def replace_regex(relative: str, pattern: str, replacement: str) -> None:
    text = read(relative)
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"{relative}: expected one regex match, found {count}: {pattern!r}")
    write(relative, updated)


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


# Permanent C1 evidence report.
replace_once(
    "docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md",
    "- 작업 상태: `IMPLEMENTED_CANDIDATE / REMOTE_VALIDATION_PENDING`",
    "- 작업 상태: `C1_ROULETTE_CORE_REMOTE_PROVEN`",
)
replace_regex(
    "docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md",
    r"## 6\. 검증 경계\n.*\Z",
    f'''## 6. 원격 검증 결과

- 검증 head: `{VALIDATED_HEAD}`
- GitHub Actions run: `{RUN_ID}`
- Godot: `4.7.1-stable`

통과:

- Ubuntu/Windows × Python 3.12/3.13 계약 검증 `4/4 SUCCESS`.
- C1 Validator·구형 활성 참조·깨진 링크 검사.
- 전체 Python 저장소 테스트 `31/31 PASSED`.
- 프로젝트 코어·Skill Validator·compile·whitespace.
- Godot editor import.
- 모든 `tests/headless/*_test.gd`.
- runtime smoke.

판정:

```text
C1_ROULETTE_CORE_REMOTE_PROVEN
+ C1U_PENDING_DECISIONS
+ HUMAN_QA_NOT_RUN
```

사람 플레이·1920×1080/1280×720 시각 QA·100,000시드 분포는 이번 자동 C1 핵심 계약과 별도다.
''',
)

# Current implementation authority.
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "- 기준 브랜치: `main`\n- 기준 커밋: `69c571c5a49502f9da57e1c8d8eba04455380c0f`",
    f"- 기준 main: `{BASE_MAIN}`\n- 원격 검증 head: `{VALIDATED_HEAD}`\n- 원격 검증 run: `{RUN_ID}`",
)
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "  - `CORE_VERTICAL_SLICE_PARTIAL`",
    "  - `C1_ROULETTE_CORE_REMOTE_PROVEN`\n  - `CORE_VERTICAL_SLICE_PARTIAL`",
)
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "| 테스트 | bootstrap·데이터·경제·룰렛 placeholder·전투·웨이브·우회 관련 headless 테스트 파일 | `IMPLEMENTED` |",
    "| 테스트 | bootstrap·데이터·경제·C1 룰렛·전투·웨이브·우회 headless 회귀와 Python 계약 | `REMOTE_PROVEN` |",
)
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "### 3.1 룰렛 — `C1_IMPLEMENTED_CANDIDATE`\n\n구현 후보:",
    "### 3.1 룰렛 — `C1_ROULETTE_CORE_REMOTE_PROVEN`\n\n검증된 구현:",
)
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "판정: `IMPLEMENTED_CANDIDATE / REMOTE_VALIDATION_PENDING`.",
    f"판정: `C1_ROULETTE_CORE_REMOTE_PROVEN` — Godot 4.7.1 import·전체 headless·runtime smoke와 4환경 계약 검증 통과 (`{RUN_ID}`).",
)
replace_regex(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    r"## 4\. 검증 증거 경계\n.*?(?=## 5\.)",
    f'''## 4. 검증 증거 경계

### 이번 C1에서 원격 실행한 것

- Godot 4.7.1 editor import.
- 전체 `tests/headless/*_test.gd`.
- runtime smoke.
- Ubuntu/Windows × Python 3.12/3.13 계약·문서·Skill 검증.
- C1 결정론·중앙 판정·등급·금화·전설 제한·보관·배치 회귀.
- 활성 문서의 구형 Work Order·Goal·Proposal 직접 참조와 깨진 링크 검사.

증거: GitHub Actions run `{RUN_ID}` / head `{VALIDATED_HEAD}`.

### 실행하지 않은 것

- 1920×1080 사람 플레이.
- 1280×720 가독성 QA.
- W1~W20 연속 플레이.
- 100,000시드 확률·경제 분포.
- 재미·밸런스·성능 계측.

따라서 C1 룰렛 핵심 계약은 `REMOTE_PROVEN`이지만 전체 코어 루프와 사람 플레이는 아직 완료가 아니다.

''',
)
replace_regex(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    r"## 5\. 현재 우선순위\n.*?(?=## 6\.)",
    '''## 5. 현재 우선순위

```text
1. PR #49 사용자 검토와 병합 결정
2. C1U 이동권·럭키 규칙 통합과 100,000시드 시뮬레이션
3. 전투 → 거점·성문·승패 목적 루프 연결
4. 승인 코어 UX 6종 최소 구현
5. 10~15분 코어 플레이테스트
6. 밸런스 안정화와 콘텐츠·아트 확장
```

''',
)
replace_regex(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    r"## 6\. 다음 완료 게이트\n.*\Z",
    f'''## 6. C1 완료 판정과 다음 게이트

C1 룰렛 핵심 계약 완료 조건:

- 중앙 판정·8개 완성선·등급·금화·전설 제한이 승인 정본과 일치한다.
- 9개 직접 카드 placeholder와 관련 회귀 계약이 제거됐다.
- 기본 병영 토큰, StageRun 보관과 라인 배치가 연결된다.
- 같은 시드·건물 스냅샷이 같은 결과를 만든다.
- Godot 4.7.1 editor import·전체 headless·runtime smoke가 통과한다.
- 활성 문서의 구형 실행 입력 직접 참조가 0건이다.

위 조건은 run `{RUN_ID}`에서 통과했다. 다음 제품 결정은 C1U 이동권·럭키·고정 상위 등급 템플릿·100,000시드 분포다.
''',
)

# README and state capsules.
replace_once(
    "README.md",
    "> 현재 상태: **기술·데이터 그레이박스 수직 슬라이스 존재 / 코어 루프 미완결 / 사람 플레이 검증 대기**",
    "> 현재 상태: **C1 룰렛 핵심 계약 원격 검증 완료 / 전투 목적 루프·사람 플레이 미완결**",
)
replace_once(
    "README.md",
    "정본·프로젝트 코어 확정·잠금 완료\n→ [현재] 승인 룰렛 핵심 계약 복구\n→ 전투를 접전지·거점·성문·승패에 연결",
    "정본·프로젝트 코어 확정·잠금 완료\n→ 승인 룰렛 핵심 계약 원격 검증 완료\n→ [다음] C1U 이동권·럭키·100,000시드 결정\n→ 전투를 접전지·거점·성문·승패에 연결",
)
replace_once(
    "README.md",
    "현재 저장소에는 Godot 기술 기준선과 수직 슬라이스 구성요소가 존재하지만, 승인 룰렛 판정·전투 목적 루프·핵심 UX가 완결되지 않았다.",
    "현재 저장소에는 Godot 기술 기준선과 원격 검증된 C1 룰렛 핵심 계약이 존재하지만, 룰렛 유틸리티·전투 목적 루프·핵심 UX는 완결되지 않았다.",
)

replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "- 저장소 상태: **기술 기준선 구현 / 핵심 수직 슬라이스 부분 구현 / 코어 루프·사람 플레이 미검증**",
    "- 저장소 상태: **C1 룰렛 핵심 계약 REMOTE_PROVEN / 전투 목적 루프·사람 플레이 미검증**",
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "TECHNICAL_BASELINE_IMPLEMENTED\n+ CORE_VERTICAL_SLICE_PARTIAL",
    "TECHNICAL_BASELINE_IMPLEMENTED\n+ C1_ROULETTE_CORE_REMOTE_PROVEN\n+ CORE_VERTICAL_SLICE_PARTIAL",
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "- 승인 룰렛 판정, 전투→거점·성문·승패 연결, 코어 UX 6종은 완결되지 않았다.\n- 자동 테스트 파일의 존재를 최신 runtime·사람 플레이 증거로 간주하지 않는다.\n- 현재 게임 기능 변경은 승인 룰렛 중앙 판정·완성선·등급·보상·보관 계약으로 한정한다.",
    f"- 승인 룰렛 중앙 판정·완성선·등급·보상·보관은 run `{RUN_ID}`에서 원격 검증됐다.\n- 전투→거점·성문·승패 연결과 코어 UX 6종은 완결되지 않았다.\n- 자동 테스트 통과를 사람 플레이·시각 QA 증거로 간주하지 않는다.",
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "정본·프로젝트 코어 확정·잠금 완료\n→ [현재] 승인 룰렛 핵심 계약 복구\n→ 전투 목적 루프 연결",
    "정본·프로젝트 코어 확정·잠금 완료\n→ 승인 룰렛 핵심 계약 원격 검증 완료\n→ [다음] C1U 이동권·럭키·100,000시드\n→ 전투 목적 루프 연결",
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "- 현재 C1 PR은 룰렛 핵심 계약과 구형 활성 참조 정리만 포함한다. 이동권·럭키·고정 상위 템플릿은 별도 결정 전 확정하지 않는다.",
    "- PR #49는 C1 룰렛 핵심 계약과 구형 활성 참조 정리를 원격 검증했다. 이동권·럭키·고정 상위 템플릿은 C1U 결정 전 확정하지 않는다.",
)

replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "- 현재 상태: **CORE_LOCKED / C1 승인 룰렛 핵심 계약 구현·원격 검증 진행 / 전투 목적 루프·사람 플레이 미검증**",
    "- 현재 상태: **CORE_LOCKED / C1 룰렛 핵심 계약 REMOTE_PROVEN / C1U·전투 목적 루프·사람 플레이 미검증**",
)
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "2. 저장소에는 기술 기준선과 수직 슬라이스 구성요소가 있으며, C1 룰렛 핵심 계약을 복구 중이다. 전투 목적·코어 UX는 아직 미완결이다.",
    "2. 저장소에는 기술 기준선과 원격 검증된 C1 룰렛 핵심 계약이 있다. C1U 유틸리티·전투 목적·코어 UX는 아직 미완결이다.",
)
replace_once("docs/HANDOFF_CONTEXT.md", "8. 현재 작업의 work_orders 문서", "8. 현재 PR·Issue와 승인 보고서")
replace_once("docs/HANDOFF_CONTEXT.md", "13. 현재 Issue / Goal / 승인 제안서", "13. 현재 PR·Issue와 검증 증거")
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "TECHNICAL_BASELINE_IMPLEMENTED\n+ CORE_VERTICAL_SLICE_PARTIAL",
    "TECHNICAL_BASELINE_IMPLEMENTED\n+ C1_ROULETTE_CORE_REMOTE_PROVEN\n+ CORE_VERTICAL_SLICE_PARTIAL",
)
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "현재 Godot 프로젝트는 기술·데이터 그레이박스와 여러 수직 슬라이스 구성요소를 포함한다. 그러나 승인 룰렛 판정, 전투 상태 기반 승패, 접전지·거점·성문 연결과 승인 UX 6종이 닫히지 않았으므로 “핵심 수직 슬라이스 완료”로 부르지 않는다.\n\n다음 순서는 정본 복구 뒤 승인 룰렛 계약, 전투 목적 루프, 코어 UX, 사람 플레이 검증이다.",
    f"현재 Godot 프로젝트는 기술·데이터 그레이박스와 run `{RUN_ID}`에서 원격 검증된 C1 룰렛 핵심 계약을 포함한다. 전투 상태 기반 승패, 접전지·거점·성문 연결과 승인 UX 6종은 닫히지 않았으므로 “핵심 수직 슬라이스 완료”로 부르지 않는다.\n\n다음 순서는 PR #49 검토 뒤 C1U 결정, 전투 목적 루프, 코어 UX, 사람 플레이 검증이다.",
)

# GDD and approved responsibility documents.
replace_once(
    "docs/OMENWARD_GAME_DESIGN.md",
    "- 상태: **프리프로덕션 계약 승인 / Godot 기술·데이터 기준선 구현 / 핵심 수직 슬라이스 부분 구현·코어 루프 미검증**",
    "- 상태: **프리프로덕션 계약 승인 / C1 룰렛 핵심 계약 REMOTE_PROVEN / 전투 목적 루프·사람 플레이 미검증**",
)
replace_once(
    "docs/OMENWARD_GAME_DESIGN.md",
    "TECHNICAL_BASELINE_IMPLEMENTED\n+ CORE_VERTICAL_SLICE_PARTIAL",
    "TECHNICAL_BASELINE_IMPLEMENTED\n+ C1_ROULETTE_CORE_REMOTE_PROVEN\n+ CORE_VERTICAL_SLICE_PARTIAL",
)
replace_once(
    "docs/OMENWARD_GAME_DESIGN.md",
    "C0 프로젝트 코어·정본 복구 완료\n→ [현재] C1 중앙 판정·완성선·등급·보상·보관 계약\n→ C1 유틸리티 규칙 통합과 100,000시드 검증",
    "C0 프로젝트 코어·정본 복구 완료\n→ C1 중앙 판정·완성선·등급·보상·보관 REMOTE_PROVEN\n→ [다음] C1 유틸리티 규칙 통합과 100,000시드 검증",
)
replace_once(
    "docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md",
    "- 상태: **프리프로덕션 구조 승인 / 기술 기준선 구현 / C1 승인 룰렛 핵심 계약 구현·원격 검증 진행**",
    "- 상태: **프리프로덕션 구조 승인 / 기술 기준선·C1 룰렛 핵심 계약 REMOTE_PROVEN / C1U·전투 목적 루프 대기**",
)
replace_once(
    "docs/design/APPROVED_ROULETTE_CORE_RULES.md",
    "- 상태: **핵심 구조 승인 / C1 중앙 판정·완성선·등급·보상·보관 구현 후보 / 유틸리티 세부 일부 미확정**",
    "- 상태: **핵심 구조 승인 / C1 중앙 판정·완성선·등급·보상·보관 REMOTE_PROVEN / 유틸리티 세부 일부 미확정**",
)
replace_once(
    "docs/design/APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md",
    "- 상태: **확률 구조·목표 분포 승인 / C1 기본 릴 가중치 구현 후보 / 100,000시드 검증·이동권 보상·럭키 해석 대기**",
    "- 상태: **확률 구조·목표 분포 승인 / C1 기본 릴 가중치 REMOTE_PROVEN / 100,000시드·이동권·럭키 C1U 대기**",
)
replace_once(
    "docs/design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md",
    "## 10. 현재 C1 검증 조건",
    f"## 10. C1 원격 검증 결과\n\nGitHub Actions run `{RUN_ID}`에서 Godot 4.7.1 editor import·전체 headless·runtime smoke와 4환경 계약 검증을 통과했다.\n\n검증 조건:",
)

# Roadmap and decisions.
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "- 현재 상태: **C0 완료 / C1 승인 룰렛 핵심 계약 구현·원격 검증 진행**",
    "- 현재 상태: **C0 완료 / C1 룰렛 핵심 계약 REMOTE_PROVEN / PR #49 사용자 검토 대기**",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "→ [현재] 승인 룰렛 핵심 계약 복구\n→ C1 이동권·럭키 규칙 통합·100,000시드 검증",
    "→ 승인 룰렛 핵심 계약 원격 검증 완료\n→ [다음] C1U 이동권·럭키 규칙 통합·100,000시드 검증",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "| P1 기술 기준선 | 실행·데이터·결정론·검증 골격 | **구현됨 / 최신 runtime 재검증 필요** | C0 정본 일치 |",
    "| P1 기술 기준선 | 실행·데이터·결정론·검증 골격 | **REMOTE_PROVEN** | 정본 유지 |",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "| C1 룰렛 핵심 계약 | 중앙 판정 줄·완성선·등급·보상·보관 | **구현·원격 검증 진행** | Godot 계약 테스트 PASS |\n| C1U 룰렛 유틸리티 | 이동권·럭키 정본 통합·100,000시드 | 미시작 | 사용자 결정·분포 기준 |",
    "| C1 룰렛 핵심 계약 | 중앙 판정 줄·완성선·등급·보상·보관 | **REMOTE_PROVEN** | PR #49 사용자 검토 |\n| C1U 룰렛 유틸리티 | 이동권·럭키 정본 통합·100,000시드 | **다음** | 사용자 결정·분포 기준 |",
)
replace_regex(
    "docs/OMENWARD_ROADMAP.md",
    r"## 15\. 지금 실행할 단 하나의 작업\n.*\Z",
    f'''## 15. 지금 실행할 단 하나의 작업

```text
PR #49 C1 원격 검증 결과·diff 사용자 검토
→ 병합 결정
→ C1U 이동권·럭키·고정 상위 템플릿·100,000시드 Plan
```

C1 핵심 계약은 run `{RUN_ID}`에서 원격 검증됐다. 전투 목적 루프·코어 UX·신규 콘텐츠는 같은 PR에 섞지 않는다.
''',
)

replace_once(
    "docs/DECISIONS_PENDING.md",
    "- 현재 작업: C1 승인 룰렛 핵심 계약 구현·원격 검증 / 다음 결정: C1U 이동권·럭키·분포",
    "- 현재 작업: PR #49 C1 원격 검증 결과 검토 / 다음 결정: C1U 이동권·럭키·분포",
)
replace_once("docs/DECISIONS_PENDING.md", "- [ ] Godot 4.7.1 원격 전체 회귀.", f"- [x] Godot 4.7.1 원격 전체 회귀 — run `{RUN_ID}`.")
replace_once("docs/DECISIONS_PENDING.md", "- [ ] 문서 PR 뒤 Godot editor import와 기존 headless suite 재실행.\n- [ ] 룰렛 복구 PR에서 같은 시드·보드·결과 결정론 검증.", f"- [x] Godot 4.7.1 editor import·전체 headless·runtime smoke — run `{RUN_ID}`.\n- [x] 같은 시드·건물 스냅샷·보드·결과 결정론 검증.")
replace_once(
    "docs/DECISIONS_PENDING.md",
    "| headless 테스트 파일 | 존재하지만 이번 문서 PR에서 Godot로 재실행하지 않음 |",
    f"| headless 테스트 | Godot 4.7.1 전체 suite 원격 통과 (`{RUN_ID}`) |",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "1. C1 승인 룰렛 핵심 계약 원격 검증\n2. C1U 이동권·럭키 정본 통합과 100,000시드 검증\n3. 전투 목적 루프 연결\n5. 승인 코어 UX 6종\n6. 10~15분 사람 플레이와 1080p·720p QA\n7. 밸런스 안정화\n8. 콘텐츠·아트 확장",
    "1. PR #49 C1 원격 검증 결과 검토·병합 결정\n2. C1U 이동권·럭키 정본 통합과 100,000시드 검증\n3. 전투 목적 루프 연결\n4. 승인 코어 UX 6종\n5. 10~15분 사람 플레이와 1080p·720p QA\n6. 밸런스 안정화\n7. 콘텐츠·아트 확장",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "현재는 새로운 병종·Tier·보스·캠페인 콘텐츠를 추가하는 단계가 아니다. 다음 기능 변경은 승인 룰렛 계약 복구로 제한한다.",
    "현재는 새로운 병종·Tier·보스·캠페인 콘텐츠를 추가하는 단계가 아니다. 다음 기능 변경은 PR #49 병합 뒤 C1U 결정으로 제한한다.",
)

# Validators and mutation tests now enforce the proven state.
replace_once("tools/validate_project_core_docs.py", '    "C1_IMPLEMENTED_CANDIDATE",', '    "C1_ROULETTE_CORE_REMOTE_PROVEN",')
replace_once("tools/validate_project_core_docs.py", '        "승인 룰렛 핵심 계약 복구",', '        "승인 룰렛 핵심 계약 원격 검증 완료",')
replace_once(
    "tools/validate_c1_roulette.py",
    "    baseline = (root / \"docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md\").read_text(encoding=\"utf-8\")",
    f'''    completion_requirements = {{
        "docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md": ("C1_ROULETTE_CORE_REMOTE_PROVEN", "GitHub Actions run: `{RUN_ID}`"),
        "docs/CURRENT_IMPLEMENTATION_STATUS.md": ("C1_ROULETTE_CORE_REMOTE_PROVEN", "원격 검증 run: `{RUN_ID}`"),
        "docs/OMENWARD_ROADMAP.md": ("승인 룰렛 핵심 계약 원격 검증 완료", "**REMOTE_PROVEN**"),
        "docs/design/APPROVED_ROULETTE_CORE_RULES.md": ("C1 중앙 판정·완성선·등급·보상·보관 REMOTE_PROVEN",),
    }}
    for relative, phrases in completion_requirements.items():
        text = (root / relative).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{{relative}} missing proven C1 evidence: {{phrase}}")
    stale_proven_state = (
        "IMPLEMENTED_CANDIDATE / REMOTE_VALIDATION_PENDING",
        "C1_IMPLEMENTED_CANDIDATE",
        "C1 승인 룰렛 핵심 계약 구현·원격 검증 진행",
        "C1 기본 릴 가중치 구현 후보",
    )
    for path in active_markdown_files(root):
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root).as_posix()
        for stale in stale_proven_state:
            if stale in text:
                errors.append(f"active document retains pre-validation C1 state: {{relative}} -> {{stale}}")

    baseline = (root / "docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md").read_text(encoding="utf-8")''',
)
replace_once(
    "tests/python/test_c1_roulette_contract.py",
    "    def test_missing_judgment_line_regression_is_rejected(self) -> None:",
    '''    def test_pending_remote_validation_state_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            report = root / "docs" / "C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md"
            report.write_text(
                report.read_text(encoding="utf-8").replace(
                    "C1_ROULETTE_CORE_REMOTE_PROVEN",
                    "IMPLEMENTED_CANDIDATE / REMOTE_VALIDATION_PENDING",
                ),
                encoding="utf-8",
            )
            self.assertTrue(any("pre-validation C1 state" in error or "missing proven C1 evidence" in error for error in validate(root)))

    def test_missing_judgment_line_regression_is_rejected(self) -> None:''',
)

# Self-clean before validation.
script = ROOT / "tools/_mark_validation_evidence.py"
if script.exists():
    script.unlink()

run("python", "-m", "py_compile", "tools/validate_c1_roulette.py", "tests/python/test_c1_roulette_contract.py", "tools/validate_project_core_docs.py")
run("python", "tools/validate_c1_roulette.py")
run("python", "-m", "unittest", "discover", "-s", "tests/python", "-v")
run("python", "tools/validate_project_core_docs.py")
if (ROOT / "tools/validate_skill_system.py").exists():
    run("python", "tools/validate_skill_system.py")
run("git", "diff", "--check")
run("git", "config", "user.name", "github-actions[bot]")
run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
run("git", "add", "-A")
run("git", "commit", "-m", "record C1 remote validation evidence")
run("git", "push", "origin", "HEAD:agent/c1-approved-roulette-contract-recovery")
