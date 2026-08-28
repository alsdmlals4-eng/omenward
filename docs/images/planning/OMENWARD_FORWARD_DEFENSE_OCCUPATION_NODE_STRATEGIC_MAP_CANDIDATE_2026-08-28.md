# OMENWARD 전진 방어·점령 노드 전략 지도 시안 · 2026-08-28

```yaml
candidate_id: OMW-VISUAL-CANDIDATE-20260828-FORWARD-DEFENSE-OCCUPATION-NODES-01
status: SUPERSEDED__BASE_FORWARD_NODE_COUNTS_AND_HOME_PRODUCTION_REMOVAL
parent_visual_decision: OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01
parent_gameplay_decision: OMW-PLAN-20260828-FORWARD-DEFENSE-OCCUPATION-NODES-01
superseded_by: OMW-PLAN-20260828-BASE-FORWARD-BATTLEFIELD-CONSTRUCTION-LAYOUT-01
successor_board: docs/images/planning/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28.md
board_scope: STRATEGIC_MAP_ONLY
runtime_asset: false
scene_implemented: false
ui_implemented: false
human_usability: NOT_RUN
player_experience: NOT_RUN
generator: OpenAI image generation
file: docs/images/planning/generated/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v5_FORWARD_DEFENSE_OCCUPATION_NODES.png
bytes: 3630422
sha256: B854C284C9FCE036CA01F8F96E02407BE30A96818BA0E1C44FBB65CF2053924C
rights_status: PLANNING_REFERENCE_ONLY__NOT_RUNTIME_ASSET__NOT_RELEASE_RIGHTS_PASS
```

## 의도와 실제 소비처

이 시안은 `PROJECT_CORE_SCENE_VISUAL_BOARD`의 새 후보이며, 사용자와 AI가 전진기지의 플레이어 가치를 같은 방식으로 이해하는지 검증한다. 실제 소비처는 현재 **planning review**뿐이다. Godot Scene, UI, Resource, runtime asset을 대체하거나 새로 만들지 않는다.

```text
WARD_CITADEL_ROOT
→ THREE_SHARED_FRONT_BRANCHES
→ WARD_FORWARD_BASE (FORWARD_BARRICADE + AUTO_ATTACK_TOWER + EMPTY_CONSTRUCTION_NODE)
→ CONTESTED_CLASH_ZONE
→ VEIL_FORWARD_BASE (same structural grammar)
→ VEIL_CITADEL_ROOT
```

## 생성 입력과 제한

- 사용자 제공 이미지 1: 동화풍 수채화 SD·아이보리 종이·섬세한 잉크 선의 **style-only reference**.
- 사용자 제공 이미지 2: 한 화면에서 전선 상태를 읽는 넓은 전략 지도의 **layout-only reference**.
- 두 레퍼런스의 고유 구도, 글자, UI, 자산을 복사하지 않았다.
- 하단 룰렛·제어 덱·인셋 패널·읽을 수 있는 문구·pseudo-text를 제외했다.
- `FORWARD_BARRICADE`, `AUTO_ATTACK_TOWER`, `EMPTY_CONSTRUCTION_NODE`는 서로 다른 지도 문법으로 보이도록 요청했다. 정확한 시스템 정의는 이미지가 아니라 `docs/design/APPROVED_OMENWARD_FORWARD_DEFENSE_AND_OCCUPATION_NODE_CONTRACT_2026-08-28.md`가 소유한다.

## 시안 검수

| 점검 | 판정 | 근거 / 후속 검증 |
|---|---|---|
| 단일 Ward 본진에서 세 전선이 갈라지는가 | PARTIAL | 좌측 본진에서 상·중·하 전선으로 나뉘지만, 런타임 해상도에서 root/branch 읽힘은 아직 검증되지 않았다. |
| 세 전선이 동시에 읽히는가 | PARTIAL | 한 프레임에 모두 보이지만 인간 가독성 검증은 `NOT_RUN`이다. |
| 전진기지의 세 요소가 구분되는가 | PARTIAL | 펜스/관문형 저지물, 탑, 원형 빈 노드를 나눴다. 실제 게임 크기에서 아이콘·상태와 함께 읽히는지는 미검증이다. |
| 고정 방어가 점령/승리를 대신하지 않는가 | PASS_AS_PLANNING | 유닛은 접전지에만 작게 배치하고, 지도에 점령 보상·자동 승리 표현을 넣지 않았다. |
| Visual Lock 준수 | PARTIAL | storybook watercolor SD, ivory/ink, Ward-vs-Veil 대비는 맞춘다. 후보일 뿐 user lock 전 current visual board를 교체하지 않는다. |
| 권리·출처 | PARTIAL | 생성 provenance와 참조 역할은 기록했다. release/runtime rights PASS는 없다. |

## 잠금 전 상태

```text
KEEP_CANDIDATE = FALSE__HISTORICAL_DISCOVERY_ONLY
CURRENT_VISUAL_DIRECTION_REPLACED = FALSE
RUNTIME_PROMOTION = FORBIDDEN
NOTION_WRITE = FORBIDDEN
NEXT_USER_ACTION = REVIEW_SUCCESSOR_V5_BASE_FORWARD_NODE_LAYOUT
```

사용자가 잠금하면 이 후보의 adopted/rejected 요소와 drift guard를 current Visual Lock Packet에 반영한다. 거절하면 이 파일은 candidate history로 남기고, 문제 축만 고쳐 새 버전을 생성한다.
