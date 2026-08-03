# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-03
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
parent_semantics_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_harness_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
parent_gameplay_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-simulation-harness-planning-20260803
current_planning_pr: RESOLVE_FROM_OPEN_PR
last_merged_planning_pr: 129
last_merged_planning_commit: 173a408eb7b89992a81165438d97946167db0e14
last_maintenance_pr: 132
last_maintenance_commit: 970ca7c52d757806c6968b55808346ac8a50b3ea
active_base: 9.4.3
product_code_authority: NONE
simulation_tool_code_authority: NONE
sheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
grill_me_approved_since_last_merge: 4
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
next_gate: OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
```

## 1. 상태 언어

```text
USER_APPROVED_PLAN
!= PRODUCT_IMPLEMENTED
!= SIMULATION_TOOL_IMPLEMENTED
!= SIMULATION_EXECUTED
!= AUTOMATED_VALIDATED
!= HUMAN_VALIDATED
```

```text
MAIN_CANONICAL_NOT_IMPLEMENTED
= approved planning merged into main
+ product code/data/Scene/Resource unchanged
```

## 2. 현재 최상위 Decision

| Decision ID | 상태 | 핵심 결정 | 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1` | `USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED` | 공통 쌍곡선 방어식, defense 0~300, 정수 half-up, Barrier 20/30%·3000ms, 30% one-hop 이전, Floor 1 HP, Status 3/1000/2000/1000ms | `design/APPROVED_OMENWARD_MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_2026-08-03.md` | fixed tick·ms 변환·modifier stacking·code·simulation pending |
| `OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1` | `USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED` | KINETIC/ARCANE, Armor/Resistance, channel/tag/profile 분리, R80A~G, Barrier/Restore/Status 의미 | `design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md` | numeric defaults는 자식 Decision으로 승인, runtime pending |
| `OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1` | `USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED` | core-first 전투 상태, deployment provenance, quantized 2D, R00~R130, same-tick snapshot·barrier, post-death objective | `design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md` | time·movement·content values·implementation pending |
| `OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1` | `USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED` | headless pure-domain fixed-tick Harness, named RNG, stable ID, event, fingerprint, T0~T3 | `design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md` | tool code·fixture·execution pending |
| `OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1` | `USER_APPROVED / MAIN_CANONICAL / NOT_IMPLEMENTED` | 공개 Trigger·same-lane filter·priority·stable tie-break·commit snapshot, A/B/C 파워 위계 | 관련 Hero 책임 원본 | exact values·simulation·runtime·human pending |

## 3. Harness 계약

```text
versioned fixture
+ explicit fixed integer tick
+ named RNG streams
+ stable object IDs
+ ordered external commands
+ pure domain transition
→ ordered event log
→ normalized final state
→ metrics summary
→ deterministic fingerprint
```

```text
GLOBAL_RANDOM_API = FORBIDDEN
WALL_CLOCK = FORBIDDEN
VARIABLE_FRAME_DELTA = FORBIDDEN
UNSORTED_COLLECTION_ORDER = FORBIDDEN
```

Headless와 engine callback은 실행 수단이며 결정론 자체가 아니다.

## 4. 공통 Combat 계약

```text
CORE_FIRST_COMMON_SCHEMA = REQUIRED
HERO_FIRST_SPECIAL_CASE_SCHEMA = REJECTED
FULL_SYSTEM_SINGLE_SCHEMA = DEFERRED
```

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

## 5. Fixed Phase Order

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

모든 적격 actor는 같은 post-movement snapshot에서 commit한다.

## 6. Damage·Protection·Status 의미

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
TRUE_DAMAGE / EXECUTE / REVIVE = FORBIDDEN_CURRENT_SLICE
```

## 7. 방어 공식·초기 수치

```text
raw_effective_defense = base + additive_buff - additive_debuff
effective_defense = clamp(raw_effective_defense, 0, 300)
denominator = 100 + effective_defense
post_mitigation = adjusted_damage <= 0
  ? 0
  : max(1, (adjusted_damage * 100 + floor(denominator/2)) div denominator)
