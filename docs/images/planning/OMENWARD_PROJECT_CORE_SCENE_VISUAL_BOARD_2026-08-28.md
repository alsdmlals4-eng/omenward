# OMENWARD Project Core Scene Visual Board · 2026-08-28

```yaml
board_id: OMW-VISUAL-BOARD-20260828-STORYBOOK-SD-THREE-FRONT-01
decision_id: OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01
revision_issue: 241
board_revision_issue: 243
map_only_revision_issue: 245
status: USER_CONFIRMED_PLANNING_LOCK__NOT_RUNTIME_ASSET
revision: v6__OPEN_BATTLEFIELD_NO_BARRICADE
map_topology: ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT
front_structure: ONE_WARD_CITADEL_ROOT -> THREE_SHARED_FRONTS -> ONE_VEIL_CITADEL_ROOT
route_state_grammar: WARD_CITADEL_HOME_BASE -> WARD_FORWARD_BASE -> CONTESTED_CLASH_ZONE -> VEIL_FORWARD_BASE -> VEIL_CITADEL_HOME_BASE
board_scope: STRATEGIC_MAP_ONLY__LOWER_UI_STORYBOARD_REMOVED
roulette_system: RETAINED__NOT_VISUALIZED_IN_CURRENT_MAP_ONLY_BOARD
layout_decision: OMW-PLAN-20260828-OPEN-BATTLEFIELD-TOWER-ONLY-01
file: docs/images/planning/generated/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v6_OPEN_BATTLEFIELD_NO_BARRICADE.png
sha256: 92A0922212ED62AAE30723FDFD97E13D61D37168F950A236104A2A1EB6F8D94D
supersedes: docs/images/planning/generated/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v5_BASE_FORWARD_NODE_LAYOUT.png__SUPERSEDED__OPEN_TERRAIN_NO_FENCE_NO_BARRICADE_REQUIRED
provenance: BUILT_IN_IMAGEGEN__USER_PROVIDED_REFERENCE_IMAGES_STYLE_AND_COMPOSITION_ONLY
rights_status: PLANNING_REFERENCE_ONLY__NOT_RUNTIME_ASSET__NOT_RELEASE_RIGHTS_PASS
visual_direction_lock_packet: docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_V6_VISUAL_DIRECTION_LOCK_2026-08-29.md
user_confirmation: 2026-08-29__USER_CONFIRMED_IN_CHAT
```

## Purpose

이 보드는 새 그림체와 세 전선 전략 지도 UI가 Omenward의 핵심 인과를 설명하는지 검수하기 위한 planning visualization이다.

v6는 사용자가 현재 planning visual direction으로 확정했다. 확정 범위는 열린 전장 지도 문법이며, 이 이미지 자체의 runtime asset·Godot 적용·human usability·player experience·release rights 승격은 아니다.

정확한 구조·상태는 repository의 `APPROVED_OMENWARD_OPEN_BATTLEFIELD_TOWER_ONLY_FORWARD_LAYOUT_2026-08-28.md`가 소유한다. **no pseudo-text used as structured truth**.

```text
PROJECT_CORE_SCENE_VISUAL_BOARD
= AI_PROJECT_UNDERSTANDING + PLAYER_FLOW_REVIEW + VISUAL_DIRECTION_CHECK
!= runtime asset batch
!= completed Godot UI/Scene
!= human usability or player experience evidence
```

## Panel read

| Panel | Screen / player goal | Board evidence | Unresolved scope |
|---|---|---|---|
| Main map | Ward/Veil 양측의 세 전선 pressure·route·전진기지·접전지·건설 수용량을 동시에 읽는다 | 양 본진은 열린 지형의 패드 4개·고정탑 2개, 각 전진기지는 패드 2개·고정탑 1개만 가진 3개 shared front | actual target-resolution legibility |

## Consistency review

- Character identity: compact SD, shield/banner/weapon silhouette first.
- Palette/value: warm ivory paper, navy/gold ally emphasis, restrained violet Veil threat.
- Camera: wide orthographic strategic map; no single-front auto zoom.
- Map topology: one Ward Citadel root and one Veil Citadel root; the same three fronts diverge from each side and meet at three central clash zones. Independent extra home bases are rejected.
- Root grammar: each root has exactly four empty construction pads and exactly two fixed towers embedded in open terrain; visible barracks/farms, fences, walls, enclosed rings, and additional root towers are absent.
- Route state grammar: every branch shows one Ward forward base, one contested clash zone, and one Veil forward base. Every forward base has exactly two empty pads and one fixed tower, with no barricade, fence, gate, or closed outpost ring. Both forward bases are route landmarks, not home bases.
- Open battlefield grammar: terrain, banners, faction color, unit mass, smoke, craters, shallow streams, and stone debris distinguish space. The pads remain discoverable fixed choices, not a freeform terrain-building grid.
- Board scope: the map fills the board. No lower roulette, cards, result/review panels, or pseudo-text. Roulette remains a retained system for its separate UI specification.
- Variation: terrain and Veil density may vary by front without changing the common grammar.
- Reference safety: no reference character, label, logo, or exact map layout is a product input.
