# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_APPROVED
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_validation_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_validation_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
parent_gameplay_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
last_sync: OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1
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
current_grill_me_count: 3
future_merge_cadence: 10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
```

최신 Decision은 피해·보호·상태 의미의 기획 계약만 승인한다. 제품·도구 코드 작성, simulation 실행, 밸런스 결론은 승인되지 않았다.

## 1. 제품 정체성

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

Harness와 전투 Schema는 핵심 플레이를 대체하지 않는다. `SpinSnapshot·TokenSource·비가역 전선 커밋→전투 결과` provenance를 보존하고, KINETIC/ARCANE 공세와 Armor/Resistance 대응이 세 전선 선택에 어떤 결과를 만들었는지 설명하는 제작 기반이다.

## 2. 현재 책임 원본

- Harness 상위 범위: `docs/design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`
- 공통 전투 Schema·순서: `docs/design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md`
- 피해·보호·상태 의미: `docs/design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md`
- 영웅 Trigger·파워 검증: `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TRIGGER_TARGET_AND_POWER_BUDGET_VALIDATION_2026-08-03.md`
- 결정 원장: `docs/PROJECT_CANON_DECISION_LEDGER.md`
- 현재 상태: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- 미확정: `docs/DECISIONS_PENDING.md`

## 3. 영웅 검증 대상

```text
A = 표준 [영웅]
B = 같은 source archetype 해금 이름 지정 [영웅]
C = 같은 계열 표준 [전설]
```

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

초기 5명:

```text
shield_guard → 불퇴의 성벽
archer       → 천공 소거
priest       → 생명의 서약
mage         → 메테오
assassin     → 그림자 분신
```

영웅은 별도 damage system·AI loop·tick clock·death resolver·save identity를 만들지 않는다.

## 4. Harness 상위 구조

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

initial core Harness는 production battle Scene, rendering, audio, NavigationServer, PhysicsServer, variable frame delta에 직접 의존하지 않는다.

## 5. 공통 Combat Schema 결정

```text
CORE_FIRST_COMMON_SCHEMA = REQUIRED
HERO_FIRST_SPECIAL_CASE_SCHEMA = REJECTED
FULL_SYSTEM_SINGLE_SCHEMA = DEFERRED
```

필수 공통 상태:

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

`DeploymentProvenance` 필수 계보:

```text
deployment_id
spin_snapshot_id
pending_reward_id
token_instance_id
token_source_id
reward_resolution_sequence
lane_commit_id
commit_sequence
```

전투 Harness는 provenance를 입력으로 소비하지만 룰렛을 재추첨하지 않는다.

## 6. 위치·Canonical Order

```text
position_q = {x_q, y_q, anchor_id}
lane_order = TOP(0), MID(1), BOTTOM(2)
canonical_key = lane_order → entity_kind_order → spawn_sequence → stable_entity_id → local_sequence
```

- quantized 2D 위치를 사용한다.
- 1D lane 좌표만으로 실제 거리 기반 cross-lane 효과를 계산하지 않는다.
- Dictionary·SceneTree traversal·callback order를 resolution 권위로 사용하지 않는다.

## 7. Fixed-Tick Resolution Order

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

모든 적격 actor는 같은 post-movement snapshot에서 intent를 commit한다. entity 순차 처리로 낮은 ID가 같은 tick 행동 우선권을 얻는 것을 금지한다.

## 8. Damage Channel·Target 분리

```text
KINETIC → ARMOR
ARCANE  → RESISTANCE
```

```text
DELIVERY_TAGS = BASIC / SKILL / AREA / DAMAGE_OVER_TIME / ENVIRONMENT / TRANSFERRED
TARGET_PROFILE = UNIT / BUILDING / OBJECTIVE + GROUND / FLYING
```

- AREA·DOT·SIEGE·FLYING은 damage channel이 아니다.
- 하나의 action이 두 channel을 사용하면 두 DamageIntent로 분리한다.
- channel은 data가 명시하며 VFX·이름에서 추론하지 않는다.
- Objective는 기본 HP target이 아니다.

## 9. R80 Damage·Protection·Status 의미

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
raw amount
→ outgoing/incoming modifiers
→ armor/resistance hook
→ barrier
→ candidate HP loss
→ one-hop redirection
→ health floor
→ HP delta or separate restore
→ status/post-hit
→ death_pending
```

핵심 불변식:

