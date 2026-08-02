# OMENWARD 해금 영웅 고유 스킬·제한형 상위호환 승인안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
approved_at: 2026-08-02 22:29 KST
approval: USER_DIRECT_REFINEMENT
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
scope: GAMEPLAY_HERO_UNIQUE_SKILL_UPGRADE_MODEL
supersedes_kit_split_in: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1
supersedes_compensation_in: OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1
refines_power_budget: OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1
activation_decision: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
product_code_authority: NONE
exact_skills: PENDING
exact_values: PENDING
assets: NOT_CREATED
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

해금하는 이름 지정 영웅은 원본 병종의 `[영웅]` 등급 유닛보다 **조금 더 강하고 임팩트 있는 제한형 상위호환**으로 설계한다.

```text
원본 병종 [영웅] 등급 유닛
+ 이름·초상·스킨·식별 연출
+ 고유 자동 사용스킬 정확히 1개
= 해금 이름 지정 영웅
```

```text
UNIQUE_ACTIVE_SKILL_COUNT = 1
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
MANDATORY_COMPENSATION_AXIS_COUNT = 0
SOURCE_BASELINE_STATS = INHERITED
NAMED_HERO_POWER_MODEL = CONSTRAINED_UPGRADE
```

- 이름 지정 영웅은 원본 `[영웅]` 등급 유닛의 역할·기본 공격·기본 스탯·사거리·이동·기본 AI·리그·공통 애니메이션을 우선 계승한다.
- 영웅 전용 패시브는 사용하지 않는다.
- 모든 이름 지정 영웅은 영웅 전용 고유 `[사용스킬]` 하나를 가진다.
- 고유 스킬은 기존 자동 전투 정본에 따라 규칙 기반으로 자동 발동한다.
- 고유 스킬을 얻는 대가로 기본 능력치나 효율을 의무적으로 낮추지 않는다.
- 동일 조건에서는 원본 유닛보다 기능적으로 우수하다는 해금 보상을 의도한다.

## 2. 상위호환의 제한 장치

상위호환은 다음 시스템 제한으로 통제한다.

```text
NAMED_HERO_GLOBAL_ACTIVE_CAP = 1
UNLOCK_REQUIRED = TRUE
ELIGIBLE_HERO_GRADE_TOKEN_REQUIRED = TRUE
LANE_DEPLOYMENT_IS_IRREVERSIBLE = TRUE
MANUAL_RETREAT_OR_SWAP = FORBIDDEN
```

- 세 전선 전체에서 활성 이름 지정 영웅은 최대 1명이다.
- 이름 지정 영웅은 영구 해금되어야 한다.
- 연결 병종의 `[영웅]` 등급 토큰이 있어야 출전한다.
- 배치 후 수동 퇴각·교대·판매·재보관·전선 이동은 허용하지 않는다.
- 다른 이름 지정 영웅이 활성 중이면 나머지 `[영웅]` 등급 토큰은 원본 병종 유닛으로 사용한다.
- 따라서 원본 `[영웅]` 등급 유닛은 해금 전과 전역 슬롯 경쟁 상황에서 계속 필요하다.

## 3. 고유 스킬 슬롯

각 이름 지정 영웅은 정확히 하나의 고유 자동 사용스킬을 가진다.

```text
SOURCE_BASIC_COMBAT
+ ONE_UNIQUE_AUTOMATIC_ACTIVE_SKILL
```

고유 스킬은 다음 필드를 공개한다.

- `trigger`
- `target_filter`
- `target_priority`
- `tie_break`
- `cooldown` 또는 `charge_rule`
- `effect`
- `failure_or_no_target_behavior`
- `visual_and_audio_cue`

규칙:

- 독립적인 두 스킬을 한 슬롯에 묶지 않는다.
- 스킬 효과는 원본 병종의 역할을 강화하거나 인상적인 고점을 만든다.
- 원본 병종과 완전히 다른 전선 역할·기본 공격 문법·이동 체계를 만들지 않는다.
- 고유 스킬의 순간 고점은 분명하게 보이는 VFX/SFX와 전투 결과로 전달한다.
- 수동 버튼·수동 타깃·수동 보류는 금지한다.

