# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-03
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_validation_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
parent_gameplay_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
last_sync: OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1
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
grill_me_approved_since_last_merge: 3
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
next_gate: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
```

`current_main`과 `current_planning_pr`은 실행 시점에 저장소에서 해석한다. 최신 Decision은 피해·보호·상태 의미의 기획 계약만 승인하며 코드 구현·simulation 실행 권한을 부여하지 않는다.

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
= approved planning is merged into main
+ product code/data/Scene/Resource remains unchanged
```

## 2. 현재 최상위 Decision

| Decision ID | 상태 | 핵심 결정 | 책임 원본 | 미완료 경계 |
|---|---|---|---|---|
| `OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1` | `USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED` | KINETIC/ARCANE 두 채널, Armor/Resistance 방어축, delivery/target tag 분리, barrier·HP-loss redirection·restore·status 의미, true/execute/revive 금지 | `design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md` | exact formula·rounding·cap·duration·numeric defaults·code·fixture·execution pending |
| `OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1` | `USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED` | core-first 공통 전투 상태, 룰렛 배치 provenance, quantized 2D 위치, R00~R130 phase order, same-tick snapshot·intent·barrier, post-death objective | `design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md` | damage semantics는 child Decision으로 승인, exact technical defaults·code·fixture·execution pending |
| `OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1` | `USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED` | headless 순수 도메인 fixed-tick Harness, versioned fixture, named RNG, stable ID, event log, fingerprint, paired A/B/C 비교 | `design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md` | common schema·damage semantics는 후속 승인, tool code·execution pending |
| `OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1` | `USER_APPROVED / MAIN_CANONICAL / NOT_IMPLEMENTED` | 공개 Trigger·same-lane Filter·Priority·stable tie-break·commit Snapshot, A/B/C encounter 파워 위계 검증 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TRIGGER_TARGET_AND_POWER_BUDGET_VALIDATION_2026-08-03.md` | exact threshold·values·simulation·runtime·human pending |

## 3. Harness 상위 계약

```text
versioned fixture
+ explicit fixed integer tick
+ named RNG streams
+ stable object IDs
+ ordered external commands
+ pure domain state transitions
→ ordered event log
→ normalized final state
→ metrics summary
→ deterministic state fingerprint
```

```text
GLOBAL_RANDOM_API = FORBIDDEN
RANDOMIZE = FORBIDDEN
WALL_CLOCK = FORBIDDEN
VARIABLE_FRAME_DELTA = FORBIDDEN
FIXED_INTEGER_TICK = REQUIRED
STABLE_OBJECT_ID = REQUIRED
EXPLICIT_SORT_KEY = REQUIRED
UNSORTED_COLLECTION_ORDER = FORBIDDEN
```

headless는 실행 수단이며 결정론 자체가 아니다.

## 4. 공통 Combat Schema 결정

```text
CORE_FIRST_COMMON_SCHEMA = REQUIRED
HERO_FIRST_SPECIAL_CASE_SCHEMA = REJECTED
FULL_SYSTEM_SINGLE_SCHEMA = DEFERRED
```

필수 상태:

```text
CombatRunState
LaneState
CombatantState
BuildingState
ObjectiveState
DeploymentProvenance
OrderedCommand
ActionIntent / EffectIntent
ProtectionInstance / StatusInstance
PendingCommit / ActiveEffect
RngStreamState
```

`DeploymentProvenance`는 다음 인과를 보존한다.

```text
SpinSnapshot
→ PendingReward
→ TokenInstance / TokenSource
→ lane commit
→ deployment_id
→ combat event and result
```

전투 Harness는 룰렛을 재추첨하지 않는다.

## 5. 위치·Canonical Order

```text
position_q = {x_q, y_q, anchor_id}
lane_order = TOP(0), MID(1), BOTTOM(2)
canonical_key = lane_order → entity_kind_order → spawn_sequence → stable_entity_id → local_sequence
```

- quantized 2D 위치는 실제 거리 기반 cross-lane 효과를 보존한다.
- 1D lane 좌표만으로 거리 판정하는 것을 금지한다.
- Dictionary·SceneTree·callback 순서는 resolution 권위가 아니다.

## 6. Fixed-Tick Resolution Order

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

동일 tick actor는 같은 post-movement snapshot에서 action을 commit한다. 낮은 stable ID actor가 먼저 피해를 적용해 다른 actor의 같은 tick 합법 행동을 지우는 순차 편향을 금지한다.

## 7. Damage·Protection·Status 결정

### 7.1 Damage Channel

```text
KINETIC → ARMOR
ARCANE  → RESISTANCE
```

```text
DAMAGE_CHANNEL = exactly one
DELIVERY_TAGS = BASIC / SKILL / AREA / DAMAGE_OVER_TIME / ENVIRONMENT / TRANSFERRED
TARGET_PROFILE = UNIT / BUILDING / OBJECTIVE + GROUND / FLYING
```

AREA·DOT·SIEGE·FLYING은 damage channel이 아니다. 한 action이 두 channel을 사용하면 두 개의 명시적 DamageIntent로 분리한다.

### 7.2 R80 Semantics

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
raw damage
→ outgoing/incoming modifiers
→ Armor/Resistance hook
→ barrier absorption
→ candidate HP loss
→ one-hop redirection
→ health-floor clamp
→ HP delta or separate restore
→ status/post-hit queue
→ death_pending
```

