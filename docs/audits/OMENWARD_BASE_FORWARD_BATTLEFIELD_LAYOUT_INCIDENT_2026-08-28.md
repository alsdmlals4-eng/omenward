# OMENWARD 본진·전진기지 전장 배치 정본 충돌 Incident · 2026-08-28

```yaml
incident_id: OMW-INC-20260828-BASE-FORWARD-BATTLEFIELD-LAYOUT-01
status: RESOLVED_IN_PLANNING__RUNTIME_FOLLOW_UP_REQUIRED
severity: MATERIAL_PLANNING_AND_VISUAL_CANON_DRIFT
current_owner: docs/design/APPROVED_OMENWARD_BASE_FORWARD_BATTLEFIELD_CONSTRUCTION_LAYOUT_2026-08-28.md
discovered_by: USER_DIRECTION_PLUS_FRESH_ACTUAL_CODE_RECHECK
runtime_evidence: NOT_RUN_FOR_NEW_LAYOUT
human_evidence: NOT_RUN
```

## Incident

기존 Stage 1 정본은 Ward 본진에 보이는 일반병 병영과 농장이 사전 구축된다고 기록했다. 그러나 사용자는 본진 건물을 제거하고, 본진에는 건설 노드 4개·방어탑 2개, 각 전진기지에는 건설 노드 2개·방어탑 1개를 배치하도록 확정했다. 이전 generated candidate는 전진기지의 단일 노드만 설명했고, 본진 node/tower 수를 소유하지 못했다.

## Impact

- 지도는 전장보다 건물 설명 보드처럼 보일 위험이 있었다.
- Stage 1의 첫 룰렛 동선과 보이는 병영·농장 규칙이 서로 충돌했다.
- 실제 `BuildingService`는 전진기지 배열 노드를 받을 수 있지만, `BaseState`에는 본진 node/tower 상태가 없어 이미지·문서만으로 구현 가능을 주장할 수 없었다.

## Solution

```text
VISIBLE_HOME_PRODUCTION_BUILDINGS = REMOVED
HOME_BASE = COMMAND_ROOT + 4_EMPTY_NODE_PADS + 2_FIXED_TOWERS
FORWARD_BASE = 2_EMPTY_NODE_PADS + FORWARD_BARRICADE + 1_FIXED_TOWER
STAGE_1 = VISIBLE_LOCKED_NODE_CAPACITY + NO_DIRECT_CONSTRUCTION
STARTING_MOBILIZATION_AND_CAPACITY = EXISTING_MAPRUN_BASELINE__NOT_A_VISIBLE_BUILDING
```

수량·state·시각 문법은 새 layout owner가 소유한다. 기존 v5 Forward Defense candidate는 역사적 discovery로 남기고, v5 Base Forward Node Layout board로 교체했다.

## Lesson

맵에서 시설의 외형을 제거할 때는 그 외형이 담당하던 **시각적 의미**와 현재 시스템의 **시작 효과**를 구분해야 한다. 둘을 동시에 삭제하거나 이미지에 남기면, player promise·FTUE·runtime model이 서로 다른 게임을 설명하게 된다.

## Base promotion

`NO_BASE_PROMOTION` — 교훈의 원인은 OMENWARD의 세 전선·Stage 1·룰렛 TokenSource 구조에 특화되어 있다. 공용 Base 정책으로 승격할 두 번째 프로젝트 evidence가 없다.
