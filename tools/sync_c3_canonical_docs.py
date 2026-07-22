from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]


def replace_once(relative: str, old: str, new: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{relative}: expected one exact match, found {count}: {old[:80]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


def regex_once(relative: str, pattern: str, replacement: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE | re.DOTALL)
    if count != 1:
        raise RuntimeError(f"{relative}: expected one regex match, found {count}: {pattern[:80]!r}")
    path.write_text(updated, encoding="utf-8", newline="\n")


# README
replace_once(
    "README.md",
    "> 현재 상태: **C1 룰렛 REMOTE_PROVEN / C2 전투 목적 루프 REMOTE_PROVEN / 사람 플레이 미완결**",
    "> 현재 상태: **C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기 / 사람 플레이 미완결**",
)
replace_once(
    "README.md",
    "→ [다음 구현] C3 승인 코어 UX 6종\n→ [결정 게이트] C1U 이동권·럭키·100,000시드\n→ 10~15분 사람 플레이와 1080p·720p 가독성 검증",
    "→ C3 승인 코어 UX 6종 구현 완료·원격 통합 검증 대기\n→ [다음 실행] 10~15분 사람 플레이와 1080p·720p 가독성 검증\n→ [결정 게이트] C1U 이동권·럭키·100,000시드",
)
replace_once(
    "README.md",
    "현재 저장소에는 원격 검증된 C1 룰렛 핵심 계약과 C2 전투 목적 루프가 존재한다. C2는 접전지·거점·성문·본진·자연 승패·경제를 연결했고 통합 자동 검증을 마쳤다. 현재 판정은 `C1_ROULETTE_CORE_REMOTE_PROVEN`, `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`, `CORE_VERTICAL_SLICE_PARTIAL`, `CORE_LOOP_NOT_PROVEN`, `HUMAN_QA_NOT_RUN`이며 사람 플레이는 아직 실행하지 않았다.",
    "현재 저장소에는 원격 검증된 C1 룰렛 핵심 계약과 C2 전투 목적 루프가 존재한다. C3는 확률 미리보기·토큰 장부·단계형 징조·전술 오버레이·웨이브 원인 보고·건설 비교를 실제 도메인 snapshot과 HUD에 연결했으며 최신 원격 통합 검증을 기다린다. 현재 판정은 `C1_ROULETTE_CORE_REMOTE_PROVEN`, `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`, `C3_IMPLEMENTED`, `CORE_VERTICAL_SLICE_PARTIAL`, `CORE_LOOP_NOT_PROVEN`, `HUMAN_QA_NOT_RUN`이다.",
)
replace_once(
    "README.md",
    "C2 구현·감사는 [`docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md`](docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md), 자동·수동 검증은",
    "C2 구현·감사는 [`docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md`](docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md), C3 구현 계약은 [`docs/C3_CORE_UX_AUDIT_2026-07-23.md`](docs/C3_CORE_UX_AUDIT_2026-07-23.md), 자동·수동 검증은",
)

# Active context
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "- 저장소 상태: **C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / 사람 플레이 미검증**",
    "- 저장소 상태: **C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기 / 사람 플레이 미검증**",
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "+ C2_BATTLE_OBJECTIVE_REMOTE_PROVEN\n+ CORE_VERTICAL_SLICE_PARTIAL",
    "+ C2_BATTLE_OBJECTIVE_REMOTE_PROVEN\n+ C3_IMPLEMENTED\n+ CORE_VERTICAL_SLICE_PARTIAL",
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "- C1·C2 통합 원격 검증은 완료됐고 코어 UX 6종·사람 플레이는 아직 완료되지 않았다.",
    "- C1·C2 통합 원격 검증은 완료됐다. C3 코어 UX 6종은 실제 snapshot과 HUD에 구현됐고 최신 영구 CI 검증을 기다리며, 사람 플레이는 아직 완료되지 않았다.",
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "→ [다음 구현] C3 승인 코어 UX 6종\n→ [결정 게이트] C1U 이동권·럭키·100,000시드\n→ 사람 플레이 검증",
    "→ C3 승인 코어 UX 6종 구현 완료·원격 통합 검증 대기\n→ [다음 실행] 사람 플레이·1080p·720p 가독성 검증\n→ [결정 게이트] C1U 이동권·럭키·100,000시드",
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "- PR #49는 main에 병합됐다. PR #50은 C2 전투 목적 루프의 원격 검증과 문서·검증 동기화를 완료했으며 병합 대상이다.",
    "- PR #49와 PR #50은 main에 병합됐다. PR #51은 C3 코어 UX 6종의 구현·문서·검증을 통합하는 현재 작업이다.",
)

# Handoff
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "- 현재 상태: **CORE_LOCKED / C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C1U·사람 플레이 미검증**",
    "- 현재 상태: **CORE_LOCKED / C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기 / C1U·사람 플레이 미검증**",
)
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "2. 저장소에는 원격 검증된 C1 룰렛 핵심과 C2 전투 목적 루프가 있다. C1U 유틸리티 결정, C3 코어 UX와 사람 플레이는 남아 있다.",
    "2. 저장소에는 원격 검증된 C1 룰렛 핵심과 C2 전투 목적 루프, 실제 데이터에 연결된 C3 코어 UX 6종이 있다. C3 최신 원격 통합 검증, C1U 유틸리티 결정과 사람 플레이가 남아 있다.",
)
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "+ C2_BATTLE_OBJECTIVE_REMOTE_PROVEN\n+ CORE_VERTICAL_SLICE_PARTIAL",
    "+ C2_BATTLE_OBJECTIVE_REMOTE_PROVEN\n+ C3_IMPLEMENTED\n+ CORE_VERTICAL_SLICE_PARTIAL",
)
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "현재 Godot 프로젝트는 C1 run `29926598807`과 통합 Core Contracts run `29936497790`에서 검증된 C1 룰렛 핵심·C2 전투 목적 루프를 포함한다. C3 승인 UX 6종과 사람 플레이는 남아 있으므로 ‘핵심 수직 슬라이스 완료’로 부르지 않는다.\n\n다음 순서는 PR #50 병합, C3 승인 코어 UX 6종, C1U 사용자 결정 게이트, 사람 플레이 검증이다.",
    "현재 Godot 프로젝트는 C1 run `29926598807`과 통합 Core Contracts run `29936497790`에서 검증된 C1 룰렛 핵심·C2 전투 목적 루프를 포함한다. C3 승인 UX 6종은 실제 도메인 snapshot과 HUD에 구현됐고 최신 영구 CI 검증을 기다린다. 사람 플레이가 남아 있으므로 ‘핵심 수직 슬라이스 완료’로 부르지 않는다.\n\n다음 순서는 C3 원격 통합 검증, 10~15분 사람 플레이·1080p·720p 가독성 검증, C1U 사용자 결정 게이트다.",
)

