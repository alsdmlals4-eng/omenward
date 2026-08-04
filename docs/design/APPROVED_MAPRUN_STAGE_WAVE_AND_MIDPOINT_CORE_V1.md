# [현행] MapRun·Stage·Wave·접전지 코어

```yaml
updated_at: 2026-08-04
status: CURRENT_MAPRUN_STAGE_WAVE_CORE / NOT_IMPLEMENTED
original_approval: 2026-07-24 USER_APPROVED
current_amendment: OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

이 문서는 MapRun → Stage → Wave의 진행 계층과 전선 지속 상태를 소유한다. Stage 콘텐츠 압력과 20 Stage 순서는 최신 압력 매트릭스가 소유한다.

## 1. 진행 계층

```text
MapRun
└─ Stage
   └─ Wave Beat
      └─ Spawn Group
```

- `MapRun`: 선택한 맵에서 시작해 승리·실패·중단까지 이어지는 한 번의 전체 작전.
- `Stage`: 건물·릴·병력·전선 상태가 누적되는 주요 진행 단위.
- `Wave`: Stage 내부에서 순차 또는 공개된 겹침 일정으로 실행되는 적 공세 단위.
- `Spawn Group`: 실제 적 출현의 내부 묶음. 플레이어용 별도 진행 계층이 아니다.

현재 기준:

```text
한 MapRun = 20 Stage
기본 Stage = 3개 Wave Beat
Danger Stage = 4 / 9 / 14 / 19
Boss Stage = 5 / 10 / 15 / 20
```

정확한 Spawn Group 수·등장 간격·Threat Budget은 시뮬레이션과 Codex 콘텐츠 데이터 설계가 소유한다.

## 2. MapRun 유지 상태

MapRun 동안 유지되는 플레이어 상태:

- 골드·마석·배치 병력·병력 한도·이동권.
- 건물 6종의 건설·업그레이드·파괴·점령 상태.
- 세 원형 릴 배열·이동 결과·TokenSource 연결.
- 보관함·미확정 결과·판매 결과.
- 배치 병력의 전선·HP·생존 상태.
- 본진·거점·건물 HP와 전선 소유권.
- Stage·Wave 진행과 정산 checkpoint.

현행 핵심 자원에 식량을 사용하지 않는다.

```text
MAPRUN_RESET
= RUN_STATE_RESET
!= PROFILE_RESET
```

Hero·Legendary·Meta·Hub 상태의 정확한 지속 규칙은 lifecycle `[보류]` 문서에서 가져오지 않고 후속 재승인 뒤 연결한다.

## 3. Stage 흐름

```text
Stage 시작
→ 전체 Stage 압력·Wave 역할·치명적 특수 행동 확인
→ Wave 1
→ Wave 전환 또는 공개된 Wave 겹침
→ Wave 2
→ Wave 3
→ 남은 적·Stage 목표 처리
→ StageSettlement
→ MaintenancePhase
→ 다음 Stage 확정
```

- Wave와 Stage를 같은 뜻으로 사용하지 않는다.
- Wave마다 별도 정비시간을 만들지 않는다.
- Stage 종료 뒤 정산과 정비시간이 한 번 발생한다.
- 최종 Stage 뒤에는 다음 Stage 정비가 아니라 MapRun 최종 정산으로 이동한다.

## 4. Stage 중 플레이어 기능

다음 기능은 일반 Stage·Danger Stage·Boss Stage에서 계속 사용할 수 있다.

1. 건설·업그레이드·수리.
2. 룰렛 회전·이동·결과 확정.
3. 보관함 관리·판매.
4. 병력 배치.
5. 전술스킬 사용.
6. 벨루 상황 설명 확인.

Danger는 핵심 기능을 임의로 차단해 난도를 만들지 않는다. Danger의 난도는 공개된 Route·Wave 시간표·주 전선 이동·Route 수렴 같은 한 가지 규칙 변형에서 나온다.

전투 중 수동 전술계획 정지의 존재·Clock 규칙은 현행 Stage 압력 정본이 승인하지 않는다. 별도 Decision 전에는 구현 입력으로 사용하지 않는다.

## 5. 공세 예고

Stage 시작 전 최소 공개:

- Stage 유형: Normal / Danger / Boss.
- 주·보조 압력 태그.
- Wave별 주 전선과 Route.
- 예상 우선 목표.
- 비행·침투·공성 같은 치명적 특수 행동.
- 공개된 Wave 겹침·주 전선 이동·Route 수렴 순서.

기본·일반 난이도에서 위 정보를 숨기지 않는다.

Stage 시작 뒤 다음 항목을 무작위로 바꾸지 않는다.

- 주 압력 정체성.
- 치명적 Route 전환.
- 필요한 공격 Layer.
- Boss의 다음 Pattern.
- 이미 공개된 주 전선 순서.

## 6. Wave 겹침

- 이전 Wave의 살아 있는 적은 새 Wave 시작 시 제거하지 않는다.
- Wave 겹침은 Stage 9 같은 콘텐츠 규칙 또는 난이도 조정으로 사용할 수 있다.
- 다음 Wave 시작 시각과 압력은 사전에 표시한다.
- 겹침은 숨은 기습이 아니라 현재 전투를 끝낼지 다음 Wave를 준비할지 선택하게 해야 한다.

## 7. Stage 종료

기본 완료 조건:

- 해당 Stage의 모든 Wave Beat가 시작됨.
- Stage가 요구한 Boss·Objective·적 병력이 처리됨.
- 공개된 추가 성공 조건이 확정됨.

기본 실패 조건:

- 아군 본진 HP 0.
- Stage가 사전에 공개한 보호 목표 파괴.
- 사전에 공개한 특수 실패 조건 달성.

Stage 종료는 살아 있는 아군·건물·전선 소유권을 자동 초기화하지 않는다.

## 8. 결과·배치

- 룰렛 결과는 보관·판매·한 전선 배치 중 선택한다.
- 배치 뒤 자유 회수·판매·전선 변경은 없다.
- 배치 병력은 농장이 제공하는 병력 한도를 사용한다.
- 보관 중 병력은 배치 병력 한도를 사용하지 않는다.
- 병력 한도 감소는 기존 배치 병력을 제거·약화하지 않고 신규 배치만 차단한다.

## 9. 접전지·전선 지속

- 상·중·하 세 전선의 거점·점령 상태는 같은 MapRun의 Stage 사이에 유지된다.
- 일반 유닛은 전선 사이를 자유롭게 횡단하지 않는다.
- 우회·공중·Cross-lane 이동은 사전에 보이는 Route 또는 명시적 능력만 허용한다.
- Stage 19 같은 Route 수렴은 시작 전에 출발 Route와 결정 전선을 전부 공개한다.
- 후방 거점을 잃어도 이미 전진한 병력을 자동 제거·후퇴시키지 않는다.

정확한 좌표·점령 계산·Pathfinding·충돌은 Codex가 소유한다.

## 10. 정비시간

StageSettlement 뒤:

- Wave 생성·이동·공격·점령 전투는 정지한다.
- Stage 종료 상인이 방문한다.
- 미션·선택지·결과를 확인한다.
- 건설·룰렛·보관·배치 기능은 사용할 수 있다.
- 다음 Stage의 전체 압력 정보를 확인하고 시작을 확정한다.

정비 중 생산·수리·회복·쿨다운 Clock의 정확한 진행 여부는 후속 Clock Decision 전까지 미확정이다. 무료 생산·무료 회복 시간으로 간주하지 않는다.

## 11. 저장 경계

- Stage 정산 완료 checkpoint는 안전 저장 경계다.
- Stage와 Wave 인덱스를 분리해 기록한다.
- 복구 시 MaintenancePhase를 Wave 전투로 잘못 재개하지 않는다.
- 맵 콘텐츠 정의를 RunState에 별도 정본으로 복제하지 않고 콘텐츠 ID·버전을 기록한다.

저장 구조·직렬화·복구 알고리즘은 Codex가 결정한다.

## 12. 현재 책임 원본

- Stage 콘텐츠·20 Stage 매트릭스: `APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- Stage 정비 용어: `APPROVED_OMENWARD_MAPRUN_STAGE_WAVE_MAINTENANCE_2026-08-02.md`
- 전장 Route·Targeting: `APPROVED_OMENWARD_COMBAT_SPACE_ROUTE_AND_TARGETING_EXPERIENCE_2026-08-04.md`
- 프로젝트 코어: `../PROJECT_CORE.md`

## 13. 상태 경계

```text
MAPRUN_STAGE_TARGET = 20
BASELINE_WAVE_BEATS = 3
DANGER_STAGES = 4 / 9 / 14 / 19
BOSS_STAGES = 5 / 10 / 15 / 20
FOOD_AS_CURRENT_RESOURCE = FALSE
TACTICAL_PLANNING_PAUSE = NOT_AUTHORIZED_BY_CURRENT_CANON
MIDRUN_CHECKPOINT = STAGE_SETTLEMENT_BOUNDARY
PRODUCT_CODE = UNCHANGED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```