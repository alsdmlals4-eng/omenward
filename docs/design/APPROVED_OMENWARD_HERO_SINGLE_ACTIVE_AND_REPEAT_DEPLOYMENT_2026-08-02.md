# 오멘워드 영웅 단일 활성·반복 출전 승인 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1
approved_at: 2026-08-02 16:24 KST
approval: USER_DIRECT_APPROVAL
status: USER_APPROVED_SINGLE_ACTIVE_LIMIT / EXIT_RULE_PENDING / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

한 MapRun의 전장 전체에는 **출전 중인 `[영웅]` 유닛이 동시에 정확히 최대 1명**만 존재할 수 있다. 제한 대상은 영웅의 이름이나 병종이 아니라 현재 전장에 활성 상태로 존재하는 모든 영웅 유닛의 합계다.

```text
ACTIVE_HERO_UNIT_COUNT_ACROSS_ALL_LANES <= 1
```

동일한 이름과 `hero_id`를 가진 영웅도 한 MapRun에서 여러 번 배치할 수 있다. 다만 이전 영웅이 더 이상 출전 중이 아닌 상태에서, 새로운 동병종 `[영웅]` 등급 토큰을 다시 소비해야 한다.

## 2. 동시 활성 제한

- 상·중·하 전선을 합쳐 출전 중인 영웅 유닛은 최대 1명이다.
- 현재 영웅의 병종·이름·배치 전선과 무관하게 전역 단일 슬롯을 공유한다.
- 서로 다른 영웅도 동시에 둘 이상 출전할 수 없다.
- 같은 영웅의 여러 복제 인스턴스도 동시에 존재할 수 없다.
- 이 제한은 일반 유닛과 원본 `[영웅]` 등급 병종 유닛에는 적용하지 않는다. 이름이 지정된 해금 영웅으로 변환된 유닛만 `active hero`로 계산한다.

## 3. 동일 영웅 반복 출전

```text
현재 active hero 없음
+ 새 동병종 [영웅] 등급 토큰 1개
+ 해당 hero_id 해금 상태
→ 같은 영웅을 다시 선택·변환·배치 가능
```

- 동일 `hero_id`의 한 런 중 반복 출전을 허용한다.
- 반복 출전마다 별도의 `[영웅]` 등급 토큰 1개를 소비한다.
- 이전 영웅 인스턴스가 전장에 남아 있는 동안에는 같은 영웅을 다시 배치할 수 없다.
- 이전 출전 횟수는 새 배치를 영구 차단하지 않는다.
- 반복 출전은 이전 인스턴스의 체력·상태·누적 효과를 복제하거나 승계한다는 뜻이 아니다. 정확한 초기 상태 계약은 후속 수치·영웅 능력 결정 대상이다.

## 4. 활성 영웅이 있을 때의 보관 토큰

활성 영웅이 존재하는 동안 새 `[영웅]` 등급 병종 토큰을 얻어도 룰렛 결과 자체는 무효화하지 않는다.

플레이어는 다음 중 하나를 선택할 수 있다.

1. 토큰을 보관함에 유지하고 active hero 슬롯이 비워질 때까지 영웅 변환을 보류한다.
2. 해금 영웅으로 변환하지 않고 원본 `[영웅]` 등급 병종 유닛으로 배치한다.

금지:

- 기존 영웅을 자동 삭제하고 새 영웅으로 강제 교체.
- 두 번째 영웅을 임시·대기·소환 상태로 전장에 동시에 존재시킴.
- active hero 제한 때문에 획득한 토큰 자체를 소멸시킴.
- 이름만 다른 영웅으로 바꾸어 단일 활성 제한을 우회함.

## 5. active 상태 경계

`active hero`는 이름이 지정된 해금 영웅으로 변환되어 전장 유닛 인스턴스로 존재하는 상태다.

```text
active_hero_unit_instance_id != null
→ 다른 영웅 변환·배치 차단

active_hero_unit_instance_id == null
→ 동병종 해금 영웅 변환·배치 가능
```

