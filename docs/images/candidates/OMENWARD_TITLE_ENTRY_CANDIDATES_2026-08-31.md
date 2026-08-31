# OMENWARD Title Entry · Candidate Image Set

```yaml
record_id: OMW-TITLE-CANDIDATES-20260831-01
decision_id: OMW-PLAN-20260831-OMEN-WARDEN-TITLE-ENTRY-01
created_at: 2026-08-31 KST
updated_at: 2026-08-31 KST
generation_mode: BUILT_IN_IMAGE_MODEL
asset_status: GENERATED_CANDIDATE__TITLE_BG_06_AND_WORDMARK_01_CURRENT_REVIEW_TARGET
runtime_consumer: NONE
runtime_binding: FORBIDDEN_UNTIL_USER_VISUAL_LOCK
review_gate: LOCK / REVISE / REJECT
rights_state: RELEASE_RIGHTS_NOT_REVIEWED
human_visual_review: USER_REVIEW_PENDING
technical_preview: FOCUSED_CONTRACTS_AND_HERA_CAPTURE_PASS
```

## Purpose and boundary

이 세트는 새 TitleScreen의 **성벽 위 수호군과 돌격하는 베일 군단**, 그리고 별도 게임 제목
워드마크를 검토하기 위한 **후보**다. 모든 PNG는 `docs/images/candidates/title/`에만 존재하며
`assets/art/` 또는 실제 `TitleScreen` runtime scene에서 소비되지 않는다. 배경·워드마크·전선
규칙·게임 로고 텍스트는 서로 다른 책임이다. 배경 안에는 생성 텍스트를 넣지 않았고, 한국어 역할
문구와 버튼은 Godot Control이 계속 소유한다. 워드마크도 현재는 candidate-preview에서만 렌더한다.

## Candidate inventory

| Candidate ID | File | Dimensions / alpha | SHA-256 | Intended future consumer | Current state |
|---|---|---|---|---|---|
| `TITLE-BG-01` | `docs/images/candidates/title/omenward_title_citadel_dawn_candidate_v1.png` | 1672×941 RGB | `17f83680ae4a0760f41e8d562a94fb4ff6d5d6ce4e0ec1ed9c5a1960f317b0c8` | `TitleScreen/Backdrop` | `REVISED_HISTORICAL` |
| `TITLE-SEAL-01` | `docs/images/candidates/title/omenward_title_ward_seal_candidate_v1.png` | 1254×1254 RGBA; alpha retained | `e86c7a8b6ccbd330662a2fb830bebbef370acbf7d17f8467a1baec573c000864` | `TitleScreen/Panel/Seal` | `RETAINED_NOT_CURRENT` |
| `TITLE-BG-02` | `docs/images/candidates/title/omenward_title_wall_command_candidate_v2.png` | 1672×941 RGB | `19f2fc217bc03840cf08f0205aee2ca5b1a99731cd0cbc5046e3bedd8e405ef1` | `TitleScreen/Backdrop` | `REVISED_NO_VISIBLE_CLASH` |
| `TITLE-BG-03` | `docs/images/candidates/title/omenward_title_wall_command_clash_candidate_v3.png` | 1672×941 RGB | `9198b129060da299f7ef33a491b563f4d9f3d746fabaf5e959a868207ddefb7b` | `TitleScreen/Backdrop` | `REVISED_COMMANDER_ANATOMY_AND_PRESSURE` |
| `TITLE-BG-04` | `docs/images/candidates/title/omenward_title_wall_command_veil_approach_candidate_v4.png` | 1672×941 RGB | `b3535598b2d141662c90e318f7c36bd1fb26ab3b2f18f1dc5ee9977a23939c89` | `TitleScreen/Backdrop` | `REVISED_TO_REAR_APPROACH` |
| `TITLE-BG-05` | `docs/images/candidates/title/omenward_title_wall_command_veil_approach_roster_candidate_v5.png` | 1672×941 RGB | `575a0d694bb7c6617c993b2dc28582e3ece9338a98c0716dd8d9419d979c149a` | `TitleScreen/Backdrop` | `REVISED_STATIC_FORMATION` |
| `TITLE-BG-06` | `docs/images/candidates/title/omenward_title_wall_command_battle_surge_candidate_v6.png` | 1672×941 RGB | `c787550308172c54e68a38c9914cac8e3e9b7f8b6b106217154a90e68ba7a128` | `TitleScreen/Backdrop` | `GENERATED_CANDIDATE__CURRENT_REVIEW_TARGET` |
| `TITLE-WORDMARK-01` | `docs/images/candidates/title/omenward_title_omenward_wordmark_candidate_v1.png` | 1972×798 RGBA; alpha retained | `1bc36a8c86114ba90b9617b6354dce068011795ed3b51442b80d6fc12887a7aa` | `TitleScreen/Wordmark` | `GENERATED_CANDIDATE__CURRENT_REVIEW_TARGET` |

