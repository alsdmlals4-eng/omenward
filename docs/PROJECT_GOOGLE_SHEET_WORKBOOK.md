# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-03
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
current_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
current_sync: OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
last_merged_planning_pr: 129
last_merged_planning_commit: 173a408eb7b89992a81165438d97946167db0e14
last_maintenance_pr: 131
last_maintenance_commit: 8ecbb78df47813a6332963db16d235131e65981a
current_planning_pr: PENDING_CREATION
current_branch: gpt/omenward-status-pending-refresh-20260803-v2
current_pr_head: RESOLVE_FROM_PR
status: PROJECT_SHEET_CONFIGURED / MAINTENANCE_SYNC_PENDING / COUNTER_0_OF_10
product_code_authority: NONE
```

이 문서는 GitHub 정본과 연결 Google Sheet의 동기화 계약을 소유한다. 연결 Sheet는 기획자가 읽고 운영하는 `USER_FACING_GDD_WORKSPACE`다. 모든 변경은 정본 Decision 또는 Sync ID와 근거를 먼저 갖춘 `PROPOSED_SHEET_CHANGE`로 취급한 뒤 read-back과 CI를 통과해야 동기화 완료로 기록한다.

## 1. 유지보수 Sync

```text
OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1
```

목적:

- `CURRENT_IMPLEMENTATION_STATUS.md`를 2026-08-03 main 영웅 정본에 맞춘다.
- `DECISIONS_PENDING.md`에 영웅·전설 exact schema·Trigger·timer·효과값·simulation·save 항목을 추가한다.
- 다음 제품 Gate를 deterministic simulation harness 설계로 고정한다.
- 제품 구현과 시뮬레이션 실행은 승인하지 않는다.
- Grill Me 카운터는 `0/10`으로 유지한다.

## 2. Sheet 반영 범위

| 목적 | 범위 |
|---|---|
| 프로젝트 Hub·현재 Sync·다음 Gate | `00_프로젝트_허브!E2:L2` |
| 유지보수 작업순서 | `01_작업순서!A40:N40` |
| 비카운트 Sync 상태 | `02_현재_확정결정!A48:M48` |
| 정본 불일치·보완 감사 | `04_누락_충돌_감사!A205:H207` |
| GDD 상태·우선순위 요약 | `05_GDD_요약!B8:J9` |
| 변경 이력 | `99_변경이력!A52:H52` |

기존 PR #129~#131 Decision·근거·감사·병합 행은 보존한다.

## 3. 감사 항목

```text
OMW-AUD-205
→ CURRENT_IMPLEMENTATION_STATUS가 2026-07-27에 고정되어 최신 영웅 main 정본을 추적하지 못함

OMW-AUD-206
→ DECISIONS_PENDING에 영웅 Trigger·timer·효과값·simulation·save 미확정 항목이 누락됨

OMW-AUD-207
→ 제품 구현 전에 deterministic harness와 공통 combat schema를 먼저 확정하지 않으면 값 재작업과 비결정성 위험이 큼
```

세 항목은 이번 Sync에서 추적 문서와 라우터를 교정해 해소한다. exact simulation schema와 값 자체는 후속 Grill Me Decision에 남긴다.

## 4. 다음 Gate

```text
NEXT_GRILL_ME_DECISION
= OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
```

```text
P0 = deterministic simulation harness 범위·재현성·입출력 계약
P1 = 전체 병종 공통 전투 schema와 피해·방어·위협도 기준
P2 = 다섯 해금 영웅 exact Trigger·timer·효과값
P3 = A/B/C 통과선·표본 수·stop-ship 기준
P4 = 100,000시드 룰렛·경제 simulation 계약
P5 = checkpoint·save schema
P6 = 첫 제품 구현 패키지·Red tests·회귀·롤백 계획
```

## 5. 쓰기·검증 절차

```text
1. 대상 범위 bounded read
2. 기존 PR #129~#131 행 보존 확인
3. Sync ID·감사·P0~P6·PR exact HEAD batch update
4. 동일 범위 bounded read-back
5. maintenance PR exact-head CI 3종 확인
6. latest main compare
7. changed path·review·thread 확인
8. OPEN_P0·OPEN_P1·MERGE_BLOCKER 검색
9. maintenance PR 병합
10. final main과 Sheet 상태 재확인
```

## 6. 필수 CI

```text
Validate Project Core Documentation
Validate Omenward GDD Sheet Adoption
Validate Base v9 adoption
```

모두 maintenance PR exact HEAD에서 `success`여야 한다.

## 7. blocker 검색

`04_누락_충돌_감사!A1:H300`에서 다음 문자열의 실제 데이터 행을 검색한다.

```text
OPEN_P0
OPEN_P1
MERGE_BLOCKER
```

헤더 외 일치 행이 없어야 한다.

## 8. 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MAIN_CANONICAL_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SHEET_WRITES = PLANNING_DATA_ONLY
EXACT_SCHEMA_AND_VALUES = PENDING
SIMULATION_PLAN = REQUIRED_BEFORE_IMPLEMENTATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. 카운터·운영 상태

```text
GRILL_ME_COUNT = 0/10
CURRENT_MAINTENANCE_SYNC = OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1
NEXT_PREFLIGHT = AFTER_10_MORE_APPROVED_GRILL_ME_DECISIONS
CURRENT_PLANNING_PR = PENDING_CREATION
LAST_MERGED_PLANNING_PR = 129
LAST_MAINTENANCE_PR = 131
```