현재 영웅이 사망하거나 전장에서 완전히 제거되어 더 이상 출전 중이 아니면 단일 활성 슬롯은 비워진다. 수동 퇴각·교대·Stage 종료 유지·자동 귀환의 허용 여부와 정확한 제거 이벤트는 다음 Decision에서 확정한다.

## 6. 기존 토큰 변환 계약과의 결합

```text
ONE_HERO_GRADE_TOKEN
→ 원본 영웅 등급 병종 유닛 1개
OR
→ active slot이 비어 있을 때 해금 영웅 유닛 1개
```

- 영웅 변환은 여전히 `1토큰 → 1유닛`이다.
- 반복 출전도 보너스 영웅을 생성하지 않는다.
- active slot이 차 있어도 원본 병종 선택은 차단하지 않는다.
- 변환 후보는 토큰과 같은 `UnitArchetype`의 해금 영웅만 표시한다.
- 전선 배치 확정 뒤 undo·회수·판매·라인 이동 불가 원칙은 유지한다.

## 7. 데이터·원자성 책임

```yaml
HeroBattlefieldState:
  active_hero_unit_instance_id
  active_hero_id
  active_hero_lane_id
  hero_deployment_history

HeroDeploymentRecord:
  deployment_id
  source_token_instance_id
  hero_id
  unit_instance_id
  lane_id
  deployed_at_stage
  ended_reason
```

- `active_hero_unit_instance_id` 확인과 토큰 변환·전선 배치는 하나의 원자적 transaction이어야 한다.
- 동시 입력·재시도·저장 복구로 두 영웅이 동시에 생성되지 않게 한다.
- active 영웅 제거 시 슬롯 해제와 종료 기록을 같은 transaction으로 처리한다.
- `hero_deployment_history`는 반복 출전을 허용하되 동시 활성 판정에 사용하지 않는다.

## 8. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 같은 영웅 반복 출전이 복제 설정과 충돌한다 | 사용자 승인 우선 | 고유성 제한이 아니라 동시 활성 1명 규칙으로 정의 |
| 강한 영웅 하나만 계속 재배치하는 지배 전략이 생긴다 | 유효 | 매번 영웅 등급 토큰 소비·능력/출현 빈도 simulation 필요 |
| 영웅이 살아 있는 동안 새 영웅 토큰이 쓸모없다 | 유효 | 보관 유지 또는 원본 영웅 등급 병종 배치 허용 |
| 다른 전선에 영웅을 추가해 제한을 우회한다 | 유효 | 세 전선 전체가 하나의 active hero 슬롯 공유 |
| 저장·동시 입력으로 영웅 둘이 생긴다 | 유효 | active slot 검증과 배치를 원자 transaction으로 처리 |
| 기존 영웅을 언제 제거할 수 있는지 모호하다 | 유효 | 수동 퇴각·교대·Stage 유지 규칙을 다음 Gate로 분리 |
| 사망한 영웅의 패시브가 계속 누적된다 | 유효 | active 상태 종료 시 해당 인스턴스의 전장 효과 종료; 지속 효과 예외는 별도 명시 필요 |

## 9. 미확정 항목

- 영웅의 수동 퇴각·교대 허용 여부.
- 영웅이 Stage 사이에 계속 남는지, Act/Stage 종료 시 처리.
- 사망 외에 active 슬롯을 비우는 정확한 이벤트.
- 반복 출전 시 체력·쿨다운·능력 초기화 계약.
- 영웅 등급 토큰의 출현 빈도와 영웅 능력·수치.
- 보관함의 active slot 표시와 교체 불가 피드백.

## 10. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-EXIT-AND-REPLACEMENT-V1
= 현재 영웅이 살아 있을 때 수동 교대·퇴각을 허용하는가, 영웅은 어떤 사건에서 active 상태를 종료하는가
```

## 11. 상태 경계

```text
DESIGN: USER_APPROVED_SINGLE_ACTIVE_HERO
SAME_HERO_REPEAT_DEPLOYMENT: ALLOWED
SIMULTANEOUS_ACTIVE_HEROES: MAX_1
EXIT_AND_REPLACEMENT: PENDING
EXACT_VALUES: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
```
