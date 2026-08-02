# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: HERO_TRIGGER_TARGET_POWER_MAIN_CANONICAL
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: NONE
current_planning_pr: NONE
last_merged_planning_pr: 129
last_merged_planning_commit: 173a408eb7b89992a81165438d97946167db0e14
base: 9.4.3_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: MAIN_CANONICAL_NOT_IMPLEMENTED
product_code_authority: NONE
codex: BLOCKED
current_grill_me_count: 0
future_merge_cadence: 10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
```

PR #129는 10/10 fresh Green preflight 뒤 squash merge됐다. 최신 기획은 main 정본이며 제품 코드·데이터·Scene·Resource는 변경되지 않았다.

## 1. 최신 정본 Decision

`OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1`

```text
READY
→ 공개 Trigger
→ 같은 전선 합법 후보 Filter
→ 공개 Priority Score
→ stability window
→ stable ID / position tie-break
→ CAST_PRECHECK
→ immutable CAST_COMMIT snapshot
```

숨은 AI·랜덤 tie-break·임의 fallback target·수동 발동·숨은 전투 종료 예측은 금지한다.

## 2. 초기 5명 Trigger·대상

```text
방패병 → 전열 압력·보호 가치 / owner 전열 anchor
궁병   → 비행 수·가중 위협도 / commit 시 합법 비행 Snapshot
사제   → 체력 기준 이하 생존 아군 / 회복 없는 체력 하한 qualifying set
마법사 → 적 군집 / 적중 수→위협도→stable 위치
암살자 → 합법 후열 고가치 표적 / 역할→후열 깊이→위협도→stable ID
```

- 분신은 독립 target selection·pathfinding·skill casting을 하지 않는다.
- 메테오는 commit 지점 고정 후 회피 가능하다.
- 사제는 회복·부활이 아니다.
- 궁병은 지상·건물·다른 전선을 공격하지 않는다.
- 방벽은 지형·navmesh를 만들지 않는다.

## 3. 공통 상태·Stage 정책

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
MAX_STORED_READY_COUNT = 1
CHARGE_ACCUMULATION = FALSE
MANA_OR_ENERGY_RESOURCE = FALSE
COOLDOWN_DURING_ACTIVE_EFFECT = FALSE
ACTIVE_COMBAT = TIMER_PROGRESS
MAINTENANCE / PREPARATION / ROULETTE / BUILD = TIMER_PAUSED
READY_AND_REMAINING_TIME = CARRY_ON_SAME_LIVING_INSTANCE
ACTIVE_EFFECT_STAGE_CARRY = FORBIDDEN
UNRESOLVED_COMMIT_STAGE_CARRY = FORBIDDEN
```

- precheck 실패는 READY 복귀·cooldown 0.
- owner-bound effect는 전투 종료 시 정리 후 full cooldown.
- 미해결 천공 소거·메테오는 취소·사용 소비·full cooldown.
- save/load·Retry 재굴림·READY 복제·payload 이중 해결 금지.

## 4. 등급·전역 슬롯

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

미래 해금 전설의 고유 3스킬 상세와 구현은 현재 범위가 아니다.

## 5. 파워 검증 Matrix

```text
A = 표준 [영웅]
B = 같은 source archetype 해금 이름 지정 [영웅]
C = 같은 계열 표준 [전설]
```

고정 조건:

```text
same source Tier and passive stage
same seed and Stage
same enemy composition and buildings
same other-two-lane state
same ordered input where possible
```

대표 family:

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

- B는 의도된 family에서 A보다 명확히 강해야 한다.
- C는 전체 대표 family 합산 가치에서 B보다 강해야 한다.
- 한 B가 모든 family 자동 최선이면 실패다.
- 고등급 한 명이 다른 두 전선의 건물·일반·엘리트 운영을 무의미하게 만들면 실패다.

## 6. 측정 지표

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
A/B/C selection value
other-two-lane contribution
```

정확 tolerance·sample size·threshold·값은 simulation 계획에서 고정한다.

## 7. 벤치마크·현업 비교

- Riot `Clarity in League`: 이해·대응 가능성, 시청각 위계, 노이즈 관리.
- TFT `Neon Nights Gameplay Overview`: largest group·lowest health ally 같은 설명 가능한 자동 대상 규칙.
- Riot balance framework: 일관된 측정과 특정 선택의 과도한 필수화 감시.

향후 모든 Grill Me는 `process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md`를 따른다. 외부 자료는 exact OMENWARD 값 권위가 아니다.

## 8. 주요 적대적 위험

```text
hidden AI / trigger flicker / unstable tie-break
barrier permanent uptime / flying encounter deletion
Priest heal or invulnerability drift / undodgeable Meteor
autonomous clone scope expansion
unlocked Hero exceeds Legendary
one Hero best in all encounters
late commit value loss
other two lanes become non-decisive
```

## 9. 책임 원본

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`
- `docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` — `PILOT_RECOMMENDATION / NOT_CANON`
- `docs/design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_COOLDOWN_CHARGE_AND_FAILURE_POLICY_2026-08-03.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TIMER_PERSISTENCE_AND_STAGE_BOUNDARY_POLICY_2026-08-03.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TRIGGER_TARGET_AND_POWER_BUDGET_VALIDATION_2026-08-03.md`
- `docs/process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md`

## 10. 구현 경계·다음 작업

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MAIN_CANONICAL_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
PUBLIC_TRIGGER_TARGET_RESOLVER = APPROVED_CONCEPT
POWER_VALIDATION_MATRIX = APPROVED_CONCEPT
EXACT_SCHEMA = PENDING
EXACT_THRESHOLDS_AND_VALUES = PENDING
SIMULATION_PLAN = REQUIRED_BEFORE_IMPLEMENTATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

```text
GRILL_ME_COUNT = 0/10
CURRENT_PLANNING_PR = NONE
NEXT_PREFLIGHT = AFTER_10_MORE_APPROVED_DECISIONS
NEXT_PRODUCT_GATE = USER_PRIORITY_OR_SEPARATELY_AUTHORIZED_SIMULATION_PLAN
```
