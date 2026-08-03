# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-03
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
current_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_validation_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
parent_gameplay_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
last_maintenance_pr: 132
last_maintenance_commit: 970ca7c52d757806c6968b55808346ac8a50b3ea
current_planning_pr: RESOLVE_FROM_OPEN_PR
current_branch: gpt/omenward-simulation-harness-planning-20260803
current_pr_head: RESOLVE_FROM_PR
status: PROJECT_SHEET_CONFIGURED / DECISION_SYNC_PENDING / COUNTER_3_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
```

이 문서는 GitHub 정본과 연결 Google Sheet의 동기화 계약을 소유한다. Sheet는 `USER_FACING_GDD_WORKSPACE`이며 모든 쓰기는 Decision ID와 근거를 갖춘 `PROPOSED_SHEET_CHANGE`로 처리하고 bounded read-back·CI를 통과해야 한다.

## 1. 현재 Decision

```text
OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
```

승인 범위:

```text
KINETIC → ARMOR
ARCANE → RESISTANCE
+ delivery tag and target profile separation
+ Damage/Restore/Protection/Status intent separation
+ R80A~R80G semantics
+ barrier·one-hop redirection·health floor·restore meanings
+ status taxonomy·stacking·expiry
+ raw/resolved event and metric separation
+ true damage·execute·revive forbidden current slice
```

Simulation tool 구현·실행·밸런스 결론은 승인되지 않았다.

## 2. Sheet 반영 범위

| 목적 | 범위 |
|---|---|
| Hub·Decision·카운터·PR HEAD | `00_프로젝트_허브!E2:L2` |
| 작업순서 | `01_작업순서!A43:N43` |
| 현재 확정 Decision | `02_현재_확정결정!A51:M51` |
| 공식 벤치마크·내부 근거 | `03_근거_라이브러리!A39:J42` |
| 적대적 감사 | `04_누락_충돌_감사!A233:H246` |
| GDD 요약 | `05_GDD_요약!B8:J9` |
| 핵심루프 연결 | `12_핵심루프!A24:J24` |
| 조작·게임규칙 연결 | `15_조작_게임규칙!A27:J27` |
| 핵심시스템 연결 | `40_핵심시스템_메인콘텐츠!A27:J27` |
| 성장·경제 경계 | `41_성장_경제!A37:I37` |
| 콘텐츠 fixture 연결 | `50_메인콘텐츠!A34:J34` |
| UX·로그 연결 | `60_UX_UI_접근성!A35:J35` |
| 아트·오디오 경계 | `70_아트_오디오_에셋!A18:J18` |
| 변경 이력 | `99_변경이력!A56:H56` |

## 3. 벤치마크 근거

Sheet 근거 행은 exact 값 권위가 아니라 제작 경계로 기록한다.

1. Riot TFT 공식 Roles·Item 자료 — Armor와 Magic Resistance의 분리된 방어축과 inspect 가능한 role/damage 정보.
2. Guild Wars 2 Barrier — 실제 HP 전에 흡수되는 임시 health buffer와 분리 UI·cap.
3. Overwatch 2019-12 공식 patch — barrier uptime이 전투 pace를 지배할 때 barrier health를 줄인 제작 의도.
4. OMENWARD internal canon — 세 전선·SpinSnapshot·TokenSource·비가역 배치와 결과 provenance.

적용 경계:

```text
EXTERNAL_EXACT_VALUES = NOT_AUTHORITY
TWO_DEFENSE_AXES = ADAPTED
TEMPORARY_SEPARATE_BARRIER = ADAPTED
BARRIER_OVERCENTRALIZATION = STOP_SHIP_CANDIDATE
```

## 4. 감사 행

```text
OMW-AUD-233 ~ OMW-AUD-246
```

대상:

- channel/tag conflation
- flying treated as damage type
- barrier double counting
- recursive HP-loss transfer
- second mitigation on transferred loss
- retroactive same-tick status cancellation
- unspecified status stacking
- hidden immunity exceptions
- restore as negative damage
- true/execute/revive bypass
- accidental objective damage
- barrier overcentralization
- color-only channel UI
- raw/final metric double counting

이전 감사:

```text
OMW-AUD-208 ~ OMW-AUD-220 = Harness
OMW-AUD-221 = stale Sheet PR-head / RESOLVED / NON_COUNTER
OMW-AUD-222 ~ OMW-AUD-232 = common combat schema·resolution order
```

## 5. 핵심 Damage·Protection·Status 계약

```text
KINETIC → ARMOR
ARCANE → RESISTANCE
```

```text
DELIVERY_TAGS = BASIC / SKILL / AREA / DAMAGE_OVER_TIME / ENVIRONMENT / TRANSFERRED
TARGET_PROFILE = UNIT / BUILDING / OBJECTIVE + GROUND / FLYING
```

```text
R80A VALIDITY_AND_ELIGIBILITY
R80B PROTECTION_SETUP
R80C DAMAGE_MITIGATION_AND_BARRIER
R80D HP_LOSS_REDIRECTION_AND_FLOOR
R80E HP_DELTA_AND_RESTORE
R80F STATUS_APPLICATION_AND_POST_HIT_QUEUE
R80G DEATH_OR_DESTRUCTION_MARK
```

```text
BARRIER != HP_OR_HEAL
RESTORE != NEGATIVE_DAMAGE
TRANSFER_DEPTH_MAX = 1
RECURSIVE_REDIRECTION = FORBIDDEN
SECOND_MITIGATION_PASS = FORBIDDEN
RETROACTIVE_STATUS_COMMIT_CANCELLATION = FORBIDDEN
TRUE_DAMAGE_EXECUTE_REVIVE = FORBIDDEN_CURRENT_SLICE
```

Status family:

```text
STAT_MODIFIER / CONTROL / DAMAGE_OVER_TIME / HEAL_OVER_TIME
IMMUNITY / TARGETING_RULE / MOVEMENT_RULE / MARK
```

Stacking policy:

```text
REPLACE_IF_STRONGER / REFRESH_DURATION / ADD_STACKS_CAPPED
INDEPENDENT_BY_SOURCE / EXCLUSIVE_GROUP
```

## 6. Event·Metric Contract

```text
RAW_DAMAGE != POST_MITIGATION_DAMAGE != BARRIER_ABSORBED != FINAL_HP_LOSS
RESTORE_AMOUNT = SEPARATE
STATUS_RESULT = SEPARATE
```

모든 event는 root effect·source·target·channel/tag·tick/phase/sequence와 해당 시 deployment_id를 보존한다.

## 7. 쓰기·검증 절차

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
10. Draft 유지 — 3/10
```

