# 오멘워드 맵런·스테이지·웨이브·정비시간 용어 및 진행 구조 승인 계약

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-MAPRUN-STAGE-WAVE-MAINTENANCE-V1
approved_at: 2026-08-02 17:41 KST
approval: USER_DIRECT_APPROVAL
status: USER_APPROVED_GAME_FLOW_TERMINOLOGY / MAINTENANCE_CLOCK_VALUES_PENDING / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

오멘워드의 한 작전은 플레이어가 `[맵]`을 선택하면서 시작한다. 선택한 맵을 기반으로 런 전용 상태를 초기화해 하나의 `MapRun`을 생성하고, MapRun 안에서 여러 `Stage`를 순서대로 진행한다. 각 Stage는 선택한 맵과 해당 Stage가 정의한 하나 이상의 `Wave`로 구성된다.

```text
맵 선택
→ MapRun 생성·런 전용 상태 초기화
→ Stage 1
   → Wave 1 ... Wave N
→ Stage 결과 정산·checkpoint
→ 정비시간
→ Stage 2
   → Wave 1 ... Wave N
→ 반복
→ 최종 Stage 종료
→ MapRun 최종 정산
```

현재 승인된 버티컬 슬라이스 목표는 한 MapRun당 20 Stage다. 맵은 Stage별 Wave 수, 적 편성, 등장 순서, 시간, 특수 규칙과 미션·선택지 후보를 정의한다. Stage 수 자체의 맵별 가변화는 별도 승인 전 도입하지 않는다.

## 2. 공식 용어

### 2.1 맵 / `MapDefinition`

- 전장 지형·전선 구조와 Stage·Wave 콘텐츠를 정의하는 제작 데이터다.
- 맵 선택은 콘텐츠 원본을 선택하는 행위이며 그 자체가 진행 중인 런 상태는 아니다.
- 같은 맵을 다시 선택해도 이전 MapRun의 전장 상태를 이어받지 않는다.

### 2.2 맵런 / `MapRun`

- 선택한 맵에서 시작해 승리·실패·중단 확정까지 이어지는 한 번의 전체 작전이다.
- 골드, 식량, 건물, 릴 배열, 보관함, 배치 병력, 점령 상태, active 영웅과 같은 RunState는 MapRun 범위다.
- Profile의 영구 해금·명부·연구 소유권은 초기화하지 않는다.

```text
MAPRUN_RESET
= RUN_STATE_RESET
!= PROFILE_RESET
```

### 2.3 스테이지 / `Stage`

- MapRun을 순서대로 구성하는 주요 진행 단위다.
- 한 Stage는 하나 이상의 Wave와 Stage 성공·실패 조건을 가진다.
- Stage 종료는 해당 Stage의 모든 Wave와 판정이 끝난 상태다.
- Stage와 Wave를 같은 의미로 사용하지 않는다.

### 2.4 웨이브 / `Wave`

- Stage 내부에서 순차적으로 실행되는 적 공세 단위다.
- Wave별 적 병종·수량·등장 전선·등장 시점·특수 행동은 맵과 Stage 데이터가 정의한다.
- `라운드`는 별도 시스템 계층이 아니다. 문서·코드·데이터의 공식 용어는 `Wave`, 사용자 표시 기본어는 `웨이브`로 통일한다.

### 2.5 정산 / `StageSettlement`

- Stage 승패, 전장 결과, 보상, 미션 결과와 저장 상태를 확정하는 처리 경계다.
- 정산 완료는 versioned checkpoint의 안전 경계다.
- 정산과 정비시간을 하나의 상태로 합치지 않는다.

### 2.6 정비시간 / `MaintenancePhase`

- 각 Stage 정산 뒤 다음 Stage가 시작되기 전에 제공되는 짧은 휴식·결정 구간이다.
- Wave 생성, 적 이동·공격, 자동전투와 점령 전투 진행은 일시정지한다.
- 미션과 선택지를 제시하고 플레이어가 내용을 확인·선택·확정한다.
- 위험 Stage 뒤에도 Stage 경계 정비시간은 존재한다. 이는 전투 중 수동 `전술계획 정지`와 별도 상태다.

