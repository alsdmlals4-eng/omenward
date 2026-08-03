# Active Context

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_APPROVED
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_validation_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
parent_gameplay_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
last_sync: OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1
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
current_grill_me_count: 3
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: OUT_OF_SCOPE_REQUIRES_SEPARATE_CONTRACT
preflight: NEXT_AT_10_OF_10
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

`current_main`, `context_baseline_commit`, `current_planning_pr`은 실행 시점에 저장소에서 해석한다. 최신 Decision은 피해·보호·상태 의미의 기획 계약만 승인한다. GDScript·Scene·Resource·fixture·test 작성과 simulation 실행 권한은 없다.

## 1. 제품 정체성·핵심 재미

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
예고된 세 전선 공세 읽기
→ 제한된 건물·TokenSource로 룰렛 설계
→ 세 원형 릴 이동과 확정으로 미래 결과 조작
→ 병력 보관·판매·획득
→ 어느 전선에 비가역 배치할지 판단
→ 자동전투·점령·건물 운영으로 전황 역전
→ 결과 원인을 복기해 다음 Stage 설계에 환류
```

Harness·공통 Combat Schema·Damage Semantics는 핵심 플레이를 대체하지 않는다. `SpinSnapshot·TokenSource·lane commit→deployment_id→combat event` 인과를 검증하고, KINETIC/ARCANE 공세에 대응한 플레이어 선택이 결과에 반영됐는지 설명하기 위한 제작 기반이다.

## 2. 현행 영웅·전설 계약

```text
표준 [영웅] = 강화 1스킬 + 표준 2스킬
해금 이름 지정 [영웅] = 강화 1스킬 + 고유 2스킬
표준 [전설] = 강화 1스킬 + 강화 표준 2스킬 + 표준 3스킬
향후 해금 이름 지정 [전설] = 강화 1스킬 + 강화 표준 2스킬 + 고유 3스킬
```

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
MAX_STORED_READY_COUNT = 1
MANUAL_CAST_OR_TARGET = FORBIDDEN
ACTIVE_EFFECT_OR_UNRESOLVED_COMMIT_STAGE_CARRY = FORBIDDEN
```

초기 5명:

```text
shield_guard → 불퇴의 성벽
archer       → 천공 소거
priest       → 생명의 서약
mage         → 메테오
assassin     → 그림자 분신
```

영웅은 별도 AI loop·tick clock·death resolver·save identity를 만들지 않고 공통 Combatant·Intent·Protection·Status·Event 계약을 사용한다.

## 3. 결정론적 Harness 상위 정본

책임 원본:

`design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`

```text
versioned fixture
+ explicit fixed integer tick
+ named RNG streams
+ stable object IDs
+ ordered external commands
+ pure domain state transition
→ ordered event log
→ normalized final state
→ metrics summary
→ deterministic state fingerprint
```

- full production battle Scene은 초기 core Harness가 아니다.
- rendering·audio·variable frame delta·NavigationServer·PhysicsServer는 전투 권위에서 제외한다.
- 현재 승인 Tier는 T0 schema, T1 replay, T2 invariants, T3 paired A/B/C의 설계 계약이다.
- T4 balance acceptance와 T5 product runtime adapter는 후속 승인이다.

## 4. 공통 Combat Schema·Resolution Order

책임 원본:

`design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md`

```text
CORE_FIRST_COMMON_SCHEMA = REQUIRED
HERO_FIRST_SPECIAL_CASE_SCHEMA = REJECTED
FULL_SYSTEM_SINGLE_SCHEMA = DEFERRED
```

필수 상태:

```text
CombatRunState
LaneState[TOP,MID,BOTTOM]
CombatantState
BuildingState
ObjectiveState
DeploymentProvenance
OrderedCommand
ActionIntent / EffectIntent
PendingCommit / ActiveEffect
ProtectionInstance / StatusInstance
RngStreamState
```

위치·정렬:

```text
position_q = {x_q, y_q, anchor_id}
lane_order = TOP(0), MID(1), BOTTOM(2)
canonical_key = lane_order → entity_kind_order → spawn_sequence → stable_entity_id → local_sequence
```

Dictionary·SceneTree·animation/navigation callback 순서를 resolution authority로 사용하지 않는다.

### Fixed-Tick Phase Order

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

모든 적격 actor는 같은 post-movement snapshot에서 commit한다. damage/effect batch 뒤 death·destruction을 원자 확정하며, objective는 post-death 생존자와 post-destruction 가동 상태만 사용한다.

## 5. Damage·Protection·Status 현행 정본

책임 원본:

`design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md`

### 5.1 Damage Channel·Defense Axis

```text
KINETIC → ARMOR
ARCANE  → RESISTANCE
```

```text
DAMAGE_CHANNEL = exactly one
DELIVERY_TAGS = BASIC / SKILL / AREA / DAMAGE_OVER_TIME / ENVIRONMENT / TRANSFERRED
TARGET_PROFILE = UNIT / BUILDING / OBJECTIVE + GROUND / FLYING
```

- AREA·DOT·SIEGE·FLYING은 새로운 damage channel이 아니다.
- action이 두 채널을 사용하면 두 개의 명시적 DamageIntent로 분리한다.
- channel은 data가 명시하며 VFX·병종 이름·delivery tag에서 추론하지 않는다.

현 Slice 금지:

```text
TRUE_DAMAGE = FORBIDDEN
EXECUTE_OR_INSTANT_KILL = FORBIDDEN
REVIVE = FORBIDDEN
FRIENDLY_FIRE = FORBIDDEN_BY_DEFAULT
SELF_DAMAGE = FORBIDDEN_BY_DEFAULT
```