# Current implementation status
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "  - `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`\n  - `CORE_VERTICAL_SLICE_PARTIAL`",
    "  - `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`\n  - `C3_IMPLEMENTED`\n  - `CORE_VERTICAL_SLICE_PARTIAL`",
)
replace_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "| 테스트 | C1·C2·전투·경제·건설·웨이브·우회 headless 및 Python mutation 계약 | `REMOTE_PROVEN` |",
    "| 테스트 | C1·C2 원격 검증, C3 정상·경계·결정론 headless 및 Python mutation 계약 | `C3_REMOTE_VALIDATION_PENDING` |",
)
regex_once(
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    r"## 6\. 아직 완결되지 않은 영역\n.*?## 7\. 현재 우선순위\n\n```text\n.*?```\n\nC3와 사람 플레이 완료 전에는 전체 코어 루프를 `PROVEN`으로 부르지 않는다\. 사람 플레이 완료 전에는 `CORE_LOOP_PROVEN` 또는 `CORE_VERTICAL_SLICE_COMPLETE`를 사용하지 않는다\.",
    """## 6. C3 코어 UX와 남은 검증

### 6.1 베일의 징조 — `IMPLEMENTED / REMOTE_VALIDATION_PENDING`

- 30초 밖에서는 다음 공세까지 시간만 표시한다.
- T-30은 라인·수량·역할, T-15는 정확한 병종·상성 힌트, T-5는 최다 위협 라인을 공개한다.

### 6.2 코어 UX — `IMPLEMENTED / REMOTE_VALIDATION_PENDING`

1. 건설 전 룰렛 확률 미리보기.
2. 룰렛 토큰 장부와 출처 건물·보상 병종.
3. T-30/T-15/T-5 공세 전조.
4. 상성·사거리·현재 타기팅 오버레이.
5. 웨이브 종료 후 실제 이벤트 기반 라인별 원인 보고.
6. 비용·식량·룰렛 기여·차단 사유를 포함한 건설 선택 비교 UI.

- UI는 계산하지 않고 `StageRun.core_ux_snapshot()`을 표시한다.
- 금화 부족·점령/교착·빈 토큰·대상 없음·미완료 웨이브와 같은 경계를 회귀로 보호한다.
- C1U 이동권·럭키·고정 상위 템플릿은 구현하지 않았다.

### 6.3 사람 플레이·콘텐츠 검증 — `NOT_RUN`

- 1920×1080·1280×720 실제 플레이와 가독성 QA.
- 10~15분 코어 재미·학습 검증.
- W1~W20 연속 플레이.
- 100,000시드 룰렛·경제 분포.
- 전투 성능·밸런스 계측.

## 7. 현재 우선순위

```text
1. C3 최신 영구 Core Contracts 원격 검증과 PR #51 병합
2. 10~15분 사람 플레이·1080p·720p 가독성 QA
3. C1U 이동권·럭키·상위 템플릿 사용자 결정 게이트
4. 밸런스 안정화
5. 콘텐츠·아트 확장
```

C3 자동 검증과 사람 플레이 완료 전에는 전체 코어 루프를 `PROVEN`으로 부르지 않는다. 사람 플레이 완료 전에는 `CORE_LOOP_PROVEN` 또는 `CORE_VERTICAL_SLICE_COMPLETE`를 사용하지 않는다.""",
)

