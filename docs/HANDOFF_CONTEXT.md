# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_APPROVED
current_validation_decision: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
parent_semantics_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_harness_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-simulation-harness-planning-20260803
current_planning_pr: RESOLVE_FROM_OPEN_PR
last_merged_planning_pr: 129
last_maintenance_pr: 132
last_maintenance_commit: 970ca7c52d757806c6968b55808346ac8a50b3ea
base: 9.4.3_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED
product_code_authority: NONE
simulation_tool_code_authority: NONE
codex: BLOCKED
current_grill_me_count: 4
future_merge_cadence: 10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
```

최신 Decision은 방어 공식과 Barrier·Redirection·Health Floor·Status 초기 수치를 승인한다. 제품·도구 코드, simulation, runtime, human QA, image·animation·HX는 승인되지 않았다.

## 1. 제품 정체성

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

검증 계층은 `SpinSnapshot·TokenSource·비가역 전선 커밋 → 전투 결과`의 인과를 증명하기 위한 제작 기반이며 핵심 플레이를 대체하지 않는다.

## 2. 현재 책임 원본

- Harness 범위: `docs/design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`
- 공통 전투 Schema: `docs/design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md`
- Damage·Protection·Status 의미: `docs/design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md`
- Mitigation·Protection 수치: `docs/design/APPROVED_OMENWARD_MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_2026-08-03.md`
- 영웅 Trigger·파워: 관련 `APPROVED_OMENWARD_HERO_*` 문서
- 결정 원장: `docs/PROJECT_CANON_DECISION_LEDGER.md`
- 현재 구현: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- 미확정: `docs/DECISIONS_PENDING.md`
- Sheet 계약: `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`

## 3. 현재 검증 계층

```text
P0 Deterministic Harness Scope
P1 Core-First Common Combat Schema·R00~R130
P2 Damage·Protection·Status Semantics
P3 Mitigation·Protection Numeric Defaults
P4 Fixed Tick·Time·Activation — NEXT
```

## 4. Harness 상위 구조

```text
versioned fixture
+ fixed integer tick
+ named RNG streams
+ stable IDs
+ ordered commands
+ pure domain transition
→ ordered events
→ normalized state
→ metrics
→ fingerprint
```

production Scene·render·audio·NavigationServer·PhysicsServer·frame delta는 초기 Harness 권위가 아니다.

## 5. Common Combat 결정

```text
CombatRunState
LaneState[TOP,MID,BOTTOM]
CombatantState / BuildingState / ObjectiveState
DeploymentProvenance
OrderedCommand
ActionIntent / EffectIntent
ProtectionInstance / StatusInstance
PendingCommit / ActiveEffect
RngStreamState
```

```text
SpinSnapshot
→ PendingReward
→ TokenInstance / TokenSource
→ lane commit
→ deployment_id
→ combat event and result
```

## 6. Fixed Phase Order

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

동일 tick actor는 같은 post-movement snapshot에서 commit한다.

## 7. Damage·Protection·Status 의미

```text
KINETIC → ARMOR
ARCANE  → RESISTANCE
```

```text
CHANNEL != DELIVERY_TAG != TARGET_PROFILE
BARRIER != HP != HEAL != DEFENSE
RESTORE != NEGATIVE_DAMAGE
HEALTH_FLOOR != HEAL != REVIVE
TRANSFER_DEPTH_MAX = 1
SECOND_MITIGATION_PASS = FORBIDDEN
```

```text
R80A validity
→ R80B protection setup
→ R80C mitigation and Barrier
→ R80D redirection and Floor
→ R80E HP delta and Restore
→ R80F Status and post-hit
→ R80G death mark
```

## 8. 수치 기본값

### 방어 공식

```text
raw_effective_defense = base + additive_buff - additive_debuff
effective_defense = clamp(raw_effective_defense, 0, 300)
denominator = 100 + effective_defense
post_mitigation = adjusted_damage <= 0
  ? 0
  : max(1, (adjusted_damage * 100 + floor(denominator/2)) div denominator)
```

### Barrier

```text
PER_APPLICATION_CAP = floor(max HP * 20%)
TOTAL_CAP = floor(max HP * 30%)
DEFAULT_DURATION = 3000ms
EXCESS = DISCARDED
CONSUME = priority → oldest → stable ID
```

### Redirection·Floor

```text
DEFAULT_REDIRECTION = 30%
MAX_RECIPIENTS = 1
INVALID_RECIPIENT = RETURN_TO_ORIGINAL_TARGET
DEFAULT_HEALTH_FLOOR = 1 HP
FLOOR_TRIGGER = instance당 1회
FLOOR_GROUP = exclusive
```

### Status

```text
ADD_STACKS_DEFAULT_CAP = 3
DOT_HOT_PULSE = 1000ms
CONTROL_DURATION_MAX = 2000ms
SAME_CONTROL_GROUP_LOCKOUT = 1000ms
```

밀리초→tick 변환은 다음 Decision 전까지 구현하지 않는다.

## 9. 조기 Stop-Ship

```text
FRONTLINE_MEAN_BARRIER_UPTIME > 40%
OR
BARRIER_ABSORBED / POST_MITIGATION_INCOMING_DAMAGE > 35%
```

최종 acceptance가 아니라 조기 후보 분류다.

## 10. 영웅 검증 대상

```text
A = 표준 영웅
B = 같은 source archetype 해금 이름 지정 영웅
C = 같은 계열 표준 전설
```

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

초기 5명은 공통 Damage·Protection·Status·Timer·Event 계약을 소비한다.

## 11. Event·Metric

```text
RAW_DAMAGE
→ ADJUSTED_DAMAGE
→ EFFECTIVE_DEFENSE
→ POST_MITIGATION_DAMAGE
→ BARRIER_ABSORBED
→ CANDIDATE_HP_LOSS
→ REDIRECTED_HP_LOSS
→ HEALTH_FLOOR_PREVENTED
→ FINAL_HP_LOSS
```

root_effect_id·source·target·tick·phase·deployment_id를 보존한다.

## 12. 적대적 감사

```text
OMW-AUD-208 ~ 220 = Harness
OMW-AUD-221 = Sheet correction / resolved
OMW-AUD-222 ~ 232 = Common Combat
OMW-AUD-233 ~ 246 = Damage Semantics
OMW-AUD-247 ~ 260 = Numeric Defaults
```

## 13. 구현 경계·다음 작업

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MITIGATION_AND_PROTECTION_NUMERIC_DEFAULTS_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
FIXED_TICK_RATE = PENDING
MS_TO_TICK_CONVERSION = PENDING
SOURCE_TARGET_MODIFIER_STACKING = PENDING
EXACT_UNIT_HERO_BUILDING_VALUES = PENDING
A_B_C_SAMPLE_AND_TOLERANCE = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

```text
GRILL_ME_COUNT = 4/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
```
