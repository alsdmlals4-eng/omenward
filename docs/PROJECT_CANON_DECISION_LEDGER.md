# 오멘워드 기획 정본 결정 원장

- 갱신일: `2026-08-01`
- 상태: `CURRENT_DECISION_LEDGER / PLANNING_ONLY / SYNC_VERIFIED`
- 동기화 프로토콜: `docs/operations/CANON_SYNC_PROTOCOL_2026-07-31.md`
- 누락 방지 게이트: `docs/operations/PROJECT_UNDERSTANDING_AND_OMISSION_PREVENTION_GATE_2026-08-01.md`
- 연결 Sheet ID: `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw`
- 제품 코드 권한: `NONE`
- Codex 실행: `BLOCKED`
- PR 병합: `NOT_AUTHORIZED`

이 원장은 주요 승인 결정, 폐기·대체 상태, GitHub 권위 경로와 Google Sheet 위치를 같은 Decision ID로 연결한다. Sheet에는 Git commit이 없으므로 GitHub authority commit과 `99_변경이력`을 상호 참조한다.

---

## 1. 현재 결정 요약

| Decision ID | 현재 상태 | 요약 |
|---|---|---|
| `OMW-DEC-20260731-CONTENT-MANIFEST-V1` | `USER_APPROVED_PLAN` | 시스템 조합형 콘텐츠 Manifest와 12장 미션 풀 |
| `OMW-DEC-20260731-CANON-SYNC-V1` | `CURRENT_PROJECT_WORK_RULE` | 승인 결정을 GitHub·Sheet에 같은 ID로 즉시 동기화 |
| `OMW-DEC-20260731-DEFEAT-RETRY-V1` | `USER_APPROVED_DETAIL / EXACT_COSTS_PENDING` | Stage 5 이후 MapRun당 1회 영구재화 재시도 |
| `OMW-DEC-20260731-DANGER-BOSS-V1` | `USER_APPROVED_PLAN / EXACT_VALUES_PENDING` | Stage 5·10·15·20 위험 공세·보스 패키지 |
| `OMW-DEC-20260731-MID-IMAGE-REVIEW-V1` | `WORKFLOW_RETAINED / CURRENT_BATCH_REJECTED / RESET_REQUIRED` | 중간 이미지 검수 절차는 유지하되 기존 배치 폐기 |
| `OMW-DEC-20260731-VISUAL-SCREEN-BOARD-V1` | `REJECTED_EVIDENCE / SUPERSEDED_PENDING_REBUILD` | 잘못된 화면 보드 V1은 재사용 금지 |
| `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1` | `CURRENT_PROJECT_WORK_RULE / CURRENT_USER_CONFIRMED_CANON` | 프로젝트 사실표·충돌 원장·누락 방지와 전장 6/3/0 불변 계약 |

---

## 2. 유지되는 기존 결정

### OMW-DEC-20260731-CONTENT-MANIFEST-V1

```yaml
decision_id: OMW-DEC-20260731-CONTENT-MANIFEST-V1
status: USER_APPROVED_PLAN
github_authority_commit: 292a00d4aad3c836d5f3907e38c6496cc03d6c73
github_pr: 116
github_merge_state: NOT_MERGED
sheet_sync_status: SYNCED_TO_PR_HEAD
verification_result: PASS
```

### OMW-DEC-20260731-CANON-SYNC-V1

```yaml
decision_id: OMW-DEC-20260731-CANON-SYNC-V1
status: CURRENT_PROJECT_WORK_RULE
github_authority_commit: 292a00d4aad3c836d5f3907e38c6496cc03d6c73
github_pr: 116
github_merge_state: NOT_MERGED
sheet_sync_status: SYNCED_TO_PR_HEAD
verification_result: PASS
```

### OMW-DEC-20260731-DEFEAT-RETRY-V1

```yaml
decision_id: OMW-DEC-20260731-DEFEAT-RETRY-V1
status: USER_APPROVED_DETAIL / EXACT_COST_VALUES_PENDING
github_authority_commit: 5e0f7d3a7e5afac3079f63422e0b21f79f83fd64
github_pr: 116
github_merge_state: NOT_MERGED
sheet_sync_status: SYNCED_TO_PR_HEAD
verification_result: PASS
```

