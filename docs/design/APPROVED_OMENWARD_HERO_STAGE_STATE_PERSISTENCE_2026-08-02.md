# 오멘워드 영웅 Stage 상태 지속 승인 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-STAGE-STATE-PERSISTENCE-V1
approved_at: 2026-08-02 18:02 KST
approval: USER_APPROVED_RECOMMENDED_OPTION
status: USER_APPROVED_LONG_TERM_STATE_PERSISTS / TRANSIENT_COMBAT_STATE_CLEARS / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

살아 있는 이름 지정 `[영웅]` 유닛은 Stage 정산·정비시간·다음 Stage 전환에서도 같은 전장 인스턴스로 유지된다. 장기적인 손상과 사용 상태는 보존하지만, 이전 Stage의 타깃·일시 효과·투사체·장판·일시 소환물 같은 전투 잔여물은 Stage 경계에서 제거한다.

```text
Stage 전투 종료
→ 영웅 생존 확인
→ 일시 버프·디버프·타깃·어그로·시전 상태 제거
→ 투사체·장판·일시 소환물 제거
→ 현재 HP·남은 쿨다운·남은 사용 횟수·고유 누적 자원 저장
→ checkpoint
→ 정비시간: 영웅 회복·쿨다운·충전 clock 정지
→ 다음 Stage에서 같은 영웅 인스턴스와 저장된 장기 상태 복원
```

## 2. Stage 경계를 넘어 유지하는 상태

살아 있는 영웅은 다음 상태를 현재 값 그대로 유지한다.

- 현재 HP와 최대 HP 관계.
- 남아 있는 스킬 쿨다운 시간.
- 소모형 스킬의 남은 사용 횟수·충전 수.
- 영웅 고유 누적 자원과 현재 게이지.
- 영웅의 배치 전선과 전장 인스턴스 식별자.
- 영웅 해금·영구 업그레이드·고유 패시브처럼 전투 이전부터 소유한 영속 능력.

예시:

```text
Stage 종료 상태
HP = 420 / 1000
Skill A cooldown = 8.0 seconds remaining
Skill B charges = 1 / 3
Unique resource = 65 / 100

다음 Stage 시작 상태
HP = 420 / 1000
Skill A cooldown = 8.0 seconds remaining
Skill B charges = 1 / 3
Unique resource = 65 / 100
```

Stage 전환 자체는 무료 회복·무료 충전·쿨다운 초기화·고유 자원 초기화를 제공하지 않는다.

## 3. Stage 경계에서 제거하는 전투 잔여 상태

Stage 정산이 시작되면 다음 상태를 제거하거나 초기화한다.

- 일시 버프와 일시 디버프.
- 현재 공격 대상과 스킬 대상.
- 어그로·위협도·표적 우선도 임시 누적.
- 공격 선딜·후딜, 이동 명령, 시전 중 상태, 채널링.
- 발사됐지만 아직 충돌하지 않은 투사체.
- 남아 있는 장판·범위 지속 효과·함정·일시 지형 효과.
- Stage 전투용으로 생성된 일시 소환물·분신·드론·토템.
- 이전 Wave·Stage의 적 또는 제거된 객체를 참조하는 상태.

다음 항목은 자동으로 제거하지 않는다.

- 영웅 정의에 포함된 고유 패시브.
- Profile·허브·연구에서 영구 해금된 능력.
- 영웅 본체의 현재 HP·쿨다운·충전·고유 자원.

영웅과 항상 함께 존재하는 영속 동반자처럼 `일시 소환물`인지 `영웅 인스턴스의 고정 구성요소`인지 모호한 개체는 개별 영웅 능력 계약에서 명시한다. 명시가 없으면 Stage 전투 중 생성된 소환물로 보고 제거한다.

## 4. 정비시간 clock 규칙

정비시간은 영웅에게 무료 회복 시간을 제공하지 않는다.

```text
MaintenancePhase
- hero HP regeneration clock: PAUSED
- hero skill cooldown clock: PAUSED
- hero charge regeneration clock: PAUSED
- hero unique-resource passive gain/decay clock: PAUSED
- temporary combat effects: ALREADY_CLEARED
```

- 정비시간 체류만으로 HP가 회복되지 않는다.
- 쿨다운이 감소하지 않는다.
- 사용 횟수·충전 수가 회복되지 않는다.
- 고유 자원이 자동 생성·감소하지 않는다.
- 영웅 능력에 `정비시간 진입 시`라는 명시적 효과를 후속으로 추가하지 않는 한 MaintenancePhase 자체는 영웅 상태를 변경하지 않는다.
- Stage 전투가 다시 시작되면 해당 영웅의 정상 전투 clock이 재개된다.

이 결정은 일반 경제·건설·수리 clock matrix 전체를 확정하지 않는다. 영웅 상태 clock에만 적용한다.

## 5. 원자적 Stage 전환 순서

```text
1. Stage combat completion confirmed
2. Resolve final combat tick and damage
3. If Hero HP <= 0 or Hero is completely removed:
   apply Hero Exit contract and clear active slot
4. Otherwise:
   clear transient combat state and transient child entities
5. capture HeroPersistentBattleState
6. write Stage settlement and checkpoint atomically
7. enter MaintenancePhase
8. start next Stage from the captured persistent state
```

