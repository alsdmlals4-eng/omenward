# 오멘워드 영웅 재출전 초기 상태·사망 무회수 승인 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-REDEPLOYMENT-INITIAL-STATE-V1
approved_at: 2026-08-02 18:25 KST
approval: USER_APPROVED_RECOMMENDED_OPTION_WITH_NO_RECOVERY_REWARD_AND_POST_DEATH_ROLL_CLARIFICATION
status: USER_APPROVED_FRESH_INSTANCE / NO_DEATH_RECOVERY_REWARD / POST_DEATH_ROULETTE_RESULT_REQUIRED / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

영웅이 사망·완전 제거되면 기존 전장 인스턴스와 해당 출전에 소비한 `[영웅]` 등급 토큰은 종료된다. 사망으로 토큰·재화·대체 보상·무료 재출전권을 회수하지 않는다.

같은 영웅이나 다른 영웅을 다시 출전시키려면, **그 영웅의 사망 사건 이후** 룰렛을 정상적으로 다시 조작해 해당 병종의 새로운 `[영웅]` 등급 결과를 확정해야 한다. 사망 전에 보관함에 넣어 둔 `[영웅]` 등급 토큰은 이름 지정 영웅의 사망 후 재출전 자격을 충족하지 않는다.

```text
기존 영웅 사망·완전 제거
→ 기존 unit_instance 종료
→ active hero 슬롯 해제
→ 토큰 반환 없음
→ 사망 회수 보상 없음
→ 자동 부활·자동 재배치 없음
→ 사망 이후 정상 룰렛에서 새로운 동병종 [영웅] 등급 결과 확정
→ post-death 자격이 기록된 새 토큰 생성
→ 원본 영웅 등급 병종 유지 OR 해금된 동병종 영웅 선택
→ 1토큰을 1새 유닛으로 변환
→ 한 전선에 비가역 배치
```

## 2. 사망 시 무회수 원칙

영웅 사망은 다음 항목을 생성하지 않는다.

- 소비한 `[영웅]` 등급 토큰 반환.
- 토큰 조각·회수권·부활권·무료 재배치권.
- 골드·식량·런 재화·영구재화 같은 영웅 사망 보상.
- 같은 영웅 또는 같은 병종의 보장 토큰.
- 다음 스핀의 영웅 등급 확률 상승·보정·pity.
- 사망 인스턴스의 HP·쿨다운·충전·고유 자원 회수.

이 규칙은 영웅 사망 자체에 대한 보상만 금지한다. Stage 완료·미션·선택지·적 처치 등 별도의 정상 보상 계약은 변경하지 않는다.

## 3. 사망 이후 새로운 룰렛 결과 필수

```text
active_hero_unit_instance_id == null
AND token.grade == HERO
AND token.UnitArchetype matches selected unlocked Hero
AND token.created_by_spin_sequence > ended_hero.death_spin_sequence
→ named-Hero redeployment may be offered
```

- 영웅 사망만으로 새 토큰을 생성하지 않는다.
- 이전 출전의 source token을 복구하거나 복제하지 않는다.
- 사망 전에 이미 보관함에 존재하던 `[영웅]` 등급 토큰은 사망 후 이름 지정 영웅 재출전에 사용할 수 없다.
- 사망 전 보관 토큰은 원본 `[영웅]` 등급 병종 유닛으로 배치하거나 계속 보관할 수 있다.
- 이름 지정 영웅을 다시 출전시키려면 사망 사건 이후 룰렛에서 동병종 `[영웅]` 등급 결과가 새로 확정되어야 한다.
- 사망 이후 획득한 토큰이라도 병종이 일치하지 않으면 해당 영웅의 재출전에 사용할 수 없다.
- active 슬롯이 비어 있어도 일반·다른 등급 토큰을 영웅으로 승격할 수 없다.
- 영웅 사망을 이유로 과거 `SpinSnapshot`, 현재 보상, 다른 토큰 또는 릴 구조를 변경하지 않는다.
- 사망 사건과 토큰 획득 순서는 단조 증가 sequence 또는 동등한 결정론적 provenance로 기록한다.

