# Adversarial Review — Storybook Role Profile Implementation

```yaml
review_id: OMW-REVIEW-20260902-STORYBOOK-ROLE-PROFILE
scope: ROLE_ASSET_PROVENANCE__CATALOG_BINDING__BATTLEFOCUS_RENDER__RUNTIME_FIXTURE
result: MACHINE_AND_RUNTIME_SCOPE_PASS_5_OF_5__HUMAN_NOT_RUN
reviewed_issue: 256
```

| Loop | Adversarial question | Finding | Resolution / evidence |
| --- | --- | --- | --- |
| 1 | Did standing image authority accidentally turn the four unapproved bytes into explicit user selections? | Risk identified. | Separate canonical records preserve `exact_user_asset_approval: FALSE` for Spear/Cavalry while Archer/Mage remain four exact user-locked derivatives. |
| 2 | Could the renderer still show every role as a Shield Guard or face Veil the wrong way? | Prior hard-coded Shield Guard path was a real defect. | Role/faction map covers Shield, Spear, Archer, Cavalry, and Mage; the contract test rejects an unsupported-role impostor and asserts Veil flip rules. |
| 3 | Did new images leave obsolete catalog references that make asset coverage lie? | Yes: eight legacy ext-resource entries were unreferenced, producing `28` rather than `20` live catalog textures. | Removed only those unused catalog references; legacy files remain preserved. `audit_runtime_image_coverage.py` and its two tests now pass. |
| 4 | Do the denser watercolor sprites obscure each other, the route strip, tower, or terrain corridor? | Former 74px display cell under-read role equipment. | Increased BattleFocus draw cell to `88×88`; fixture capture contains 3×3 faction count, fixed tower, single-row minimap, and six intact silhouettes without terrain-corridor overlap. |
| 5 | Is the result being overstated as player or release acceptance? | Evidence is machine/runtime only. | QA owner explicitly retains `HUMAN_NOT_RUN`, rights pending, no balance claim, and a capture-analyzer caveat. |

No unresolved P0/P1 machine-scope defect remains in this packet. The remaining
decision is user/player readability of a combat-produced mixed roster; it is not
silently promoted by the fixture capture.
