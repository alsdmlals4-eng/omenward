# OMENWARD 해금 영웅 고유 2스킬 cooldown·charge·실패 정책 승인안

```yaml
decision_id: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1
approved_at: 2026-08-03 07:47 KST
refined_at: 2026-08-03 08:12 KST
approval: USER_APPROVED_RECOMMENDATION
status: USER_APPROVED / REFINED_BY_TIMER_STAGE_BOUNDARY_POLICY / NOT_IMPLEMENTED
current_child_authority: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1
child_document: APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TIMER_PERSISTENCE_AND_STAGE_BOUNDARY_POLICY_2026-08-03.md
benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
product_code_authority: NONE
exact_seconds: PENDING
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 공통 상태 머신

```text
INITIAL_WARMUP
→ READY_WAITING_FOR_VALID_CONDITION
→ CAST_PRECHECK
→ CAST_COMMIT
→ RESOLUTION_OR_ACTIVE_EFFECT
→ COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
```

```text
MAX_STORED_READY_COUNT = 1
MAX_CHARGE_COUNT = 1
CHARGE_ACCUMULATION = FALSE
MANA_OR_ENERGY_RESOURCE = FALSE
STAGE_PER_USE_LIMIT = FALSE
MANUAL_CAST = FALSE
MANUAL_HOLD = FALSE
MANUAL_TARGET = FALSE
COOLDOWN_DURING_ACTIVE_EFFECT = FALSE
```

- 새 전장 배치 뒤 첫 사용 전에 `INITIAL_WARMUP`을 거친다.
- cooldown 완료는 READY 1회를 저장한다.
- 유효 조건이 없으면 READY를 보존하지만 추가 사용권은 비축하지 않는다.
- 다섯 스킬은 같은 상태 머신을 사용하고 정확 cooldown 값만 개별 데이터로 둔다.

## 2. commit 전 실패

```text
CAST_PRECHECK
+ invalid trigger OR invalid target
→ READY_WAITING_FOR_VALID_CONDITION
→ cooldown consumption = 0
```

임의의 대체 표적으로 즉시 redirect하지 않고 다음 deterministic 평가 주기에 다시 검사한다.

## 3. commit 후 처리 유형

### 단발 해결형

- `천공 소거`: commit target snapshot을 한 번 해결한다.
- `메테오`: commit 지점에 한 번 해결한다.

### owner-bound 지속형

- `불퇴의 성벽`.
- `생명의 서약`.
- `그림자 분신`.

시전자 사망·완전 제거 시 owner-bound 효과는 종료한다.

## 4. cooldown 시작점

```text
불퇴의 성벽: 지속시간 또는 흡수 예산 종료 뒤
천공 소거: 일제사격 판정 해결 뒤
생명의 서약: 체력 하한 지속시간 종료 뒤
메테오: 충돌·폭발 해결 뒤
그림자 분신: 지속시간 또는 조기 종료 뒤
```

active effect가 진행되는 동안 cooldown을 동시에 회복하지 않는다.

## 5. timer 지속·Stage 경계 refinement

정확 Stage·정비시간 규칙은 자식 책임 원본이 소유한다.

```text
ACTIVE_COMBAT = warmup·cooldown progress
MAINTENANCE / PREPARATION / ROULETTE / BUILD = timer paused
READY = carry
remaining warmup/cooldown = carry on same living instance
```

```text
owner-bound active at combat end
→ terminate effect
→ full cooldown

unresolved committed single-shot at combat end
→ cancel event
→ consume use
→ full cooldown
```

- Stage·Act 전환은 timer 초기화 지점이 아니다.
- 정비시간 대기로 cooldown을 무료 회복하지 않는다.
- 미해결 commit을 다음 Stage에 이월하거나 새 표적으로 재지정하지 않는다.
- save/load·Retry는 timer와 commit payload를 그대로 복원한다.

현행 책임 원본:

`APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TIMER_PERSISTENCE_AND_STAGE_BOUNDARY_POLICY_2026-08-03.md`

## 6. 결정론·저장

필수 저장 상태:

```text
state enum
warmup_remaining
cooldown_remaining
READY count
target snapshot
commit payload
committed position
remaining resolution delay
active duration or budget
owner link
resolved flag
battle phase
```

```text
same saved state + same ordered inputs
= same state transitions + same target + same resolution
```

save/load·Retry로 timer 초기화, target 재굴림, READY 복제, commit 이중 해결을 허용하지 않는다.

## 7. UX

플레이어가 `INITIAL_WARMUP`, `READY`, 조건대기 이유, `CAST_COMMIT`, active effect, `COOLDOWN`, `PAUSED_BY_NON_COMBAT_PHASE`를 구분할 수 있어야 한다.

READY는 charge가 아니며 최대 1회만 저장된다.

## 8. 적대적 경계

- warmup이 너무 짧거나 길어지는 문제는 simulation·human test 대상.
- active와 cooldown 중첩 금지.
- 유효 조건 없는 자동 소모 금지.
- charge 누적·mana farming 금지.
- commit 전 대상 무효화의 사용권 손실 금지.
- Stage·Act 초기화 exploit 금지.
- 정비시간 무료 cooldown 회복 금지.
- commit payload 이중 해결 금지.

## 9. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
COMMON_TIMER_POLICY = APPROVED
TIMER_STAGE_BOUNDARY_POLICY = APPROVED_BY_CHILD_AUTHORITY
EXACT_WARMUP_SECONDS = PENDING
EXACT_COOLDOWN_SECONDS = PENDING
EXACT_TRIGGER_THRESHOLDS = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 10. 다음 Gate

```text
OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
```