## 3. Stage 진행 중 사용 가능한 네 기능

다음 기능은 정비시간 전용 기능이 아니다. Stage의 Wave와 전투가 진행되는 중에도 사용할 수 있다.

1. **건설·업그레이드·수리**
2. **룰렛 조작과 병력 확보**
3. **보관함 관리**
4. **병력 배치**

```text
STAGE_ACTIVE
→ BUILD / UPGRADE / REPAIR available
→ ROULETTE / ACQUIRE available
→ STORAGE_MANAGEMENT available
→ TROOP_DEPLOYMENT available
```

- 위험 Stage에서는 전투 중 전술계획 정지를 사용할 수 없더라도 네 기능 자체는 실시간으로 사용할 수 있다.
- 자원 부족, 식량 한도, 노드 점유, TokenSource BLOCKED, active hero 슬롯, PendingReward 처리 같은 기존 개별 조건은 그대로 적용한다.
- Stage 진행 중 사용 가능하다는 이유로 배치 취소·라인 이동·보상 재판정·SpinSnapshot 변경을 허용하지 않는다.

## 4. 정비시간에서의 기능

정비시간에서도 네 가지 런 운영 기능을 사용할 수 있다. 차이는 기능의 존재가 아니라 전장 공세가 잠시 멈추고 미션·선택지를 처리할 수 있다는 점이다.

```text
StageSettlement complete
→ MaintenancePhase entered
→ combat and Wave progression paused
→ mission / choice review and confirmation
→ build / upgrade / repair / roulette / storage / deployment remain operable
→ next Stage confirmed
```

정비시간 중 다음 시간축의 정확한 진행 여부는 아직 확정하지 않는다.

- 골드·식량 등 경제 생산 tick.
- 건설·업그레이드·수리 진행 시간.
- 유닛 회복·지속 피해·쿨다운.
- 버프·디버프·영웅 고유 자원.

따라서 이번 결정은 `명령과 UI 사용 가능 여부`를 승인하며, 정비시간이 무료 생산·무료 수리·무료 회복 시간이 된다고 승인하지 않는다.

## 5. 상태 전이 계약

```text
MAP_SELECTED
→ MAPRUN_INITIALIZING
→ STAGE_ACTIVE
→ WAVE_ACTIVE
→ WAVE_TRANSITION
→ WAVE_ACTIVE ...
→ STAGE_SETTLEMENT
→ MAINTENANCE_PHASE
→ NEXT_STAGE_START
```

- Wave 사이에는 기본적으로 별도 정비시간을 만들지 않는다.
- 맵이 다중 Wave를 정의하면 Stage 안에서 연속 진행한다.
- Stage 종료 후 정산을 완료한 뒤 정비시간으로 진입한다.
- 정비시간을 종료하고 다음 Stage 시작을 확정해야 새 Wave가 시작된다.
- 최종 Stage 뒤에는 다음 Stage 정비가 아니라 MapRun 최종 정산과 결과 화면으로 이동한다.

## 6. 영웅·유닛 상태 연결

- Stage 종료와 정비시간 진입은 active 영웅 슬롯 해제 사건이 아니다.
- 살아 있는 영웅은 정비시간과 다음 Stage에도 같은 전선의 동일 인스턴스로 유지된다.
- 일반 배치 유닛도 별도 사망·제거 규칙이 없는 한 MapRun 전장 상태를 유지한다.
- 정비시간 중에도 살아 있는 영웅을 수동 퇴각·교대·판매·재보관할 수 없다.
- 영웅의 체력·쿨다운·버프·디버프·소환물·고유 자원이 정비시간과 다음 Stage에서 어떻게 처리되는지는 후속 Decision 대상이다.

## 7. 데이터 책임

