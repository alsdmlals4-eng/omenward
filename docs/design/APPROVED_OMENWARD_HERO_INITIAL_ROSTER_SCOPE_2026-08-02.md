# OMENWARD 이름 지정 영웅 초기 로스터 범위 승인안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-INITIAL-ROSTER-SCOPE-V1
approved_at: 2026-08-02 21:45 KST
approval: USER_APPROVED_RECOMMENDED_OPTION
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
scope: GAMEPLAY_HERO_INITIAL_VALIDATION_ROSTER
parent_kit_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1
parent_balance_decision: OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1
product_code_authority: NONE
exact_archetypes: PENDING
exact_heroes: PENDING
assets: NOT_CREATED
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

최초 제작·검증할 이름 지정 영웅 로스터는 **서로 다른 기존 핵심 병종 4종에 영웅 1명씩, 총 4명**으로 구성한다.

```text
서로 다른 기존 UnitArchetype 4종
→ 병종마다 이름 지정 영웅 1명
→ 패시브형 2명
→ 자동 사용스킬형 2명
→ 초기 검증 로스터 총 4명
```

```text
INITIAL_NAMED_HERO_COUNT = 4
INITIAL_SOURCE_ARCHETYPE_COUNT = 4
HEROES_PER_SOURCE_ARCHETYPE = 1
PASSIVE_VARIANT_COUNT = 2
AUTOMATIC_ACTIVE_SKILL_VARIANT_COUNT = 2
DUPLICATE_SOURCE_ARCHETYPE_IN_INITIAL_ROSTER = FORBIDDEN
```

이 범위는 영웅 시스템의 첫 제작·밸런스·UX·자산 재사용 검증을 위한 초기 로스터다. 최종 출시 전체 로스터 수나 이후 확장 상한을 결정하지 않는다.

## 2. 서로 다른 병종 4종

초기 영웅 4명은 각각 서로 다른 기존 `UnitArchetype`에 연결한다.

- 동일 병종에 복수 영웅을 배치하지 않는다.
- 병종별 원본 `[영웅]` 등급 유닛과 이름 지정 영웅을 직접 비교할 수 있어야 한다.
- 네 병종은 전투 기능과 플레이 판단이 가능한 한 겹치지 않게 선정한다.
- 정확한 병종 ID·이름·현행 데이터 적합성은 후속 Decision에서 저장소의 실제 유닛 명단을 검토해 확정한다.
- 특정 병종이 자산 재사용·자동 전투·상쇄 축 검증에 부적합하면 후보에서 제외할 수 있다.

초기 후보의 역할 범주는 예시일 뿐 아직 정본 병종 배정이 아니다.

- 전선 유지·방어.
- 지속 원거리 공격.
- 제어·지원.
- 공성·대형 적 대응.

## 3. 패시브형 2명·자동 사용스킬형 2명

```text
PASSIVE_XOR_AUTOMATIC_ACTIVE_SKILL
```

- 패시브형 영웅 2명으로 조건부 효과·기본 공격 변주·위치 또는 조합 규칙을 검증한다.
- 자동 사용스킬형 영웅 2명으로 공개 trigger·target priority·tie-break·cooldown 또는 charge를 검증한다.
- 각 영웅은 패시브와 사용스킬 중 하나만 가진다.
- 수동 스킬 버튼·수동 타깃은 계속 금지한다.
- 정확히 2:2를 맞추기 위해 병종 정체성과 맞지 않는 능력을 억지로 부여하지 않는다. 후보 병종 선정 단계에서 자연스럽게 2:2를 만족하는 조합을 선택한다.

## 4. 단일 차이·단일 상쇄 축 적용

각 초기 영웅은 기존 승인 계약을 그대로 따른다.

```text
원본 [영웅] 등급 병종 데이터
+ 스킨·이름·최소 식별 연출
+ 패시브 또는 자동 사용스킬 1개
- 직접 관련된 상쇄 축 1개
= 초기 이름 지정 영웅
```

불변식:

```text
signature_delta_count == 1
compensation_axis_count == 1
compensation_axis_is_related == true
all_other_source_axes_inherited == true
```

- 무료 능력 추가는 금지한다.
- 영웅별 전체 스탯 재설계는 금지한다.
- 원본 병종이 더 좋은 대표 상황을 유지한다.
- 네 영웅 모두 같은 단일 차이 패턴이나 같은 상쇄 축에 편중되지 않도록 후보를 검토한다.
- 정확 효과·상쇄 축·수치는 후속 설계와 simulation 전까지 pending이다.

## 5. 초기 로스터 선정 기준

각 후보 병종은 다음 기준을 만족해야 한다.

1. **원본 완성도**: 원본 `[영웅]` 등급 유닛의 역할·기본 공격·AI·데이터 구조가 비교 가능한 수준으로 정의돼 있어야 한다.
2. **자산 재사용성**: 기존 리그·애니메이션·투사체·AI·UI 구조를 스킨형 변주로 재사용할 수 있어야 한다.
3. **전술 차별성**: 다른 세 후보와 전투 판단이 과도하게 겹치지 않아야 한다.
4. **검증 가치**: 패시브형 또는 자동 사용스킬형의 핵심 위험을 실제로 시험할 수 있어야 한다.
5. **상쇄 가독성**: 얻는 것 하나와 잃는 것 하나를 플레이어가 짧게 이해할 수 있어야 한다.
6. **콘텐츠 노출성**: 대표 Stage·Wave·전선에서 장점과 약점이 모두 드러나야 한다.

