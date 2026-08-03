# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-03
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
current_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
parent_gameplay_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
last_maintenance_pr: 132
last_maintenance_commit: 970ca7c52d757806c6968b55808346ac8a50b3ea
current_planning_pr: RESOLVE_FROM_OPEN_PR
current_branch: gpt/omenward-simulation-harness-planning-20260803
current_pr_head: RESOLVE_FROM_PR
status: PROJECT_SHEET_CONFIGURED / DECISION_SYNC_PENDING / COUNTER_1_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
```

이 문서는 GitHub 정본과 연결 Google Sheet의 동기화 계약을 소유한다. Sheet는 `USER_FACING_GDD_WORKSPACE`이며 모든 쓰기는 Decision ID와 근거를 갖춘 `PROPOSED_SHEET_CHANGE`로 처리하고 bounded read-back·CI를 통과해야 한다.

## 1. 현재 Decision

```text
OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
```

승인 범위:

```text
versioned fixture
+ fixed integer tick
+ named RNG streams
+ stable object IDs
+ ordered external commands
+ pure domain state transition
→ ordered event log
→ normalized final state
→ metrics summary
→ state fingerprints
```

현재 승인된 검증 Tier는 T0 schema, T1 replay determinism, T2 rule invariants, T3 paired A/B/C metrics의 **설계 계약**이다. Simulation tool 구현·실행·밸런스 결론은 승인되지 않았다.

## 2. Sheet 반영 범위

| 목적 | 범위 |
|---|---|
| Hub·Decision·카운터·PR HEAD | `00_프로젝트_허브!E2:L2` |
| 작업순서 | `01_작업순서!A41:N41` |
| 현재 확정 Decision | `02_현재_확정결정!A49:M49` |
| 공식 벤치마크·내부 근거 | `03_근거_라이브러리!A29:J34` |
| 적대적 감사 | `04_누락_충돌_감사!A208:H220` |
| GDD 요약 | `05_GDD_요약!B8:J9` |
| 핵심루프 연결 | `12_핵심루프!A22:J22` |
| 조작·게임규칙 연결 | `15_조작_게임규칙!A25:J25` |
| 핵심시스템 연결 | `40_핵심시스템_메인콘텐츠!A25:J25` |
| 성장·경제 검증 연결 | `41_성장_경제!A35:I35` |
| 콘텐츠 fixture 연결 | `50_메인콘텐츠!A32:J32` |
| UX·로그 연결 | `60_UX_UI_접근성!A33:J33` |
| 아트·오디오 제외 경계 | `70_아트_오디오_에셋!A16:J16` |
| 변경 이력 | `99_변경이력!A53:H53` |

## 3. 벤치마크 근거

Sheet 근거 행은 exact 값 권위가 아니라 제작 경계로 기록한다.

1. Godot command-line `--headless`와 CI script 실행.
2. fixed physics processing과 variable idle processing 차이.
3. `RandomNumberGenerator` seed·state와 독립 instance.
4. JSON 숫자 float 변환과 canonical state hash 경계.
5. FileAccess 기반 결과 파일 입출력.
6. OMENWARD main 영웅 Trigger·A/B/C 검증 정본.

## 4. 감사 행

```text
OMW-AUD-208 ~ OMW-AUD-220
```

대상:

- global RNG coupling
- wall-clock·frame delta leakage
- unstable collection order
- float·platform divergence
- fixture drift
- family overfitting
- Harness/runtime divergence
- excessive event log
- placeholder balance conclusion
- contaminated A/B/C comparison
- omitted other-two-lane contribution
- missing save/Retry state
- headless/determinism confusion

## 5. 쓰기·검증 절차

```text
1. 대상 범위 bounded read
2. PR exact HEAD 확인
3. Decision·근거·감사·시스템 연결 batch update
4. 동일 범위 bounded read-back
5. exact-head CI 3종
6. latest main compare
7. changed paths·reviews·threads
8. OPEN_P0·OPEN_P1·MERGE_BLOCKER 검색
9. PR body exact evidence 갱신
10. Draft 유지 — 1/10
```

## 6. 필수 CI

```text
Validate Project Core Documentation
Validate Omenward GDD Sheet Adoption
Validate Base v9 adoption
```

모두 PR exact HEAD에서 `success`여야 한다.

## 7. blocker 검색

`04_누락_충돌_감사!A1:H300`에서 다음 문자열의 실제 데이터 행이 없어야 한다.

```text
OPEN_P0
OPEN_P1
MERGE_BLOCKER
```

## 8. 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = HARNESS_SCOPE_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SHEET_WRITES = PLANNING_DATA_ONLY
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
EXACT_COMBAT_SCHEMA = PENDING
EXACT_TICK_RATE = PENDING
EXACT_FORMULAS_AND_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. 카운터·다음 Gate

```text
GRILL_ME_COUNT = 1/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
NEXT_PREFLIGHT = AT_10_OF_10
CURRENT_PLANNING_PR = RESOLVE_FROM_OPEN_PR
LAST_MAINTENANCE_PR = 132
```
