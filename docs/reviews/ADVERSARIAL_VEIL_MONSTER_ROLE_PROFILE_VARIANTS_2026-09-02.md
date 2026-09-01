# Adversarial Review — Veil Monster Role Variants

```yaml
review_id: OMW-REVIEW-20260902-VEIL-MONSTER-ROLE-VARIANTS
scope: VEIL_ROLE_IDENTITY__ASSET_PROVENANCE__ROLE_BINDING__RUNTIME_CAPTURE
result: MACHINE_AND_RUNTIME_SCOPE_PASS_5_OF_5__HUMAN_NOT_RUN
```

| Loop | Adversarial question | Finding | Resolution / evidence |
| --- | --- | --- | --- |
| 1 | Does the request mean every dark faction asset must be replaced, including the already non-human shield guard? | No; the shield guard already has a faceless carapace silhouette, while four role sprites expose human face/skin/hair cues. | Scoped to Veil Spear Guard, Archer, Cavalry, and Mage only; Shield Guard stays untouched. |
| 2 | Could stronger monster treatment erase the role-first read at 88px? | A fully amorphous/limbless option would endanger spear, bow, mount, and staff recognition. | Kept the role weapon and full-body pose as the first silhouette cue, then added horns, void apertures, chitin, claws, and rift cracks. |
| 3 | Did new images overwrite approved bytes or falsely claim exact user asset selection? | Risk identified for the prior Veil Archer/Mage exact-selection record. | Generated versioned sibling paths; historical files remain unchanged. New record says `exact_user_asset_approval: FALSE` and cites standing authority plus the user direction. |
| 4 | Did opaque black/checkerboard generation output reach the product? | Two source images had opaque connected backgrounds. | Removed only connected outer background pixels, then normalized each intact subject to transparent `512×512` at `(256,448)`; all four output alpha channels range `0..255`. |
| 5 | Is the updated capture genuinely from new assets rather than the stale earlier fixture process? | A stale fixture initially produced the prior capture hash. | Stopped only the verified stale QA fixture PID, relaunched the fixture through the Omenward editor, and recorded a different capture SHA `AAD650…49BE6` with clean diagnostics. |

No P0/P1 machine or technical-runtime defect remains in this narrow packet.
Remaining evidence is intentionally limited: player readability under a
combat-produced mixed roster, physical-device behavior, rights review, and
release acceptance are all still `NOT_RUN`.
