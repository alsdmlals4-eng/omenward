# Active Context

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: DETERMINISTIC_SIMULATION_HARNESS_SCOPE_APPROVED
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
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
current_grill_me_count: 1
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: OUT_OF_SCOPE_REQUIRES_SEPARATE_CONTRACT
preflight: NEXT_AT_10_OF_10
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

`current_main`, `context_baseline_commit`, `current_planning_pr`은 실행 시점에 저장소에서 해석한다. 최신 Decision은 Harness의 기획 범위만 승인하며 GDScript·Scene·Resource·테스트 코드 작성과 실제 simulation 실행 권한을 부여하지 않는다.

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

Harness는 이 핵심 루프를 대체하지 않는다. 수치·AI·영웅 파워가 핵심 판단을 훼손하지 않는지 반복 가능하게 검증하는 도구 계약이다.

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

## 3. 공통 상태·Resolver 계약

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

## 4. 결정론적 Harness 현행 정본

책임 원본:

`design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`

선택한 구조:

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

### 4.1 실행 계층

```text
Godot --headless --script
→ Fixture Schema
→ Domain State
→ Fixed-Tick Scheduler
→ Deterministic Resolver Set
→ Metrics/Event Log
→ Replay/Fingerprint Verification
```

- full production battle Scene은 초기 기준 Harness가 아니다.
- 렌더·오디오·실시간 프레임·NavigationServer·PhysicsServer는 core Harness 의존성에서 제외한다.
- 실제 제품 Scene adapter 검증은 별도 후속 Gate다.

### 4.2 입력 핵심

```text
schema_version
fixture_id / encounter_family
parameter_set_id / engine_contract_version
master_seed / named_rng_streams
tick_duration_units / max_ticks
initial_state
ordered_external_commands
expected_invariants
comparison_group
```

### 4.3 출력 핵심

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

### 4.4 결정론 불변식

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

headless 실행은 결정론을 자동 보장하지 않는다. 결정론은 입력·시간·RNG·순서·숫자 계약으로 보장한다.

## 5. A/B/C 비교 Harness

```text
A = 표준 [영웅]
B = 같은 source archetype 해금 이름 지정 [영웅]
C = 같은 계열 표준 [전설]
```

paired comparison에서 동일해야 하는 항목:

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

다른 필드가 변하면 `INVALID_COMPARISON`이다.

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

## 6. 검증 Tier

```text
T0 = fixture schema validation
T1 = replay determinism
T2 = rule invariants
T3 = paired A/B/C metrics
T4 = aggregate balance evaluation after tolerance approval
T5 = product runtime adapter after separate authorization
```

현재 승인 범위는 T0~T3의 설계 계약이다. T4 밸런스 결론과 T5 제품 adapter 구현은 승인되지 않았다.

## 7. 벤치마크 경계

Godot 공식 자료에서 다음을 참고했다.

- `--headless`와 script·CI 실행.
- `_physics_process()`의 고정 주기와 `_process()`의 가변 프레임 차이.
- `RandomNumberGenerator`의 seed·state와 복수 RNG 인스턴스.
- JSON 숫자의 float 변환 한계와 FileAccess 직렬화.

적용 경계:

- JSON은 manifest 교환 형식일 수 있지만 raw JSON 문자열은 state hash 권위가 아니다.
- deterministic 핵심 수치는 scaled integer·문자열 ID·명시적 field order를 사용한다.
- 초기 완료 조건은 동일 승인 engine build와 reference CI 환경의 bit-identical 결과다.
- cross-platform float bitwise parity는 주장하지 않는다.

## 8. 적대적 위험

```text
OMW-AUD-208 global RNG coupling
OMW-AUD-209 wall-clock or frame delta leakage
OMW-AUD-210 unstable collection iteration order
OMW-AUD-211 float and cross-platform divergence
OMW-AUD-212 fixture drift from canon
OMW-AUD-213 overfitting to ten encounter families
OMW-AUD-214 harness/runtime divergence
OMW-AUD-215 excessive event-log cost
OMW-AUD-216 balance conclusions from placeholder values
OMW-AUD-217 contaminated A/B/C comparisons
OMW-AUD-218 omission of other-two-lane contribution
OMW-AUD-219 missing save/Retry state
OMW-AUD-220 confusing headless execution with determinism
```

## 9. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = USER_APPROVED_HARNESS_SCOPE_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
EXACT_COMBAT_SCHEMA = PENDING
EXACT_TICK_RATE = PENDING
EXACT_DAMAGE_AND_DEFENSE_FORMULA = PENDING
EXACT_HERO_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 10. 다음 Gate

```text
GRILL_ME_COUNT = 1/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
