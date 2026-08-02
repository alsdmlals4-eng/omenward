# 오멘워드 해금 영웅 고유 2스킬 자동 발동 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
approved_at: 2026-08-02 19:26 KST
refined_at: 2026-08-03 07:47 KST
status: USER_APPROVED / REFINED_BY_COOLDOWN_CHARGE_FAILURE_POLICY / NOT_IMPLEMENTED
current_authority: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

초기 해금 이름 지정 영웅은 표준 영웅 등급의 2스킬을 고유 2스킬로 교체하며, 공통 상태 머신과 병종별 유효 조건을 사용해 자동 발동한다.

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
NAMED_HERO_UNIQUE_SKILL_SLOT = 2
MANUAL_ACTIVATION = FALSE
COMMON_STATE_MACHINE = TRUE
MAX_STORED_READY_COUNT = 1
CHARGE_ACCUMULATION = FALSE
MANA_OR_ENERGY_RESOURCE = FALSE
READY_STATE_PERSISTS_WITHOUT_VALID_CONDITION = TRUE
```

상세 책임 원본은 `APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_COOLDOWN_CHARGE_AND_FAILURE_POLICY_2026-08-03.md`다.

## 2. INITIAL_WARMUP

- 새 전장 배치 뒤 첫 사용 전에 초기 준비시간을 거친다.
- save/load·Retry로 warmup을 초기화하거나 단축할 수 없다.
- 정확 warmup 초는 simulation 전까지 고정하지 않는다.
- Stage·정비시간 경계에서 timer를 어떻게 carry할지는 후속 Decision이 소유한다.

## 3. READY와 실패 정책

- cooldown 완료 뒤 READY 1회만 저장한다.
- 유효 조건이 없어도 READY를 유지한다.
- READY 상태에서 추가 사용권을 비축하지 않는다.
- `CAST_COMMIT` 전 trigger·target이 무효화되면 READY로 돌아가고 cooldown을 소비하지 않는다.
- 임의의 대체 대상으로 즉시 재지정하지 않고 다음 deterministic 평가 주기에 재검사한다.

## 4. CAST_COMMIT 이후

단발 해결형:

- `천공 소거`는 commit된 표적 snapshot을 한 번 해결한다.
- `메테오`는 commit된 지점에 예고 후 한 번 낙하한다.
- commit 뒤 시전자 사망만으로 단발 사건을 취소하지 않는다.

시전자 귀속 지속형:

- `불퇴의 성벽`.
- `생명의 서약`.
- `그림자 분신`.

시전자가 사망·완전 제거되면 남은 owner-bound 지속 효과를 종료한다.

## 5. cooldown 시작점

```text
불퇴의 성벽: 지속시간 또는 흡수 예산 종료 후
천공 소거: 일제사격 판정 완료 후
생명의 서약: 체력 하한 지속시간 종료 후
메테오: 낙하·폭발 판정 완료 후
그림자 분신: 분신 지속시간 또는 조기 종료 후
```

```text
COOLDOWN_DURING_ACTIVE_EFFECT = FALSE
```

모든 스킬에 동일한 exact cooldown을 강제하지 않는다. 공통 상태 머신 안에서 스킬별 cooldown 값을 데이터로 둔다.

## 6. 필수 데이터

각 고유 2스킬은 다음을 명시한다.

- 발동 가능한 전투 조건.
- 대상 후보 조건.
- 대상 우선순위.
- 결정론적 동률 처리.
- warmup과 cooldown 길이.
- cooldown 시작 시점.
- 유효 대상이 없을 때 READY 유지 규칙.
- 발동 직전 재검증.
- commit payload.
- 효과와 종료 조건.
- 식별 가능한 VFX/SFX·전투 로그.
- save/load·Retry·Stage 경계에서 유지할 상태.

## 7. 플레이어 통제·UX

플레이어는 스킬 버튼·직접 타기팅·수동 보류를 사용하지 않는다. 대신 다음을 확인한다.

- 고유 2스킬 이름과 전장 역할.
- 유효 발동 조건.
- 현재 `INITIAL_WARMUP | READY | ACTIVE | COOLDOWN` 상태.
- READY지만 조건이 없어 대기 중인 이유.
- commit 예고와 대상·범위.
- 효과 또는 cooldown 남은 시간.
- 전장 전체 `[영웅]·[전설]` 활성 슬롯 `0/1` 또는 `1/1`.

자동 발동은 숨은 랜덤이 아니라 예고된 공세와 전선 배치 판단에 사용할 수 있는 공개 규칙이어야 한다.

## 8. 결정론·저장

```text
동일 저장 상태
+ 동일 전투 입력 순서
= 동일 준비 전환·대상·발동 결과
```

저장 대상:

- state enum.
- warmup·cooldown 남은 시간.
- 선택 대상 stable ID·snapshot.
- commit된 메테오 위치와 남은 낙하시간.
- 지속효과 남은 시간·예산·대상별 하한.
- 분신 owner link.

저장·Retry로 대상·발동 시점·READY 사용권을 재굴림하거나 복제할 수 없다.

## 9. 전장 임팩트와 등급 상한

- 고유 2스킬은 한 번의 발동으로 배치 전선의 국면에 명확한 변화를 만든다.
- 표준 `[영웅]`보다 강하지만 표준 `[전설]`의 전체 키트보다 약해야 한다.
- 여러 독립 효과를 묶어 사실상 궁극기 세트로 만들지 않는다.
- active effect와 cooldown을 동시에 흘려 사실상 상시 유지하지 않는다.

## 10. 향후 해금 전설

```text
FUTURE_NAMED_LEGENDARY_UNIQUE_SKILL_SLOT = 3
FUTURE_NAMED_LEGENDARY_IMPLEMENTATION = NOT_NOW
```

현재 문서는 해금 전설의 정확 trigger·cooldown·효과를 승인하지 않는다.

## 11. 금지

- 표준 2스킬과 고유 2스킬 동시 보유.
- 수동 스킬·수동 타깃·수동 보류.
- mana·energy·rage 등 신규 영웅 전용 자원.
- 다중 charge·READY 누적.
- 유효 조건 없는 자동 소모.
- precommit 무효화 후 cooldown 소비.
- active effect 중 cooldown 진행.
- 숨은 무작위 대상 선택.
- 저장·Retry 재굴림.
- 영웅별 신규 AI 아키텍처·전체 신규 리그 요구.
- 해금 전설을 현재 구현 범위에 포함.

## 12. 구현 경계

```text
PRODUCT_CODE = UNCHANGED
COMMON_STATE_MACHINE = APPROVED
SINGLE_READY_STORAGE = APPROVED
INITIAL_WARMUP = APPROVED
EXACT_WARMUP_SECONDS = PENDING
EXACT_PER_SKILL_COOLDOWNS = PENDING
STAGE_AND_MAINTENANCE_TIMER_POLICY = PENDING
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
