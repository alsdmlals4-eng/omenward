# OMENWARD Storybook SD Shield Guard True-Alpha Pair V1

```yaml
asset_id: OMW-IMG-20260830-STORYBOOK-SD-SHIELD-GUARD-PAIR-V1
status: USER_APPROVED__CANON_REGISTERED__IMPLEMENTED__RUNTIME_NOT_RUN
approval_source: USER_CHAT__2026-08-30__"확정해 진행하자"
approved_at: 2026-08-30 KST
user_asset_lock: USER_APPROVED_EXACT_PAIR
creation_route: AI_GENERATED__TECHNICAL_RGBA_NORMALIZATION
generator: BUILT_IN_IMAGEGEN
source_type: ORIGINAL_GENERATION__STYLE_REFERENCE_ONLY
source_record: docs/images/planning/OMENWARD_STORYBOOK_SD_SHIELD_GUARD_TRUE_ALPHA_PAIR_CANDIDATE_2026-08-30.md
target_archetype: shield_guard
runtime_cell_px: 512x512
runtime_pivot_px: 256x448
implementation_issue: Issue #256
adversarial_review: docs/reviews/ADVERSARIAL_STORYBOOK_SHIELD_GUARD_PAIR_IMPLEMENTATION_REVIEW_2026-08-30.md
runtime: NOT_RUN
human_readability: NOT_RUN
release_rights: REVIEW_PENDING__NOT_RELEASE_PASS
```

## Canonical runtime derivatives

| Faction | External source master | Source SHA-256 | Runtime derivative | Runtime SHA-256 | Alpha / visual facing |
|---|---|---|---|---|---|
| Lumern | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-fa7d9874-ec24-40f3-a408-04f28bcf5e5b.png` | `39412EB350BB80E4A5CB49673CB776C394B90278B5C816857A99E589275482A8` | `assets/art/units/lumern_shield_guard_storybook_idle_v1.png` | `4426957729861232BFBD1BEC5A9D5F9A7E471EA1B74978DBCA4A5689C7A4F2E5` | RGBA, alpha extrema `0..255`, source-facing right |
| Veil | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-fac4123e-b93a-4b8d-ba34-d1d673fa41bb.png` | `1934D51AA023A180D08771B081EE94F0CFA3E8B57FAC29DDED9BDD554BD718C8` | `assets/art/units/veil_shield_guard_storybook_idle_v1.png` | `EEDD123679F29465A4188D54D11D755E3B4D75E6F1FD629A722BBB542935D3CE` | RGBA, alpha extrema `0..255`, source-facing left |

## Normalization and binding

The runtime derivatives were made only through a non-destructive technical
normalization: alpha-bounds crop, LANCZOS fit inside a maximum `460×416` art
area, then horizontal centering on a transparent `512×512` canvas with the art
grounded to y=`448`. No inpainting, redrawing, background, cast shadow, or
legacy texture overwrite occurred.

- `data/bootstrap_catalog.tres::VisualShieldLumern` binds the Lumern derivative
  with `idle_pivot = Vector2(256, 448)`.
- `data/bootstrap_catalog.tres::VisualShieldVeil` binds the Veil derivative
  with the same pivot and `idle_mirror_for_veil = false`. The approved Veil
  source already faces left, so this contained per-profile exception prevents
  the shared renderer from double-flipping it. All other Veil profiles retain
  the default mirror behavior.
- `scenes/units/unit.tscn::IdleSprite` receives both textures through
  `scripts/units/unit_view.gd`.
- `scripts/ui/run_command_screen.gd::UNIT_TOKEN_TEXTURE` uses the Lumern
  derivative for the existing command token.

## Evidence ceiling and rollback

The focused headless Shield Guard asset contract verifies the paths, 512×512
geometry, pivot, profile binding, and Veil direction exception. That does not
prove a live Godot render, player readability, platform compatibility,
commercial release rights, or release readiness; those remain `NOT_RUN` or
`REVIEW_PENDING`.

Rollback is non-destructive: rebind `VisualShieldLumern`, `VisualShieldVeil`,
and the Run Command token to their prior paths and remove the two sibling
derivatives. The pre-existing textures and external source-master records are
retained.
