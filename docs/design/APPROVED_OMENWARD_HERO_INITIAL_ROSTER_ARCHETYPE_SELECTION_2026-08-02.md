# OMENWARD 초기 이름 지정 영웅 병종 선정 승인안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1
approved_at: 2026-08-02 22:10 KST
refined_at: 2026-08-02 22:29 KST
approval: USER_DIRECT_SELECTION_AND_REFINEMENT
status: USER_APPROVED / FIVE_UNIQUE_SKILL_HEROES / NOT_IMPLEMENTED
scope: GAMEPLAY_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION
kit_authority: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
product_code_authority: NONE
exact_hero_identities: PENDING
exact_unique_skills: PENDING
assets: NOT_CREATED
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 확정 병종 5종

```text
shield_guard / 방패병
archer / 궁병
priest / 사제
mage / 마법사
assassin / 암살자
```

각 병종에 이름 지정 영웅 1명을 연결한다. 다섯 영웅은 모두 고유 자동 사용스킬 하나를 가진다.

```text
shield_guard → UNIQUE_AUTOMATIC_ACTIVE_SKILL
archer       → UNIQUE_AUTOMATIC_ACTIVE_SKILL
priest       → UNIQUE_AUTOMATIC_ACTIVE_SKILL
mage         → UNIQUE_AUTOMATIC_ACTIVE_SKILL
assassin     → UNIQUE_AUTOMATIC_ACTIVE_SKILL
```

```text
INITIAL_HERO_COUNT = 5
INITIAL_PASSIVE_COUNT = 0
INITIAL_AUTOMATIC_ACTIVE_SKILL_COUNT = 5
HEROES_PER_ARCHETYPE = 1
```

이전 패시브 3명·자동 사용스킬 2명 배정은 폐기됐다.

## 2. 병종별 검증 역할

| 병종 | 원본 역할·타기팅 | 고유 스킬 설계가 검증할 축 |
|---|---|---|
| 방패병 | 전열·최근접 적·원거리 방어 | 전열 보호·피해 차단·위기 대응 자동 스킬 |
| 궁병 | 지속 원거리·비행 우선·대공 | 비행 또는 우선 표적에 대한 순간 화력 스킬 |
| 사제 | 지원·최저 체력 아군 | 아군 구조·치유·보호 자동 타기팅 스킬 |
| 마법사 | 원거리·적 군집 우선 | 군집 광역·제어·연쇄 효과 자동 스킬 |
| 암살자 | 우회·적 후열 우선 | 후열 침투·처형·탈출 또는 재진입 스킬 |

정확 스킬 효과는 이 문서에서 확정하지 않는다.

## 3. 공통 상위호환 구조

```text
원본 병종 [영웅] 등급 기본 성능 계승
+ 고유 자동 사용스킬 1개
+ 스킬 식별 VFX/SFX
= 해금 이름 지정 영웅
```

- 영웅 전용 패시브는 없다.
- 기본 능력치 강제 하향이나 의무 상쇄 축은 없다.
- 이름 지정 영웅은 해금 보상으로 원본보다 조금 더 강하고 임팩트 있게 느껴져야 한다.
- 전역 활성 이름 지정 영웅 최대 1명 제한은 유지한다.

## 4. 역할 중복 경계

궁병과 마법사는 모두 원거리지만 다음처럼 구분한다.

```text
궁병 = 비행·우선 표적 지속 화력과 정밀 순간 화력
마법사 = 적 군집 판단과 광역·제어 고점
```

사제와 마법사의 자동 타기팅 테스트를 분리한다.

```text
사제 = lowest-health ally
마법사 = enemy cluster
```

암살자 스킬은 기존 `backline` 타기팅을 그대로 반복하지 않고 발동 조건·전투 결과·연출이 분명한 추가 행동을 제공해야 한다.

## 5. 자산 재사용

각 영웅은 원본 병종의 다음 자산을 우선 재사용한다.

- 리그·본 구조.
- 이동·기본 공격·피격·사망 애니메이션.
- 기본 투사체·충돌·이동·타기팅 코드.
- 공통 영웅 카드·cooldown·상태 표시 UI.

신규 제작은 이름·초상·스킨·장비 또는 실루엣 변주·고유 스킬 VFX/SFX에 집중한다.

## 6. 적대적 검토

- 고유 스킬 5개로 범위가 커진다. 공통 스킬 프레임과 데이터·UI·VFX 규격을 공유한다.
- 원거리 후열 병종이 3종이라 약점이 숨겨질 수 있다. 후열 압박·분산·비행·군집 counter encounter를 모두 포함한다.
- 상위호환이 해금 강제로 변하지 않도록 원본 유닛만으로 진행 가능한지 검증한다.
- 전역 활성 1명 제한 아래에서 다섯 영웅 간 선택률이 한 명으로 몰리지 않는지 검증한다.

## 7. 금지

- 패시브형 배정.
- 고유 스킬 없는 영웅.
- 한 영웅에 독립 고유 스킬 두 개 이상.
- 거인·기병 등 다른 병종을 초기 로스터에 자동 추가.
- 다섯 영웅을 완전 신규 유닛으로 제작.
- 수동 스킬·수동 타깃.
- 정확 영웅 이름·스킬·수치·구현을 검증 전에 완료로 표시.

## 8. 다음 결정

```text
NEXT_GATE = OMW-DEC-20260802-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-CONCEPTS-V1
```

후속 결정에서 다섯 병종 각각의 고유 스킬 전술 콘셉트를 확정한다.

## 9. 구현 경계

```text
USER_APPROVED = TRUE
EXACT_ARCHETYPES = [shield_guard, archer, priest, mage, assassin]
INITIAL_PASSIVE_COUNT = 0
INITIAL_AUTOMATIC_ACTIVE_SKILL_COUNT = 5
EXACT_HERO_IDENTITIES = PENDING
EXACT_UNIQUE_SKILLS = PENDING
PRODUCT_IMPLEMENTED = FALSE
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