### OMW-DEC-20260731-DANGER-BOSS-V1

```yaml
decision_id: OMW-DEC-20260731-DANGER-BOSS-V1
status: USER_APPROVED_PLAN / EXACT_VALUES_PENDING
github_authority_commit: b97b435e938f5fa4b4f537e0133de25c49e1e956
github_pr: 116
github_merge_state: NOT_MERGED
sheet_sync_status: SYNCED_TO_PR_HEAD
verification_result: PASS
```

---

## 3. 비주얼 결정 정정

### OMW-DEC-20260731-MID-IMAGE-REVIEW-V1

```yaml
decision_id: OMW-DEC-20260731-MID-IMAGE-REVIEW-V1
original_approved_at: 2026-07-31T21:09:00+09:00
corrected_at: 2026-08-01T04:36:00+09:00
status: WORKFLOW_RETAINED / CURRENT_BATCH_REJECTED / RESET_REQUIRED
github_authority_paths:
  - docs/DOCUMENTATION_MAP.md
  - docs/reviews/APPROVED_MIDPOINT_IMAGE_REVIEW_GATE_2026-07-31.md
  - docs/operations/PROJECT_UNDERSTANDING_AND_OMISSION_PREVENTION_GATE_2026-08-01.md
github_authority_commit: 8853b4deb6d9a48913a73c0f48e97e4f8d6aad4a
github_pr: 116
github_merge_state: NOT_MERGED
sheet_ranges:
  - 00_프로젝트_허브!E2:K2
  - 02_현재_확정결정!A10:L10
  - 60_UX_UI_접근성!A6:J6
  - 71_이미지기획_생성목록!E6:F11
  - 71_이미지기획_생성목록!J6:J11
  - 71_이미지기획_생성목록!L6:L11
  - 72_이미지검수_승인로그!C3:L8
  - 80_데모_버티컬슬라이스_플레이테스트!A6:L6
  - 99_변경이력!A12:H12
sheet_sync_status: SYNCED_TO_PR_HEAD
verified_at: 2026-08-01T04:36:00+09:00
verification_result: PASS
```

정정 요약:

- 실제 이미지는 생성되지 않은 것이 아니라 생성 후 사용자 검토에서 폐기됐다.
- `OM-IMG-005~010`은 모두 `REJECTED_* / RESET_REQUIRED`다.
- 중간 이미지 검수 절차는 유지하지만 기존 생성 배치와 입력 화면 보드는 재사용하지 않는다.
- 새 이미지 생성은 사실표·토폴로지·세 물리 릴 검산·독립 브리프 사용자 확인 전 차단한다.

### OMW-DEC-20260731-VISUAL-SCREEN-BOARD-V1

```yaml
decision_id: OMW-DEC-20260731-VISUAL-SCREEN-BOARD-V1
original_approved_at: 2026-07-31T21:30:00+09:00
rejected_at: 2026-08-01T04:36:00+09:00
status: REJECTED_EVIDENCE / SUPERSEDED_PENDING_REBUILD
github_authority_paths:
  - docs/DOCUMENTATION_MAP.md
  - docs/design/OMENWARD_VISUAL_SITUATIONAL_INGAME_SCREEN_SPEC_BOARD_2026-07-31.md
  - docs/reviews/OMENWARD_COMPREHENSIVE_PROJECT_INTEGRITY_REVIEW_2026-08-01.md
github_authority_commit: 8853b4deb6d9a48913a73c0f48e97e4f8d6aad4a
github_pr: 116
github_merge_state: NOT_MERGED
sheet_ranges:
  - 00_프로젝트_허브!E2:K2
  - 02_현재_확정결정!A11:L11
  - 60_UX_UI_접근성!A7:J7
  - 71_이미지기획_생성목록!E6:F11
  - 71_이미지기획_생성목록!J6:J11
  - 71_이미지기획_생성목록!L6:L11
  - 72_이미지검수_승인로그!C3:L8
  - 80_데모_버티컬슬라이스_플레이테스트!A7:L7
  - 99_변경이력!A12:H12
sheet_sync_status: SYNCED_TO_PR_HEAD
verified_at: 2026-08-01T04:36:00+09:00
verification_result: PASS
```

