# 오멘워드 기획 정본 결정 원장

- 갱신일: `2026-08-01`
- 상태: `CURRENT_DECISION_LEDGER / PLANNING_ONLY`
- 동기화 프로토콜: `docs/operations/CANON_SYNC_PROTOCOL_2026-07-31.md`
- 연결 Sheet ID: `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw`
- 제품 코드·Codex·병합: `NONE / BLOCKED / NOT_AUTHORIZED`

## 1. 현재 결정 요약

| Decision ID | 상태 | 요약 |
|---|---|---|
| `OMW-DEC-20260731-CONTENT-MANIFEST-V1` | `USER_APPROVED_PLAN` | 전장 1·4막·Stage 20·공세 8·위험 4·보스 3·미션 12 |
| `OMW-DEC-20260731-CANON-SYNC-V1` | `CURRENT_PROJECT_WORK_RULE` | 승인 즉시 GitHub·Sheet 동일 ID 동기화 |
| `OMW-DEC-20260731-DEFEAT-RETRY-V1` | `EXACT_COSTS_PENDING` | Stage 5 이후 MapRun당 최대 1회 제품 유료 Retry |
| `OMW-DEC-20260731-DANGER-BOSS-V1` | `EXACT_VALUES_PENDING` | Stage 5·10·15·20 위험 공세·보스 |
| `OMW-DEC-20260731-VISUAL-SCREEN-BOARD-V1` | `REJECTED_EVIDENCE` | 과거 잘못된 화면 보드 재사용 금지 |
| `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1` | `CURRENT_CANON` | 전장 `6/3/0=30`, 사실표·충돌 원장 |
| `OMW-DEC-20260801-BELU-IDENTITY-V1` | `CURRENT_CANON` | 정본명 벨루, 율비는 역사 별칭 |
| `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1` | `SPEC_WRITTEN_NOT_EXECUTED` | 최신 Red 명세·Legacy 테스트 판정 |
| `OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1` | `SYNC_VERIFIED` | Base·GitHub·25개 Sheet·CI 전수 감사 |
| `OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2` | `TEXT_SPEC_CURRENT / IMAGE_NOT_GENERATED` | 8개 독립 화면·공통 시각·정보 위계·생성 순서 |

## 2. Screen Board V2 결정

```yaml
decision_id: OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2
status: RECOMMENDED_DEFAULT_APPROVED / TEXT_SPEC_CURRENT / IMAGE_NOT_GENERATED
authority_commit: 116f24bb3cbaf00b7de88ba71e77c2223d166928
authority_path: docs/design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md
brief_paths:
  - docs/design/screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_011_RUN_ENTRY_2026-08-01.md
  - docs/design/screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_012_STAGE_PREPARATION_2026-08-01.md
  - docs/design/screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_013_PHYSICAL_REELS_2026-08-01.md
  - docs/design/screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_014_PENDING_REWARD_DEPLOYMENT_2026-08-01.md
  - docs/design/screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_015_STANDARD_BATTLE_2026-08-01.md
  - docs/design/screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_016_BOUNDARY_BREAKER_2026-08-01.md
  - docs/design/screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_017_SETTLEMENT_CAUSAL_RECAP_2026-08-01.md
  - docs/design/screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_018_DEFEAT_PAID_RETRY_2026-08-01.md
image_ids:
  - OM-IMG-011
  - OM-IMG-012
  - OM-IMG-013
  - OM-IMG-014
  - OM-IMG-015
  - OM-IMG-016
  - OM-IMG-017
  - OM-IMG-018
foundation_order:
  - OM-IMG-013
  - OM-IMG-015
visual_reference_binary_migration: PENDING
image_generation: BLOCKED
product_code: UNCHANGED
runtime: NOT_RUN
human_visual_review: NOT_RUN
sheet_sync_status: PENDING
```

화면 구성:

```text
011 메인·런 진입
012 Stage 준비·공세·건설
013 세 물리 릴 설계
014 PendingReward·보관·판매·배치
015 일반 세 라인 전투
016 Stage 15 경계파쇄자
017 Stage 정산·인과 복기
018 패배·제품 유료 재시도
```

통합 보드는 독립 화면 검수 후 `3-3-2` 배열로 조립한다. 이미지 내부에는 상태 범례·기술 보고서·정확 미확정 수치를 넣지 않는다.

## 3. 최신 Red 테스트 결정

```yaml
decision_id: OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1
status: SPEC_WRITTEN_NOT_EXECUTED
authority_commit: 1aba7e9f5e3fbc4e93d0291a4a06f204d196ab7e
latest_test_files: NOT_CREATED
expected_red_execution: NOT_RUN
```

## 4. Base·프로젝트·Sheet 감사 결정

```yaml
decision_id: OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1
status: CURRENT_REPOSITORY_WIDE_AUDIT / SYNC_VERIFIED
authority_commit: 6882777ac42d30a8d25e621b98f9731fbe8537be
verification_commit: e46ed794bcb5e90924362464bc3abff92deb86d1
active_project_base: 9.1.0
recommended_next_base: 9.3.0
last_observed_ci:
  base_v9_adoption: PASS
  project_core_documentation: FAIL
  gdd_sheet_adoption: FAIL
```

## 5. 현재 상태

```text
CURRENT_PRODUCT: LEGACY_PROTOTYPE
LATEST_VERTICAL_SLICE: APPROVED_NOT_IMPLEMENTED
SCREEN_BOARD_V2_TEXT: CURRENT
SCREEN_IMAGES_011_TO_018: NOT_GENERATED
VISUAL_BINARY_MIGRATION: PENDING
LATEST_RED_TEST_FILES: NOT_CREATED
PRODUCT_CODE: NOT_AUTHORIZED
CODEX: BLOCKED
RUNTIME_AND_HUMAN_QA: NOT_RUN
PR_READY: NO
PR_MERGE: BLOCKED
```

## 6. 다음 작업

```text
Screen Board V2 Sheet 동기화·read-back
→ 경제·Retry·save/checkpoint Approval Bundle·시뮬레이션 계약
→ 시각자료 바이너리 이관·Visual Index 재검증
→ OM-IMG-013 독립 이미지 중간 검수
→ 최신 Red test Work Order·expected-failure package
→ Base v9.3 원자 migration package
→ validator Green
→ 사용자 승인 Codex 제품 구현 Plan
```

텍스트 화면 계약 승인과 실제 이미지·Runtime UI·제품 구현 완료를 혼동하지 않는다.