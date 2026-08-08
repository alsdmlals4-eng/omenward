# [현행] 오멘워드 기획·운영 정본 결정 원장

```yaml
updated_at: 2026-08-09
status: CURRENT_DECISION_LEDGER
source_main_observed: 02b803b075d5e44f5aa3db895c5dad025d048148
base_main_observed: 2a6ced23f6d6de1fb6e0a281c7138beb03f1a13b
current_process_decision: OMW-DEC-20260808-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-4-AND-RECONCILE-ENTRY-STATE-V1
last_gate_update_decision: OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-MEASUREMENT-SCENARIOS-DEFINITION-V1
base_recovery_status: COMPLETE
project_base_adapter_status: FRESHNESS_RECONCILED
active_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.4
onboarding_planning_status: APPROVED_10_OF_10_WITH_TOKEN_SOURCE_AMENDMENT
current_simulation_batch: 5_OF_10_SMOKE_PASS / 6_OF_10_REVIEW_COMPLETE / 7_OF_10_OBSERVABLES_DEFINED / 8_OF_10_ROBUSTNESS_REVIEW_COMPLETE / 9_OF_10_ROBUSTNESS_10000_PASS / FUNCTIONAL_VALUE_REVIEW_COMPLETE / MEASUREMENT_SCENARIOS_DEFINED
current_simulation_pr: 170
product_code_authority: NONE
entry_gate: BLOCK
```

이 원장은 current Decision 색인과 충돌 해소 우선순위를 책임진다. Google Sheet는 동일 Decision ID와 exact-head/merge evidence를 기록하지만 제품 정본을 단독 대체하지 않는다.

## 1. 병영 Decision lineage

| 단계 | 상태 | Decision |
|---|---|---|
| 5/10 | exact 2,000-seed remediation smoke PASS | `OMW-DEC-20260808-PLANNING-BARRACKS-CAPABILITY-PROXY-AND-MULTI-SPECIAL-TOKEN-BURST-REMEDIATION-V1` |
| 6/10 review | parameter-selection pre-review complete | `OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-DECISION-SWEEP-REVIEW-V1` |
| 7/10 | observables / V00 cost+interval non-final envelope | `OMW-DEC-20260808-PLANNING-BARRACKS-PARAMETER-SELECTION-OBSERVABLES-DEFINITION-V1` |
| 8/10 review | robustness execution review / 당시 10k NOT_RUN | `OMW-DEC-20260808-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-ONLY-REVIEW-V1` |
| 9/10 | dedicated exact 10,000-seed V00 robustness PASS | `OMW-DEC-20260809-PLANNING-BARRACKS-10000-SEED-ROBUSTNESS-EXECUTION-V1` |
| functional-value review | base numerics present / role output runtime partial | `OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-COMBAT-NUMERICS-DEFINITION-REVIEW-V1` |
| measurement scenarios | deterministic same-input role vectors defined / missing outputs blocked | `OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-MEASUREMENT-SCENARIOS-DEFINITION-V1` |

9/10 evidence remains exact:

```text
SPECIAL_TOKEN_SHARE_10_MIN = 0.296265
SPECIAL_TOKEN_SHARE_BURST_MAX = 0.333333
10K_JSON_SHA256 = 1675d5068d6299c618df2f5b27cca4cf6fb06990729d622cedf9c36282c8d3c3
10K_CSV_SHA256 = e7324cb7a46cdab3d765011890d38a234c541c9e28741a2e6af6d3bf2bbc0e8b
```

## 2. Functional-value measurement scenarios

```text
FIXTURE_POLICY = DETERMINISTIC_SAME_INPUT
FUNCTIONAL_VALUE_COMPARISON = ROLE_SPECIFIC_VECTOR_NO_SINGLE_WEIGHTED_SCORE
POST_HOC_WEIGHT_TUNING = FORBIDDEN
BLOCKED_RUNTIME_OUTPUT = NEVER_SYNTHESIZE_AS_ZERO
MONTE_CARLO_ROLE_VALUE = NOT_AUTHORIZED_BEFORE_ROLE_OUTPUT_RUNTIME_EXISTS
```

Approved scenarios:

```text
FV-COMMON-01 = common single-target contact
FV-PRIEST-01 = support attrition
FV-MAGE-01 = cluster versus Archer
FV-FLIER-01 = backline pressure versus Assassin
FV-GIANT-01 = siege/frontline versus Greatsword
```

Role relationships:

```text
ARCHER_SUSTAINED_SINGLE_TARGET_DPS > MAGE
ASSASSIN_SINGLE_TARGET_BURST > FLIER
FLIER_BACKLINE_PRESSURE_DURATION > ASSASSIN
GIANT_VALUE_REQUIRES_SURVIVAL_AOE_SIEGE_ADVANTAGE
PRIEST_VALUE_REQUIRES_SUPPORT_OUTPUT_NOT_DAMAGE_SCALAR
```

Missing role-defining outputs remain blockers, not zero observations.

## 3. Blocker transition

Closed by the current Decision:

```text
BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_REQUIRED
```

Current barracks blocker:

```text
BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED
```

First next action:

```text
BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE
```

That package is a planning/implementation-contract Gate. Persistent Godot mutation remains separately gated by tool state and authoring authority.

## 4. Product taxonomy and historical analysis taxonomy

Current product taxonomy:

```text
PRODUCT_SPECIAL_CORPS = PRIEST / MAGE / FLIER / GIANT
ASSASSIN = BASIC_BARRACKS_SPECIALIZATION
```

Historical smoke model `ASSASSIN / PRIEST / MAGE / FLYING / GIANT` remains point-in-time analysis labels and is not product membership authority.

## 5. Base freshness

```text
Base current main = 2a6ced23f6d6de1fb6e0a281c7138beb03f1a13b
Base release pin = 9.4.3 / NO_AUTOMATIC_MIGRATION
Base delta classification = CONTINUOUS_WORK_BLOCKER_RECOVERY_ROUTING_ONLY
Project Base Adapter schema/generator/validator delta = NONE_OBSERVED
```

## 6. Tool / Entry Gate current remote evidence

Current repository evidence at this Gate baseline still shows:

```text
project.godot editor plugin enablement = Godot AI only
addons/godot_ai/plugin.cfg = 3.1.2
addons/gut/plugin.cfg = 9.7.1
addons/hera_agent_godot/plugin.cfg = 1.0.0
```

User subsequently declared Godot AI 3.1.3 and Hera/GUT plugin enablement+approval. That user-approved state will be reconciled under a separate tool-state Decision so this PR stays planning-only and does not falsely claim remote sync.

Entry Gate remains `BLOCK` pending runtime-output implementation and current remote/tool synchronization.

## 7. Current responsibility sources

- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md`
- `docs/design/APPROVED_OMENWARD_BARRACKS_10000_SEED_ROBUSTNESS_EXECUTION_RESULTS_2026-08-09.md`
- `docs/design/APPROVED_OMENWARD_BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_DEFINITION_REVIEW_2026-08-09.md`
- `docs/design/APPROVED_OMENWARD_BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_2026-08-09.md`
- `docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json`
