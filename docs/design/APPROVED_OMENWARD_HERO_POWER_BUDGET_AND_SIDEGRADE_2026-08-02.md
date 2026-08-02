# 오멘워드 해금 영웅 전투 예산·등급 계층 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1
approved_at: 2026-08-02 19:05 KST
refined_at: 2026-08-02 23:07 KST
status: MERGED_USER_APPROVED / REFINED_TO_GRADE_HIERARCHY / NOT_IMPLEMENTED
current_authority: OMW-DEC-20260802-GAMEPLAY-HERO-GRADE-SLOT-AND-UNLOCKED-SKILL-REPLACEMENT-V1
product_code_authority: NONE
exact_values: PENDING
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 현행 파워 계층

```text
표준 [영웅] 등급
< 해금 이름 지정 [영웅]
< 표준 [전설] 등급
```

```text
NAMED_HERO_POWER_FLOOR > STANDARD_HERO_POWER
NAMED_HERO_POWER_CEILING < STANDARD_LEGENDARY_POWER
```

- 해금 영웅은 표준 영웅보다 강하고 임팩트 있는 해금 보상이다.
- 해금 영웅은 표준 전설의 전체 전투 고점을 넘지 않는다.
- 정확 수치·허용 오차·역할별 가치 환산은 simulation 전까지 pending이다.

## 2. 키트 비교

```text
표준 [영웅]
= 강화된 1스킬 + 표준 2스킬

해금 이름 지정 [영웅]
= 강화된 1스킬 + 고유 2스킬

표준 [전설]
= 강화된 1스킬 + 강화된 표준 2스킬 + 표준 3스킬
```

- 해금 영웅은 표준 2스킬을 고유 2스킬로 교체한다.
- 표준 2스킬과 고유 2스킬을 동시에 보유하지 않는다.
- 추가 3번째 스킬 슬롯이나 영웅 전용 패시브는 없다.
- 기본 능력치 의무 하향·강제 상쇄 축은 없다.

## 3. 전역 슬롯과 전투 예산

```text
ACTIVE_UNIT_COUNT_WHERE_GRADE_IN(HERO, LEGENDARY) <= 1
```

표준 영웅·해금 영웅·표준 전설·향후 해금 전설이 같은 전역 슬롯을 사용한다. 이 제한은 파워를 직접 깎는 세금이 아니라 세 전선 중 어느 곳에 최고 등급을 투입할지 만드는 전략적 기회비용이다.

## 4. 고유 2스킬 임팩트 상한

고유 2스킬은 한 번의 발동으로 전선 국면을 바꿀 수 있다.

허용 예:

- 무너지는 전열을 일정 시간 안정화.
- 고가치 비행 위협을 신속 제거.
- 치명적 피해를 입은 아군 집단 복구.
- 밀집 공세를 분산·무력화.
- 적 후열의 핵심 지원 유닛 제거.

금지:

- 피해·제어·회복·소환을 모두 독립적으로 제공하는 복합 궁극기.
- 모든 공세 유형과 전선에서 같은 수준의 최고 효율.
- 표준 전설의 강화 2스킬+3스킬 전체보다 높은 평균·고점 기여.
- 영웅 고유 스킬만으로 건물·룰렛·전선 배치 판단을 무의미하게 만드는 효과.

## 5. 비교 검증

각 고유 2스킬은 같은 병종·같은 Stage·같은 전선 조건에서 다음을 비교한다.

1. 표준 영웅의 표준 2스킬 기여.
2. 해금 영웅의 고유 2스킬 기여.
3. 표준 전설의 강화 2스킬+3스킬 및 상위 기본 성능 기여.
4. 발동 전후 전선 유지시간·피해·회복·제어·목표 제거.
5. 전역 슬롯 점유시간과 다른 전선 기회비용.

```text
STANDARD_HERO < NAMED_HERO < STANDARD_LEGENDARY
```

위 순서를 대표 encounter와 장기 MapRun 모두에서 유지해야 한다.

## 6. 향후 해금 전설

```text
향후 해금 이름 지정 [전설]
= 강화된 1스킬 + 강화된 표준 2스킬 + 고유 3스킬
```

```text
FUTURE_NAMED_LEGENDARY_UNIQUE_SKILL_SLOT = 3
FUTURE_NAMED_LEGENDARY_IMPLEMENTATION = NOT_NOW
```

향후 해금 전설과 표준 전설의 정확 파워 관계는 별도 Decision에서 확정한다.

## 7. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 해금 영웅이 사실상 3스킬이라 전설을 침범한다 | 해소 | 표준 2스킬을 고유 2스킬로 교체, 추가 슬롯 금지 |
| 상위호환 때문에 표준 영웅이 무의미하다 | 의도된 수직 성장 | 미해금 상태 기본 진행 가능성 유지 |
| 고유 2스킬 한 번이 전설 전체 키트보다 강하다 | 유효 | 등급 비교 매트릭스·상한 simulation 필수 |
| 전역 슬롯이 파워 밸런스를 모두 해결한다 | 거짓 | 스킬 자체의 총 전투 가치와 콘텐츠 지배율 별도 검증 |
| 한 영웅이 모든 Stage의 유일한 정답이 된다 | 유효 | 병종별 조건·counter pressure·선택률 검증 |
| 전설 당첨이 슬롯 충돌로 손해처럼 느껴진다 | 유효 | 보관·판매 가치·UI·장기 슬롯 점유 검증 |

## 8. 구현 경계

```text
PRODUCT_CODE = UNCHANGED
EXACT_SKILLS = PENDING
EXACT_VALUES = PENDING
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
