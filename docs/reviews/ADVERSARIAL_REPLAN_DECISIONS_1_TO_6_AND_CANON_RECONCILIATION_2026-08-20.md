# OMENWARD · 2026-08-20 재기획 Decision 1~6 + Canon Reconciliation 적대적 검토

```yaml
review_id: OMW-REVIEW-20260820-REPLAN-DEC1-6-CANON-01
status: CLEAN_REVIEW_EXIT_FOR_REVIEWED_SCOPE
reviewed_at: 2026-08-20
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
skill: running-adversarial-review-and-refinement
full_loop_count: 6
minimum_full_loops: 5
review_scope:
  - approved replan Decisions 1 through 6
  - active GitHub + Notion project entry/routing canon
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

```text
OMW-PLAN-20260820-WORLD-ROLE-01
OMW-PLAN-20260820-MAPRUN-WORLD-01
OMW-PLAN-20260820-PRESSURE-LANGUAGE-01
OMW-PLAN-20260820-MOBILIZATION-REGISTRY-01
OMW-PLAN-20260820-FIRST5-FTUE-01
OMW-PLAN-20260820-RUN-COMMAND-SHELL-01
```

Protected boundaries:

```text
IMAGE_GENERATION = PAUSED_PENDING_USER_REFERENCE_FILES
PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY
CURRENT_RUNTIME = NOT_RUN
HUMAN_PLAYER_EVIDENCE = NOT_RUN
```

Fresh work-item truth:

```text
PR175 = CLOSED_UNMERGED_HISTORICAL
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
ISSUE176 = OPEN_HISTORICAL_FOLLOWUP_REQUIRES_RECONCILIATION
PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY
```

## 2. Full loop 1 · next-gate / fresh-state attack

```yaml
loop_index: 1
input_state_or_head: 5ed18714b2cf9bd0c07670519cb5f50973d00c79
full_scope_findings:
  - CURRENT_CONFIRMED_DECISIONS still routed to already-completed Visual Requirement Inventory
  - active current-state docs no longer matched fresh PR175/177 truth
validated_findings:
  - MUST_FIX: stale next gate
  - MUST_FIX: historical PR state exposed as current
changes:
  - visual A direction retained but generation paused; first candidate REJECTED_NOT_CANON
  - planning routed to non-image work/world-story
better_alternative:
  - preserve historical evidence with explicit labels rather than delete it
clean_exit_candidate: false
```

## 3. Full loop 2 · primary active-entry attack

```yaml
loop_index: 2
full_scope_findings:
  - README / AGENTS / GDD / PROJECT_CORE / CURRENT_IMPLEMENTATION_STATUS / DECISIONS_PENDING still exposed old 10/10, Phase C, PR175 OPEN state
  - old signal11 diagnosis was presented as current blocker despite current runtime NOT_RUN
validated_findings:
  - MUST_FIX / CONFLICT: active entrypoint state drift
  - MUST_FIX / EVIDENCE_CEILING: historical runtime state promoted to current
changes:
  - refreshed six primary active documents
  - current runtime reset to NOT_RUN / blocker UNVERIFIED until fresh execution
better_alternative:
  - thin current summaries + historical owner links instead of copying old execution packets forward
clean_exit_candidate: false
```

## 4. Full loop 3 · mechanic / FTUE / UX re-attack

```yaml
loop_index: 3
full_scope_findings:
  - potential wheel↔lane 1:1 confusion
  - plausible Stage 1 overload from six mandatory T1 buildings
  - world conflict/Omen Cycle cause/Stage20 meaning still absent
validated_findings:
  - REJECTED_CRITIQUE: do not change wheel grammar; current Decision already forbids fixed mapping
  - DEFER/REVISIT: do not reduce Stage1 buildings without human evidence; keep three-group progressive disclosure
  - USER_DECISION_REQUIRED: world/story gap is real
changes:
  - protected THREE_REELS_TO_THREE_LANES_FIXED_MAPPING = FORBIDDEN
  - exposed world/story gap in current owners
better_alternative:
  - no evidence-supported alternative justified reopening Decisions 1~6
clean_exit_candidate: false
```

## 5. Full loop 4 · broader routing / evidence / workstream attack

```yaml
loop_index: 4
full_scope_findings:
  - DOCUMENTATION_MAP and DOCUMENT_LIFECYCLE_REGISTRY still routed to v4.5 / Phase C / PR175
  - Google Sheet was described by old process lineage as current human source
validated_findings:
  - MUST_FIX: router/lifecycle omissions and conflicts
  - NO_CHANGE: PR197 remains read-only
  - NO_CHANGE: old signal11/GUT/FV evidence remains history, not deletion target
