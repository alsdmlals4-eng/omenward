# 오멘워드 해금 영웅 고유 2스킬 자동 발동 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
approved_at: 2026-08-02 19:26 KST
refined_at: 2026-08-02 23:07 KST
status: USER_APPROVED / REFINED_BY_GRADE_SLOT_AND_SKILL_REPLACEMENT / NOT_IMPLEMENTED
current_authority: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

초기 해금 이름 지정 영웅은 표준 영웅 등급의 2스킬을 고유 2스킬로 교체하며, 해당 스킬은 공통 cooldown 프레임과 병종별 유효 조건을 사용해 자동 발동한다.

```text
COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
→ trigger·target filter·priority·tie-break 확인
→ 발동 직전 대상·조건 재검증
→ CAST_COMMIT
→ 효과·VFX/SFX·로그
→ COOLDOWN
```

```text
NAMED_HERO_UNIQUE_SKILL_SLOT = 2
MANUAL_ACTIVATION = FALSE
COMMON_COOLDOWN_FRAMEWORK = TRUE
READY_STATE_PERSISTS_WITHOUT_VALID_CONDITION = TRUE
```

## 2. 필수 필드

각 고유 2스킬은 다음을 명시한다.

- 발동 가능한 전투 조건.
- 대상 후보 조건.
- 대상 우선순위.
- 결정론적 동률 처리.
- cooldown 길이와 시작 시점.
- 유효 대상이 없을 때 준비 상태 유지 규칙.
- 발동 직전 재검증.
- 효과와 종료 조건.
- 식별 가능한 VFX/SFX·전투 로그.
- Stage 경계·저장·Retry에서 유지할 상태.

## 3. 플레이어 통제

플레이어는 스킬 버튼·직접 타기팅·수동 보류를 사용하지 않는다. 대신 배치 전에 다음을 확인한다.

- 고유 2스킬 이름과 전장 역할.
- 유효 발동 조건.
- 우선 대상 범주.
- 현재 `COOLDOWN` 또는 `READY` 상태.
- 전장 전체 `[영웅]·[전설]` 활성 슬롯 `0/1` 또는 `1/1`.

자동 발동은 숨은 랜덤이 아니라 예고된 공세와 전선 배치 판단에 사용할 수 있는 공개 규칙이어야 한다.

## 4. 결정론

```text
동일 저장 상태
+ 동일 전투 입력 순서
= 동일 준비 전환·대상·발동 결과
```

- 마지막 tie-break는 stable ID 또는 저장되는 결정론적 순서를 사용한다.
- 저장·Retry로 대상·발동 시점·cooldown을 재굴림할 수 없다.
- 준비 상태·남은 cooldown·발동 커밋·선택 대상에 영향을 주는 상태를 저장한다.

## 5. 전장 임팩트와 등급 상한

- 고유 2스킬은 한 번의 발동으로 배치 전선의 국면에 명확한 변화를 만들어야 한다.
- 임팩트는 피해 숫자만이 아니라 전열 유지, 위협 제거, 회복, 군집 붕괴, 후열 차단 등 병종 역할에 맞춰 설계한다.
- 표준 `[영웅]`보다 강해야 하지만 표준 `[전설]`의 강화 2스킬+3스킬을 합친 전체 키트보다 약해야 한다.
- 여러 독립 효과를 묶어 사실상 궁극기 세트로 만들지 않는다.

## 6. 향후 해금 전설

향후 해금 이름 지정 `[전설]`은 같은 자동 발동 원칙을 사용하되 고유 스킬 슬롯은 3이다.

```text
FUTURE_NAMED_LEGENDARY_UNIQUE_SKILL_SLOT = 3
FUTURE_NAMED_LEGENDARY_IMPLEMENTATION = NOT_NOW
```

현재 문서는 해금 전설의 정확 trigger·cooldown·효과를 승인하지 않는다.

## 7. 금지

- 표준 2스킬과 고유 2스킬 동시 보유.
- 수동 스킬·수동 타깃·수동 보류.
- cooldown 완료 즉시 유효하지 않은 대상에게 낭비 발동.
- 숨은 무작위 대상 선택.
- 저장·Retry 재굴림.
- 고유 2스킬 내부에 독립 능력 여러 개 숨김.
- 영웅별 신규 AI 아키텍처·전체 신규 리그 요구.
- 해금 전설을 현재 구현 범위에 포함.

## 8. 구현 경계

```text
PRODUCT_CODE = UNCHANGED
EXACT_SKILLS = PENDING
EXACT_COOLDOWNS = PENDING
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
