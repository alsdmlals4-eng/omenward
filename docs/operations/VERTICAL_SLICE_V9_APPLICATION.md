---
document_role: PROJECT_V9_APPLICATION_CONTRACT
contract_source: templates/prompts/VERTICAL_SLICE_INTEGRATED_EXECUTION_PROMPT_v9.md
shared_body_policy: REFERENCE_ONLY_NO_COPY
execution_profile: RECONCILIATION_PLANNING_PROFILE
status: PROPOSED_ON_ISSUE_115_BRANCH
---

# 오멘워드(OMENWARD) Vertical Slice v9 적용 계약

## 1. 실행 바인딩

| 항목 | 값 |
| --- | --- |
| 프로젝트 | 오멘워드(OMENWARD) |
| GitHub | `alsdmlals4-eng/omenward` |
| 기준 `origin/main` | `774087dccc903bc9a8e2aec72eec2a2d13b216ce` |
| 작업 Issue | `#115` |
| 작업 Branch | `gpt/issue-115-base-v9-3-vertical-slice-v9` |
| Base release line | `v9.3.0` |
| Base release commit | `30ca6c7b5f93521f0eb0eed42d01437cd43c50ae` |
| Base evidence commit | `462a86db192d23d0f386281a1eb54b0a8cbad62e` |
| Base Registry SHA-256 | `9847bb2b225c776ad7916930f0f48c490bc2a898bea8e02ea1fdd0e6caac60c1` |
| 현재 Adapter / Snapshot / Router | Base v9.1 기준, `MIGRATION_REQUIRED` |
| 프로젝트 Registry | `skills/SKILL_REGISTRY.json`, 현재 SHA-256 `be0cb612909059426139ca9b1973ee416c1ba3505a29d69549254b19bbaf0050` |
| Google Sheet | `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw` / `오멘워드(OMENWARD)` |
| Sheet 상태 | 25개 계약 탭 확인, 현재 v9.1 `SYNCED` 기록, v9.3 병합 전 `READ_ONLY / SYNC_PENDING` |
| 주 플랫폼 | `PC_PRIMARY` |
| 후속 플랫폼 | `MOBILE_FUTURE_FEASIBILITY / NOT_IN_CURRENT_SCOPE` |
| 엔진 | Godot 4.7 계열, GDScript, Compatibility renderer |
| 보호 경로 | `data/`, `scripts/`, `scenes/`, `assets/`, `addons/`, `project.godot` |

## 2. 권한과 읽기 순서

```text
최신 사용자 결정
→ AGENTS.md
→ docs/BASE_RULES_VERSION.md
→ docs/DOCUMENTATION_MAP.md
→ 이 적용 계약
→ docs/PROJECT_CORE.md
→ docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md
→ docs/CURRENT_IMPLEMENTATION_STATUS.md
→ docs/ACTIVE_CONTEXT.md
→ docs/HANDOFF_CONTEXT.md
→ Issue #115와 연결된 감사·계획
→ 실제 코드·데이터·Scene·테스트
→ PROJECT_BASE_ADAPTER / PROJECT_SKILL_SNAPSHOT / router
→ 고정된 Base v9.3 공용 계약
```

하위 자료는 상위 정본을 자동으로 덮어쓰지 않는다. v6~v8 Prompt와 과거 `CORE_POC`·3스테이지 표현은 현재 정본에 대조해 `CURRENT`, `LEGACY_REFERENCE_ALLOWED`, `CANON_CONFLICT`, `STALE_REFERENCE` 중 하나로 판정한다.

## 3. 실행 프로필과 범위

현재 요청은 운영체계 이관이므로 다음 경계를 사용한다.

```text
Work Mode: PLAN → BUILD(운영 문서·계약만) → REVIEW
Execution Profile: RECONCILIATION_PLANNING_PROFILE
Product Code Authorization: NO
Google Sheet Write: NO
```

### 포함

- Base v9.3 Application Binding과 Vertical Slice v9 실행 계약 연결
- 정본·Context·Handoff의 중복·누락·충돌 감사
- Adapter·Snapshot·Router·Registry·공통 실행 계약 이관 계획
- 프로젝트 전용 Skill과 Base 공용 Skill의 책임 경계
- 운영 Health와 Critical Gate 재생성
- Validator·reference freshness·적대적 검토·PR 검증

### 제외

- 게임 코드·Scene·Resource·데이터·에셋 변경
- 새 게임 규칙·밸런스·콘텐츠 발명
- 제품 구현 승인 또는 Codex Build 승인
- Google Sheet 값 변경
- 모바일 구현·입력·UI·성능 목표 확정

## 4. 프로젝트 고유 책임 경계