## 4. 새 인스턴스의 초기 상태

사망 이후 새 룰렛 결과로 생성된 적격 `[영웅]` 등급 토큰을 소비한 이름 지정 영웅 인스턴스는 다음 상태로 시작한다.

```yaml
FreshHeroInstance:
  current_hp: max_hp
  remaining_skill_cooldowns: 0
  remaining_uses_and_charges: ability_defined_initial_values
  unique_resources: ability_defined_initial_values_default_zero
  temporary_buffs: none
  temporary_debuffs: none
  target_and_aggro: none
  cast_or_channel_state: none
  transient_projectiles_areas_traps: none
  temporary_summons: none
  inherited_state_from_previous_instance: none
```

- 현재 HP는 최대 HP로 시작한다.
- 기본 스킬은 사용 가능 상태로 시작한다.
- 횟수·충전형 능력은 각 능력 계약의 기본 시작값으로 시작한다.
- 고유 자원은 능력 계약의 초기값으로 시작하며, 별도 명시가 없으면 `0`이다.
- 이전 사망 인스턴스의 체력 손실·쿨다운·충전·버프·디버프·고유 자원을 승계하지 않는다.
- 이전 인스턴스가 남긴 투사체·장판·소환물·객체 참조도 승계하지 않는다.
- 동일 `hero_id`를 다시 선택하더라도 새 `unit_instance_id`와 새 `deployment_id`를 만든다.

## 5. 같은 영웅·다른 영웅 선택

active 슬롯이 비고 사망 이후 획득한 적격 동병종 토큰이 준비되면 다음 선택이 가능하다.

1. 토큰의 원본 `[영웅]` 등급 병종 유닛을 그대로 배치한다.
2. 같은 `UnitArchetype`에 연결된 해금 영웅 중 한 명을 선택해 새 이름 지정 영웅 인스턴스로 변환한다.

- 이전에 사망한 영웅과 같은 `hero_id`를 다시 선택할 수 있다.
- 같은 병종의 다른 해금 영웅을 선택할 수도 있다.
- 다른 병종 영웅은 후보가 아니다.
- 이전 사망 영웅을 자동 우선 선택하거나 자동 재배치하지 않는다.
- 변환하지 않고 원본 영웅 등급 병종을 사용하는 선택은 항상 유지한다.

## 6. 상태·원자성 책임

```yaml
HeroDeploymentRecord:
  deployment_id
  source_token_instance_id
  hero_id
  unit_instance_id
  lane_id
  deployed_at_stage
  ended_at_stage
  ended_reason
  ended_sequence

HeroGradeTokenProvenance:
  token_instance_id
  created_by_spin_id
  created_sequence
  unit_archetype
  grade

FreshHeroCreationTransaction:
  require_active_slot_empty
  require_unconsumed_matching_hero_grade_token
  require_token_created_after_previous_hero_ended_sequence
  consume_source_token_once
  create_new_unit_instance_once
  create_new_deployment_record_once
  set_default_initial_state
  commit_irreversible_lane_deployment
```

- 사망·슬롯 해제와 새 인스턴스 생성은 별개의 transaction이다.
- 사망 transaction은 보상이나 토큰을 생성하지 않는다.
- 새 인스턴스 생성은 사망 이후 룰렛에서 획득한 적격 토큰을 한 번 소비해야 한다.
- 동시 입력·Retry·저장 복구로 토큰 하나에서 두 영웅을 생성하면 안 된다.
- 새 인스턴스는 이전 persistent snapshot을 참조하지 않는다.
- 이전 사망 기록은 기록으로 남지만 새 인스턴스 초기화 입력으로 사용하지 않는다.
- 토큰 provenance 검증·토큰 소비·새 유닛·배치 기록 생성은 원자적으로 처리한다.

## 7. UX 책임

