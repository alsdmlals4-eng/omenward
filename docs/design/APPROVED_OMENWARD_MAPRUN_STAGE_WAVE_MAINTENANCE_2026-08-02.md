# [현행] 오멘워드 MapRun·Stage·Wave·정비시간 용어 및 진행 구조

```yaml
decision_id: OMW-DEC-20260802-GAMEPLAY-MAPRUN-STAGE-WAVE-MAINTENANCE-V1
original_approval: USER_DIRECT_APPROVAL
updated_at: 2026-08-04
amended_by: OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1
status: CURRENT_GAME_FLOW_TERMINOLOGY / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 진행 구조

```text
맵 선택
→ MapRun 생성·RunState 초기화
→ Stage 1
   → Wave Beat 1~3
→ StageSettlement·checkpoint
→ MaintenancePhase
→ 다음 Stage
→ Stage 20 Final Boss
→ MapRun 최종 정산
```

현재 콘텐츠 기준선:

```text
MapRun당 Stage = 20
기본 Wave Beat = 3
Danger Stage = 4 / 9 / 14 / 19
Boss Stage = 5 / 10 / 15 / 20
```

정확한 Wave 지속시간·Spawn 묶음·Threat Budget은 시뮬레이션 전 정본 수치로 고정하지 않는다.

## 2. 공식 용어

### 맵 / `MapDefinition`

전장 지형·Route·Stage 콘텐츠 변형을 정의하는 제작 데이터다. 맵 선택은 콘텐츠 원본 선택이며 진행 중인 런 상태가 아니다.

### MapRun

선택한 맵에서 시작해 승리·실패·중단까지 이어지는 한 번의 전체 작전이다.

MapRun 범위:

- 골드·마석·배치 병력·병력 한도·이동권.
- 건물·릴·보관함·병력·전선·거점 상태.
- 현재 Stage·Wave·Phase와 checkpoint.

Profile 영구 해금·설정은 MapRun 초기화 대상이 아니다.

### Stage

MapRun의 주요 성장·결정 단위다. 하나 이상의 Wave와 성공·실패 조건을 가진다. 현재 기준선은 3개의 Wave Beat다.

### Wave

Stage 내부의 적 공세 단위다. 적 역할·전선·Route·예상 목표·특수 행동을 가진다.

`라운드`는 별도 시스템 계층으로 사용하지 않는다.

### StageSettlement

Stage 승패, 전장 결과, 보상, 미션 결과와 저장 상태를 확정하는 경계다.

### MaintenancePhase

Stage 정산 뒤 다음 Stage 전에 제공되는 짧은 휴식·결정 구간이다.

- Wave·자동전투·점령 진행 정지.
- Stage 종료 상인 방문.
- 미션·선택지·결과 확인.
- 다음 Stage 압력 정보 확인.
- 건설·룰렛·보관·판매·배치 사용 가능.

## 3. Stage 유형

### Normal

- 하나 또는 두 압력을 학습·조합한다.
- Wave 1 Probe → Wave 2 Complication → Wave 3 Commitment Test.

### Danger

- Stage 전체에 공개된 한 가지 규칙 변형을 사용한다.
- 핵심 기능이나 치명적 정보를 숨기지 않는다.
- 현재 유형:
  - Stage 4 우회 Route 활성 순서.
  - Stage 9 Wave 겹침 시간표.
  - Stage 14 주 전선 이동 순서.
  - Stage 19 Route 수렴 순서.

### Boss

- Route·태세·목표·호위·집중 공격 기회를 바꾼다.
- HP·피해만 올리는 Boss를 승인하지 않는다.
- 현재 유형:
  - Stage 5 공성 준비 창.
  - Stage 10 공중/우회 Route 전환.
  - Stage 15 행군/포격 태세.
  - Stage 20 세 Omen Pattern.

## 4. Stage 진행 중 사용 가능 기능

다음 기능은 Normal·Danger·Boss 전투 중 유지된다.

1. 건설·업그레이드·수리.
2. 룰렛 회전·이동·확정.
3. 보관함 관리·판매.
4. 병력 배치.
5. 전술스킬.
6. 벨루 정보 확인.

Danger는 위 기능을 임의로 차단해서 난도를 만들지 않는다.

전투 중 수동 전술계획 정지의 존재와 Clock Matrix는 현재 정본이 승인하지 않았다. 과거 문서의 정지 규칙을 구현 입력으로 사용하지 않는다.

## 5. 정비시간의 시간축 경계

정비시간 중 다음 Clock은 아직 미확정이다.

- 경제 수급.
- 건설·업그레이드·수리 진행.
- 유닛 회복·지속 피해.
- 쿨다운·버프·디버프.
- 전술 자원 회복.

따라서 정비시간을 무한 무료 생산·수리·회복 구간으로 해석하지 않는다.

## 6. Stage 정보 공개

Stage 시작 전 공개:

- Stage 유형.
- 주·보조 압력.
- Wave별 전선·Route.
- 예상 우선 목표.
- 치명적 특수 행동.
- Danger/Boss 전환 순서.

기본·일반 난이도에서 위 정보를 숨기지 않는다.

Stage 시작 뒤 무작위로 압력 정체성·치명적 Route·필요 공격 Layer를 변경하지 않는다.

## 7. 정산·전환

```text
모든 Wave Beat 시작
→ 남은 Stage 목표 처리
→ StageSettlement
→ checkpoint 저장
→ MaintenancePhase
→ 상인·미션·선택지
→ 다음 Stage 시작 확정
```

- Wave 사이에 기본 정비시간을 만들지 않는다.
- Stage 종료가 살아 있는 병력·건물·전선 상태 초기화 사건은 아니다.
- Final Boss 뒤에는 MaintenancePhase 대신 MapRun 최종 결과로 이동한다.

Hero·Legendary·Meta의 정확한 Stage 전환 상태는 lifecycle `[보류]` 문서에서 가져오지 않고 후속 재승인 뒤 연결한다.

## 8. 데이터 책임 경계

플레이어 기획 정본이 소유:

- Stage 유형과 압력 역할.
- Wave Beat의 학습 역할.
- 정보 공개 약속.
- Danger/Boss의 플레이어 체감 규칙.
- Stage 정산·정비의 기능 경계.

Codex가 소유:

- 데이터 Schema.
- Spawn Group 구조.
- Timer·Clock 구현.
- 저장·복구·버전 계약.
- Stage 전이 코드와 테스트.

## 9. 현재 책임 원본

- Stage 압력 매트릭스: `APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- MapRun·접전지 코어: `APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`
- 프로젝트 코어: `../PROJECT_CORE.md`
- 현행 GDD: `../OMENWARD_GDD_CURRENT_CANON.md`

## 10. 상태 경계

```text
MAPRUN_STAGE_TARGET = 20
BASELINE_WAVE_BEATS = 3
DANGER_STAGES = 4 / 9 / 14 / 19
BOSS_STAGES = 5 / 10 / 15 / 20
MAINTENANCE_AFTER_STAGE = YES
MAINTENANCE_AFTER_WAVE = NO
CURRENT_RESOURCES = GOLD / MANA_STONE / TROOP_CAP / MOVE_TICKET
TACTICAL_PLANNING_PAUSE = NOT_AUTHORIZED_BY_CURRENT_CANON
MAINTENANCE_CLOCK_MATRIX = PENDING
PRODUCT_CODE = UNCHANGED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```