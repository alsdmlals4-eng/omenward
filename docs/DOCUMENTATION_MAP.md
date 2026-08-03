# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-03
work_mode: TOTAL_PLANNING
current_phase: DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_APPROVED
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
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
current_grill_me_count: 3
preflight: NEXT_AT_10_OF_10
next_gate: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
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
| 승인 Decision·3/10 카운터 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_AUTHORITY / ACTIVE_BRANCH` |
| 결정론적 simulation Harness 범위 | `design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md` | `CURRENT_HARNESS_SCOPE_AUTHORITY / NOT_IMPLEMENTED` |
| 공통 전투 Schema·동일 tick 처리 순서 | `design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md` | `CURRENT_COMMON_COMBAT_AUTHORITY / NOT_IMPLEMENTED` |
| 피해 채널·보호·상태 의미 | `design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md` | `CURRENT_DAMAGE_PROTECTION_STATUS_AUTHORITY / NOT_IMPLEMENTED` |
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
→ ProtectionInstance / StatusInstance / PendingCommit / ActiveEffect
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

## 6. Fixed-Tick Resolution Order

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

## 7. Damage·Protection·Status 라우팅

```text
KINETIC → ARMOR
ARCANE  → RESISTANCE
```

```text
DamageIntent
RestoreIntent
ProtectionIntent
StatusApplicationIntent
```

채널과 다른 분류는 독립이다.

```text
DELIVERY_TAGS = BASIC / SKILL / AREA / DAMAGE_OVER_TIME / ENVIRONMENT / TRANSFERRED
TARGET_PROFILE = UNIT / BUILDING / OBJECTIVE + GROUND / FLYING
```

금지:

```text
TRUE_DAMAGE
EXECUTE_OR_INSTANT_KILL
REVIVE
CHANNEL_INFERRED_FROM_VFX_OR_UNIT_NAME
FLYING_OR_SIEGE_AS_DAMAGE_CHANNEL
```

### R80 내부 의미

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
BARRIER != HP_OR_HEAL
RESTORE != NEGATIVE_DAMAGE
TRANSFER_DEPTH_MAX = 1
SECOND_MITIGATION_PASS_ON_TRANSFER = FORBIDDEN
RETROACTIVE_STATUS_COMMIT_CANCELLATION = FORBIDDEN
```

정확 formula·rounding·cap·duration은 다음 numeric Gate가 소유한다.

## 8. Status·Target Boundary

Status family:

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

Stacking policy:

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

- OBJECTIVE는 기본 HP target이 아니다.
- BUILDING은 명시적 building eligibility가 필요하다.
- FLYING·GROUND는 targeting eligibility이며 damage channel이 아니다.
- 일반 status는 이미 commit된 same-tick 행동을 소급 취소하지 않는다.

## 9. Event·Metric 권위

```text
RAW_DAMAGE
POST_MITIGATION_DAMAGE
BARRIER_ABSORBED
FINAL_HP_LOSS
RESTORE_AMOUNT
STATUS_RESULT
```

위 단계는 서로 다른 metric이며 중복 집계하지 않는다. 모든 event는 root effect·source·target·channel/tag·tick/phase/sequence와 해당 시 deployment_id를 보존한다.

## 10. 동일 Tick 공정성

```text
ALL_ELIGIBLE_ACTORS_COMMIT_FROM_SAME_PHASE_SNAPSHOT
SEQUENTIAL_ENTITY_ID_KILL_ADVANTAGE = FORBIDDEN
FALLBACK_RETARGET_AFTER_COMMIT = FORBIDDEN
DEATH_FINALIZATION_BEFORE_DAMAGE_BATCH_END = FORBIDDEN
OBJECTIVE_USES_POST_DEATH_SURVIVORS = REQUIRED
DESTROYED_BUILDING_PASSIVE_REMOVED_AFTER_FINALIZE = REQUIRED
RETROACTIVE_STATUS_COMMIT_CANCELLATION = FORBIDDEN
```

## 11. 검증 Tier

```text
T0 = fixture/common schema/channel/tag/target/stack validation
T1 = replay determinism and phase-event parity
T2 = same-tick fairness·death/objective·provenance·damage/protection/status invariants
T3 = paired A/B/C metrics with all three lanes and KINETIC/ARCANE response
T4 = aggregate balance after acceptance approval
T5 = product runtime adapter after separate authorization
```

현재 승인된 설계 범위는 T0~T3다.

## 12. 벤치마크 경계

- Godot fixed physics callback과 variable idle frame을 구분한다.
- RNG는 개별 seed·state를 가진 named stream으로 분리한다.
- JSON 숫자·문자열 표현 자체를 canonical fingerprint 권위로 사용하지 않는다.
- TFT의 Armor/Magic Resistance 분리는 참고하되 아이템 메타와 복합 channel은 복사하지 않는다.
- Guild Wars 2의 Barrier는 HP와 분리된 임시 buffer 참고 사례로만 사용한다.
- Overwatch barrier 조정 사례처럼 barrier uptime이 전투 pace와 선택을 대체하면 stop-ship이다.
- 외부 게임 전투 순서를 복사하지 않고 OMENWARD 세 전선·룰렛 provenance·점령 인과를 우선한다.

## 13. 적대적 검토

```text
OMW-AUD-208 ~ OMW-AUD-220 = Harness scope
OMW-AUD-221 = Sheet stale PR-head / resolved / non-counter
OMW-AUD-222 ~ OMW-AUD-232 = common combat schema·resolution order
OMW-AUD-233 ~ OMW-AUD-246 = damage·protection·status semantics
```

주요 방어:

```text
DeploymentProvenance required
Hero special-case pollution forbidden
phase snapshot and barrier required
post-death objective resolution required
quantized 2D position required
channel/tag/target separation required
barrier/restore/transfer/status meanings separated
R120 fingerprint barrier required
```

## 14. 구현 전 우선순위

```text
P0 = deterministic Harness scope — APPROVED
P1 = common combat schema·resolution order — APPROVED
P2 = damage·protection·status semantics — APPROVED
P3 = mitigation formula·protection numeric defaults — NEXT
P4 = tick·activation·quantization technical defaults
P5 = Hero exact Trigger·timer·effects
P6 = A/B/C tolerance·sample·stop-ship
P7 = roulette/economy 100,000-seed simulation
P8 = checkpoint/save schema
P9 = implementation package·Red tests·regression·rollback
```

## 15. 구현 경계

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
CURRENT_COUNT = 3/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
NEXT_PREFLIGHT = AT_10_OF_10
CURRENT_PLANNING_PR = RESOLVE_FROM_OPEN_PR
LAST_MAINTENANCE_PR = 132
```
