# OMENWARD 이름 지정 영웅 초기 로스터 범위 승인안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1
approved_at: 2026-08-02 21:45 KST
refined_at: 2026-08-02 22:10 KST
approval: USER_APPROVED_RECOMMENDED_OPTION_THEN_DIRECTLY_REFINED
status: USER_APPROVED / REFINED_BY_ARCHETYPE_SELECTION / NOT_IMPLEMENTED
scope: GAMEPLAY_HERO_INITIAL_VALIDATION_ROSTER
refining_decision: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1
product_code_authority: NONE
assets: NOT_CREATED
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 최신 범위

최초 권장안은 서로 다른 병종 4종·영웅 4명이었으나, 사용자가 후속 직접 선택에서 방패병·궁병·사제·마법사·암살자를 모두 포함하도록 수정했다.

따라서 현행 초기 제작·검증 범위는 다음과 같다.

```text
서로 다른 기존 UnitArchetype 5종
→ 병종마다 이름 지정 영웅 1명
→ 패시브형 3명
→ 자동 사용스킬형 2명
→ 초기 검증 로스터 총 5명
```

```text
INITIAL_NAMED_HERO_COUNT = 5
INITIAL_SOURCE_ARCHETYPE_COUNT = 5
HEROES_PER_SOURCE_ARCHETYPE = 1
PASSIVE_VARIANT_COUNT = 3
AUTOMATIC_ACTIVE_SKILL_VARIANT_COUNT = 2
INITIAL_ROSTER_IS_FINAL_RELEASE_CAP = FALSE
```

수량·유형 분배·정확 병종은 `APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md`가 우선한다.

## 2. 확정 병종

```text
shield_guard
archer
priest
mage
assassin
```

- 동일 병종 복수 영웅은 초기 로스터에서 금지한다.
- 다섯 병종은 전열·대공·지원·군집 제어·후열 침투를 검증한다.
- 초기 5명은 최종 출시 전체 로스터 상한이 아니다.
- 거인·기병·창병·비행병·대검전사는 초기 범위에 포함하지 않으며 이후 확장 후보로 남긴다.

## 3. 유형 분배

```text
PASSIVE = [shield_guard, archer, assassin]
AUTOMATIC_ACTIVE_SKILL = [priest, mage]
```

- 패시브형 3명은 전열 조건·대공/표적 조건·후열/첫 타격 조건을 검증한다.
- 자동 사용스킬형 2명은 부상 아군과 적 군집 타기팅을 검증한다.
- 각 영웅은 패시브와 사용스킬 중 하나만 가진다.
- 구체 효과·상쇄 축·수치는 후속 Decision 전까지 pending이다.

## 4. 공통 제작·밸런스 계약

```text
원본 [영웅] 등급 병종 데이터
+ 스킨·이름·최소 식별 연출
+ 패시브 또는 자동 사용스킬 1개
- 직접 관련된 상쇄 축 1개
= 초기 이름 지정 영웅
```

```text
signature_delta_count == 1
compensation_axis_count == 1
all_other_source_axes_inherited == true
```

- 원본 역할·기본 공격·사거리·이동·AI·리그·기본 애니메이션을 우선 재사용한다.
- 무료 능력 추가·다축 하향·전체 성장 곡선 재설계를 금지한다.
- 원본 병종이 더 나은 대표 상황을 병종마다 하나 이상 유지한다.

## 5. 선정 기준·검증

1. 원본 Profile·attack profile·animation contract가 비교 가능해야 한다.
2. 원본 자산·AI·UI를 스킨형 변주로 재사용할 수 있어야 한다.
3. 타기팅·전술 판단이 서로 구별돼야 한다.
4. 얻는 것 하나와 잃는 것 하나가 읽혀야 한다.
5. 대표 encounter에서 장점·약점이 모두 드러나야 한다.

측정 항목:

- 원본/영웅·병종별·유형별 선택률.
- 조건 충족률·고점·저점·상쇄 체감.
- ally-lowest-health·enemy-cluster 자동 타기팅 결정론.
- 신규 자산량·재사용률·병종별 제작시간.
- 특정 영웅의 전 맵 지배 또는 함정 선택 여부.

## 6. 적대적 경계

- 이전 4명 문구가 남아 현행 5명과 충돌하지 않도록 모든 활성 라우터와 Sheet를 5명으로 갱신한다.
- 궁병과 마법사는 모두 ranged지만 궁병은 지속 대공, 마법사는 군집 광역 자동 스킬로 역할을 구분한다.
- 사제와 마법사의 자동 스킬 타기팅 테스트를 분리한다.
- 암살자 패시브는 기존 backline 규칙을 반복하는 장식 효과가 아니라 실제 선택을 바꿔야 한다.
- 다섯 영웅 모두 완전 신규 유닛으로 제작하지 않는다.

## 7. 구현 경계

```text
USER_APPROVED = TRUE
INITIAL_NAMED_HERO_COUNT = 5
INITIAL_SOURCE_ARCHETYPE_COUNT = 5
EXACT_ARCHETYPES = [shield_guard, archer, priest, mage, assassin]
PASSIVE_VARIANT_COUNT = 3
AUTOMATIC_ACTIVE_SKILL_VARIANT_COUNT = 2
EXACT_HERO_IDENTITIES = PENDING
EXACT_SIGNATURE_EFFECTS = PENDING
EXACT_COMPENSATION_AXES = PENDING
PRODUCT_IMPLEMENTED = FALSE
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
