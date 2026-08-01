---
document_role: PROJECT_V9_APPLICATION_CONTRACT
contract_source: templates/prompts/VERTICAL_SLICE_INTEGRATED_EXECUTION_PROMPT_v9.md
shared_body_policy: REFERENCE_ONLY_NO_COPY
execution_profile: RECONCILIATION_PLANNING_PROFILE
status: CURRENT_PLANNING_BINDING / MIGRATION_NOT_EXECUTED
current_audit_decision: OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1
---

# 오멘워드 Vertical Slice v9 적용 계약

## 1. 현재 바인딩

| 항목 | 현재 값 |
|---|---|
| 프로젝트 | 오멘워드 / OMENWARD |
| 저장소 | `alsdmlals4-eng/omenward` |
| 작업 PR | `#116 DRAFT / OPEN / NOT_MERGED` |
| 주 플랫폼 | `PC_PRIMARY` |
| 엔진 | Godot 4.7, GDScript, Compatibility |
| 활성 프로젝트 Base | `v9.1.0` |
| 활성 Base release | `3c158f52cfdad889970aef4d6ce6650a6fea0645` |
| 활성 Base evidence | `dd20ad3852e264d7e337e34d2cb963f71053a6cb` |
| 권장 다음 Base | `v9.3.0` |
| v9.3 release | `30ca6c7b5f93521f0eb0eed42d01437cd43c50ae` |
| v9.3 evidence | `462a86db192d23d0f386281a1eb54b0a8cbad62e` |
| v9.3 Registry SHA-256 | `9847bb2b225c776ad7916930f0f48c490bc2a898bea8e02ea1fdd0e6caac60c1` |
| Google Sheet | `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw` |
| 제품 코드 | `NOT_AUTHORIZED` |
| Codex | `BLOCKED` |

Base v9.3은 Base 저장소에서 released 상태지만 Omenward Adapter에는 아직 적용되지 않았다. Base release 상태와 프로젝트 adoption 상태를 혼동하지 않는다.

## 2. 권위 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ docs/BASE_RULES_VERSION.md
→ docs/DOCUMENTATION_MAP.md
→ docs/PROJECT_CORE.md
→ docs/audits/OMENWARD_BASE_PROJECT_SHEET_REPOSITORY_WIDE_AUDIT_2026-08-01.md
→ docs/PROJECT_CANON_DECISION_LEDGER.md
→ docs/DECISIONS_PENDING.md
→ 분야 APPROVED 계약
→ docs/CURRENT_IMPLEMENTATION_STATUS.md
→ 실제 code/data/Scene/tests
→ 프로젝트 Adapter·Registry
→ 고정된 Base 공용 계약
→ 연결 Google Sheet
```

과거 CORE_POC·3스테이지·V6 intake·독립 가중치 9칸 룰렛은 현재 제품 권위가 아니다.

## 3. 현재 실행 프로필

```text
Work Mode: PLAN
Execution Profile: RECONCILIATION_PLANNING_PROFILE
Product Code Authorization: NO
Codex Execution: BLOCKED
PR Merge: BLOCKED
Sheet Write: APPROVED_CANON_SYNC_ONLY
```

현재 포함:

- Base·프로젝트·Sheet 정본 대조.
- 승인 결정과 감사 결과 동기화.
- 화면·경제·테스트·운영 마이그레이션의 선행 계약 작성.
- Legacy/current 경계와 실패 증거 보존.

현재 제외:

- Godot 제품 코드·Scene·Resource·데이터·에셋 변경.
- Adapter·Snapshot·Router·workflow·validator의 부분 마이그레이션.
- Codex Build·PR merge.
- Runtime·기기·사람 검증 완료 주장.

## 4. 프로젝트 고유 책임 경계

| 구분 | Base 공용 책임 | Omenward 전용 책임 |
|---|---|---|
| 요청·작업 계약 | Work Mode·Approval Bundle·검증 형식 | 현재 제품 Gate와 승인 Decision |
| 운영체계 | Adapter·Registry·generated view 계약 | 프로젝트 경로·보호 대상·Sheet binding |
| 기획 | 컨셉·Vertical Slice·근거·검증 프레임 | 세 물리 릴·30노드·3라인·비가역 배치 |
| Godot | 공용 검증·계약 보존 원리 | 결정론·save·transaction·실제 Runtime |
| UX | 정보 위계·접근성·플레이테스트 | 공세→릴→배치→전투 인과·벨루 |
| 아트 | 이미지 브리프·검수 절차 | Omenward 시각 언어·화면·자산 |

프로젝트 전용 활성 Skill 4개는 유지한다.

```text
omenward-core-design
omenward-godot
omenward-core-ux
omenward-art-assets
```

Base 공용 Skill 본문을 프로젝트에 복제하지 않는다.

## 5. Base v9.3 마이그레이션 원칙

다음은 **별도 원자 패키지**에서만 수행한다.

```text
latest main·PR base 재확인
→ v9.3 release/evidence/Registry hash 검증
→ PROJECT_BASE_ADAPTER migration
→ Base route·project route 정합성
→ generated Snapshot/Health/compatibility view 전체 재생성
→ validator·tests 동시 갱신
→ protected paths diff 0
→ reference freshness·adversarial review
→ required checks 통과
```

부분적으로 Adapter만 수정하거나 generated view를 수동 편집하지 않는다.

## 6. 과거 실행 계획 판정

`docs/superpowers/plans/2026-07-31-base-v9-3-vertical-slice-v9-migration.md`는 다음 상태다.

```text
HISTORICAL_EXECUTION_CANDIDATE
DO_NOT_EXECUTE_CURRENTLY
SUPERSEDED_BY_CURRENT_AUDIT_AND_NEW_ATOMIC_PACKAGE_REQUIREMENT
```

해당 문서의 agentic execution header, 기준 main SHA, 금지됐던 Sheet write 전제와 명령을 현재 실행 권한으로 사용하지 않는다. 실제 마이그레이션은 최신 main·현재 Adapter·CI 상태를 다시 읽은 별도 Plan이 소유한다.

## 7. 현재 Critical Gate

| Gate | 상태 | 다음 조건 |
|---|---|---|
| Base v9.3 adoption | `NOT_STARTED` | 별도 원자 migration package |
| Canon consistency | `PROPAGATION_IN_PROGRESS` | Context·Ledger·Sheet read-back |
| Project Core workflow | `FAIL` | 최신 정본을 보존하는 validator package |
| GDD Sheet workflow | `FAIL` | stale Base SHA·C1 assertion 교체 |
| Latest Red tests | `SPEC_WRITTEN_NOT_EXECUTED` | 실제 test files·expected failure |
| Runtime | `NOT_RUN` | 제품 구현 승인 뒤 |
| Human | `NOT_RUN` | 실행 가능한 build 뒤 |
| Screen Board V2 | `NOT_WRITTEN` | 현재 감사·Screen Brief |

## 8. 다음 순서

```text
정본·Sheet 의미 drift 동기화
→ Screen Board V2 텍스트 명세
→ 경제·Retry·save/checkpoint Approval Bundle
→ 최신 Red test Work Order·expected-failure package
→ Base v9.3 원자 migration package
→ Codex 제품 구현 Plan
```

```text
BASE_V9_3_SELECTED_AS_NEXT_TARGET
+ APPLICATION_BINDING_CURRENT
+ ADAPTER_MIGRATION_NOT_EXECUTED
+ PRODUCT_CODE_NOT_AUTHORIZED
+ CODEX_BLOCKED
+ PR_NOT_READY
```