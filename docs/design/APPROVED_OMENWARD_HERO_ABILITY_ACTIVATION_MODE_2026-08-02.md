# 오멘워드 해금 영웅 고유 스킬 자동 발동 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
approved_at: 2026-08-02 19:26 KST
refined_at: 2026-08-02 22:29 KST
status: MERGED_USER_APPROVED / REFINED_BY_UNIQUE_SKILL_UPGRADE_MODEL / NOT_IMPLEMENTED
current_specialization: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

모든 해금 이름 지정 영웅은 영웅 전용 고유 `[사용스킬]` 하나를 가지며 규칙 기반으로 자동 발동한다.

```text
전투 상태 갱신
→ 공개 trigger 평가
→ target filter·priority·tie-break 적용
→ 대상·cooldown 또는 charge 재검증
→ 고유 스킬 자동 발동
→ 상태와 전투 로그 기록
```

```text
EVERY_NAMED_HERO_HAS_UNIQUE_ACTIVE_SKILL = TRUE
UNIQUE_ACTIVE_SKILL_COUNT_PER_HERO = 1
HERO_EXCLUSIVE_PASSIVE_COUNT = 0
MANUAL_ACTIVATION = FALSE
```

## 2. 자동 발동 필수 필드

각 스킬은 다음을 명시한다.

- 발동 trigger.
- 대상 후보 조건.
- 대상 우선순위.
- 동률 tie-break.
- cooldown 또는 charge 규칙.
- 유효 대상이 없을 때의 처리.
- 발동 직전 재검증.
- 저장·재시도 시 결정론을 유지하는 상태.
- 식별 가능한 VFX/SFX와 전투 로그.

## 3. 플레이어 통제

플레이어는 스킬 버튼이나 직접 타기팅을 사용하지 않는다. 대신 다음 정보를 사전에 확인한다.

- 스킬이 발동할 조건.
- 예상 대상 범주.
- 현재 cooldown 또는 charge.
- 다음 발동 가능성.
- 전역 활성 이름 지정 영웅 `1/1` 상태.

자동 발동은 숨은 랜덤이 아니라 공개 규칙에 따른 예측 가능한 전술 시스템이어야 한다.

## 4. 결정론

```text
동일 저장 상태
+ 동일 전투 입력 순서
= 동일 trigger 판정·대상·발동 결과
```

- tie-break 마지막 단계는 stable ID 또는 저장되는 결정론적 순서를 사용한다.
- 저장·Retry로 대상이나 발동 여부를 재굴림할 수 없다.
- cooldown·charge·선택 대상에 영향을 주는 상태를 저장한다.

## 5. 상위호환과 스킬 예산

고유 스킬은 원본 `[영웅]` 등급 유닛에 추가되는 해금 보상이다.

- 강제 능력치 하향이나 상쇄 축을 요구하지 않는다.
- 밸런스는 trigger·cooldown·charge·효과 범위·대상 조건과 전역 활성 1명 제한으로 조정한다.
- 스킬은 원본 역할을 강화하되 다른 병종 역할을 완전히 대체하지 않는다.
- 고유 스킬의 발동 순간은 전투 결과와 연출에서 분명한 임팩트를 가져야 한다.

## 6. 금지

- 영웅 전용 패시브.
- 한 영웅의 독립 고유 스킬 두 개 이상.
- 수동 스킬 버튼·수동 타깃·수동 보류.
- 숨은 무작위 타깃 선택.
- 저장·Retry 재굴림.
- 원본 병종과 무관한 새 AI 아키텍처.
- 정확 trigger·cooldown·효과를 검증 전에 완료로 표시.

## 7. 초기 5명

```text
shield_guard = AUTOMATIC_UNIQUE_SKILL
archer       = AUTOMATIC_UNIQUE_SKILL
priest       = AUTOMATIC_UNIQUE_SKILL
mage         = AUTOMATIC_UNIQUE_SKILL
assassin     = AUTOMATIC_UNIQUE_SKILL
```

## 8. 구현 경계

```text
CURRENT_AUTHORITY = OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUE-SKILL-UPGRADE-MODEL-V1
PRODUCT_CODE = UNCHANGED
EXACT_SKILLS = PENDING
EXACT_TRIGGERS = PENDING
EXACT_COOLDOWNS = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
