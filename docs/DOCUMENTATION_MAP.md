# 오멘워드 Documentation Map

- 갱신일: `2026-08-01`
- Work Mode: `PLAN / PLANNING_ONLY_PROFILE`
- 현재 제품: `LEGACY_PROTOTYPE`
- 최신 Vertical Slice: `APPROVED / NOT_IMPLEMENTED`
- 제품 코드·Codex: `NOT_AUTHORIZED / BLOCKED`
- PR: `#116 DRAFT / OPEN / NOT_MERGED`
- CI: `BASE_ADOPTION_PASS / PROJECT_CORE_FAIL / GDD_SHEET_FAIL`
- 이미지: `PREVIOUS_BATCH_REJECTED / NEW_GENERATION_BLOCKED`
- 활성 Base: `v9.1`
- 권장 다음 Base: `v9.3 / SEPARATE_ATOMIC_MIGRATION`

이 문서는 질문별 책임 원본을 선택하는 권위 라우터다. 최신 사용자 지시와 현재 책임 원본을 우선하며 Legacy 구현·폐기 화면 보드·생성 실패 이미지·구형 실행 계획을 활성 제품 정본으로 사용하지 않는다.

## 1. 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ DOCUMENTATION_MAP.md
→ PROJECT_CORE.md
→ Project Understanding Gate
→ Base·프로젝트·Sheet 전수 감사
→ 질문 분야의 최신 APPROVED 계약
→ PROJECT_CANON_DECISION_LEDGER.md
→ DECISIONS_PENDING.md
→ CURRENT_IMPLEMENTATION_STATUS.md
→ 실제 Scene·Script·Resource·data·tests
→ 연결 Google Sheet
→ 사실표·충돌 원장·적대적 검토
```

## 2. 필수 작업 게이트

| 질문 | 책임 원본 | 권한 |
|---|---|---|
| 프로젝트 이해·누락 방지 | `operations/PROJECT_UNDERSTANDING_AND_OMISSION_PREVENTION_GATE_2026-08-01.md` | `CURRENT_MANDATORY_PREFLIGHT` |
| Base·프로젝트·Sheet 전체 상태 | `audits/OMENWARD_BASE_PROJECT_SHEET_REPOSITORY_WIDE_AUDIT_2026-08-01.md` | `CURRENT_REPOSITORY_WIDE_AUDIT` |
| 종합 무결성·기존 이미지 실패 | `reviews/OMENWARD_COMPREHENSIVE_PROJECT_INTEGRITY_REVIEW_2026-08-01.md` | `CURRENT_REVIEW_EVIDENCE` |
| 승인 결정 동기화 | `operations/CANON_SYNC_PROTOCOL_2026-07-31.md` | `CURRENT_PROJECT_WORK_RULE` |
| 새 시스템·핵심 규칙·UX | `operations/BENCHMARK_FIRST_PLANNING_RULE_2026-07-31.md` | `CURRENT_PROJECT_WORK_RULE` |
| 최신 구현 전 Red 계약 | `testing/LATEST_VERTICAL_SLICE_RED_TEST_SPEC_2026-08-01.md` | `SPEC_WRITTEN_NOT_EXECUTED` |
| Legacy 테스트 마이그레이션 | `testing/LEGACY_TEST_PRESERVE_REPLACE_RETIRE_MATRIX_2026-08-01.md` | `CURRENT_MIGRATION_TEST_AUTHORITY` |
| Base v9.3 프로젝트 적용 | `operations/VERTICAL_SLICE_V9_APPLICATION.md` | `CURRENT_PLANNING_BINDING / MIGRATION_NOT_EXECUTED` |

열린 P1은 관련 구현·이미지 생성·PR ready/merge를 차단한다.

## 3. 현재 활성 책임 원본

| 질문 | 책임 원본 | 권한 |
|---|---|---|
| 제품 정체성·범위·불변 조건 | `PROJECT_CORE.md` | `CURRENT_CORE_AUTHORITY` |
| 전체 시스템 관계 | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `CURRENT_USER_APPROVED_PLAN` |
| 전장 토폴로지·건설 노드 | `design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_CONSTRUCTION_NODE_INVARIANTS_2026-08-01.md` | `CURRENT_USER_CONFIRMED_CANON` |
| 룰렛 물리 구조·판정·이동 | `design/APPROVED_ROULETTE_CORE_RULES.md` | `CURRENT_APPROVED_DETAIL` |
| MapRun·Stage·접전지 | `design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md` | `APPROVED_DETAIL / LATEST_OVERRIDES_APPLY` |
| 런 시간·20 Stage·4막 | 2026-07-31 Run Duration·20 Stage 계약 | `CURRENT_USER_APPROVED_PLAN` |
| 콘텐츠 Manifest·미션 | `design/APPROVED_VERTICAL_SLICE_CONTENT_MANIFEST_AND_MISSION_CARD_POOL_2026-07-31.md` | `CURRENT_USER_APPROVED_PLAN` |
| 위험 Stage·보스 | `design/APPROVED_VERTICAL_SLICE_DANGER_STAGE_AND_BOSS_PACKAGE_2026-07-31.md` | `EXACT_VALUES_PENDING` |
| 패배·유료 재시도 | `design/APPROVED_VERTICAL_SLICE_DEFEAT_AND_PAID_RETRY_PRINCIPLE_2026-07-31.md` | `EXACT_COSTS_PENDING` |
| 안내자 벨루 | `design/APPROVED_BELU_GUIDE_IDENTITY_AND_NAMING_CONTRACT_2026-08-01.md` | `CURRENT_USER_CONFIRMED_CANON` |
| 최신 Red 테스트 | `testing/LATEST_VERTICAL_SLICE_RED_TEST_SPEC_2026-08-01.md` | `TEST_FILES_NOT_CREATED` |
| Legacy 테스트 판정 | `testing/LEGACY_TEST_PRESERVE_REPLACE_RETIRE_MATRIX_2026-08-01.md` | `CURRENT_MIGRATION_TEST_AUTHORITY` |
| 전체 감사·다음 순서 | `audits/OMENWARD_BASE_PROJECT_SHEET_REPOSITORY_WIDE_AUDIT_2026-08-01.md` | `CURRENT_REPOSITORY_WIDE_AUDIT` |
| 현재 상태 압축 | `ACTIVE_CONTEXT.md` | `CURRENT_ACTIVE_CONTEXT` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF` |
| Decision·GitHub/Sheet 위치 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_LEDGER` |
| 미확정 수치·콘텐츠 | `DECISIONS_PENDING.md` | `PENDING_ONLY` |
| 실제 구현·Legacy 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 연결 Google Sheet | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `USER_FACING_GDD_WORKSPACE_CONTRACT` |

## 4. Base 라우팅

```text
CURRENT_PROJECT_BASE = v9.1
NEXT_RECOMMENDED_BASE = v9.3
BASE_V9_3_RELEASED_IN_BASE != BASE_V9_3_ADOPTED_BY_OMENWARD
```

- 현재 Adapter·Snapshot·Router·validator는 v9.1 기준이다.
- Base v9.3은 별도 원자 migration package에서만 적용한다.
- 과거 `docs/superpowers/plans/2026-07-31-base-v9-3-vertical-slice-v9-migration.md`는 `HISTORICAL_EXECUTION_CANDIDATE / DO_NOT_EXECUTE_CURRENTLY`다.

## 5. 벨루 명칭

```text
CANONICAL_NAME_KO = 벨루
CANONICAL_NAME_EN = Belu
HISTORICAL_ALIAS = 율비
```

신규 UI·대사·에셋·데이터·파일명은 `벨루 / Belu / belu`를 사용한다.

## 6. 비주얼·화면 작업

| 질문 | 책임 원본 | 상태 |
|---|---|---|
| 시각자료 Router | `images/VISUAL_REFERENCE_INDEX.md` | `CURRENT_VISUAL_REFERENCE_ROUTER` |
| 중간 검수 절차 | `reviews/APPROVED_MIDPOINT_IMAGE_REVIEW_GATE_2026-07-31.md` | `WORKFLOW_RETAINED` |
| 과거 Screen Board V1 | `design/OMENWARD_VISUAL_SITUATIONAL_INGAME_SCREEN_SPEC_BOARD_2026-07-31.md` | `REJECTED_EVIDENCE / DO_NOT_REUSE` |
| Screen Board V2 | 미작성 | `NEXT_PLANNING_DELIVERABLE` |

다음 작업은 이미지 생성이 아니라 화면별 독립 브리프와 Screen Board V2 텍스트 명세다.

```text
현재 감사
→ Topology·Roulette·Belu·Implementation Status
→ 메인/Stage 준비/전투/정산 기본 화면 브리프
→ 위험/패배 파생 화면 브리프
→ Screen Board V2 텍스트 명세
→ 사용자 시각 구조 검수
→ 이미지 생성
```

## 7. 현재 Decision

| Decision ID | 결정 | 상태 |
|---|---|---|
| `OMW-DEC-20260731-CONTENT-MANIFEST-V1` | 콘텐츠 Manifest·미션 | `USER_APPROVED_PLAN` |
| `OMW-DEC-20260731-CANON-SYNC-V1` | GitHub·Sheet 동기화 | `CURRENT_WORK_RULE` |
| `OMW-DEC-20260731-DEFEAT-RETRY-V1` | 제품 유료 Retry | `EXACT_COSTS_PENDING` |
| `OMW-DEC-20260731-DANGER-BOSS-V1` | 위험 Stage·보스 | `EXACT_VALUES_PENDING` |
| `OMW-DEC-20260731-MID-IMAGE-REVIEW-V1` | 이미지 검수 절차 | `WORKFLOW_RETAINED / BATCH_REJECTED` |
| `OMW-DEC-20260731-VISUAL-SCREEN-BOARD-V1` | 과거 화면 보드 | `REJECTED_EVIDENCE` |
| `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1` | 사실표·6/3/0=30 | `CURRENT_WORK_RULE` |
| `OMW-DEC-20260801-BELU-IDENTITY-V1` | 벨루 명칭 | `CURRENT_CANON` |
| `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1` | Red 명세·Legacy 판정 | `SPEC_WRITTEN_NOT_EXECUTED` |
| `OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1` | Base·GitHub·25개 Sheet·CI 전수 감사 | `CURRENT_REPOSITORY_WIDE_AUDIT` |

## 8. 상태 판정

```text
CURRENT_CANON != CURRENT_IMPLEMENTATION
LEGACY_PROVEN != LATEST_PROVEN
APPROVED_STRUCTURE != EXACT_VALUES_APPROVED
RED_SPEC_WRITTEN != RED_TESTS_CREATED
BASE_RELEASED != PROJECT_ADOPTED
SYNCED_TO_PR_HEAD != SYNCED_TO_MAIN
DRAFT_PR != READY_FOR_REVIEW
CI_PARTIAL_FAILURE != VALIDATED
GENERATED_IMAGE != APPROVED_ASSET
```

## 9. Legacy 해석

| Legacy | 보존 | 최신 교체 |
|---|---|---|
| C1 룰렛 | 중앙 판정·완성선·금화 resolver | 세 물리 릴·TokenInstance·snapshot·이동 |
| C2 전장 | 3라인·구조 피해·승패 | 30노드·고정시간 점령·최신 거래 |
| C3 UX | read-only snapshot·원인 보고 | 제품 화면·물리 릴·30노드 정보 |
| Retry | 개발용 same-stage restart | 제품 영구재화 1회 Retry |
| PR #92/#97 | 역사 승인·기술 계보 | 최신 exact building/economy 권위 아님 |

## 10. 다음 작업

```text
1. 현재 정본·Sheet read-back과 PR body 동기화
2. Screen Board V2 화면별 독립 브리프·텍스트 명세
3. 경제·Retry·save/checkpoint Approval Bundle·시뮬레이션 계약
4. 실제 최신 Red test Work Order·expected-failure package
5. 별도 Base v9.3 Adapter 원자 migration package
6. 사용자 승인 Codex 제품 구현 Plan
```

제품 코드 변경, Codex 실행, 새 이미지 생성, PR ready/merge는 현재 승인 범위가 아니다.