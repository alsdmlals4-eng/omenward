# [현행] 오멘워드 로드맵

```yaml
updated_at: 2026-08-20
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
planning_status: REOPENED_REVIEW_IN_PROGRESS
current_next_gate: VISUAL_REFERENCE_RECONCILIATION
implementation_authorized: false
visual_reference_files_received: true
visual_reference_status: REFERENCE_ONLY_NOT_CANON
visual_generation: PAUSED_UNTIL_VISUAL_DIRECTION_REAPPROVAL
```

## Current milestone

```text
PROJECT_STATE_RECOVERED
→ DECISION_1_TO_6_CONFIRMED
→ 6_FULL_ADVERSARIAL_LOOPS_AND_CANON_RECONCILIATION
→ WORLD_CONFLICT_AND_CORE_STORY_CONFIRMED
→ 20_STAGE_CONTENT_AND_BOSS_STRUCTURE_CONFIRMED
→ NORMALIZED_BALANCE_BUDGET_CONFIRMED
→ TEXT_UX_AND_STATE_TRANSITION_CONFIRMED
→ USER_VISUAL_REFERENCES_RECEIVED_REFERENCE_ONLY
→ VISUAL_REFERENCE_RECONCILIATION = CURRENT_NEXT
```

## Current planning order

### P0 — Visual reference reconciliation — CURRENT NEXT

사용자가 제공한 6개 시안은 예시이며 아직 확정이 아니다. 최종 스타일로 승격하지 않고 최소 3개의 실질 대안을 비교한다.

```text
A = PIXEL_ILLUSTRATION_HYBRID
B = FULL_TACTICAL_PIXEL
C = WATERCOLOR_ILLUSTRATION_WITH_PIXEL_UI_ACCENTS
```

평가축:

```text
AI-look reduction
pixel/dot identity strength
3-lane battlefield readability
small-unit silhouette readability
world/core-system fit
UI density at 960x540 internal target
reusable layer/asset production feasibility
long-term faction/biome expansion
```

User reference owner:
`docs/design/REFERENCE_OMENWARD_USER_MOCKUP_INTAKE_2026-08-20.md`

이미지 생성은 이 방향 Decision 승인 전 재개하지 않는다.

### Visual North Star — AFTER DIRECTION APPROVAL

승인된 방향으로 **정확히 1장**만 생성한다.

우선 후보는 기존 A-direction lineage인 `Stage 2 PREPARE · Omen Wheels Focus`를 유지하되, 새 reference reconciliation 결과에 따라 rendering/UI composition을 수정한다.

생성 결과는 자동 정본이 아니다. 사용자 결과 승인이 있어야 Notion 승인 visual reference로 승격한다.

### Final planning review

Visual direction/result reconciliation 후:

```text
minimum 5 full adversarial loops / until clean
Decision 1~10 + Visual contract regression review
Notion/GitHub sync
implementation Definition of Ready
explicit user implementation authority
```

Only then open implementation handoff.

## Current Text UX authority

Owners:

- `docs/design/APPROVED_OMENWARD_TEXT_UX_AND_STATE_TRANSITION_2026-08-20.md`
- `docs/analysis/ui/current_text_ux_state_contract.v1.json`

```text
PREPARE = problem/change
COMMIT = staged assignment + atomic irreversible confirm
BATTLE = tactical timing
REVIEW = causal explanation
```

`REVIEW.RESULT / REVIEW.MAINTENANCE`는 REVIEW substate다.

Player UI는 raw internal reason/code를 숨기고 `무엇이 부족한지 / 무엇이 준비되지 않았는지 / 어떤 조건이 맞지 않는지 / 무엇이 비가역인지`를 직접 설명한다.

## Current normalized Balance authority

Owners:

- `docs/design/APPROVED_OMENWARD_NORMALIZED_BALANCE_BUDGET_2026-08-20.md`
- `docs/analysis/balance/current_normalized_balance_budget.v1.json`

```text
SE = current 20 Gold Spin anchor
ME = current 50 Gold first-T2-class anchor = 2.5 SE
TU = simulation-only relative threat unit
```

Economy drift remains intentionally unresolved until implementation reconciliation.

## Current world / content authority

```text
PLAYER_ROLE = Omen Warden
VEIL = hostile boundary phenomenon, not one enemy race
ONE_MAPRUN = ONE_WARD_CITADEL + ONE_20_STAGE_OMEN_CYCLE
RUN_HISTORY_RESET = FALSE

Stage 1~5   = PRESSURE LITERACY
Stage 6~10  = COMBINATION
Stage 11~15 = OPPORTUNITY COST
Stage 16~20 = SYNTHESIS

Boss 5  = PRIORITY
Boss 10 = ROUTE
Boss 15 = STANCE
Boss 20 = SEQUENTIAL_SYNTHESIS

DANGER_STAGE_TYPE = REMOVED
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
```

## Current GitHub work-item routing

```text
PR175 = CLOSED_UNMERGED_HISTORICAL
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
ISSUE176 = OPEN_HISTORICAL_FOLLOWUP_REQUIRES_RECONCILIATION
PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY
```

PR197 is protected from this planning workstream.

## Current runtime/evidence gate

```text
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
STAGED_COMMIT_USABILITY = NOT_RUN
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

No historical runtime diagnosis is promoted as current without fresh execution.

## Platform / release deferred

```text
PC / Steam = PRIMARY_PLANNING_AND_VALIDATION_TARGET
Android / Google Play = COMMITTED_RELEASE_TARGET_EXECUTION_DEFERRED_RELEASE_NEAR
SHARED_SAVE_SCHEMA = NOT_STARTED
EXPORT_PRESETS = ABSENT
```
