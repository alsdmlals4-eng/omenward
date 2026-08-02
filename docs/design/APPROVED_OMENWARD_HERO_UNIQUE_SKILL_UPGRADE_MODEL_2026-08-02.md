# OMENWARD 해금 영웅 고유 2스킬·제한형 상위호환 승인안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
approved_at: 2026-08-02 22:29 KST
refined_at: 2026-08-02 23:07 KST
approval: USER_DIRECT_REFINEMENT
status: USER_APPROVED / REFINED_BY_GRADE_SLOT_AND_SKILL_REPLACEMENT / NOT_IMPLEMENTED
current_authority: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
product_code_authority: NONE
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 현행 결정

해금 이름 지정 영웅은 표준 `[영웅]` 등급보다 강하고 표준 `[전설]` 등급보다 약한 제한형 상위호환이다.

```text
표준 [영웅]
= 강화된 1스킬 + 표준 2스킬

해금 이름 지정 [영웅]
= 강화된 1스킬 + 고유 2스킬
```

```text
STANDARD_HERO_POWER < UNLOCKED_NAMED_HERO_POWER < STANDARD_LEGENDARY_POWER
UNIQUE_SKILL_SLOT = 2
STANDARD_SKILL_2 = REPLACED
EXTRA_SKILL_ADDED = FALSE
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
MANDATORY_COMPENSATION_AXIS_COUNT = 0
```

- 과거의 `원본 영웅 키트 + 고유 스킬 추가` 표현은 폐기한다.
- 고유 스킬은 표준 2스킬과 같은 슬롯을 사용한다.
- 강화된 1스킬과 병영 Tier 핵심 패시브는 표준 영웅 등급 계약을 따른다.
- 기본 능력치를 의무적으로 낮추지 않는다.
- 고유 2스킬은 한 번의 발동으로 해당 전선에 식별 가능한 국면 변화를 만들어야 한다.
- 수동 발동·수동 타깃·숨은 패시브는 금지한다.

## 2. 전역 제한의 현행 해석

과거의 `이름 지정 영웅만 전역 1명` 표현은 폐기한다.

```text
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

표준 영웅·해금 영웅·표준 전설·향후 해금 전설을 모두 합쳐 상·중·하 전선 전체에 최대 1명만 활성화한다.

- 제한은 룰렛 보상 획득이 아니라 전장 배치에 적용한다.
- 슬롯 충돌 토큰은 보관·판매할 수 있다.
- 자동 삭제·자동 교체·수동 퇴각·수동 교대는 금지한다.
- 일반·엘리트 등급은 이 슬롯에 포함하지 않는다.

## 3. 자동 발동

```text
COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
→ 병종별 유효 조건·대상 확인
→ deterministic priority·tie-break
→ CAST_COMMIT
→ 효과·VFX/SFX·로그
→ COOLDOWN
```

- 공통 cooldown 프레임을 사용한다.
- 유효 조건이 없으면 준비 상태를 유지하고 cooldown을 낭비하지 않는다.
- 동일 저장 상태와 동일 입력 순서에서는 동일 결과를 낸다.

## 4. 초기 5명

```text
shield_guard / 방패병 → UNIQUE_SKILL_2
archer / 궁병         → UNIQUE_SKILL_2
priest / 사제         → UNIQUE_SKILL_2
mage / 마법사         → UNIQUE_SKILL_2
assassin / 암살자     → UNIQUE_SKILL_2
```

```text
INITIAL_NAMED_HERO_COUNT = 5
INITIAL_UNIQUE_SKILL_SLOT = 2
INITIAL_PASSIVE_COUNT = 0
```

정확 영웅 이름·스킬 효과·발동 조건·cooldown·VFX/SFX·수치는 후속 Decision에서 확정한다.

## 5. 향후 해금 전설

향후 해금 이름 지정 `[전설]`은 표준 전설의 3스킬을 고유 3스킬로 교체한다.

```text
표준 [전설]
= 강화된 1스킬 + 강화된 표준 2스킬 + 표준 3스킬

향후 해금 이름 지정 [전설]
= 강화된 1스킬 + 강화된 표준 2스킬 + 고유 3스킬
```

```text
FUTURE_NAMED_LEGENDARY_UNIQUE_SKILL_SLOT = 3
FUTURE_NAMED_LEGENDARY_IMPLEMENTATION = NOT_NOW
```

해금 전설의 로스터·획득·토큰·수치·자산·표준 전설 대비 파워는 별도 Decision 전까지 확정하지 않는다.

## 6. 적대적 경계

- 고유 2스킬이 표준 전설 전체 키트를 항상 압도하면 실패다.
- 해금 후 표준 영웅이 선택되지 않는 것은 의도된 수직 성장 결과다. 다만 미해금 상태에서도 기본 진행이 가능해야 한다.
- 영웅 이상 등급 슬롯이 차 있어도 새 결과를 소멸시키지 않는다.
- 전설 당첨을 즉시 배치하지 못하는 좌절은 보관·판매·충돌 UI와 경제 가치로 검증한다.
- 다섯 고유 스킬이 다섯 신규 AI·리그·전체 애니메이션으로 확대되면 실패다.
- 미래 해금 전설을 현재 구현 범위에 포함하지 않는다.

## 7. 책임 원본

현행 세부 계약은 다음 문서가 소유한다.

`APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md`

## 8. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
PRODUCT_CODE = UNCHANGED
EXACT_SKILLS = PENDING
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
