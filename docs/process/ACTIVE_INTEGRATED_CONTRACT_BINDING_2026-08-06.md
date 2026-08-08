# [현행] OMENWARD 통합 작업지시문 v4.4 활성 바인딩

```yaml
decision_id: OMW-DEC-20260808-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-4-AND-RECONCILE-ENTRY-STATE-V1
last_gate_update_decision: OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-MEASUREMENT-SCENARIOS-DEFINITION-V1
contract_name: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION
contract_version: "4.4"
contract_status: ACTIVE_INTEGRATED_AUDIT_IMPLEMENTATION_DELIVERY_CONTRACT
binding_status: ACTIVE
counter: NON_COUNTER
activation_authority: USER_DIRECT_APPROVAL_IN_CURRENT_CONVERSATION
source_repository_main: 02b803b075d5e44f5aa3db895c5dad025d048148
base_recovery_exact_commit: fa69a77a14f923a756064f6ae151d34cadb374f7
base_current_main_observed: 2a6ced23f6d6de1fb6e0a281c7138beb03f1a13b
reconciliation_branch: planning/barracks-functional-value-measurement-scenarios-20260809
entry_gate: BLOCK
```

## 1. 현재 병영 lineage

```text
5/10 = exact 2,000-seed remediation smoke PASS
6/10 = parameter-selection pre-review complete
7/10 = observables defined / V00 cost60 interval1.70 non-final envelope
8/10 = robustness execution review complete / 당시 10k NOT_RUN
9/10 = dedicated exact 10,000-seed V00 robustness PASS
FUNCTIONAL_VALUE_COMBAT_NUMERICS_REVIEW = COMPLETE
FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS = DEFINED
```

9/10 evidence remains unchanged.

```text
SPECIAL_TOKEN_SHARE_10_MIN = 0.296265
SPECIAL_TOKEN_SHARE_BURST_MAX = 0.333333
10K_JSON_SHA256 = 1675d5068d6299c618df2f5b27cca4cf6fb06990729d622cedf9c36282c8d3c3
10K_CSV_SHA256 = e7324cb7a46cdab3d765011890d38a234c541c9e28741a2e6af6d3bf2bbc0e8b
```

## 2. Functional-value measurement contract

```text
FIXTURE_POLICY = DETERMINISTIC_SAME_INPUT
FUNCTIONAL_VALUE_COMPARISON = ROLE_SPECIFIC_VECTOR_NO_SINGLE_WEIGHTED_SCORE
POST_HOC_WEIGHT_TUNING = FORBIDDEN
BLOCKED_RUNTIME_OUTPUT = NEVER_SYNTHESIZE_AS_ZERO
MONTE_CARLO_ROLE_VALUE = NOT_AUTHORIZED_BEFORE_ROLE_OUTPUT_RUNTIME_EXISTS
```

Scenario IDs:

```text
FV-COMMON-01
FV-PRIEST-01
FV-MAGE-01
FV-FLIER-01
FV-GIANT-01
```

Role-defining missing outputs remain explicitly blocked. No final functional-value scalar is selected.

## 3. Blocker transition

Closed:

```text
BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_REQUIRED
```

Still blocking:

```text
BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED
```

First allowed next action:

```text
BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE
```

This next Gate defines the runtime schema/behavior/instrumentation/test package. It does not itself authorize persistent Godot mutation.

## 4. Tool-state boundary

Current repository baseline still records Godot AI 3.1.2 enabled, with GUT 9.7.1 and Hera 1.0.0 files present but not enabled in remote `project.godot`.

The user has explicitly declared:

```text
GODOT_AI_APPROVED_VERSION = 3.1.3
HERA_PLUGIN = ENABLED_AND_USER_APPROVED
GUT_PLUGIN = ENABLED_AND_USER_APPROVED
```

This approval is recognized, but remote synchronization is not claimed inside this planning-only Decision. A separate tool-state reconciliation Decision will replace stale approval blockers with remote-sync verification blockers.

## 5. Entry Gate

```text
ENTRY_GATE = BLOCK
```

Current planning/runtime blocker:
- `BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED`

Current remote/tool blockers remain until separate reconciliation:
- `GUT_ADOPTION_SPEC_PR155_NOT_MERGED`
- `HIGODOT_EXACT_SOURCE_OR_VERSION_UNVERIFIED`
- `HERA_PRESENT_BUT_ADOPTION_NOT_VERIFIED`
- `DIRECT_MAIN_HERA_IMPORT_NOT_YET_DISPOSITIONED`
- local Godot/audio unavailable
- historical secret-scan accepted risk

Continue to forbid:

```text
PRODUCT_IMPLEMENTATION
GODOT_AUTHORING_MUTATION
BARRACKS_10000_SEED_PARAMETER_SELECTION_EXECUTION
BARRACKS_50000_SEED_CONFIRMATION
FINAL_FUNCTIONAL_VALUE_INDEX_SELECTION
FINAL_PARAMETER_VECTOR_SELECTION
```

## 6. Sheet sync

Same Decision ID is recorded in GitHub and Sheet:

`OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-MEASUREMENT-SCENARIOS-DEFINITION-V1`

No seed run occurs in this Gate, so `47_병영_Smoke_결과` remains unchanged.
