# Active Context

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: MODIFIER_STACKING_AND_EFFECT_PRECEDENCE_APPROVED
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1
parent_time_decision: OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
parent_numeric_decision: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
parent_semantics_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_harness_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_branch: main
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-simulation-harness-planning-20260803
active_base_version: 9.4.3
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
product_code_authority: NONE
simulation_tool_code_authority: NONE
codex_execution: BLOCKED
last_merged_planning_pr: 129
last_merged_planning_commit: 173a408eb7b89992a81165438d97946167db0e14
last_maintenance_pr: 132
last_maintenance_commit: 970ca7c52d757806c6968b55808346ac8a50b3ea
current_planning_pr: RESOLVE_FROM_OPEN_PR
current_grill_me_count: 6
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: OUT_OF_SCOPE_REQUIRES_SEPARATE_CONTRACT
preflight: NEXT_AT_10_OF_10
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

`current_main`, `context_baseline_commit`, `current_planning_pr`은 실행 시점 저장소에서 해석한다. 최신 Decision은 Modifier stacking·effect precedence 기획 계약만 승인하며 제품 코드·Simulation tool·fixture·test·이미지·animation·HX 권한을 부여하지 않는다.

## 1. 제품 정체성·핵심 재미

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
예고된 세 전선 공세 읽기
→ 제한된 건물·TokenSource로 세 원형 릴 설계
→ SpinSnapshot 결과 보관·판매·획득
→ 한 전선에 비가역 배치
→ 공통 자동전투·점령·건물 운영
→ provenance와 ordered event로 원인 복기
→ 다음 Stage 설계
```

검증 Stack은 코어 재미를 대체하지 않고 플레이어 선택과 결과의 인과를 검증한다.

## 2. 승인된 검증 계층

```text
P0 Harness Scope
P1 Common Combat Schema
P2 Damage/Protection/Status Semantics
P3 Mitigation/Protection Numeric Defaults
P4 Fixed Tick/Time/Activation Defaults
P5 Modifier Stacking/Effect Precedence
```

P5 책임 원본:

`design/APPROVED_OMENWARD_MODIFIER_STACKING_AND_EFFECT_PRECEDENCE_2026-08-03.md`

## 3. Modifier 핵심

```text
BASIS_POINTS = 10000
SOURCE_OUTGOING_RANGE = 50%~150%
TARGET_INCOMING_RANGE = 50%~150%
COMBINED_PRE_DEFENSE_RANGE = 25%~200%
```

```text
R60 = source outgoing snapshot
R80 = target incoming·defense·Barrier snapshot
```

```text
REFRESH_DURATION
REPLACE_IF_STRONGER
ADD_STACKS_CAPPED
INDEPENDENT_BY_SOURCE
EXCLUSIVE_GROUP
```

Armor·Resistance는 integer point additive만 허용한다. Generic flat damage, override, penetration, next-hit 소비형 Modifier는 현 Slice에서 금지한다.

## 4. Effect Precedence

```text
P00 Target validity
P10 Immunity
P20 Source snapshot load
P30 Target incoming aggregate
P40 Armor/Resistance mitigation
P50 Barrier
P60 Redirection
P70 Health Floor
P80 HP delta / Restore
P90 Status / post-hit
P100 Death pending
```

Transferred HP loss는 두 번째 Modifier·mitigation·Barrier pass를 거치지 않는다.

## 5. 시간·전투 불변식

```text
DOMAIN_TPS = 30
ACTIVE_RANGE = [start_tick,end_tick_exclusive)
SPAWN_AT_T → ACTIVATE_AT_T_PLUS_1
ALL_ELIGIBLE_ACTORS_COMMIT_FROM_SAME_PHASE_SNAPSHOT
DEATH_FINALIZE_AFTER_DAMAGE_BATCH
OBJECTIVE_USES_POST_DEATH_ACTIVE_SURVIVORS
WALL_CLOCK_TIMER_ANIMATION_CALLBACK = NON_AUTHORITATIVE
```

## 6. Trigger 의미

```text
ON_VALID_IMPACT
ON_POST_MITIGATION_DAMAGE
ON_BARRIER_ABSORBED
ON_FINAL_HP_LOSS
ON_STATUS_APPLIED
ON_TARGET_DEATH_FINALIZED
```

모호한 `on hit` 단독 정의는 금지한다.

## 7. 적대적 감사 계보

```text
OMW-AUD-208 ~ 220 = Harness scope
OMW-AUD-221 = Sheet stale PR-head correction / RESOLVED / NON_COUNTER
OMW-AUD-222 ~ 232 = common combat schema·resolution
OMW-AUD-233 ~ 246 = damage·protection·status semantics
OMW-AUD-247 ~ 260 = mitigation·protection numeric defaults
OMW-AUD-261 = CI compatibility-marker recovery / RESOLVED / NON_COUNTER
OMW-AUD-262 ~ 275 = fixed tick·time·activation defaults
OMW-AUD-276 ~ 289 = modifier stacking·effect precedence
```

## 8. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MODIFIER_STACKING_EFFECT_PRECEDENCE_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
MODIFIER_RESOLVER_CODE = NOT_AUTHORIZED
SPATIAL_QUANTIZATION_MOVEMENT_TARGETING = PENDING
EXACT_UNIT_HERO_BUILDING_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. 다음 Gate

```text
GRILL_ME_COUNT = 6/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-SPATIAL-QUANTIZATION-MOVEMENT-AND-TARGETING-DEFAULTS-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
