# Active Context

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: FIXED_TICK_TIME_AND_ACTIVATION_DEFAULTS_APPROVED
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
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
current_grill_me_count: 5
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: OUT_OF_SCOPE_REQUIRES_SEPARATE_CONTRACT
preflight: NEXT_AT_10_OF_10
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

`current_main`, `context_baseline_commit`, `current_planning_pr`은 실행 시점 저장소에서 해석한다. 최신 Decision은 시간축 기획 계약만 승인하며 제품 코드·Simulation tool·fixture·test·이미지·animation·HX 권한을 부여하지 않는다.

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

검증 Harness·전투 Schema·피해 공식·시간축은 코어 재미를 대체하지 않고 플레이어 선택과 결과의 인과를 검증한다.

## 2. 승인된 검증 계층

### P0 — Deterministic Harness Scope

`design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`

```text
versioned fixture + explicit integer tick + named RNG + stable IDs
→ ordered events + normalized state + metrics + fingerprint
```

### P1 — Core-First Common Combat Schema

`design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md`

```text
CombatRunState / LaneState[TOP,MID,BOTTOM]
Combatant / Building / Objective / DeploymentProvenance
R00~R130 phase resolver
```

### P2 — Damage·Protection·Status Semantics

`design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md`

```text
KINETIC → ARMOR
ARCANE  → RESISTANCE
```

Channel·delivery·target profile을 분리하고 Barrier·Restore·redirection·Health Floor·Status를 독립 의미로 처리한다.

### P3 — Mitigation·Protection Numeric Defaults

`design/APPROVED_OMENWARD_MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_2026-08-03.md`

```text
effective_defense = clamp(base + buff - debuff, 0, 300)
post_mitigation = max(1, positive_integer_half_up(adjusted * 100 / (100 + defense)))
Barrier = application 20% / total 30% / 3000ms
Redirection = 30% / recipient 1
Health Floor = 1 HP / instance 1회
Status = stack 3 / pulse 1000ms / control 2000ms / lockout 1000ms
```

### P4 — Fixed Tick·Time·Activation Defaults

`design/APPROVED_OMENWARD_FIXED_TICK_TIME_AND_ACTIVATION_DEFAULTS_2026-08-03.md`

```text
DOMAIN_TPS = 30
AUTHORING_TIME = integer ms
COMBAT_TIME_AUTHORITY = integer tick
duration_ticks = ceil(duration_ms * 30 / 1000)
ACTIVE_RANGE = [start_tick, end_tick_exclusive)
SPAWN_AT_T → ACTIVATE_AT_T_PLUS_1
```

```text
3000ms = 90 ticks
1000ms = 30 ticks
2000ms = 60 ticks
1000ms = 30 ticks
```

## 3. Tick·Activation 불변식

```text
R00_EXPIRES_END_TICK_EXCLUSIVE_BEFORE_COMMANDS
R10_ACCEPTS_ONLY_COMMANDS_SCHEDULED_FOR_CURRENT_TICK
R20_SPAWNED_ENTITY_EXISTS_AND_IS_TARGETABLE
R20_SPAWNED_ENTITY_CANNOT_COMMIT_ACTION_UNTIL_NEXT_TICK
ACTIVE_ACTOR_PROTECTION_COMMIT_CAN_MATERIALIZE_AT_SAME_TICK_R80B
WALL_CLOCK_TIMER_ANIMATION_CALLBACK = NON_AUTHORITATIVE
DOMAIN_TICK_SKIP_OR_MERGE = FORBIDDEN
```

Tick `T`에 생성된 개체는 같은 Tick 공격받을 수 있으나 이동·대상 선택·공격·스킬·보호·점령 기여는 `T+1`부터 가능하다.

## 4. Pause·Save·Render 경계

```text
ACTIVE_COMBAT = DOMAIN_TICK_ADVANCES
MAINTENANCE_PREPARATION_APPLICATION_PAUSE = DOMAIN_TICK_PAUSED
SAVE_BOUNDARY = AFTER_R130_ONLY
SAVE_TIMER = INTEGER_TICKS
RENDER_INTERPOLATION = VISUAL_ONLY
GODOT_TIMER = NON_AUTHORITATIVE_FOR_COMBAT
```

Normal/Danger의 pause 허용 정책은 별도 UX·콘텐츠 권위가 소유한다. 허용된 pause에서는 모든 전투 도메인 시간이 함께 멈춘다.

## 5. 전투·수치 불변식

```text
ALL_ELIGIBLE_ACTORS_COMMIT_FROM_SAME_PHASE_SNAPSHOT
SEQUENTIAL_ENTITY_ID_KILL_ADVANTAGE = FORBIDDEN
FALLBACK_RETARGET_AFTER_COMMIT = FORBIDDEN
DEATH_FINALIZATION_BEFORE_DAMAGE_BATCH_END = FORBIDDEN
OBJECTIVE_USES_POST_DEATH_SURVIVORS = REQUIRED
NEGATIVE_DEFENSE = FORBIDDEN
DEFENSE_MAX = 300
MINIMUM_VALID_DAMAGE = 1
TRANSFER_DEPTH_MAX = 1
SECOND_MITIGATION_PASS = FORBIDDEN
```

## 6. 조기 Stop-Ship Guard

```text
FRONTLINE_MEAN_BARRIER_UPTIME > 40_PERCENT
OR
BARRIER_ABSORBED / POST_MITIGATION_INCOMING_DAMAGE > 35_PERCENT
```

최종 밸런스 합격선이 아니라 Barrier가 병종·전선 선택을 대체하는지 조기 분류하는 guard다.

## 7. 적대적 감사 계보

```text
OMW-AUD-208 ~ 220 = Harness scope
OMW-AUD-221 = Sheet stale PR-head correction / RESOLVED / NON_COUNTER
OMW-AUD-222 ~ 232 = common combat schema·resolution
OMW-AUD-233 ~ 246 = damage·protection·status semantics
OMW-AUD-247 ~ 260 = mitigation·protection numeric defaults
OMW-AUD-261 = CI compatibility-marker recovery / RESOLVED / NON_COUNTER
OMW-AUD-262 ~ 275 = fixed tick·time·activation defaults
```

## 8. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = FIXED_TICK_TIME_ACTIVATION_DEFAULTS_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
DOMAIN_TPS = 30_APPROVED_NOT_IMPLEMENTED
MS_TO_TICK_CONVERSION = APPROVED_NOT_IMPLEMENTED
SOURCE_TARGET_MODIFIER_STACKING = PENDING
EXACT_UNIT_HERO_BUILDING_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. 다음 Gate

```text
GRILL_ME_COUNT = 5/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-MODIFIER-STACKING-AND-EFFECT-PRECEDENCE-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
