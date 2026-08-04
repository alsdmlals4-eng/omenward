# OMENWARD 결정론적 시뮬레이션 Harness 범위 승인안

```yaml
decision_id: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
approved_at: 2026-08-03 09:11 KST
approval: USER_APPROVED_RECOMMENDATION
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
scope: DETERMINISTIC_HEADLESS_DOMAIN_SIMULATION_HARNESS
parent_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
product_code_authority: NONE
simulation_tool_implementation: NOT_AUTHORIZED
simulation_execution: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

OMENWARD의 전투·영웅 파워 검증은 **Godot headless 실행이 가능한 순수 도메인 고정-tick Harness**를 기준으로 설계한다.

```text
versioned fixture
+ explicit fixed tick
+ named RNG streams
+ stable object IDs
+ ordered external commands
+ pure domain state transition
→ ordered event log
→ normalized final state
→ metrics summary
→ deterministic state fingerprint
```

이 Decision은 Harness의 범위·입출력·재현성 계약을 승인한다. GDScript, Scene, Resource, 테스트 코드 또는 실제 simulation 실행 권한은 부여하지 않는다.

## 2. 선택한 접근

### A. Headless 순수 도메인 Harness — 승인

```text
Godot editor binary --headless --script
→ fixture loader
→ domain runner
→ fixed-tick scheduler
→ deterministic resolvers
→ result writer
```

핵심 전투 상태를 Node tree·렌더링·오디오·실시간 입력·NavigationServer·PhysicsServer에 직접 의존하지 않는 명시적 데이터 객체로 표현한다.

### B. 실제 전투 Scene을 그대로 headless 실행 — 초기 기준으로 미채택

장점:

- 실제 제품과 가까운 실행 경로.
- Scene·animation·navigation 통합 문제를 빠르게 노출.

문제:

- physics·navigation·node processing 순서와 제품 프레임 수명주기에 강하게 결합.
- fixture 구성과 결과 해석 비용이 큼.
- 밸런스 수치 변경과 표현 계층 오류가 섞임.
- 빠른 대량 A/B/C 비교에 부적합.

제품 Scene adapter 검증은 도메인 Harness 이후 별도 Gate로 둔다.

### C. Spreadsheet·정적 계산 Proxy만 사용 — 보조 도구로만 허용

경제·단일 피해량 계산에는 유용하지만 Trigger 안정화, target snapshot, cooldown, Stage 경계, 분신 owner link, late commit 취소를 검증할 수 없으므로 주 Harness가 될 수 없다.

## 3. 벤치마크·현업 비교

### Godot headless 실행

Godot 공식 command-line 문서는 `--headless`가 표시·오디오 드라이버 없이 script를 실행하고 CI 환경에서 사용하는 방식임을 설명한다.

적용:

- 렌더 창 없이 fixture batch를 실행할 수 있다.
- CI에서 동일 명령으로 반복 검증할 수 있다.
- headless 실행 자체가 결정론을 보장하지는 않으므로 별도 상태·RNG·순서 계약이 필요하다.

### 고정 주기 처리

Godot 공식 문서는 `_physics_process()`가 기본적으로 고정 주기로 호출되고 `_process()`는 실제 프레임률에 따라 달라진다고 설명한다.

적용:

- Harness는 variable frame delta를 입력으로 사용하지 않는다.
- fixture가 명시한 정수 tick 단위로 상태를 전진시킨다.
- 정확 tick rate는 공통 combat schema Decision에서 확정한다.

### RNG seed·state

Godot 공식 RandomNumberGenerator 문서는 개별 RNG 인스턴스가 seed와 state를 가지며 replay·rewind 같은 용도에 적합하다고 설명한다.

적용:

- 전역 RNG 사용을 금지한다.
- 목적별 named RNG stream을 사용한다.
- 각 stream의 seed·state·draw count를 결과에 기록한다.

### JSON·파일 직렬화

Godot 공식 JSON 문서는 key 정렬을 지원하지만 JSON 숫자가 float로 변환되고 비유한 숫자 처리에 한계가 있음을 경고한다. FileAccess는 결과 파일 입출력을 제공한다.

적용:

- JSON은 fixture manifest와 결과 교환 형식으로 사용할 수 있다.
- deterministic 핵심 수치는 제한 범위의 scaled integer 또는 문자열 ID로 저장한다.
- raw JSON 문자열 자체를 상태 권위나 hash 입력으로 사용하지 않는다.
- 명시된 필드 순서로 canonical typed state를 직렬화해 fingerprint를 계산한다.

## 4. Harness 계층

```text
Layer 1: Fixture Schema
Layer 2: Domain State
Layer 3: Fixed-Tick Scheduler
Layer 4: Deterministic Resolver Set
Layer 5: Metrics and Event Log
Layer 6: Replay and Fingerprint Verification
```

### 4.1 Fixture Schema

Harness 입력은 versioned fixture다.

필수 상위 필드:

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

### 4.2 Domain State

최소 상태 범위:

```text
battle_phase
current_tick
lane_states
unit_states
building_states
objective_states
high_grade_global_slot
hero_skill_states
pending_commits
active_effects
named_rng_states
resolved_event_ids
```

정확 필드와 숫자 타입은 다음 공통 combat schema Decision에서 확정한다.

### 4.3 Fixed-Tick Scheduler

```text
for each tick:
1. apply ordered external commands
2. evaluate phase transitions
3. evaluate movement and legal positions
4. evaluate target and trigger candidates
5. commit immutable actions
6. resolve damage, protection and effects
7. resolve death and removal
8. update objectives
9. advance timers
10. emit ordered events and metrics
11. calculate optional checkpoint fingerprint
```

동일 tick 내 실제 세부 순서는 공통 combat schema에서 확정하지만, 한 번 확정된 순서는 모든 fixture와 제품 adapter가 공유해야 한다.

## 5. 입력 계약

### 5.1 Seed와 RNG

```text
GLOBAL_RANDOM_API = FORBIDDEN
RANDOMIZE = FORBIDDEN
NAMED_RNG_STREAM = REQUIRED_FOR_EACH_RANDOM_DOMAIN
SEED_AND_STATE_SERIALIZATION = REQUIRED
RNG_DRAW_COUNT_LOG = REQUIRED
```

예상 stream 예시:

```text
enemy_spawn_variation
attack_variance
content_selection
loot_or_reward
```

공개 deterministic target tie-break에는 RNG를 사용하지 않는다.

### 5.2 시간

```text
WALL_CLOCK = FORBIDDEN
OS_TIME = FORBIDDEN
VARIABLE_FRAME_DELTA = FORBIDDEN
FIXED_INTEGER_TICK = REQUIRED
```

- 모든 timer는 tick 또는 제한된 scaled integer 시간으로 표현한다.
- exact tick duration은 fixture와 결과에 명시한다.
- 렌더 FPS는 결과에 영향을 주지 않는다.

### 5.3 ID와 순서

```text
STABLE_OBJECT_ID = REQUIRED
UNSORTED_DICTIONARY_ITERATION_AS_GAMEPLAY_ORDER = FORBIDDEN
EXPLICIT_SORT_KEY = REQUIRED
SAME_TICK_EVENT_SEQUENCE = REQUIRED
```

기본 동률 처리 방향:

```text
rule-specific priority
→ stable lane order
→ stable quantized position
→ stable object ID
```

정확 규칙은 각 Resolver 책임 원본이 소유한다.

### 5.4 위치·숫자

- deterministic 비교에 사용되는 위치는 양자화된 좌표 또는 고정된 lane anchor ID를 사용한다.
- `NaN`, `INF`, 숨은 epsilon 비교를 금지한다.
- float가 필요한 제품 표현과 deterministic 판정 값을 분리한다.
- 초기 Gate에서는 서로 다른 CPU·OS의 bitwise float parity를 완료 조건으로 주장하지 않는다.

## 6. 출력 계약

각 실행은 다음 결과 묶음을 생성한다.

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

### 6.1 Event Log

필수 공통 event envelope:

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

이벤트는 UI 문구가 아니라 원인 추적과 replay를 위한 도메인 기록이다.

### 6.2 Metrics Summary

최소 지표:

```text
lane victory / defense success
objective survival / capture
time to collapse or stabilization
damage dealt / prevented
health-floor prevented lethal damage
cast count / interval
READY waiting time
no-cast rate
precheck failure rate
combat-end committed cancellation rate
active uptime
A/B/C comparison delta
other-two-lane contribution
```

### 6.3 Fingerprint

- 동일 canonical typed state는 동일 fingerprint를 생성해야 한다.
- fingerprint algorithm은 구현 계획에서 고정한다.
- raw Dictionary 순서나 raw JSON text를 fingerprint 권위로 사용하지 않는다.
- fingerprint 불일치는 첫 divergent tick과 event sequence를 보고해야 한다.

## 7. A/B/C 비교 계약

```text
A = 표준 [영웅]
B = 같은 source archetype의 해금 이름 지정 [영웅]
C = 같은 계열 표준 [전설]
```

한 comparison group에서 다음은 동일해야 한다.

```text
fixture base state
master seed and named RNG streams
source Tier and passive stage
Stage and enemy composition
buildings and objectives
other-two-lane state
ordered external commands
parameter set except compared grade/kit fields
```

A/B/C 중 비교 대상 외 필드가 달라지면 해당 run은 `INVALID_COMPARISON`으로 판정한다.

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

각 family는 하나의 fixture에 고정하지 않고 최소한 여러 난이도·배치·seed 변형을 가질 수 있어야 한다. 정확 표본 수는 후속 acceptance Decision에서 확정한다.

## 9. 검증 Tier

### T0 — Schema validation

- 필수 필드 존재.
- version 지원.
- stable ID 중복 없음.
- numeric range와 enum 유효.
- 비교 group의 변경 허용 필드 검사.

### T1 — Replay determinism

```text
same fixture + same ordered input + same reference environment
→ identical event log
→ identical checkpoint fingerprints
→ identical final state fingerprint
```

### T2 — Rule invariants

예시:

```text
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
READY count <= 1
resolved event ID executes once
precommit invalidation consumes no cooldown
unresolved commit does not cross Stage
clone has no independent target or skill cast
```

### T3 — Paired A/B/C comparison

A/B/C가 같은 fixture·seed·입력을 공유하는지 확인하고 metric delta를 생성한다.

### T4 — Aggregate balance evaluation

표본 수·허용오차·파워 통과선이 승인된 뒤에만 수행한다. 현재 Decision은 T4 결과를 만들거나 밸런스를 확정하지 않는다.

### T5 — Product runtime adapter

실제 Godot 전투 Scene의 snapshot·event를 Harness와 비교하는 단계다. 초기 Harness scope에 포함하지 않으며 별도 구현 Gate가 필요하다.

## 10. 재현성 수준

초기 필수 재현성:

```text
same approved engine build
+ same reference CI environment
+ same fixture and ordered input
= bit-identical canonical event and state fingerprints
```

추가 목표:

```text
same engine build across supported OS/CPU
= semantically equivalent metrics and events
```

cross-platform bitwise parity는 fixed-point·physics·navigation 전략이 승인되기 전까지 완료 조건이 아니다.

## 11. 적대적 검토

### OMW-AUD-208 — 전역 RNG 결합

한 시스템의 random draw 추가가 다른 시스템 결과를 바꿀 수 있다.

대응: named RNG stream과 draw count 기록.

### OMW-AUD-209 — wall-clock·frame delta 유입

실행 속도와 FPS가 전투 결과를 바꿀 수 있다.

대응: fixed integer tick 외 시간 입력 금지.

### OMW-AUD-210 — collection 순서 불안정

Dictionary·node traversal 순서가 target·damage 순서를 바꿀 수 있다.

대응: stable ID와 explicit sort key.

### OMW-AUD-211 — float·플랫폼 차이

같은 공식도 CPU·OS에서 bitwise 차이가 생길 수 있다.

대응: deterministic-critical 값은 scaled integer·양자화 사용, 초기 cross-platform bitwise claim 금지.

### OMW-AUD-212 — fixture drift

fixture가 실제 정본 schema와 분리되면 잘못된 결론을 만든다.

대응: schema version·parameter set ID·authority commit 기록과 migration 검사.

### OMW-AUD-213 — 10개 family 과적합

정해진 family만 통과하도록 영웅을 조정할 수 있다.

대응: family당 변형과 holdout fixture를 후속 acceptance plan에 포함.

### OMW-AUD-214 — Harness와 제품 runtime 분기

순수 도메인 결과가 실제 Scene에서 재현되지 않을 수 있다.

대응: 이후 product adapter T5를 별도 필수 Gate로 둔다.

### OMW-AUD-215 — 과도한 event log 비용

모든 상태를 매 tick 기록하면 대량 batch가 느려진다.

대응: 원인 event는 항상 기록하고 full snapshot은 configurable checkpoint에서만 기록.

### OMW-AUD-216 — placeholder 값으로 밸런스 확정

Harness 구조가 준비됐다는 이유로 임시 수치 결과를 정본화할 수 있다.

대응: parameter set status와 acceptance Decision이 없으면 balance result는 `EXPLORATORY_ONLY`.

### OMW-AUD-217 — A/B/C 비교 오염

등급 외 건물·seed·적 배치가 달라지면 파워 위계 결론이 왜곡된다.

대응: comparison field diff validator와 paired run.

### OMW-AUD-218 — 다른 두 전선 제거

단일 전선 전투만 보면 고등급 1명 제한의 전략 비용을 측정하지 못한다.

대응: other-two-lane state와 contribution metric을 fixture 필수 필드로 유지.

### OMW-AUD-219 — save·Retry 상태 누락

timer·RNG·commit·resolved 상태를 저장하지 않으면 replay가 일치하지 않는다.

대응: save round-trip fixture와 checkpoint fingerprint를 T1/T2에 포함.

### OMW-AUD-220 — headless를 결정론으로 오인

창을 띄우지 않는 실행은 결정론을 자동 보장하지 않는다.

대응: headless는 실행 수단일 뿐이고 결정론은 입력·시간·RNG·순서·숫자 계약으로 보장한다.

## 12. 명시적 제외

```text
PRODUCT_SCENE_EXECUTION = NOT_AUTHORIZED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
EXACT_COMBAT_SCHEMA = PENDING
EXACT_TICK_RATE = PENDING
EXACT_DAMAGE_AND_DEFENSE_FORMULA = PENDING
EXACT_HERO_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
BALANCE_CONCLUSION = FORBIDDEN
CROSS_PLATFORM_BITWISE_PARITY = NOT_CLAIMED
```

## 13. 완료 조건

이 Decision의 기획 완료 조건:

- Harness 계층·입력·출력·재현성 범위가 정본에 기록됨.
- A/B/C paired comparison과 10개 encounter family가 연결됨.
- RNG·tick·stable ordering·fingerprint 경계가 기록됨.
- headless·JSON·float의 한계가 명시됨.
- 제품 구현·simulation 실행이 승인되지 않았음.

## 14. 다음 Gate

```text
NEXT_DECISION
= OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
```

다음 결정에서 다음을 고정한다.

- 공통 Unit·Building·Objective state schema.
- 피해·방어·보호·상태이상 분류.
- threat·role·frontline·backline·cluster 의미.
- 위치 양자화와 stable ID.
- 동일 tick resolution order.
- fixture가 참조할 정확한 field dictionary.

## 15. 공식 참고 자료

- Godot Engine command line tutorial — `--headless`와 CI script 실행.
  - https://docs.godotengine.org/en/4.4/tutorials/editor/command_line_tutorial.html
- Godot Engine idle and physics processing — fixed physics processing과 variable idle processing 구분.
  - https://docs.godotengine.org/en/4.6/tutorials/scripting/idle_and_physics_processing.html
- Godot Engine random number generation / RandomNumberGenerator — seed·state와 복수 RNG instance.
  - https://docs.godotengine.org/en/stable/tutorials/math/random_number_generation.html
  - https://docs.godotengine.org/en/4.7/classes/class_randomnumbergenerator.html
- Godot Engine JSON / FileAccess — 직렬화와 숫자·파일 경계.
  - https://docs.godotengine.org/en/stable/classes/class_json.html
  - https://docs.godotengine.org/en/stable/classes/class_fileaccess.html

외부 자료는 OMENWARD exact schema·수치·구현 권위가 아니라 설계·제작 경계의 참고 근거다.
