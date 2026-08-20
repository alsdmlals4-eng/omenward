# OMENWARD · 2026-08-20 재기획 Decision 1~6 + Canon Reconciliation 적대적 검토

```yaml
review_id: OMW-REVIEW-20260820-REPLAN-DEC1-6-CANON-01
status: CLEAN_REVIEW_EXIT_FOR_REVIEWED_SCOPE
reviewed_at: 2026-08-20
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
skill: running-adversarial-review-and-refinement
full_loop_count: 5
minimum_full_loops: 5
review_scope:
  - approved replan Decisions 1 through 6
  - active project entry/routing canon
  - Notion/GitHub routing meaning
  - current PR/runtime/evidence boundary
  - visual pause state
not_in_scope_as_completed:
  - world conflict/core story decision
  - 20 Stage detailed content/boss identities
  - balance budget
  - text UX specification
  - current Godot runtime verification
```

## 1. Review input

Approved 2026-08-20 Decisions:

```text
OMW-PLAN-20260820-WORLD-ROLE-01
OMW-PLAN-20260820-MAPRUN-WORLD-01
OMW-PLAN-20260820-PRESSURE-LANGUAGE-01
OMW-PLAN-20260820-MOBILIZATION-REGISTRY-01
OMW-PLAN-20260820-FIRST5-FTUE-01
OMW-PLAN-20260820-RUN-COMMAND-SHELL-01
```

Protected user/workstream boundaries:

```text
IMAGE_GENERATION = PAUSED_PENDING_USER_REFERENCE_FILES
PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY
CURRENT_RUNTIME = NOT_RUN
HUMAN_PLAYER_EVIDENCE = NOT_RUN
```

Fresh GitHub work-item truth used by the review:

```text
PR175 = CLOSED_UNMERGED_HISTORICAL
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
ISSUE176 = OPEN_HISTORICAL_FOLLOWUP_REQUIRES_RECONCILIATION
PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY
```

## 2. Full loop 1

```yaml
loop_index: 1
input_state_or_head: 5ed18714b2cf9bd0c07670519cb5f50973d00c79
evidence_delta:
  - visual generation was paused after user rejected the first generated candidate
  - CURRENT_CONFIRMED_DECISIONS still routed NEXT to Visual Requirement Inventory
  - fresh PR175/177 state no longer matched several active documents
full_scope_findings:
  - current Decision index had a stale next gate
  - active routing could send a future agent back into completed visual-inventory work
  - old Phase C/PR175 state was capable of overriding reopened planning in practice
validated_findings:
  - MUST_FIX / CONFLICT: current next gate drift
  - MUST_FIX / CONFLICT: active current-state documents still treated historical PR175 state as current
changes_applied:
  - rerouted planning toward non-image work and world/story after review
  - preserved visual A direction but marked first generated candidate REJECTED_NOT_CANON and generation paused
verification:
  - fresh current Decision/Active Context readback
better_alternative_result:
  - rejected deleting all historical Phase B/C0/PR175 evidence; explicit history labels preserve provenance with lower compatibility risk
long_term_fit:
  - current routing becomes resumable without losing old evidence
unresolved:
  - world conflict/core story remains genuinely undecided
clean_exit_candidate: false
```

## 3. Full loop 2

