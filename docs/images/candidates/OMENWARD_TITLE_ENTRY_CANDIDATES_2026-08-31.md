# OMENWARD Title Entry · Candidate Image Set

```yaml
record_id: OMW-TITLE-CANDIDATES-20260831-01
decision_id: OMW-PLAN-20260831-OMEN-WARDEN-TITLE-ENTRY-01
created_at: 2026-08-31 KST
generation_mode: BUILT_IN_IMAGE_MODEL
asset_status: GENERATED_CANDIDATE
runtime_consumer: NONE
runtime_binding: FORBIDDEN_UNTIL_USER_VISUAL_LOCK
review_gate: LOCK / REVISE / REJECT
rights_state: RELEASE_RIGHTS_NOT_REVIEWED
human_visual_review: USER_REVIEW_PENDING
```

## Purpose and boundary

이 세트는 새 TitleScreen의 수호 성채·베일 대비와 작은 수호 문장을 검토하기 위한 **후보**다.
두 PNG는 `docs/images/candidates/title/`에만 존재하며 `assets/art/` 또는 `TitleScreen` runtime
scene에서 소비되지 않는다. 배경·문장·전선 규칙·게임 로고 텍스트는 서로 다른 책임이다. 제목과
한국어 문구는 생성 이미지 안에 넣지 않고 Godot Label이 계속 소유한다.

## Candidate inventory

| Candidate ID | File | Dimensions / alpha | SHA-256 | Intended future consumer | Current state |
|---|---|---|---|---|---|
| `TITLE-BG-01` | `docs/images/candidates/title/omenward_title_citadel_dawn_candidate_v1.png` | 1672×941 RGB | `17f83680ae4a0760f41e8d562a94fb4ff6d5d6ce4e0ec1ed9c5a1960f317b0c8` | `TitleScreen/Backdrop` | `GENERATED_CANDIDATE` |
| `TITLE-SEAL-01` | `docs/images/candidates/title/omenward_title_ward_seal_candidate_v1.png` | 1254×1254 RGBA; alpha retained | `e86c7a8b6ccbd330662a2fb830bebbef370acbf7d17f8467a1baec573c000864` | `TitleScreen/Panel/Seal` | `GENERATED_CANDIDATE` |

Both files were copied without transformation from the built-in generator output. Readback hashes match
their source outputs exactly. The original generated copies remain outside the repository under the Codex
generated-image area; they are not runtime dependencies.

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

## Inspection result

- `TITLE-BG-01`: source and copied candidate were visually inspected. It maintains a connected route and a clean central title-safe region; the Ward Citadel is world-setting context rather than an in-battle building model.
- `TITLE-SEAL-01`: source and copied candidate were visually inspected. It has no generated text and retains an RGBA alpha channel; it reads as a title ornament rather than a game economy or combat object.
- `scenes/preview/omenward_title_entry_candidate_preview.tscn` rendered both candidates with the exact native title, Korean role line, and primary button at 960×540. Its captured preview is `docs/images/candidates/title/omenward_title_entry_candidate_preview_runtime.png` with SHA-256 `edbd6ca90f55b02316aeff008be1d18387daaa3bdb0711437b3b26f9fa38fcc9`. The runtime inspector reported all nine expected Controls visible and no clipping signal; this is composition evidence only, not an approved runtime consumer.
- Neither inspection is a runtime proof, human usability approval, release-rights review, or visual lock.

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
