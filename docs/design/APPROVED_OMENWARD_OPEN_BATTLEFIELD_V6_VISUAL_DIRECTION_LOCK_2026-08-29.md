# [현행] OMENWARD 열린 전장 v6 Visual Direction Lock Packet

```yaml
packet_id: OMW-VISUAL-LOCK-20260829-OPEN-BATTLEFIELD-V6-01
decision_id: OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01
layout_decision_id: OMW-PLAN-20260828-OPEN-BATTLEFIELD-TOWER-ONLY-01
approved_at: 2026-08-29 KST
approval: USER_CONFIRMED_IN_CHAT
status: USER_CONFIRMED_CURRENT__PLANNING_LOCKED__NOT_RUNTIME_IMPLEMENTED
selected_candidate: OMW-VISUAL-BOARD-20260828-STORYBOOK-SD-THREE-FRONT-01__V6_OPEN_BATTLEFIELD_NO_BARRICADE
board_file: docs/images/planning/generated/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v6_OPEN_BATTLEFIELD_NO_BARRICADE.png
board_sha256: 92A0922212ED62AAE30723FDFD97E13D61D37168F950A236104A2A1EB6F8D94D
scope: PLANNING_VISUAL_DIRECTION_AND_STRATEGIC_MAP_GRAMMAR_ONLY
product_code_authority: NONE
runtime_asset: NOT_CREATED
runtime: NOT_RUN
human_usability: NOT_RUN
player_experience: NOT_RUN
rights_status: PLANNING_REFERENCE_ONLY__NOT_RUNTIME_ASSET__NOT_RELEASE_RIGHTS_PASS
repository_destination: docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_V6_VISUAL_DIRECTION_LOCK_2026-08-29.md
notion_destination: NONE__REPOSITORY_ONLY_POLICY
```

## 1. Selected candidate and reason

사용자는 v6 열린 전장 보드를 확정했다. 이 선택은 단일 Ward 본진과 단일 Veil 본진에서 세 shared front가 갈라지고 다시 맞물리는 구조를, 울타리·성벽·고정 전진 바리케이드 없이 전투 흔적과 작은 병력 군집으로 읽게 한다.

```text
ADOPTED = OPEN_TERRAIN + DISCOVERABLE_FIXED_PADS + FIXED_AUTO_TOWERS + THREE_SHARED_FRONTS
REJECTED = FENCED_OR_ENCLOSED_BASES + FIXED_FORWARD_BARRICADES + PARALLEL_THREE_LANE_ROADS + FREEFORM_TERRAIN_GRID_BUILDING
SELECTION_REASON = 세 전선의 압력·비가역 커밋·안정 점령 뒤 고정 패드 선택을 한 화면에서 읽게 하되, 전장이 작은 요새 보드나 다른 게임의 복제로 보이지 않게 한다.
```

## 2. Global and layer anchors

| Layer | Confirmed anchor |
|---|---|
| Global style | `STORYBOOK_WATERCOLOR_SD_TACTICAL_ILLUSTRATION`; ivory paper, delicate blue-gray ink, soft watercolor, restrained pixel tactility |
| Character | 2.5~3등신 SD 전술 미니어처. shield/banner/weapon/role silhouette가 장식보다 먼저 읽힌다. |
| Environment | 열린 전장 지형, 얕은 물길·분화구·바위 능선·연기·손상 석재를 사용한다. Ward/Veil 본진은 각각 하나이며, 건물 군집·성벽·울타리 없이 지휘 표식, fixed tower, construction pad로만 읽힌다. |
| UI | 지도 우선. 얇은 종이 패널·상징 아이콘·제한된 금색 강조를 사용한다. 이 board에는 하단 룰렛·카드·결과 UI를 넣지 않는다. |
| VFX | 작은 별빛, ward 문장 광택, 제한된 Veil rift glow만 사용한다. 전황을 가리는 flash·shake·폭발 연출은 허용하지 않는다. |

## 3. Confirmed flow / screen anchors

