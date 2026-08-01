# 오멘워드 기획 정본 결정 원장

- 갱신일: `2026-08-01`
- 상태: `CURRENT_DECISION_LEDGER / PLANNING_ONLY / SYNC_VERIFIED`
- 동기화 프로토콜: `docs/operations/CANON_SYNC_PROTOCOL_2026-07-31.md`
- 연결 Sheet ID: `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw`
- 제품 코드·Codex·병합: `NONE / BLOCKED / NOT_AUTHORIZED`

이 원장은 주요 승인 결정, 폐기·대체 상태, GitHub 책임 경로와 Google Sheet 위치를 같은 Decision ID로 연결한다. 상세 규칙은 각 책임 원본이 소유한다.

## 1. 현재 결정 요약

| Decision ID | 상태 | 요약 |
|---|---|---|
| `OMW-DEC-20260731-CONTENT-MANIFEST-V1` | `USER_APPROVED_PLAN` | 전장 1·4막·Stage 20·공세 8·위험 4·보스 3·미션 12 |
| `OMW-DEC-20260731-CANON-SYNC-V1` | `CURRENT_PROJECT_WORK_RULE` | 승인 즉시 GitHub·Sheet 동일 ID 동기화 |
| `OMW-DEC-20260731-DEFEAT-RETRY-V1` | `EXACT_COSTS_PENDING` | Stage 5 이후 MapRun당 최대 1회 제품 유료 Retry |
| `OMW-DEC-20260731-DANGER-BOSS-V1` | `EXACT_VALUES_PENDING` | Stage 5·10·15·20 위험 공세·보스 |
| `OMW-DEC-20260731-MID-IMAGE-REVIEW-V1` | `WORKFLOW_RETAINED / BATCH_REJECTED` | 화면별 중간 검수 절차 |
| `OMW-DEC-20260731-VISUAL-SCREEN-BOARD-V1` | `REJECTED_EVIDENCE` | 잘못된 Screen Board V1 재사용 금지 |
| `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1` | `CURRENT_WORK_RULE / CURRENT_CANON` | 사실표·충돌 원장·전장 `6/3/0=30` |
| `OMW-DEC-20260801-BELU-IDENTITY-V1` | `CURRENT_CANON` | 정본명 벨루, 율비는 역사 별칭 |
| `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1` | `SPEC_WRITTEN_NOT_EXECUTED` | 최신 Red 명세·Legacy 테스트 판정 |
| `OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1` | `CURRENT_REPOSITORY_WIDE_AUDIT / SYNC_VERIFIED` | Base·GitHub·25개 Sheet·실제 코드·CI 전수 감사와 다음 순서 |

## 2. 최신 Red 테스트 결정

```yaml
decision_id: OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1
status: SPEC_WRITTEN_NOT_EXECUTED
authority_commit: 1aba7e9f5e3fbc4e93d0291a4a06f204d196ab7e
authority_paths:
  - docs/testing/LATEST_VERTICAL_SLICE_RED_TEST_SPEC_2026-08-01.md
  - docs/testing/LEGACY_TEST_PRESERVE_REPLACE_RETIRE_MATRIX_2026-08-01.md
latest_test_files: NOT_CREATED
expected_red_execution: NOT_RUN
product_code: UNCHANGED
sheet_sync_status: SYNCED_TO_PR_HEAD
```

## 3. Base·프로젝트·Sheet 전수 감사 결정

```yaml
decision_id: OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1
status: CURRENT_REPOSITORY_WIDE_AUDIT / RECOMMENDED_DECISIONS_APPROVED / SYNC_VERIFIED
authority_commit: 6882777ac42d30a8d25e621b98f9731fbe8537be
authority_path: docs/audits/OMENWARD_BASE_PROJECT_SHEET_REPOSITORY_WIDE_AUDIT_2026-08-01.md
verification_commit: e46ed794bcb5e90924362464bc3abff92deb86d1
verification_path: docs/audits/OMENWARD_BASE_PROJECT_SHEET_AUDIT_SYNC_VERIFICATION_2026-08-01.md
github_pr: 116
github_merge_state: NOT_MERGED
active_project_base: 9.1.0
recommended_next_base: 9.3.0
base_v9_3_adoption: SEPARATE_ATOMIC_PACKAGE_REQUIRED
product_code: UNCHANGED
codex: BLOCKED
runtime: NOT_RUN
human_qa: NOT_RUN
last_observed_ci:
  base_v9_adoption: PASS
  project_core_documentation: FAIL
  gdd_sheet_adoption: FAIL
sheet_ranges:
  - 00_프로젝트_허브!E1:L2
  - 01_작업순서!A2:J6
  - 02_현재_확정결정!A14:L15
  - 04_누락_충돌_감사!A14:H18
  - 05_GDD_요약!A1:J8
  - 10_제품방향!A1:F4
  - 12_핵심루프!A1:J5
  - 15_조작_게임규칙!A1:J3
  - 40_핵심시스템_메인콘텐츠!A1:K5
  - 41_성장_경제!A1:I4
  - 50_메인콘텐츠!A1:J5
  - 99_변경이력!A14:H15
sheet_sync_status: CANON_AND_SHEET_READBACK_PASS
```

