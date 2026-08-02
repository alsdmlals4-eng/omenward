# 오멘워드 해금 영웅 전투 예산·제한형 상위호환 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1
approved_at: 2026-08-02 19:05 KST
refined_at: 2026-08-02 22:29 KST
status: MERGED_USER_APPROVED / REFINED_BY_UNIQUE_SKILL_UPGRADE_MODEL / NOT_IMPLEMENTED
current_authority: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
product_code_authority: NONE
exact_values: PENDING
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 현행 결정

이름 지정 영웅은 원본 `[영웅]` 등급 유닛보다 조금 더 강하고 임팩트 있는 해금 보상이다.

```text
원본 [영웅] 등급 기본 전투 성능
+ 고유 자동 사용스킬 1개
= 제한형 상위호환 이름 지정 영웅
```

```text
HERO_POWER_MODEL = CONSTRAINED_UPGRADE
SOURCE_BASELINE_STATS = INHERITED
UNIQUE_AUTOMATIC_ACTIVE_SKILL_COUNT = 1
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
MANDATORY_COMPENSATION_AXIS_COUNT = 0
```

이전의 평균 예산 동등 sidegrade·강제 상쇄 축 모델은 현행 정본이 아니다.

## 2. 전투력 통제 방식

상위호환은 원본 능력치 하향이 아니라 다음 제한으로 통제한다.

- 세 전선 전체 활성 이름 지정 영웅 최대 1명.
- 영구 해금 필요.
- 연결 병종 `[영웅]` 등급 토큰 필요.
- 비가역 전선 배치.
- 수동 퇴각·교대·판매·재보관·전선 이동 금지.
- 고유 스킬 cooldown 또는 charge.
- 공개 trigger·대상 우선순위·결정론적 tie-break.

원본 `[영웅]` 등급 유닛은 미해금 상태와 다른 이름 지정 영웅이 전역 슬롯을 점유한 상태에서 계속 사용된다.

## 3. 허용되는 강화

- 원본 역할을 강화하는 순간 고점.
- 원본 타기팅 문법을 활용한 추가 공격·보호·치유·제어.
- 적절한 cooldown 또는 charge를 가진 인상적인 자동 스킬.
- 전투 결과와 VFX/SFX에서 즉시 체감되는 해금 보상.

정확 강화 폭은 각 고유 스킬의 역할 가치로 산정한다. 모든 영웅에게 동일한 공격력 배율을 주지 않는다.

## 4. 금지되는 강화

- 영웅 전용 패시브 또는 숨은 상시 보너스.
- 고유 스킬 두 개 이상.
- 원본 기본 스탯과 성장 곡선 전체 재설계.
- 원본 병종과 완전히 다른 기본 공격·사거리·전선 역할.
- 수동 궁극기·수동 타깃.
- 새 AI 아키텍처나 전체 신규 애니메이션 세트를 기본 요구.
- 모든 전선·Stage에서 한 영웅이 유일한 정답이 되는 예산.

## 5. 검증 계약

각 영웅은 최소 다음을 검증한다.

1. 고유 스킬 발동 전·후 전투 기여.
2. cooldown 또는 charge 공백 구간.
3. 병종별 대표 타기팅 조건.
4. 다른 이름 지정 영웅과의 전역 슬롯 경쟁.
5. 원본 유닛만으로 콘텐츠 진행 가능성.
6. 영웅 미해금 상태와 해금 상태의 체감 차이.

측정 항목:

- 원본 대비 평균·고점 전투 기여.
- 고유 스킬 발동 빈도와 유효 적중률.
- 영웅 간 선택률.
- Stage·전선별 지배율.
- 해금 전후 난이도 변화.
- 신규 자산량과 제작 시간.

정확 허용 강화 폭·표본 수·선택률 목표는 아직 확정하지 않는다.

## 6. UX 책임

```text
원본 [영웅] 등급: 기본 최고 등급
해금 이름 지정 영웅: 동일 기본 성능 + 고유 자동 사용스킬 1개
```

- 고유 스킬 이름·효과·발동 조건·cooldown 또는 charge를 표시한다.
- 이름 지정 영웅이 더 강한 해금 보상임을 숨기지 않는다.
- 전역 활성 제한 `1/1`과 다른 영웅과의 경쟁을 명확히 표시한다.

## 7. 구현 경계

```text
CURRENT_AUTHORITY = APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md
TOTAL_COMBAT_BUDGET = SOURCE_BASELINE_PLUS_SIGNATURE_SKILL
HERO_POWER_MODEL = CONSTRAINED_UPGRADE
BASELINE_NERF_REQUIRED = FALSE
PRODUCT_CODE = UNCHANGED
EXACT_SKILLS = PENDING
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
