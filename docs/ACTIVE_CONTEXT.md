# Active Context

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: HERO_UNIQUE_SKILL_2_TIMER_STAGE_POLICY_APPROVED
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_branch: main
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
active_base_version: 9.4.3
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / ACTIVE_BRANCH_SYNCED / NOT_IMPLEMENTED
product_code_authority: NONE
codex_execution: BLOCKED
last_merged_planning_pr: 127
current_planning_pr: 129
current_grill_me_count: 9
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: OUT_OF_SCOPE_REQUIRES_SEPARATE_CONTRACT
preflight: NEXT_AT_10_OF_10
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

`current_main`과 `context_baseline_commit`은 저장소 기본 브랜치에서 실행 시점에 해석한다. 승인 기획은 Draft PR #129에 누적하며 제품 구현 권한은 없다.

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

영웅·전설은 이름 지정 여부와 관계없이 상·중·하 전선 전체에서 슬롯 1개를 공유한다. 제한은 획득이 아니라 배치에 적용하며 충돌 토큰은 보관·판매한다.

## 3. 초기 5명 고유 2스킬

```text
shield_guard / 방패병 → 불퇴의 성벽
archer / 궁병         → 천공 소거
priest / 사제         → 생명의 서약
mage / 마법사         → 메테오
assassin / 암살자     → 그림자 분신
```

- 불퇴의 성벽: 새 지형 없이 짧은 전열 유지와 피해 흡수.
- 천공 소거: 같은 전선 유효 비행 표적 동시 일제사격.
- 생명의 서약: 회복 없는 짧은 체력 하한 보호.
- 메테오: deterministic 적 밀집 지점에 예고 후 단발 지연 낙하.
- 그림자 분신: 독립 AI 없이 원본 표적과 기본 공격 일부를 복제하는 owner-bound proxy 1체.

## 4. 공통 cooldown·실패 정책

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
```

- 유효 조건이 없으면 READY를 보존한다.
- commit 전 무효화는 READY 복귀·cooldown 0이다.
- 천공 소거·메테오는 commit 후 단발 해결형이다.
- 방벽·서약·분신은 owner-bound 지속형이다.
- cooldown은 사건 해결 또는 지속효과 종료 뒤 시작한다.

## 5. timer 지속·Stage 경계 현행 정본

```text
ACTIVE_COMBAT
→ warmup·cooldown 진행

MAINTENANCE / PREPARATION / ROULETTE / BUILD
→ timer 일시정지
→ READY 유지

NEXT_STAGE_ACTIVE_COMBAT
→ 동일 생존 인스턴스의 남은 상태 재개
```

- Stage·Act 전환은 warmup·cooldown 초기화 지점이 아니다.
- READY와 남은 timer는 동일 영웅 인스턴스에 유지한다.
- 방벽·서약·분신은 전투 종료 시 정리하고 full cooldown으로 들어간다.
- 전투 종료 시 미해결 천공 소거·메테오 commit은 취소하지만 사용은 소비하며 full cooldown으로 들어간다.
- 전투 timer는 정비시간 동안 감소하지 않는다.
- 사망·완전 제거 시 timer·READY·commit·active 상태를 삭제하고 전역 고등급 슬롯을 해제한다.
- save/load·Retry는 상태, 잔여시간, target snapshot, commit payload를 그대로 복원하며 재굴림·중복 해결을 금지한다.

책임 원본: `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TIMER_PERSISTENCE_AND_STAGE_BOUNDARY_POLICY_2026-08-03.md`.

## 6. 벤치마크·현업 비교 정책

모든 Grill Me 질문과 승인 작업은 `process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md`를 적용한다.

```text
project canon
→ official/commercial benchmark 2~4
→ OMENWARD 차이
→ production cost·dependencies
→ adversarial review
→ options·recommendation
```

직접 비교 사례가 없으면 `DIRECT_COMPARABLE_NOT_FOUND`를 기록한다.

## 7. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
UNIQUE_SKILL_2_CONCEPTS = APPROVED
COMMON_TIMER_POLICY = APPROVED
TIMER_STAGE_BOUNDARY_POLICY = APPROVED
EXACT_WARMUP_SECONDS = PENDING
EXACT_PER_SKILL_COOLDOWN_SECONDS = PENDING
EXACT_TRIGGER_THRESHOLDS = PENDING
EXACT_DURATIONS_AND_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 다음 Gate

```text
OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
```

10번째 승인 후 latest main·exact-head CI·Sheet read-back·blocker·review·product-path preflight를 새로 실행한다.
