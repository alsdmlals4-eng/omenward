# OMENWARD Base v9.3 Application Binding 감사 Packet

- 날짜: 2026-07-31
- Issue: `#115`
- 기준 main: `774087dccc903bc9a8e2aec72eec2a2d13b216ce`
- Work Mode: `PLAN / REVIEW`
- 실행 프로필: `RECONCILIATION_PLANNING_PROFILE`
- 제품 코드 권한: `NO`
- Sheet 쓰기: `NO`

이 Packet은 Base v9.3의 필수 감사 산출물을 한 파일에 통합한다. 각 절은 독립 책임을 가지며, 후속 구현 PR은 이 Packet의 Finding과 승인 범위를 추적해야 한다.

---

## 1. Baseline Recovery Record

### 1.1 프로젝트 바인딩

| 항목 | 확인값 | 상태 |
| --- | --- | --- |
| 프로젝트 | 오멘워드(OMENWARD) | `CONFIRMED` |
| 저장소 | `alsdmlals4-eng/omenward` | `CONFIRMED` |
| 기본 브랜치 | `main` | `CONFIRMED` |
| 기준 main | `774087dccc903bc9a8e2aec72eec2a2d13b216ce` | `CONFIRMED` |
| 현재 운영 이관 | Base v9.1, PR #114 | `CURRENT_BUT_SUPERSEDED_BY_USER_REQUEST` |
| 사용자 지정 Base | Base v9.3.0 | `CONFIRMED_TARGET` |
| 사용자 지정 실행문 | Vertical Slice v9 | `CONFIRMED_TARGET` |
| 주 플랫폼 | PC | `CONFIRMED` |
| 후속 플랫폼 | 모바일 검토 예정 | `OUT_OF_CURRENT_SCOPE` |
| 엔진 | Godot 4.7 계열 / GDScript / Compatibility | `CONFIRMED_BASELINE` |

### 1.2 Base 릴리스 증거

| 항목 | 값 |
| --- | --- |
| Base repository | `alsdmlals4-eng/Base` |
| Release state | `BASE_RELEASED` |
| Release line | `v9.3.0` |
| Release commit | `30ca6c7b5f93521f0eb0eed42d01437cd43c50ae` |
| Evidence commit | `462a86db192d23d0f386281a1eb54b0a8cbad62e` |
| Registry SHA-256 | `9847bb2b225c776ad7916930f0f48c490bc2a898bea8e02ea1fdd0e6caac60c1` |
| Active execution contract | `templates/prompts/VERTICAL_SLICE_INTEGRATED_EXECUTION_PROMPT_v9.md` |

### 1.3 현재 프로젝트 운영 계약

| 경로 | 현재 역할 | 확인 상태 |
| --- | --- | --- |
| `skills/PROJECT_BASE_ADAPTER.json` | v9.1 프로젝트 통합 정본 | `MIGRATION_REQUIRED` |
| `skills/PROJECT_SKILL_SNAPSHOT.json` | v9.1 생성 route view | `REGENERATE_REQUIRED` |
| `.agents/skills/omenward-workflow-router/SKILL.md` | v9.1 thin router | `UPDATE_REQUIRED` |
| `skills/SKILL_REGISTRY.json` | 프로젝트 전용 4개 Skill 정본 | `KEEP_WITH_ID_RECONCILIATION` |
| `skills/SHARED_EXECUTION_CONTRACT.md` | 프로젝트 공통 실행 규칙 | `STALE_FIXED_ID_REFERENCES` |
| `docs/PROJECT_OPERATING_HEALTH.json` | OM/PE와 Critical Gate | `REGENERATE_REQUIRED` |
| `docs/PROJECT_OPERATING_DASHBOARD.html` | 생성 운영 view | `REGENERATE_REQUIRED` |

현재 프로젝트 Registry raw SHA-256은 `be0cb612909059426139ca9b1973ee416c1ba3505a29d69549254b19bbaf0050`, Adapter raw SHA-256은 `aba0b88f877cf916247f14f23f99db6f16d695b3689f0a2e9cc4cbca57903c49`로 기록되어 있다.

### 1.4 보호 범위

```text
data/
scripts/
scenes/
assets/
addons/
project.godot
```

`resources/`는 프로젝트 문서에서 기술 보호 범위로 반복 언급되지만 현재 Adapter의 `protected_paths`에는 없다. 실제 tracked 경로 존재와 정책 의도를 확인한 뒤 `P1` 또는 `NOT_APPLICABLE`로 판정해야 한다. 사용자 승인 없이 보호 정책을 약화하지 않는다.

