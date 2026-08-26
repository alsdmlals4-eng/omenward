# OMENWARD · Autonomous Required-Image Production Policy

```yaml
policy_id: OMW-VIS-POLICY-20260826-AUTONOMOUS-REQUIRED-IMAGES-V1
status: USER_AUTHORIZED_CURRENT
authorized_at: 2026-08-26
authority_input: "필요하다고 판단한 이미지면 승인 받지말고 자동으로 만들어서 노션,로컬에 저장까지해"
scope: PROJECT_REQUIRED_RASTER_IMAGES_AND_THEIR_LOCAL_NOTION_DUAL_STORAGE
visual_generation: AUTONOMOUS_WITHIN_PROJECT_REQUIRED_SCOPE
source_storage: PROJECT_LOCAL_LIBRARY_REQUIRED
notion_record: REQUIRED_PER_APPROVED_SOURCE_IMAGE
style_guard: EXISTING_OMENWARD_CONCEPT_LANGUAGE_REQUIRED
godot_codex_implementation: SEPARATE_SCOPE
runtime_claims: SEPARATE_EVIDENCE_REQUIRED
```

## Operating rule

The agent may identify and generate an image only when it has a confirmed project consumer or is a required derivative of an approved project image. It automatically saves each approved source in the project-local vault and creates a corresponding Notion record with the local path and SHA-256. Candidate-only artifacts may remain local without a Notion approval record until the agent promotes them under this policy.

## Style guard · non-negotiable

Every autonomous image must remain inside the established OMENWARD visual language:

- `FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION`.
- Crisp hard pixel edges and 2–4 tone shading; no blur, painterly texture, text/UI screenshot, or watermark.
- Lumern: navy, ivory, cool-gray metal, restrained gold.
- Veil: black-purple, dark red, carapace gray, limited rift glow; never a simple purple human-knight recolor.
- Preserve role-first silhouettes, tactical readability, and the visual relationship established by the approved unit and building sources.

## Boundaries retained

- Automatic image approval does not authorize unrelated story/UI/product changes, Godot code, Scene/Resource edits, external publication, or runtime PASS claims.
- Generated source images may receive deterministic cleanup masters without overwriting originals.
- New atlas dimensions, crop envelopes, pivots, animation timing, and `IMPLEMENTATION_READY` still require an evidence-backed production contract; do not invent them merely because an image exists.
- The user remains the direction owner and may override or stop this policy at any time.
