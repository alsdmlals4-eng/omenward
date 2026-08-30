# [Candidate] OMENWARD Storybook SD Runtime Unit Source Sheets

```yaml
record_id: OMW-IMG-20260830-STORYBOOK-SD-UNIT-RUNTIME-SHEETS-V1
created_at: 2026-08-30 KST
status: GENERATED_CANDIDATE__TECHNICAL_CELL_NORMALIZATION_PENDING_REVIEW
implementation_issue: Issue #256
approval_direction_source: USER_CHAT__"승인, 진행해줘"
generator: BUILT_IN_IMAGEGEN
source_sheet_dimensions_px: 1254x1254
source_sheet_grid: 3x3
source_sheet_cell_px: 418x418
target_runtime_cell_px: 512x512
target_runtime_pivot_px: 256x448
source_facing: RIGHT
runtime_assets: NOT_CREATED
runtime: NOT_RUN
human_readability: NOT_RUN
rights_status: GENERATION_PROVENANCE_RECORDED__RELEASE_RIGHTS_REVIEW_PENDING
```

## Source sheets

| Faction | Source path | SHA-256 | Cell order |
|---|---|---|---|
| Lumern | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-a31ccff9-e9ce-4093-a4da-020df071c9b2.png` | `616C7E1F754B57653760542EBDD612F9163EFCF5149A1E14AF03A6CCE1591C0F` | shield_guard, greatsword_warrior, assassin, spear_guard, archer, cavalry, priest, mage, flier |
| Veil | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-2b7bd80d-53cb-4860-b297-bd8ea8aee5f4.png` | `82A3DA09D5101F0EC19D6C956A117F4F13C1F696A1EF04264FD15040627138CF` | shield_guard, greatsword_warrior, assassin, spear_guard, archer, cavalry, priest, mage, flier |

## Candidate purpose

The sheets adopt the user-approved storybook watercolor SD tactical direction:
Lumern uses ivory, navy, and restrained gold; Veil uses charcoal, muted violet,
and limited rift glow. Each cell maps to an existing runtime archetype and
must preserve the current `UnitView` source-facing and 512×512/pivot contract.

```text
READ_ORDER = ROLE -> WEAPON -> SCALE -> FACTION_COLOR -> TIER -> DECORATION
LUMERN_VEIL_COMBAT_TIMING_DIFFERENCE = FORBIDDEN
RUNTIME_CELL = 512x512
RUNTIME_PIVOT = 256x448
```

## Promotion boundary

The generated files currently contain a visible checkerboard rather than true
alpha data. They are source candidates only and must **not** be cropped or
bound into `assets/art/units/` until a non-destructive, true-alpha cell export
is checked against the 512×512 runtime geometry and its visual result is
reviewed. No existing approved/legacy unit texture is overwritten.

```text
GENERATED_SOURCE_SHEETS
-> TRUE_ALPHA_CELL_DERIVATIVES
-> USER_APPROVED_EXACT_RUNTIME_CELLS
-> CANON_REGISTERED_WITH_PER_CELL_SHA256
-> BOUND_TO_EXISTING_FACTION_VISUAL_PROFILES
-> RUNTIME_RENDERED_AND_HUMAN_READABILITY_REVIEWED
```
