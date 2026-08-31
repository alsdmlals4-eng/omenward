# [Approved] OMENWARD Title Entry Assets V1

```yaml
asset_bundle_id: OMW-IMG-20260831-TITLE-ENTRY-ASSETS-V1
decision_id: OMW-PLAN-20260831-OMEN-WARDEN-TITLE-ENTRY-01
approved_at: 2026-08-31 KST
status: USER_APPROVED__CANON_REGISTERED__IMPLEMENTED__MACHINE_VERIFIED__RUNTIME_TECHNICAL_SMOKE_PASS__HUMAN_NOT_RUN
user_asset_lock: USER_APPROVED_EXACT_WORDMARK_AND_LAST_ATTACHED_BATTLE_SURGE_BACKGROUND
approval_source: USER_CHAT__2026-08-31__"2번째(워드 로고), 마지막 이미지 승인"__"메인화면 이거야"
creation_route: AI_GENERATED__BUILT_IN_IMAGE_MODEL
source_archive: docs/images/candidates/OMENWARD_TITLE_ENTRY_CANDIDATES_2026-08-31.md
runtime_consumer: scenes/ui/title_screen.tscn::TitleScreen/Backdrop + TitleScreen/TitleWordmark
human_visual_approval: USER_APPROVED_EXACT_ASSET_SELECTION
human_usability_evidence: NOT_RUN
release_rights_status: RELEASE_BLOCKED_UNVERIFIED
```

## Canonical runtime assets

| Asset ID | Repository path | Source master / archived candidate | SHA-256 | Runtime role |
| --- | --- | --- | --- | --- |
| `TITLE-BG-06` | `assets/art/ui/title/omenward_title_wall_battle_surge_v1.png` | `C:/Users/user/.codex/generated_images/01a04af4-0452-7a13-9b6e-1a6077568d72/exec-8db03157-b188-4778-8e59-207848f46d7a.png` / `docs/images/candidates/title/omenward_title_wall_command_battle_surge_candidate_v6.png` (removed after promotion) | `c787550308172c54e68a38c9914cac8e3e9b7f8b6b106217154a90e68ba7a128` | Full-screen `TitleScreen/Backdrop` background |
| `TITLE-WORDMARK-01` | `assets/art/ui/title/omenward_title_omenward_wordmark_v1.png` | `docs/images/candidates/title/omenward_title_omenward_wordmark_candidate_v1.png` (removed after promotion) | `1bc36a8c86114ba90b9617b6354dce068011795ed3b51442b80d6fc12887a7aa` | Transparent, separate `TitleScreen/TitleWordmark` layer |

The canonical copies are byte-for-byte copies of their approved source images:
no crop, redraw, compositing, text baking, or alpha modification was applied.
`TITLE-BG-06` is 1672×941 RGB. `TITLE-WORDMARK-01` retains its 1972×798 RGBA
alpha channel. The wordmark is deliberately not baked into the background, so
the game title remains an independent, replaceable UI layer.

## Runtime composition and retained boundaries

```text
TitleScreen
├── Backdrop       = approved battle-surge image, full rect / aspect covered
├── TitleWordmark  = approved transparent OMENWARD texture, upper center
├── RoleLine       = native localized Godot Label
└── Panel
    ├── route context / bootstrap status = native Godot Labels
    └── 원정 시작 = the one real executable action
```

The full battle illustration remains readable around the UI: the Wordmark uses
the calm upper-center space, while the small lower action panel avoids a second
opaque full-screen card. The background remains world presentation only; it
does not add a construction node, a second front, a tower mechanic, or a new
gameplay rule. The actual tutorial route and its `내정 → 룰렛 → 전선` flow are
unchanged.

## Provenance, reference boundary, and rights ceiling

The archived candidate record contains the full generator prompt and its source
hashes. The user-provided comparison images were visual momentum/style input
only; no external image file is included in the build, and no external title,
characters, symbols, or pixels were copied into the canonical files.

```yaml
commercial_use: UNKNOWN
distribution_in_game_build: UNKNOWN
raw_source_redistribution: UNKNOWN
modification: NOT_REQUIRED__BYTE_EXACT_PROMOTION
ai_model_service_version: BUILT_IN_IMAGE_MODEL__TERM_VERSION_NOT_RECORDED
ai_terms_checked_at: NOT_RUN
ai_input_rights: USER_PROVIDED_REFERENCE_IMAGES__LEGAL_REVIEW_NOT_PERFORMED
ai_output_terms: NOT_RUN
reference_brief: STORYBOOK_WATERCOLOR_SD_FANTASY_WARD_VS_VEIL_TITLE_COMPOSITION
forbidden_expression: EXTERNAL_PIXEL_OR_CHARACTER_OR_LOGO_COPY__FORBIDDEN
reference_similarity_status: BLOCKED_UNVERIFIED
shipping_and_marketing_usage: RELEASE_BLOCKED_UNVERIFIED
secure_original_location: USER_LOCAL_CODEX_GENERATED_IMAGE_AREA__NOT_A_RUNTIME_DEPENDENCY
```

User visual approval and successful technical rendering do not establish
commercial terms, distribution rights, legal similarity clearance, platform
submission, or release readiness. Those remain `RELEASE_BLOCKED_UNVERIFIED`
until the relevant rights review is completed.

## Rollback

Revert the two canonical runtime files and the two `TextureRect` bindings in
`scenes/ui/title_screen.tscn`. The native TitleScreen route remains independent
of these images, so no save migration or gameplay rollback is required. The
discarded candidate revisions are intentionally not restored; their IDs,
hashes, prompts, and decision history remain in the archived candidate record.
