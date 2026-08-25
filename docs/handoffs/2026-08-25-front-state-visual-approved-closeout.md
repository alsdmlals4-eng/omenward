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

## 1. Why this handoff exists

This is the durable restart point for a new chat. The next session must not reconstruct the current visual direction from conversation history or from older North Star images. Read fresh GitHub + Notion and use the exact approved asset/Decision below.

## 2. Product identity that remains protected

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

The player is the **Omen Warden**, a commander who reads omens, prepares a Ward Citadel, obtains troops through the designed mobilization/roulette system, irreversibly commits them to fronts, and observes auto-battle results with limited tactical intervention.

The commander is not primarily a melee hero. The current visual role anchor is a **long command flag**.

## 3. Current approved battlefield presentation

```text
TOP FRONT    = current clash/front-state view + its own minimap
MIDDLE FRONT = current clash/front-state view + its own minimap
BOTTOM FRONT = current clash/front-state view + its own minimap
LOWER AREA   = current Focus-adaptive Control Deck
```

Required:
- all three current front situations are readable at the same time;
- each front has its own minimap;
- minimaps communicate front progress/position, strongholds/defense line, route/infiltration/air context, and relevant Boss/Siege position;
- minimaps do not reproduce every unit/VFX and are not a second battlefield;
- long roads from the citadel to the enemy base are **not** the default composition anymore.

## 4. Current approved visual style

```text
VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
MATERIAL_FINISH = HIGH_RES_PIXEL_TEXTURE_AND_RESTRAINED_LIGHTING
WORLD_TONE = FANTASY_WARD_CITADEL + MAGIC_WARFARE
NORMAL_COMBAT_UNIT_RULE = SILHOUETTE_FIRST
```

Allied language:
- navy, ivory, cool gray metal, restrained gold;
- arch, shield, banner, relic, vertical-line language;
- omen sigils, sanctified/arcane geometry, magic civilization.

Veil language:
- black-purple, dark red, carapace gray, limited rift glow;
- asymmetric rift, carapace, spike, void aperture.

SD does not mean generic cute mobile chibi. Weapon, shield, wing, staff, armor and mass must still define combat roles before faces/details.

## 5. Approved image — do not regenerate from memory

`OM-IMG-023` is the user-approved current visual reference.

Full-resolution source:
- Drive ID: `1-JRf4q95wZm51DsEYPH_-hnH_GLEIAQ5`
- https://drive.google.com/file/d/1-JRf4q95wZm51DsEYPH_-hnH_GLEIAQ5/view?usp=drivesdk
- `1536x1024 PNG`
- SHA-256: `0326b012d1fbefba85b545086b84992051591edff6f3b7e159cf3e083f204224`

Human-facing current surfaces:
- Home: https://app.notion.com/p/3c41b237eb1c816fbbc8e2dddc18b6eb
- Visual Bible: https://app.notion.com/p/3c01b237eb1c81c38be5e3ee9f64b59d
- Visual Components: https://app.notion.com/p/3c21b237eb1c81e29be2d6ce397c9c85

Home and Visual Bible place the current approved preview before the old North Star and link to the full-resolution Drive asset.

## 6. Superseded visual assumptions

Do not revert to these merely because older docs/images still contain them:

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
- allied vs Veil faction contrast;
- compact lower Control Deck direction;
- role-silhouette readability;
- 3x3 roulette/direct arrows and Run Command state flow.

## 7. Current implementation/evidence boundary

The visual closeout did **not** resume product implementation.

```text
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_UI_RUNTIME = NOT_RUN
CURRENT_MINIMAP_READABILITY = NOT_RUN
CURRENT_SD_UNIT_RUNTIME_READABILITY = NOT_RUN
CURRENT_HUMAN_USABILITY = NOT_RUN
CURRENT_PLAYER_EXPERIENCE = NOT_RUN
```

The previously approved orchestration-first Run Command vertical-slice packet remains retained, but a future session must fresh-read current authority before resuming it. This closeout does not silently expand its scope.

## 8. New-chat mandatory read order

1. Fresh Base `main`, `AGENTS.md`, relevant Skill, open PRs.
2. Fresh OMENWARD default branch, latest commit, open PRs/issues.
3. `AGENTS.md`.
4. `docs/CURRENT_CONFIRMED_DECISIONS.md`.
5. `docs/ACTIVE_CONTEXT.md`.
6. This handoff.
7. `docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md` for visual/battlefield work.
8. `docs/images/planning/canonical/OMENWARD_APPROVED_FRONT_STATE_VISUAL_2026-08-25.md`.
9. Notion Home + Visual Bible + Visual Components and their current image readback.
10. Google Sheet only as compatibility/history; report conflicts rather than treating it as current authority.
11. Only then inspect product code/runtime if the user reactivates implementation.

If a new image is requested, first fetch the approved visual from Drive/Notion and preserve its composition/style unless the user explicitly changes them. Do not generate from a prose-only memory of this chat.

## 9. GitHub work boundaries at closeout

- PR #210 owns this current visual/handoff workstream until merged.
- PR #209 is a different front-door documentation workstream and remains read-only.
- PR #205 is an older orchestration planning workstream and remains read-only.
- Never absorb, close, rebase or rewrite those other PRs without explicit named authorization.

Fresh GitHub state always wins over the numbers above if they change after this handoff.

## 10. Sheet conflict warning

The Google Sheet `00_프로젝트_허브` is currently stale and still describes an older PR175/Issue176/runtime period. It is compatibility/history material only. The 2026-08-25 visual Decision and approved image rows are newer than that hub summary.

## 11. Base learning handoff

A project-derived Base proposal is being submitted separately as:

`BCP-2026-032-visual-canon-approval-override-and-handoff-integrity`

Its scope is the reusable workflow lesson only: after a human approves a visual direction/reference, persist the approved asset, explicit supersession boundaries, current human-facing override, high-authority router update, and new-session readback before further visual generation. OMENWARD-specific art, three fronts, Omen Warden, palette and product identity remain project-owned and must not be promoted to Base.

Base proposal submission is **not** active Base implementation authority.

## 12. Closeout rule

After this handoff is integrated:
- stop OMENWARD work;
- do not resume Godot/runtime implementation automatically;
- do not generate another image automatically;
- resume only when the user explicitly reactivates OMENWARD or requests a specific visual/implementation task.
