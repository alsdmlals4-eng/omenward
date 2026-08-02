# OMENWARD 이름 지정 영웅 단일 차이·스킨형 변주 승인안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1
approved_at: 2026-08-02 21:08 KST
refined_at: 2026-08-02 21:28 KST
approval: USER_DIRECT_REFINEMENT
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
scope: GAMEPLAY_HERO_SINGLE_DELTA_VARIANT_KIT
balance_decision: OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1
product_code_authority: NONE
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

이름 지정 영웅은 연결된 기존 병종의 원본 `[영웅]` 등급 유닛을 기반으로 하는 **스킨형 전술 변주**다. 완전히 새로운 유닛 키트를 제작하지 않고, 외형·이름·연출을 바꾸면서 전투 규칙은 핵심 차이 하나만 둔다.

```text
기존 병종 [영웅] 등급 유닛
+ 영웅 전용 외형·이름·최소 연출 차이
+ 패시브 1개 또는 자동 [사용스킬] 1개
- 직접 관련된 상쇄 축 1개
= 이름 지정 영웅
```

```text
SIGNATURE_DELTA_COUNT = 1
SIGNATURE_DELTA_TYPE = PASSIVE OR AUTOMATIC_ACTIVE_SKILL
PASSIVE_AND_ACTIVE_TOGETHER = FORBIDDEN_BY_DEFAULT
COMPENSATION_AXIS_COUNT = 1
```

## 2. 원본 병종 계승

이름 지정 영웅은 원본 `[영웅]` 등급 병종에서 다음을 기본적으로 그대로 계승한다.

- 핵심 역할과 전선 포지션.
- 기본 공격 방식·사거리·공격 주기·대상 범주.
- 이동·충돌·배치 규칙.
- 기본 스탯 구조와 성장 곡선.
- 일반 애니메이션 구조·리그·피격·이동·사망 처리.
- 기본 AI와 대상 탐색 구조.
- Stage·사망·재출전·저장 규칙.

정확 수치는 단일 상쇄 축 하나에서만 조정할 수 있으며, 별도 병종처럼 전체를 다시 설계하지 않는다.

## 3. 단일 차이 슬롯

각 이름 지정 영웅은 다음 두 유형 중 정확히 하나를 선택한다.

### A. 패시브형

```text
원본 [영웅] 등급 병종 규칙
+ 영웅 패시브 1개
- 관련 상쇄 축 1개
```

- 조건부 능력치 변화, 기본 공격의 단순 효과 추가, 위치·전선·조합 조건 중 하나를 사용한다.
- 독립 쿨다운·충전·별도 대상 선택이 있으면 패시브가 아니라 사용스킬로 분류한다.
- 여러 하위 효과를 묶더라도 하나의 조건과 하나의 전술 목적만 가져야 한다.

### B. 사용스킬형

```text
원본 [영웅] 등급 병종 규칙
+ 영웅 자동 사용스킬 1개
- 관련 상쇄 축 1개
```

- `[사용스킬]`은 수동 버튼이 아니라 규칙 기반 자동 발동 능력이다.
- trigger·target filter·target priority·tie-break·cooldown 또는 charge를 공개한다.
- 원본 병종이 이미 가진 일반 기능을 유지하면서 영웅 전용 자동 능력 하나만 추가하거나 교체한다.
- 수동 발동·수동 타깃 지정·수동 보류는 금지한다.

## 4. 패시브와 사용스킬의 상호 배타성

```text
PASSIVE_ONLY
XOR
AUTOMATIC_ACTIVE_SKILL_ONLY
```

- 한 이름 지정 영웅에 영웅 전용 패시브와 영웅 전용 사용스킬을 동시에 주지 않는다.
- 기본 공격 수치 조정이나 단순 VFX는 별도 능력으로 계산하지 않는다.
- 기본 공격에 조건부 추가 효과·상태 이상·별도 대상 판단이 붙으면 패시브 슬롯을 소비한다.
- 독립 쿨다운·충전·자원을 가진 효과는 사용스킬 슬롯을 소비한다.
- 패시브 또는 사용스킬 내부에 여러 독립 능력을 숨기지 않는다.