### 1.5 Google Sheet Baseline

- Spreadsheet ID: `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw`
- 제목: `오멘워드(OMENWARD)`
- Locale / Time zone: `ko_KR / Asia/Seoul`
- 확인 탭 수: 25
- 핵심 탭: `00_프로젝트_허브`, `01_작업순서`, `02_현재_확정결정`, `04_누락_충돌_감사`, `05_GDD_요약`, `80_데모_버티컬슬라이스_플레이테스트`, `99_변경이력`

확인된 Sheet 상태:

- `00_프로젝트_허브`는 Base SHA `3c158f52...`와 `SYNCED`를 기록한다.
- `04_누락_충돌_감사`는 PR #114의 Base v9.1 이관을 `PASS_WITH_DECLARED_GAPS`로 기록한다.
- `05_GDD_요약`은 Base v9.1과 OM-L0 / PE-0를 기록한다.
- `99_변경이력`은 main `774087d...`와 v9.1 동기화를 마지막 완료 상태로 기록한다.

따라서 Sheet는 현재 main과 v9.1 기준으로는 일치하지만, 사용자 최신 v9.3 목표와는 아직 동기화되지 않았다. 이번 감사·이관 PR이 병합되고 새 main을 재조회하기 전에는 쓰지 않는다.

---

## 2. 현재 정본·실제 구현·증거 경계

### Confirmed

- 프로젝트 코어는 세 원형 릴, TokenSource, 세 전선, 명시적 확정, 비가역 라인 배치와 자동전투 인과다.
- 최신 Vertical Slice 방향은 별도 CORE_POC가 아니라 Full-System Vertical Slice다.
- 최신 제품 구현은 시작되지 않았고 Legacy C1·C2·C3만 과거 계약 기준 실행 증거가 있다.
- 사람·기기·접근성·최신 Runtime 증거는 `NOT_RUN`이다.
- 현재 Base 운영계약은 v9.1이다.

### Assumed / Undecided

- 모바일은 PC 버전 증거 후 검토하는 후속 플랫폼으로 해석한다. 모바일 UI·입력·성능·배포는 이번 범위에서 결정하지 않는다.
- `resources/`의 보호 경로 포함 여부는 실제 tracked 경로와 기존 정책 원본을 검사한 뒤 확정한다.
- Base route 확장은 현재 작업에 필요한 최소 집합만 추가하고 전체 Registry를 무조건 노출하지 않는다.

---

## 3. Legacy Requirement Traceability

| 과거 입력·용어 | 현재 판정 | 현행 책임 원본 | 처리 |
| --- | --- | --- | --- |
| Vertical Slice v6 master reference | `LEGACY_REFERENCE_ALLOWED` | 최신 Project Core와 Vertical Slice 계약 | 요구 누락 비교에만 사용 |
| Vertical Slice v7/v8 prompt | `SUPERSEDED_COMPATIBILITY` | Base v9 active prompt | 삭제하지 않고 이력 보존 |
| Base v9.1 project adapter | `CURRENT_UNTIL_MIGRATION_MERGE` | Issue #115의 v9.3 목표 | 병합 전 현행, 병합 후 superseded |
| 별도 CORE_POC | `STALE_REFERENCE` | Project Core: `SKIPPED_BY_USER_DECISION` | 활성 Context에서 제거, 이력에서만 보존 |
| 3스테이지 최소 Slice | `STALE_REFERENCE` | Full-System Vertical Slice | 활성 다음 작업에서 제거 |
| Legacy C1·C2·C3 | `LEGACY_REFERENCE_ALLOWED` | Current Implementation Status | 보존 seam·회귀 근거로만 사용 |
| `discipline.omenward-*` 본문 ID | `CANON_CONFLICT` | Registry `omenward-*` | 기계 ID와 본문 표기를 통일 |
| `foundation.project-intake` 등 v4 고정 ID | `STALE_REFERENCE` | Snapshot의 실제 Base route | 동적 route 이름으로 교체 |
| HTML 운영 Dashboard | `GENERATED_DERIVATIVE` | Adapter/Snapshot/Health | 수동 정본 취급 금지 |
| Sheet `SYNCED` v9.1 기록 | `CURRENT_FOR_774087D` | 병합된 main | v9.3 병합 전 수정 금지 |

---

## 4. Source / Consumer / Propagation Map

