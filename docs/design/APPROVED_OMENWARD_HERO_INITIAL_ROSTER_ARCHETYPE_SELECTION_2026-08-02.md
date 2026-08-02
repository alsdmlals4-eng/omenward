# OMENWARD 초기 이름 지정 영웅 병종 선정 승인안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1
approved_at: 2026-08-02 22:10 KST
refined_at: 2026-08-02 23:07 KST
status: USER_APPROVED / REFINED_TO_UNIQUE_SKILL_2 / NOT_IMPLEMENTED
current_authority: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
product_code_authority: NONE
```

## 1. 초기 5개 병종

```text
shield_guard / 방패병
archer / 궁병
priest / 사제
mage / 마법사
assassin / 암살자
```

각 병종에 해금 이름 지정 `[영웅]` 1명씩 배정한다.

```text
INITIAL_NAMED_HERO_COUNT = 5
INITIAL_SOURCE_ARCHETYPE_COUNT = 5
HEROES_PER_SOURCE_ARCHETYPE = 1
INITIAL_ROSTER_IS_FINAL_RELEASE_CAP = FALSE
```

## 2. 스킬 구조

다섯 영웅은 모두 표준 영웅 등급의 2스킬을 고유 2스킬로 교체한다.

```text
shield_guard → UNIQUE_SKILL_2
archer       → UNIQUE_SKILL_2
priest       → UNIQUE_SKILL_2
mage         → UNIQUE_SKILL_2
assassin     → UNIQUE_SKILL_2
```

- 표준 2스킬과 고유 2스킬을 동시에 보유하지 않는다.
- 추가 3번째 스킬 슬롯은 없다.
- 영웅 전용 패시브는 없다.
- 정확 영웅 이름과 고유 2스킬은 후속 Decision에서 확정한다.

## 3. 역할 검증 범위

| 병종 | 원본 역할·타기팅 | 고유 2스킬 검증 목표 |
|---|---|---|
| 방패병 | 전열·최근접 적·원거리 방어 | 전열 붕괴 방지와 전선 유지 |
| 궁병 | 원거리·비행 우선 | 고가치 비행 위협 제거와 대공 고점 |
| 사제 | 지원·최저 체력 아군 | 다수 피해 또는 치명적 위기 복구 |
| 마법사 | 군집 우선·원거리 제어 | 밀집 공세 붕괴와 전선 공간 변화 |
| 암살자 | 후열 우선·우회 | 핵심 후열 제거와 적 지원망 붕괴 |

각 스킬은 전장 임팩트가 커야 하지만 원본 병종 역할에서 벗어나 다른 병종을 완전히 대체하지 않는다.

## 4. 전역 슬롯

```text
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

초기 해금 영웅만 제한되는 것이 아니다. 표준 영웅·표준 전설도 같은 슬롯을 사용하므로 플레이어는 어느 병종과 어느 전선에 고등급 슬롯을 사용할지 판단한다.

## 5. 파워 계층

```text
표준 [영웅] < 초기 해금 이름 지정 [영웅] < 표준 [전설]
```

- 초기 고유 2스킬은 표준 영웅보다 명확한 강화다.
- 표준 전설의 전체 키트보다 약해야 한다.
- 정확 전투 예산은 simulation 전까지 pending이다.

## 6. 자동 발동

다섯 영웅은 공통 cooldown 프레임과 병종별 유효 조건을 사용한다.

```text
COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
→ 유효 조건·대상·priority·tie-break
→ CAST_COMMIT
→ 효과·VFX/SFX·로그
→ COOLDOWN
```

## 7. 제작 경계

- 다섯 완전 신규 유닛 제작 금지.
- 원본 리그·기본 애니메이션·AI·투사체·전선 이동 재사용.
- 영웅별 이름·초상·스킨·실루엣/장비 변주와 고유 2스킬 VFX/SFX에 집중.
- 새 AI 아키텍처·전체 애니메이션 세트는 기본적으로 금지.

## 8. 향후 해금 전설

해금 전설은 초기 5명 범위에 포함하지 않는다.

```text
FUTURE_NAMED_LEGENDARY_UNIQUE_SKILL_SLOT = 3
FUTURE_NAMED_LEGENDARY_IMPLEMENTATION = NOT_NOW
```

## 9. 구현 경계

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
