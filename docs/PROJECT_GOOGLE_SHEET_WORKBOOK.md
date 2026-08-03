# OMENWARD 프로젝트 Google Sheets Workbook

```yaml
updated_at: 2026-08-03
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
spreadsheet_title: 오멘워드(OMENWARD)
workspace_role: USER_FACING_GDD_WORKSPACE
change_protocol: PROPOSED_SHEET_CHANGE
current_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_validation_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
parent_gameplay_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
last_maintenance_pr: 132
last_maintenance_commit: 970ca7c52d757806c6968b55808346ac8a50b3ea
current_planning_pr: RESOLVE_FROM_OPEN_PR
current_branch: gpt/omenward-simulation-harness-planning-20260803
current_pr_head: RESOLVE_FROM_PR
status: PROJECT_SHEET_CONFIGURED / DECISION_SYNC_PENDING / COUNTER_2_OF_10
product_code_authority: NONE
simulation_tool_code_authority: NONE
```

이 문서는 GitHub 정본과 연결 Google Sheet의 동기화 계약을 소유한다. Sheet는 `USER_FACING_GDD_WORKSPACE`이며 모든 쓰기는 Decision ID와 근거를 갖춘 `PROPOSED_SHEET_CHANGE`로 처리하고 bounded read-back·CI를 통과해야 한다.

## 1. 현재 Decision

```text
OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
```

승인 범위:

```text
core-first common combat schema
+ roulette deployment provenance
+ quantized 2D position
+ canonical lane/entity/event order
+ R00~R130 fixed-tick phase order
+ same-tick snapshot·intent·barrier
+ post-death objective resolution
+ Hero/Legendary extension seam
```

공통 Schema는 룰렛·경제 전체를 재실행하지 않는다. 전장 유닛은 `SpinSnapshot·TokenSource·lane commit→deployment_id` provenance를 필수로 보존한다.

Simulation tool 구현·실행·밸런스 결론은 승인되지 않았다.

## 2. Sheet 반영 범위

| 목적 | 범위 |
|---|---|
| Hub·Decision·카운터·PR HEAD | `00_프로젝트_허브!E2:L2` |
| 작업순서 | `01_작업순서!A42:N42` |
| 현재 확정 Decision | `02_현재_확정결정!A50:M50` |
| 공식 벤치마크·내부 근거 | `03_근거_라이브러리!A35:J38` |
| 적대적 감사 | `04_누락_충돌_감사!A222:H232` |
| GDD 요약 | `05_GDD_요약!B8:J9` |
| 핵심루프 연결 | `12_핵심루프!A23:J23` |
| 조작·게임규칙 연결 | `15_조작_게임규칙!A26:J26` |
| 핵심시스템 연결 | `40_핵심시스템_메인콘텐츠!A26:J26` |
| 성장·경제 경계 | `41_성장_경제!A36:I36` |
| 콘텐츠 fixture 연결 | `50_메인콘텐츠!A33:J33` |
| UX·로그 연결 | `60_UX_UI_접근성!A34:J34` |
| 아트·오디오 제외 경계 | `70_아트_오디오_에셋!A17:J17` |
| 변경 이력 | `99_변경이력!A55:H55` |

## 3. 벤치마크 근거

Sheet 근거 행은 exact 값 권위가 아니라 제작 경계로 기록한다.

1. Godot fixed physics processing과 variable idle processing 차이.
2. `RandomNumberGenerator` instance별 seed·state.
3. JSON 숫자 처리와 canonical state hash 경계.
4. OMENWARD core: 세 전선·SpinSnapshot·TokenSource·비가역 배치·점령 인과.

```text
HEADLESS != DETERMINISTIC
ENGINE_FIXED_CALLBACK != COMPLETE_DETERMINISM
RAW_JSON_TEXT != CANONICAL_STATE_HASH
```

## 4. 감사 행

```text
OMW-AUD-222 ~ OMW-AUD-232
```

대상:

- roulette provenance omission
- Hero special-case schema pollution
- sequential stable-ID action bias
- early death finalization
- hidden fallback retarget
- dead-unit objective contribution
- retroactive building-action cancellation
- 1D position cross-lane distortion
- exact values smuggled into schema
- SceneTree order leakage
- ambiguous fingerprint phase

`OMW-AUD-221`은 이전 Sheet-only stale PR-head 교정이며 `RESOLVED / NON_COUNTER`다.

## 5. 핵심 Schema·순서

```text
CombatRunState
LaneState
CombatantState
BuildingState
ObjectiveState
DeploymentProvenance
OrderedCommand
ActionIntent / EffectIntent
StatusInstance / PendingCommit / ActiveEffect
RngStreamState
```

```text
R00 TICK_OPEN_AND_EXPIRE
R10 ORDERED_COMMAND_INGEST
R20 SPAWN_AND_ACTIVATION
R30 MOVEMENT_INTENT_BUILD
R40 MOVEMENT_RESOLVE
R50 TARGET_SENSE_AND_SELECT
R60 ACTION_AND_SKILL_COMMIT
R70 IMPACT_AND_EFFECT_INTENT_BUILD
R80 DAMAGE_PROTECTION_STATUS_APPLY
R90 DEATH_AND_DESTRUCTION_FINALIZE
R100 OBJECTIVE_AND_OWNERSHIP_RESOLVE
R110 TIMER_COOLDOWN_STATUS_ADVANCE
R120 METRICS_EVENT_FINGERPRINT
R130 TICK_CLOSE
```

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
10. Draft 유지 — 2/10
```

## 7. 필수 CI

```text
Validate Project Core Documentation
Validate Omenward GDD Sheet Adoption
Validate Base v9 adoption
```

모두 PR exact HEAD에서 `success`여야 한다.

## 8. blocker 검색

`04_누락_충돌_감사!A1:H300`에서 다음 문자열의 실제 데이터 행이 없어야 한다.

```text
OPEN_P0
OPEN_P1
MERGE_BLOCKER
```

## 9. 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = COMMON_COMBAT_SCHEMA_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SHEET_WRITES = PLANNING_DATA_ONLY
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
EXACT_TICK_RATE = PENDING
EXACT_ACTIVATION_POLICY = PENDING
EXACT_DAMAGE_DEFENSE_PROTECTION_FORMULAS = PENDING
EXACT_HERO_TRIGGER_TIMER_EFFECT_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 10. 카운터·다음 Gate

```text
GRILL_ME_COUNT = 2/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
NEXT_PREFLIGHT = AT_10_OF_10
CURRENT_PLANNING_PR = RESOLVE_FROM_OPEN_PR
LAST_MAINTENANCE_PR = 132
```