| Source | 주요 소비자 | 필요한 전파 | 재조회·검증 |
| --- | --- | --- | --- |
| Base v9.3 lock | Project Adapter, Base Rules Version, 운영 Dashboard | release/evidence/hash | Base validator와 raw hash |
| `skills/PROJECT_BASE_ADAPTER.json` | Snapshot, Router, Health, Dashboard, compatibility views | 모든 생성물 재생성 | `build_project_operating_artifacts.py --check` |
| `skills/SKILL_REGISTRY.json` | Adapter hash, Snapshot project routes, Skill docs | ID·path·status 일치 | project skill tests |
| `skills/PROJECT_SKILL_SNAPSHOT.json` | Router와 실행 Skill 선택 | effective route 전체 | generated drift 검사 |
| `AGENTS.md` | 모든 AI·Codex 콜드 스타트 | 읽기 순서와 Gate | 새 대화 복원 검사 |
| `docs/DOCUMENTATION_MAP.md` | 질문별 정본 선택 | v9 application·audit·plan 링크 | 링크·권한 검사 |
| `docs/PROJECT_CORE.md` | Context, Handoff, GDD 요약, Issue | CORE_POC 생략·Full Slice | stale term scan |
| `docs/ACTIVE_CONTEXT.md` | 현재 작업·Codex 인계 | 다음 Gate 통일 | Handoff와 비교 |
| `docs/HANDOFF_CONTEXT.md` | 새 작업자 인계 | 현재 Gate·미검증 통일 | Active Context와 비교 |
| `skills/SHARED_EXECUTION_CONTRACT.md` | 프로젝트 전용 Skill 4개 | 고정 legacy ID 제거 | Registry/Snapshot 대조 |
| `docs/PROJECT_OPERATING_HEALTH.json` | Dashboard, 완료 보고 | OM/PE/Gate 증거 | 생성물 check |
| GitHub merged main | Google Sheet | 허용 탭·range만 후속 동기화 | 쓰기 전후 재조회 |

Untouched consumer 검토 대상:

- `README.md`, `START_HERE` 계열
- `docs/BASE_SHARED_SKILL_INTEGRATION.md`
- `docs/base/START_HERE_SKILLS.md`
- Archive manifest와 compatibility views
- Python tests와 GitHub Actions
- Sheet Workbook 계약 문서

---

## 5. Duplicate·Omission·Conflict Finding Ledger

| ID | 심각도 | Finding | 근거 | 판정 | 처리 |
| --- | --- | --- | --- | --- | --- |
| V9-F001 | P1 | Adapter/Snapshot/Router가 v9.1에 고정 | 실제 파일 | `MUST_FIX` | Base v9.3 pin으로 생성·검증 |
| V9-F002 | P1 | Active Context/Handoff에 CORE_POC·3스테이지 흐름 잔존 | 활성 진입점 | `MUST_FIX` | Full-System Slice Gate로 정렬 |
| V9-F003 | P1 | AGENTS 읽기 순서가 최신 Documentation Map보다 구형 V2 문서를 앞세움 | AGENTS vs Map | `MUST_FIX` | v9 application 포함 순서로 수정 |
| V9-F004 | P1 | Registry ID `omenward-*`와 Skill 본문 `discipline.omenward-*` 불일치 | Registry/4개 Skill | `MUST_FIX` | `omenward-*`로 통일 권장 |
| V9-F005 | P1 | Shared Execution Contract가 존재하지 않는 legacy Foundation/Specialist ID 호출 | 공통 계약 | `MUST_FIX` | Snapshot effective route 기반으로 교체 |
| V9-F006 | P1 | v9 실행에 필요한 Vertical Slice·적대적 검토 Base route가 Snapshot에 없음 | Snapshot/Base Registry | `MUST_FIX` | 최소 route 추가 후 재생성 |
| V9-F007 | P1 | Sheet가 v9.1 `SYNCED`를 기록 | 실제 Sheet | `EXPECTED_DRIFT` | 병합 전 읽기 전용, 병합 후 별도 동기화 |
| V9-F008 | P2 | Health evidence 배열이 Legacy 증거와 연결되지 않음 | Health/Implementation Status | `SHOULD_FIX` | OM/PE 분리 유지하며 근거 링크 |
| V9-F009 | P2 | `resources/` 보호 범위 문서와 Adapter 차이 | 문서/Adapter | `BLOCKED_UNVERIFIED` | tracked 경로·정책 원본 검사 |
| V9-F010 | P2 | v9.1 사람용 통합 문서·Dashboard·호환 view가 v9.3 이후 stale 가능 | 다중 소비자 | `SHOULD_FIX` | source-consumer 전파 검사 |
| V9-F011 | P3 | 모바일 후속 계획이 구조화된 Gate로 없음 | 사용자 최신 지시 | `DEFER` | PC Slice 증거 후 별도 Issue |

