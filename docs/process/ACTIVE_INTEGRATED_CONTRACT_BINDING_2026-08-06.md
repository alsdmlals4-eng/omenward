# [현행] OMENWARD 통합 작업지시문 v4.4 활성 바인딩

```yaml
decision_id: OMW-DEC-20260808-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-4-AND-RECONCILE-ENTRY-STATE-V1
last_gate_update_decision: OMW-DEC-20260809-TOOLS-GODOT-AI-3-1-3-HERA-GUT-USER-APPROVAL-REMOTE-SYNC-RECONCILIATION-V1
contract_name: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION
contract_version: "4.4"
contract_status: ACTIVE_INTEGRATED_AUDIT_IMPLEMENTATION_DELIVERY_CONTRACT
binding_status: ACTIVE
counter: NON_COUNTER
activation_authority: USER_DIRECT_APPROVAL_IN_CURRENT_CONVERSATION
source_repository_main: f1bf8939208a864bce1f99eea0555f05369dc9d6
base_recovery_exact_commit: fa69a77a14f923a756064f6ae151d34cadb374f7
base_current_main_observed: 2a6ced23f6d6de1fb6e0a281c7138beb03f1a13b
reconciliation_branch: tools/godot-ai-3-1-3-hera-gut-approval-sync-20260809
entry_gate: BLOCK
```

## 1. 병영 planning state

```text
9/10 = dedicated exact 10,000-seed V00 robustness PASS
FUNCTIONAL_VALUE_COMBAT_NUMERICS_REVIEW = COMPLETE
FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS = DEFINED
BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED = OPEN
NEXT_GATE = BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE
```

9/10 evidence and final-value boundaries remain unchanged.

## 2. User-approved tool state

```text
GODOT_AI_APPROVED_VERSION = 3.1.3
GUT_9_7_1 = APPROVED
GUT_USER_REPORTED_LOCAL_ENABLEMENT = ENABLED_NOT_HOST_VERIFIED
HERA_1_0_0 = APPROVED
HERA_USER_REPORTED_LOCAL_ENABLEMENT = ENABLED_NOT_HOST_VERIFIED
```

Upstream evidence:

```text
Godot AI = hi-godot/godot-ai v3.1.3 / plugin SHA256 10fac40e7f4900e788d79f8ee57228e355e02ee01008d8e7093da2bb1580a4c7
GUT = bitwes/Gut v9.7.1 / branch godot_4_7
Hera = NotNull92/hera-agent-godot v1.0.0 / MIT
```

Current role split remains mandatory:

```text
Godot AI/HiGodot = SOLE_PERSISTENT_GODOT_AUTHORING_AUTHORITY
GUT = DETERMINISTIC_GDSCRIPT_TEST_AUTHORITY
Hera = LIVE_QA_AND_OBSERVABILITY_ONLY
Hera persistent source mutation = FORBIDDEN
ROLE_OVERLAP = FORBIDDEN
```

## 3. Existing Solution First — Hera

```text
HERA_EXISTING_SOLUTION_DISPOSITION = REUSE_APPROVED_BY_USER
HERA_PROJECT_PLUGIN_VERSION = 1.0.0
HERA_UPSTREAM_RELEASE = v1.0.0
HERA_LICENSE = MIT
HERA_BUNDLED_README_VERSION = 0.9.0_STALE_METADATA_NONBLOCKING
```

The historical direct-main Hera import is no longer an unresolved adoption/disposition blocker.

## 4. Remote synchronization readback

Current remote main:

```text
REMOTE_SYNC_MAIN = f1bf8939208a864bce1f99eea0555f05369dc9d6
REMOTE_GODOT_AI_VERSION = 3.1.3
REMOTE_PROJECT_GODOT_GODOT_AI_ENABLED = TRUE
REMOTE_PROJECT_GODOT_GUT_ENABLED = TRUE
REMOTE_PROJECT_GODOT_HERA_ENABLED = TRUE
REMOTE_HERA_GAME_INSPECTOR_AUTOLOAD = PRESENT
REMOTE_SYNC_COMPLETION = VERIFIED
```

Closed approval/provenance/sync blockers:

```text
HIGODOT_EXACT_SOURCE_OR_VERSION_UNVERIFIED
GUT_ADOPTION_SPEC_PR155_NOT_MERGED
HERA_PRESENT_BUT_ADOPTION_NOT_VERIFIED
DIRECT_MAIN_HERA_IMPORT_NOT_YET_DISPOSITIONED
GODOT_AI_3_1_3_REMOTE_SYNC_REQUIRED
GUT_REMOTE_ENABLEMENT_SYNC_REQUIRED
HERA_REMOTE_ENABLEMENT_SYNC_REQUIRED
```

## 5. Entry Gate

```text
ENTRY_GATE = BLOCK
```

Current blockers:

- `BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED`
- `LOCAL_GODOT_AND_AUDIO_VAULT_UNAVAILABLE`
- historical secret-scan accepted risk

Allowed planning action is `BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE`.

Continue to forbid unverified completion claims and unauthorized mutation:

```text
PRODUCT_IMPLEMENTATION
GODOT_AUTHORING_MUTATION_WITHOUT_HIGODOT
HERA_PERSISTENT_SOURCE_MUTATION
HERA_LIVE_QA_COMPLETION_CLAIM_WITHOUT_RUN
LOCAL_MAIN_SYNC_CLAIM
GODOT_RUNTIME_CLAIM
BARRACKS_10000_SEED_PARAMETER_SELECTION_EXECUTION
BARRACKS_50000_SEED_CONFIRMATION
```

## 6. Hosted/local boundary

The user's local plugin enablement report is accepted as a user fact and the same configuration is now present on remote main. This hosted session still cannot inspect the Windows editor/runtime directly, so local editor/runtime verification remains unclaimed.

## 7. Sheet sync

Current Decision ID to synchronize in GitHub and Sheet:

`OMW-DEC-20260809-TOOLS-GODOT-AI-3-1-3-HERA-GUT-USER-APPROVAL-REMOTE-SYNC-RECONCILIATION-V1`

No seed run occurs in this Gate; `47_병영_Smoke_결과` remains unchanged.
