# OMENWARD 이름 지정 영웅 단일 차이·단일 상쇄 축 승인안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1
approved_at: 2026-08-02 21:28 KST
approval: USER_APPROVED_RECOMMENDED_OPTION
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
scope: GAMEPLAY_HERO_SIGNATURE_DELTA_BALANCE
parent_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1
product_code_authority: NONE
exact_values: PENDING
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

이름 지정 영웅은 원본 병종 `[영웅]` 등급 유닛의 전투 데이터를 우선 복사하고, 영웅 전용 패시브 또는 자동 `[사용스킬]` 하나를 추가·교체한 뒤 그 효과와 직접 관련된 **상쇄 축 하나만** 하향하거나 조건화한다.

```text
원본 [영웅] 등급 병종 데이터 복사
→ 영웅 전용 단일 차이 적용
→ 직접 관련된 상쇄 축 1개 선택
→ 그 축만 하향 또는 조건화
→ 나머지 원본 전투 데이터 유지
```

```text
SIGNATURE_DELTA_COUNT = 1
COMPENSATION_AXIS_COUNT = 1
COMPENSATION_MUST_BE_CAUSALLY_RELATED = TRUE
FULL_STAT_REDESIGN = FORBIDDEN
FREE_SIGNATURE_POWER = FORBIDDEN
```

## 2. 단일 상쇄 축

각 이름 지정 영웅은 `compensation_axis`를 정확히 하나 가진다.

허용 가능한 축의 예시는 다음과 같다.

- 기본 공격 피해.
- 공격 주기 또는 공격 속도.
- 단일 대상 효율 또는 광역 대상 효율.
- 방어력·최대 HP·피해 경감 중 하나.
- 사거리 또는 유효 대응 범위.
- 효과 지속률·발동 가능 시간·조건 의존도.
- 특정 대상군에 대한 효율.

한 영웅에서 여러 축을 동시에 낮추거나, 전체 스탯을 다시 작성하지 않는다.

## 3. 직접 관련성 원칙

상쇄 축은 영웅 전용 차이의 가치와 직접 연결돼야 한다.

허용 예시:

```text
광역 패시브 추가
→ 단일 대상 기본 공격 피해 하향

자동 폭발 사용스킬 추가
→ 평상시 기본 공격 피해 또는 공격 주기 중 하나만 하향

낮은 체력에서 방어 강화
→ 높은 체력 구간의 방어 효율 조건화

중장갑 대상 추가 피해
→ 비중장갑 대상 효율 하향

아군 조합 패시브
→ 조건 미충족 구간의 효율 하향
```

금지 예시:

- 제어 능력을 추가하고 무관한 이동 속도만 낮춰 실질 비용을 회피.
- 강력한 광역 능력을 추가한 뒤 거의 체감되지 않는 자원 하나만 감소.
- 공격 능력 하나 때문에 공격력·HP·방어력·사거리를 동시에 하향.
- 모든 영웅에게 동일한 고정 세금을 적용.
- 원본과 같은 스탯을 유지한 채 능력만 무료 추가.

## 4. 원본 데이터 재사용

상쇄 축 외에는 원본 `[영웅]` 등급 병종의 값을 기본적으로 유지한다.

```text
SOURCE_STAT_PROFILE = INHERITED
OVERRIDDEN_STAT_OR_CONDITION_COUNT = 1
```

- 역할·기본 공격 문법·사거리·이동·AI·리그·기본 애니메이션 재사용 원칙을 유지한다.
- 상쇄 때문에 새로운 병종처럼 역할을 다시 설계하지 않는다.
- 수치 변경이 필요 없는 대신 조건 의존도를 높이는 경우에도 조건 하나를 상쇄 축으로 계산한다.
- 영웅별 전체 성장 곡선·스탯 테이블을 새로 만들지 않는다.

## 5. 패시브형 적용

패시브형 영웅은 다음 구조를 사용한다.

```text
원본 병종 전투 데이터
+ 패시브 1개
- 관련 상쇄 축 1개
```

- 패시브의 조건·효과·실패 조건을 공개한다.
- 패시브가 여러 독립 이득을 제공하면 단일 차이 계약 위반이다.
- 패시브가 상시 적용되는 경우 상쇄 축은 실제 평균 전투 성능에 영향을 줘야 한다.
- 조건부 패시브는 조건 미충족 구간 자체를 상쇄 축으로 사용할 수 있다.

## 6. 자동 사용스킬형 적용

사용스킬형 영웅은 다음 구조를 사용한다.

```text
원본 병종 전투 데이터
+ 규칙 기반 자동 사용스킬 1개
- 관련 상쇄 축 1개
```

