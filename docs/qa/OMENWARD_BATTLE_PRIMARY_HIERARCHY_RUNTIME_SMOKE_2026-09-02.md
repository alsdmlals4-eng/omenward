# OMENWARD BATTLE-Primary Hierarchy Runtime Technical Smoke — 2026-09-02

```yaml
qa_id: OMW-QA-20260902-BATTLE-PRIMARY-HIERARCHY-RUNTIME-SMOKE
status: RUNTIME_TECHNICAL_SMOKE_PASS__HUMAN_NOT_RUN
runtime_code_head: 350100620f66617e42450f3f9fef66f392d159c0
runtime_scene: res://scenes/main/main.tscn
viewport: 960x540
capture: docs/qa/captures/battle_hierarchy/omenward_battle_primary_hierarchy_35010062_2026-09-02.png
runtime_path: TITLE_START -> PREPARE_SPIN -> ROULETTE_ROW_RIGHT_1 -> LOCK_RESULT -> CONFIRM_RESULT -> BEGIN_BATTLE
diagnostics: CLEAN__ERRORS_0__WARNINGS_0
human_player_evidence: NOT_RUN
multi_unit_readability: NOT_RUN
rights_release_device_accessibility: NOT_RUN
```

## Observed runtime facts

- The real title button opened the retained Run Command flow; no test-only state mutation was used.
- The actual `BATTLE` phase exposed `BattleFocusViewport` at `x=16, y=110,
  w=926, h=304`, `MarchMinimap` at `x=16, y=62, w=926, h=40`, and `LowerDeck`
  at `x=16, y=422, w=928, h=106`.
- The minimap rendered one connected, read-only five-sector ribbon. The battle
  surface remained the only close combat view and showed the one fixed tower;
  no map building, construction node, fence, barricade, unit marker, or second
  tower was introduced.
- Hera diagnostics reported `error_count: 0` and `warning_count: 0` after the
  capture. The image analyzer reported a nonblank 960×540 capture and a
  conservative `possible_clipping: true`; visual inspection found no clipped
  active control, but that analyzer flag is retained rather than suppressed.

## Evidence ceiling

This ordinary player-flow seed reached BATTLE without a confirmed earned unit,
so the captured battle frame is intentionally sparse. It proves the actual
phase transition, one-front hierarchy, rectangles, single-row context ribbon,
and clean technical diagnostics. It does **not** prove human readability of a
mixed multi-unit formation, accessibility, device behavior, asset rights, or
release readiness. Those remain `NOT_RUN`.
