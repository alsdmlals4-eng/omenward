# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-03
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
current_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
last_merged_planning_pr: 129
last_merged_planning_commit: 173a408eb7b89992a81165438d97946167db0e14
current_planning_pr: NONE
current_branch: main
current_pr_head: NONE
status: PROJECT_SHEET_CONFIGURED / SYNCED_TO_MAIN_PR129 / MERGE_VERIFIED / COUNTER_0_OF_10
product_code_authority: NONE
```

이 문서는 GitHub 정본과 연결 Google Sheet의 동기화 계약을 소유한다. 연결 Sheet는 기획자가 읽고 운영하는 `USER_FACING_GDD_WORKSPACE`다. 모든 변경은 정본 Decision ID와 근거를 먼저 갖춘 `PROPOSED_SHEET_CHANGE`로 취급한 뒤 read-back과 CI를 통과해야 동기화 완료로 기록한다.

PR #129는 squash merge됐고 최신 기획은 main 정본이다. exact current main은 자기참조 commit을 만들지 않도록 저장소 기본 브랜치에서 동적으로 해석하며, Sheet에는 feature planning merge SHA와 post-merge 검증 결과를 기록한다.

## 1. 병합된 현행 Decision

```text
OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
```

```text
READY
→ public trigger
→ same-lane legal filter
→ public priority score
→ stability window
→ stable tie-break
→ CAST_PRECHECK
→ immutable CAST_COMMIT snapshot
```

```text
A = 표준 [영웅]
B = 해금 이름 지정 [영웅]
C = 표준 [전설]
```

- 최신 기획은 `MAIN_CANONICAL_NOT_IMPLEMENTED`다.
- 제품 코드·데이터·Scene·Resource는 변경되지 않았다.
- 카운터는 병합 후 `0/10`으로 재설정한다.

## 2. Post-merge Sheet 반영 범위

| 목적 | 범위 |
|---|---|
| 프로젝트 Hub·main·카운터 | `00_프로젝트_허브!E2:L2` |
| 작업순서 | `01_작업순서!A39:N39` |
| 확정 Decision 병합 상태 | `02_현재_확정결정!A47:M47` |
| post-merge 감사 | `04_누락_충돌_감사!A203:H203` |
| GDD 상태 요약 | `05_GDD_요약!D8:J8`, `05_GDD_요약!B9:J9` |
| 변경 이력 | `99_변경이력!A50:H50` |

기존 10/10 Decision·근거·감사·시스템 행은 보존한다.

## 3. 병합 증거

```text
PLANNING_PR = 129
MERGED = TRUE
MERGE_METHOD = SQUASH
FEATURE_MERGE_COMMIT = 173a408eb7b89992a81165438d97946167db0e14
PRE_MERGE_EXACT_HEAD = 55dc617226afdaad918d512d7feddcd13f53cc7a
PRE_MERGE_CI = 746 / 466 / 447
PRE_MERGE_PRODUCT_PATHS = 0
PRE_MERGE_BLOCKERS = 0
```

## 4. 쓰기·검증 절차

```text
1. post-merge 대상 범위 bounded read
2. 기존 10/10 행 보존 확인
3. main merge SHA·0/10 상태 batch update
4. 동일 범위 bounded read-back
5. post-merge sync PR exact-head CI 3종 확인
6. latest main compare
7. changed path·review·thread 확인
8. OPEN_P0·OPEN_P1·MERGE_BLOCKER 검색
9. sync PR 병합
10. final main과 Sheet merge state 재확인
```

## 5. 필수 CI

```text
Validate Project Core Documentation
Validate Omenward GDD Sheet Adoption
Validate Base v9 adoption
```

모두 post-merge sync PR exact HEAD에서 `success`여야 한다.

## 6. blocker 검색

`04_누락_충돌_감사!A1:H300`에서 다음 문자열의 실제 데이터 행을 검색한다.

```text
OPEN_P0
OPEN_P1
MERGE_BLOCKER
```

헤더 외 일치 행이 없어야 한다.

## 7. 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MAIN_CANONICAL_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SHEET_WRITES = PLANNING_DATA_ONLY
PUBLIC_TRIGGER_TARGET_RESOLVER = APPROVED_CONCEPT
POWER_VALIDATION_MATRIX = APPROVED_CONCEPT
EXACT_SCHEMA_AND_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 카운터·다음 Gate

```text
GRILL_ME_COUNT = 0/10
NEXT_PREFLIGHT = AFTER_10_MORE_APPROVED_GRILL_ME_DECISIONS
CURRENT_PLANNING_PR = NONE
LAST_MERGED_PLANNING_PR = 129
```
