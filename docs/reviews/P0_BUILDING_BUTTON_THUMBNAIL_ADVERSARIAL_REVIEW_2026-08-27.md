# P0 Building Button Thumbnail Consumer · Adversarial Review

```yaml
review_id: OMW-REVIEW-20260827-P0-BUILDING-BUTTON-THUMBNAILS-01
scope: THREE_EXISTING_STAGE_HUD_BUILD_ACTIONS
status: PARTIAL_RUNTIME_EVIDENCE__NO_P0_OR_P1_FINDING
```

## Five review passes

1. **Provenance and mutation attack:** checked every output in the manifest/run record against its approved cleanup-master SHA-256. All three derivatives retain binary alpha and transparent corners; no master was overwritten.
2. **Missing/incorrect mapping attack:** created and ran the HUD contract before implementation (RED: every texture, binding, display mode, and compact width was absent). After the scene binding and Godot import, the same contract passed (GREEN).
3. **Regression and scope-creep attack:** ran all 18 headless tests. The implementation touches only three `Button.icon` properties plus deterministic export/test/evidence files; construction rules, prices, service logic, scene geometry, and the battlefield stay unchanged.
4. **Importer and live-interaction attack:** imported the three PNGs with Godot 4.7.1, captured the live Stage HUD, then clicked Barracks and Tower. Their existing gold deduction and occupied/disabled state still occurred; screenshot analysis found no clipping signal and Hera diagnostics were clean.
5. **Authority and drift attack:** grounded the slice in GitHub Issue #223, retained the four unconsumed approved masters as source-only, and will advance the Base protected baseline only after the protected asset/scene commit is recorded.

## Result

`P0 = none`, `P1 = none`, `P2 = compact-icon readability has no human-study evidence`, `P3 = none`.

The implementation deliberately does not imply that buildings belong in the compact three-front battlefield. Human player evidence remains `NOT_RUN`.