### 5.2 R80 내부 의미

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
raw_amount
→ outgoing/incoming modifiers
→ KINETIC: armor hook | ARCANE: resistance hook
→ barrier absorption
→ candidate HP loss
→ one-hop redirection
→ health-floor clamp
→ HP delta / separate restore
→ status and post-hit queue
→ death_pending
```

정확 formula·rounding·cap·duration은 다음 numeric Decision이 소유한다.

### 5.3 Barrier·Redirection·Restore

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

- same-tick 합법 ProtectionIntent는 R80B에서 피해 전에 materialize한다.
- barrier는 channel mitigation 뒤 남은 피해를 흡수한다.
- HP-loss redirection은 barrier 뒤 candidate loss를 재배분하며 root effect ID를 보존한다.
- health floor는 damage clamp이며 heal·revive가 아니다.
- Restore는 max HP clamp를 적용하고 death_pending/dead를 되돌리지 않는다.

### 5.4 Status

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

각 definition은 다음 중 정확히 하나의 stacking policy를 가진다.

```text
REPLACE_IF_STRONGER
REFRESH_DURATION
ADD_STACKS_CAPPED
INDEPENDENT_BY_SOURCE
EXCLUSIVE_GROUP
```

```text
ACTIVE_INTERVAL = [start_tick, end_tick_exclusive)
EXPIRY = R00 when end_tick_exclusive <= current_tick
```

일반 status는 이미 commit된 same-tick action을 소급 취소하지 않는다. 즉시 보호는 ProtectionIntent가 소유한다.

### 5.5 Target Boundary

- UNIT은 action filter가 허용하면 targetable이다.
- BUILDING은 명시적 building eligibility가 필요하다.
- OBJECTIVE는 기본적으로 HP damage target이 아니며 R100 ownership resolver가 소유한다.
- FLYING·GROUND는 target eligibility이며 damage type이 아니다.

## 6. Event·Metric Contract

```text
DAMAGE_INTENT_CREATED
DAMAGE_REJECTED
DAMAGE_MODIFIED
CHANNEL_MITIGATION_APPLIED
BARRIER_APPLIED / CONSUMED / EXPIRED
HP_LOSS_REDIRECTED
HEALTH_FLOOR_CLAMPED
HP_LOSS_APPLIED
RESTORE_APPLIED
STATUS_APPLIED / REFRESHED / STACKED / REPLACED / REJECTED / EXPIRED / DISPELLED
DEATH_PENDING
```

```text
RAW_DAMAGE != POST_MITIGATION_DAMAGE != BARRIER_ABSORBED != FINAL_HP_LOSS
```

모든 event는 root effect·source·target·channel/tag·tick/phase/sequence를 기록하며 배치 유닛은 deployment_id까지 역추적한다.

## 7. 검증 Tier

```text
T0 = fixture·schema·channel/tag/target/stack policy validation
T1 = replay determinism·phase/event parity
T2 = same-tick fairness·no true/execute/revive·barrier/transfer/status invariants
T3 = KINETIC/ARCANE threat와 Armor/Resistance 대응을 포함한 paired A/B/C
T4 = aggregate balance after acceptance approval
T5 = product Scene/runtime adapter after separate authorization
```

## 8. 벤치마크·생산 비교

- TFT 공식 Roles·Item 자료의 Armor와 Magic Resistance 분리를 참고하되 아이템 메타와 3개 이상 channel은 복사하지 않는다.
- Guild Wars 2 Barrier의 임시 HP buffer·분리 UI·cap 필요성을 참고하되 exact 수치를 복사하지 않는다.
- Overwatch barrier 조정 사례에서 barrier uptime이 전투 pace와 선택을 대체하는 위험을 stop-ship으로 채택한다.
- PC-first 화면에서는 channel을 색상만으로 표현하지 않고 아이콘·문자 라벨을 병행한다.

## 9. 적대적 위험

```text
OMW-AUD-208 ~ OMW-AUD-220 = Harness scope risks
OMW-AUD-221 = stale Sheet PR-head correction / resolved / non-counter
OMW-AUD-222 ~ OMW-AUD-232 = common combat schema·resolution order risks
OMW-AUD-233 = channel/tag conflation
OMW-AUD-234 = flying treated as damage type
OMW-AUD-235 = barrier double-counted as HP/heal/defense
OMW-AUD-236 = recursive HP-loss transfer
OMW-AUD-237 = transferred loss receives second mitigation
OMW-AUD-238 = retroactive same-tick status cancellation
OMW-AUD-239 = unspecified status stacking
OMW-AUD-240 = hidden immunity exceptions
OMW-AUD-241 = restore implemented as negative damage
OMW-AUD-242 = true/execute/revive bypasses core counterplay
OMW-AUD-243 = accidental objective HP damage
OMW-AUD-244 = permanent barrier overcentralization
OMW-AUD-245 = color-only channel UI
OMW-AUD-246 = raw/final damage metric double counting
```

## 10. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DAMAGE_PROTECTION_STATUS_SEMANTICS_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
COMMON_COMBAT_SCHEMA = USER_APPROVED_NOT_IMPLEMENTED
DAMAGE_PROTECTION_STATUS_SEMANTICS = USER_APPROVED_NOT_IMPLEMENTED
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

## 11. 다음 Gate

```text
GRILL_ME_COUNT = 3/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
