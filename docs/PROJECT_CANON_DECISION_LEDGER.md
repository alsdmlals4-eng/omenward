# 오멘워드 기획 정본 결정 원장

```yaml
updated_at: 2026-08-03
status: CURRENT_DECISION_LEDGER / ACTIVE_PLANNING_BRANCH
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
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
grill_me_approved_since_last_merge: 1
future_merge_cadence: 10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
next_gate: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
```

`current_main`과 `current_planning_pr`은 실행 시점에 저장소에서 해석한다. 최신 Decision은 simulation Harness의 기획 범위만 승인하며 코드 구현·simulation 실행 권한을 부여하지 않는다.

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
| `OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1` | `USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED` | headless 순수 도메인 fixed-tick Harness, versioned fixture, named RNG, stable ID, event log, fingerprint, paired A/B/C 비교 | `design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md` | exact combat schema·tick rate·formula·tool code·execution pending |
| `OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1` | `USER_APPROVED / MAIN_CANONICAL / NOT_IMPLEMENTED` | 공개 Trigger·same-lane Filter·Priority·stable tie-break·commit Snapshot, A/B/C encounter 파워 위계 검증 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TRIGGER_TARGET_AND_POWER_BUDGET_VALIDATION_2026-08-03.md` | exact schema·threshold·values·simulation·runtime·human pending |

## 3. Harness 승인 계약

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

## 4. Harness 입력·출력

필수 입력 상위 필드:

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

필수 출력:

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

JSON은 manifest 교환 형식일 수 있지만 raw JSON 문자열과 float 변환 결과는 상태 hash 권위가 아니다.

## 5. 검증 Tier

```text
T0 = fixture schema validation
T1 = replay determinism
T2 = rule invariants
T3 = paired A/B/C metrics
T4 = aggregate balance evaluation after acceptance approval
T5 = product runtime adapter after separate authorization
```

현재 승인 범위는 T0~T3의 기획 계약이다.

## 6. A/B/C 비교 계약

```text
A = 표준 [영웅]
B = 같은 source archetype 해금 이름 지정 [영웅]
C = 같은 계열 표준 [전설]
```

paired group에서 fixture·seed·source Tier·Stage·적 구성·건물·다른 두 전선·ordered input은 같아야 한다. 등급/키트 외 필드가 달라지면 `INVALID_COMPARISON`이다.

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

## 7. 벤치마크·현업 경계

공식 Godot 자료를 적용했다.

- `--headless`와 CI script 실행.
- fixed physics process와 variable idle frame 구분.
- `RandomNumberGenerator` seed·state·복수 stream.
- JSON 숫자 float 변환·FileAccess 직렬화 경계.

```text
REFERENCE_ENVIRONMENT_BIT_PARITY = REQUIRED_LATER
CROSS_PLATFORM_FLOAT_BIT_PARITY = NOT_CLAIMED
SCALED_INTEGER_OR_QUANTIZED_CRITICAL_VALUES = RECOMMENDED_BOUNDARY
```

## 8. 적대적 검토

```text
OMW-AUD-208 global RNG coupling
OMW-AUD-209 wall-clock or frame delta leakage
OMW-AUD-210 unstable collection iteration order
OMW-AUD-211 float and cross-platform divergence
OMW-AUD-212 fixture drift from canon
OMW-AUD-213 encounter-family overfitting
OMW-AUD-214 harness/runtime divergence
OMW-AUD-215 excessive event-log cost
OMW-AUD-216 placeholder balance conclusions
OMW-AUD-217 contaminated A/B/C comparison
OMW-AUD-218 omitted other-two-lane contribution
OMW-AUD-219 missing save/Retry state
OMW-AUD-220 headless mistaken for determinism
```

## 9. 기존 Hero 정본 계보

PR #129에서 병합된 영웅 등급·초기 5명·cooldown·Stage·Trigger·파워 검증 Decision은 main 정본이다. 상세 계보는 각 `APPROVED_OMENWARD_*` 책임 원본과 이전 원장 history에서 확인한다.

핵심 불변식:

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
MAX_STORED_READY_COUNT = 1
MANUAL_CAST_OR_TARGET = FORBIDDEN
ACTIVE_EFFECT_OR_UNRESOLVED_COMMIT_STAGE_CARRY = FORBIDDEN
```

## 10. 비카운트 운영 정책·Sync

| ID | 상태 | 역할 |
|---|---|---|
| `OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1` | `ACTIVE_STANDING_POLICY / MAIN_CANONICAL` | 공식 벤치마크·차이·제작비·QA·적대적 검토를 모든 Grill Me에 적용 |
| `OMW-SYNC-20260803-LIFECYCLE-STATUS-CLEANUP-V1` | `MAINTENANCE_SYNC / MAIN_CANONICAL / NON_COUNTER` | Decision 생명주기 우선순위 교정 |
| `OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1` | `MAINTENANCE_SYNC / MAIN_CANONICAL / NON_COUNTER` | 구현 상태·미확정 목록 최신화와 simulation-first Gate 라우팅 |

## 11. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = USER_APPROVED_HARNESS_SCOPE_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
SIMULATION_TOOL_CODE_AUTHORITY = NONE
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

## 12. 카운터·다음 Gate

```text
CURRENT_COUNT_SINCE_MERGE = 1_OF_10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
NEXT_PREFLIGHT_AT = 10_OF_10
```
