# [현행] OMENWARD Handoff Context

```yaml
updated_at: 2026-08-25
status: PAUSED_QUEUED_AFTER_VISUAL_CLOSEOUT
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
current_visual_decision: OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01
current_visual_asset: OM-IMG-023
current_visual_handoff: docs/handoffs/2026-08-25-front-state-visual-approved-closeout.md
implementation_execution: NOT_RESUMED
visual_generation: STOPPED_AFTER_APPROVED_CLOSEOUT
```

This file is the short restart router. Detailed current visual/handoff truth is owned by:

- `docs/handoffs/2026-08-25-front-state-visual-approved-closeout.md`
- `docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md`
- `docs/images/planning/canonical/OMENWARD_APPROVED_FRONT_STATE_VISUAL_2026-08-25.md`

## New-session read order

1. fresh Base current `main`, authority, relevant Skill, open PRs;
2. fresh OMENWARD default branch, latest commit, open PRs/issues;
3. `AGENTS.md`;
4. `docs/CURRENT_CONFIRMED_DECISIONS.md`;
5. `docs/ACTIVE_CONTEXT.md`;
6. `docs/handoffs/2026-08-25-front-state-visual-approved-closeout.md`;
7. Notion Home + Visual Bible + Visual Components;
8. full-resolution approved image from Drive ID `1-JRf4q95wZm51DsEYPH_-hnH_GLEIAQ5`;
9. current GDD/Project Core and relevant detailed owner;
10. Google Sheet only as compatibility/history.

## Current visual truth

```text
BATTLEFIELD_PRESENTATION = THREE_SIMULTANEOUS_FRONT_STATE_VIEWS
PER_FRONT_MINIMAP = REQUIRED
MINIMAP_IS_CONTEXT_NOT_SECOND_BATTLEFIELD = TRUE
VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
COMMANDER_ROLE_ANCHOR = LONG_COMMAND_FLAG
APPROVED_VISUAL = OM-IMG-023
```

The approved visual is a `1536x1024 PNG` stored in Drive and shown as a Notion-native inline preview on Home/Visual Bible. The old North Star v2.1, long-road layout, no-minimap rule and standalone Anime-Pixel/Clean-Pixel style are historical/partial references where they conflict with the 2026-08-25 Decision.

## Protected product identity

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

Omen Warden is a commander, not primarily a melee hero. Keep three-front strategic responsibility, 3x3 roulette/direct arrows, irreversible front commitment, auto-battle, PREPARE -> COMMIT -> BATTLE -> REVIEW, silhouette-first troops and allied-vs-Veil contrast.

## Evidence ceiling

```text
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_UI_RUNTIME = NOT_RUN
CURRENT_MINIMAP_READABILITY = NOT_RUN
CURRENT_SD_UNIT_RUNTIME_READABILITY = NOT_RUN
CURRENT_HUMAN_USABILITY = NOT_RUN
CURRENT_PLAYER_EXPERIENCE = NOT_RUN
```

Visual approval is not runtime or player-experience proof.

## Closeout

OMENWARD is paused/queued after this visual closeout. Do not automatically resume Godot/runtime work or generate another image. Resume only after an explicit user request and a fresh authority/readback pass.

Base reusable workflow lesson is tracked separately as `BCP-2026-032-visual-canon-approval-override-and-handoff-integrity`; proposal submission does not authorize active Base implementation.