## 4. 패시브 폐기

이전의 `패시브 또는 자동 사용스킬` 선택 구조를 폐기한다.

```text
PASSIVE_XOR_AUTOMATIC_ACTIVE_SKILL = SUPERSEDED
PASSIVE_VARIANT = FORBIDDEN
AUTOMATIC_ACTIVE_SKILL = REQUIRED
```

- 기본 공격·기본 AI·기본 스탯에 숨은 영웅 전용 패시브를 넣지 않는다.
- 스킬 설명 밖에서 상시 적용되는 보너스를 제공하지 않는다.
- 영웅의 개성은 스킨·이름·연출과 고유 자동 사용스킬 하나에 집중한다.
- 원본 능력 수정형이 아니라 원본 전투 기반 위에 고유 스킬을 추가하는 구조를 기본으로 한다.

## 5. 강제 상쇄 축 폐기

이전의 `단일 차이 + 관련 상쇄 축 1개` 의무를 폐기한다.

```text
COMPENSATION_AXIS_REQUIRED = FALSE
BASELINE_NERF_REQUIRED = FALSE
ORIGINAL_UNIT_PICK_CASE_REQUIRED_BY_STAT_WEAKNESS = FALSE
```

- 고유 스킬 추가를 이유로 공격력·체력·방어력·사거리·지원 효율을 자동으로 낮추지 않는다.
- 형식적인 약점을 만들어 해금 보상의 임팩트를 희석하지 않는다.
- 밸런스는 스킬 cooldown·charge·trigger·효과 범위와 전역 활성 1명 제한으로 조정한다.
- 특정 영웅이 모든 병종·전선·Stage에서 유일한 정답이 되지 않도록 영웅 간 선택 상황과 콘텐츠 대응 범위를 검증한다.

## 6. 전투 예산 방향

```text
SOURCE_HERO_GRADE_BASELINE
+ CONTROLLED_SIGNATURE_SKILL_VALUE
= NAMED_HERO_TOTAL_POWER
```

- 이름 지정 영웅의 평균 전투 기여는 연결된 원본 `[영웅]` 등급 유닛보다 높아도 된다.
- 목표는 해금 직후 체감되는 명확한 강화와 연출적 만족감이다.
- 정확 강화 폭은 아직 고정하지 않는다.
- 강화 폭은 모든 영웅에게 동일한 DPS 배율로 주지 않고 각 고유 스킬의 역할 가치로 산정한다.
- 기본 스탯을 별도 영웅 테이블로 다시 설계하지 않는다.

## 7. 초기 5명 적용

현재 초기 로스터의 다섯 영웅은 모두 자동 사용스킬형이다.

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
```

정확 영웅 이름·스킬 효과·발동 조건·cooldown·VFX/SFX는 후속 Decision에서 확정한다.

## 8. 데이터 계약 방향

```yaml
NamedHeroUpgradeSpec:
  hero_id: string
  source_hero_grade_unit_id: string
  visual_variant_id: string
  unique_active_skill_id: string
  trigger: string
  target_filter: string
  target_priority: string
  tie_break: string
  cooldown_or_charge_rule: string
  effect: string
  no_target_behavior: string
  visual_cue: string
  audio_cue: string
  source_baseline_inherited: true
  hero_exclusive_passive: null
  mandatory_compensation_axis: null
  exact_values_status: PENDING
  simulation_status: NOT_RUN
