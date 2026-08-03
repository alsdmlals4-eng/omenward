# Active Context

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: HERO_TRIGGER_TARGET_POWER_MAIN_CANONICAL
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_branch: main
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: NONE
active_base_version: 9.4.3
current_product: LEGACY_PROTOTYPE
latest_planning: MAIN_CANONICAL / NOT_IMPLEMENTED
product_code_authority: NONE
codex_execution: BLOCKED
last_merged_planning_pr: 129
last_merged_planning_commit: 173a408eb7b89992a81165438d97946167db0e14
current_planning_pr: NONE
current_grill_me_count: 0
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: OUT_OF_SCOPE_REQUIRES_SEPARATE_CONTRACT
preflight: NEXT_AT_10_OF_10
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

`current_main`과 `context_baseline_commit`은 저장소 기본 브랜치에서 실행 시점에 해석한다. PR #129는 squash merge됐으며 위 merge commit은 병합 증거다. 최신 기획은 main 정본이지만 제품 구현 권한이나 완료 증거는 아니다.

## 1. 제품 정체성·핵심 재미

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
예고된 세 전선 공세 읽기
→ 제한된 건물·TokenSource로 룰렛 설계
→ 가로·세로 이동과 확정으로 결과 조작
→ 병력 보관·판매·획득
→ 어느 전선에 비가역 배치할지 판단
→ 자동전투·점령·건물 운영으로 전황 역전
→ 다음 Stage 설계에 환류
```

핵심 시스템은 공세 예측, 건물·병영·금고 기반 토큰 구조, SpinSnapshot 룰렛 조작, 보관·판매·비가역 전선 배치, 세 전선 자동전투·점령·거점 운영이다.

보조 시스템은 골드·식량·보관함, 건설·업그레이드·수리·파괴, 병영 Tier 패시브와 룰렛 등급 성장, 20 Stage MapRun·Wave·정비시간·checkpoint, 미션·메타 해금·벨루·UI·아트·오디오다.

전체 시스템 권위는 `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`, 적대적 검토 계보는 `reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`다.

룰렛 통제감 Evidence Pilot은 `benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md`이며 상태는 정확히 `PILOT_RECOMMENDATION / NOT_CANON`이다. Evidence Pilot은 현행 APPROVED 정본을 자동 변경하지 않는다.

## 2. 등급·전역 슬롯

```text
[일반] = 1스킬
[엘리트] = 강화된 1스킬
[영웅] = 강화된 1스킬 + 표준 2스킬
해금 이름 지정 [영웅] = 강화된 1스킬 + 고유 2스킬
[전설] = 강화된 1스킬 + 강화된 표준 2스킬 + 표준 3스킬
향후 해금 이름 지정 [전설] = 강화된 1스킬 + 강화된 표준 2스킬 + 고유 3스킬
```

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

영웅·전설은 이름 지정 여부와 관계없이 상·중·하 전선 전체에서 슬롯 1개를 공유한다. 제한은 획득이 아니라 배치에 적용하며 충돌 토큰은 보관·판매한다. 미래 해금 전설 상세와 구현은 현재 범위가 아니다.

## 3. 초기 5명 고유 2스킬

```text
shield_guard / 방패병 → 불퇴의 성벽
archer / 궁병         → 천공 소거
priest / 사제         → 생명의 서약
mage / 마법사         → 메테오
assassin / 암살자     → 그림자 분신
```

- 방벽은 지형·navmesh를 만들지 않는 전열 피해 흡수 사건이다.
- 천공 소거는 같은 전선 비행 표적 Snapshot을 동시 공격한다.
- 생명의 서약은 회복 없는 짧은 체력 하한 보호다.
- 메테오는 deterministic 적 군집 지점을 예고 후 단발 타격한다.
- 분신은 독립 AI 없이 원본 표적과 기본 공격 일부를 종속 복제하는 proxy 1체다.

## 4. 공통 cooldown·Stage 정책

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

- commit 전 무효화는 READY 복귀·cooldown 0이다.
- Stage·Act 전환은 timer 초기화 지점이 아니다.
- owner-bound effect는 전투 종료 시 정리하고 full cooldown으로 들어간다.
- 미해결 천공 소거·메테오는 취소·사용 소비·full cooldown이다.
- save/load·Retry 재굴림·READY 복제·payload 이중 해결을 금지한다.

## 5. Trigger·대상 Resolver

```text
READY
→ public trigger
→ same-lane legal filter
→ public priority score
→ data-driven stability window
→ stable ID / stable position tie-break
→ CAST_PRECHECK
→ immutable CAST_COMMIT snapshot
```

```text
PUBLIC_TRIGGER_RULE = REQUIRED
PUBLIC_TARGET_PRIORITY = REQUIRED
DETERMINISTIC_TIE_BREAK = REQUIRED
ARBITRARY_FALLBACK_RETARGET = FORBIDDEN
HIDDEN_FUTURE_BATTLE_END_ORACLE = FORBIDDEN
MANUAL_CAST_OR_TARGET = FORBIDDEN
```

- 방패병: 전열 압력과 유효 보호 가치.
- 궁병: 같은 전선 비행 수·가중 위협도와 합법 비행 Snapshot.
- 사제: 체력 기준 이하 생존 아군 집합과 회복 없는 체력 하한.
- 마법사: 적중 수 → 총 위협도 → stable 위치 순으로 메테오 지점 결정.
- 암살자: 역할 → 후열 깊이 → 위협도 → stable ID; 분신 독립 재탐색 금지.

책임 원본: `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TRIGGER_TARGET_AND_POWER_BUDGET_VALIDATION_2026-08-03.md`.

## 6. 파워 위계 검증

```text
A = 표준 [영웅]
B = 같은 source archetype의 해금 이름 지정 [영웅]
C = 같은 계열 표준 [전설]
```

동일 source Tier·seed·Stage·적 구성·건물·다른 두 전선 상태에서 대표 encounter family를 비교한다.

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

- B는 의도된 encounter에서 A보다 명확히 강해야 한다.
- C는 대표 encounter 전체 합산 가치에서 B보다 높아야 한다.
- 한 해금 영웅이 모든 encounter에서 자동 최선이면 실패다.
- 고등급 한 명이 다른 두 전선 운영을 무의미하게 만들면 실패다.
- 정확 tolerance·sample size·값은 simulation 계획에서 고정한다.

## 7. 벤치마크·현업 비교 정책

모든 Grill Me 질문과 승인 작업은 `process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md`를 적용한다.

이번 결정은 Riot의 전투 가독성, TFT의 설명 가능한 자동 대상 규칙, Riot balance framework의 일관된 측정·선택 다양성 원칙을 참고했다. 외부 자료는 exact 값 권위가 아니다.

## 8. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = MAIN_CANONICAL_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
PUBLIC_TRIGGER_TARGET_RESOLVER = APPROVED_CONCEPT
POWER_VALIDATION_MATRIX = APPROVED_CONCEPT
EXACT_SCHEMA = PENDING
EXACT_TRIGGER_THRESHOLDS = PENDING
EXACT_STABILITY_WINDOWS = PENDING
EXACT_WARMUP_AND_COOLDOWN_SECONDS = PENDING
EXACT_DURATIONS_AND_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION_PLAN = REQUIRED_BEFORE_IMPLEMENTATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. 다음 Gate

```text
GRILL_ME_COUNT = 0/10
NEXT_PREFLIGHT = AFTER_10_MORE_APPROVED_GRILL_ME_DECISIONS
NEXT_PRODUCT_GATE = USER_PRIORITY_OR_SIMULATION_PLAN_WITH_SEPARATE_AUTHORIZATION
```