### 승인된 권장안

```text
CURRENT_PROJECT_BASE = v9.1
NEXT_RECOMMENDED_BASE = v9.3
V9_3_MIGRATION = SEPARATE_ATOMIC_PACKAGE
PR116 = DRAFT / PLANNING_CANON_AND_AUDIT / NOT_READY
PR92_PR97_EXACT_VALUES = HISTORICAL_APPROVED_SOURCE
LATEST_BUILDING_EXACT_VALUES = PENDING
NEXT_VISUAL_DELIVERABLE = SCREEN_BOARD_V2_TEXT_SPEC
PRODUCT_CODE = NOT_AUTHORIZED
```

### 감사로 확인된 P1

- Active Context·Handoff stale 상태: `VERIFIED_FIXED`.
- Sheet Base SHA·authority commit·PR head 의미 혼합: `VERIFIED_FIXED`.
- 역사 PR #92/#97의 current exact 권위 오인: `VERIFIED_FIXED_FOR_AUDITED_RANGES`.
- Project Core Documentation workflow 실패: `OPEN_P1`.
- GDD Sheet Adoption workflow 실패: `OPEN_P1`.
- Base v9.3 실제 Adapter migration 미실행: `OPEN_P1`.
- 과거 Base v9.3 실행 계획은 `HISTORICAL_EXECUTION_CANDIDATE / DO_NOT_EXECUTE_CURRENTLY`.

## 4. 벨루 결정

```yaml
decision_id: OMW-DEC-20260801-BELU-IDENTITY-V1
status: CURRENT_CANON
canonical_name_ko: 벨루
canonical_name_en: Belu
historical_alias_ko: 율비
identity_relation: SAME_CHARACTER
product_asset_approval: PENDING
```

## 5. 프로젝트 상태

```text
OPEN_P0: 0
OPEN_P1: CI_FAILURES / V9_3_MIGRATION_NOT_EXECUTED / IMPLEMENTATION_PLANNING_PENDING
CURRENT_PRODUCT: LEGACY_PROTOTYPE
LATEST_VERTICAL_SLICE: APPROVED_NOT_IMPLEMENTED
VISUAL_SCREEN_BOARD_V1: REJECTED_EVIDENCE
LATEST_RED_SPEC: WRITTEN
LATEST_RED_TEST_FILES: NOT_CREATED
PRODUCT_CODE: NOT_AUTHORIZED
CODEX: BLOCKED
RUNTIME_AND_HUMAN_QA: NOT_RUN
PR_READY: NO
PR_MERGE: BLOCKED
CANON_AND_SHEET_SYNC: PASS
```

과거 `PR97-VS`, `PR92-BUILDING`, `F-30`, `OMENWARD-EVP-001`, C1/C2/C3 proof는 삭제하지 않고 `HISTORICAL_APPROVED_SOURCE`, `LEGACY_PROVEN`, `HISTORICAL_EVIDENCE`로 분류한다.

## 6. 다음 작업 게이트

```text
Screen Board V2 화면별 독립 브리프·텍스트 명세
→ 경제·Retry·save/checkpoint Approval Bundle·시뮬레이션 계약
→ 실제 최신 Red test Work Order·expected-failure package
→ 별도 Base v9.3 Adapter 원자 migration package
→ CI validator Green
→ 사용자 승인 Codex 제품 구현 Plan
```

최신 Red expected-failure 증거와 관련 P1 해소 없이 제품 구현을 시작하지 않는다.