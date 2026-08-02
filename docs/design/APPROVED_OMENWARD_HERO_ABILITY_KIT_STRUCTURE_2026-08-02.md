# OMENWARD 이름 지정 영웅 2단 핵심 능력 키트 승인안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1
approved_at: 2026-08-02 21:08 KST
approval: USER_APPROVED_RECOMMENDED_OPTION
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
scope: GAMEPLAY_HERO_ABILITY_KIT_STRUCTURE
product_code_authority: NONE
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

모든 이름 지정 영웅은 다음 공통 2단 핵심 키트 구조를 사용한다.

```text
병종 기반 기본 공격
+ 고유 특성 1개
+ 자동 발동 전투 능력 1개
+ 명시적 약점·대응법 1개 이상
```

정규 키트 슬롯은 다음과 같다.

```text
BASE_ATTACK_PROFILE
HERO_TRAIT
HERO_COMBAT_ABILITY
OPTIONAL_UNIQUE_RESOURCE
COUNTERPLAY_METADATA
```

`OPTIONAL_UNIQUE_RESOURCE`는 능력 슬롯이 아니며 정말 필요한 영웅만 최대 1종 사용할 수 있다.

## 2. 병종 기반 기본 공격

- 이름 지정 영웅은 연결된 기존 `UnitArchetype`의 기본 공격 역할과 전술적 문법을 유지한다.
- 기본 공격은 사거리·공격 대상 영역·공격 리듬·핵심 역할을 완전히 다른 병종처럼 바꾸지 않는다.
- 영웅 고유 특성이 기본 공격을 변형할 수 있지만, 변형은 해당 병종 정체성을 보존해야 한다.
- 기본 공격 변형이 독립 쿨다운·충전·자원 소비·별도 대상 선택을 가지면 `HERO_COMBAT_ABILITY`로 계산한다.

## 3. 고유 특성 1개

`HERO_TRAIT`는 다음 중 하나를 주 역할로 가진다.

1. 기본 공격 변화.
2. 조건부 패시브.
3. 위치·전선·조합 규칙.

고유 특성은 다음 경계를 따른다.

- 항상 또는 조건부로 영웅의 전술 정체성을 설명한다.
- 독립적인 수동 입력을 요구하지 않는다.
- 별도 쿨다운 능력 둘 이상을 숨겨 넣지 않는다.
- 다수의 하위 효과가 있더라도 하나의 명확한 조건과 하나의 전술 목적 아래 묶여야 한다.
- 조건·효과·실패 조건·약점은 사용자에게 공개한다.

## 4. 자동 발동 전투 능력 1개

`HERO_COMBAT_ABILITY`는 이름 지정 영웅이 보유하는 유일한 정규 전투 능력 슬롯이다.

- 규칙 기반 자동 발동만 사용한다.
- 수동 스킬 버튼·수동 타깃 지정·수동 발동 보류는 없다.
- trigger, ability priority, target filter, target priority, tie-break를 공개한다.
- cooldown, charge, unique resource threshold 중 필요한 조합을 사용할 수 있다.
- 같은 combat tick에 합법 능력이 여러 개 존재하는 구조를 만들지 않는다.
- 대상 상실·중단·비용 소비·쿨다운 시작 시점은 개별 `HeroAbilitySpec`에서 명시한다.
- 저장·Retry로 능력 또는 타깃 결과를 재굴림할 수 없다.

## 5. 공통 궁극기 슬롯 금지

```text
UNIVERSAL_HERO_ULTIMATE_SLOT = FORBIDDEN
MANUAL_ULTIMATE_BUTTON = FORBIDDEN
SECOND_FULL_COMBAT_ABILITY = FORBIDDEN_BY_DEFAULT
```

- 모든 영웅에게 별도 궁극기 슬롯을 의무화하지 않는다.
- 강한 고점은 정규 전투 능력의 조건부 발동과 전술 조건 조성으로 만든다.
- 연출 규모가 크다는 이유만으로 별도 능력 슬롯으로 분리하지 않는다.
- 장기적으로 두 번째 정규 능력이 필요한 예외가 발견되면 별도 Decision ID와 적대적 검토가 필요하다.

## 6. 선택적 고유 자원