changes:
  - refreshed DOCUMENTATION_MAP and DOCUMENT_LIFECYCLE_REGISTRY
  - current human-facing authority routed to Notion; structured/runtime authority to GitHub
better_alternative:
  - lifecycle labels CURRENT/EVIDENCE/PAUSED/COMPATIBILITY are safer than mass deletion
clean_exit_candidate: false
```

## 6. Full loop 5 · remaining active-router attack

```yaml
loop_index: 5
full_scope_findings:
  - PROJECT_CANON_DECISION_LEDGER still treated v4.5/Phase C as current
  - OMENWARD_ROADMAP still treated PR175 as current milestone
validated_findings:
  - MUST_FIX: two active router conflicts
changes:
  - refreshed Decision Ledger
  - refreshed Roadmap
  - next product Decision = WORLD_CONFLICT_AND_CORE_STORY
better_alternative:
  - keep settled mechanics and close the missing story layer rather than churn the six approved Decisions
clean_exit_candidate: provisional
```

## 7. Full loop 6 · post-change GitHub + Notion readback

Loop 5 뒤 post-change monitor에서 Notion Project Home의 상단 핵심 흐름을 다시 공격했다.

```yaml
loop_index: 6
input_state_or_head: GitHub main 1bf4200192d89881f2dd684f96e22928cb6868ef + current Notion Project Home
full_scope_findings:
  - GitHub active routing was aligned
  - Notion Project Home top summary still said Lobby → Prepare → Battle/Tactical → Reward/Growth and omitted approved COMMIT/REVIEW Focus phases
validated_findings:
  - MUST_FIX / HUMAN_FACING_CANON_DRIFT: top-level Notion flow summary lagged Decision 6
changes:
  - Project Home summary corrected to Lobby → PREPARE → COMMIT → BATTLE/Tactical → REVIEW/Reward/Growth → next Stage
  - Project Home Repo Main SHA readback synchronized to current main
verification:
  - Notion Project Home readback after update
  - no Decision 1~6 mechanic change required
  - no runtime/human PASS synthesized
  - PR197 untouched
better_alternative:
  - keep detailed phase flow in 03 Flow Map and only a concise synchronized summary in Project Home
long_term_fit:
  - prevents human-facing workspace from drifting behind structured Decision canon
clean_exit_candidate: true
```

## 8. Finding disposition

| Finding | Class | Decision |
|---|---|---|
| stale Visual Inventory next gate | CONFLICT | MUST_FIX · fixed |
| primary current docs old Phase C/PR175 state | CONFLICT | MUST_FIX · fixed |
| old signal11 as current blocker | EVIDENCE_CEILING | MUST_FIX · fixed to NOT_RUN/UNVERIFIED |
| Documentation Map/Lifecycle stale routing | OMISSION / CONFLICT | MUST_FIX · fixed |
| Decision Ledger/Roadmap stale routing | CONFLICT | MUST_FIX · fixed |
| Notion Project Home omitted COMMIT/REVIEW | HUMAN_FACING_CANON_DRIFT | MUST_FIX · fixed in loop 6 |
| wheel ↔ lane 1:1 confusion | regression risk | already protected; no mechanic change |
| Stage1 six-building overload | usability hypothesis | DEFER / human-test revisit |
| PR197 | other workstream risk | READ_ONLY · untouched |
| PR175/177 history | legacy evidence | ALLOWED_LEGACY / do not revive |
| Issue176 | historical follow-up | DEFER until implementation reconciliation |
| world conflict/story missing | product decision gap | USER_DECISION_REQUIRED · next scope |

## 9. CLEAN_REVIEW_EXIT

```text
FULL_LOOP_COUNT = 6
MINIMUM_FULL_LOOPS_SATISFIED = TRUE
NEW_MUST_FIX_AFTER_FINAL_LOOP = 0
DECISION_1_TO_6_REGRESSION = NONE_FOUND
CURRENT_GITHUB_ROUTING_CONFLICT = NONE_FOUND_AFTER_FIXES
CURRENT_NOTION_ROUTING_CONFLICT = NONE_FOUND_AFTER_LOOP_6_FIX
CURRENT_RUNTIME_PASS_CLAIM = NONE
HUMAN_PASS_CLAIM = NONE
PR197_MUTATION = NONE
VISUAL_REJECTED_CANDIDATE_PROMOTED = FALSE
CLEAN_REVIEW_EXIT = PASS_FOR_DECISIONS_1_TO_6_AND_CURRENT_ROUTING_SCOPE
WHOLE_PROJECT_PLANNING_COMPLETE = FALSE
NEXT_PRODUCT_DECISION = WORLD_CONFLICT_AND_CORE_STORY
```

Clean exit means only the reviewed scope is clean enough to proceed. OMENWARD 전체 기획, 구현, runtime, visual, human validation 완료를 뜻하지 않는다.