```yaml
loop_index: 2
input_state_or_head: active entry docs before 2026-08-20 reconciliation
evidence_delta:
  - README, AGENTS, GDD, PROJECT_CORE, CURRENT_IMPLEMENTATION_STATUS, DECISIONS_PENDING still exposed MAIN_CANONICAL_APPROVED_10_OF_10 and/or PR175 OPEN as current
full_scope_findings:
  - user-facing and agent-facing entrypoints contradicted fresh GitHub truth
  - GDD and Project Core mixed correct mechanics with obsolete operational state
  - runtime status promoted old signal11 diagnosis to current blocker despite current runtime NOT_RUN
validated_findings:
  - MUST_FIX / CONFLICT: stale active entrypoint state
  - MUST_FIX / EVIDENCE_CEILING: historical runtime blocker stated as current
changes_applied:
  - refreshed README.md
  - refreshed AGENTS.md
  - rebuilt OMENWARD_GDD_CURRENT_CANON.md around Decisions 1~6 and current evidence ceiling
  - refreshed PROJECT_CORE.md
  - refreshed CURRENT_IMPLEMENTATION_STATUS.md
  - refreshed DECISIONS_PENDING.md
verification:
  - current docs explicitly say PR175/177 closed-unmerged, Issue176 historical-reconcile, PR197 read-only, current runtime NOT_RUN
better_alternative_result:
  - selected thin current summaries plus links to detailed historical owners instead of copying old runtime packets forward
long_term_fit:
  - reduces accidental reactivation of closed work while preserving detailed evidence for later reconciliation
unresolved:
  - broader router documents had not yet been rechecked
clean_exit_candidate: false
```

## 4. Full loop 3

```yaml
loop_index: 3
input_state_or_head: reconciled core entry docs
evidence_delta:
  - Decision 1~6 semantics re-attacked against core mechanics and current UI/prototype lineage
full_scope_findings:
  - potential confusion between three Omen Wheels and three lanes
  - plausible Stage 1 overload from six mandatory T1 buildings
  - rejected visual candidate itself incorrectly suggested lane-linked wheels but is non-canon
  - world conflict / cause of Omen Cycle / Stage 20 meaning still absent
validated_findings:
  - REJECTED_CRITIQUE for changing the three-wheel mechanic: current Decision explicitly forbids wheel-lane fixed mapping
  - DEFER/REVISIT for reducing Stage 1 buildings: overload is plausible but no human evidence exists; progressive three-group disclosure is lower-risk current solution
  - USER_DECISION_REQUIRED: world/story gap is real and is not solved by Decisions 1~6
changes_applied:
  - protected THREE_REELS_TO_THREE_LANES_FIXED_MAPPING = FORBIDDEN across current owners
  - preserved six T1 FTUE with explicit human-test revisit condition
  - made world/story gap explicit in GDD, Project Core, Pending Decisions
verification:
  - current GDD/Project Core/Decision index agree on protected mechanics and pending story scope
better_alternative_result:
  - no stronger evidence-supported alternative justified reopening Decisions 1~6
long_term_fit:
  - modular Pressure language + world-independent mechanics support future factions/regions without reworking counters
unresolved:
  - world/story Decision intentionally remains next
clean_exit_candidate: false
```

## 5. Full loop 4

```yaml
loop_index: 4
input_state_or_head: core docs corrected; broader repository routing re-attacked
evidence_delta:
  - DOCUMENTATION_MAP and DOCUMENT_LIFECYCLE_REGISTRY still routed to v4.5/Phase C/PR175
  - current GitHub workstream and evidence boundaries were rechecked
full_scope_findings:
  - active documentation routing remained stale even after primary entry docs were corrected
  - old Google Sheet routing was still described as current human source in legacy process docs
  - PR197 protection and runtime NOT_RUN needed to remain fail-closed
validated_findings:
  - MUST_FIX / OMISSION+CONFLICT: current router/lifecycle consumers not updated
  - NO_CHANGE: PR197 remains read-only; no scope expansion justified
  - NO_CHANGE: historical signal11/GUT/FV records remain evidence, not deletion candidates
changes_applied:
  - refreshed DOCUMENTATION_MAP.md
  - refreshed DOCUMENT_LIFECYCLE_REGISTRY.md
  - marked v4.5 binding/C0 materials historical evidence
  - routed current human-facing canon to Notion and structured/runtime canon to GitHub
verification:
  - current entry order starts at README/AGENTS/CURRENT_CONFIRMED_DECISIONS/ACTIVE_CONTEXT/GDD
better_alternative_result:
  - explicit lifecycle labels are safer than mass-deleting old evidence and test-consumed markers
long_term_fit:
  - future agents can distinguish CURRENT, EVIDENCE, PAUSED, and compatibility markers
unresolved:
  - Decision Ledger and Roadmap still required re-attack
clean_exit_candidate: false
```