## 5. 스킨형 제작 범위

이름 지정 영웅은 다음 제작 자산을 우선 재사용한다.

- 원본 병종의 리그·본 구조.
- 이동·기본 공격·피격·사망 애니메이션.
- 기본 투사체·충돌·AI·전선 이동 코드.
- 공통 UI 카드·상태 표시 구조.
- 원본 병종의 기본 음향을 기반으로 한 변주.

영웅별 신규 제작은 다음에 집중한다.

- 영웅 전용 이름·초상·색상·장비·실루엣 변주.
- 필요한 범위의 스킨·머티리얼·VFX·SFX 변주.
- 단일 패시브 또는 단일 자동 사용스킬의 식별 연출.
- 영웅 차이를 설명하는 짧은 카드 문구.

```text
NEW_FULL_RIG = NOT_REQUIRED_BY_DEFAULT
NEW_FULL_ANIMATION_SET = NOT_REQUIRED_BY_DEFAULT
UNIQUE_VOICE_PACK = NOT_REQUIRED_BY_DEFAULT
NEW_AI_ARCHITECTURE = FORBIDDEN_BY_DEFAULT
```

외형은 스킨에 가까운 제작량을 목표로 하지만 전투 차이는 실제 선택에 영향을 주는 단일 전술 차이여야 한다.

## 6. 단일 상쇄 축

주 책임 원본:

`APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md`

```text
원본 전투 데이터 복사
→ 단일 차이 적용
→ 직접 관련된 상쇄 축 정확히 1개
→ 나머지 원본 데이터 유지
```

- 상쇄 축은 패시브 또는 사용스킬의 가치와 직접 연결돼야 한다.
- 기본 공격 피해·공격 주기·대상 효율·방어 효율·사거리·조건 의존도 등에서 하나만 선택한다.
- 여러 스탯을 동시에 낮추거나 전체 성장 곡선을 새로 만들지 않는다.
- 모든 영웅에게 같은 고정 능력치 세금을 적용하지 않는다.
- 조건 미충족 구간을 상쇄로 쓰는 경우 실제 전투 결과에 저점이 나타나야 한다.
- 원본 병종이 더 나은 대표 상황을 최소 하나 유지한다.

```text
VISUAL_VARIANT != FREE_POWER
ONE_SIGNATURE_DELTA != UNIVERSAL_UPGRADE
ONE_COMPENSATION_AXIS != FULL_STAT_REDESIGN
```

## 7. 고유 자원·궁극기 경계

```text
UNIVERSAL_HERO_ULTIMATE_SLOT = FORBIDDEN
SECOND_HERO_SIGNATURE_DELTA = FORBIDDEN_BY_DEFAULT
UNIQUE_RESOURCE = FORBIDDEN_BY_DEFAULT
```

- 스킨형 제작량을 유지하기 위해 고유 자원은 기본적으로 사용하지 않는다.
- 단일 사용스킬이 단순 쿨다운 또는 충전으로 설명되지 않을 때만 별도 Decision으로 예외를 검토한다.
- 공통 궁극기 슬롯·수동 궁극기 버튼은 두지 않는다.

## 8. 데이터 계약 방향

```yaml
NamedHeroVariantSpec:
  hero_id: string
  unit_archetype_id: string
  source_hero_grade_unit_id: string
  visual_variant_id: string
  signature_delta_type: PASSIVE | AUTOMATIC_ACTIVE_SKILL
  passive_spec: null_or_single_passive
  active_skill_spec: null_or_single_automatic_skill
  compensation_axis: string
  source_axis_value: number_or_rule
  hero_axis_value: number_or_rule
  causal_link_explanation: string
  tactical_identity: string
  peak_condition: string
  explicit_tradeoff: string
  original_unit_pick_case: string
  counter_pressure: list
```

불변식:

```text
(passive_spec != null) XOR (active_skill_spec != null)
compensation_axis_count == 1
all_other_source_axes_inherited == true
```

정확 schema·serialization·Resource 구조는 구현 계획에서 확정하며 제품 코드 변경 권한은 없다.

## 9. UX 요구

