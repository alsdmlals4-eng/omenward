# Active Context

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_APPROVED
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-VALIDATION-MITIGATION-FORMULA-AND-PROTECTION-NUMERIC-DEFAULTS-V1
parent_semantics_decision: OMW-DEC-20260803-VALIDATION-DAMAGE-PROTECTION-AND-STATUS-SEMANTICS-V1
parent_combat_decision: OMW-DEC-20260803-VALIDATION-COMMON-COMBAT-SCHEMA-AND-RESOLUTION-ORDER-V1
parent_harness_decision: OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
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
current_grill_me_count: 4
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: OUT_OF_SCOPE_REQUIRES_SEPARATE_CONTRACT
preflight: NEXT_AT_10_OF_10
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

`current_main`, `context_baseline_commit`, `current_planning_pr`은 실행 시점에 저장소에서 해석한다. 최신 Decision은 방어 공식과 보호·상태 초기 수치의 기획 계약만 승인하며 제품 코드·Simulation tool·fixture·test·이미지·animation·HX 제작 권한을 부여하지 않는다.

## 1. 제품 정체성·핵심 재미

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
예고된 세 전선 공세 읽기
→ 제한된 건물·TokenSource로 세 원형 릴 설계
→ SpinSnapshot 결과를 보관·판매·획득
→ 어느 전선에 비가역 배치할지 판단
→ 자동전투·점령·건물 운영으로 전황 변화
→ provenance와 event로 결과 원인 복기
→ 다음 Stage 설계에 환류
```

검증 Harness·전투 Schema·피해 공식은 이 핵심 루프를 대체하지 않는다. 플레이어가 설계한 룰렛과 비가역 전선 커밋이 결과를 만들었는지 증명하는 제작 기반이다.

## 2. 승인된 검증 계층

### P0 — Deterministic Harness Scope

책임 원본:

`design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md`

```text
versioned fixture
+ explicit fixed integer tick
+ named RNG streams
+ stable object IDs
+ ordered external commands
+ pure domain transition
→ ordered event log
→ normalized final state
→ metrics
→ deterministic fingerprint
```

### P1 — Core-First Common Combat Schema

책임 원본:

`design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md`

```text
CombatRunState
LaneState[TOP,MID,BOTTOM]
CombatantState / BuildingState / ObjectiveState
DeploymentProvenance
OrderedCommand
ActionIntent / EffectIntent
StatusInstance / PendingCommit / ActiveEffect
R00~R130 phase resolver
```

모든 적격 actor는 같은 post-movement snapshot에서 commit하며 damage/effect batch 뒤 death를 확정한다.

### P2 — Damage·Protection·Status Semantics

책임 원본:

`design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md`

```text
KINETIC → ARMOR
ARCANE  → RESISTANCE
```

- channel·delivery tag·target profile을 분리한다.
- Barrier·Restore·Health Floor·HP-loss redirection·Status 의미를 분리한다.
- true damage·execute·revive는 현 Slice에서 금지한다.
- 일반 Status는 이미 commit된 같은 tick 행동을 소급 취소하지 않는다.

### P3 — Mitigation·Protection Numeric Defaults

책임 원본:

`design/APPROVED_OMENWARD_MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_2026-08-03.md`

```text
effective_defense = clamp(base + buffs - debuffs, 0, 300)
post_mitigation = max(1, round_half_up(adjusted_damage * 100 / (100 + effective_defense)))
```

```text
TOTAL_BARRIER_CAP = max HP 30%
PER_APPLICATION_CAP = max HP 20%
DEFAULT_BARRIER_DURATION = 3000ms
DEFAULT_REDIRECTION = 30% / recipient 1
DEFAULT_HEALTH_FLOOR = 1 HP / instance 1회
DEFAULT_ADD_STACKS_CAP = 3
DOT_HOT_PULSE = 1000ms
MAX_CONTROL_DURATION = 2000ms
SAME_CONTROL_GROUP_LOCKOUT = 1000ms
```

## 3. 동일 Tick·R80 핵심 불변식

```text
ALL_ELIGIBLE_ACTORS_COMMIT_FROM_SAME_PHASE_SNAPSHOT
SEQUENTIAL_ENTITY_ID_KILL_ADVANTAGE = FORBIDDEN
FALLBACK_RETARGET_AFTER_COMMIT = FORBIDDEN
DEATH_FINALIZATION_BEFORE_DAMAGE_BATCH_END = FORBIDDEN
OBJECTIVE_USES_POST_DEATH_SURVIVORS = REQUIRED
```

```text
R80A VALIDITY_AND_ELIGIBILITY
R80B PROTECTION_SETUP
R80C DAMAGE_MITIGATION_AND_BARRIER
R80D HP_LOSS_REDIRECTION_AND_FLOOR
R80E HP_DELTA_AND_RESTORE
R80F STATUS_APPLICATION_AND_POST_HIT_QUEUE
R80G DEATH_OR_DESTRUCTION_MARK
```

## 4. 수치 경계

```text
NEGATIVE_DEFENSE = FORBIDDEN
DEFENSE_MAX = 300
MAX_REDUCTION_FROM_DEFENSE = 75_PERCENT
MINIMUM_VALID_DAMAGE = 1
DEFENSE_PENETRATION = FORBIDDEN_UNTIL_SEPARATE_DECISION
BARRIER_EXCESS = DISCARDED
TRANSFER_DEPTH_MAX = 1
SECOND_MITIGATION_PASS = FORBIDDEN
MULTIPLE_ACTIVE_CORE_HEALTH_FLOORS = FORBIDDEN
```

밀리초 기본값은 승인됐지만 fixed tick과 변환 규칙이 아직 미확정이므로 runtime 구현에 임의 tick 값을 넣지 않는다.

## 5. 조기 Stop-Ship Guard

대표 중립 Fixture에서 다음 중 하나면 Barrier overcentralization 후보로 분류한다.

```text
FRONTLINE_MEAN_BARRIER_UPTIME > 40_PERCENT
OR
BARRIER_ABSORBED / POST_MITIGATION_INCOMING_DAMAGE > 35_PERCENT
```

이는 최종 밸런스 합격선이 아니라 조기 중단 guard다.

## 6. 영웅·전설 경계

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

초기 5명은 공통 Combatant·Intent·Protection·Status·Timer·Event 계약을 소비한다. 영웅별 별도 피해 공식·AI loop·tick clock·death resolver·save identity를 만들지 않는다.

## 7. 적대적 감사 계보

```text
OMW-AUD-208 ~ OMW-AUD-220 = Harness scope
OMW-AUD-221 = Sheet stale PR-head correction / RESOLVED / NON_COUNTER
OMW-AUD-222 ~ OMW-AUD-232 = common combat schema·resolution
OMW-AUD-233 ~ OMW-AUD-246 = damage·protection·status semantics
OMW-AUD-247 ~ OMW-AUD-260 = mitigation·protection numeric defaults
```

## 8. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MITIGATION_AND_PROTECTION_NUMERIC_DEFAULTS_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
FIXED_TICK_RATE = PENDING
MS_TO_TICK_CONVERSION = PENDING
SOURCE_TARGET_MODIFIER_STACKING = PENDING
EXACT_UNIT_HERO_BUILDING_VALUES = PENDING
EXACT_SAMPLE_SIZE_AND_TOLERANCE = PENDING
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. 다음 Gate

```text
GRILL_ME_COUNT = 4/10
NEXT_DECISION = OMW-DEC-20260803-VALIDATION-FIXED-TICK-TIME-AND-ACTIVATION-DEFAULTS-V1
NEXT_PREFLIGHT = AT_10_OF_10
```