- trigger·대상 우선순위·tie-break·cooldown 또는 charge를 공개한다.
- 사용스킬이 준비되지 않았거나 유효 대상이 없을 때 원본보다 낮아지는 축이 명확해야 한다.
- 수동 버튼·수동 타깃 지정은 계속 금지한다.
- 사용스킬의 순간 고점과 평상시 상쇄를 별도로 측정한다.

## 7. 데이터 계약 방향

```yaml
HeroSignatureDeltaBalanceSpec:
  hero_id: string
  source_hero_grade_unit_id: string
  signature_delta_type: PASSIVE | AUTOMATIC_ACTIVE_SKILL
  signature_delta_id: string
  compensation_axis: string
  source_axis_value: number_or_rule
  hero_axis_value: number_or_rule
  causal_link_explanation: string
  peak_condition: string
  original_unit_pick_case: string
  counter_pressure: list
  exact_values_status: PENDING
  simulation_status: NOT_RUN
```

불변식:

```text
signature_delta_count == 1
compensation_axis_count == 1
compensation_axis_is_related == true
all_other_source_axes_inherited == true
```

정확 schema·타입·serialization은 구현 계획에서 확정하며 이 문서는 제품 코드 변경 권한을 부여하지 않는다.

## 8. UX 요구

원본 병종과 이름 지정 영웅 비교 화면은 다음을 한 쌍으로 표시한다.

```text
얻는 것: 패시브 또는 자동 사용스킬 하나
잃는 것: 직접 관련된 상쇄 축 하나
```

최소 표시 항목:

- 원본과 동일한 역할.
- 바뀌는 단일 차이.
- 상쇄되는 능력치 또는 조건.
- 유리한 상황.
- 원본 병종이 더 나은 상황.

여러 능력치 변화 목록을 보여주는 영웅은 이 계약을 위반한다.

## 9. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 상쇄 축이 너무 작아 무료 능력과 동일해진다 | 유효 | 대표 encounter에서 체감 가능한 손실과 원본 선택 상황 검증 |
| 무관한 축을 낮춰 실질 비용을 회피한다 | 유효 | `causal_link_explanation` 필수 |
| 여러 스탯을 조금씩 낮춰 사실상 전체 재설계한다 | 유효 | 상쇄 축 정확히 1개 |
| 모든 영웅에 동일한 세금을 적용해 역할별 왜곡 발생 | 유효 | 영웅 전용 차이와 직접 관련된 축만 선택 |
| 조건부 상쇄가 대부분 충족돼 실질 약점이 없다 | 유효 | 조건 충족률·미충족 encounter 분리 측정 |
| 단일 축 하향이 지나쳐 영웅이 함정 선택이 된다 | 유효 | 원본/영웅 선택률과 평균 예산 비교 |
| 수치 하나만 바꾸지만 파생 효과 여러 개가 함께 변한다 | 유효 | 파생 영향 포함 총 전투 예산 검증 |

## 10. 검증 계약

각 영웅은 최소 다음 시나리오를 비교한다.

1. 단일 차이가 유리한 조건.
2. 단일 차이가 불리하거나 작동하지 않는 조건.
3. 원본 병종이 더 안정적인 조건.
4. 대표 Stage·Wave·전선 상태.
5. 표준 조합과 최적 조합.

측정 항목:

- 원본과 영웅의 평균 총 전투 기여.
- 고점과 저점.
- 상쇄 축의 실제 체감.
- 원본/영웅 선택률.
- 조건 충족률.
- 한 영웅의 전 맵 지배 여부.

정확 허용 편차·표본 수·목표 선택률은 아직 확정하지 않는다.

## 11. 금지

- 원본과 같은 전투 데이터를 유지한 무료 능력 추가.
- 상쇄 축 두 개 이상.
- 영웅마다 전체 스탯·성장 곡선 새 설계.
- 모든 영웅 공통 고정 능력치 세금.
- 능력과 무관한 형식적 하향.
- 설명에만 존재하고 전투 결과에 영향 없는 약점.
- 상쇄를 이유로 원본 병종 역할·AI·기본 공격 문법을 변경.
- 정확 수치와 simulation을 실행 전에 완료로 표시.

## 12. 후속 결정

- 패시브형과 사용스킬형의 허용 상쇄 축 목록 확정 여부.
- 첫 원본 병종–이름 지정 영웅 샘플.
- 정확 허용 편차와 선택률 기준.
- 단일 축 파생 영향 계산 방식.
- 영웅 카드 비교 UI.

## 13. 구현 경계

```text
USER_APPROVED = TRUE
GITHUB_AUTHORITY = THIS_DOCUMENT
BALANCE_MODEL = SOURCE_PROFILE_PLUS_ONE_DELTA_MINUS_ONE_RELATED_AXIS
PRODUCT_IMPLEMENTED = FALSE
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