## 6. Full loop 5

```yaml
loop_index: 5
input_state_or_head: broad routing mostly reconciled
evidence_delta:
  - PROJECT_CANON_DECISION_LEDGER and OMENWARD_ROADMAP were fresh-read
  - both still exposed v4.5/Phase C/PR175 as current routing
full_scope_findings:
  - two remaining active routers could resurrect obsolete execution direction
validated_findings:
  - MUST_FIX / CONFLICT: Decision Ledger stale current phase
  - MUST_FIX / CONFLICT: Roadmap stale current milestone
changes_applied:
  - refreshed PROJECT_CANON_DECISION_LEDGER.md
  - refreshed OMENWARD_ROADMAP.md
  - current next product decision is world conflict/core story
  - current implementation remains unauthorized and runtime NOT_RUN
verification:
  - fresh main readback after router changes
  - remaining old PR175/10-of-10 strings are classified as historical/compatibility material or explicitly labeled historical in current docs
better_alternative_result:
  - current six Decisions survive without mechanic reversal; best next improvement is to close the missing story layer rather than churn settled mechanics
long_term_fit:
  - current architecture separates reusable mechanics from expandable world/faction/content layers
unresolved:
  - world/story/content/balance/text UX are planned next scope, not blockers to CLEAN exit for Decision 1~6 + routing review
clean_exit_candidate: true
```

## 7. Finding disposition

| Finding | Class | Decision |
|---|---|---|
| stale Visual Inventory next gate | CONFLICT | MUST_FIX · fixed |
| README/AGENTS/GDD/Core old Phase C state | CONFLICT | MUST_FIX · fixed |
| old signal11 presented as current blocker | EVIDENCE_CEILING | MUST_FIX · fixed to NOT_RUN/UNVERIFIED |
| Documentation Map/Lifecycle stale routing | OMISSION / CONFLICT | MUST_FIX · fixed |
| Decision Ledger/Roadmap stale routing | CONFLICT | MUST_FIX · fixed |
| wheel ↔ lane 1:1 confusion | regression risk | already protected; no mechanic change |
| Stage1 six-building overload | usability hypothesis | DEFER / human-test revisit |
| PR197 | DUPLICATE/other workstream risk | READ_ONLY · untouched |
| PR175/177 history | legacy evidence | ALLOWED_LEGACY / do not revive |
| Issue176 | historical follow-up | DEFER until implementation reconciliation |
| world conflict/story missing | product decision gap | USER_DECISION_REQUIRED · next scope |

## 8. CLEAN_REVIEW_EXIT

```text
FULL_LOOP_COUNT = 5
MINIMUM_FULL_LOOPS_SATISFIED = TRUE
NEW_MUST_FIX_IN_REVIEWED_SCOPE_AFTER_LOOP_5 = 0
DECISION_1_TO_6_REGRESSION = NONE_FOUND
CURRENT_ROUTING_CONFLICT = NONE_FOUND_AFTER_FIXES
CURRENT_RUNTIME_PASS_CLAIM = NONE
HUMAN_PASS_CLAIM = NONE
PR197_MUTATION = NONE
VISUAL_REJECTED_CANDIDATE_PROMOTED = FALSE
CLEAN_REVIEW_EXIT = PASS_FOR_DECISIONS_1_TO_6_AND_CURRENT_ROUTING_SCOPE
WHOLE_PROJECT_PLANNING_COMPLETE = FALSE
NEXT_PRODUCT_DECISION = WORLD_CONFLICT_AND_CORE_STORY
```

Clean exit here means the **reviewed scope** is clean enough to proceed. It does not mean OMENWARD planning, implementation, runtime validation, visual validation, or human play validation is complete.
