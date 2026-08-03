# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-03
work_mode: TOTAL_PLANNING
current_phase: MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_APPROVED
current_planning_decision: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
parent_semantics_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_harness_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
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
current_grill_me_count: 4
preflight: NEXT_AT_10_OF_10
next_gate: OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
```

이 문서는 질문별 현행 책임 원본을 선택하는 라우터다. 실행 시점 SHA와 PR은 저장소에서 다시 확인한다.

## 1. 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ DOCUMENTATION_MAP.md
→ PROJECT_CORE.md
→ PROJECT_CANON_DECISION_LEDGER.md
→ 현재 질문의 APPROVED 책임 원본
→ benchmark·production comparison
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
| 승인 Decision·4/10 카운터 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_AUTHORITY / ACTIVE_BRANCH` |
| Deterministic Harness 범위 | `design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md` | `CURRENT_HARNESS_SCOPE_AUTHORITY / NOT_IMPLEMENTED` |
| 공통 전투 Schema·동일 tick 순서 | `design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md` | `CURRENT_COMMON_COMBAT_AUTHORITY / NOT_IMPLEMENTED` |
| Damage·Protection·Status 의미 | `design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md` | `CURRENT_DAMAGE_SEMANTICS_AUTHORITY / NOT_IMPLEMENTED` |
| 방어 공식·보호·상태 초기 수치 | `design/APPROVED_OMENWARD_MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_2026-08-03.md` | `CURRENT_COMBAT_NUMERIC_DEFAULTS_AUTHORITY / NOT_IMPLEMENTED` |
| 전체 시스템 Vertical Slice | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `CURRENT_VERTICAL_SLICE_AUTHORITY / NOT_IMPLEMENTED` |
| Vertical Slice 적대적 검토 | `reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md` | `CURRENT_ADVERSARIAL_REVIEW_LINEAGE` |
| 룰렛 통제감 Evidence Pilot | `benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` | `PILOT_RECOMMENDATION / NOT_CANON` |
| Grill Me 벤치마크 정책 | `process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md` | `ACTIVE_STANDING_POLICY / NON_COUNTER` |
| 병종 등급·Tier·표준 스킬 | `design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md` | `MERGED_STANDARD_GRADE_AUTHORITY` |
| 영웅 등급·슬롯·해금 교체 | `design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md` | `MAIN_CANONICAL_GRADE_SLOT_AUTHORITY` |
| 초기 5명 고유 2스킬 | `design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md` | `MAIN_CANONICAL_FIRST_FIVE_AUTHORITY` |
| 영웅 cooldown·Stage·Trigger·파워 | 관련 `APPROVED_OMENWARD_HERO_*` 문서 | `MAIN_CANONICAL_HERO_VALIDATION_AUTHORITY` |
| 실제 구현·Legacy·최신 기획 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 미확정 기술·값·검증 | `DECISIONS_PENDING.md` | `CURRENT_PENDING_AUTHORITY` |
| 현재 작업·다음 Gate | `ACTIVE_CONTEXT.md` | `CURRENT_CONTEXT_PACK` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF` |
| Google Sheet 동기화 | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `CURRENT_SHEET_CONTRACT` |

## 3. Evidence Pilot 경계

```text
PILOT_RECOMMENDATION / NOT_CANON
```

`benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md`는 벤치마크·가설·검증 후보를 제공하지만 APPROVED 정본이나 구현 권한이 아니다. 현행 Vertical Slice 책임 원본과 충돌하면 ADAPT 또는 REJECT하고 정본을 우선한다.

## 4. 검증 계층

```text
P0 Harness Scope
→ P1 Common Combat Schema·R00~R130
→ P2 Damage·Protection·Status Semantics
→ P3 Mitigation·Protection Numeric Defaults
→ P4 Fixed Tick·Time·Activation Defaults
→ P5 Hero Exact Trigger·Timer·Effects
→ P6 A/B/C Sample·Tolerance·Stop-Ship
→ P7 Implementation Package·Red Tests·Rollback
```

현재 P0~P3만 사용자 승인된 기획 계약이다.

## 5. Core-First Combat 라우팅

```text
SpinSnapshot / TokenSource / lane commit provenance
→ CombatRunState + three LaneState
→ Combatant / Building / Objective
→ OrderedCommand / Intent / Protection / Status
→ R00~R130 fixed phase resolver
→ ordered event / metric / fingerprint
→ next Stage design feedback
```

영웅·전설은 공통 계약을 확장하며 별도 AI loop·clock·damage formula·death resolver를 만들지 않는다.

## 6. 피해·보호 의미 라우팅

```text
KINETIC → ARMOR
ARCANE  → RESISTANCE
```

```text
channel != delivery tag != target profile
Barrier != HP != Heal != Defense
Restore != negative damage
Health Floor != Heal != Revive
HP-loss transfer != new attack != true damage
```

```text
R80A validity
→ R80B protection setup
→ R80C mitigation and Barrier
→ R80D redirection and Floor
→ R80E HP delta and Restore
→ R80F Status and post-hit
→ R80G death mark
```

## 7. 현행 수치 권위

```text
DEFENSE_MIN = 0
DEFENSE_MAX = 300
MITIGATION_CONSTANT = 100
MINIMUM_VALID_DAMAGE = 1
ROUNDING = POSITIVE_INTEGER_HALF_UP
```

```text
post_mitigation
= max(1, round_half_up(adjusted_damage * 100 / (100 + effective_defense)))
```

```text
BARRIER_TOTAL_CAP = max HP 30%
BARRIER_PER_APPLICATION_CAP = max HP 20%
BARRIER_DEFAULT_DURATION = 3000ms
REDIRECTION_DEFAULT = 30% / one recipient
HEALTH_FLOOR_DEFAULT = 1 HP / one trigger
ADD_STACKS_DEFAULT_CAP = 3
DOT_HOT_PULSE = 1000ms
CONTROL_DURATION_MAX = 2000ms
SAME_CONTROL_GROUP_LOCKOUT = 1000ms
```

밀리초→tick 변환은 다음 Gate가 소유한다.

## 8. Event·Metric 라우팅

```text
RAW_DAMAGE
→ ADJUSTED_DAMAGE
→ EFFECTIVE_DEFENSE
→ POST_MITIGATION_DAMAGE
→ BARRIER_ABSORBED
→ CANDIDATE_HP_LOSS
→ REDIRECTED_HP_LOSS
→ HEALTH_FLOOR_PREVENTED
→ FINAL_HP_LOSS
```

Restore·Status 결과는 별도 event·metric이다. 모든 단계는 root effect와 가능한 경우 deployment provenance를 유지한다.

## 9. 조기 Stop-Ship Guard

```text
FRONTLINE_MEAN_BARRIER_UPTIME > 40%
OR
BARRIER_ABSORBED / POST_MITIGATION_INCOMING_DAMAGE > 35%
```

최종 밸런스 합격선이 아니라 조기 중단 후보 분류다.

## 10. 검증 Tier

```text
T0 = fixture/schema/default field validation
T1 = replay determinism and intermediate integer parity
T2 = phase·damage·Barrier·transfer·Floor·Status invariants
T3 = paired A/B/C metrics including all three lanes
T4 = aggregate balance after acceptance approval
T5 = product runtime adapter after separate authorization
```

## 11. 적대적 감사 계보

```text
OMW-AUD-208 ~ 220 = Harness
OMW-AUD-221 = Sheet correction / resolved / non-counter
OMW-AUD-222 ~ 232 = Common Combat
OMW-AUD-233 ~ 246 = Damage Semantics
OMW-AUD-247 ~ 260 = Numeric Defaults
```

## 12. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MITIGATION_AND_PROTECTION_NUMERIC_DEFAULTS_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
FIXED_TICK_RATE = PENDING
MS_TO_TICK_CONVERSION = PENDING
SOURCE_TARGET_MODIFIER_STACKING = PENDING
EXACT_UNIT_HERO_BUILDING_VALUES = PENDING
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 13. 운영 Gate

```text
CURRENT_COUNT = 4/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
NEXT_PREFLIGHT = AT_10_OF_10
CURRENT_PLANNING_PR = RESOLVE_FROM_OPEN_PR
```