- 고유 자원은 영웅당 최대 1종이다.
- 고유 자원은 키트의 조건을 읽기 쉽게 만들 때만 사용한다.
- 단순 쿨다운으로 충분한 능력에 장식용 게이지를 추가하지 않는다.
- 획득·소비·상한·Stage 지속·정비시간 정지·사망 초기화 규칙을 공개한다.
- 이전 승인에 따라 생존 영웅의 현재 고유 자원은 Stage 경계를 넘어 유지하고 정비시간에는 clock이 정지한다.
- 새 적격 토큰으로 재출전한 영웅은 해당 자원의 정의된 초기값으로 시작한다.

## 7. 약점·대응법

각 영웅 키트는 최소 다음을 명시한다.

1. 고점 조건.
2. 고점 보상.
3. 실제 약점 또는 기회비용.
4. 원본 `[영웅]` 등급 병종이 더 나은 상황.
5. 적·맵·Wave·전선 상태 중 하나 이상의 대응 압력.

약점은 설명문에만 존재해서는 안 되며 실제 전투 결과에 영향을 줘야 한다.

## 8. 전투 예산 경계

- 키트의 기본 공격 변형·특성·자동 능력·고유 자원 효과는 하나의 총 전투 예산으로 평가한다.
- 정규 능력이 하나뿐이라는 이유로 해당 능력의 피해·제어·지원·기동성을 무제한으로 키우지 않는다.
- 고유 특성과 자동 능력이 같은 조건에서 동시에 상시 고점을 제공하지 않도록 조건 충족률을 검증한다.
- 원본 병종과 이름 지정 영웅의 평균 총 전투 예산은 대표 encounter에서 비교한다.
- 이름 지정 영웅은 조건부 전문화 sidegrade이며 순수 상위호환이 아니다.

## 9. 데이터 계약 방향

```yaml
HeroKitSpec:
  hero_id: string
  unit_archetype_id: string
  base_attack_profile_id: string
  trait:
    trait_id: string
    public_condition: string
    public_effect: string
    failure_condition: string
  combat_ability:
    ability_id: string
    trigger_conditions: list
    cooldown_or_charge_policy: object
    target_filter: object
    target_priority: list
    tie_break_rule: list
    invalid_target_policy: string
    interrupt_policy: string
  unique_resource: null_or_single_resource_spec
  peak_condition: string
  peak_payoff: string
  weakness: string
  original_unit_pick_case: string
  counter_pressure: list
```

정확한 schema 이름·필드 타입·serialization은 구현 계획에서 검증하며 이 문서는 제품 코드 변경 권한을 부여하지 않는다.

## 10. UX 요구

영웅 선택·변환 화면과 전투 정보에서 최소 다음을 보여준다.

- 병종 기반 기본 공격 역할.
- 고유 특성 한 줄 요약과 상세 조건.
- 자동 능력 trigger·대상 우선순위·쿨다운 또는 충전.
- 선택적 고유 자원 획득·소비·현재값.
- 고점 조건과 명시적 약점.
- 원본 병종과 비교했을 때 영웅을 선택할 이유와 선택하지 않을 이유.

## 11. 금지

- 기본 공격 변형·특성·자동 능력에 독립 능력을 숨겨 사실상 3~4개 능력 키트로 만드는 것.
- 영웅별로 능력 슬롯 수를 임의 변경하는 것.
- 공통 수동 궁극기 버튼.
- 장식용 고유 자원.
- 숨은 trigger·대상 선택·동률 해소.
- 약점 없는 상시 고점.
- 원본 병종의 역할을 완전히 대체하는 병종 이탈.
- 승인 문서를 구현·simulation·runtime·human QA 완료로 표시하는 것.

## 12. 후속 결정

다음 항목은 별도 Decision이 필요하다.

- 고유 특성의 허용 패턴과 금지 패턴 세부 분류.
- 자동 전투 능력의 cooldown·charge·resource 모델 우선순위.
- 첫 영웅 샘플과 해당 병종 원본 비교.
- invalid-target·interrupt·비용 소비 공통 정책.
- 영웅 카드·전투 HUD의 정확 정보 구조.
- 실제 수치·조건 충족률·선택률·counter encounter simulation.

## 13. 구현 경계

```text
USER_APPROVED = TRUE
GITHUB_AUTHORITY = THIS_DOCUMENT
PRODUCT_IMPLEMENTED = FALSE
EXACT_HERO_KITS = PENDING
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
