# OMENWARD · Front-State Visual Approved Closeout Handoff · 2026-08-25

```yaml
handoff_state: PAUSED_QUEUED_AFTER_VISUAL_CLOSEOUT
handoff_packet_state: PACKET_READY
receiver_state: PENDING_RECEIVER_ACK
visual_decision: OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01
approved_visual: OM-IMG-023
approved_visual_record: docs/images/planning/canonical/OMENWARD_APPROVED_FRONT_STATE_VISUAL_2026-08-25.md
visual_spec: docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md
product_runtime_resumed: false
runtime_readability: NOT_RUN
human_usability: NOT_RUN
player_experience: NOT_RUN
image_generation_after_closeout: STOPPED
prepared_from_project_main_sha: 4e10ea441ecf537e4bef5af9d1991ddf99be217d
prepared_with_base_main_sha: 6726d23276b8a808a6d49d51ad6081c6c96f8f72
```

## 1. Restart purpose

This is the durable restart point for a new chat. Do not reconstruct the current visual direction from old conversation history or older North Star images. Fresh-read GitHub + Notion + applicable instructions, then use the exact approved Decision/asset below.

This file records a sender packet. `PACKET_READY` is not `TRANSFER_ACCEPTED`. A future receiver must compare current canon with this packet and explicitly acknowledge the current state, next action, protected scope, pending decisions and already-applied side effects before mutation.

## 2. Protected product identity

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

The player is the **Omen Warden**, a commander who reads omens, prepares a Ward Citadel, obtains troops through the mobilization/roulette system, irreversibly commits them to fronts, and observes auto-battle results with limited tactical intervention. The commander is not primarily a melee hero. Current role anchor: **long command flag**.

## 3. Current approved battlefield presentation

```text
TOP FRONT    = current clash/front-state view + its own minimap
MIDDLE FRONT = current clash/front-state view + its own minimap
BOTTOM FRONT = current clash/front-state view + its own minimap
LOWER AREA   = current Focus-adaptive Control Deck
```

Required:
- all three current front situations readable simultaneously;
- each front owns a minimap for progress/position, stronghold/defense line, route/infiltration/air context and relevant Boss/Siege position;
- minimaps are context surfaces, not miniature duplicate battlefields;
- long citadel-to-enemy roads are no longer the default composition.

## 4. Current approved visual style

```text
VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
MATERIAL_FINISH = HIGH_RES_PIXEL_TEXTURE_AND_RESTRAINED_LIGHTING
WORLD_TONE = FANTASY_WARD_CITADEL + MAGIC_WARFARE
NORMAL_COMBAT_UNIT_RULE = SILHOUETTE_FIRST
```

Allied visual language: navy, ivory, cool gray metal, restrained gold; arch/shield/banner/relic/vertical-line shapes; omen sigils and restrained arcane/sanctified geometry.

Veil language: black-purple, dark red, carapace gray, limited rift glow; asymmetric rift/carapace/spike/void-aperture shapes.

SD does not mean generic cute mobile chibi. Weapon, shield, wing, staff, armor and mass must define combat roles before faces/details.

## 5. Approved image — refetch, do not regenerate from memory

`OM-IMG-023` is the user-approved current visual reference.

Full-resolution authority:
- Drive ID: `1-JRf4q95wZm51DsEYPH_-hnH_GLEIAQ5`
- https://drive.google.com/file/d/1-JRf4q95wZm51DsEYPH_-hnH_GLEIAQ5/view?usp=drivesdk
- `1536x1024 PNG`
- SHA-256: `0326b012d1fbefba85b545086b84992051591edff6f3b7e159cf3e083f204224`

Human-facing current surfaces:
- Home: https://app.notion.com/p/3c41b237eb1c816fbbc8e2dddc18b6eb
- Visual Bible: https://app.notion.com/p/3c01b237eb1c81c38be5e3ee9f64b59d
- Visual Components: https://app.notion.com/p/3c21b237eb1c81e29be2d6ce397c9c85