인기·설정 매력만으로 후보를 선정하지 않는다. 시스템 검증 가치와 제작 가능성이 우선이다.

## 6. 제작량 계약

초기 로스터 4명은 다음 공통 제작 구조를 사용한다.

- 원본 병종 리그·기본 애니메이션·AI·이동·피격·사망 처리 재사용.
- 영웅별 이름·초상·스킨·장비 또는 실루엣 변주.
- 단일 차이를 식별하는 최소 VFX/SFX.
- 원본 대비 `얻는 것 1개 / 잃는 것 1개` 카드 문구.
- 패시브형 2개와 자동 사용스킬형 2개의 데이터·UI 템플릿.

```text
FOUR_FULL_NEW_UNITS = FORBIDDEN
FOUR_SKIN_LIKE_TACTICAL_VARIANTS = REQUIRED
```

초기 영웅 한 명이 새 리그·전체 애니메이션·별도 AI 아키텍처를 요구하면 후보 선정 또는 설계를 재검토한다.

## 7. 검증 매트릭스

초기 4명은 최소 다음을 함께 검증한다.

| 검증 축 | 요구 |
|---|---|
| 병종 다양성 | 서로 다른 UnitArchetype 4종 |
| 능력 유형 | 패시브형 2명·자동 사용스킬형 2명 |
| 전술 역할 | 기능 중복 최소화 |
| 상쇄 | 영웅별 직접 관련된 상쇄 축 1개 |
| 원본 선택 | 각 병종마다 원본이 더 나은 대표 상황 1개 이상 |
| 자산 | 원본 리그·기본 애니메이션·AI 재사용 가능 |
| UX | 원본/영웅 차이를 한 쌍의 교환으로 표시 |
| 콘텐츠 | 조건 on/off와 원본 우위 encounter 포함 |

측정 항목:

- 원본/영웅 선택률.
- 패시브형/사용스킬형 선택률.
- 조건 충족률·고점·저점.
- 상쇄 축 체감.
- 병종별 제작 시간과 신규 자산량.
- 자동 사용스킬 결정론 오류.
- 특정 영웅 또는 병종의 전 맵 지배 여부.

정확 목표치·표본 수·허용 편차는 아직 확정하지 않는다.

## 8. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 4명은 전체 게임 로스터로 너무 적다 | 유효하지만 범위 오해 | 초기 검증 로스터이며 최종 전체 로스터 수는 별도 Decision |
| 2:2 할당이 병종에 맞지 않는 능력을 강제한다 | 유효 | 능력을 억지로 바꾸지 않고 자연스럽게 2:2가 되는 병종 후보를 선정 |
| 서로 다른 병종이어도 실제 역할이 모두 비슷할 수 있다 | 유효 | 기능 중복 최소화와 대표 encounter 차별성 필수 |
| 네 영웅이 모두 같은 상쇄 축을 사용해 검증 폭이 좁다 | 유효 | 후보 검토에서 단일 차이·상쇄 패턴 편중을 경고 |
| 자산 재사용이 어려운 병종을 선택해 제작량이 폭증한다 | 유효 | 리그·애니메이션·AI 재사용 가능성을 선정 Gate로 사용 |
| 인기 캐릭터 우선으로 시스템 검증 가치가 약해진다 | 유효 | 초기 로스터는 제작 가능성과 검증 가치 우선 |
| 동일 병종 복수 영웅 비교가 불가능해진다 | 유효하지만 후속 범위 | 초기에는 병종 다양성을 우선하고 동일 병종 복수 영웅은 후속 확장 검증 |
| 4명 결정이 영구 출시 상한으로 오해된다 | 유효 | `INITIAL_VALIDATION_ROSTER`, 확장 상한 미확정 명시 |

## 9. 금지

- 초기 로스터에서 같은 `UnitArchetype`에 복수 이름 지정 영웅 배정.
- 패시브형과 사용스킬형의 2:2 검증 없이 한 유형으로 편중.
- 역할·전투 판단이 사실상 동일한 병종 4종 선정.
- 인기·서사만으로 병종을 선정하고 제작·검증 조건을 무시.
- 초기 4명을 모두 완전 신규 유닛으로 제작.
- 정확 병종·영웅·효과가 미확정인데 구현 완료로 표시.
- 초기 4명을 최종 출시 전체 로스터 상한으로 해석.

## 10. 후속 결정

- 실제 유닛 명단에서 초기 후보 병종 4종 선정.
- 네 병종의 역할 커버리지와 중복 검토.
- 각 병종에 패시브형 또는 자동 사용스킬형 배정.
- 첫 4명 이름·외형 콘셉트·단일 차이·상쇄 축.
- 초기 로스터 이후 확장 조건과 동일 병종 복수 영웅 도입 시점.

## 11. 구현 경계

```text
USER_APPROVED = TRUE
GITHUB_AUTHORITY = THIS_DOCUMENT
INITIAL_NAMED_HERO_COUNT = 4
INITIAL_SOURCE_ARCHETYPE_COUNT = 4
PASSIVE_VARIANT_COUNT = 2
AUTOMATIC_ACTIVE_SKILL_VARIANT_COUNT = 2
EXACT_ARCHETYPES = PENDING
EXACT_HEROES = PENDING
PRODUCT_IMPLEMENTED = FALSE
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
