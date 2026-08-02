# 오멘워드 영웅 퇴각·교대·활성 종료 승인 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-HERO-EXIT-AND-REPLACEMENT-V1
approved_at: 2026-08-02 17:18 KST
approval: USER_APPROVED_RECOMMENDED_OPTION
status: USER_APPROVED_NO_MANUAL_EXIT / STAGE_STATE_VALUES_PENDING / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

전선에 배치한 이름 지정 `[영웅]` 유닛은 플레이어가 수동으로 퇴각시키거나 다른 영웅으로 교체할 수 없다. 영웅은 배치한 전선에 비가역 커밋되며, 살아 있는 동안 Stage와 Act가 전환되어도 같은 전장 유닛 인스턴스로 계속 출전한다.

```text
영웅 배치
→ 선택 전선에 비가역 커밋
→ 수동 퇴각 불가
→ 수동 교체 불가
→ Stage·Act 전환만으로 귀환하지 않음
→ 사망·완전 제거 시 active hero 슬롯 해제
→ MapRun 종료 시 active 상태 종료
```

## 2. 수동 퇴각·교대 금지

- 전투 중 영웅을 보관함·대기열·허브로 회수할 수 없다.
- Stage 사이에도 영웅을 임의로 귀환시킬 수 없다.
- 자원·영구재화·Retry 비용을 지불해 잘못된 영웅 배치를 취소할 수 없다.
- 살아 있는 영웅을 새 영웅 등급 토큰 또는 다른 해금 영웅으로 강제 교체할 수 없다.
- 전선 변경·판매·재보관·토큰 환원은 허용하지 않는다.
- 영웅을 제거하지 않은 채 초상·이름·병종만 바꾸는 교대 우회도 금지한다.

이 규칙은 일반 병력과 공유하는 `한 전선 비가역 배치` 원칙을 영웅에게도 유지한다.

## 3. Stage·Act 전환 지속

```text
active_hero_unit_instance_id != null
AND hero unit is alive and present
AND MapRun continues
→ same hero unit instance remains active
```

- Stage 종료는 active hero 슬롯을 비우지 않는다.
- Act 종료·다음 Act 진입도 그 자체로 영웅을 귀환시키지 않는다.
- 다음 Stage에는 새 영웅을 다시 배치하는 것이 아니라 기존 영웅 인스턴스가 계속 존재한다.
- 영웅의 배치 전선은 Stage·Act 전환 후에도 유지한다.
- Stage 전환을 무료 회복·부활·재배치로 간주하지 않는다.
- 체력·쿨다운·일시 상태·소환물의 정확한 Stage 전환 처리는 다음 Decision에서 확정한다.

## 4. active hero 슬롯 해제 사건

현재 승인된 슬롯 해제 사건은 다음 두 가지다.

### 4.1 영웅 사망·완전 제거

- 영웅 유닛이 사망하고 전장 인스턴스가 완전히 제거되면 active hero 슬롯을 비운다.
- 슬롯 해제와 해당 출전 기록의 종료는 같은 원자적 transaction으로 기록한다.
- 슬롯이 비워진 뒤에는 새 동병종 `[영웅]` 등급 토큰을 소비해 같은 영웅 또는 다른 해금 영웅을 다시 출전시킬 수 있다.
- 사망한 영웅의 active 전장 효과는 함께 종료한다. 지속 효과 예외는 개별 능력 계약에 명시된 경우에만 허용한다.

### 4.2 MapRun 종료

- MapRun 승리·실패·중단 확정으로 전장이 종료되면 active hero 상태도 종료한다.
- MapRun 종료 시 영웅 유닛을 다음 MapRun으로 직접 이월하지 않는다.
- Profile의 영웅 해금·명부 소유권은 유지하지만, 전장 인스턴스·active 슬롯·전투 상태는 Run 범위다.

## 5. 새 영웅 출전 조건

```text
active_hero_unit_instance_id == null
AND matching Hero-grade token is available
AND selected hero is unlocked
AND selected hero matches token UnitArchetype
→ new Hero deployment may be confirmed
```

