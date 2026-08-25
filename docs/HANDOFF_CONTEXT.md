# [현행] OMENWARD Handoff Context

```yaml
updated_at: 2026-08-25
status: PAUSED_QUEUED_AFTER_VISUAL_CLOSEOUT
handoff_packet_state: PACKET_READY
receiver_state: PENDING_RECEIVER_ACK
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
current_visual_decision: OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01
current_visual_asset: OM-IMG-023
current_visual_handoff: docs/handoffs/2026-08-25-front-state-visual-approved-closeout.md
implementation_execution: NOT_RESUMED
visual_generation_policy: USER_REQUEST_ONLY
visual_generation: STOPPED_AFTER_APPROVED_CLOSEOUT
prepared_from_project_main_sha: 4e10ea441ecf537e4bef5af9d1991ddf99be217d
prepared_with_base_main_sha: 6726d23276b8a808a6d49d51ad6081c6c96f8f72
```

This file is the short restart router. It is a **sender packet**, not proof that a future chat has accepted control. A new chat must fresh-read current GitHub + Notion + applicable instructions and produce a `receiver_ack` before any persistent mutation. If current canon differs from this packet, use `CONTEXT_DRIFT_RECHECK_REQUIRED`, not the packet as a frozen source of truth.

Detailed current visual/handoff truth is owned by:

- `docs/handoffs/2026-08-25-front-state-visual-approved-closeout.md`
- `docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md`
- `docs/images/planning/canonical/OMENWARD_APPROVED_FRONT_STATE_VISUAL_2026-08-25.md`

## New-session read order

1. fresh Base current `main`, `AGENTS.md`, relevant Skill, open PRs;
2. fresh OMENWARD default branch, latest commit, open PRs/issues;
3. OMENWARD `AGENTS.md` and any nearer applicable instruction;
4. `docs/CURRENT_CONFIRMED_DECISIONS.md`;
5. `docs/ACTIVE_CONTEXT.md`;
6. this file + `docs/handoffs/2026-08-25-front-state-visual-approved-closeout.md`;
7. current visual spec + approved asset record;
8. Notion Home + Visual Bible + Visual Components;
9. full-resolution approved image from Drive ID `1-JRf4q95wZm51DsEYPH_-hnH_GLEIAQ5`;
10. current GDD/Project Core and relevant detailed owner;
11. Google Sheet only as compatibility/history; report conflicts rather than letting stale Sheet values override GitHub/Notion;
12. inspect code/runtime only after explicit user reactivation of that scope.

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

Omen Warden is a commander, not primarily a melee hero. Keep three-front strategic responsibility, 3x3 roulette/direct arrows, irreversible front commitment, auto-battle, `PREPARE -> COMMIT -> BATTLE -> REVIEW`, silhouette-first troops and allied-vs-Veil contrast.

## Evidence ceiling

```text
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_UI_RUNTIME = NOT_RUN
CURRENT_MINIMAP_READABILITY = NOT_RUN
CURRENT_SD_UNIT_RUNTIME_READABILITY = NOT_RUN
CURRENT_HUMAN_USABILITY = NOT_RUN
CURRENT_PLAYER_EXPERIENCE = NOT_RUN
RIGHTS_REVIEW = NOT_RUN
NOTION_SERVER_READBACK = PASS
NOTION_HUMAN_VISIBLE_CLIENT = NOT_RUN
```

Visual approval is not runtime, rights, accessibility, device or player-experience proof.

## Resume checkpoint / side-effect ledger

```yaml
last_safe_checkpoint: >-
  OM-IMG-023 user approval recorded; full-resolution PNG persisted in Drive;
  current visual Decision/spec/router/handoff prepared on PR #210; Notion Home and
  Visual Bible contain current approved inline preview with server readback; Sheet
  image planning/review rows contain OM-IMG-023; Base proposal/evidence exists as PR #693.
next_safe_action: >-
  In a new chat, fresh-read current Base + OMENWARD + Notion, compare packet baseline
  against observed current main/PR states, read back current state/protected scope,
  then record receiver_ack before any persistent mutation.
side_effects_already_applied:
  - OM-IMG-023 generated and user-approved
  - full-resolution PNG uploaded to Drive file 1-JRf4q95wZm51DsEYPH_-hnH_GLEIAQ5
  - Notion Home current approved preview attached and server-read back
  - Notion Visual Bible current approved preview attached and server-read back
  - Sheet 71/72 OM-IMG-023 planning/review records written
  - OMENWARD current-task PR #210 created and carries visual closeout/handoff work
  - Base proposal PR #693 carries BCP-2026-033 OMENWARD visual-canon/handoff lessons
  - accidental placeholder main write 7013d52 was already reverted by 4e10ea4; do not repeat either mutation
idempotency:
  retry_safe: false
  verify_before_retry:
    - do not re-upload OM-IMG-023 unless the durable Drive file is missing or hash differs
    - do not recreate BCP-2026-033 while Base PR #693 exists
    - do not recreate or duplicate PR #210
    - do not repeat Notion attachment/upload if current image block readback already passes
```

## Pending decisions / reactivation gate

```yaml
pending_user_decisions: []
approval_required_before_resume: false
reactivation_required_before_product_or_runtime_mutation: true
safe_work_before_reactivation:
  - fresh-read current authorities
  - inspect current PR/Issue/Notion/Sheet state read-only
  - report drift/conflicts
```

The user has approved the current visual. There is no unresolved visual choice in this packet. Product/runtime implementation remains paused and must not restart merely because this handoff exists.

## Instruction / freshness receipt

```yaml
instruction_surface_readback:
  base_root_agents: PASS_AT_BASE_6726d23276b8a808a6d49d51ad6081c6c96f8f72
  project_root_agents: PASS_ON_PR210_BRANCH
  nearest_applicable_agents: RECHECK_ON_RESUME
  project_visual_router: PASS_ON_PR210_BRANCH
prepared_from_main_sha: 4e10ea441ecf537e4bef5af9d1991ddf99be217d
resume_observed_main_sha: RESOLVE_FRESH_IN_RECEIVER_SESSION
canon_freshness: PENDING_RECEIVER_RECHECK
```

`prepared_from_main_sha != resume_observed_main_sha` is expected after PR #210 is merged; the receiver must verify that the new main contains this handoff and current Decision rather than treating the SHA change itself as failure.

## Context sanitation

```yaml
canonical_read_order_count: 7_CORE_LOCATORS_PLUS_CURRENT_EXTERNAL_SURFACES
raw_tool_logs_included: false
full_transcript_required: false
superseded_material_included_only_if_needed: true
```

Do not require this conversation transcript to resume. Use current repository/Notion owners and the approved asset locator.

## GitHub / Base learning boundary

- OMENWARD PR #210 is the current visual/handoff workstream until integrated.
- PR #209 and PR #205 are other workstreams and stay read-only unless explicitly named.
- Base PR #693 is the existing proposal-only `BCP-2026-033-visual-canon-approval-and-handoff-integrity` submission with OMENWARD problem/lesson evidence. Do not duplicate or mutate that open Base PR from this project closeout.
- Proposal submission is not active Base implementation authority.

## Transfer state

The sender can close this work as:

```text
PACKET_READY
PENDING_RECEIVER_ACK
```

Only a future fresh chat/receiver that has performed the readback above may set `TRANSFER_ACCEPTED`. Until then, do not claim the handoff has been accepted.