# Roadmap
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "- 현재 상태: **C0·C1·C2 REMOTE_PROVEN / C1U 사용자 결정 대기 / C3 코어 UX 다음 구현**",
    "- 현재 상태: **C0·C1·C2 REMOTE_PROVEN / C3 IMPLEMENTED·원격 검증 대기 / C1U 사용자 결정 대기 / 사람 QA 다음**",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "- 현재 구현·감사 입력: `docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md`",
    "- 현재 구현·감사 입력: `docs/C3_CORE_UX_AUDIT_2026-07-23.md`",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "→ [다음 구현] C3 승인 코어 UX 6종\n→ [결정 게이트] C1U 이동권·럭키 규칙 통합·100,000시드 검증\n→ 10~15분 코어 플레이테스트",
    "→ C3 승인 코어 UX 6종 구현 완료·원격 통합 검증 대기\n→ [다음 실행] 10~15분 코어 플레이테스트·1080p·720p 가독성 QA\n→ [결정 게이트] C1U 이동권·럭키 규칙 통합·100,000시드 검증",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "| C3 코어 UX | 승인 UX 6종을 실제 데이터와 연결 | **다음 구현** | 이해도·가독성 기준 |",
    "| C3 코어 UX | 승인 UX 6종을 실제 데이터와 연결 | **IMPLEMENTED / REMOTE_VALIDATION_PENDING** | 영구 CI·사람 가독성 기준 |",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "PR #50 C2 검증 결과 병합\n→ C3 승인 코어 UX 6종 최소 구현\n→ C1U는 사용자 결정 전 보류\n→ 10~15분 사람 플레이 준비",
    "PR #50 C2 병합 완료\n→ C3 승인 코어 UX 6종 구현 완료·원격 검증 대기\n→ 10~15분 사람 플레이·가독성 QA 준비\n→ C1U는 사용자 결정 전 보류",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "C1 핵심 계약은 최종 run `29926598807`에서 검증되고 main에 병합됐다. C2는 통합 head `496157d0b87ab71ea2c9f25780f21df9f68b67f3`, `Validate Core Contracts` run `29936497790`에서 원격 검증됐다. C1U·코어 UX·신규 콘텐츠는 같은 PR에 섞지 않는다.",
    "C1 핵심 계약은 최종 run `29926598807`에서 검증되고 main에 병합됐다. C2는 통합 Core Contracts에서 원격 검증된 뒤 PR #50으로 main에 병합됐다. C3는 PR #51에서 실제 snapshot·HUD·정상/경계/결정론 회귀를 구현했으며 최신 영구 CI 검증을 기다린다. C1U와 신규 콘텐츠는 같은 PR에 섞지 않는다.",
)

