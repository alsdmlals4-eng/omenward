# Active Context

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_APPROVED
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
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
current_grill_me_count: 2
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: OUT_OF_SCOPE_REQUIRES_SEPARATE_CONTRACT
preflight: NEXT_AT_10_OF_10
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

`current_main`, `context_baseline_commit`, `current_planning_pr`은 실행 시점에 저장소에서 해석한다. 최신 Decision은 코어 우선 공통 전투 Schema와 fixed-tick resolution order의 기획 계약만 승인하며 GDScript·Scene·Resource·테스트 코드 작성과 실제 simulation 실행 권한을 부여하지 않는다.

## 1. 제품 정체성·핵심 재미

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
예고된 세 전선 공세 읽기
→ 제한된 건물·TokenSource로 룰렛 설계
→ 릴 이동과 확정으로 미래 결과 조작
→ 병력 보관·판매·획득
→ 어느 전선에 비가역 배치할지 판단
→ 자동전투·점령·건물 운영으로 전황 역전
→ 다음 Stage 설계에 환류
```

Harness와 공통 전투 Schema는 이 핵심 루프를 대체하지 않는다. 배치 provenance와 세 전선 전체 결과를 통해 룰렛 설계·비가역 커밋·전황 변화의 인과를 반복 검증하는 제작 기반이다.

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
```

초기 5명:

```text
shield_guard → 불퇴의 성벽
archer       → 천공 소거
priest       → 생명의 서약
mage         → 메테오
assassin     → 그림자 분신
```

## 3. 공통 영웅 상태·Resolver 계약

```text
INITIAL_WARMUP
→ READY_WAITING_FOR_VALID_CONDITION
→ CAST_PRECHECK
→ CAST_COMMIT
→ RESOLUTION_OR_ACTIVE_EFFECT
→ COOLDOWN
→ READY
```

```text
READY
→ public trigger
→ same-lane legal filter
→ public priority score
→ stability window
→ stable ID / stable position tie-break
→ CAST_PRECHECK
→ immutable CAST_COMMIT snapshot
```

```text
MAX_STORED_READY_COUNT = 1
CHARGE_ACCUMULATION = FALSE
MANA_OR_ENERGY_RESOURCE = FALSE
MANUAL_CAST_OR_TARGET = FALSE
ACTIVE_COMBAT = TIMER_PROGRESS
MAINTENANCE_OR_PREPARATION = TIMER_PAUSED
ACTIVE_EFFECT_OR_UNRESOLVED_COMMIT_STAGE_CARRY = FORBIDDEN
```

## 4. 결정론적 Harness 상위 정본

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

- full production battle Scene은 초기 기준 Harness가 아니다.
- 렌더·오디오·실시간 프레임·NavigationServer·PhysicsServer는 core Harness 의존성에서 제외한다.
- 실제 제품 Scene adapter 검증은 별도 후속 Gate다.
- 현재 승인 Tier는 T0 schema, T1 replay, T2 invariants, T3 paired A/B/C의 설계 계약이다.

## 5. 공통 Combat Schema·Resolution Order 현행 정본

책임 원본:

`design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md`

선택한 경계:

```text
CORE_FIRST_COMMON_SCHEMA = REQUIRED
HERO_FIRST_SPECIAL_CASE_SCHEMA = REJECTED
FULL_SYSTEM_SINGLE_SCHEMA = DEFERRED
```

### 5.1 필수 공통 상태

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

전장에 배치된 모든 유닛은 다음 인과를 추적한다.

```text
SpinSnapshot
→ PendingReward
→ TokenInstance / TokenSource
→ lane commit
→ deployment_id
→ combat event and result
```

전투 Harness는 룰렛을 재추첨하지 않고 이 provenance를 입력으로 소비한다.

### 5.2 위치·정렬

- `TOP=0`, `MID=1`, `BOTTOM=2`는 canonical serialization 순서다.
- 전투 위치는 `position_q{x_q,y_q,anchor_id}` quantized 2D 좌표다.
- 1D lane 좌표만 사용해 실제 거리 기반 cross-lane 효과를 왜곡하는 것을 금지한다.
- Dictionary·SceneTree 순회를 resolution order로 사용하지 않는다.

