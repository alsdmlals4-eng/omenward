# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: HERO_UNIQUE_SKILL_2_TIMER_STAGE_POLICY_APPROVED
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
current_benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-hero-kit-planning-20260802
current_planning_pr: 129
last_merged_planning_pr: 127
base: 9.4.3_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED
product_code_authority: NONE
codex: BLOCKED
current_grill_me_count: 9
future_merge_cadence: 10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
```

## 1. 최신 사용자 결정

Decision ID:

`OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1`

```text
전투 중만 warmup·cooldown 진행
정비·준비·룰렛·건설 중 timer pause
READY와 잔여 timer는 동일 생존 인스턴스에 유지
Stage·Act 전환 초기화 없음
active effect와 미해결 commit은 다음 Stage 이월 없음
```

## 2. 현행 자동 스킬 상태 머신

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

- commit 전 조건·대상 무효화는 READY 복귀, cooldown 0.
- 천공 소거·메테오는 단발 해결형.
- 불퇴의 성벽·생명의 서약·그림자 분신은 owner-bound 지속형.

## 3. Stage 경계 처리표

| 종료 순간 상태 | 다음 전투 상태 |
|---|---|
| INITIAL_WARMUP | 잔여시간 그대로 재개 |
| READY | READY 유지 |
| CAST_PRECHECK | READY 복귀, 무소모 |
| 미해결 CAST_COMMIT | 사건 취소, 사용 소비, full cooldown |
| ACTIVE_EFFECT | 효과 종료, full cooldown |
| COOLDOWN | 잔여시간 그대로 재개 |

- 정비시간은 전투 timer를 감소시키지 않는다.
- 메테오 좌표·일제사격 target snapshot을 새 Stage 적에게 재지정하지 않는다.
- 방벽 예산·체력 하한·분신 지속시간을 다음 Stage로 이월하지 않는다.
- 전투 종료 취소 사유를 로그에 남긴다.

## 4. 저장·Retry

저장해야 할 핵심 상태:

```text
hero_instance_id
skill_state
warmup_remaining
cooldown_remaining
ready_stored_count
target_snapshot
commit_payload
committed_position
remaining_resolution_delay
active_remaining
active_budget
owner_link
stage_phase
battle_clock_state
resolved_flag
```

```text
same saved state + same ordered inputs
= same resumed timer + same transitions + same result
```

Retry·load로 timer 초기화, READY 복제, target 재굴림, commit 이중 해결을 허용하지 않는다.

## 5. 초기 5명 고유 2스킬

```text
방패병 → 불퇴의 성벽
궁병   → 천공 소거
사제   → 생명의 서약
마법사 → 메테오
암살자 → 그림자 분신
```

- 사제는 회복이 아닌 체력 하한 보호다.
- 메테오는 예고 후 확정 지점에 단발 낙하한다.
- 분신은 독립 AI가 아닌 owner-bound proxy다.

## 6. 등급·전역 슬롯

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

## 7. 벤치마크·현업 비교

이번 직접 비교는 `DIRECT_COMPARABLE_NOT_FOUND`다. Godot stable의 pause/process mode와 saving games 원칙을 상위 production boundary로 사용했다.

- 전투 simulation clock과 정비 UI clock 분리.
- timer state·잔여시간·commit payload 명시적 직렬화.

향후 모든 Grill Me는 `process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md`를 따른다.

## 8. 적대적 위험

- 정비시간 무료 cooldown 회복.
- Stage·Act 전환 초기화 exploit.
- 방벽·서약·분신 다음 Stage 이월.
- 미해결 메테오·일제사격 새 Stage 재타깃.
- 짧은 Stage에서 warmup 때문에 스킬 미사용.
- 전투 종료 직전 commit되어 효과 없이 소비.
- save/load 이중 해결.
- pause 이유가 보이지 않는 UX.

해소·후속 검증은 `design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TIMER_PERSISTENCE_AND_STAGE_BOUNDARY_POLICY_2026-08-03.md`가 소유한다.

## 9. 책임 원본

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md`
- `docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` — `PILOT_RECOMMENDATION / NOT_CANON`
- `docs/design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md`
- `docs/design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_COOLDOWN_CHARGE_AND_FAILURE_POLICY_2026-08-03.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TIMER_PERSISTENCE_AND_STAGE_BOUNDARY_POLICY_2026-08-03.md`
- `docs/process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md`

## 10. 구현 경계·다음 작업

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
COMMON_TIMER_POLICY = APPROVED
TIMER_STAGE_BOUNDARY_POLICY = APPROVED
EXACT_SECONDS = PENDING
EXACT_TRIGGER_THRESHOLDS = PENDING
EXACT_DURATIONS_AND_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

다음 Decision:

```text
OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
```

10번째 승인 뒤 fresh preflight가 Green이면 문서 PR #129는 standing authorization에 따라 병합한다. 제품 구현은 별도 계약이다.