### 7.3 Protection·Restore

```text
BARRIER != HP
BARRIER != HEAL
BARRIER != ARMOR_OR_RESISTANCE
TRANSFER_DEPTH_MAX = 1
RECURSIVE_REDIRECTION = FORBIDDEN
SECOND_MITIGATION_PASS = FORBIDDEN
RESTORE != NEGATIVE_DAMAGE
OVERHEAL_DEFAULT = DISCARDED
```

same-tick 합법 ProtectionIntent는 피해 전에 materialize한다. health floor는 damage clamp이며 heal·revive가 아니다.

### 7.4 Status

```text
STAT_MODIFIER
CONTROL
DAMAGE_OVER_TIME
HEAL_OVER_TIME
IMMUNITY
TARGETING_RULE
MOVEMENT_RULE
MARK
```

각 definition은 다음 중 하나의 stacking policy를 반드시 선언한다.

```text
REPLACE_IF_STRONGER
REFRESH_DURATION
ADD_STACKS_CAPPED
INDEPENDENT_BY_SOURCE
EXCLUSIVE_GROUP
```

일반 status는 이미 commit된 same-tick 행동을 소급 취소하지 않는다.

### 7.5 Current Slice Exclusions

```text
TRUE_DAMAGE = FORBIDDEN
EXECUTE_OR_INSTANT_KILL = FORBIDDEN
REVIVE = FORBIDDEN
FRIENDLY_FIRE = FORBIDDEN_BY_DEFAULT
SELF_DAMAGE = FORBIDDEN_BY_DEFAULT
OBJECTIVE_HP_DAMAGE = FORBIDDEN_BY_DEFAULT
```

## 8. Event·Metric Contract

```text
RAW_DAMAGE != POST_MITIGATION_DAMAGE != BARRIER_ABSORBED != FINAL_HP_LOSS
RESTORE_AMOUNT = SEPARATE
STATUS_RESULT = SEPARATE
```

모든 event는 root effect·source·target·channel/tag·tick/phase/sequence를 기록한다. 배치 유닛이면 deployment_id까지 역추적한다.

## 9. 동일 Tick 불변식

```text
ALL_ELIGIBLE_ACTORS_COMMIT_FROM_SAME_PHASE_SNAPSHOT
SEQUENTIAL_ENTITY_ID_KILL_ADVANTAGE = FORBIDDEN
FALLBACK_RETARGET_AFTER_COMMIT = FORBIDDEN
DEATH_FINALIZATION_BEFORE_DAMAGE_BATCH_END = FORBIDDEN
OBJECTIVE_USES_POST_DEATH_SURVIVORS = REQUIRED
DESTROYED_BUILDING_PASSIVE_REMOVED_AFTER_FINALIZE = REQUIRED
RETROACTIVE_STATUS_COMMIT_CANCELLATION = FORBIDDEN
```

## 10. 검증 Tier

```text
T0 = fixture·common schema·channel/tag/target/stack validation
T1 = replay determinism·phase-event parity
T2 = same-tick fairness·death/objective·damage/protection/status invariants
T3 = paired A/B/C metrics including all three lanes and KINETIC/ARCANE response
T4 = aggregate balance evaluation after acceptance approval
T5 = product runtime adapter after separate authorization
```

