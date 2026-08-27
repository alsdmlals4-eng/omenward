# Run Command Vertical Slice · Adversarial Review

```yaml
review_id: OMW-REV-20260827-RUN-COMMAND-VERTICAL-SLICE-01
reviewed_at: 2026-08-27
scope: RUN_COMMAND_ORCHESTRATION_FIRST_VERTICAL_SLICE
implementation_packet: docs/implementation/OMENWARD_RUN_COMMAND_VERTICAL_SLICE_WORK_PRODUCTION_INPUT_PACKET_2026-08-27.md
result: PASS_5_OF_5_MACHINE_SCOPE
human_play_evidence: NOT_RUN
```

This review is limited to the implemented Run Command vertical slice. It does not promote broad gameplay readability, balance, controller support, Windows runtime, or human/player evidence.

| Loop | Attack | Evidence | Result |
|---|---|---|---|
| 1 | Advance wave/economy before the player enters battle. | `run_command_phase_contract_test.gd` verifies `PREPARE` does not advance and `BATTLE` does. | PASS |
| 2 | Charge twice or alter legacy roulette command history while splitting stop and resolve. | `economy_roulette_test.gd` confirms legacy `spin()` remains one recorded roulette action; phase contract confirms stopped-board payment occurs exactly once and preview is free. | PASS |
| 3 | Partially reserve capacity, log, or spawn only part of a multi-unit commit. | Batch deployment preflights every card and total food before mutation; the over-capacity batch regression test leaves food, deployment list, and input log unchanged, and the phase test forces a Shield Guard reward through an explicit middle-front COMMIT. | PASS |
| 4 | Let technical HUD/Stage selector compete with the new player surface, or omit simultaneous front context. | Live Hera run confirms hidden technical HUD and selector, visible three front panels with one minimap-context surface each, and `PREPARE → STOPPED 3X3 → MANIPULATE → RESULT_CONFIRM → COMMIT → BATTLE`. Diagnostics reported zero errors. | PASS |
| 5 | Use unapproved or non-runtime-safe visual files. | Visual manifest/run record binds only approved local masters to deterministic runtime exports; `run_command_visual_asset_test.gd` validates all seven exported PNGs. | PASS |

## Evidence

- Headless Godot suite: 21 scripts passed.
- Scoped Python documentation/authority suite: 61 tests passed.
- Current documentation validator: `Project Core documentation validation PASSED`.
- Live technical smoke: a fresh Omenward Godot session reached `BATTLE`; diagnostics: 0 errors, 0 warnings.

## Remaining gates

```text
CURRENT_GODOT_RUNTIME = PARTIAL__RUN_COMMAND_UI_TECHNICAL_SMOKE_CAPTURED
CURRENT_MINIMAP_READABILITY = NOT_RUN
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
```

## Incident / Solution / Lesson · 2026-08-27

- **Incident:** the current repository's CI-routed static tests still expected a superseded protected baseline and Godot AI `3.1.4`, while the actual current adapter and enabled plugin report `d4d99168…` and `3.2.0` respectively. This made the verification surface contradict the checked-in state.
- **Solution:** updated only those test expectations to the exact current tracked values, then reran both authority/tool-state suites successfully. The unrelated local `test_base_recovery_map` requirement for a CI-only `_base_recovery` checkout remains an environment limitation, not a PASS claim.
- **Lesson:** version and protected-baseline assertions must be refreshed together with their canonical tracked owner; a historical approval record must remain historical rather than being used as a live version assertion.
