# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-03
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
current_decision: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
parent_semantics_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_harness_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
last_maintenance_pr: 132
last_maintenance_commit: 970ca7c52d757806c6968b55808346ac8a50b3ea
current_planning_pr: RESOLVE_FROM_OPEN_PR
current_branch: gpt/omenward-simulation-harness-planning-20260803
current_pr_head: RESOLVE_FROM_PR
status: PROJECT_SHEET_CONFIGURED / DECISION_SYNC_PENDING / COUNTER_4_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
```

이 문서는 GitHub 정본과 연결 Google Sheet의 동기화 계약을 소유한다. 모든 Sheet 쓰기는 같은 Decision ID·PR exact HEAD·근거·감사·bounded read-back을 가져야 한다.

## 1. 현재 Decision

```text
OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
```

승인 범위:

```text
Armor/Resistance common hyperbolic formula
+ effective defense 0~300
+ positive integer half-up rounding
+ minimum valid damage 1
+ Barrier 20% application / 30% total / 3000ms
+ HP-loss redirection 30% / one recipient
+ Health Floor 1 HP / one trigger / exclusive group
+ Status stack 3 / pulse 1000ms / Control 2000ms / lockout 1000ms
+ Barrier early stop-ship guards
```

코드·fixture·test·simulation·balance 결론은 승인되지 않았다.

## 2. Sheet 반영 범위

| 목적 | 범위 |
|---|---|
| Hub·Decision·카운터·PR HEAD | `00_프로젝트_허브!E2:L2` |
| 작업순서 | `01_작업순서!A44:N44` |
| 현재 확정 Decision | `02_현재_확정결정!A52:M52` |
| 공식 벤치마크·내부 근거 | `03_근거_라이브러리!A43:J46` |
| 적대적 감사 | `04_누락_충돌_감사!A247:H260` |
| GDD 요약 | `05_GDD_요약!B8:J9` |
| 핵심루프 연결 | `12_핵심루프!A25:J25` |
| 조작·게임규칙 연결 | `15_조작_게임규칙!A28:J28` |
| 핵심시스템 연결 | `40_핵심시스템_메인콘텐츠!A28:J28` |
| 성장·경제 경계 | `41_성장_경제!A38:I38` |
| 콘텐츠 fixture 연결 | `50_메인콘텐츠!A35:J35` |
| UX·로그 연결 | `60_UX_UI_접근성!A36:J36` |
| 아트·오디오 제외 경계 | `70_아트_오디오_에셋!A19:J19` |
| 변경 이력 | `99_변경이력!A57:H57` |

## 3. 핵심 수치

```text
EFFECTIVE_DEFENSE_MIN = 0
EFFECTIVE_DEFENSE_MAX = 300
MITIGATION_CONSTANT = 100
ROUNDING = POSITIVE_INTEGER_HALF_UP
MINIMUM_VALID_DAMAGE = 1
```

```text
post_mitigation
= adjusted_damage <= 0
  ? 0
  : max(1, (adjusted_damage * 100 + floor((100 + defense)/2)) div (100 + defense))
```

```text
BARRIER_PER_APPLICATION_CAP = 20% max HP
BARRIER_TOTAL_CAP = 30% max HP
BARRIER_DEFAULT_DURATION = 3000ms
REDIRECTION_DEFAULT = 30%
REDIRECTION_RECIPIENT_MAX = 1
HEALTH_FLOOR_DEFAULT = 1 HP
ADD_STACKS_DEFAULT_CAP = 3
DOT_HOT_PULSE = 1000ms
CONTROL_DURATION_MAX = 2000ms
SAME_CONTROL_GROUP_LOCKOUT = 1000ms
```

## 4. 근거 행

Sheet 근거는 외부 exact 수치를 복사하는 권위가 아니라 제작 경계로 기록한다.

1. 분모형 방어 공식의 완만한 추가 효율.
2. Armor와 Resistance의 동일 곡선으로 학습·QA 비용 제한.
3. Barrier를 HP와 분리하고 cap·duration으로 과집중 통제.
4. OMENWARD core: 세 전선·SpinSnapshot·TokenSource·비가역 배치·원인 복기.

## 5. 감사 행

```text
OMW-AUD-247 ~ OMW-AUD-260
```

대상:

- negative defense bypass
- defense cap omission
- float/rounding replay divergence
- minimum damage applied to invalid/zero effect
- Barrier application cap bypass
- max HP change retroactive truncation
- collection-order Barrier consumption
- Barrier overcentralization
- redirection rounding conservation
- invalid recipient loss deletion
- hit-order Health Floor bias
- multiple Floor immortality
- Control chain lock
- ms→tick arbitrary conversion

## 6. 쓰기·검증 절차

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
10. Draft 유지 — 4/10
```

## 7. 필수 CI

```text
Validate Project Core Documentation
Validate Omenward GDD Sheet Adoption
Validate Base v9 adoption
```

모두 PR exact HEAD에서 success여야 한다.

## 8. Blocker 검색

`04_누락_충돌_감사!A1:H300`에서 다음 실제 데이터 행이 없어야 한다.

```text
OPEN_P0
OPEN_P1
MERGE_BLOCKER
```

`OPEN_NUMERIC_GATE`는 후속 결정 대기 상태이며 위 blocker 문자열과 동일하지 않다.

## 9. 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MITIGATION_AND_PROTECTION_NUMERIC_DEFAULTS_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SHEET_WRITES = PLANNING_DATA_ONLY
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
FIXED_TICK_RATE = PENDING
MS_TO_TICK_CONVERSION = PENDING
SOURCE_TARGET_MODIFIER_STACKING = PENDING
EXACT_UNIT_HERO_BUILDING_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 10. 카운터·다음 Gate

```text
GRILL_ME_COUNT = 4/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
NEXT_PREFLIGHT = AT_10_OF_10
CURRENT_PLANNING_PR = RESOLVE_FROM_OPEN_PR
LAST_MAINTENANCE_PR = 132
```