| 구분 | Base 공용 책임 | 오멘워드 전용 책임 |
| --- | --- | --- |
| 요청·작업 계약 | Work Mode, Approval Bundle, Issue/Goal 형식 | 현재 제품 Gate와 사용자 결정 |
| 운영체계 | Adapter/Snapshot/Router/Health 계약과 검증 원리 | 프로젝트 경로·정본·보호 범위·Sheet binding |
| 게임 기획 | 컨셉·Vertical Slice·검증 프레임 | 3릴·3전선·TokenSource·비가역 커밋 규칙 |
| Godot | 공용 검증·계약 보존 원리 | `omenward-godot`의 결정론·저장·실행 경계 |
| UX·플레이테스트 | 증거 형식·접근성·성능 Gate | `omenward-core-ux`의 첫 10~15분 인과 검증 |
| 아트·시각 | 중간 시각화와 시각 QA 절차 | `omenward-art-assets`의 전장 정보·에셋·판정 동기화 |

프로젝트 전용 활성 Skill은 다음 네 개를 유지한다.

- `omenward-core-design`
- `omenward-godot`
- `omenward-core-ux`
- `omenward-art-assets`

Base 공용 Skill 본문은 프로젝트에 복제하지 않는다.

## 5. 기본 중간 시각화 시나리오

| 항목 | 값 |
| --- | --- |
| 한 화면 흐름 | 세 전선 공세 예고 + 세 원형 릴 + TokenSource 출처 + 라인 커밋 결과 |
| 플랫폼·해상도·입력 | PC, 1920×1080 출력 / 960×540 논리 화면, 키보드·마우스 우선 |
| 확인할 해석 위험 | 건물이 미래 릴을 바꾼다는 인과, 잔여 RNG와 설계 결과 구분, 비가역 배치의 비용 |
| 산출물 권한 | `DRAFT_VISUAL` 또는 Screen Brief; 정본·최종 자산·Godot 증거 아님 |

시각화는 사용자 요청 또는 P1 해석 위험이 있을 때만 수행한다.

## 6. Critical Gate

| Gate | 현재 상태 | 근거 | 다음 조건 |
| --- | --- | --- | --- |
| Base v9.3 binding | `MIGRATION_REQUIRED` | 현재 Adapter/Snapshot/Router가 v9.1 | Issue #115 이관·검증 |
| Canon consistency | `P1_BLOCKED` | CORE_POC/3스테이지 stale context | 활성 진입점 정렬 |
| Static operating integrity | `NOT_RUN_ON_V9_3` | v9.3 validator 미실행 | 생성물 재생성 후 검사 |
| Runtime | `NOT_RUN` | 제품 코드 미승인 | 후속 구현 Gate |
| Human | `NOT_RUN` | 사람 플레이 미실행 | 정확한 build/seed/session |
| Device | `NOT_RUN` | PC 실기기 검증 미실행 | 후속 제품 검증 |
| Accessibility | `NOT_RUN` | 해상도·입력 검증 미실행 | 후속 UX 검증 |
| Mobile | `NOT_IN_CURRENT_SCOPE` | 후속 플랫폼 | PC Slice 증거 후 별도 결정 |
| Sheet sync | `BLOCKED_UNTIL_MERGED_MAIN_RECHECK` | Sheet는 v9.1 SYNCED 기록 | PR 병합 후 별도 범위 승인 |

## 7. 감사 산출물

- Baseline Recovery Record: `docs/audits/OMENWARD_BASE_V9_3_APPLICATION_BINDING_PACKET_2026-07-31.md`
- Legacy Requirement Traceability: 같은 감사 Packet의 3절
- Source / Consumer / Propagation Map: 같은 감사 Packet의 4절
- Finding Ledger: 같은 감사 Packet의 5절
- Readiness / Critical Gate: 같은 감사 Packet의 6절
- Approval Bundle / Change Plan: `docs/audits/OMENWARD_BASE_V9_3_APPROVAL_BUNDLE_2026-07-31.md`
- 실행 계획: `docs/superpowers/plans/2026-07-31-base-v9-3-vertical-slice-v9-migration.md`

## 8. 상태 판정

```text
BASE_V9_3_SELECTED_BY_USER
+ VERTICAL_SLICE_V9_SELECTED_BY_USER
+ APPLICATION_BINDING_RECORDED
+ OPERATING_MIGRATION_NOT_YET_EXECUTED
+ PRODUCT_CODE_NOT_AUTHORIZED
+ SHEET_READ_ONLY
```

이 문서가 브랜치에 존재하는 것만으로 Adapter 이관, 제품 구현, 런타임·사람 검증 또는 Sheet 동기화를 완료 처리하지 않는다.