```text
BARRIER != HP_OR_HEAL
RESTORE != NEGATIVE_DAMAGE
TRANSFER_DEPTH_MAX = 1
RECURSIVE_REDIRECTION = FORBIDDEN
SECOND_MITIGATION_PASS = FORBIDDEN
RETROACTIVE_STATUS_COMMIT_CANCELLATION = FORBIDDEN
```

## 10. Status

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

각 status definition은 정확히 하나의 stacking policy를 선언한다.

```text
REPLACE_IF_STRONGER
REFRESH_DURATION
ADD_STACKS_CAPPED
INDEPENDENT_BY_SOURCE
EXCLUSIVE_GROUP
```

```text
ACTIVE_INTERVAL = [start_tick, end_tick_exclusive)
EXPIRY = R00
```

일반 status는 이미 commit된 same-tick 행동을 소급 취소하지 않는다. 즉시 보호는 ProtectionIntent가 소유한다.

## 11. Current Slice Exclusions

```text
TRUE_DAMAGE = FORBIDDEN
EXECUTE_OR_INSTANT_KILL = FORBIDDEN
REVIVE = FORBIDDEN
FRIENDLY_FIRE = FORBIDDEN_BY_DEFAULT
SELF_DAMAGE = FORBIDDEN_BY_DEFAULT
OBJECTIVE_HP_DAMAGE = FORBIDDEN_BY_DEFAULT
```

미래 추가는 새 Decision이 필요하다.

## 12. Event·Fingerprint

```text
RAW_DAMAGE != POST_MITIGATION_DAMAGE != BARRIER_ABSORBED != FINAL_HP_LOSS
RESTORE_AMOUNT = SEPARATE
STATUS_RESULT = SEPARATE
```

모든 event는 root effect·source·target·channel/tag·tick/phase/sequence와 해당 시 deployment_id를 보존한다. R120 이후 다음 tick 전 mutation은 금지한다.

## 13. 검증 Tier

```text
T0 = fixture·schema·channel/tag/target/stack validation
T1 = replay determinism·phase-event parity
T2 = same-tick fairness·death/objective·damage/protection/status invariants
T3 = paired A/B/C metrics including all three lanes and KINETIC/ARCANE response
T4 = aggregate balance after acceptance approval
T5 = product Scene/runtime adapter after separate authorization
```

현재 승인 범위는 T0~T3의 기획 계약이다.

## 14. 벤치마크·현업 비교

- Godot fixed processing·instance RNG·JSON serialization 경계를 참고한다.
- TFT의 Armor/Magic Resistance 분리는 두 방어축의 참고 사례다.
- Guild Wars 2 Barrier는 HP와 분리된 temporary buffer·명시 UI·cap 필요성의 참고 사례다.
- Overwatch barrier 조정 사례처럼 barrier uptime이 전투 pace와 선택을 대체하면 stop-ship이다.
- 외부 게임 exact 수치·아이템 메타·전투 순서는 복사하지 않는다.

## 15. 적대적 위험

```text
OMW-AUD-208 ~ OMW-AUD-220 = Harness 범위
OMW-AUD-221 = Sheet stale PR-head / RESOLVED / NON_COUNTER
OMW-AUD-222 ~ OMW-AUD-232 = common combat schema·resolution order
OMW-AUD-233 ~ OMW-AUD-246 = damage·protection·status semantics
```

핵심 방어:

- channel/tag/target conflation 금지.
- flying을 damage type으로 취급 금지.
- barrier double counting 금지.
- recursive transfer·second mitigation 금지.
- same-tick status 소급 취소 금지.
- hidden immunity 금지.
- restore를 negative damage로 처리 금지.
- true/execute/revive 금지.
- Objective 우발 damage 금지.
- barrier 상시 유지 stop-ship.
- color-only channel UI 금지.
- raw/final damage metric 이중 집계 금지.

## 16. 구현 경계·다음 작업

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DAMAGE_PROTECTION_STATUS_SEMANTICS_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
DAMAGE_CHANNELS = KINETIC_AND_ARCANE
TRUE_DAMAGE_EXECUTE_REVIVE = FORBIDDEN_CURRENT_SLICE
EXACT_MITIGATION_FORMULA = PENDING
EXACT_ARMOR_RESISTANCE_DEFAULTS = PENDING
EXACT_BARRIER_BUDGET_CAP_DURATION = PENDING
EXACT_STATUS_STACK_CAP_DURATION = PENDING
EXACT_TICK_RATE_AND_ACTIVATION_POLICY = PENDING
EXACT_HERO_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

```text
GRILL_ME_COUNT = 3/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
```