- 새 출전은 반드시 새로운 `[영웅]` 등급 토큰 하나를 소비한다.
- 이전 영웅이 사망했다고 무료 재출전·자동 부활·자동 교대를 제공하지 않는다.
- 같은 `hero_id`의 반복 출전도 동일한 조건을 따른다.
- active 영웅이 살아 있는 동안 얻은 영웅 등급 토큰은 보관하거나 원본 영웅 등급 병종 유닛으로 배치할 수 있다.

## 6. 데이터·상태 책임

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
  ended_at_stage
  ended_reason

ApprovedHeroEndedReason:
  HERO_DEATH
  MAPRUN_COMPLETED
  MAPRUN_FAILED
  MAPRUN_ABANDONED_CONFIRMED
```

- 수동 퇴각·수동 교체를 위한 종료 사유는 만들지 않는다.
- Stage·Act 전환은 `ended_reason`이 아니다.
- 영웅 사망 판정, 슬롯 해제, 전장 효과 종료, 기록 갱신은 원자적으로 처리한다.
- 저장 복구 후 살아 있는 영웅 인스턴스와 active 슬롯이 서로 불일치하면 오류로 처리하고 무단으로 새 영웅을 생성하지 않는다.

## 7. UX 책임

- active 영웅 초상·전선·생존 상태·슬롯 점유를 항상 확인할 수 있게 한다.
- 영웅 상세·보관함 화면에 `퇴각 불가`, `교체 불가`, `사망 또는 작전 종료 시 슬롯 해제`를 명시한다.
- 새 영웅 후보가 비활성화된 경우 현재 영웅과 점유 전선을 보여 준다.
- 수동 퇴각이 가능한 것처럼 보이는 귀환·교체·판매 버튼을 노출하지 않는다.
- Stage·Act 전환 화면에서 영웅이 유지된다는 사실을 명확히 보여 준다.

## 8. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 잘못 배치한 영웅이 오래 살아 다른 선택을 막는다 | 의도된 기회비용 | 원본 영웅 등급 병종 사용·전선 판단·영웅 밸런스로 대응, 퇴각 취소권은 제공하지 않음 |
| 안전할 때 영웅을 회수해 위험을 제거한다 | 유효 | 수동 퇴각·교대·판매·보관 금지 |
| Stage 종료마다 무료로 영웅을 바꾼다 | 유효 | Stage·Act 전환에도 동일 인스턴스 유지 |
| 영웅 사망 후 자동 부활로 토큰 비용을 우회한다 | 유효 | 새 출전마다 새 영웅 등급 토큰 소비 |
| 사망한 영웅 효과가 남아 단일 활성 제한을 우회한다 | 유효 | active 효과는 슬롯 해제와 함께 종료, 예외는 개별 능력에 명시 |
| 저장 복구로 영웅이 둘이 되거나 슬롯이 잠긴다 | 유효 | 사망·종료·슬롯 해제를 원자 기록하고 fault test 필요 |
| 영웅이 Stage 사이에 계속 남지만 상태 처리가 모호하다 | 유효 | 체력·쿨다운·상태 지속 규칙을 다음 Gate로 분리 |

## 9. 미확정 항목

- Stage 전환 시 영웅 체력 유지·회복 비율.
- Stage 전환 시 스킬 쿨다운·충전·일시 버프·디버프 처리.
- 소환물·장판·투사체 같은 파생 인스턴스의 Stage 경계 처리.
- 반복 출전 시 새 인스턴스의 초기 체력·쿨다운·고유 자원.
- 영웅별 능력·명단·등급·수치.
- 영웅 사망 연출·결과 로그·접근성 피드백.

## 10. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-STAGE-STATE-PERSISTENCE-V1
= 살아 있는 영웅의 체력·쿨다운·버프·디버프·고유 자원은 Stage 전환에서 어떻게 유지·회복되는가
```

## 11. 상태 경계

```text
DESIGN: USER_APPROVED_NO_MANUAL_EXIT
MANUAL_RETREAT: FORBIDDEN
MANUAL_REPLACEMENT: FORBIDDEN
STAGE_AND_ACT_TRANSITION: SAME_HERO_INSTANCE_REMAINS
ACTIVE_SLOT_CLEAR: HERO_DEATH_OR_MAPRUN_END
NEW_DEPLOYMENT: NEW_HERO_GRADE_TOKEN_REQUIRED
STAGE_STATE_VALUES: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
```