```

```text
BARRIER_PER_APPLICATION_CAP = floor(max HP * 20%)
BARRIER_TOTAL_CAP = floor(max HP * 30%)
BARRIER_DEFAULT_DURATION = 3000ms
BARRIER_EXCESS = DISCARDED
```

```text
REDIRECTION_DEFAULT = 30%
REDIRECTION_RECIPIENT_MAX = 1
INVALID_RECIPIENT = RETURN_TO_ORIGINAL_TARGET
HEALTH_FLOOR_DEFAULT = 1 HP / one trigger / exclusive group
```

```text
ADD_STACKS_DEFAULT_CAP = 3
DOT_HOT_PULSE_INTERVAL = 1000ms
CONTROL_DURATION_MAX = 2000ms
SAME_CONTROL_GROUP_LOCKOUT = 1000ms
```

## 8. 조기 Stop-Ship Guard

```text
FRONTLINE_MEAN_BARRIER_UPTIME > 40%
OR
BARRIER_ABSORBED / POST_MITIGATION_INCOMING_DAMAGE > 35%
```

이는 최종 balance acceptance가 아니라 조기 중단 후보 분류다.

## 9. 동일 Tick 불변식

```text
ALL_ELIGIBLE_ACTORS_COMMIT_FROM_SAME_PHASE_SNAPSHOT
SEQUENTIAL_ENTITY_ID_KILL_ADVANTAGE = FORBIDDEN
FALLBACK_RETARGET_AFTER_COMMIT = FORBIDDEN
DEATH_FINALIZATION_BEFORE_DAMAGE_BATCH_END = FORBIDDEN
OBJECTIVE_USES_POST_DEATH_SURVIVORS = REQUIRED
HEALTH_FLOOR_APPLIES_TO_TARGET_BATCH = REQUIRED
FLOAT_ROUNDING_IN_DETERMINISTIC_RESOLVER = FORBIDDEN
```

## 10. 검증 Tier

```text
T0 = fixture·schema·numeric default validation
T1 = replay·intermediate integer·event parity
T2 = same-tick·damage·Barrier·transfer·Floor·Status invariants
T3 = paired A/B/C metrics with all three lanes
T4 = aggregate balance after acceptance approval
T5 = product runtime adapter after separate authorization
```

## 11. 기존 Hero 정본 계보

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
MAX_STORED_READY_COUNT = 1
MANUAL_CAST_OR_TARGET = FORBIDDEN
ACTIVE_EFFECT_OR_UNRESOLVED_COMMIT_STAGE_CARRY = FORBIDDEN
```

영웅은 공통 Combatant·Intent·Protection·Status·Timer·Event 계약을 소비한다.

## 12. 비카운트 정책·Sync

| ID | 상태 | 역할 |
|---|---|---|
| `OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1` | `ACTIVE_STANDING_POLICY / MAIN_CANONICAL` | 모든 Grill Me에 benchmark·difference·production cost·QA·adversarial review 적용 |
| `OMW-SYNC-20260803-LIFECYCLE-STATUS-CLEANUP-V1` | `MAINTENANCE_SYNC / MAIN_CANONICAL / NON_COUNTER` | Decision 생명주기 우선순위 교정 |
| `OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1` | `MAINTENANCE_SYNC / MAIN_CANONICAL / NON_COUNTER` | 구현 상태·미확정 목록 최신화 |
| `OMW-SYNC-20260803-PR133-HEAD-READBACK-CORRECTION-V1` | `SHEET_MAINTENANCE / NON_COUNTER` | stale PR head 교정 |

## 13. 적대적 감사 계보

```text
OMW-AUD-208 ~ 220 = Harness
OMW-AUD-221 = Sheet correction / resolved
OMW-AUD-222 ~ 232 = Common Combat
OMW-AUD-233 ~ 246 = Damage Semantics
OMW-AUD-247 ~ 260 = Numeric Defaults
```

## 14. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MITIGATION_AND_PROTECTION_NUMERIC_DEFAULTS_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
SIMULATION_TOOL_CODE_AUTHORITY = NONE
FIXED_TICK_RATE = PENDING
MS_TO_TICK_CONVERSION = PENDING
SOURCE_TARGET_MODIFIER_STACKING = PENDING
DEFENSE_PENETRATION = FORBIDDEN_UNTIL_SEPARATE_DECISION
EXACT_UNIT_HERO_BUILDING_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 15. 카운터·다음 Gate

```text
CURRENT_COUNT_SINCE_MERGE = 4_OF_10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
NEXT_PREFLIGHT_AT = 10_OF_10
```
