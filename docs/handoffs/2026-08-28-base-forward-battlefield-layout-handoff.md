# OMENWARD 본진·전진기지 전장 배치 Handoff · 2026-08-28

```yaml
handoff_id: OMW-HANDOFF-20260828-BASE-FORWARD-BATTLEFIELD-LAYOUT-01
status: SUPERSEDED_RESTART_ROUTER__OPEN_BATTLEFIELD_TOWER_ONLY_SUCCESSOR
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
current_layout_owner: docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_TOWER_ONLY_FORWARD_LAYOUT_2026-08-28.md
current_visual_board: docs/images/planning/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28.md
repository_human_facing_canon: true
notion_current_authority: RETIRED__NO_FUTURE_READ_OR_WRITE
current_gate: HISTORICAL__USER_CONFIRM_REVISED_BASE_FORWARD_BATTLEFIELD_PLANNING_BOARD
product_code_authority: NONE_FOR_BASE_FORWARD_LAYOUT
successor_handoff: docs/handoffs/2026-08-28-open-battlefield-tower-only-layout-handoff.md
```

## Historical snapshot (superseded)

```text
HOME_BASE = 4_EMPTY_CONSTRUCTION_PADS + 2_FIXED_AUTO_ATTACK_TOWERS + NO_VISIBLE_PRODUCTION_BUILDINGS
FORWARD_BASE = 2_EMPTY_CONSTRUCTION_PADS + 1_FORWARD_BARRICADE + 1_FIXED_AUTO_ATTACK_TOWER__HISTORICAL_ONLY
MAP = ONE_WARD_ROOT -> THREE_SHARED_FRONTS -> ONE_VEIL_ROOT
STAGE_1 = SHOW_CAPACITY_LOCKED__NO_DIRECT_CONSTRUCTION
CURRENT_BOARD = V5_BASE_FORWARD_NODE_LAYOUT__GENERATED_EXPLORATION__SUPERSEDED
```

병영·농장은 지도 위 본진 건물로 보이지 않는다. 이 시각 삭제는 기존 MapRun 시작 baseline 자체의 삭제가 아니며, 실제 starting mobilization/capacity를 새 model로 바꾸는 일은 Phase 2 구현 계약에서만 다룬다.

## 실제 구현 대조

- 전진기지: `BuildingService.register_outpost(..., node_ids: Array)`가 여러 node ID를 받으므로 기지당 2개 노드로의 데이터 확장 기반은 있다.
- 본진: `BaseState`와 `BattleSimulator`에는 본진 4 node/2 tower의 state·소유·잠금·combat consumer가 없다.
- 고정 바리케이드·고정 자동공격탑: 새 런타임 consumer가 없다.
- 따라서 새 배치는 `CONFIRMED__PLANNING_ONLY__NOT_IMPLEMENTED`다. 이미지/문서만으로 Godot 적용 또는 runtime PASS를 주장하지 않는다.

## 최근 검증 ceiling

현재 `main` 기반에서 headless editor import와 Roulette/Economy, C2 battle objective, Run Command phase contract 테스트는 다시 실행했다. 테스트 자체는 통과했지만, 새 배치의 runtime은 실행하지 않았고 종료 시 ObjectDB/RID cleanup warning은 별도 원인 분석 전까지 남는다.

```text
NEW_LAYOUT_RUNTIME = NOT_RUN
NEW_LAYOUT_TARGET_RESOLUTION_READABILITY = NOT_RUN
NEW_LAYOUT_HUMAN_USABILITY = NOT_RUN
NEW_LAYOUT_PLAYER_EXPERIENCE = NOT_RUN
```

## Historical next work

1. 이 historical v5 board 대신 successor v6 open-battlefield board를 사용자가 확정/수정한다.
2. 확정 뒤 Visual Lock Packet에 adopted/rejected elements와 Keep/Avoid/Do Not Drift를 기록한다.
3. Phase 2를 열려면 별도 Issue, RED 테스트, Resource/State/UI implementation packet, target-resolution 검증이 필요하다.

과거 `2026-08-26-gpt-work-image-production-handoff.md`의 Notion entry point와 당시 이미지 작업 상태는 historical discovery다. 현재 재시작에서 Notion을 읽거나 쓰지 않는다.
