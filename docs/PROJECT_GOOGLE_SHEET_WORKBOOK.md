# [현행] OMENWARD Google Sheet 정본 동기화 계약

```yaml
updated_at: 2026-08-11
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
status: PROJECT_SHEET_CONFIGURED / USER_FACING_GDD_WORKSPACE / PROPOSED_SHEET_CHANGE
current_decision: OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1
planning_status: MAIN_CANONICAL_APPROVED_10_OF_10
contract_version: 4.5
work_phase: PHASE_A_GPT_CHAT_PLANNING
current_working_pr: 178
base_main_observed: 315c66eea9614c284b9c11c4d522141065dfa4b0
project_activation_baseline: 87339f87949c8faea0dfe1482c5d0887a04d94f4
```

Google Sheet는 GitHub 책임 원본을 운영·탐색 목적으로 미러링하는 `USER_FACING_GDD_WORKSPACE`다. Sheet 단독 변경은 프로젝트 canon 변경이 아니며 Draft PR 단계의 쓰기는 `PROPOSED_SHEET_CHANGE`, 병합 뒤 같은 Decision row의 상태는 `MERGED_CANON`이다.

## 1. 같은 Decision ID 동기화

현재 동기화 Decision:

`OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1`

최소 current-facing surface:

```text
00_프로젝트_허브
01_작업순서
02_현재_확정결정
04_누락_충돌_감사
05_GDD_요약
15_조작_게임규칙
99_변경이력
```

과거 완료 Decision·PR·CI·runtime 진단 행을 덮어쓰지 않는다. 같은 질문의 현재값이 바뀌면 새 corrective row를 추가하고 active summary row만 직접 정정한다.

## 2. 현행 병영 Tier 동기화 값

### 일반병 병영

```text
GENERAL_T1_AUTO_PRODUCTION = BASIC_INFANTRY
GENERAL_T1_TOKEN_SOURCE = BASIC_INFANTRY
GENERAL_T2_BRANCHES = SHIELD / GREATSWORD / SPEAR / ARCHER / CAVALRY
GENERAL_T2_AUTO_PRODUCTION = SELECTED_GENERAL_UNIT
GENERAL_T2_TOKEN_SOURCE = SELECTED_GENERAL_UNIT
```

### 특수병 병영

최종 owner:

`docs/design/APPROVED_OMENWARD_BARRACKS_AUTO_PRODUCTION_AND_TOKEN_SOURCE_AMENDMENT_2026-08-06.md`

```text
SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT
SPECIAL_T1_SELECTED_UNIT_PERSISTENCE = FIXED_WHILE_BUILDING_REMAINS_T1
SPECIAL_T1_AUTO_PRODUCTION = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_AUTO_PRODUCTION_AND_TOKEN_SOURCE = SAME_SELECTED_UNIT_SEPARATE_ACQUISITION_PATHS
SPECIAL_T1_SAVE_RELOAD_RESELECT = FORBIDDEN
SPECIAL_T1_FREE_REROLL = FORBIDDEN
SPECIAL_T2_BRANCHES = MAGE / PRIEST / ASSASSIN / FLYING_UNIT / GIANT
SPECIAL_T2_AUTO_PRODUCTION = SELECTED_SPECIAL_UNIT
SPECIAL_T2_TOKEN_SOURCE = SELECTED_SPECIAL_UNIT
SPECIAL_UNIT_FUNCTIONAL_POWER = STRONGER_THAN_GENERAL_UNIT
SPECIAL_AUTO_PRODUCTION_INTERVAL = LONGER_THAN_GENERAL_UNIT
```

구형 “특수 T1 TokenSource 없음”은 `OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1` 당시 history로만 남긴다. current-facing Sheet row는 final amendment를 명시해야 한다.

### 방어탑·직선 강화

```text
DEFENSE_TOWER_T2 = ARTILLERY / DEFENSE_ENHANCEMENT / SNIPER
LINEAR_TIER_BUILDINGS = VAULT / FARM / COMMAND_POST / MANA_TOWER
LINEAR_T2_BRANCHING = FORBIDDEN
```

## 3. Planning·runtime 상태 동기화