현재 P0는 확인되지 않았다. P1은 구현 PR에서 모두 해소되거나 명시적 차단 상태로 남아야 한다.

---

## 6. Vertical Slice Readiness + Critical Gate

### 플레이어 약속

> 플레이어가 예고된 세 전선의 위협을 읽고, 건물과 TokenSource로 미래 릴 구조를 설계한 뒤, 남은 무작위성을 감수해 결과를 한 전선에 비가역적으로 커밋하고 그 결과를 다음 설계에 사용한다.

### 현재 준비도

| 축 | 상태 | 설명 |
| --- | --- | --- |
| 제품 정체성 | `CURRENT` | Project Core가 소유 |
| 통합 설계 | `USER_APPROVED_PLAN` | Full-System Slice 계약 존재 |
| 최신 제품 구현 | `NOT_STARTED` | Legacy 증거와 분리 |
| 운영체계 v9.3 | `MIGRATION_REQUIRED` | Issue #115 |
| 정적 계약 | `NOT_RUN_ON_V9_3` | 생성·검증 전 |
| Runtime | `NOT_RUN` | 제품 코드 미승인 |
| 사람 검증 | `NOT_RUN` | 합성 검토만 존재 |
| PC 가독성·입력 | `NOT_RUN` | 실제 build 증거 없음 |
| 모바일 | `NOT_IN_CURRENT_SCOPE` | 후속 가능성만 확인 |
| Sheet | `READ_ONLY_SYNC_PENDING` | v9.1 main 기준 데이터 |

### Critical Gate 판정

```text
OPERATING_MIGRATION_GATE: BLOCKED_BY_P1_FINDINGS
PRODUCT_BUILD_GATE: NOT_AUTHORIZED
VERTICAL_SLICE_PROVEN: NO
CORE_LOCK: NO
SHEET_SYNC_GATE: BLOCKED_UNTIL_MERGED_MAIN_RECHECK
MOBILE_GATE: DEFERRED
```

---

## 7. Approval Bundle 요약

### 승인된 목표

Base v9.3과 Vertical Slice v9를 Omenward 운영체계의 새 기준으로 채택한다.

### 최소 변경

- 운영 계약·정본 진입점·Skill routing·생성물·검증기만 변경한다.
- 프로젝트 전용 4개 Skill과 제품 코어는 보존한다.
- stale CORE_POC·3스테이지·v4 fixed route 표현을 활성 경로에서 제거한다.

### 비목표

- 제품 코드·Scene·데이터·에셋·밸런스 변경
- 모바일 구현
- Sheet 쓰기
- 사람·기기·Runtime 완료 주장

### 수용 기준

1. Base v9.3 release/evidence/hash 일치.
2. Adapter → Snapshot → Router → Health 생성 계보 일치.
3. 프로젝트 Skill 4개와 Base route에 orphan·duplicate·cycle 없음.
4. 모든 활성 진입점이 같은 제품 Gate와 다음 작업을 반환.
5. 보호 경로 변경 0건.
6. v9.3 static validation 통과.
7. 독립 적대적 검토에서 미해결 P0/P1 없음.
8. Sheet는 변경하지 않고 후속 동기화 조건만 기록.

### 롤백

- 기준 main `774087dccc903bc9a8e2aec72eec2a2d13b216ce`로 브랜치 폐기 가능.
- v9.1 Adapter와 생성물은 Git 이력에 보존한다.
- 생성물 실패 시 수동 부분 채택하지 않고 Adapter 수정 후 전체 재생성한다.

---

## 8. 최종 감사 판정

```text
APPLICATION_BINDING: RECORDED
BASE_V9_3_RELEASE: CONFIRMED
SHEET_STRUCTURE: CONFIRMED_READ_ONLY
CANON_CONFLICT: PRESENT
OPERATING_MIGRATION: REQUIRED
PRODUCT_CODE_CHANGE: FORBIDDEN_IN_THIS_ISSUE
READY_FOR_CODEX_OPERATING_MIGRATION_PLAN: YES
READY_FOR_PRODUCT_BUILD: NO
```
