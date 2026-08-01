# 오멘워드 기획 정본 결정 원장

- 갱신일: `2026-08-01`
- 상태: `CURRENT_DECISION_LEDGER / PLANNING_ONLY / SYNC_VERIFIED`
- 동기화 프로토콜: `docs/operations/CANON_SYNC_PROTOCOL_2026-07-31.md`
- 누락 방지 게이트: `docs/operations/PROJECT_UNDERSTANDING_AND_OMISSION_PREVENTION_GATE_2026-08-01.md`
- 연결 Sheet ID: `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw`
- 제품 코드·Codex·병합: `NONE / BLOCKED / NOT_AUTHORIZED`

이 원장은 주요 승인 결정, 폐기·대체 상태, GitHub 권위 경로와 Google Sheet 위치를 같은 Decision ID로 연결한다. 현재 브랜치 head는 PR metadata가 소유한다.

## 1. 현재 결정 요약

| Decision ID | 상태 | 요약 |
|---|---|---|
| `OMW-DEC-20260731-CONTENT-MANIFEST-V1` | `USER_APPROVED_PLAN` | 전장 1개·4막, Stage 20, 공세 8, 위험 4, 보스 3, 미션 12 |
| `OMW-DEC-20260731-CANON-SYNC-V1` | `CURRENT_PROJECT_WORK_RULE` | GitHub·Sheet 동일 Decision ID 동기화 |
| `OMW-DEC-20260731-DEFEAT-RETRY-V1` | `USER_APPROVED_DETAIL / EXACT_COSTS_PENDING` | Stage 5 이후 MapRun당 1회 유료 재시도 |
| `OMW-DEC-20260731-DANGER-BOSS-V1` | `USER_APPROVED_PLAN / EXACT_VALUES_PENDING` | Stage 5·10·15·20 위험 공세·보스 |
| `OMW-DEC-20260731-MID-IMAGE-REVIEW-V1` | `WORKFLOW_RETAINED / CURRENT_BATCH_REJECTED` | 화면별 이미지 검수 절차 유지 |
| `OMW-DEC-20260731-VISUAL-SCREEN-BOARD-V1` | `REJECTED_EVIDENCE / SUPERSEDED` | 잘못된 화면 보드 V1 재사용 금지 |
| `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1` | `CURRENT_PROJECT_WORK_RULE / CURRENT_USER_CONFIRMED_CANON` | 사실표·충돌 원장·전장 `6/3/0=30` |
| `OMW-DEC-20260801-BELU-IDENTITY-V1` | `CURRENT_USER_CONFIRMED_CANON` | 벨루·율비 동일 인물, 정본명 벨루 |
| `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1` | `CURRENT_IMPLEMENTATION_GATE / SPEC_WRITTEN_NOT_EXECUTED` | 최신 계약 Red 명세와 Legacy 테스트 보존·교체·폐기 판정 |

## 2. 벨루 정체성 결정

```yaml
decision_id: OMW-DEC-20260801-BELU-IDENTITY-V1
status: CURRENT_USER_CONFIRMED_CANON
canonical_name_ko: 벨루
canonical_name_en: Belu
historical_alias_ko: 율비
identity_relation: SAME_CHARACTER
github_authority_commit: 214cedf259ee9ad848117a33dd70d62c4293bf27
github_pr: 116
github_merge_state: NOT_MERGED
sheet_sync_status: SYNCED_TO_PR_HEAD
verification_evidence_commit: 5ba10618339f71336a63dee1435a53ead7014080
```

- 신규 UI·대사·에셋·데이터·파일명은 `벨루 / Belu / belu`를 사용한다.
- `율비 / Yulbi`는 과거 시안 파일명·변경 이력의 역사 별칭으로만 보존한다.
- 벨루는 설명·경고·결과 반응을 제공하되 전술 결정을 대신하지 않는다.

## 3. 최신 계약 Red 테스트 결정

