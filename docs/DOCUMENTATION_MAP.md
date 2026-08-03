# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-03
work_mode: TOTAL_PLANNING
current_phase: COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_APPROVED
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_validation_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
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
current_grill_me_count: 2
preflight: NEXT_AT_10_OF_10
next_gate: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
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
| 승인 Decision·2/10 카운터 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_AUTHORITY / ACTIVE_BRANCH` |
| 결정론적 simulation Harness 범위 | `design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md` | `CURRENT_HARNESS_SCOPE_AUTHORITY / NOT_IMPLEMENTED` |
| 공통 전투 Schema·동일 tick 처리 순서 | `design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md` | `CURRENT_COMMON_COMBAT_AUTHORITY / NOT_IMPLEMENTED` |
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

## 4. Harness 상위 구조

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

## 5. 공통 Combat Schema 라우팅

```text
CombatRunState
→ LaneState[TOP,MID,BOTTOM]
→ CombatantState / BuildingState / ObjectiveState
→ DeploymentProvenance
→ OrderedCommand
→ ActionIntent / EffectIntent
→ StatusInstance / PendingCommit / ActiveEffect
→ phase resolver
→ event / metric / fingerprint
```

필수 core-fit:

```text
SpinSnapshot and TokenSource provenance
three-lane full state
irreversible lane commitment
building and objective state
other-two-lane contribution
```

영웅·전설은 이 공통 Schema를 확장한다. 영웅별 별도 AI loop·tick clock·death resolver·save identity는 금지한다.

## 6. fixed-tick Resolution Order

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

동일 tick actor는 같은 post-movement snapshot에서 intent를 commit한다. entity ID 순차 피해로 같은 tick 행동이 지워지는 것을 금지한다.

## 7. 위치·정렬·event 권위

```text
position_q = {x_q, y_q, anchor_id}
lane_order = TOP(0), MID(1), BOTTOM(2)
canonical_key = lane_order → entity_kind_order → spawn_sequence → stable_id → local_sequence
```

1D lane 좌표만으로 실제 거리 기반 cross-lane 효과를 계산하지 않는다. Dictionary·SceneTree traversal은 resolution order 권위가 아니다.

공통 event:

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

## 8. 피해·보호 상위 순서

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

정확 공식과 수치는 다음 Gate가 소유한다. health-floor는 회복이 아니며 명시적 revive 계약 없이는 사망을 되돌리지 않는다.

## 9. 동일 tick 공정성

```text
ALL_ELIGIBLE_ACTORS_COMMIT_FROM_SAME_PHASE_SNAPSHOT
SEQUENTIAL_ENTITY_ID_KILL_ADVANTAGE = FORBIDDEN
FALLBACK_RETARGET_AFTER_COMMIT = FORBIDDEN
DEATH_FINALIZATION_BEFORE_DAMAGE_BATCH_END = FORBIDDEN
OBJECTIVE_USES_POST_DEATH_SURVIVORS = REQUIRED
DESTROYED_BUILDING_PASSIVE_REMOVED_AFTER_FINALIZE = REQUIRED
```

## 10. 검증 Tier

```text
T0 = fixture and common schema validation
T1 = replay determinism and phase-event parity
T2 = same-tick fairness·death/objective order·provenance invariants
T3 = paired A/B/C metrics with all three lanes
T4 = aggregate balance after acceptance approval
T5 = product runtime adapter after separate authorization
```

현재 승인된 설계 범위는 T0~T3다.

## 11. A/B/C 라우팅

```text
A = 표준 [영웅]
B = 같은 source archetype 해금 이름 지정 [영웅]
C = 같은 계열 표준 [전설]
```

paired group에서 seed·Stage·적 구성·건물·다른 두 전선·ordered input은 같아야 한다. 비교 대상 외 차이는 `INVALID_COMPARISON`이다.

## 12. 벤치마크 경계

- Godot fixed physics callback과 variable idle frame을 구분한다.
- RNG는 개별 seed·state를 가진 named stream으로 분리한다.
- JSON 숫자·문자열 표현 자체를 canonical fingerprint 권위로 사용하지 않는다.
- deterministic-critical 값은 scaled integer·quantized position·stable ID를 우선한다.
- 외부 게임 전투 순서를 복사하지 않고 OMENWARD 세 전선·룰렛 provenance·점령 인과를 우선한다.

## 13. 적대적 검토

```text
OMW-AUD-208 ~ OMW-AUD-220 = Harness scope
OMW-AUD-221 = Sheet stale PR-head / resolved / non-counter
OMW-AUD-222 ~ OMW-AUD-232 = common combat schema·resolution order
```

주요 방어:

```text
DeploymentProvenance required
Hero special-case pollution forbidden
phase snapshot and barrier required
post-death objective resolution required
quantized 2D position required
R120 fingerprint barrier required
```

## 14. 구현 전 우선순위

```text
P0 = deterministic Harness scope — APPROVED
P1 = common combat schema·resolution order — APPROVED
P2 = damage·protection·status semantics — NEXT
P3 = Hero exact Trigger·timer·effects
P4 = A/B/C tolerance·sample·stop-ship
P5 = roulette/economy 100,000-seed simulation
P6 = checkpoint/save schema
P7 = implementation package·Red tests·regression·rollback
```

## 15. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = COMMON_COMBAT_SCHEMA_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
EXACT_TICK_RATE = PENDING
EXACT_DAMAGE_DEFENSE_PROTECTION_FORMULAS = PENDING
EXACT_ACTIVATION_POLICY = PENDING
EXACT_HERO_VALUES = PENDING
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 16. Decision 생명주기 상태 우선순위

```text
PROJECT_CANON_DECISION_LEDGER.md
→ ACTIVE_CONTEXT.md
→ DOCUMENTATION_MAP.md 권한 열
→ 개별 Decision 문서의 status 필드
```

개별 문서의 과거 branch 상태는 계보 증거일 뿐 현재 원장 분류를 뒤집지 않는다. 제품 구현 여부는 `CURRENT_IMPLEMENTATION_STATUS.md`와 실제 product path가 소유한다.

## 17. 운영 Gate

```text
CURRENT_COUNT = 2/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
NEXT_PREFLIGHT = AT_10_OF_10
CURRENT_PLANNING_PR = RESOLVE_FROM_OPEN_PR
LAST_MAINTENANCE_PR = 132
```