```

불변식:

```text
unique_active_skill_count == 1
hero_exclusive_passive_count == 0
source_baseline_inherited == true
manual_activation == false
named_hero_global_active_count <= 1
```

정확 schema·Resource·serialization은 구현 계획에서 확정하며 이 문서는 제품 코드 변경 권한을 부여하지 않는다.

## 9. UX·연출 요구

영웅 선택 화면은 원본과 이름 지정 영웅을 다음처럼 설명한다.

```text
원본 [영웅] 등급: 기본 병종의 최고 등급 유닛
해금 이름 지정 영웅: 동일 기본 성능 + 고유 자동 사용스킬 1개
```

최소 표시 항목:

- 영웅 이름과 연결 병종.
- 고유 스킬 이름.
- 발동 조건과 주요 효과.
- 자동 발동 표시.
- 전역 이름 지정 영웅 활성 제한 `1/1`.
- cooldown 또는 charge 상태.

연출 요구:

- 스킬 발동 순간을 전투 화면에서 즉시 식별할 수 있어야 한다.
- 초상·실루엣·장비·스킬 VFX/SFX 중 최소 두 축으로 원본과 구분한다.
- 단순 색상 변경만으로 해금 보상을 표현하지 않는다.

## 10. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 원본 유닛이 완전히 무의미해진다 | 부분 유효 | 미해금·다른 영웅 활성 중·전역 슬롯 경쟁에서 원본 유지 |
| 무료 고유 스킬로 파워 크리프가 누적된다 | 유효 | 전역 활성 1명·스킬 예산·콘텐츠 매트릭스·영웅 간 선택률 검증 |
| 모든 영웅이 궁극기처럼 과도하게 복잡해진다 | 유효 | 고유 스킬 정확히 1개·하나의 전술 목적·공통 자동 발동 프레임 |
| 패시브를 스킬 내부에 숨긴다 | 유효 | 상시 효과·숨은 보너스 금지, 공개 trigger 기반 효과만 허용 |
| 영웅별 새 AI·리그·전체 애니메이션으로 제작량이 폭증한다 | 유효 | 원본 AI·리그·기본 애니메이션 재사용, 스킬 연출만 추가 |
| 상위호환이 특정 병종 해금을 강제한다 | 유효 | 기본 원본만으로 진행 가능·해금 순서·콘텐츠 요구도 검증 |
| 자동 발동이 플레이어에게 통제 불가능하게 느껴진다 | 유효 | trigger·priority·cooldown·예상 대상 공개 |
| 스킬 임팩트가 약해 해금 보상이 느껴지지 않는다 | 유효 | 명확한 전투 결과·VFX/SFX·사용성 테스트 필수 |

## 11. 금지

- 영웅 전용 패시브.
- 영웅별 고유 스킬 두 개 이상.
- 수동 스킬 버튼·수동 타깃·수동 보류.
- 고유 스킬 대가로 자동 적용되는 의무 능력치 하향.
- 숨은 상시 보너스나 숨은 패시브.
- 원본 병종과 완전히 다른 기본 공격·전선 역할·이동 구조.
- 이름 지정 영웅별 신규 AI 아키텍처.
- 기본적으로 새 리그·전체 애니메이션 세트를 요구하는 설계.
- 전역 활성 1명 제한 제거를 이 Decision에 포함하는 것.
- 정확 수치와 구현·simulation을 실행 전에 완료로 표시.

## 12. 후속 결정

- 초기 다섯 영웅의 고유 스킬 전술 콘셉트.
- 고유 스킬의 공통 cooldown·charge 정책.
- 스킬 임팩트의 최소 VFX/SFX 기준.
- 영웅 간 선택률과 허용 강화 폭.
- 해금 순서와 메타 진행 배치.

## 13. 구현 경계

```text
USER_APPROVED = TRUE
GITHUB_AUTHORITY = THIS_DOCUMENT
HERO_POWER_MODEL = CONSTRAINED_UPGRADE
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
UNIQUE_AUTOMATIC_ACTIVE_SKILL_COUNT = 1_PER_HERO
MANDATORY_COMPENSATION_AXIS_COUNT = 0
GLOBAL_ACTIVE_NAMED_HERO_CAP = 1
PRODUCT_IMPLEMENTED = FALSE
EXACT_SKILLS = PENDING
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