```yaml
MapDefinition:
  map_id
  stage_definitions

StageDefinition:
  stage_id
  wave_definitions
  mission_pool
  choice_pool
  success_conditions
  failure_conditions

WaveDefinition:
  wave_id
  enemy_spawns
  spawn_timing
  lane_targets
  special_rules

MapRunState:
  map_id
  current_stage_index
  current_wave_index
  phase
  run_resources
  battlefield_state
  reel_state
  storage_state

RunPhase:
  MAPRUN_INITIALIZING
  STAGE_ACTIVE
  STAGE_SETTLEMENT
  MAINTENANCE_PHASE
  MAPRUN_RESULT
```

- `Stage`와 `Wave` 인덱스를 별도로 저장한다.
- 정산 완료 checkpoint에서 Stage 결과와 다음 진입 Phase를 원자 기록한다.
- 저장 복구 시 `MAINTENANCE_PHASE`를 전투 중 Wave로 잘못 재개하지 않는다.
- 맵의 Stage·Wave 정의를 RunState에 복제해 독립 정본처럼 만들지 말고 맵 콘텐츠 ID와 버전 계약을 기록한다.

## 8. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 정비시간이 건설·룰렛을 할 수 있는 유일한 구간으로 오해된다 | 유효 | 네 기능은 Stage 진행 중에도 사용 가능한 상시 런 운영 기능으로 명시 |
| Stage와 Wave를 같은 뜻으로 사용해 저장·UI·밸런스가 엇갈린다 | 유효 | Stage는 주요 진행 단위, Wave는 Stage 내부 공세 단위로 분리 |
| `라운드`를 별도 상태로 추가해 계층이 중복된다 | 유효 | 공식 용어를 Wave로 통일하고 라운드는 별도 시스템 명칭으로 사용하지 않음 |
| 정비시간이 무한 무료 수리·생산·회복 구간이 된다 | 유효 | 명령 사용 가능과 시간축 진행을 분리하고 정확 clock matrix는 pending |
| 위험 Stage에서는 정비시간도 제거된다 | 충돌 | 전투 중 전술계획 정지 금지와 Stage 경계 정비시간을 별도 상태로 정의 |
| MapRun 초기화가 Profile 영구 해금을 지운다 | 유효 | RunState reset과 Profile persistence를 명시적으로 분리 |
| Wave마다 정비시간이 들어가 전투 리듬이 끊긴다 | 유효 | 기본 정비시간은 Stage 종료 뒤 한 번만 발생 |
| Stage 종료가 영웅 퇴각 기회로 변한다 | 유효 | 정비시간은 active 슬롯 해제 사건이 아니며 영웅 퇴각·교대 금지 유지 |

## 9. 미확정 항목

- 맵·Stage별 정확한 Wave 수와 적 편성.
- 정비시간의 정확한 길이와 플레이어 종료 방식.
- 정비시간 중 경제·건설·수리·회복·쿨다운 clock matrix.
- 미션·선택지의 제시 수, 선택 수, 갱신 규칙과 보상.
- Stage 전환 시 영웅·일반 유닛의 체력·상태 지속 규칙.
- 최종 Stage 뒤 후처리와 결과 화면의 정확한 UX.

## 10. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-STAGE-STATE-PERSISTENCE-V1
= Stage 정산·정비시간·다음 Stage 전환에서 살아 있는 영웅의 체력·쿨다운·버프·디버프·고유 자원을 어떻게 처리하는가
```

## 11. 상태 경계

```text
DESIGN: USER_APPROVED_MAPRUN_STAGE_WAVE_MAINTENANCE
MAPRUN_STAGE_TARGET: 20
STAGE_CONTAINS_WAVES: YES
ROUND_AS_SEPARATE_STATE: NO
MAINTENANCE_AFTER_EACH_STAGE: YES
MAINTENANCE_COMBAT_PAUSE: YES
STAGE_RUNTIME_BUILD_ROULETTE_STORAGE_DEPLOYMENT: YES
MAINTENANCE_CLOCK_MATRIX: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
```