# Decisions
replace_once(
    "docs/DECISIONS_PENDING.md",
    "- 현재 작업: PR #50 C2 병합 및 C3 코어 UX 착수 / 다음 사용자 결정: C1U 이동권·럭키·분포",
    "- 현재 작업: PR #51 C3 코어 UX 원격 검증·병합 / 다음 사용자 결정: C1U 이동권·럭키·분포",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "- [ ] PR #50 병합.",
    "- [x] PR #50 병합 완료.",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "- [ ] 본진·성문·거점 상태의 월드 표시와 HUD 정보 계층은 C3 UX에서 검증.",
    "- [x] 본진·성문·거점 상태와 C3 HUD 정보 계층의 자동 계약 구현. 최종 배치·가독성은 사람 QA 대기.",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "- [x] C1·C2 통합 Godot·4환경 계약·문서·Skill 검증 — run `29936497790`.\n- [x] 같은 시드·건물 스냅샷·보드·결과 결정론 검증.\n- [ ] 코어 UX 뒤 1920×1080·1280×720 사람 플레이.",
    "- [x] C1·C2 통합 Godot·4환경 계약·문서·Skill 검증 — run `29936497790`.\n- [x] 같은 시드·건물 스냅샷·보드·결과 결정론 검증.\n- [x] C3 코어 UX 6종 구현과 정상·경계·결정론 계약 추가. 최신 영구 원격 run은 병합 전 기록.\n- [ ] C3 뒤 1920×1080·1280×720 사람 플레이.",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "| headless 테스트 | Godot 4.7.1 전체 suite 원격 통과 (C1 `29926598807`, 통합 C1·C2 `29936497790`) |",
    "| headless 테스트 | Godot 4.7.1 전체 suite 원격 통과 (C1 `29926598807`, 통합 C1·C2 `29936497790`); C3 최신 통합 run 대기 |",
)

# GDD
replace_once("docs/OMENWARD_GAME_DESIGN.md", "- 문서 버전: **v0.22**", "- 문서 버전: **v0.23**")
replace_once(
    "docs/OMENWARD_GAME_DESIGN.md",
    "- 상태: **프리프로덕션 계약 승인 / C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / 사람 플레이 미검증**",
    "- 상태: **프리프로덕션 계약 승인 / C1 룰렛 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기 / 사람 플레이 미검증**",
)
replace_once(
    "docs/OMENWARD_GAME_DESIGN.md",
    "+ C2_BATTLE_OBJECTIVE_REMOTE_PROVEN\n+ CORE_VERTICAL_SLICE_PARTIAL",
    "+ C2_BATTLE_OBJECTIVE_REMOTE_PROVEN\n+ C3_IMPLEMENTED\n+ CORE_VERTICAL_SLICE_PARTIAL",
)
replace_once(
    "docs/OMENWARD_GAME_DESIGN.md",
    "C2 전투 목적 루프는 `같은 라인 교전 → 접전지 → 중간거점 → 성문 → 본진·W15 보스 → 자연 승패`와 점령 기반 건물·경제를 연결하며 통합 Core Contracts run `29936497790`에서 검증됐다. 본진 독립 방어 수치와 접전지 별도 점령 시간은 미승인이므로 기존 승인 계약을 가역 fallback으로 재사용한다. 전체 설계와 사람 경험이 완결됐다는 뜻은 아니며 실제 구현 여부는 상태 문서와 코드·데이터·테스트를 대조한다.",
    "C2 전투 목적 루프는 `같은 라인 교전 → 접전지 → 중간거점 → 성문 → 본진·W15 보스 → 자연 승패`와 점령 기반 건물·경제를 연결한다. C3는 건설 전 확률 미리보기, 토큰 장부, T-30/T-15/T-5 징조, 상성·사거리·타기팅, 라인별 원인 보고, 건설 비교를 실제 도메인 snapshot과 HUD에 연결했다. 본진 독립 방어 수치와 접전지 별도 점령 시간은 미승인이므로 기존 승인 계약을 가역 fallback으로 재사용한다. 최신 원격 통합 검증과 사람 플레이 전에는 전체 코어가 완결됐다고 부르지 않는다.",
)

