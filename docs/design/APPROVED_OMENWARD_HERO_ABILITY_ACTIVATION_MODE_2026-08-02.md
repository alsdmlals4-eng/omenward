# 오멘워드 영웅 능력 자동 발동 승인 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
approved_at: 2026-08-02 19:26 KST
approval: USER_APPROVED_RECOMMENDED_OPTION
status: USER_APPROVED / CURRENT_BRANCH_SYNCED / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

이름 지정 영웅의 기본 공격과 전투 능력은 규칙 기반으로 자동 발동한다. 플레이어는 전투 중 스킬 버튼을 누르거나 타깃을 직접 지정하지 않는다. 플레이어의 통제는 영웅 선택, 전선 배치, 병력 조합, 건물·룰렛 운영과 발동 조건 조성에 둔다.

```text
전투 상태 갱신
→ 공개된 발동 조건 평가
→ 공개된 능력 우선순위 평가
→ 공개된 대상 우선순위와 동률 해소 규칙 적용
→ 유효 대상·비용·쿨다운·충전 재검증
→ 능력 자동 시작
→ 결과·쿨다운·충전·고유 자원 기록
```

## 2. 플레이어 조작 경계

허용:

- 원본 `[영웅]` 등급 병종 또는 이름 지정 영웅 선택.
- 영웅을 배치할 전선 선택.
- 영웅의 고점 조건을 만들 병력·건물·적 대응 조합 구성.
- 공개된 발동 조건과 대상 우선순위를 보고 배치 시점 판단.

금지:

- 영웅 능력 수동 발동 버튼.
- 수동 타깃 지정·드래그·조준.
- 능력 발동 직전 수동 취소 또는 보류.
- 자동 판단을 우회하는 숨은 명령 큐.
- 영웅마다 자동·수동·혼합 방식을 임의로 섞는 예외.

## 3. 능력 계약 필수 필드

모든 영웅 전투 능력은 최소 다음을 정의한다.

```yaml
ability_id:
activation_mode: AUTOMATIC_RULE_BASED
trigger_conditions: []
ability_priority:
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

- 조건과 우선순위는 사용자에게 이해 가능한 언어로 공개한다.
- 동률 해소는 거리, 전선 진행도, 생성 순서, 고정 ID 등 결정론적 기준을 사용한다.
- 무작위 타깃 선택이 필요하면 별도 승인된 seed와 로그가 없는 한 사용하지 않는다.
- 능력 시작 전 대상·비용·충전·쿨다운을 다시 검증한다.
- 대상이 사라졌을 때의 취소·재탐색·비용 소비 여부를 능력별로 명시한다.

## 4. 다중 능력 우선순위

한 영웅의 여러 능력이 동시에 준비되면 고정된 `ability_priority` 순서로 평가한다.

```text
높은 우선순위 능력의 모든 조건 충족
→ 해당 능력 시작

높은 우선순위 능력의 조건 불충족
→ 다음 우선순위 능력 평가
```

- 우선순위는 숨기지 않는다.
- 같은 combat tick에 복수 능력을 동시에 시작하지 않는다.
- 능력 하나가 시작되면 다른 능력은 다음 합법 평가 시점까지 대기한다.
- 영웅별 우선순위 변경은 명시적 상태 효과나 능력 계약이 없으면 허용하지 않는다.

## 5. 결정론·저장·Stage 경계

- 동일한 저장 상태와 동일한 입력 순서에서는 같은 능력·대상·결과를 선택해야 한다.
- 저장·불러오기·Retry로 발동 순서, 대상 우선순위, 쿨다운 또는 충전을 다시 굴리지 않는다.
- 살아 있는 영웅의 남은 쿨다운·충전·고유 자원은 기존 Stage 지속 계약을 따른다.
- MaintenancePhase에서는 영웅 쿨다운·충전·고유 자원 clock이 진행되지 않는다.
- Stage 정산 시 진행 중 시전·타깃·일시 파생 개체는 기존 상태 정리 계약을 따른다.
- 사망한 영웅의 능력 상태는 새 인스턴스에 승계하지 않는다.

## 6. 전투 예산과 약점

자동 발동은 이름 지정 영웅의 조건부 전문화 sidegrade 계약을 약화하지 않는다.

- 좋은 조건을 플레이어가 조성했을 때 높은 고점이 나타나야 한다.
- 조건이 맞지 않으면 능력이 늦게 발동하거나 덜 적합한 대상을 선택하는 위험이 존재할 수 있다.
- 단, 비효율은 숨은 오작동이 아니라 공개된 조건·우선순위·약점에서 예측 가능해야 한다.
- 자동 발동 편의성 자체를 무료 전투력으로 계산하지 않는다.
- 수동 조작 숙련도나 APM을 전투 예산의 숨은 조건으로 사용하지 않는다.

주 책임 원본:

- 전투 예산·조건부 고점·약점: `APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`
- Stage 상태 지속: `APPROVED_OMENWARD_HERO_STAGE_STATE_PERSISTENCE_2026-08-02.md`
- 토큰 변환·배치: `APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md`

## 7. UX 요구

배치·비교 화면에는 다음을 제공한다.

- 자동 발동 표기.
- 핵심 발동 조건.
- 대상 우선순위.
- 능력 우선순위.
- 고점 조건과 명시적 약점.
- 현재 전선에서 조건 충족 가능성을 판단할 정보.

전투 중에는 다음을 제공한다.

- 발동 전 예고 애니메이션·아이콘·범위 표시.
- 실제 선택 대상 표시.
- 발동 실패·취소·대상 상실의 짧은 원인 로그.
- 쿨다운·충전·고유 자원 상태 표시.

## 8. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 자동 능력이 숨은 조건 때문에 멋대로 작동한다 | 유효 | 조건·대상·우선순위 공개 의무 |
| 능력 둘이 동시에 준비되어 비결정적으로 선택된다 | 유효 | 고정 ability_priority와 tie-break |
| 저장 후 더 좋은 대상이 나올 때까지 재로드한다 | 유효 | 저장 상태·입력 순서 기반 결정론 유지 |
| 자동 발동이 잘못된 대상에 낭비되어 통제감이 없다 | 유효 | 타깃 필터·우선순위·예고·원인 로그 제공 |
| 수동 궁극기만 예외로 추가되어 APM 게임이 된다 | 유효 | 모든 이름 지정 영웅 능력에 동일 자동 규칙 적용 |
| 자동 편의성과 전투 능력을 함께 받아 순수 상위호환이 된다 | 유효 | 다축 전투 예산·명시적 약점 계약 유지 |
| 고점 조건이 자동으로 항상 충족된다 | 유효 | encounter matrix와 조건 충족률 simulation 필요 |

## 9. 미확정 항목

- 영웅별 능력 명단·정확 트리거·우선순위·수치.
- combat tick과 능력 평가 주기.
- 무작위가 필요한 능력의 seed 정책.
- 정확한 예고 시간·로그 문구·접근성 표현.
- 자동 판단 UX·결정론·저장 복구 runtime test.

## 10. 상태 경계

```text
ABILITY_ACTIVATION = AUTOMATIC_RULE_BASED
MANUAL_SKILL_BUTTON = FORBIDDEN
MANUAL_TARGETING = FORBIDDEN
TRIGGER_AND_PRIORITY_DISCLOSURE = REQUIRED
DETERMINISTIC_TIE_BREAK = REQUIRED
SAVE_REROLL = FORBIDDEN
EXACT_ABILITIES_AND_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
PRODUCT_CODE = UNCHANGED
```