영웅 선택 화면은 원본 `[영웅]` 등급 병종과 이름 지정 영웅의 차이를 짧게 비교한다.

```text
얻는 것: 바뀌는 단 하나의 패시브 또는 자동 사용스킬
잃는 것: 직접 관련된 상쇄 축 하나
```

- 원본과 동일한 핵심 역할.
- 그 차이가 유리한 조건.
- 상쇄되는 약점 또는 원본이 더 나은 상황.
- 사용스킬형은 자동 발동임을 명시.

사용자가 긴 스킬·스탯 목록을 읽지 않고도 `같은 병종의 스킨형 변주 + 차이 1개 + 상쇄 1개`로 이해할 수 있어야 한다.

## 10. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 차이 하나가 너무 작아 장식 전용 스킨처럼 느껴진다 | 유효 | 전술 선택을 바꾸는 명확한 조건과 결과 요구 |
| 외형만 바꾸고 무료 능력을 추가해 원본을 폐기한다 | 유효 | 단일 관련 상쇄 축·원본 선택 상황 유지 |
| 여러 스탯을 조금씩 낮춰 전체 신규 유닛처럼 재설계한다 | 유효 | 상쇄 축 정확히 1개 |
| 능력과 무관한 축을 낮춰 비용을 회피한다 | 유효 | `causal_link_explanation` 필수 |
| 패시브 안에 여러 효과를 넣어 작업량이 다시 커진다 | 유효 | 하나의 조건·하나의 전술 목적·독립 능력 금지 |
| 사용스킬이 수동 버튼으로 해석된다 | 유효 | 모든 `[사용스킬]`은 `AUTOMATIC_RULE_BASED` |
| 영웅마다 새 리그·애니메이션·AI를 요구한다 | 유효 | 원본 자산·AI·코드 재사용이 기본 계약 |
| 모든 영웅이 같은 색놀이로 보여 수집 매력이 약하다 | 유효 | 이름·초상·실루엣·장비·VFX 중 식별 가능한 차이 요구 |
| 단일 차이가 새 병종 수준으로 역할을 바꾼다 | 유효 | 원본 역할·사거리·기본 공격 문법 유지 |

## 11. 금지

- 영웅 전용 패시브와 영웅 전용 사용스킬을 동시에 제공.
- 둘 이상의 독립 패시브 또는 둘 이상의 사용스킬.
- 상쇄 축 두 개 이상.
- 영웅별 전체 스탯·성장 곡선 재설계.
- 모든 영웅 공통 고정 능력치 세금.
- 능력과 무관한 형식적 하향.
- 원본 병종과 완전히 다른 기본 공격·사거리·전선 역할.
- 이름 지정 영웅별 신규 AI 아키텍처.
- 기본적으로 새 리그·전체 애니메이션 세트를 요구하는 설계.
- 수동 스킬·수동 타깃·수동 궁극기.
- 약점·상쇄 없는 무료 능력 추가.
- `스킨형`이라는 이유로 전투 차이가 전혀 없는 장식 전용 영웅.

## 12. 후속 결정

- 초기 이름 지정 영웅 로스터 규모.
- 패시브형 영웅의 허용 패턴.
- 사용스킬형 영웅의 cooldown·charge 공통 모델.
- 첫 원본 병종–이름 지정 영웅 샘플 비교.
- 스킨·실루엣·VFX 최소 차별화 기준.
- 정확 허용 편차와 선택률 기준.
- 영웅 카드의 원본 대비 비교 UX.

## 13. 구현 경계

```text
USER_APPROVED = TRUE
GITHUB_AUTHORITY = THIS_DOCUMENT
HERO_MODEL = SOURCE_HERO_GRADE_UNIT_PLUS_ONE_SIGNATURE_DELTA
BALANCE_MODEL = ONE_DELTA_MINUS_ONE_RELATED_AXIS
SIGNATURE_DELTA = PASSIVE_XOR_AUTOMATIC_ACTIVE_SKILL
VISUAL_SCOPE = SKIN_LIKE_VARIANT
PRODUCT_IMPLEMENTED = FALSE
EXACT_HERO_VARIANTS = PENDING
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