현재 승인 범위는 T0~T3의 기획 계약이다.

## 11. 벤치마크·현업 경계

- Godot fixed physics processing, instance RNG seed/state, JSON serialization 경계를 적용한다.
- TFT의 Armor/Magic Resistance 분리는 두 방어축과 읽기 쉬운 정보 구조의 참고 사례다.
- Guild Wars 2 Barrier는 HP와 분리된 임시 buffer와 cap 필요성의 참고 사례다.
- Overwatch barrier 조정 사례처럼 barrier uptime이 전투 pace와 선택을 대체하면 stop-ship이다.
- 외부 게임의 수치·아이템 메타·전투 순서를 복사하지 않는다.

## 12. 적대적 검토

```text
OMW-AUD-208 ~ OMW-AUD-220 = deterministic Harness scope
OMW-AUD-221 = stale Sheet PR-head correction / RESOLVED / NON_COUNTER
OMW-AUD-222 ~ OMW-AUD-232 = common combat schema·resolution order
OMW-AUD-233 = channel/tag conflation
OMW-AUD-234 = flying treated as damage type
OMW-AUD-235 = barrier double-counting
OMW-AUD-236 = recursive HP-loss transfer
OMW-AUD-237 = second mitigation on transferred loss
OMW-AUD-238 = retroactive same-tick status cancellation
OMW-AUD-239 = unspecified status stacking
OMW-AUD-240 = hidden immunity exceptions
OMW-AUD-241 = restore as negative damage
OMW-AUD-242 = true/execute/revive bypass
OMW-AUD-243 = accidental objective damage
OMW-AUD-244 = barrier overcentralization
OMW-AUD-245 = color-only channel UI
OMW-AUD-246 = raw/final metric double counting
```

## 13. 기존 Hero 정본 계보

PR #129에서 병합된 영웅 등급·초기 5명·cooldown·Stage·Trigger·파워 검증 Decision은 main 정본이다.

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
MAX_STORED_READY_COUNT = 1
MANUAL_CAST_OR_TARGET = FORBIDDEN
ACTIVE_EFFECT_OR_UNRESOLVED_COMMIT_STAGE_CARRY = FORBIDDEN
```

영웅은 공통 `CombatantState·Intent·ProtectionInstance·StatusInstance·event envelope`를 소비하며 별도 AI loop·tick clock·death resolver를 만들지 않는다.

## 14. 비카운트 운영 정책·Sync

| ID | 상태 | 역할 |
|---|---|---|
| `OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1` | `ACTIVE_STANDING_POLICY / MAIN_CANONICAL` | 공식 벤치마크·차이·제작비·QA·적대적 검토를 모든 Grill Me에 적용 |
| `OMW-SYNC-20260803-LIFECYCLE-STATUS-CLEANUP-V1` | `MAINTENANCE_SYNC / MAIN_CANONICAL / NON_COUNTER` | Decision 생명주기 우선순위 교정 |
| `OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1` | `MAINTENANCE_SYNC / MAIN_CANONICAL / NON_COUNTER` | 구현 상태·미확정 목록 최신화와 simulation-first Gate 라우팅 |
| `OMW-SYNC-20260803-PR133-HEAD-READBACK-CORRECTION-V1` | `SHEET_MAINTENANCE / NON_COUNTER` | `05_GDD_요약!D9` stale PR head 교정 |

## 15. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DAMAGE_PROTECTION_STATUS_SEMANTICS_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
SIMULATION_TOOL_CODE_AUTHORITY = NONE
DAMAGE_CHANNELS = KINETIC_AND_ARCANE
TRUE_DAMAGE_EXECUTE_REVIVE = FORBIDDEN_CURRENT_SLICE
EXACT_MITIGATION_FORMULA = PENDING
EXACT_ARMOR_RESISTANCE_DEFAULTS = PENDING
EXACT_BARRIER_BUDGET_CAP_DURATION = PENDING
EXACT_STATUS_STACK_CAP_DURATION = PENDING
EXACT_TICK_RATE_AND_ACTIVATION_POLICY = PENDING
EXACT_HERO_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 16. 카운터·다음 Gate

```text
CURRENT_COUNT_SINCE_MERGE = 3_OF_10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
NEXT_PREFLIGHT_AT = 10_OF_10
```