# Documentation map
replace_once(
    "docs/DOCUMENTATION_MAP.md",
    "현재 C3 시작점은 `CURRENT_IMPLEMENTATION_STATUS.md`, `OMENWARD_ROADMAP.md`, 승인 UI·징조·룰렛·전투 표시 책임 문서와 실제 `scripts/ui/`, `scenes/ui/`, 테스트다. C1·C2 보고서는 검증 증거로 보존하며, 과거 Work Order·Goal·Proposal은 Git 이력에서만 추적한다.",
    "현재 사람 QA 시작점은 `CURRENT_IMPLEMENTATION_STATUS.md`, `C3_CORE_UX_AUDIT_2026-07-23.md`, `OMENWARD_ROADMAP.md`, 실제 `scripts/core/core_ux_service.gd`, `scripts/ui/`, `scenes/ui/`, 테스트다. C1·C2 보고서는 검증 증거로 보존하며, 과거 Work Order·Goal·Proposal은 Git 이력에서만 추적한다.",
)
replace_once(
    "docs/DOCUMENTATION_MAP.md",
    "| `DECISIONS_PENDING.md` | 미확정·PoC 조정 항목 |",
    "| `DECISIONS_PENDING.md` | 미확정·PoC 조정 항목 |\n| `C3_CORE_UX_AUDIT_2026-07-23.md` | C3 코어 UX 6종 구현·경계·검증 계약 |",
)
replace_once(
    "docs/DOCUMENTATION_MAP.md",
    "| C2 구현·검증 증거 | `C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md` |",
    "| C2 구현·검증 증거 | `C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md` |\n| C3 코어 UX 구현·검증 계약 | `C3_CORE_UX_AUDIT_2026-07-23.md` |",
)

# Godot project structure
replace_once(
    "docs/GODOT_PROJECT_STRUCTURE.md",
    "- 상태: **기술 기준선·C1 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN**",
    "- 상태: **기술 기준선·C1 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기**",
)
replace_once(
    "docs/GODOT_PROJECT_STRUCTURE.md",
    "- 받은 상태를 표시하고 사용자 의도를 Signal로 반환한다.\n- 금화 차감, 건설 확정, 유닛 생성, 점령 판정을 직접 실행하지 않는다.",
    "- `StageRun.core_ux_snapshot()`으로 받은 상태를 표시하고 사용자 의도를 Signal로 반환한다.\n- 확률, 경제, 원인 코드, 금화 차감, 건설 확정, 유닛 생성, 점령 판정을 직접 계산·실행하지 않는다.\n- C3 HUD는 토큰·확률·징조·사거리/대상·웨이브 원인·건설 비교를 표시한다.",
)
replace_once(
    "docs/GODOT_PROJECT_STRUCTURE.md",
    "targeting_profile_id\ncapture_power",
    "targeting_profile_id\ncounter_tags\ntarget_priority_tags\ncapture_power",
)

# Validation
replace_once(
    "docs/VERTICAL_SLICE_VALIDATION.md",
    "python tools/validate_c2_battle_objective.py\npython tools/validate_c2_battle_objective.py",
    "python tools/validate_c2_battle_objective.py\npython tools/validate_c3_core_ux.py",
)
replace_once(
    "docs/VERTICAL_SLICE_VALIDATION.md",
    "- C1·C2·프로젝트 코어·Skill Validator.",
    "- C1·C2·C3·프로젝트 코어·Skill Validator.",
)
replace_once(
    "docs/VERTICAL_SLICE_VALIDATION.md",
    "- 모든 `tests/headless/*_test.gd`.\n- runtime smoke.",
    "- 모든 `tests/headless/*_test.gd`를 파일별 60초 상한으로 실행.\n- runtime smoke를 60초 상한으로 실행.\n- 임시 C3 수리·진단 파일의 재유입 거부.",
)
replace_once(
    "docs/VERTICAL_SLICE_VALIDATION.md",
    "- C2 같은 라인 목적 이동, 접전지·거점 점령·교착, 건물 효과·경제 전환.\n- 라인별 성문·본진 공격, 자연 승리·패배, W15 전설 보스 승리.",
    "- C2 같은 라인 목적 이동, 접전지·거점 점령·교착, 건물 효과·경제 전환.\n- 라인별 성문·본진 공격, 자연 승리·패배, W15 전설 보스 승리.\n- C3 건설 전 확률, 토큰 출처, 단계형 징조, 사거리·대상·상성, 웨이브 원인, 건설 비교.\n- C3 금화 부족·점령/교착·빈 토큰·대상 없음·미완료 웨이브 경계와 snapshot 결정론.",
)
replace_once(
    "docs/VERTICAL_SLICE_VALIDATION.md",
    "2. 병영 건설→룰렛→결과 보관→라인 배치→접전지→중간거점→성문→결과를 확인한다.\n3. 1280×720에서 보드·등급·보관·세 라인·목적 상태가 읽히는지 확인한다.",
    "2. 병영 건설→확률 변화·토큰 출처→룰렛→결과 보관→라인 배치→접전지→중간거점→성문→웨이브 원인 보고를 확인한다.\n3. 1280×720에서 보드·등급·보관·세 라인·징조·사거리/대상·건설 비교·목적 상태가 읽히는지 확인한다.",
)

print("C3 canonical document sync completed")
