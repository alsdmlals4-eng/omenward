# 오멘워드 영웅 전투 예산·전문화 Sidegrade 승인 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1
approved_at: 2026-08-02 19:05 KST
status: MERGED_USER_APPROVED / NOT_IMPLEMENTED
current_specialization: OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1
kit_structure_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1
product_code_authority: NONE
exact_values: PENDING
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

이름 지정 영웅은 같은 `UnitArchetype`의 원본 `[영웅]` 등급 유닛을 모든 상황에서 압도하는 순수 상위호환이 아니다.

```text
원본 [영웅] 등급 병종
= 일관성 + 범용성 + 낮은 조건 의존도

이름 지정 영웅
= 원본 병종 기반 스킨형 변주
+ 패시브 1개 또는 자동 사용스킬 1개
- 직접 관련된 상쇄 축 1개
```

## 2. 단일 차이·단일 상쇄 축

```text
SIGNATURE_DELTA_COUNT = 1
SIGNATURE_DELTA = PASSIVE XOR AUTOMATIC_ACTIVE_SKILL
COMPENSATION_AXIS_COUNT = 1
COMPENSATION_MUST_BE_CAUSALLY_RELATED = TRUE
ALL_OTHER_SOURCE_AXES_INHERITED = TRUE
```

- 단일 패시브 또는 자동 사용스킬의 가치를 피해·생존·사거리·제어·지원·기동·안정성·조건 의존도로 평가한다.
- 상쇄는 그 효과와 직접 관련된 능력치·효율·조건 축 정확히 하나에서만 적용한다.
- 상쇄 축 외의 원본 전투 데이터와 성장 구조는 기본적으로 유지한다.
- 조건 의존도를 상쇄로 사용하면 조건 미충족 구간에서 원본보다 낮은 효율이 실제로 나타나야 한다.
- 외형·이름·VFX 차이는 전투 예산으로 계산하지 않는다.
- 자동 발동 편의성 자체를 무료 전투력으로 계산하지 않는다.
- 원본 병종이 더 좋은 대표 상황을 최소 하나 유지한다.

주 책임 원본:

`APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md`

## 3. 허용되는 차이와 상쇄 예시

### 패시브형

- 광역 패시브 ↔ 단일 대상 피해 하향.
- 낮은 체력 방어 강화 ↔ 높은 체력 구간 방어 효율 조건화.
- 중장갑 대상 추가 피해 ↔ 비중장갑 대상 효율 하향.
- 아군 조합 보너스 ↔ 조건 미충족 구간 효율 하향.

### 자동 사용스킬형

- 자동 폭발 능력 ↔ 평상시 기본 공격 피해 하향.
- 자동 제어 능력 ↔ 기본 공격 피해 또는 공격 주기 중 하나만 하향.
- 특정 대상 처형 능력 ↔ 비해당 대상 효율 하향.
- 긴 cooldown 순간 고점 ↔ cooldown 구간의 원본 대비 낮은 지속 효율.

한 영웅에서 여러 상쇄 축을 동시에 적용하지 않는다.

## 4. 금지되는 상위호환·과잉 재설계

- 원본 스탯을 그대로 유지하면서 패시브 또는 사용스킬을 무료로 추가.
- 패시브와 사용스킬을 동시에 제공.
- 상쇄 축 두 개 이상.
- 여러 스탯을 조금씩 낮춰 사실상 전체 스탯을 다시 설계.
- 모든 영웅에게 동일한 고정 능력치 세금 적용.
- 능력과 무관하거나 체감되지 않는 축만 형식적으로 하향.
- 패시브 내부에 여러 독립 효과를 숨김.
- 사용스킬 내부에 둘 이상의 독립 능력을 묶음.
- 조건이 명목상 존재하지만 대부분의 전투에서 상시 충족됨.
- 원본 병종을 선택할 이유가 사라짐.
- 같은 병종의 다른 영웅을 수치 단계로 압도함.
- 단일 차이가 새 병종 수준으로 역할·사거리·AI를 변경함.

## 5. 필수 설계 필드

```yaml
NamedHeroVariantBudget:
  hero_id: string
  source_hero_grade_unit_id: string
  signature_delta_type: PASSIVE | AUTOMATIC_ACTIVE_SKILL
  signature_delta_id: string
  tactical_identity: string
  peak_condition: string
  peak_payoff: string
  compensation_axis: string
  source_axis_value: number_or_rule
  hero_axis_value: number_or_rule
  causal_link_explanation: string
  explicit_tradeoff: string
  original_unit_pick_case: string
  counter_pressure: list
  exact_values_status: PENDING
  simulation_status: NOT_RUN
```

- `compensation_axis`는 정확히 하나다.
- `causal_link_explanation`이 없으면 형식적 상쇄로 간주한다.
- `original_unit_pick_case`가 없으면 승인 가능한 영웅 설계가 아니다.
- 패시브형과 사용스킬형을 단일 DPS 수치로만 비교하지 않는다.

## 6. 제작량과 전투 가치 경계

- 원본 리그·애니메이션·AI·기본 공격 구조를 재사용하는 것은 제작량 절감이며 전투 약점으로 계산하지 않는다.
- 신규 제작량이 적다는 이유로 무료 능력 추가를 허용하지 않는다.
- 반대로 신규 자산이 많다는 이유로 전투력을 높이지 않는다.
- 영웅별 전체 스탯·성장 곡선을 새로 만들지 않는다.
- 이름 지정 영웅의 수집 매력은 외형·이름·연출 차이와 단일 전술 변주에서 확보한다.

## 7. 검증 계약

구현 전·후에 최소 다음을 비교한다.

- 원본 병종과 이름 지정 영웅의 조건 충족·불충족 encounter.
- 원본·패시브형·사용스킬형 선택률.
- 단일 차이의 평균 가치와 고점 가치.
- 상쇄 축의 실제 손실과 파생 영향.
- 원본 선택 상황이 실제로 발생하는지.
- 같은 병종 영웅 간 역할 중복과 지배 여부.
- 기본 Profile과 원본 병종만으로 콘텐츠 완료 가능성.

정확 허용 편차·표본 수·가중치는 아직 확정하지 않는다.

## 8. UX 책임

영웅 변환 화면은 다음을 짧게 비교한다.

```text
얻는 것: 패시브 또는 자동 사용스킬 하나
잃는 것: 직접 관련된 상쇄 축 하나
```

- 원본과 동일한 핵심 역할.
- 유리한 조건과 핵심 이득.
- 상쇄되는 능력치·효율·조건.
- 원본 병종을 선택할 대표 상황.

`완전한 강화`, `상위 버전`, `무료 스킬 추가`처럼 순수 상위호환으로 오해시키는 표현을 사용하지 않는다.

## 9. 구현 경계

```text
HERO_MODEL = SOURCE_HERO_GRADE_UNIT_PLUS_ONE_SIGNATURE_DELTA
BALANCE_MODEL = ONE_DELTA_MINUS_ONE_RELATED_AXIS
TOTAL_COMBAT_BUDGET = COMPARABLE_NOT_IDENTICAL
ORIGINAL_UNIT_PICK_CASE = REQUIRED
FREE_SIGNATURE_POWER = FORBIDDEN
FULL_STAT_REDESIGN = FORBIDDEN
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
PRODUCT_CODE = UNCHANGED
```
