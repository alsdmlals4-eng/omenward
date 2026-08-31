# OMENWARD Title Entry · Candidate Decision Archive

```yaml
record_id: OMW-TITLE-CANDIDATES-20260831-01
decision_id: OMW-PLAN-20260831-OMEN-WARDEN-TITLE-ENTRY-01
created_at: 2026-08-31 KST
archived_at: 2026-08-31 KST
generation_mode: BUILT_IN_IMAGE_MODEL
asset_status: ARCHIVED__TITLE_BG_06_AND_WORDMARK_01_PROMOTED__OTHER_CANDIDATES_DELETED
promotion_authority: USER_CHAT__2026-08-31__"2번째(워드 로고), 마지막 이미지 승인"__"메인화면 이거야"
physical_candidate_images: DELETED_AFTER_CANONICAL_COPY_AND_REFERENCE_READBACK
current_canonical_record: docs/images/approved/OMENWARD_TITLE_ENTRY_ASSETS_V1.md
runtime_consumer: scenes/ui/title_screen.tscn
runtime_binding: TITLE_BG_06_AND_TITLE_WORDMARK_01_ONLY
rights_state: RELEASE_RIGHTS_NOT_REVIEWED
human_visual_review: USER_APPROVED_EXACT_SELECTION
technical_preview: SUPERSEDED_BY_RUNTIME_VALIDATION
```

## Archive purpose

The candidate PNGs were transient review material, not independent runtime
assets. The user selected only the `TITLE-WORDMARK-01` wordmark and the last
attached `TITLE-BG-06` battle-surge background. Those two bytes were copied
unchanged to `assets/art/ui/title/` and are now owned by the approved record.
Every other candidate image and the candidate-only composition capture were
deleted from the workspace at the user's request. This archive retains enough
identity, prompt, hash, and decision information to explain the promotion
without keeping redundant image files.

## Disposition inventory

| Candidate ID | Former repository path | SHA-256 | Final disposition |
| --- | --- | --- | --- |
| `TITLE-BG-01` | `docs/images/candidates/title/omenward_title_citadel_dawn_candidate_v1.png` | `17f83680ae4a0760f41e8d562a94fb4ff6d5d6ce4e0ec1ed9c5a1960f317b0c8` | `DELETED_AFTER_REVIEW` |
| `TITLE-SEAL-01` | `docs/images/candidates/title/omenward_title_ward_seal_candidate_v1.png` | `e86c7a8b6ccbd330662a2fb830bebbef370acbf7d17f8467a1baec573c000864` | `DELETED_AFTER_REVIEW` |
| `TITLE-BG-02` | `docs/images/candidates/title/omenward_title_wall_command_candidate_v2.png` | `19f2fc217bc03840cf08f0205aee2ca5b1a99731cd0cbc5046e3bedd8e405ef1` | `DELETED_AFTER_REVIEW` |
| `TITLE-BG-03` | `docs/images/candidates/title/omenward_title_wall_command_clash_candidate_v3.png` | `9198b129060da299f7ef33a491b563f4d9f3d746fabaf5e959a868207ddefb7b` | `DELETED_AFTER_REVIEW` |
| `TITLE-BG-04` | `docs/images/candidates/title/omenward_title_wall_command_veil_approach_candidate_v4.png` | `b3535598b2d141662c90e318f7c36bd1fb26ab3b2f18f1dc5ee9977a23939c89` | `DELETED_AFTER_REVIEW` |
| `TITLE-BG-05` | `docs/images/candidates/title/omenward_title_wall_command_veil_approach_roster_candidate_v5.png` | `575a0d694bb7c6617c993b2dc28582e3ece9338a98c0716dd8d9419d979c149a` | `DELETED_AFTER_REVIEW` |
| `TITLE-BG-06` | `docs/images/candidates/title/omenward_title_wall_command_battle_surge_candidate_v6.png` | `c787550308172c54e68a38c9914cac8e3e9b7f8b6b106217154a90e68ba7a128` | `PROMOTED_BYTE_EXACT_TO_assets/art/ui/title/omenward_title_wall_battle_surge_v1.png` |
| `TITLE-WORDMARK-01` | `docs/images/candidates/title/omenward_title_omenward_wordmark_candidate_v1.png` | `1bc36a8c86114ba90b9617b6354dce068011795ed3b51442b80d6fc12887a7aa` | `PROMOTED_BYTE_EXACT_TO_assets/art/ui/title/omenward_title_omenward_wordmark_v1.png` |

## Approved-source prompt provenance

### `TITLE-BG-06`

```text
Use case: precise composition edit of the previous title-background candidate.
Reference handling: the user-supplied combat image conveyed momentum only; no layout,
characters, symbols, names, or visual assets were copied.
Primary request: a storybook watercolor fantasy war seen from behind the Ward defenders.
At left, one rear-view Omen Warden with exactly two arms/hands, one separate standard-bearer
with one long blue-and-ivory flag, and one small fixed stone defensive tower. All Ward units
are rear-facing: a braced shield guard, thrusting spear soldier, archer releasing arrows,
staff mage preparing pale-blue magic, winged angel preparing white-gold magic, and hooded
priest preparing warm-gold magic. From the right, a black-purple mixed Veil host surges in
an irregular charge with sword-and-shield, halberd, caster, brute, and airborne silhouettes.
Constraints: no baked title text, logo, UI, watermark, construction node, or copied imagery;
leave the upper center calm enough for a separate title overlay.
```

### `TITLE-WORDMARK-01`

```text
Use case: transparent title-wordmark candidate for preview only.
Primary request: the exact original word OMENWARD in ornate dark-navy, ivory, and restrained
gold fantasy calligraphy with small omen-star and celestial-line ornaments; transparent alpha;
no background, character, seal, UI, watermark, or imitation of an existing title treatment.
```

## Retained evidence boundary

The last candidate-only technical preview and its 960×540 screenshot were deleted because
the preview was no longer the consumer after promotion. They do not prove the final runtime
layout. Runtime rendering, machine validation, visual user approval, rights review, and
release approval remain distinct states in the approved record and QA evidence.

Rollback means reverting the canonical TitleScreen binding and the two approved runtime files;
the deleted alternate candidates are intentionally not restored.