```text
PLANNING_CANON = MAIN_CANONICAL_APPROVED_10_OF_10
V4_5_PHASE = PHASE_A_GPT_CHAT_PLANNING
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = REQUIRED
PHASE_B_FINAL_PLANNING_REVIEW = NOT_RUN
PHASE_C = BLOCKED
PR175 = OPEN_DRAFT
PR175_HEAD_OBSERVED = bde85549560fca90f7aa25fc4842bc0a3afb92e7
ISSUE176_APPROVED_RUNTIME_GAPS = 7
PR177 = REFERENCE_ONLY_DO_NOT_MERGE
```

PR175의 기존 11/11 Actions는 과거 exact-head/base 증거이며 current canon PR merge 뒤 strict up-to-date runtime Green으로 표시하지 않는다.

## 4. Current Hub

`00_프로젝트_허브!A2:L2`는 최소 다음을 한 행에서 보여준다.

```text
project = OMENWARD
stage = PHASE_A_GPT_CHAT_PLANNING
mode = CANON_FRESHNESS_V45_THIN_ADAPTER
planning = MAIN_CANONICAL_APPROVED_10_OF_10
Base = 315c66eea9614c284b9c11c4d522141065dfa4b0
OMENWARD baseline main = 87339f87949c8faea0dfe1482c5d0887a04d94f4
Decision = OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1
planning PR = 178
runtime PR = 175 / 7 gaps / Draft
handoff PR = 177 / reference only
Phase C blocker = explicit planning-complete declaration + Phase B
```

## 5. Current Decision row

`02_현재_확정결정`에는 과거 1~10/10·platform·analysis·runtime package 행을 삭제하지 않고 다음 새 Decision row를 추가한다.

```text
Decision = OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1
scope = canon freshness + v4.5 Thin Adapter + Sheet sync
product mutation = NONE
current phase = PHASE_A_GPT_CHAT_PLANNING
phase C = BLOCKED
special T1 TokenSource = SELECTED_RANDOM_SPECIAL_UNIT
v4.4 binding/state = HISTORICAL_V4_4_BINDING
```

## 6. Audit row

`04_누락_충돌_감사`에는 다음 finding을 같은 Decision으로 기록한다.

- active GDD와 Workbook/Sheet가 superseded Special T1 no-TokenSource 표현을 current처럼 재발행.
- cold-start docs가 6/10·7/10·10/10 및 다른 runtime 시점으로 갈라짐.
- live Base SHA가 stale.
- v4.4 current binding과 사용자 승인 v4.5 단계 계약이 충돌.
- 수정은 current consumer propagation만 수행하고 historical design/runtime evidence는 보존.

## 7. 15_조작_게임규칙 처리

과거 `OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1` row는 history로 보존한다. 그 row를 소급 수정하지 않는다.

그 대신 같은 current tab에 새 corrective row를 추가해:

```text
SPECIAL_T1 = successful construction commit selects one special unit
AUTO_PRODUCTION = selected unit
TOKEN_SOURCE = same selected unit / separate acquisition path
SAVE_RELOAD_RESELECT = forbidden
FREE_REROLL = forbidden
```

를 명시한다.

## 8. 05_GDD_요약 처리

`05_GDD_요약`의 current 핵심 게임플레이 row는 history가 아니라 사용자용 현재 요약이므로 직접 고친다.

```text
특수 T1 = 건설 확정 시 무작위 선정 → 선정 병종 자동생산 + 같은 병종 TokenSource 별도 공급
```

## 9. 쓰기 규칙

1. GitHub 책임 원본과 Decision ID를 먼저 고정한다.
2. Draft PR exact head를 기록한다.
3. 과거 완료 Decision·audit·history 행을 덮어쓰지 않는다.
4. write 직후 같은 bounded range를 다시 읽는다.
5. Decision ID·PR head·Base SHA·phase·TokenSource 불일치는 blocker다.
6. Draft 단계 `PROPOSED_SHEET_CHANGE`, merge 뒤 `MERGED_CANON`.
7. Sheet와 GitHub가 충돌하면 GitHub 책임 원본을 수정하기 전에 어떤 surface가 stale인지 먼저 판정한다.

## 10. v4.5 단계 경계

```text
PHASE_A_GPT_CHAT_PLANNING
→ 같은 Decision canon + Sheet sync
→ planning PR review/merge
→ USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION
→ PHASE_B
→ PHASE_C
```

Sheet sync 완료는 Phase C 시작 승인이 아니다.

## 11. 검증 증거

현재 Decision의 proposed write/readback 결과는 다음 파일에 보존한다.

`docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json`

병합 뒤 같은 Decision ID와 최종 merge SHA로 Sheet 상태를 다시 갱신하고 bounded reread한다.
