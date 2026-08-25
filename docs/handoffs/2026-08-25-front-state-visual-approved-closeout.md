# OMENWARD · Front-State Visual Approved Closeout Handoff · 2026-08-25

```yaml
handoff_state: PAUSED_QUEUED_AFTER_VISUAL_CLOSEOUT
visual_decision: OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01
approved_visual: OM-IMG-023
approved_visual_record: docs/images/planning/canonical/OMENWARD_APPROVED_FRONT_STATE_VISUAL_2026-08-25.md
visual_spec: docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md
product_runtime_resumed: false
runtime_readability: NOT_RUN
human_usability: NOT_RUN
player_experience: NOT_RUN
image_generation_after_closeout: STOPPED
```

## 1. Restart purpose

This is the durable restart point for a new chat. Do not reconstruct the current visual direction from old conversation history or older North Star images. Fresh-read GitHub + Notion, then use the exact approved Decision/asset below.

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

Home and Visual Bible place a Notion-native inline preview of the approved image before the old North Star and link to the full-resolution Drive asset. Server readback returned a Notion-hosted image URL. This is attachment/readback evidence, not human-device visual PASS.

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
```

The previously approved orchestration-first Run Command vertical-slice packet remains retained. A future session must fresh-read current authority before resuming it.

## 8. New-chat mandatory read order

1. Fresh Base main, `AGENTS.md`, relevant Skill, open PRs.
2. Fresh OMENWARD default branch, latest commit, open PRs/issues.
3. OMENWARD `AGENTS.md`.
4. `docs/CURRENT_CONFIRMED_DECISIONS.md`.
5. `docs/ACTIVE_CONTEXT.md`.
6. `docs/HANDOFF_CONTEXT.md` and this handoff.
7. Current visual spec and approved visual asset record.
8. Notion Home + Visual Bible + Visual Components and the full-resolution Drive image.
9. Current GDD/Project Core + relevant detailed owner; when older visual wording conflicts, the 2026-08-25 Decision wins.
10. Google Sheet only as compatibility/history and report conflicts.
11. Inspect code/runtime only after explicit user reactivation.

If a new image is requested, **refetch OM-IMG-023 first** and preserve approved composition/style unless the user explicitly changes it.

## 9. GitHub boundaries at closeout

- PR #210 owns this visual/handoff workstream until integrated.
- PR #209 is a different front-door documentation workstream and remains read-only.
- PR #205 is an older orchestration planning workstream and remains read-only.
- Never absorb/close/rebase/rewrite those other PRs without explicit named authorization.
- Fresh GitHub state always wins if these numbers later change.

## 10. Sheet conflict warning

Google Sheet `00_프로젝트_허브` is stale and still describes an older PR175/Issue176/runtime period. It is compatibility/history only. The 2026-08-25 visual Decision, `OM-IMG-023` rows and GitHub/Notion current state are newer.

## 11. Base learning handoff

Fresh Base reconciliation found an existing `BCP-2026-032-ai-visual-continuity-and-notion-preview-fallback`, already `APPROVED_FOR_IMPLEMENTATION`. Its scope is persistent-character visual continuity and Notion preview transport fallback.

The distinct OMENWARD-derived closeout lesson is submitted separately as:

`BCP-2026-033-visual-canon-approval-and-handoff-integrity` · Base PR #693

BCP-033 only proposes the reusable canon lifecycle: stable approved Asset/Decision, explicit supersession, current human-surface ordering, destination readback, and approved-reference refetch before future generation. OMENWARD-specific art, fronts, minimaps, commander, palette and product identity remain project-owned. Proposal submission is **not** active Base implementation authority.

The first collided Base branch/PR #691 was closed unmerged after the BCP-032 collision was discovered.

## 12. Closeout rule

After this handoff is integrated:
- stop OMENWARD work;
- do not resume Godot/runtime implementation automatically;
- do not generate another image automatically;
- resume only when the user explicitly reactivates OMENWARD or requests a specific visual/implementation task.
