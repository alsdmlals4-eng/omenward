# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: DETERMINISTIC_SIMULATION_HARNESS_SCOPE_APPROVED
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
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
current_grill_me_count: 1
future_merge_cadence: 10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
```

최신 Decision은 simulation Harness의 기획 범위만 승인한다. 제품·도구 코드 작성, simulation 실행, 밸런스 결론은 승인되지 않았다.

## 1. 제품 정체성

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

Harness는 핵심 플레이를 대체하는 시스템이 아니라 수치·AI·영웅 파워가 이 판단 구조를 훼손하지 않는지 반복 검증하는 제작 도구 계약이다.

## 2. 영웅 검증 대상

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

## 3. 승인된 Harness 구조

책임 원본:

`docs/design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`

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

실행 개념:

```text
Godot editor --headless --script
→ fixture loader
→ domain runner
→ fixed-tick scheduler
→ deterministic resolver set
→ result writer
```

initial core Harness는 production battle Scene, rendering, audio, NavigationServer, PhysicsServer, variable frame delta에 직접 의존하지 않는다.

## 4. 입력 계약

```text
schema_version
fixture_id
encounter_family
parameter_set_id
engine_contract_version
master_seed
named_rng_streams
tick_duration_units
max_ticks
initial_state
ordered_external_commands
expected_invariants
comparison_group
```

```text
GLOBAL_RANDOM_API = FORBIDDEN
RANDOMIZE = FORBIDDEN
WALL_CLOCK = FORBIDDEN
VARIABLE_FRAME_DELTA = FORBIDDEN
FIXED_INTEGER_TICK = REQUIRED
STABLE_OBJECT_ID = REQUIRED
EXPLICIT_SORT_KEY = REQUIRED
```

RNG target tie-break는 금지하며 모든 random domain은 named stream·seed·state·draw count를 가진다.

## 5. 출력 계약

```text
run_manifest
normalized_final_state
ordered_event_log
metrics_summary
invariant_results
named_rng_final_states
checkpoint_fingerprints
final_state_fingerprint
termination_reason
```

공통 event envelope:

```text
event_schema_version
tick
sequence_in_tick
event_id
event_type
source_id
target_ids
lane_id
payload
rng_stream_and_draw_index_if_any
```

## 6. 결정론 수준

초기 필수:

```text
same approved engine build
+ same reference CI environment
+ same fixture and ordered input
= identical event log and state fingerprints
```

cross-platform float bitwise parity는 현 Gate에서 주장하지 않는다. deterministic-critical 값은 scaled integer, quantized position, string/stable ID를 우선한다. JSON raw text 자체는 fingerprint 권위가 아니다.

## 7. 검증 Tier

```text
T0 = schema validation
T1 = replay determinism
T2 = rule invariants
T3 = paired A/B/C metrics
T4 = aggregate balance after acceptance approval
T5 = product Scene/runtime adapter after separate authorization
```

현재 승인 범위는 T0~T3의 기획 계약이다.

## 8. 필수 Encounter Family

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

family당 여러 배치·난이도·seed 변형과 후속 holdout fixture가 필요하다.

## 9. A/B/C 비교 불변식

paired group에서 다음을 고정한다.

```text
fixture base state
master seed and named RNG state
source Tier and passive stage
Stage and enemy composition
buildings and objectives
other-two-lane state
ordered external commands
parameter set except compared grade/kit fields
```

비교 대상 외 field 차이가 있으면 `INVALID_COMPARISON`이다.

## 10. 벤치마크·현업 비교

Godot 공식 자료:

- `--headless` command-line/CI script.
- fixed physics processing과 variable idle processing.
- `RandomNumberGenerator` seed·state.
- JSON number float 변환 및 FileAccess.

중요 판정:

```text
HEADLESS != DETERMINISTIC
JSON_TEXT != CANONICAL_STATE_HASH
FIXED_TICK + NAMED_RNG + STABLE_ORDER + CANONICAL_STATE = DETERMINISM_CONTRACT
```

## 11. 적대적 위험

```text
OMW-AUD-208 global RNG coupling
OMW-AUD-209 frame/wall-clock leakage
OMW-AUD-210 unstable collection order
OMW-AUD-211 float/platform divergence
OMW-AUD-212 fixture drift
OMW-AUD-213 family overfitting
OMW-AUD-214 harness/runtime divergence
OMW-AUD-215 event-log cost
OMW-AUD-216 placeholder balance conclusions
OMW-AUD-217 A/B/C contamination
OMW-AUD-218 other-lane omission
OMW-AUD-219 save/Retry state omission
OMW-AUD-220 headless/determinism confusion
```

## 12. 책임 원본

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- `docs/DECISIONS_PENDING.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TRIGGER_TARGET_AND_POWER_BUDGET_VALIDATION_2026-08-03.md`
- `docs/process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md`

## 13. 구현 경계·다음 작업

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = HARNESS_SCOPE_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
EXACT_COMBAT_SCHEMA = PENDING
EXACT_TICK_RATE = PENDING
EXACT_FORMULAS_AND_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

```text
GRILL_ME_COUNT = 1/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
```
