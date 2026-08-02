# OMENWARD 이름 지정 영웅 고유 2스킬 구조 승인안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1
approved_at: 2026-08-02 21:08 KST
refined_at: 2026-08-02 23:07 KST
status: USER_APPROVED / REFINED_TO_UNIQUE_SKILL_2_REPLACEMENT / NOT_IMPLEMENTED
current_authority: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
product_code_authority: NONE
```

## 1. 현행 키트

```text
표준 [영웅]
= 강화된 1스킬 + 표준 2스킬

해금 이름 지정 [영웅]
= 강화된 1스킬 + 고유 2스킬
```

```text
UNIQUE_SKILL_SLOT = 2
STANDARD_SKILL_2 = REPLACED
EXTRA_SKILL_COUNT = 0
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
```

- 고유 2스킬은 추가 스킬이 아니라 표준 2스킬 교체다.
- 이름·초상·스킨·장비·식별 VFX/SFX는 원본 병종 자산을 기반으로 변주한다.
- 원본 역할·기본 공격·사거리·이동·기본 AI·리그·공통 애니메이션을 유지한다.
- 기본 능력치를 의무적으로 낮추지 않는다.
- 패시브·숨은 상시 보너스·수동 스킬은 사용하지 않는다.

## 2. 파워 경계

```text
표준 [영웅] < 해금 이름 지정 [영웅] < 표준 [전설]
```

고유 2스킬은 전선 국면을 바꾸는 임팩트를 가져야 하지만 표준 전설의 강화 2스킬·3스킬·상위 기본 전투 예산 전체를 넘지 않는다.

## 3. 전역 슬롯

```text
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

이름 지정 영웅만이 아니라 표준 영웅·표준 전설·향후 해금 전설도 같은 전역 슬롯을 공유한다.

## 4. 자동 발동

```text
COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
→ 병종별 trigger·대상·priority·tie-break
→ CAST_COMMIT
→ 효과·VFX/SFX·로그
→ COOLDOWN
```

## 5. 제작 범위

재사용:

- 원본 병종 리그·본 구조.
- 이동·기본 공격·피격·사망 애니메이션.
- 기본 투사체·충돌·전선 이동 코드.
- 기본 AI와 타기팅 프레임.
- 공통 카드·cooldown·상태 UI.

신규:

- 이름·초상·스킨·장비/실루엣 변주.
- 고유 2스킬 데이터.
- 발동을 식별하는 VFX/SFX.
- 짧은 스킬 설명과 자동 발동 표시.

```text
NEW_FULL_RIG = NOT_REQUIRED_BY_DEFAULT
NEW_FULL_ANIMATION_SET = NOT_REQUIRED_BY_DEFAULT
NEW_AI_ARCHITECTURE = FORBIDDEN_BY_DEFAULT
```

## 6. 향후 해금 전설

```text
향후 해금 이름 지정 [전설]
= 강화된 1스킬 + 강화된 표준 2스킬 + 고유 3스킬
```

```text
FUTURE_NAMED_LEGENDARY_UNIQUE_SKILL_SLOT = 3
FUTURE_NAMED_LEGENDARY_IMPLEMENTATION = NOT_NOW
```

## 7. 금지

- 표준 2스킬과 고유 2스킬 동시 보유.
- 별도 세 번째 스킬 슬롯 추가.
- 영웅 전용 패시브·숨은 상시 보너스.
- 수동 발동·수동 타깃.
- 영웅마다 새 리그·AI·전체 애니메이션 세트 제작.
- 표준 전설 전체 키트를 항상 압도하는 고유 2스킬.
- 해금 전설을 현재 초기 5명 구현 범위에 포함.

## 8. 구현 경계

```text
PRODUCT_CODE = UNCHANGED
EXACT_HERO_IDENTITIES = PENDING
EXACT_UNIQUE_SKILL_2 = PENDING
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
