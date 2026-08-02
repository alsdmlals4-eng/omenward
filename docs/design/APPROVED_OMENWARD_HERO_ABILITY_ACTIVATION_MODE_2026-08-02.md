# 오멘워드 영웅 능력 자동 발동 승인 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
approved_at: 2026-08-02 19:26 KST
status: MERGED_USER_APPROVED / NOT_IMPLEMENTED
current_specialization: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-KIT-STRUCTURE-V1
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정

이름 지정 영웅의 영웅 전용 `[사용스킬]`은 규칙 기반으로 자동 발동한다. 플레이어는 전투 중 스킬 버튼을 누르거나 타깃을 직접 지정하지 않는다.

```text
전투 상태 갱신
→ 공개 trigger 평가
→ 공개 target filter·priority·tie-break 적용
→ 대상·비용·cooldown·charge 재검증
→ 자동 발동
→ 결과 상태 기록
```

## 2. 현재 단일 차이 구조와의 관계

현재 이름 지정 영웅은 기존 병종 `[영웅]` 등급 유닛의 스킨형 변주이며 영웅 전용 차이는 정확히 하나다.

```text
PASSIVE_TYPE
XOR
AUTOMATIC_ACTIVE_SKILL_TYPE
```

- 패시브형 영웅은 영웅 전용 사용스킬이 없다.
- 사용스킬형 영웅은 영웅 전용 패시브가 없다.
- 사용스킬형의 단 하나의 영웅 전용 능력에 이 자동 발동 계약을 적용한다.
- 원본 병종에서 계승한 기본 공격·일반 AI 기능은 영웅 전용 차이 슬롯으로 계산하지 않는다.
- 영웅 전용 다중 능력 우선순위는 현재 구조에서 발생하지 않는다.

## 3. 플레이어 조작 경계

허용:

- 원본 `[영웅]` 등급 병종 또는 이름 지정 영웅 선택.
- 배치 전선 선택.
- 패시브 또는 자동 사용스킬의 유리한 조건을 만들 조합·배치·건물·룰렛 운영.
- 공개 trigger와 대상 규칙을 보고 배치 시점 판단.

금지:

- 영웅 능력 수동 발동 버튼.
- 수동 타깃 지정·드래그·조준.
- 발동 직전 수동 취소·보류.
- 자동 판단을 우회하는 숨은 명령 큐.
- 영웅별 자동·수동·혼합 입력 방식.

## 4. 자동 사용스킬 필수 필드

```yaml
ability_id:
activation_mode: AUTOMATIC_RULE_BASED
trigger_conditions: []
target_filter:
target_priority:
tie_break_rule:
precast_tell:
cast_or_windup_time:
interrupt_policy:
resource_cost:
charge_policy:
cooldown_policy:
invalid_target_policy:
stage_persistence_scope:
```

- 조건·대상·동률 해소는 사용자에게 이해 가능한 언어로 공개한다.
- 동률 해소는 거리·전선 진행도·생성 순서·고정 ID 등 결정론적 기준을 사용한다.
- 시작 전 대상·비용·charge·cooldown을 다시 검증한다.
- 대상 상실 시 취소·재탐색·비용 소비 여부를 명시한다.

## 5. 결정론·저장·Stage 경계

- 동일 저장 상태와 동일 입력 순서는 같은 능력·대상·결과를 만든다.
- 저장·불러오기·Retry로 발동 순서·대상·cooldown·charge를 재굴림하지 않는다.
- 생존 영웅의 남은 cooldown·charge는 Stage 지속 계약을 따른다.
- MaintenancePhase에서는 영웅 clock이 진행되지 않는다.
- 사망한 영웅의 능력 상태는 새 인스턴스에 승계하지 않는다.

## 6. 전투 예산

- 자동 사용스킬은 무료 전투력이 아니다.
- 사용스킬의 가치는 기본 스탯·안정성·범용성에서 상쇄한다.
- 패시브형과 사용스킬형 모두 원본 병종이 더 좋은 상황을 유지한다.
- 자동 비효율은 숨은 오작동이 아니라 공개된 trigger·대상 규칙·약점에서 예측 가능해야 한다.
- 수동 조작 숙련도나 APM을 전투 예산의 숨은 조건으로 사용하지 않는다.

## 7. UX 요구

배치·비교 화면:

- `패시브형` 또는 `자동 사용스킬형` 표시.
- 원본 병종과 동일한 핵심 역할.
- 바뀌는 단 하나의 규칙.
- 사용스킬형의 trigger·target priority·cooldown 또는 charge.
- 고점 조건·상쇄·원본 병종 선택 사유.

전투 중:

- 발동 전 예고·범위·선택 대상 표시.
- 발동 실패·취소·대상 상실 원인 로그.
- cooldown·charge 표시.

## 8. 금지

- 사용스킬형에 추가 영웅 전용 패시브 제공.
- 둘 이상의 영웅 전용 사용스킬.
- 수동 궁극기·수동 타깃.
- 숨은 trigger·대상 규칙·무작위 동률 해소.
- save/retry 재굴림.
- 새 AI 아키텍처를 요구하는 영웅별 예외.

## 9. 구현 경계

```text
ABILITY_ACTIVATION = AUTOMATIC_RULE_BASED
HERO_SIGNATURE_ACTIVE_COUNT = MAX_1
HERO_SIGNATURE_PASSIVE_AND_ACTIVE = MUTUALLY_EXCLUSIVE
MANUAL_SKILL_BUTTON = FORBIDDEN
MANUAL_TARGETING = FORBIDDEN
SAVE_REROLL = FORBIDDEN
EXACT_ABILITIES_AND_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
PRODUCT_CODE = UNCHANGED
```