폐기 사유:

- 잘못된 어두운 비주얼 추론을 목표 방향처럼 고정했다.
- 세 물리 릴·3×3 정지 보드와 하나의 전장·세 라인을 정확히 고정하지 못했다.
- 건설 노드 한 종류, 본진 6/진영, 중간 거점 3/거점, 접전지 0을 검산하지 않았다.
- 승인 정본·현재 구현·Legacy·제안·폐기 증거를 충분히 분리하지 않았다.

---

## 4. OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1

```yaml
decision_id: OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1
approved_at: 2026-08-01T04:36:00+09:00
status: CURRENT_PROJECT_WORK_RULE / CURRENT_USER_CONFIRMED_CANON
github_authority_paths:
  - AGENTS.md
  - docs/DOCUMENTATION_MAP.md
  - docs/CURRENT_IMPLEMENTATION_STATUS.md
  - docs/operations/PROJECT_UNDERSTANDING_AND_OMISSION_PREVENTION_GATE_2026-08-01.md
  - docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_CONSTRUCTION_NODE_INVARIANTS_2026-08-01.md
  - docs/reviews/OMENWARD_COMPREHENSIVE_PROJECT_INTEGRITY_REVIEW_2026-08-01.md
  - docs/images/VISUAL_REFERENCE_INDEX.md
github_authority_commit: 8853b4deb6d9a48913a73c0f48e97e4f8d6aad4a
github_pr: 116
github_merge_state: NOT_MERGED
sheet_ranges:
  - 00_프로젝트_허브!E2:K2
  - 02_현재_확정결정!A10:L12
  - 04_누락_충돌_감사!A6:H13
  - 15_조작_게임규칙!A4:J5
  - 60_UX_UI_접근성!A6:J8
  - 71_이미지기획_생성목록!E6:F11
  - 71_이미지기획_생성목록!J6:J11
  - 71_이미지기획_생성목록!L6:L11
  - 72_이미지검수_승인로그!C3:L8
  - 80_데모_버티컬슬라이스_플레이테스트!A6:L8
  - 99_변경이력!A12:H12
sheet_sync_status: SYNCED_TO_PR_HEAD
verified_at: 2026-08-01T04:36:00+09:00
verification_result: PASS
```

### 4.1 프로젝트 이해 게이트

모든 중형 이상 기획·화면·이미지·구현 작업 전에 다음을 분리한다.

```text
CURRENT_CANON
CURRENT_IMPLEMENTATION
LEGACY_PROVEN
PROPOSED
REJECTED_EVIDENCE
UNRESOLVED
```

작업 질문, 최신 사용자 결정, 문서↔구현↔Sheet↔시각자료 충돌과 열린 P0/P1 Finding을 기록한다. 열린 P0가 있으면 이미지 생성·제품 구현·최종 기획 승격을 차단한다.

### 4.2 전장·노드 불변 계약

```text
node_kind = CONSTRUCTION_NODE_ONLY
battlefield_count = 1
lane_count = 3
base_count = 2
nodes_per_base = 6
midpoint_outposts = 3_lanes × 2_factions = 6
nodes_per_midpoint_outpost = 3
clash_zones = 3
nodes_per_clash_zone = 0
total_nodes = 2×6 + 6×3 = 30
```

- 중앙 접전지는 점령 목적지이며 건설 장소가 아니다.
- 본진·중간 거점은 노드 종류가 아니라 건설 노드가 속한 위치다.
- 방어·전진·특수·접전지 노드를 임의로 추가하지 않는다.

### 4.3 Legacy와 최신 구현 경계

실제 저장소에는 다음 Legacy seam이 있다.

- 독립 9칸 가중 룰렛.
- 중간 거점당 `front_a / front_b / rear` 세 node ID.
- 본진 노드 데이터 부재와 `construct_home()`의 중단 거점 별칭.
- `capture_power` 합산 점령.
- barracks/tower/farm 세 건물.
- 영구재화 없는 무료 Stage retry.
- 코드 드로잉 graybox·Label 중심 HUD.

