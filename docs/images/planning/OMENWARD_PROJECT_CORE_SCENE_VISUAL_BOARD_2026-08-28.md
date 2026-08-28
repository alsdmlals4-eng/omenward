# OMENWARD Project Core Scene Visual Board · 2026-08-28

```yaml
board_id: OMW-VISUAL-BOARD-20260828-STORYBOOK-SD-THREE-FRONT-01
decision_id: OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01
revision_issue: 241
board_revision_issue: 243
map_only_revision_issue: 245
status: GENERATED_EXPLORATION__USER_REVIEW_PENDING
revision: v4__DUAL_CITADEL_MAP_ONLY
map_topology: ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT
front_structure: ONE_WARD_CITADEL_ROOT -> THREE_SHARED_FRONTS -> ONE_VEIL_CITADEL_ROOT
route_state_grammar: WARD_CITADEL_HOME_BASE -> WARD_FORWARD_BASE -> CONTESTED_CLASH_ZONE -> VEIL_FORWARD_BASE -> VEIL_CITADEL_HOME_BASE
board_scope: STRATEGIC_MAP_ONLY__LOWER_UI_STORYBOARD_REMOVED
roulette_system: RETAINED__NOT_VISUALIZED_IN_CURRENT_MAP_ONLY_BOARD
file: docs/images/planning/generated/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v4_DUAL_CITADEL_MAP_ONLY.png
sha256: F2474F7816D86DCCAE4C93E55E8A02CA1DB92BE9043342B7360EF66C19A4E7B2
supersedes: docs/images/planning/generated/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v3_FORWARD_BASES_AND_CLASH_ZONES.png__SUPERSEDED__VEIL_ROOT_AND_MAP_ONLY_SCOPE_CORRECTED
provenance: BUILT_IN_IMAGEGEN__USER_PROVIDED_REFERENCE_IMAGES_STYLE_AND_COMPOSITION_ONLY
rights_status: PLANNING_REFERENCE_ONLY__NOT_RUNTIME_ASSET__NOT_RELEASE_RIGHTS_PASS
```

## Purpose

이 보드는 새 그림체와 세 전선 전략 지도 UI가 Omenward의 핵심 인과를 설명하는지 검수하기 위한 planning visualization이다.

정확한 구조·상태는 repository/Notion의 책임 문서가 소유한다. **no pseudo-text used as structured truth**.

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
| Main map | Ward/Veil 양측의 세 전선 pressure·route·전진기지·접전지 관계를 동시에 읽는다 | Ward root → Ward forward base → clash zone → Veil forward base → Veil root의 3개 shared front | actual target-resolution legibility |

## Consistency review

- Character identity: compact SD, shield/banner/weapon silhouette first.
- Palette/value: warm ivory paper, navy/gold ally emphasis, restrained violet Veil threat.
- Camera: wide orthographic strategic map; no single-front auto zoom.
- Map topology: one Ward Citadel root and one Veil Citadel root; the same three fronts diverge from each side and meet at three central clash zones. Independent extra home bases are rejected.
- Route state grammar: every branch shows one Ward forward base, one contested clash zone, and one Veil forward base. Both forward bases are route outposts, not home bases.
- Board scope: the map fills the board. No lower roulette, cards, result/review panels, or pseudo-text. Roulette remains a retained system for its separate UI specification.
- Variation: terrain and Veil density may vary by front without changing the common grammar.
- Reference safety: no reference character, label, logo, or exact map layout is a product input.
