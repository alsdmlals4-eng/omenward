# OMENWARD Integrated Contract v4.3 Activation Plan

```yaml
decision_id: OMW-DEC-20260806-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-3-V1
contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION
contract_version: "4.3"
contract_status: ACTIVE_INTEGRATED_AUDIT_IMPLEMENTATION_DELIVERY_CONTRACT
base_main: 7588317f294d602cfad5f7f15bfebcf849b8a77b
base_repository_main: 4f98f968a377f7b6a11aafa4fc94d11bddbebedc
counter: NON_COUNTER
```

## Goal

Bind user-approved contract v4.3 as the active operating contract without opening product, Godot authoring, formal GUT execution, merge, local sync, or runtime gates prematurely.

## Test-first sequence

1. Add a focused Python contract test that requires an active v4.3 state and validator. Confirm RED because the validator/state do not exist.
2. Add the binding document, machine-readable state, validator, workflow, and adversarial review.
3. Confirm the bootstrap Python contract tests pass while the entry gate remains intentionally blocked.
4. Open a Draft PR and synchronize the same Decision ID and exact head to Google Sheet.
5. Re-read the Draft PR, Sheet rows, and exact-head workflow evidence.

## Exact scope

```text
docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-06.md
docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json
docs/reviews/ADVERSARIAL_INTEGRATED_CONTRACT_V4_3_ACTIVATION_REVIEW_2026-08-06.md
docs/superpowers/plans/2026-08-06-activate-integrated-contract-v4-3.md
tests/python/test_active_integrated_contract_v4_3.py
tools/validate_active_integrated_contract_v4_3.py
.github/workflows/validate-active-integrated-contract-v4-3.yml
```

## Non-goals

- Do not copy or modify `addons/gut/**`.
- Do not modify Scene, Resource, Theme, Animation, `project.godot`, InputMap, autoload, product code, data, image, or audio assets.
- Do not claim exact Godot 4.7.x, HiGodot version/commit, audio Vault access, GUT discovery, JUnit, Windows, Android, local sync, or runtime validation.
- Do not mark PR #155 or PR #156 Ready and do not merge them.

## Contract transition

- v4.3 becomes the active operating contract for this project and conversation.
- v4.2 becomes historical comparison evidence only.
- `APPLICATION_BINDING=ACTIVE` does not imply `ENTRY_GATE=PASS`.
- Until the blocking evidence closes, allowed work is restricted to reconciliation, adoption-spec review, provenance evidence, and exact-path remediation records.
