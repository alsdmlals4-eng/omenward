# Barracks Role-Output Runtime Implementation Plan

> Decision: `OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1`
> Baseline: `b77fb4dcf0bead75ab796cb287fa510dd7ec751e`
> Mode: execution plan only; persistent Godot authoring requires HiGodot.

## Preconditions

- [ ] Fresh-read Base main, OMENWARD main, open PRs, Sheet and Entry Gate before execution.
- [ ] Verify Godot AI/HiGodot 3.1.3, GUT 9.7.1 and Hera 1.0.0 remain enabled/approved.
- [ ] Confirm no conflicting product/runtime PR touched the target files after this package baseline.
- [ ] Preserve `FINAL_FUNCTIONAL_VALUE_INDEX = NOT_SELECTED` and `FINAL_PARAMETER_VECTOR = NOT_SELECTED`.

## Task 1 — GUT RED: common combat contracts

**Authority:** GUT test authority. No product write.

- [ ] Create adopted GUT suite for role-output runtime behavior.
- [ ] RED: physical damage exercises armor; magic damage exercises magic resistance.
- [ ] RED: existing `target_priority_tags` are consumed deterministically, with nearest fallback.
- [ ] RED: identical scenario input emits stable event ordering.
- [ ] Fail if zero-test discovery occurs.

Expected Red: current `receive_damage(raw_damage)` has no channel/MR path and `LaneState.find_target()` ignores target priorities.

## Task 2 — GUT RED: Priest / FV-PRIEST-01

- [ ] RED: Priest deterministically selects same-lane lowest-health ally.
- [ ] RED: heal output separates raw/effective/overheal.
- [ ] RED: when no heal target exists, encouragement starts instead.
- [ ] RED: buff uptime and supported-target seconds are measurable.
- [ ] Preserve PoC values as `PROVISIONAL_POC_INPUT`, never final numeric authority.

## Task 3 — GUT RED: Mage / FV-MAGE-01

- [ ] RED: `cluster` priority chooses a deterministic legal target.
- [ ] RED: primary vs collateral AoE damage is separately observable.
- [ ] RED: bounded max-target behavior.
- [ ] RED: magic channel reaches MR path.
- [ ] Keep control output `BLOCKED_RUNTIME_OUTPUT` unless a real control behavior is implemented in scope.

## Task 4 — GUT RED: Flier / FV-FLIER-01

- [ ] RED: Flier backline contact does not degrade to ordinary nearest-frontline movement.
- [ ] RED: first backline-contact tick/time is observable.
- [ ] RED: dive event/output is deterministic when its provisional action is active.
- [ ] RED: Archer `flying` priority can choose Flier when applicable.
- [ ] Keep air-targetability exposure blocked until actual anti-air exposure semantics exist.

## Task 5 — GUT RED: Giant / FV-GIANT-01

- [ ] RED: slam hits bounded same-lane targets deterministically.
- [ ] RED: slam excludes air targets.
- [ ] RED: slam targets-hit and total-damage are observable.
- [ ] RED: existing gate/base siege event outputs remain intact.

## Task 6 — HiGodot authoring manifest

**Persistent writer:** HiGodot only.

Candidate files, only when demanded by a Red test:

- `scripts/battle/unit_instance.gd`
- `scripts/battle/lane_state.gd`
- `scripts/battle/battle_simulator.gd`
- `scripts/data/unit_archetype_profile.gd` only if existing fields cannot express an accepted Red case
- `data/units/priest.tres`
- `data/units/mage.tres`
- `data/units/flier.tres`
- `data/units/giant.tres`
- deterministic role-output collector/harness
- GUT tests

`project.godot` is not an expected authoring target because all three plugins are already enabled.

Authoring rules:
- [ ] Do not build a generic ability framework.
- [ ] Reuse `role`, `magic_resistance`, `target_priority_tags`, `attack_profile_id`, `structure_damage_tags` first.
- [ ] Extend existing `_record_event()` / `drain_events()` instead of creating a parallel telemetry bus.
- [ ] If a new exported field is unavoidable, prove it with a Red test and document its rollback.
- [ ] Read back every persisted HiGodot target after save.

## Task 7 — GUT Green + regression

- [ ] All focused role-output GUT tests Green.
- [ ] GUT discovered test count > 0 and at/above package minimum.
- [ ] Existing GUT/headless affected regressions Green.
- [ ] No test/fixture cleanup mutates product source.
- [ ] Godot import/parse completes without plugin/resource/script errors.

## Task 8 — Deterministic scenario collector

- [ ] Run `FV-COMMON-01`.
- [ ] Run `FV-PRIEST-01`.
- [ ] Run `FV-MAGE-01`.
- [ ] Run `FV-FLIER-01`.
- [ ] Run `FV-GIANT-01`.
- [ ] Emit role-specific vectors only; no weighted utility.
- [ ] Preserve raw event evidence.
- [ ] Serialize unavailable outputs as `BLOCKED_RUNTIME_OUTPUT`, never numeric zero.

## Task 9 — Hera live QA

- [ ] Snapshot tracked source before Hera.
- [ ] Execute run/input/inspect/assert/diagnostics only.
- [ ] Validate Priest, Mage, Flier and Giant observable behavior in live runtime.
- [ ] Do not use Hera persistent editor/source mutation.
- [ ] Snapshot tracked source after Hera.
- [ ] Require **tracked source delta NONE**.

## Task 10 — exact-head implementation PR

- [ ] Full changed-file inventory matches HiGodot Authoring Manifest + GUT test files.
- [ ] Godot AI/HiGodot authoring evidence attached.
- [ ] GUT focused + regression evidence attached; zero-test discovery forbidden.
- [ ] Hera source delta NONE evidence attached.
- [ ] Windows/Android shared-core contract unaffected or validated where touched.
- [ ] GPT role-separated adversarial review P0/P1 = 0.
- [ ] Required workflows Green on current validation identity.
- [ ] Same Decision lineage synced to Sheet.
- [ ] Squash merge using inherited approval authority if no new user decision is introduced.
- [ ] Merged-main readback.

## Current execution status

`DEFERRED_EXTERNAL_EXECUTOR`: this ChatGPT session has no callable HiGodot persistent-authoring executor. GitHub text mutation must not be used to bypass that authority. The package is ready for a HiGodot-capable executor, while global Entry Gate remains blocked until actual runtime implementation and verification complete.