```text
PREPARE: 세 전선의 forecast pressure와 route를 비교한다.
ROULETTE: 별도 3×3 UI에서 병력 분포를 설계한다. 이 map-only board에는 표현하지 않는다.
COMMIT: 획득 병력을 세 전선 중 하나에 비가역으로 커밋한다.
BATTLE: 하나의 전략 지도에서 Ward/Veil 전진, 세 접전지, 보조 탑 화력을 읽는다.
REVIEW: forecast → design → commit → outcome의 인과를 복기한다.
```

## 4. Map grammar

```text
MAP_TOPOLOGY = ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT
ROUTE_STATE_GRAMMAR = WARD_CITADEL_HOME_BASE -> WARD_FORWARD_BASE -> CONTESTED_CLASH_ZONE -> VEIL_FORWARD_BASE -> VEIL_CITADEL_HOME_BASE
HOME_BASE_PER_FACTION = 4_DISCOVERABLE_FIXED_CONSTRUCTION_PADS + 2_FIXED_AUTO_ATTACK_TOWERS
FORWARD_BASE_PER_SIDE_PER_FRONT = 2_DISCOVERABLE_FIXED_CONSTRUCTION_PADS + 1_FIXED_AUTO_ATTACK_TOWER
FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL
FENCED_OR_ENCLOSED_BASE_BOUNDARY = FORBIDDEN
BUILD_PLACEMENT_FREEDOM = DISCOVERABLE_FIXED_PADS_IN_OPEN_TERRAIN__NOT_FREEFORM_TERRAIN_GRID
```

## 5. Keep / Avoid / Do Not Drift / allowed variation

| Keep | Avoid | Do Not Drift | Allowed variation |
|---|---|---|---|
| 동시 세 전선, Ward navy/ivory와 Veil charcoal/violet의 명도 위계, 전장-primary, small-unit silhouette, 열린 지형에서 보이는 fixed pad | 벽·울타리·원형 거점·고정 바리케이드, 본진 생산 건물, 독립 본진 세 개, 병렬 도로, dense per-unit minimap, 하단 roulette storyboard | player-constructed probability engine, reel-to-lane fixed mapping 금지, 비가역 commit, 단일 양쪽 본진과 세 shared front | branch마다 식생·물길·석재·안개·Veil 균열 밀도·피해 흔적은 달라질 수 있다. topology, counts, material language, faction hierarchy, route-state 의미는 바꾸지 않는다. |

## 6. Superseded references and provenance

- v1~v5 planning board는 v6의 열린 지형·no-fence·no-fixed-barricade grammar에 의해 superseded다.
- `OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1`는 현 build consumer만 보유한 legacy runtime asset이다. 이 lock이 교체·삭제·style-fit 통과를 뜻하지 않는다.
- 사용자가 제공한 이미지와 Commander Quest, Thronefall, Cataclismo은 reference/benchmark only다. 캐릭터·UI·로고·고유 배치·표현을 복제하지 않는다.
- v6는 built-in ImageGen으로 만든 planning visualization이다. independent source asset, product runtime asset, commercial/release rights pass가 아니다.

## 7. Phase 2 boundary and destination readback

```text
NEXT_GATE = PHASE2_OPEN_BATTLEFIELD_READINESS_REVIEW__ISSUE_RED_TEST_PROVENANCE_TARGET_RESOLUTION_REQUIRED
PHASE2_START_REQUIRES = FRESH_MAIN_AND_OPEN_WORK_ITEM_READ / ISSUE / RED_TEST / IMPLEMENTATION_PACKET / PROVENANCE_REVIEW / TARGET_RESOLUTION_RUNTIME_QA
NOTION_WRITE = FORBIDDEN__REPOSITORY_ONLY_POLICY
DESTINATION_READBACK = REQUIRED_ON_EXACT_PR_HEAD_AND_POSTMERGE_MAIN
```

This packet locks planning visual grammar only. It does not create a Godot Scene, Resource, UI, runtime asset, user-play evidence, or release-rights approval.