Home and Visual Bible place a Notion-native inline preview of the approved image before the old North Star and link to the full-resolution Drive asset. Fresh destination fetch returned a Notion-hosted `prod-files-secure` image block on both pages. Visual Components carries the current override/contract and links back into the same current visual system. This proves server-side attachment/readback, not actual browser/device human-visible rendering.

## 6. Superseded assumptions

```text
LONG_FULL_ROAD_PRESENTATION_AS_DEFAULT = SUPERSEDED
NO_MINIMAP = SUPERSEDED
MINIMAP_NOT_REQUIRED = SUPERSEDED
ANIME_PIXEL_ART_AS_STANDALONE_CHARACTER_CANON = SUPERSEDED
CLEAN_PIXEL_ART_AS_STANDALONE_BATTLEFIELD_CANON = SUPERSEDED
NORTH_STAR_V2_1_AS_CURRENT_LAYOUT = SUPERSEDED_TO_REFERENCE
```

Retained from older work:
- battlefield-primary hierarchy;
- three fronts as simultaneous strategic responsibility;
- allied vs Veil contrast;
- compact lower Control Deck;
- role-silhouette readability;
- 3x3 roulette/direct arrows and `PREPARE -> COMMIT -> BATTLE -> REVIEW`.

## 7. Evidence boundary

The visual closeout did **not** resume product implementation.

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

The previously approved orchestration-first Run Command vertical-slice packet remains retained. A future session must fresh-read current authority before resuming it.

## 8. New-chat mandatory read order

1. Fresh Base main, root `AGENTS.md`, relevant Skill, open PRs.
2. Fresh OMENWARD default branch, latest commit, open PRs/issues.
3. OMENWARD `AGENTS.md` and any nearer applicable instruction.
4. `docs/CURRENT_CONFIRMED_DECISIONS.md`.
5. `docs/ACTIVE_CONTEXT.md`.
6. `docs/HANDOFF_CONTEXT.md` and this handoff.
7. Current visual spec and approved visual asset record.
8. Notion Home + Visual Bible + Visual Components and the full-resolution Drive image.
9. Current GDD/Project Core + relevant detailed owner; when older visual wording conflicts, the 2026-08-25 Decision wins.
10. Google Sheet only as compatibility/history and report conflicts.
11. Inspect code/runtime only after explicit user reactivation.

If a new image is requested, **refetch OM-IMG-023 first** and preserve approved composition/style unless the user explicitly changes it.

## 9. Resume checkpoint and idempotency

```yaml
last_safe_checkpoint: >-
  User-approved OM-IMG-023 is persisted and current human surfaces have passed Notion
  server readback; visual Decision/spec/current routing and closeout packet are present
  on the current-task PR; Sheet visual planning/review records exist; reusable Base
  problem/lesson proposal exists separately as Base PR #693.
next_safe_action: >-
  New receiver fresh-reads current authorities and destinations, compares observed state
  with this packet baseline, then records receiver_ack before any persistent mutation.
side_effects_already_applied:
  - OM-IMG-023 generated and user-approved
  - full-resolution approved PNG uploaded to Drive file 1-JRf4q95wZm51DsEYPH_-hnH_GLEIAQ5
  - current approved preview attached to Notion Home and read back
  - current approved preview attached to Notion Visual Bible and read back
  - Sheet OM-IMG-023 planning/review rows written
  - OMENWARD PR #210 created for this current visual/handoff workstream
  - Base PR #693 already contains BCP-2026-033 proposal + OMENWARD evidence + registry entry
  - accidental OMENWARD main placeholder write was already reverted and must not be repeated
idempotency:
  retry_safe: false
  verify_before_retry:
    - verify Drive ID/hash before any image re-upload
    - verify Notion image block before any new attachment
    - verify Base PR #693 before creating any BCP-033-like proposal
    - verify PR #210 state before opening another visual-closeout PR
```

## 10. Pending decisions / safe work

```yaml
pending_user_decisions: []
approval_required_before_resume: false
reactivation_required_before_product_or_runtime_mutation: true
safe_work_while_paused:
  - read-only authority freshness checks
  - current PR/Issue/Notion/Sheet readback
  - conflict/drift reporting
```

