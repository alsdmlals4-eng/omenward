# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_APPROVED
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_validation_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
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
current_grill_me_count: 2
future_merge_cadence: 10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
```

최신 Decision은 공통 전투 Schema와 fixed-tick resolution order의 기획 계약만 승인한다. 제품·도구 코드 작성, simulation 실행, 밸런스 결론은 승인되지 않았다.

## 1. 제품 정체성

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

공통 전투 Schema는 핵심 플레이를 대체하지 않는다. `SpinSnapshot·TokenSource·비가역 전선 커밋 → 전투 결과`의 provenance를 보존하고 세 전선 전체의 결과 원인을 설명하기 위한 제작 기반이다.

## 2. 현재 책임 원본

- Harness 상위 범위: `docs/design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`
- 공통 전투 Schema·순서: `docs/design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md`
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
ActionIntent
EffectIntent
StatusInstance
PendingCommit
ActiveEffect
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

전투 Harness는 이 provenance를 입력으로 소비하지만 룰렛을 재추첨하지 않는다.

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

## 8. Damage·Effect 상위 순서

```text
impact validity
→ immunity / eligibility
→ pre-mitigation modifier
→ armor / resistance formula hook
→ barrier / absorption
→ health-floor clamp
→ HP delta or restore
→ post-hit status and trigger
→ death_or_destruction_mark
```

정확 공식·수치는 미확정이다. health-floor는 회복이 아니며 명시적 revive 계약 없이는 사망을 되돌리지 않는다.

## 9. 동일 Tick 공정성

```text
ALL_ELIGIBLE_ACTORS_COMMIT_FROM_SAME_PHASE_SNAPSHOT
SEQUENTIAL_ENTITY_ID_KILL_ADVANTAGE = FORBIDDEN
FALLBACK_RETARGET_AFTER_COMMIT = FORBIDDEN
DEATH_FINALIZATION_BEFORE_DAMAGE_BATCH_END = FORBIDDEN
OBJECTIVE_USES_POST_DEATH_SURVIVORS = REQUIRED
DESTROYED_BUILDING_PASSIVE_REMOVED_AFTER_FINALIZE = REQUIRED
```

- damage/effect batch 뒤 death·destruction을 원자 확정한다.
- 이미 commit된 합법 행동은 source의 같은 tick 사망 때문에 ID 순서로 취소하지 않는다.
- 점령은 post-death 생존자와 post-destruction 가동 상태만 사용한다.

## 10. 공통 event·fingerprint

```text
tick
phase_order
resolver_order
source_canonical_key
local_sequence
event_id / event_type
source_id / target_ids / lane_id
payload
rng_stream_and_draw_index_if_any
deployment_id_if_applicable
```

R120 phase barrier 이후 canonical state fingerprint를 생성하며 다음 tick 전 mutation을 금지한다.

## 11. 검증 Tier

```text
T0 = fixture·common schema·provenance validation
T1 = replay determinism·phase-event parity
T2 = same-tick fairness·death/objective order·no fallback invariants
T3 = paired A/B/C metrics including all three lanes
T4 = aggregate balance after acceptance approval
T5 = product Scene/runtime adapter after separate authorization
```

현재 승인 범위는 T0~T3의 기획 계약이다.

## 12. 벤치마크·현업 비교

Godot 공식 자료의 fixed physics processing, instance RNG seed/state, JSON 숫자 처리 경계를 참고한다.

```text
HEADLESS != DETERMINISTIC
ENGINE_FIXED_CALLBACK != COMPLETE_DETERMINISM
RAW_JSON_TEXT != CANONICAL_STATE_HASH
```

OMENWARD 권위는 explicit integer tick·named RNG·phase barrier·canonical order·normalized state가 소유한다.

## 13. 적대적 위험

```text
OMW-AUD-208 ~ OMW-AUD-220 = Harness 범위
OMW-AUD-221 = Sheet stale PR-head / RESOLVED / NON_COUNTER
OMW-AUD-222 ~ OMW-AUD-232 = common combat schema·resolution order
```

핵심 방어:

- 룰렛 provenance 누락 금지.
- 영웅 5명 예외로 공통 Schema 오염 금지.
- 순차 entity kill bias 금지.
- hidden fallback retarget 금지.
- 사망 유닛 점령 기여 금지.
- 1D 위치로 cross-lane 거리 왜곡 금지.
- R120 이전/이후 fingerprint 시점 혼용 금지.

## 14. 구현 경계·다음 작업

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = COMMON_COMBAT_SCHEMA_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
EXACT_TICK_RATE = PENDING
EXACT_DAMAGE_DEFENSE_PROTECTION_FORMULAS = PENDING
EXACT_ACTIVATION_POLICY = PENDING
EXACT_HERO_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

```text
GRILL_ME_COUNT = 2/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
```
