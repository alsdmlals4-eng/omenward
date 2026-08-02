# OMENWARD 해금 영웅 고유 2스킬 timer 지속·Stage 경계 정책 승인안

```yaml
decision_id: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1
approved_at: 2026-08-03 08:12 KST
approval: USER_APPROVED_RECOMMENDATION
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
scope: UNIQUE_SKILL_2_TIMER_PERSISTENCE_AND_STAGE_BOUNDARY
parent_decision: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1
benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
product_code_authority: NONE
exact_seconds: PENDING
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

고유 2스킬의 `INITIAL_WARMUP`과 `COOLDOWN`은 **실제 전투 simulation clock에서만 진행**한다.

```text
ACTIVE_COMBAT
→ INITIAL_WARMUP·COOLDOWN 감소

MAINTENANCE / PREPARATION / ROULETTE / BUILD
→ timer 일시정지
→ READY 상태 유지

NEXT_STAGE_ACTIVE_COMBAT
→ 동일 생존 영웅 인스턴스의 남은 상태 재개
```

정비시간을 오래 유지해 cooldown을 무료 회복하거나, Stage 전환으로 warmup·cooldown을 초기화하는 행위는 허용하지 않는다.

## 2. 상태별 Stage 경계 규칙

| 전투 종료 순간 상태 | 다음 Stage 시작 상태 | 규칙 |
|---|---|---|
| `INITIAL_WARMUP` | 같은 상태와 잔여시간 | 정비시간 동안 감소하지 않음 |
| `READY_WAITING_FOR_VALID_CONDITION` | READY 유지 | READY 사용권은 1회만 유지 |
| `CAST_PRECHECK` | READY 복귀 | commit 전이므로 사용권·cooldown 소비 없음 |
| `CAST_COMMIT` 단발 해결 대기 | `COOLDOWN` | 예약 사건 취소, 사용은 소비됨 |
| `ACTIVE_EFFECT` owner-bound | `COOLDOWN` | 전투 종료와 함께 효과 정리 후 cooldown 진입 |
| `COOLDOWN` | 같은 상태와 잔여시간 | 정비시간 동안 감소하지 않음 |

## 3. 전투 종료 시 commit·active 처리

### 3.1 commit 전

```text
CAST_PRECHECK
+ combat end
→ READY_WAITING_FOR_VALID_CONDITION
→ cooldown consumption = 0
```

### 3.2 commit 후 미해결 단발 사건

`천공 소거` 또는 `메테오`가 `CAST_COMMIT`됐지만 전투 종료 시점까지 해결되지 않았다면:

```text
pending committed event
→ cancel unresolved event
→ consume READY use
→ enter full cooldown
→ write cancellation reason to combat log
```

- 다음 Stage의 새 적에게 target snapshot을 재지정하지 않는다.
- 메테오의 좌표·낙하 예약을 다음 Stage로 옮기지 않는다.
- 취소된 사건을 save/load로 복구하거나 두 번 해결하지 않는다.

### 3.3 owner-bound 지속효과

`불퇴의 성벽`, `생명의 서약`, `그림자 분신`은 전투 종료 시 정리한다.

```text
combat end
→ terminate owner-bound active effect
→ discard remaining duration or budget
→ enter full cooldown
```

- 방벽 흡수 예산, 체력 하한, 분신 지속시간을 다음 Stage로 이월하지 않는다.
- 전투가 끝났는데 효과를 유지해 정비시간·다음 Wave에 무료 가치를 주지 않는다.

## 4. Stage·Act·정비시간

- 살아 있는 동일 영웅 인스턴스는 Stage와 Act를 넘어 유지된다.
- 영웅 인스턴스가 유지되는 한 READY·warmup·cooldown도 유지된다.
- `MAINTENANCE`, 공세 예고, 건설, 룰렛 조작, 보관·판매 UI에서는 전투 timer를 감소시키지 않는다.
- Act 전환도 자동 초기화 지점이 아니다.
- MapRun 종료는 해당 Run의 전투 상태를 종료한다. 다음 Run 초기 상태는 별도 Run 시작 계약이 소유한다.

## 5. 사망·완전 제거

```text
hero death or complete removal
→ clear warmup
→ clear READY
→ clear cooldown
→ cancel precheck
→ cancel unresolved commit payload unless already independently resolved
→ terminate owner-bound effects
→ release global high-grade battlefield slot
```

사망한 인스턴스의 timer 상태를 다른 영웅 토큰이나 재출전 인스턴스에 상속하지 않는다.

## 6. 저장·불러오기·Retry

저장 대상:

```text
hero_instance_id
skill_state
warmup_remaining
cooldown_remaining
ready_stored_count
precheck_target_ids
commit_payload
committed_position
remaining_resolution_delay
active_effect_remaining
active_budget
owner_link
stage_phase
battle_clock_state
```

불변식:

```text
same saved state + same ordered inputs
= same resumed timer + same state transitions + same resolution
```

- 전투 중 저장은 잔여시간과 commit payload를 그대로 복원한다.
- 정비시간 저장은 timer가 정지된 상태로 복원한다.
- Retry가 timer를 초기화하거나 READY를 복제하거나 target을 재굴림하면 실패다.
- 이미 해결된 commit payload가 load 후 다시 해결되면 실패다.

## 7. UX 계약

플레이어는 다음을 구분할 수 있어야 한다.

- `INITIAL_WARMUP`: 첫 사용 준비 중.
- `READY`: 사용 가능하지만 유효 조건 대기 중일 수 있음.
- `CAST_COMMIT`: 취소 불가능한 사건 예약.
- `ACTIVE_EFFECT`: 지속효과 진행 중.
- `COOLDOWN`: 다음 사용까지 남은 전투시간.
- `PAUSED_BY_NON_COMBAT_PHASE`: 정비시간이라 timer가 멈춰 있음.

전투 timer를 초 단위로 표시할 경우 정비시간에는 감소하지 않는다는 상태 문구를 함께 제공한다.

## 8. 벤치마크·현업 비교

```text
DIRECT_COMPARABLE_NOT_FOUND
```

완전히 같은 장기 생존 영웅·다중 Stage·정비시간·자동 고유 스킬 구조의 직접 상용 비교 사례는 확인하지 못했다.

사용한 상위 원칙:

1. Godot stable `Pausing games and process mode`
   - SceneTree pause와 노드 process mode로 실행되는 시스템과 멈추는 시스템을 분리할 수 있다.
   - OMENWARD 적용: 전투 simulation clock과 정비 UI clock을 분리한다.
2. Godot stable `Saving games`
   - 영속 대상과 관련 변수를 명시적으로 직렬화하는 구조를 안내한다.
   - OMENWARD 적용: 상태 enum·잔여 timer·commit payload·owner-bound 상태를 명시적으로 저장한다.

이는 exact 구현이나 수치 권위가 아니라 production boundary다.

## 9. 적대적 검토

### OMW-AUD-182 — 정비시간 무료 cooldown 회복

- 공격: 플레이어가 메뉴를 오래 열어 영웅 스킬을 매 Stage READY로 만들 수 있다.
- 해소: 전투 simulation clock에서만 timer 진행.

### OMW-AUD-183 — Stage 초기화 exploit

- 공격: Stage마다 warmup·cooldown을 초기화하면 유리한 상태를 반복 생성할 수 있다.
- 해소: 동일 인스턴스의 상태와 잔여시간 유지.

### OMW-AUD-184 — 지속효과 다음 Stage 이월

- 공격: 방벽·서약·분신이 다음 전투 시작 보너스로 누적된다.
- 해소: 전투 종료 시 정리하고 cooldown 진입.

### OMW-AUD-185 — 미해결 메테오의 새 Stage 재타깃

- 공격: 이전 전투의 commit을 다음 적에게 적용하면 target 권위와 대응 가능성이 무너진다.
- 해소: unresolved committed event 취소, 사용 소비, full cooldown.

### OMW-AUD-186 — 짧은 전투의 스킬 무가치화

- 공격: warmup이나 cooldown이 긴 영웅은 짧은 Stage에서 스킬을 못 쓸 수 있다.
- 판정: 유효 위험. 정확 시간은 Stage 길이 분포 simulation 후 확정.

### OMW-AUD-187 — 전투 종료 직전 자동 발동 손실

- 공격: 종료 직전 commit되어 효과 없이 cooldown만 받을 수 있다.
- 해소 방향: trigger 안정화·남은 전투 기대시간 조건을 후속 trigger Decision에서 검증. 현재 자동 환불은 승인하지 않음.

### OMW-AUD-188 — save/load 이중 해결

- 공격: commit payload가 저장 전후 두 번 실행될 수 있다.
- 해소: payload unique ID와 resolved flag 직렬화.

### OMW-AUD-189 — Act 전환 숨은 초기화

- 공격: Stage는 유지하지만 Act 전환에서 초기화하면 동일 exploit이 남는다.
- 해소: Act 전환도 carry/pause 계약 적용.

### OMW-AUD-190 — timer 정지 이유 불명확

- 공격: 정비시간에 숫자가 멈추면 버그처럼 보인다.
- 해소: `PAUSED_BY_NON_COMBAT_PHASE` 상태와 설명 제공.

## 10. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
BATTLE_CLOCK_ONLY_TIMER_PROGRESS = APPROVED
MAINTENANCE_TIMER_PAUSE = APPROVED
READY_AND_REMAINING_TIME_CARRY = APPROVED
ACTIVE_EFFECT_STAGE_CARRY = FORBIDDEN
UNRESOLVED_COMMIT_STAGE_CARRY = FORBIDDEN
EXACT_SECONDS = PENDING
EXACT_TRIGGER_THRESHOLDS = PENDING
STAGE_LENGTH_SIMULATION = NOT_RUN
SAVE_LOAD_RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 11. 다음 Gate

```text
OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TRIGGER-TARGET-AND-POWER-BUDGET-VALIDATION-V1
```

다음 Decision은 초기 다섯 스킬의 유효 발동 조건·대상 우선순위·동률 처리·표준 영웅과 전설 사이 파워 예산 검증 방식을 소유한다.