- 마지막 전투 틱의 피해보다 먼저 임의 회복하거나 상태를 저장하지 않는다.
- 사망한 영웅을 생존 상태로 checkpoint에 기록하지 않는다.
- Stage 정산 실패 시 이전 정상 checkpoint를 파괴하지 않는다.
- 저장 중단·재시도·중복 입력으로 영웅 HP·쿨다운·자원이 복제되거나 두 번 차감되면 안 된다.

## 6. 데이터·저장 책임

```yaml
HeroPersistentBattleState:
  hero_unit_instance_id
  hero_id
  lane_id
  current_hp
  max_hp_reference
  skill_cooldown_remaining_by_skill_id
  remaining_charges_by_skill_id
  unique_resource_by_resource_id
  persistent_ability_state
  captured_at_stage

HeroTransientBattleState:
  target_unit_id
  aggro_state
  active_temporary_buffs
  active_temporary_debuffs
  attack_or_cast_state
  active_projectile_ids
  active_area_effect_ids
  active_temporary_summon_ids
```

- `HeroPersistentBattleState`는 checkpoint 저장 대상이다.
- `HeroTransientBattleState`는 Stage 경계에서 제거하며 다음 Stage 저장 데이터에 포함하지 않는다.
- 로드 시 persistent 상태를 동일 영웅 인스턴스에 정확히 한 번 복원한다.
- 존재하지 않는 스킬·자원 ID, 음수 HP, 최대치를 초과한 충전·자원, active 슬롯과 인스턴스 불일치는 오류로 처리한다.
- 오류를 자동으로 영웅 전회복·무료 재배치·새 영웅 생성으로 보정하지 않는다.

## 7. UX 책임

- Stage 정산 화면에 영웅의 현재 HP, 남은 주요 쿨다운·충전, 고유 자원 유지 여부를 표시한다.
- 정비시간 HUD에서 `영웅 상태 유지`, `정비 중 회복·쿨다운 정지`를 명시한다.
- 제거된 일시 버프·디버프와 유지되는 장기 상태를 혼동시키지 않는다.
- 다음 Stage 미리보기에서 같은 영웅·같은 전선·현재 HP로 이어진다는 사실을 보여 준다.
- 정비시간 동안 쿨다운 숫자가 감소하거나 충전 UI가 차오르는 연출을 하지 않는다.
- Stage 전환을 영웅 부활·전회복·무료 스킬 초기화처럼 보이게 하지 않는다.

## 8. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 매 Stage 스킬 쿨다운을 초기화해 강력한 개막기를 반복한다 | 유효 | 남은 쿨다운·사용 횟수를 그대로 유지 |
| 정비시간에 무한 체류해 영웅을 전회복한다 | 유효 | HP·쿨다운·충전·고유 자원 clock 정지 |
| 이전 Stage 투사체나 장판이 다음 Stage 적을 즉시 공격한다 | 유효 | Stage 경계에서 투사체·장판·일시 소환물 제거 |
| 디버프가 영원히 남아 영웅이 사실상 사용 불가능해진다 | 유효 | 일시 버프·디버프는 Stage 종료 시 제거 |
| 버프를 유지해 다음 Stage에 사전 축적한다 | 유효 | 일시 버프도 함께 제거; 영속 효과만 능력 계약으로 허용 |
| 마지막 전투 틱 사망을 저장 순서로 회피한다 | 유효 | 최종 피해·사망 처리 뒤 persistent snapshot 생성 |
| 저장·로드로 HP나 충전이 복제된다 | 유효 | persistent state 원자 저장·단일 복원·fault test 필요 |
| 오래 생존한 영웅의 손상이 누적돼 지나치게 약해진다 | 의도된 장기 비용 | 힐러·전투 중 회복·영웅 밸런스로 검증; Stage 무료 회복은 제공하지 않음 |
| 영속 동반자와 일시 소환물의 구분이 모호하다 | 유효 | 개별 영웅 능력 계약으로 명시, 기본값은 일시 소환물 제거 |

## 9. 미확정 항목

- 영웅이 사망한 뒤 새 토큰으로 반복 출전하는 새 인스턴스의 초기 HP·쿨다운·충전·고유 자원.
- 영웅별 정확 스킬·고유 자원·충전 구조와 수치.
- 전투 중 HP 회복·재생·치유 병종의 정확 수치.
- 영속 동반자·소환 특화 영웅의 개별 예외.
- 정비시간의 일반 경제·건설·수리 clock matrix.
- Stage 정산·정비시간 화면의 정확 레이아웃과 접근성 검증.

## 10. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-REDEPLOYMENT-INITIAL-STATE-V1
= 영웅 사망 뒤 새 영웅 등급 토큰을 소비해 같은 영웅 또는 다른 영웅을 다시 배치할 때 새 인스턴스의 HP·쿨다운·충전·고유 자원은 어떤 초기값으로 시작하는가
```

## 11. 상태 경계

```text
DESIGN: USER_APPROVED_LONG_TERM_STATE_PERSISTS
CURRENT_HP: PERSISTS
SKILL_COOLDOWN_REMAINING: PERSISTS
SKILL_CHARGES_AND_USES: PERSIST
UNIQUE_RESOURCE: PERSISTS
TEMPORARY_BUFFS_AND_DEBUFFS: CLEAR_AT_STAGE_SETTLEMENT
TARGET_AGGRO_CAST_STATE: RESET
PROJECTILES_AREAS_TEMP_SUMMONS: REMOVE
MAINTENANCE_HERO_CLOCKS: PAUSED
FREE_HEAL_OR_COOLDOWN_RESET: FORBIDDEN
REDEPLOYMENT_INITIAL_STATE: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
```