# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-03
work_mode: TOTAL_PLANNING
current_phase: DETERMINISTIC_SIMULATION_HARNESS_SCOPE_APPROVED
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
parent_gameplay_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
last_sync: OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-simulation-harness-planning-20260803
active_base: 9.4.3_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED
product_code_authority: NONE
simulation_tool_code_authority: NONE
last_merged_planning_pr: 129
last_maintenance_pr: 132
current_planning_pr: RESOLVE_FROM_OPEN_PR
current_grill_me_count: 1
preflight: NEXT_AT_10_OF_10
next_gate: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
```

이 문서는 질문별 현행 책임 원본을 선택하는 라우터다. `current_main`과 `current_planning_pr`은 실행 시점에 저장소에서 해석한다.

## 1. 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ DOCUMENTATION_MAP.md
→ PROJECT_CORE.md
→ PROJECT_CANON_DECISION_LEDGER.md
→ 현재 질문의 APPROVED 분야 문서
→ benchmark·production comparison 자료
→ CURRENT_IMPLEMENTATION_STATUS.md
→ DECISIONS_PENDING.md
→ ACTIVE_CONTEXT.md
→ HANDOFF_CONTEXT.md
→ 실제 code/data/Scene/Resource/tests
→ 연결 Google Sheet
```

## 2. 현재 책임 원본

| 질문 | 현행 책임 원본 | 권한 |
|---|---|---|
| 제품 정체성·플레이어 약속 | `PROJECT_CORE.md` | `CURRENT_CORE_AUTHORITY` |
| 승인 Decision·1/10 카운터 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_AUTHORITY / ACTIVE_BRANCH` |
| 결정론적 simulation Harness 범위 | `design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md` | `CURRENT_HARNESS_SCOPE_AUTHORITY / NOT_IMPLEMENTED` |
| Grill Me 벤치마크·현업 비교 | `process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md` | `ACTIVE_STANDING_POLICY / NON_COUNTER` |
| 전체 시스템 Vertical Slice | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `CURRENT_VERTICAL_SLICE_AUTHORITY / NOT_IMPLEMENTED` |
| Vertical Slice 적대적 검토 | `reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md` | `CURRENT_ADVERSARIAL_REVIEW_LINEAGE` |
| 룰렛 통제감 Evidence Pilot | `benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` | `PILOT_RECOMMENDATION / NOT_CANON` |
| 병종 등급·Tier·표준 스킬 | `design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md` | `MERGED_STANDARD_GRADE_AUTHORITY` |
| 영웅 이상 전역 단일 활성·해금 스킬 교체 | `design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md` | `MAIN_CANONICAL_GRADE_SLOT_AND_SKILL_AUTHORITY` |
| 초기 5명 고유 2스킬 | `design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md` | `MAIN_CANONICAL_FIRST_FIVE_SKILL_AUTHORITY` |
| cooldown·charge·실패 정책 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_COOLDOWN_CHARGE_AND_FAILURE_POLICY_2026-08-03.md` | `MAIN_CANONICAL_TIMER_PARENT` |
| timer 지속·Stage 경계 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TIMER_PERSISTENCE_AND_STAGE_BOUNDARY_POLICY_2026-08-03.md` | `MAIN_CANONICAL_TIMER_STAGE_AUTHORITY` |
| Trigger·대상·파워 검증 | `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TRIGGER_TARGET_AND_POWER_BUDGET_VALIDATION_2026-08-03.md` | `MAIN_CANONICAL_TRIGGER_TARGET_POWER_AUTHORITY` |
| 실제 구현·Legacy·main 기획 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 미확정 schema·수치·검증 우선순위 | `DECISIONS_PENDING.md` | `CURRENT_PENDING_AUTHORITY` |
| 현재 작업·다음 Gate | `ACTIVE_CONTEXT.md` | `CURRENT_CONTEXT_PACK` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF` |
| Google Sheet 동기화 | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `CURRENT_SHEET_CONTRACT` |

## 3. Evidence Pilot 경계

```text
PILOT_RECOMMENDATION / NOT_CANON
```

`benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md`는 반드시 라우팅하지만 APPROVED 정본이나 구현 완료 증거가 아니다.

## 4. Harness 선택 구조

```text
Godot --headless --script
→ versioned fixture
→ pure domain state
→ fixed integer tick scheduler
→ deterministic resolvers
→ event log / metrics / fingerprints
```

초기 Harness에서 제외:

```text
full production battle Scene
rendering and audio
real-time frame delta
NavigationServer and PhysicsServer dependency
balance acceptance conclusion
product runtime adapter
```

## 5. 입력·출력 라우팅

입력:

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

출력:

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

## 6. 결정론 불변식

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

headless는 실행 방식일 뿐 결정론 보장이 아니다.

## 7. 검증 Tier

```text
T0 = fixture schema validation
T1 = replay determinism
T2 = rule invariants
T3 = paired A/B/C metrics
T4 = aggregate balance after acceptance approval
T5 = product runtime adapter after separate authorization
```

현재 승인된 설계 범위는 T0~T3다.

## 8. A/B/C 라우팅

```text
A = 표준 [영웅]
B = 같은 source archetype 해금 이름 지정 [영웅]
C = 같은 계열 표준 [전설]
```

paired group에서 seed·Stage·적 구성·건물·다른 두 전선·ordered input은 같아야 한다. 비교 대상 외 차이는 `INVALID_COMPARISON`이다.

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

## 9. 벤치마크 경계

- Godot `--headless`는 CI script 실행 수단이다.
- fixed physics process와 variable idle frame을 구분한다.
- RNG는 개별 seed·state를 가진 named stream으로 분리한다.
- JSON 숫자는 float로 변환될 수 있으므로 raw JSON text를 fingerprint 권위로 쓰지 않는다.
- deterministic-critical 값은 scaled integer·quantized position·string ID를 우선한다.
- cross-platform float bitwise parity는 현 Gate의 완료 조건이 아니다.

## 10. 구현 전 우선순위

```text
P0 APPROVED_SCOPE → deterministic Harness 범위·입출력·재현성
P1 NEXT → common combat schema·resolution order
P2 → Hero exact Trigger·timer·effects
P3 → A/B/C tolerance·sample·stop-ship
P4 → roulette/economy 100,000-seed simulation
P5 → checkpoint/save schema
P6 → implementation package·Red tests·regression·rollback
```

## 11. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = HARNESS_SCOPE_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
EXACT_COMBAT_SCHEMA = PENDING
EXACT_TICK_RATE = PENDING
EXACT_FORMULAS_AND_VALUES = PENDING
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 12. Decision 생명주기 상태 우선순위

```text
PROJECT_CANON_DECISION_LEDGER.md
→ ACTIVE_CONTEXT.md
→ DOCUMENTATION_MAP.md 권한 열
→ 개별 Decision 문서의 status 필드
```

개별 문서의 과거 branch 상태는 계보 증거일 뿐 현재 원장 분류를 뒤집지 않는다. 제품 구현 여부는 `CURRENT_IMPLEMENTATION_STATUS.md`와 실제 product path가 소유한다.

## 13. 운영 Gate

```text
CURRENT_COUNT = 1/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
NEXT_PREFLIGHT = AT_10_OF_10
CURRENT_PLANNING_PR = RESOLVE_FROM_OPEN_PR
LAST_MAINTENANCE_PR = 132
```