```yaml
decision_id: OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1
status: CURRENT_IMPLEMENTATION_GATE / SPEC_WRITTEN_NOT_EXECUTED
authority_commit: 1aba7e9f5e3fbc4e93d0291a4a06f204d196ab7e
github_pr: 116
github_merge_state: NOT_MERGED
github_authority_paths:
  - docs/testing/LATEST_VERTICAL_SLICE_RED_TEST_SPEC_2026-08-01.md
  - docs/testing/LEGACY_TEST_PRESERVE_REPLACE_RETIRE_MATRIX_2026-08-01.md
  - docs/DECISIONS_PENDING.md
sheet_ranges:
  - 00_프로젝트_허브!E2:K2
  - 01_작업순서!A5:J5
  - 02_현재_확정결정!A14:L14
  - 04_누락_충돌_감사!A14:H14
  - 80_데모_버티컬슬라이스_플레이테스트!A9:L9
  - 99_변경이력!A14:H14
sheet_sync_status: SYNCED_TO_PR_HEAD
verification_result: PASS_FOR_SPEC_AND_SHEET_SYNC
latest_test_files: NOT_CREATED
expected_red_execution: NOT_RUN
product_code: UNCHANGED
```

정본화된 범위:

- 본진 6/진영·중간 거점 6곳×3·접전지 0·전체 30노드.
- 왼쪽·중앙·오른쪽 세 물리 릴, TokenInstance, 영구 가로 이동, immutable SpinSnapshot.
- 유닛 수·Tier·등급과 무관한 고정시간 점령.
- 금고·농장·타워·병영·지휘소 5개 건물 가족.
- PendingReward·보관·판매·한 라인 비가역 배치.
- Stage 5 이후 MapRun당 최대 1회 제품 유료 재시도와 개발 재시도 분리.
- Legacy 테스트의 `PRESERVE / PRESERVE_SEAM / SPLIT_REPLACE / RETIRE_AS_CURRENT_GATE` 판정.

아직 완료되지 않은 것:

- 실제 `tests/headless/latest/**`, `tests/python/latest/**` 파일.
- 현재 Legacy에서 의도한 계약 미구현 이유로 실패하는 Red 실행 증거.
- CI expected-failure wiring.
- 사용자 승인 Codex 구현 Plan.

## 4. 프로젝트 무결성 상태

```text
OPEN_P0: 0
BELU_IDENTITY_CONFLICT: VERIFIED_FIXED
PROJECT_CORE_REFRESH: VERIFIED
HISTORICAL_CURRENT_SHEET_CLASSIFICATION: VERIFIED
VISUAL_SCREEN_BOARD_V1: REJECTED_EVIDENCE
GENERATED_IMAGES: REJECTED_EVIDENCE
VISUAL_BINARY_MIGRATION: PENDING
LATEST_CONTRACT_RED_TEST_SPEC: WRITTEN
LATEST_CONTRACT_TEST_FILES: NOT_CREATED
LATEST_CONTRACT_RED_EXECUTION: NOT_RUN
PRODUCT_CODE: NOT_AUTHORIZED
CODEX_EXECUTION: BLOCKED
RUNTIME_AND_HUMAN_QA: NOT_RUN
```

과거 Sheet 행 `PR97-VS`, `PR92-BUILDING`, `F-30`, `OMENWARD-EVP-001`은 삭제하지 않고 `HISTORICAL_APPROVED_SOURCE`, `LEGACY_PROVEN`, `HISTORICAL_EVIDENCE`로 분류한다. 현재 정본 권한으로 사용하지 않는다.

## 5. 비주얼 결정 상태

```text
MID_IMAGE_REVIEW: WORKFLOW_RETAINED / CURRENT_BATCH_REJECTED
VISUAL_SCREEN_BOARD_V1: REJECTED_EVIDENCE / DO_NOT_REUSE
OM-IMG-005_TO_010: REJECTED / RESET_REQUIRED
NEW_IMAGE_GENERATION: BLOCKED_PENDING_SCREEN_BRIEF_APPROVAL
```

## 6. Sheet 재검증 결과

```text
RED_DECISION_ID_MATCH: PASS
RED_AUTHORITY_COMMIT_MATCH: PASS
RED_SPEC_STATE: SPEC_WRITTEN_NOT_EXECUTED
LEGACY_TEST_CLASSIFICATION: PASS
EXISTING_FORMATS_PRESERVED: PASS
SYNC_STATE: SYNCED_TO_PR_HEAD
```

## 7. 다음 작업 게이트

```text
Base 전체 현행 스킬·작업 구조 분석
→ Omenward GitHub·Google Sheet 전수 진행도 감사
→ 적대적 검토와 남은 기획 보완
→ 같은 Decision ID로 정본·Sheet 동기화
→ 화면 명세 보드 V2
→ 실제 최신 Red 테스트 작성·실행 Work Order
→ 사용자 승인 Codex 구현 Plan
```

실제 최신 Red 테스트와 expected-failure 증거 없이 Codex 제품 구현을 시작하지 않는다.
