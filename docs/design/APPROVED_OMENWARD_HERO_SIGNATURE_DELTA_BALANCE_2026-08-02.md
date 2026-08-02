# OMENWARD 이름 지정 영웅 단일 상쇄 축 과거 결정

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-SIGNATURE-DELTA-BALANCE-V1
approved_at: 2026-08-02 21:28 KST
superseded_at: 2026-08-02 22:29 KST
status: USER_APPROVED_HISTORY / SUPERSEDED_BY_UNIQUE_SKILL_UPGRADE_MODEL / NOT_IMPLEMENTED
superseded_by: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
product_code_authority: NONE
```

## 1. 과거 결정

이 문서는 이름 지정 영웅의 단일 차이와 직접 관련된 상쇄 축 하나를 의무화했던 과거 결정을 보존한다.

```text
과거 모델
= PASSIVE OR AUTOMATIC_ACTIVE_SKILL
+ COMPENSATION_AXIS_COUNT 1
+ SIDEGRADE
```

## 2. 폐기된 항목

최신 사용자 결정에 따라 다음은 현행 정본이 아니다.

```text
COMPENSATION_AXIS_REQUIRED = SUPERSEDED
BASELINE_NERF_REQUIRED = SUPERSEDED
ORIGINAL_UNIT_PICK_CASE_REQUIRED_BY_WEAKNESS = SUPERSEDED
PASSIVE_VARIANT = SUPERSEDED
```

- 고유 스킬 추가 대가로 공격력·체력·방어력·사거리·지원 효율을 의무적으로 낮추지 않는다.
- 이름 지정 영웅은 원본 `[영웅]` 등급 유닛보다 조금 더 강하고 임팩트 있는 해금 보상으로 설계한다.
- 모든 영웅은 패시브가 아니라 고유 자동 사용스킬 하나를 가진다.

## 3. 현행 책임 원본

`APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md`

현행 모델:

```text
원본 [영웅] 등급 유닛 기본 성능 계승
+ 고유 자동 사용스킬 1개
+ 강제 상쇄 없음
+ 전역 활성 이름 지정 영웅 최대 1명
= 제한형 상위호환
```

## 4. 유지되는 검증 교훈

과거 적대적 검토 중 다음 교훈은 계속 유효하다.

- 정확 수치와 평균 전투 기여는 simulation 전까지 확정하지 않는다.
- 고유 스킬의 파생 효과를 총 전투 예산에 포함한다.
- 특정 이름 지정 영웅이 모든 콘텐츠의 유일한 정답이 되지 않는지 검증한다.
- 영웅 간 선택률·조건 충족률·고점·cooldown 공백을 비교한다.
- 제품 구현 완료를 문서 승인과 혼동하지 않는다.

## 5. 금지

- 이 문서의 상쇄 축 규칙을 현행 설계에 다시 적용.
- 이전 `패시브 XOR 자동 사용스킬` 구조를 현행으로 해석.
- 과거 Decision을 삭제해 계보를 잃는 것.
- 정확 simulation 없이 강화 폭이 안전하다고 주장.

## 6. 상태 경계

```text
HISTORICAL_DECISION = TRUE
CURRENT_AUTHORITY = OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
MANDATORY_COMPENSATION_AXIS_COUNT = 0
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
PRODUCT_IMPLEMENTED = FALSE
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
