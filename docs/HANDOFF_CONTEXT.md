# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: IMPLEMENTATION_STATUS_AND_PENDING_REFRESH
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
current_sync: OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-status-pending-refresh-20260803
current_planning_pr: PENDING_CREATION
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
preflight: MAINTENANCE_SYNC_REQUIRED
```

PR #129는 10/10 fresh Green preflight 뒤 squash merge됐고 PR #130이 post-merge 상태를 동기화했다. 최신 기획은 main 정본이며 제품 코드·데이터·Scene·Resource는 변경되지 않았다.

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

## 2. 최신 영웅 정본

`OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1`

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
shield_guard / 방패병 → 불퇴의 성벽
archer / 궁병         → 천공 소거
priest / 사제         → 생명의 서약
mage / 마법사         → 메테오
assassin / 암살자     → 그림자 분신
```

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

## 4. Trigger·대상 Resolver

```text
READY
→ public trigger
→ same-lane legal filter
→ public priority score
→ stability window
→ stable ID / position tie-break
→ CAST_PRECHECK
→ immutable CAST_COMMIT snapshot
```

숨은 AI·랜덤 tie-break·임의 fallback target·수동 발동·숨은 전투 종료 예측은 금지한다.

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

## 6. 이번 유지보수 Sync

`OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1`

목적:

- `CURRENT_IMPLEMENTATION_STATUS.md`의 2026-07-27 고정 상태를 2026-08-03 main 영웅 정본으로 교정.
- `DECISIONS_PENDING.md`에 영웅 Trigger·timer·효과값·simulation·save 상태를 추가.
- 제품 구현과 main 기획 정본을 계속 분리.
- 다음 제품 Gate를 deterministic simulation harness 설계로 명시.

이 Sync는 제품 Decision 카운터에 포함하지 않는다.

## 7. 구현 전 우선순위

```text
P0 = deterministic simulation harness 범위·재현성·입출력 계약
P1 = 전체 병종 공통 전투 schema와 피해·방어·위협도 기준
P2 = 다섯 해금 영웅 exact Trigger·timer·효과값
P3 = A/B/C 통과선·표본 수·stop-ship 기준
P4 = 100,000시드 룰렛·경제 simulation 계약
P5 = checkpoint·save schema
P6 = 첫 제품 구현 패키지·Red tests·회귀·롤백 계획
```

## 8. 책임 원본

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- `docs/DECISIONS_PENDING.md`
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

## 9. 구현 경계·다음 작업

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MAIN_CANONICAL_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
EXACT_SCHEMA = PENDING
EXACT_THRESHOLDS_AND_VALUES = PENDING
SIMULATION_PLAN = REQUIRED_BEFORE_IMPLEMENTATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

```text
CURRENT_MAINTENANCE_SYNC = OMW-SYNC-20260803-IMPLEMENTATION-STATUS-AND-PENDING-REFRESH-V1
GRILL_ME_COUNT = 0/10
NEXT_GRILL_ME_DECISION = OMW-DEC-20260803-VALIDATION-DETERMINISTIC-SIMULATION-HARNESS-SCOPE-V1
NEXT_PRODUCT_GATE = SEPARATELY_AUTHORIZED_SIMULATION_PLAN
```