- 영웅 사망 시 `영웅 슬롯 해제`, `토큰 반환 없음`, `사망 이후 새 [영웅] 결과 필요`를 명확히 표시한다.
- 사망 화면에 회수·부활·재배치 보상처럼 보이는 연출을 사용하지 않는다.
- 사망 전 보관 토큰은 이름 지정 영웅 재출전 자격이 없음을 표시한다.
- 사망 전 보관 토큰은 원본 영웅 등급 병종으로는 사용할 수 있음을 구분해 표시한다.
- 사망 이후 적격 토큰이 없으면 영웅 후보 버튼을 비활성화하고 필요한 조건을 설명한다.
- 새 인스턴스 상세에는 최대 HP·준비된 스킬·기본 충전·초기 고유 자원을 미리 보여 준다.
- 같은 영웅을 다시 선택하더라도 이전 인스턴스 상태를 이어받지 않는다는 것을 표시한다.
- 일반 Stage·미션 보상과 영웅 사망 무보상을 혼동하지 않게 로그 원인을 분리한다.

## 8. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 영웅을 일부러 죽여 토큰이나 재화를 반복 회수한다 | 유효 | 사망 회수 보상·토큰 반환·부활권 전부 없음 |
| 사망 전에 쌓아 둔 보관 토큰으로 즉시 영웅을 교대한다 | 유효 | 사망 이후 룰렛에서 새로 생성된 적격 토큰만 이름 지정 영웅 재출전에 사용 |
| 사망 즉시 같은 영웅이 자동 생성된다 | 유효 | 사망 이후 정상 룰렛의 새 동병종 영웅 등급 결과를 필수 조건으로 둠 |
| 일반 토큰을 영웅으로 승격해 희귀도 비용을 우회한다 | 유효 | 실제 `[영웅]` 등급 토큰만 변환 가능 |
| 이전 사망 인스턴스의 낮은 HP를 버리고 새 토큰으로 완전 회복한다 | 의도된 새 토큰 가치 | 사망 이후 별도의 희귀 룰렛 결과를 다시 획득·소비한 완전한 새 인스턴스이며 무료 부활이 아님 |
| 같은 토큰을 저장·재시도로 두 번 소비한다 | 유효 | provenance 검증·토큰 소비·유닛 생성·배치 기록을 원자 처리하고 fault test 필요 |
| 사망이 다음 스핀의 확률 보정을 몰래 제공한다 | 유효 | 사망은 릴 odds·SpinSnapshot·pity를 변경하지 않음 |
| 사망 기록이 새 인스턴스 상태를 오염한다 | 유효 | 새 unit_instance는 이전 persistent snapshot을 참조하지 않음 |
| 무보상이 일반 Stage 보상까지 제거하는 것으로 오해된다 | 유효 | 영웅 사망 보상만 금지하고 별도 정상 보상 계약은 유지 |

## 9. 미확정 항목

- 병종별 정확한 영웅 명단·능력·초기 충전·고유 자원 값.
- 영웅 등급 토큰의 정확 출현 빈도와 릴 구성.
- 영웅 사망 연출·음향·로그 문구.
- 영웅과 원본 영웅 등급 병종의 정확 power budget.
- 반복 출전 빈도·강한 영웅 편중에 대한 simulation.

## 10. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1
= 이름 지정 영웅은 원본 [영웅] 등급 병종과 비교해 순수 상위호환인가, 같은 총 전투 예산을 다른 능력 구조로 교환하는 전문화 sidegrade인가
```

## 11. 상태 경계

```text
DESIGN: USER_APPROVED_FRESH_HERO_INSTANCE
DEATH_RECOVERY_REWARD: NONE
SOURCE_TOKEN_RETURN_ON_DEATH: NO
AUTOMATIC_REVIVE_OR_REDEPLOY: NO
PRE_DEATH_STORED_TOKEN_FOR_NAMED_HERO_REDEPLOYMENT: FORBIDDEN
POST_DEATH_MATCHING_HERO_GRADE_ROULETTE_RESULT: REQUIRED
FRESH_INSTANCE_HP: MAX
FRESH_INSTANCE_COOLDOWNS: READY
FRESH_INSTANCE_CHARGES: ABILITY_DEFAULT
FRESH_INSTANCE_UNIQUE_RESOURCE: ABILITY_DEFAULT_ZERO
PREVIOUS_INSTANCE_STATE_INHERITANCE: NONE
PRODUCT_CODE: UNCHANGED
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
```