Canonical key:

```text
lane_order
→ entity_kind_order
→ spawn_sequence
→ stable_entity_id
→ local_sequence
```

### 5.3 fixed-tick phase order

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

동일 tick의 모든 적격 actor는 같은 post-movement snapshot에서 action을 commit한다. 낮은 stable ID가 먼저 피해를 주어 다른 actor의 합법적인 같은 tick 행동을 삭제하는 순차 편향을 금지한다.

### 5.4 효과 적용 상위 순서

```text
impact validity
→ immunity / eligibility
→ pre-mitigation modifier
→ armor / resistance hook
→ barrier / absorption
→ health-floor clamp
→ HP delta or restore
→ post-hit status and trigger
→ death_or_destruction_mark
```

정확 공식·상한·수치는 미승인이다. health-floor는 회복이 아니며 명시적 revive 계약 없이 사망 상태를 되돌리지 않는다.

### 5.5 죽음·파괴·점령

- damage/effect batch 뒤 죽음·파괴를 원자 확정한다.
- 이미 commit된 합법 행동은 source가 같은 tick에 사망했다는 이유만으로 ID 순서에 따라 취소되지 않는다.
- 건물 passive는 파괴 finalize 이후 제거하되 이미 commit된 행동을 소급 취소하지 않는다.
- 점령은 post-death 생존자와 post-destruction 가동 상태만 사용한다.
- commit 뒤 자동 fallback retarget은 금지한다.

## 6. A/B/C 비교 Harness

```text
A = 표준 [영웅]
B = 같은 source archetype 해금 이름 지정 [영웅]
C = 같은 계열 표준 [전설]
```

paired comparison에서 fixture·seed·source Tier·Stage·적 구성·건물·다른 두 전선·ordered input은 같아야 한다. 등급/키트 외 필드가 달라지면 `INVALID_COMPARISON`이다.

필수 family:

```text
NEUTRAL_MIXED
FRONTLINE_PRESSURE
FLYING_HEAVY
ALLY_BURST_CRISIS
DENSE_ENEMY_CLUSTER
DISPERSED_ENEMY_FORMATION
HIGH_VALUE_BACKLINE
LONG_ATTRITION
SHORT_STAGE
LATE_COMMIT_BOUNDARY
```

## 7. 벤치마크 경계

Godot 공식 자료에서 다음을 참고한다.

- `_physics_process()`의 고정 주기와 `_process()`의 가변 프레임 차이.
- `RandomNumberGenerator` instance별 seed·state.
- JSON 숫자 처리·직렬화 한계.

적용:

```text
ENGINE_FIXED_CALLBACK != COMPLETE_DETERMINISM
HEADLESS != DETERMINISTIC
RAW_JSON_TEXT != CANONICAL_STATE_HASH
```

OMENWARD 권위는 explicit integer tick·named RNG·canonical order·phase barrier·normalized state가 소유한다.

## 8. 적대적 위험

```text
OMW-AUD-208 ~ OMW-AUD-220 = Harness scope risks
OMW-AUD-221 = stale Sheet PR-head correction / resolved / non-counter
OMW-AUD-222 = roulette provenance omission
OMW-AUD-223 = Hero exception pollution
OMW-AUD-224 = sequential stable-ID action bias
OMW-AUD-225 = early death finalization
OMW-AUD-226 = hidden fallback retarget
OMW-AUD-227 = dead-unit capture contribution
OMW-AUD-228 = retroactive building-action cancellation
OMW-AUD-229 = 1D position cross-lane distortion
OMW-AUD-230 = exact values smuggled into schema
OMW-AUD-231 = SceneTree order leakage
OMW-AUD-232 = ambiguous fingerprint phase
```

## 9. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = COMMON_COMBAT_SCHEMA_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
COMMON_COMBAT_SCHEMA = USER_APPROVED_NOT_IMPLEMENTED
EXACT_TICK_RATE = PENDING
EXACT_DAMAGE_DEFENSE_PROTECTION_FORMULAS = PENDING
EXACT_ACTIVATION_POLICY = PENDING
EXACT_HERO_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 10. 다음 Gate

```text
GRILL_ME_COUNT = 2/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