The approved visual itself does not require another approval. This handoff also does not reactivate Godot/runtime implementation.

## 11. Instruction and canon freshness snapshot

```yaml
instruction_surface_readback:
  base_root_agents: PASS_AT_6726d23276b8a808a6d49d51ad6081c6c96f8f72
  project_root_agents: PASS_ON_PR210_BRANCH
  nearest_applicable_agents: RECHECK_ON_RESUME
  current_visual_router: PASS_ON_PR210_BRANCH
prepared_from_main_sha: 4e10ea441ecf537e4bef5af9d1991ddf99be217d
resume_observed_main_sha: RESOLVE_FRESH_IN_RECEIVER_SESSION
canon_freshness: PENDING_RECEIVER_RECHECK
context_sanitation:
  raw_tool_logs_included: false
  full_transcript_required: false
  superseded_material_included_only_if_needed: true
```

A different project main SHA after PR #210 integration is expected. The receiver must verify that the new main contains this current Decision/handoff rather than blindly treating the expected postmerge SHA change as failure.

## 12. GitHub boundaries at closeout

- PR #210 owns this visual/handoff workstream until integrated.
- PR #209 is a different front-door documentation workstream and remains read-only.
- PR #205 is an older orchestration planning workstream and remains read-only.
- Never absorb/close/rebase/rewrite those other PRs without explicit named authorization.
- Fresh GitHub state always wins if these numbers later change.

## 13. Sheet conflict warning

Google Sheet `00_프로젝트_허브` is stale and still describes an older PR175/Issue176/runtime period. It is compatibility/history only. The 2026-08-25 visual Decision and `OM-IMG-023` rows in image planning/review tabs are newer. Do not use the stale hub to overwrite GitHub/Notion current state.

## 14. Base learning handoff

Fresh Base reconciliation found an existing visual transport/continuity workstream (`BCP-2026-032`) and a distinct OMENWARD-derived proposal already submitted as:

`BCP-2026-033-visual-canon-approval-and-handoff-integrity` · Base PR #693

Base PR #693 contains the proposal, OMENWARD problem/lesson evidence and Proposal Registry entry. The evidence captures the actual failures from this work: under-reading project/reference context before generation, missing established art lineage, old and new visual canon coexisting ambiguously, and conversation-only image authority. Its generic candidate is the approved-visual canon lifecycle: stable Decision/Asset identity, explicit supersession, current human-surface ordering, durable locator/readback and approved-reference refetch in future sessions.

OMENWARD-specific fronts, minimaps, commander, roulette, palette and art identity remain project-owned. PR #693 is **proposal-only** and is not active Base implementation authority. Because #693 is an independent existing Base workstream, this project closeout must not duplicate or mutate it.

## 15. Fresh-chat resumability questions

A future receiver must be able to answer without this conversation transcript:

1. What product is being made and what is the player's role?
2. What current battlefield presentation and art direction are approved?
3. Where is the exact approved image and what supersedes what?
4. What is approved versus runtime/human/rights `NOT_RUN`?
5. What project work is paused and what requires explicit reactivation?
6. Which PRs/issues are protected/read-only?
7. What Sheet data is stale versus still useful compatibility evidence?
8. What Base problem/lesson proposal already exists and why must it not be duplicated?
9. What external side effects already happened and must be verified before retry?
10. Can the receiver restate current state, next action and protected scope as `receiver_ack`?

If the answer to any of these requires old chat memory, treat the packet as `HANDOFF_NOT_READY`.

## 16. Transfer state and closeout rule

Sender-side terminal state:

```text
PACKET_READY
PENDING_RECEIVER_ACK
```

Only a future fresh chat/receiver that completes current authority readback may set:

```text
TRANSFER_ACCEPTED
```

After PR #210 is integrated and destination readback passes:
- stop OMENWARD work;
- do not resume Godot/runtime implementation automatically;
- do not generate another image automatically;
- resume only when the user explicitly reactivates OMENWARD or requests a specific visual/implementation task.