# OMENWARD 이름 지정 영웅 초기 로스터 범위 승인안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1
approved_at: 2026-08-02 21:45 KST
refined_at: 2026-08-02 22:29 KST
status: USER_APPROVED / REFINED_TO_FIVE_UNIQUE_SKILL_HEROES / NOT_IMPLEMENTED
current_roster_authority: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-ARCHETYPE-SELECTION-V1
current_kit_authority: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
product_code_authority: NONE
assets: NOT_CREATED
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 현행 초기 검증 로스터

```text
서로 다른 기존 UnitArchetype 5종
→ 병종마다 이름 지정 영웅 1명
→ 모든 영웅이 고유 자동 사용스킬 1개 보유
→ 초기 검증 로스터 총 5명
```

```text
INITIAL_NAMED_HERO_COUNT = 5
INITIAL_SOURCE_ARCHETYPE_COUNT = 5
HEROES_PER_SOURCE_ARCHETYPE = 1
INITIAL_PASSIVE_VARIANT_COUNT = 0
INITIAL_AUTOMATIC_ACTIVE_SKILL_COUNT = 5
INITIAL_ROSTER_IS_FINAL_RELEASE_CAP = FALSE
```

이전 4명·2:2 및 5명·패시브 3/자동 스킬 2 분배는 최신 사용자 결정으로 대체됐다.

## 2. 목적

초기 5명은 다음을 검증한다.

- 원본 병종 자산 재사용.
- 이름 지정 영웅의 고유 스킬 해금 보상.
- 공개 trigger·대상 우선순위·tie-break·cooldown 또는 charge.
- 다섯 병종의 서로 다른 자동 타기팅 문법.
- 전역 활성 이름 지정 영웅 최대 1명 제한에서의 영웅 선택.
- 스킬 발동 임팩트와 VFX/SFX 가독성.

5명은 최종 출시 전체 로스터 수나 이후 확장 상한이 아니다.

## 3. 공통 제작 계약

각 초기 영웅은 다음 구조를 사용한다.

```text
원본 [영웅] 등급 병종 성능·역할·기본 AI·리그·공통 애니메이션 재사용
+ 영웅 이름·초상·스킨·식별 연출
+ 고유 자동 사용스킬 1개
```

- 영웅 전용 패시브는 사용하지 않는다.
- 고유 스킬 대가로 의무 능력치 하향을 적용하지 않는다.
- 고유 스킬 두 개 이상을 만들지 않는다.
- 완전 신규 유닛 5종으로 제작하지 않는다.

## 4. 검증 매트릭스

| 검증 축 | 요구 |
|---|---|
| 병종 다양성 | 서로 다른 UnitArchetype 5종 |
| 능력 유형 | 자동 고유 사용스킬형 5명 |
| 전술 역할 | 기능·타기팅 중복 최소화 |
| 전투력 | 원본 기본 성능 + 제한된 스킬 가치 |
| 활성 제한 | 세 전선 전체 이름 지정 영웅 최대 1명 |
| 자산 | 원본 리그·기본 애니메이션·AI 재사용 |
| UX | 스킬·trigger·cooldown·자동 발동·1/1 슬롯 표시 |
| 콘텐츠 | 각 타기팅 조건과 counter pressure 노출 |

측정 항목:

- 원본 대비 평균·고점 전투 기여.
- 고유 스킬 발동 빈도·유효 적중률.
- 영웅 간 선택률.
- 자동 타기팅 결정론 오류.
- 신규 자산량·자산 재사용률·제작 시간.
- 특정 영웅의 전 맵 지배 여부.

## 5. 적대적 검토

- 다섯 영웅 모두 고유 스킬이므로 제작량이 증가한다. 공통 자동 스킬 데이터·UI·VFX 틀을 재사용한다.
- 강제 상쇄가 없어 파워 크리프 위험이 있다. 전역 활성 1명·스킬 예산·콘텐츠 매트릭스로 통제한다.
- 패시브를 숨은 기본 공격 효과로 되살리지 않는다.
- 5명이 전체 출시 로스터로 오해되지 않도록 `INITIAL_VALIDATION_ROSTER`를 유지한다.

## 6. 금지

- 패시브형 영웅 배정.
- 고유 스킬 없는 이름 지정 영웅.
- 한 영웅에 독립 고유 스킬 두 개 이상.
- 5명 전부 신규 리그·AI·전체 애니메이션 제작.
- 초기 5명을 최종 출시 상한으로 해석.
- 제품 구현·자산·simulation 완료를 문서 승인과 혼동.

## 7. 구현 경계

```text
USER_APPROVED = TRUE
INITIAL_NAMED_HERO_COUNT = 5
INITIAL_SOURCE_ARCHETYPE_COUNT = 5
INITIAL_PASSIVE_COUNT = 0
INITIAL_AUTOMATIC_ACTIVE_SKILL_COUNT = 5
EXACT_ARCHETYPES = [shield_guard, archer, priest, mage, assassin]
EXACT_HERO_IDENTITIES = PENDING
EXACT_SKILLS = PENDING
PRODUCT_IMPLEMENTED = FALSE
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
