# OMENWARD 이름 지정 영웅 단일 고유 스킬 구조 승인안

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1
approved_at: 2026-08-02 21:08 KST
refined_at: 2026-08-02 22:29 KST
approval: USER_DIRECT_REFINEMENT
status: USER_APPROVED / REFINED_BY_UNIQUE_SKILL_UPGRADE_MODEL / NOT_IMPLEMENTED
scope: GAMEPLAY_HERO_SINGLE_UNIQUE_SKILL_KIT
current_authority: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
product_code_authority: NONE
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 현행 결정

이름 지정 영웅은 연결된 원본 병종 `[영웅]` 등급 유닛의 기본 전투 구조를 재사용하고, 영웅 전용 고유 자동 사용스킬 하나를 추가한다.

```text
원본 병종 [영웅] 등급 유닛
+ 이름·초상·스킨·최소 식별 연출
+ 고유 자동 사용스킬 정확히 1개
= 해금 이름 지정 영웅
```

```text
UNIQUE_AUTOMATIC_ACTIVE_SKILL_COUNT = 1
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
SOURCE_BASELINE_INHERITED = TRUE
```

이전의 `패시브 XOR 자동 사용스킬` 구조는 폐기됐다. 모든 해금 영웅은 사용스킬형으로 고정한다.

## 2. 원본 병종 계승

다음을 원본 `[영웅]` 등급 유닛에서 우선 재사용한다.

- 핵심 역할·전선 포지션.
- 기본 공격 방식·사거리·공격 주기·대상 범주.
- 이동·충돌·배치 규칙.
- 기본 스탯 구조와 성장 곡선.
- 기본 AI와 대상 탐색 구조.
- 리그·이동·기본 공격·피격·사망 애니메이션.
- Stage·사망·재출전·저장 규칙.

영웅 전용 신규 제작은 이름·초상·스킨·장비 또는 실루엣 변주·고유 스킬 VFX/SFX에 집중한다.

## 3. 고유 스킬 슬롯

```text
SOURCE_BASIC_COMBAT
+ ONE_UNIQUE_AUTOMATIC_ACTIVE_SKILL
```

고유 스킬은 다음을 공개한다.

- trigger.
- target filter.
- target priority.
- deterministic tie-break.
- cooldown 또는 charge.
- effect.
- 유효 대상이 없을 때의 처리.
- 식별 가능한 VFX/SFX.

수동 스킬 버튼·수동 타깃·수동 보류는 허용하지 않는다.

## 4. 상위호환 방향

이름 지정 영웅은 원본 병종보다 조금 더 강하고 임팩트 있는 해금 보상이다.

```text
SOURCE_HERO_GRADE_BASELINE
+ UNIQUE_SKILL_VALUE
= CONSTRAINED_UPGRADE
```

- 고유 스킬 추가 대가로 기본 능력치를 의무적으로 낮추지 않는다.
- 전역 활성 이름 지정 영웅 최대 1명 제한을 유지한다.
- 해금 전·다른 이름 지정 영웅 활성 중에는 원본 `[영웅]` 등급 유닛이 계속 필요하다.
- 정확 강화 폭은 후속 simulation 전까지 미확정이다.

## 5. 스킨형 제작 범위

```text
NEW_FULL_RIG = NOT_REQUIRED_BY_DEFAULT
NEW_FULL_ANIMATION_SET = NOT_REQUIRED_BY_DEFAULT
NEW_AI_ARCHITECTURE = FORBIDDEN_BY_DEFAULT
UNIQUE_VOICE_PACK = NOT_REQUIRED_BY_DEFAULT
```

단순 색상 변경만으로 끝내지 않으며, 초상·실루엣·장비·스킬 연출 중 최소 두 축에서 원본과 구분한다.

## 6. 데이터 계약 방향

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
  source_baseline_inherited: true
  hero_exclusive_passive: null
```

불변식:

```text
unique_active_skill_count == 1
hero_exclusive_passive_count == 0
source_baseline_inherited == true
manual_activation == false
```

## 7. UX 요구

```text
원본 [영웅] 등급 = 병종의 기본 최고 등급
해금 이름 지정 영웅 = 동일 기본 성능 + 고유 자동 사용스킬 1개
```

영웅 카드에는 고유 스킬 이름·발동 조건·효과·cooldown 또는 charge·자동 발동·전역 활성 `1/1` 상태를 표시한다.

## 8. 적대적 검토

- 고유 스킬이 너무 약해 해금 보상이 느껴지지 않으면 실패다.
- 고유 스킬 안에 둘 이상의 독립 능력을 숨기면 실패다.
- 패시브나 숨은 상시 보너스를 추가하면 실패다.
- 영웅별 새 AI·리그·전체 애니메이션을 요구하면 제작량 계약 위반이다.
- 특정 영웅이 모든 전선·Stage에서 유일한 정답이 되면 스킬 예산 또는 콘텐츠 대응을 조정한다.

## 9. 금지

- 영웅 전용 패시브.
- 고유 스킬 두 개 이상.
- 수동 발동·수동 타깃·수동 보류.
- 의무적인 능력치 하향 또는 강제 상쇄 축.
- 원본 병종과 완전히 다른 기본 공격·전선 역할·이동 구조.
- 이름 지정 영웅별 신규 AI 아키텍처.
- 정확 수치·구현·simulation을 실행 전에 완료로 표시.

## 10. 구현 경계

```text
CURRENT_AUTHORITY = APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md
HERO_POWER_MODEL = CONSTRAINED_UPGRADE
UNIQUE_AUTOMATIC_ACTIVE_SKILL_COUNT = 1_PER_HERO
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
PRODUCT_IMPLEMENTED = FALSE
EXACT_SKILLS = PENDING
EXACT_VALUES = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
