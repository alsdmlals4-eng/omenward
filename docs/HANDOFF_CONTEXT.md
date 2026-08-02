# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-03
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: HERO_UNIQUE_SKILL_2_COOLDOWN_POLICY_APPROVED
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1
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
current_grill_me_count: 8
future_merge_cadence: 10
planning_docs_merge_policy: AUTO_PROCEED_AFTER_GREEN_PREFLIGHT_UNDER_STANDING_USER_AUTHORIZATION
product_code_merge_policy: SEPARATE_CONTRACT_REQUIRED
preflight: NEXT_AT_10_OF_10
```

`current_main`은 저장소 기본 브랜치에서 실행 시점에 해석한다.

## 1. 최신 사용자 결정

Decision ID:

`OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1`

```text
단일 cooldown
+ READY 1회 저장
+ charge 누적 없음
+ 새 배치 후 INITIAL_WARMUP
+ precommit 실패 시 READY 복귀
+ 효과 종료 뒤 cooldown 시작
```

## 2. 공통 상태 머신

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

- 유효 조건이 없으면 READY를 유지한다.
- READY 상태에서 추가 사용권을 비축하지 않는다.
- 스킬별 exact cooldown은 공통 상태 머신 안의 데이터다.
- exact warmup·cooldown 초는 simulation 전까지 고정하지 않는다.

## 3. 실패·commit 정책

### CAST_COMMIT 전

```text
trigger invalid OR target invalid
→ READY 복귀
→ cooldown 소비 0
```

- 임의 대상에게 즉시 재지정하지 않는다.
- 다음 deterministic 평가 주기에 다시 검사한다.

### CAST_COMMIT 후 단발 해결형

- `천공 소거`: commit된 표적 snapshot을 한 번 해결한다.
- `메테오`: commit된 지점에 예고 후 한 번 낙하한다.
- commit 후 시전자 사망만으로 사건을 취소하지 않는다.

### CAST_COMMIT 후 owner-bound 지속형

- `불퇴의 성벽`.
- `생명의 서약`.
- `그림자 분신`.

시전자가 사망·완전 제거되면 남은 지속효과를 종료한다.

## 4. cooldown 시작점

```text
불퇴의 성벽: 지속시간 또는 흡수 예산 종료 후
천공 소거: 일제사격 판정 완료 후
생명의 서약: 체력 하한 지속시간 종료 후
메테오: 낙하·폭발 완료 후
그림자 분신: 분신 지속시간 또는 조기 종료 후
```

active effect와 cooldown을 동시에 흘리지 않는다.

## 5. 저장·UX

저장:

- state enum.
- warmup·cooldown 남은 시간.
- target stable ID·snapshot.
- 메테오 commit 위치·낙하시간.
- 방벽 예산·체력 하한·분신 owner link.

UX:

- INITIAL_WARMUP과 남은 시간.
- READY 여부와 대기 이유.
- CAST_COMMIT 대상·범위.
- active effect·cooldown 남은 시간.

save/load·Retry로 target·READY·timer를 재굴림하거나 복제하지 않는다.

## 6. 초기 5명 고유 2스킬

```text
방패병 → 불퇴의 성벽
궁병   → 천공 소거
사제   → 생명의 서약
마법사 → 메테오
암살자 → 그림자 분신
```

- 사제는 회복이 아니라 유효 체력 하한 보호다.
- 메테오는 지면 경고 후 commit 지점에 단발 낙하한다.
- 분신은 독립 AI 없는 owner-bound 기본 공격 proxy 1체다.

## 7. 기존 등급·전역 슬롯

```text
표준 [영웅] = 강화 1스킬 + 표준 2스킬
해금 이름 지정 [영웅] = 강화 1스킬 + 고유 2스킬
표준 [전설] = 강화 1스킬 + 강화 표준 2스킬 + 표준 3스킬
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

전역 슬롯은 획득이 아니라 배치에 적용하며 슬롯 충돌 토큰은 보관·판매한다.

## 8. 벤치마크·현업 비교 정책

모든 Grill Me에는 공식 상용 사례·OMENWARD 차이·구현/데이터/AI/pathfinding/animation/VFX/UI/save/determinism/QA 비교·적대적 검토·선택지·권장안을 포함한다.

이번 결정은 마나형, 고정 cooldown형, 다중 charge형, Stage당 1회형을 비교해 단일 cooldown+READY 1회를 선택했다. 사례는 exact 수치 권위가 아니다.

## 9. 적대적 검토

- warmup이 너무 짧으면 배치 즉시 폭발, 너무 길면 해금 보상이 죽는다.
- effect 중 cooldown이 흐르면 상시 유지 위험이 생긴다.
- 다중 charge는 전역 고등급 슬롯 한 명의 연속 고점을 과도하게 만든다.
- precommit 실패 시 사용권 소모는 자동전투 신뢰를 해친다.
- save/load·Retry·Stage 전환 timer reset은 exploit이다.
- Stage·정비시간 timer 진행 규칙은 아직 미확정이다.

## 10. 책임 원본

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_COOLDOWN_CHARGE_AND_FAILURE_POLICY_2026-08-03.md`
- `docs/design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md`
- `docs/process/APPROVED_GRILL_ME_BENCHMARK_AND_PRODUCTION_COMPARISON_POLICY_2026-08-03.md`

## 11. 구현 경계·다음 작업

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
COMMON_STATE_MACHINE = APPROVED
SINGLE_READY_STORAGE = APPROVED
INITIAL_WARMUP = APPROVED
EXACT_WARMUP_SECONDS = PENDING
EXACT_PER_SKILL_COOLDOWNS = PENDING
STAGE_AND_MAINTENANCE_TIMER_POLICY = PENDING
EXACT_TRIGGER_THRESHOLDS = PENDING
EXACT_DURATIONS_AND_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

```text
NEXT_GATE = OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1
```
