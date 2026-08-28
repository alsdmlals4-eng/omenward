# OMENWARD · 열린 전장 / 탑 전용 배치 Handoff

```yaml
handoff_id: OMW-HANDOFF-20260828-OPEN-BATTLEFIELD-TOWER-ONLY-01
updated_at: 2026-08-28
status: CURRENT_RESTART_ROUTER
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
notion_current_authority: RETIRED__NO_FUTURE_READ_OR_WRITE
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
layout_owner: docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_TOWER_ONLY_FORWARD_LAYOUT_2026-08-28.md
planning_board_owner: docs/images/planning/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28.md
current_gate: USER_CONFIRM_OPEN_BATTLEFIELD_TOWER_ONLY_PLANNING_BOARD
product_code_authority: NONE_FOR_OPEN_BATTLEFIELD_LAYOUT
runtime: NOT_RUN
human_usability: NOT_RUN
player_experience: NOT_RUN
new_layout_runtime: NOT_RUN
new_layout_human_usability: NOT_RUN
new_layout_player_experience: NOT_RUN
```

## Current decision

```text
MAP_TOPOLOGY = ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT
HOME_BASE = 4_FIXED_CONSTRUCTION_PADS + 2_FIXED_AUTO_ATTACK_TOWERS
FORWARD_BASE = 2_FIXED_CONSTRUCTION_PADS + 1_FIXED_AUTO_ATTACK_TOWER
FORWARD_BASE_FIXED_DEFENSE_STACK = AUTO_ATTACK_TOWER_ONLY
FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL
FENCED_OR_ENCLOSED_BASE_BOUNDARY = FORBIDDEN
BUILD_PLACEMENT_FREEDOM = DISCOVERABLE_FIXED_PADS_IN_OPEN_TERRAIN__NOT_FREEFORM_TERRAIN_GRID
STAGE_1_DIRECT_CONSTRUCTION = FORBIDDEN
OCCUPATION_NODE_ACTIVATION = STABLE_PLAYER_OWNED_OUTPOST_ONLY
TACTICAL_COMMAND_BARRICADE = OUT_OF_SCOPE__RETAINED
NEW_LAYOUT_RUNTIME = NOT_RUN
NEW_LAYOUT_HUMAN_USABILITY = NOT_RUN
NEW_LAYOUT_PLAYER_EXPERIENCE = NOT_RUN
```

## Planning board

```text
PLANNING_BOARD = OMW-VISUAL-BOARD-20260828-STORYBOOK-SD-THREE-FRONT-01__V6_OPEN_BATTLEFIELD_NO_BARRICADE
PLANNING_BOARD_FILE = docs/images/planning/generated/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v6_OPEN_BATTLEFIELD_NO_BARRICADE.png
PLANNING_BOARD_SHA256 = 92A0922212ED62AAE30723FDFD97E13D61D37168F950A236104A2A1EB6F8D94D
PLANNING_BOARD_STATUS = GENERATED_EXPLORATION__USER_CONFIRM_PENDING
PLANNING_BOARD_RIGHTS = PLANNING_REFERENCE_ONLY__NOT_RUNTIME_ASSET__NOT_RELEASE_RIGHTS_PASS
```

v6는 세 shared front의 넓은 접전지, 지형별 엄폐물·물길·분화구·연기와 작은 병력 군집을 사용한다. 울타리, 성벽, 닫힌 거점 링, 고정 바리케이드는 없다. 사용자 제공 이미지는 전장 밀도와 자유로운 지면 감각을 읽기 위한 reference-only input이며, 캐릭터·UI·로고·고유 배치의 제품 자산/복제 입력이 아니다.

## Implementation boundary and next route

실제 코드 재대조 결과 `BuildingService.register_outpost(..., node_ids: Array)`는 다중 node 배열을 받을 기반이 있지만, `scripts/core/stage_run.gd`는 현행 3 node만 등록한다. home node·fixed tower·open terrain map의 runtime consumer는 아직 없다. 따라서 이 handoff는 새 Scene/Resource/data/UI 구현, runtime asset 적용, 수치 확정, 가독성 PASS를 승인하지 않는다.

다음 작업자는 fresh Base/main/open PR·Issue를 읽고, 사용자가 v6를 확정한 뒤에만 `VISUAL_DIRECTION_LOCK_PACKET`을 만든다. 그 뒤 Phase 2 issue·RED test·provenance review·target-resolution runtime QA를 별도로 통과해야 구현을 시작할 수 있다.