## 8. 필수 CI

```text
Validate Project Core Documentation
Validate Omenward GDD Sheet Adoption
Validate Base v9 adoption
```

모두 PR exact HEAD에서 `success`여야 한다.

## 9. blocker 검색

`04_누락_충돌_감사!A1:H300`에서 다음 문자열의 실제 데이터 행이 없어야 한다.

```text
OPEN_P0
OPEN_P1
MERGE_BLOCKER
```

## 10. 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DAMAGE_PROTECTION_STATUS_SEMANTICS_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SHEET_WRITES = PLANNING_DATA_ONLY
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
DAMAGE_CHANNELS = KINETIC_AND_ARCANE
TRUE_DAMAGE_EXECUTE_REVIVE = FORBIDDEN_CURRENT_SLICE
EXACT_MITIGATION_FORMULA = PENDING
EXACT_ARMOR_RESISTANCE_DEFAULTS = PENDING
EXACT_BARRIER_BUDGET_CAP_DURATION = PENDING
EXACT_STATUS_STACK_CAP_DURATION = PENDING
EXACT_TICK_RATE_AND_ACTIVATION_POLICY = PENDING
EXACT_HERO_TRIGGER_TIMER_EFFECT_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 11. 카운터·다음 Gate

```text
GRILL_ME_COUNT = 3/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
NEXT_PREFLIGHT = AT_10_OF_10
CURRENT_PLANNING_PR = RESOLVE_FROM_OPEN_PR
LAST_MAINTENANCE_PR = 132
```