이는 최신 세 물리 릴·30노드·5건물·고정 점령·유료 Retry·제품 UI의 구현 증거가 아니다.

---

## 5. 2026-08-01 적대적 검토 Finding

| Finding | Severity | 현재 상태 |
|---|---|---|
| 생성·폐기 이미지가 미생성으로 남음 | P0 | `MITIGATED / SHEET_VERIFIED` |
| 잘못된 화면 보드가 활성 정본 | P0 | `MITIGATED / REJECTED_AND_ROUTED_OUT` |
| 프로젝트 이해 선행 게이트 부재 | P0 | `MITIGATED / GATE_ADDED` |
| 노드 관계식·접전지 0 의미 누락 | P1 | `MITIGATED / CONTRACT_ADDED` |
| 시각자료 경로·최신 자료 누락 | P1 | `MITIGATED / INDEX_UPDATED` |
| 활성 Base v9.1과 v9.3 계획 혼동 | P1 | `DECLARED / NOT_ADOPTED` |
| Legacy와 최신 제품 계약 혼재 | P1 | `DECLARED / MIGRATION_REQUIRED` |
| 최신 구조 자동 계약 없음 | P1 | `OPEN / BLOCKS_CODEX_BUILD` |
| 벨루·율비 관계 미정 | P1 | `OPEN / BLOCKS_GUIDE_CANON` |
| 구형 Sheet 역사 행 상태 혼재 | P2 | `OPEN / CLEANUP_PENDING` |

열린 P1은 관련 작업을 차단한다. 벨루·율비가 해결되기 전 안내자 비주얼·대사 정본 승격을 하지 않으며, 최신 Red 테스트가 준비되기 전 Codex 제품 구현을 승인하지 않는다.

---

## 6. Google Sheet 재검증

재조회 범위:

- `00_프로젝트_허브!E2:K2`
- `02_현재_확정결정!A10:L12`
- `04_누락_충돌_감사!A6:H13`
- `15_조작_게임규칙!A4:J5`
- `60_UX_UI_접근성!A6:J8`
- `71_이미지기획_생성목록!E6:F11`
- `71_이미지기획_생성목록!J6:J11`
- `71_이미지기획_생성목록!L6:L11`
- `72_이미지검수_승인로그!C3:L8`
- `80_데모_버티컬슬라이스_플레이테스트!A6:L8`
- `99_변경이력!A12:H12`

검증 결과:

- 새 Decision ID와 authority commit이 모든 기록 surface에서 일치한다.
- 기존 화면 보드는 `REJECTED_EVIDENCE`, 이미지 배치는 `REJECTED_* / RESET_REQUIRED`로 정정됐다.
- 노드 구조는 `건설 노드 1종 / 본진 6 / 중간 거점 3 / 접전지 0 / 전체 30`으로 기록됐다.
- Legacy와 최신 구현 경계, 열린 Finding과 작업 차단이 기록됐다.
- 새 행과 수정 행은 기존 상단 정렬·줄바꿈·글꼴 크기·날짜 서식을 유지한다.
- 제품 코드·실제 에셋·런타임 검증·사람 검증 완료를 주장하지 않는다.

---

## 7. 현재 동기화 상태

```text
GITHUB_AUTHORITY: WRITTEN
GOOGLE_SHEET: WRITTEN
SYNC_VERIFICATION: PASS
SYNC_STATE: SYNCED_TO_PR_HEAD
PROJECT_FACT_MATRIX: REQUIRED
CONTRADICTION_REGISTER: REQUIRED
VISUAL_SCREEN_BOARD_V1: REJECTED
PREVIOUS_GENERATED_IMAGES: REJECTED_EVIDENCE
NEW_IMAGE_GENERATION: BLOCKED
LATEST_VERTICAL_SLICE_IMPLEMENTATION: NOT_STARTED
LATEST_CONTRACT_TESTS: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: NOT_AUTHORIZED
CODEX_EXECUTION: BLOCKED
PR_MERGE: NOT_AUTHORIZED
```

PR #116이 사용자 최종 승인 뒤 병합되면 GitHub SHA와 Sheet 상태를 main commit 기준 `SYNCED_TO_MAIN`으로 다시 동기화해야 한다.