Each repository candidate was copied without transformation from the built-in generator output. Readback
hashes match their corresponding source output exactly. The original generated copies remain outside the
repository under the Codex generated-image area; they are not runtime dependencies.

## Prompt provenance

### `TITLE-BG-01`

```text
Use case: illustration-story
Asset type: candidate 16:9 Godot game title-screen background, preview only; not a final runtime asset yet.
Primary request: original storybook watercolor fantasy landscape for OMENWARD: Ward Citadel and one navy-and-ivory standard at left; distant black-purple Veil rift and dark spires at right; broad quiet center for native UI.
Scene: one connected open meadow and stone path suggesting a single eastward march; no river, lanes, map UI, tower, combat, soldiers, construction nodes, text, logo, watermark, or characters.
Style: delicate ink, ivory paper texture, soft watercolor, first-light dawn, navy/ivory/cool-gray/gold at Ward side and restrained black-purple/dark-red/carapace-gray at Veil side.
```

### `TITLE-SEAL-01`

```text
Use case: logo-brand
Asset type: candidate UI seal for a Godot fantasy strategy title screen, preview only; not a final runtime asset yet.
Primary request: original square heraldic Ward seal with blue enamel shield, simple gold four-point omen star, ivory rim, silver-gray details, and narrow navy ribbon on genuine transparent alpha.
Constraints: no letters, words, logo type, watermark, characters, weapons, currency, building, tower, roulette device, combat, or imitation of existing game artwork.
```

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

## Inspection result

- `TITLE-BG-01` through `TITLE-BG-05` are retained revision history. They are not current art
  selections and have no runtime consumer.
- `TITLE-BG-06` was source/copy-hash verified and visually inspected. It reads as active warfare:
  the right-side Veil mass charges irregularly while the rear-facing Ward roles visibly brace,
  fire arrows, and prepare distinct magic. The single tower and flag remain environmental world
  context, never a construction node or a second gameplay front.
- `TITLE-WORDMARK-01` was source/copy-hash verified and has a genuine RGBA alpha channel. It is
  layered only in the candidate preview, not baked into `TITLE-BG-06` and not bound to runtime.
- `scenes/preview/omenward_title_entry_candidate_preview.tscn` renders `TITLE-BG-06` and
  `TITLE-WORDMARK-01` with the native Korean role line and primary button at 960×540. Its latest
  technical capture is
  `docs/images/candidates/title/omenward_title_wall_command_battle_surge_candidate_preview_runtime.png`
  (960×540; SHA-256 `e8748eccddd95e52eba717b508b370a902a53826661aa0ffd9f32d8317f84734`).
  The runtime UI inspector reported all six expected Controls visible; screenshot analysis reported
  `possible_clipping: false`; diagnostics reported zero errors and zero warnings. This is technical
  composition evidence only, not an approved runtime consumer.
- Neither inspection is a human usability approval, release-rights review, visual lock, or release PASS.

## Promotion gate

```text
USER_RESPONSE = LOCK / REVISE / REJECT

LOCK
→ copy only locked candidate into assets/art/ui/title/
→ add SHA-256, source candidate, prompt, approval, and exact consumer to an approved asset record
→ bind only the locked asset to TitleScreen
→ add a failing asset-consumer test, then run full machine verification and a technical runtime capture

REVISE
→ keep this candidate record, generate a bounded new version, and never overwrite these bytes

REJECT
→ remove only the rejected candidate after readback; preserve established runtime assets and the decision/spec history
```
