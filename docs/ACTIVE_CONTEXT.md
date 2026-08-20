# [현행] Active Context

```yaml
updated_at: 2026-08-20
current_branch: main
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
planning_status: REOPENED_REVIEW_IN_PROGRESS
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_gdd: docs/OMENWARD_GDD_CURRENT_CANON.md
current_review: CLEAN_REVIEW_EXIT_FOR_DECISIONS_1_TO_6_AND_ROUTING
current_review_full_loop_count: 6
current_text_ux_decision: OMW-PLAN-20260820-TEXT-UX-STATE-01
current_text_ux_owner: docs/design/APPROVED_OMENWARD_TEXT_UX_AND_STATE_TRANSITION_2026-08-20.md
current_text_ux_machine_owner: docs/analysis/ui/current_text_ux_state_contract.v1.json
current_visual_reference_owner: docs/design/REFERENCE_OMENWARD_USER_MOCKUP_INTAKE_2026-08-20.md
current_next_gate: VISUAL_REFERENCE_RECONCILIATION
implementation_authorized: false
current_chat_runtime_status: NOT_RUN
human_player_evidence: NOT_RUN
visual_generation: PAUSED_UNTIL_VISUAL_DIRECTION_REAPPROVAL
```

## Current planning state

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 10
WORLD_ROLE = CONFIRMED
MAPRUN_WORLD_MEANING = CONFIRMED
PRESSURE_LANGUAGE = CONFIRMED
MOBILIZATION_REGISTRY_WORLD_MEANING = CONFIRMED
FIRST5_FTUE_MASTERY_LADDER = CONFIRMED
RUN_COMMAND_SCREEN_FOCUS_MODES = CONFIRMED
WORLD_CONFLICT_AND_CORE_STORY = CONFIRMED
20_STAGE_CONTENT_AND_BOSS_STRUCTURE = CONFIRMED
BALANCE_BUDGET = CONFIRMED
TEXT_UX_AND_STATE_TRANSITION = CONFIRMED
DECISION_1_TO_6_ADVERSARIAL_REVIEW = CLEAN_REVIEW_EXIT
USER_VISUAL_REFERENCES = RECEIVED_REFERENCE_ONLY_NOT_CANON
CURRENT_NEXT = VISUAL_REFERENCE_RECONCILIATION
IMPLEMENTATION_START = NOT_AUTHORIZED
```

## Current product promise

```text
징조 관측
→ 건설 / 동원 인장 / 미래 병력 분포 설계
→ 세 징조륜에서 병력 획득
→ 세 전선 중 하나에 비가역 커밋
→ 자동전투 + 결정적 순간의 수동 전술
→ 인과 복기
→ 다음 설계
```

Player role: `징조수호관(Omen Warden)`

Run shell: `PREPARE → COMMIT → BATTLE → REVIEW`

## Current Text UX contract

```text
PREPARE = 다가오는 문제를 보고 무엇을 바꿀 것인가?
COMMIT = 얻은 병력을 어느 전선에 확정할 것인가?
BATTLE = 지금 직접 개입해야 하는가?
REVIEW = 왜 이런 결과가 나왔는가?
```

State flow:

```text
STAGE_ENTER
→ PREPARE
→ COMMIT
→ BATTLE
→ REVIEW.RESULT
→ REVIEW.MAINTENANCE
→ NEXT PREPARE
```

Stage 20:

```text
BATTLE → REVIEW.FINAL → MAPRUN_FINAL_SETTLEMENT
```

COMMIT:

```text
PENDING_COMMIT = editable plan only
FINAL_CONFIRM = atomic irreversible deployment
POST_CONFIRM_RECALL = FORBIDDEN
POST_CONFIRM_SELL = FORBIDDEN
POST_CONFIRM_CROSS_LANE_MOVE = FORBIDDEN
```

Player UI는 raw reason code를 노출하지 않고 부족 자원/미준비 조건/대상 조건/비가역 결과를 직접 설명한다. REVIEW는 사실과 인과만 설명하고 다음 정답 빌드를 명령하지 않는다.

## Current world / content spine

```text
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

## Current normalized Balance envelope

```text
SE = current 20 Gold Spin anchor
ME = current 50 Gold first-T2-class anchor = 2.5 SE
TU = simulation-only relative threat unit
THREAT_VECTOR = Raw TU + Active Lanes + Signature Count + Route Complexity + Wave Overlap + Elite/Boss Complexity
```

```text
Act I   = 1.00 reference
Act II  = 1.15~1.35
Act III = 1.40~1.65
Act IV  = 1.70~2.05
Wave 1  = 20~30%
Wave 2  = 25~35%
Final   = 40~50% including Elite
```

Economy drift remains open:

```text
analysis = base 3/20s + Vault 3/20s + foundation 250
current main observed = base 5/20s + control 4/60s + outpost 2/30s + default starting_gold 160
ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

## Visual reference state

사용자가 제공한 6개 시안은 예시이며 아직 확정이 아니다.

```text
USER_REFERENCE_FILES_RECEIVED = TRUE
REFERENCE_COUNT = 6
REFERENCE_STATUS = REFERENCE_ONLY_NOT_CANON
FIRST_GENERATED_CANDIDATE = REJECTED_NOT_CANON
VISUAL_DIRECTION_FINAL = NOT_SELECTED
IMAGE_GENERATION = PAUSED_UNTIL_VISUAL_DIRECTION_REAPPROVAL
```

Reference에서 가치가 높은 요소:

```text
3-lane left-to-right battlefield grammar
allied ivory/blue/gold vs Veil violet/crimson contrast
2.5~3-head SD role silhouettes and tier evolution
navy/charcoal UI + restrained gold trim
```

Rework required:

```text
square 3x3/gacha-like reward emphasis -> current triple Omen Wheel military grammar에 맞게 재해석
all-panels-always-visible density -> Focus Mode hierarchy 적용
painterly-only rendering -> user-requested stronger pixel/dot direction과 재조정
style-board option 1 recommendation -> NOT_CANON
```

Visual reconciliation candidates:

```text
A = PIXEL_ILLUSTRATION_HYBRID
B = FULL_TACTICAL_PIXEL
C = WATERCOLOR_ILLUSTRATION_WITH_PIXEL_UI_ACCENTS
```

아직 선택하지 않는다.

## Runtime / work-item boundary

```text
PR175 = CLOSED_UNMERGED_HISTORICAL
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
ISSUE176 = OPEN_HISTORICAL_FOLLOWUP_REQUIRES_RECONCILIATION
PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
STAGED_COMMIT_USABILITY = NOT_RUN
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

PR197은 이 채팅에서 수정·retarget·merge하지 않는다.

## Current planning order

```text
1. Visual reference reconciliation + final visual direction decision
2. if approved, exactly one new North Star image generation
3. user review of generated result; rejected result stays non-canon
4. final full planning adversarial review
5. Notion/GitHub final sync
6. implementation handoff only after explicit user authority
```

## Resume order

1. fresh OMENWARD main.
2. `docs/CURRENT_CONFIRMED_DECISIONS.md`.
3. this `docs/ACTIVE_CONTEXT.md`.
4. Text UX + Balance + Content/Story owner docs.
5. `docs/design/REFERENCE_OMENWARD_USER_MOCKUP_INTAKE_2026-08-20.md`.
6. Project Notion Home + `02/03/08/09/10/11/12` pages.
7. open/draft PR inventory; PR197 read-only.
8. actual runtime only when execution is explicitly resumed.
