# OMENWARD · Current Confirmed Decisions

```yaml
updated_at: 2026-08-20
status: CURRENT_DECISION_RECOVERY_INDEX
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
planning_reopened_at: 2026-08-20
current_planning_track: WORLD_STORY_CONTENT_BALANCE_TEXT_UX_REPLAN
adversarial_review_decisions_1_to_6: CLEAN_REVIEW_EXIT
adversarial_review_full_loop_count: 6
adversarial_review_owner: docs/reviews/ADVERSARIAL_REPLAN_DECISIONS_1_TO_6_AND_CANON_RECONCILIATION_2026-08-20.md
runtime_evidence_ceiling: NOT_CHANGED_BY_THIS_INDEX
human_play_evidence: NOT_RUN
visual_generation: PAUSED_PENDING_USER_REFERENCE_FILES
```

이 문서는 현재 승인 Decision을 새 채팅에서 빠르게 복원하기 위한 인덱스다. 상세 규칙은 각 Decision owner가 책임지며, Notion은 사람이 읽는 전체 그림·Flow·비교표를 책임진다. 구현·runtime truth는 repository code/data/scene/test/evidence가 책임진다.

## 2026-08-20 재기획 현재 Decision

| Decision ID | 승인 핵심 | Repository structured owner | Notion human-facing owner | 상태 |
|---|---|---|---|---|
| `OMW-PLAN-20260820-WORLD-ROLE-01` | 플레이어는 `징조수호관(Omen Warden)`이며 룰렛은 도박이 아니라 군사적 확률/동원 장치다. | `docs/design/APPROVED_OMENWARD_WORLD_ROLE_AND_OMEN_WARD_IDENTITY_2026-08-20.md` | Project Home | CONFIRMED |
| `OMW-PLAN-20260820-MAPRUN-WORLD-01` | 한 MapRun은 하나의 수호성이 버티는 20 Stage `Omen Cycle`; 세계에는 여러 수호성이 존재한다. | `docs/design/APPROVED_OMENWARD_OMEN_CYCLE_MAPRUN_WORLD_2026-08-20.md` | Project Home + `08` | CONFIRMED |
| `OMW-PLAN-20260820-PRESSURE-LANGUAGE-01` | 5 Pressure는 적 종족이 아니라 복합 가능한 `Omen Signature`; 세 전선도 특정 Pressure 전용이 아니다. | `docs/design/APPROVED_OMENWARD_PRESSURE_LANGUAGE_AND_OMEN_SIGNATURES_2026-08-20.md` | Project Home + `다섯 압력 모델` + `08` | CONFIRMED |
| `OMW-PLAN-20260820-MOBILIZATION-REGISTRY-01` | 자동생산은 직접 훈련, TokenSource는 동원 인장 등록. 세 징조륜은 세 전선과 1:1 대응하지 않는다. | `docs/design/APPROVED_OMENWARD_MOBILIZATION_REGISTRY_AND_TRIPLE_OMEN_WHEELS_2026-08-20.md` | Project Home + `자동생산 ≠ TokenSource` + `세 원형 릴` + `08` | CONFIRMED |
| `OMW-PLAN-20260820-FIRST5-FTUE-01` | Stage 1~5를 `인과 이해 → 미래 수정 → 순간 개입 → 응용 시험 → 첫 결산`의 숙련 사다리로 운영한다. | `docs/design/APPROVED_OMENWARD_FIRST5_FTUE_MASTERY_LADDER_2026-08-20.md` + `docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md` | Project Home + `03` + `08` | CONFIRMED |
| `OMW-PLAN-20260820-RUN-COMMAND-SHELL-01` | 하나의 Run Command Screen에서 `PREPARE → COMMIT → BATTLE → REVIEW` Focus Mode를 사용한다. | `docs/design/APPROVED_OMENWARD_RUN_COMMAND_SCREEN_FOCUS_MODES_2026-08-20.md` | Project Home + `03` + `08` | CONFIRMED |
| `OMW-PLAN-20260820-WORLD-CONFLICT-STORY-01` | `Veil`은 적 종족이 아니라 적대적 경계현상. 20 Stage는 Veil 수렴기이며 Stage 20 승리는 해당 수호성의 수렴을 끝낸 실제 전쟁 기록이다. | `docs/design/APPROVED_OMENWARD_VEIL_CONVERGENCE_FRONT_AND_CORE_STORY_2026-08-20.md` | Project Home + `09 · 세계관 · 핵심 스토리` | CONFIRMED |
| `OMW-PLAN-20260820-CONTENT-BOSS-ARC-01` | 20 Stage를 `징조 문해 → 복합 징조 → 대가와 선택 → 대수렴`의 4×5 authored spine으로 운영한다. Boss 5/10/15/20은 Priority/Route/Stance/Sequential Synthesis를 시험한다. Danger Stage는 없고 옛 4/9/14/19 아이디어는 공개 일반 Stage variation으로만 재사용한다. | `docs/design/APPROVED_OMENWARD_20_STAGE_CONTENT_AND_BOSS_ARC_2026-08-20.md` | Project Home + `10 · 20 Stage · Boss 구조` | CONFIRMED |
| `OMW-PLAN-20260820-BALANCE-BUDGET-01` | 최종 숫자보다 `SE / ME / TU + Threat Vector`의 정규화된 예산을 먼저 승인한다. 기존 Foundation 250, Spin 20, 첫 T2 약 50, Stage 1~5 TU, 10k robustness는 calibration anchor이며 current runtime과의 economy drift는 구현 전 reconciliation 필수다. | `docs/design/APPROVED_OMENWARD_NORMALIZED_BALANCE_BUDGET_2026-08-20.md` + `docs/analysis/balance/current_normalized_balance_budget.v1.json` | Project Home + `11 · Balance Budget` | CONFIRMED |

## Adversarial review result

Decision 1~6 및 당시 현행 GitHub/Notion routing은 Base `running-adversarial-review-and-refinement` 규칙으로 6회의 full-scope loop를 완료했다.

```text
FULL_LOOP_COUNT = 6
MINIMUM_FULL_LOOPS_SATISFIED = TRUE
DECISION_1_TO_6_REGRESSION = NONE_FOUND
CURRENT_GITHUB_ROUTING_CONFLICT = NONE_FOUND_AFTER_FIXES
CURRENT_NOTION_ROUTING_CONFLICT = NONE_FOUND_AFTER_LOOP_6_FIX
CLEAN_REVIEW_EXIT = PASS_FOR_REVIEWED_SCOPE
WHOLE_PROJECT_PLANNING_COMPLETE = FALSE
```

## 보호되는 상위 정체성

```text
건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.

징조 관측
→ 건설 / 동원 인장 / 확률 설계
→ 병력 획득
→ 세 전선 중 하나에 비가역 커밋
→ 자동전투 + 제한된 수동 전술
→ 인과 복기
→ 다음 설계
```

보호:

- `ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE`
- `GAMBLING_FANTASY_POSITIONING = FORBIDDEN`
- `PAID_SPIN = FORBIDDEN`
- 세 전선 비가역 커밋
- 자동생산과 TokenSource 별도 획득 경로
- 세 릴 ↔ 세 전선 고정 대응 금지
- `Veil ≠ Pressure ≠ 단일 적 종족`
- Stage 5/10/15/20 Boss cadence
- every-stage final-wave Elite
- `DANGER_STAGE_TYPE = REMOVED`
- Final Boss 다섯 Pressure 동시 난사 금지; 순차 Pattern 사용
- Forecast는 대응 가능한 정보를 주되 정답 카운터를 직접 지시하지 않음
- Balance complexity와 Raw TU를 동시에 무제한 증폭하지 않음
- 최종 제품 수치는 simulation/runtime/human evidence 전 승인하지 않음
- 시간 루프는 기본 Run 반복 설명으로 사용하지 않음
- player-experience PASS는 release-near Vertical Slice 사람 플레이 전까지 금지

## Current content spine

```text
Stage 1~5   = PRESSURE LITERACY
Stage 6~10  = COMBINATION
Stage 11~15 = OPPORTUNITY COST
Stage 16~20 = SYNTHESIS

Boss 5  = PRIORITY
Boss 10 = ROUTE
Boss 15 = STANCE
Boss 20 = SEQUENTIAL_SYNTHESIS
```

Vertical Slice는 안정적인 authored spine을 우선하며, 장기 반복성은 Stage 역할을 보존한 bounded variation으로 확장한다.

## Current normalized Balance envelope

```text
SE = current 20 Gold Spin anchor
ME = current 50 Gold first-T2-class anchor = 2.5 SE
TU = simulation-only relative threat unit
THREAT_VECTOR = Raw TU + Lanes + Signatures + Route + Overlap + Elite/Boss complexity
```

Search envelope:

```text
Act I   = 1.00 reference
Act II  = 1.15~1.35
Act III = 1.40~1.65
Act IV  = 1.70~2.05

Wave 1 = 20~30%
Wave 2 = 25~35%
Final  = 40~50% including Elite
Boss raw TU search = same-Act normal median × 1.25~1.45, reducible for mechanic complexity
```

Current economy drift requiring implementation reconciliation:

```text
analysis baseline = base 3/20s + Vault 3/20s + foundation 250
current main observation = base 5/20s + control 4/60s + outpost 2/30s + StageDefinition default 160
ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION
```

## Visual status

```text
VISUAL_REQUIREMENT_INVENTORY = COMPLETE_PROPOSED
VISUAL_NORTH_STAR_DIRECTION_A = APPROVED_DIRECTION_ONLY
FIRST_GENERATED_CANDIDATE = REJECTED_NOT_CANON
VISUAL_GENERATION = PAUSED_PENDING_USER_REFERENCE_FILES
```

사용자 보유 시안/레퍼런스 파일을 받기 전에는 이미지 생성·수정을 재개하지 않는다.

## Current pending Decision class

```text
WORLD_CONFLICT_AND_CORE_STORY = CONFIRMED
20_STAGE_CONTENT_AND_BOSS_STRUCTURE = CONFIRMED
BALANCE_BUDGET = CONFIRMED
CURRENT_NEXT_PRODUCT_DECISION = TEXT_UX_AND_STATE_TRANSITION_SPEC
AFTER_TEXT_UX = VISUAL_REFERENCE_RECONCILIATION_WHEN_USER_FILES_ARRIVE
IMPLEMENTATION_START = NOT_AUTHORIZED
CURRENT_GODOT_RUNTIME = NOT_RUN
HUMAN_PLAYER_EVIDENCE = NOT_RUN
OPEN_DRAFT_PR_197 = READ_ONLY_OTHER_WORKSTREAM
```

Text UX에서 다음을 닫는다.

```text
PREPARE_COPY_AND_INFORMATION_HIERARCHY
COMMIT_CONFIRMATION_AND_IRREVERSIBILITY_COPY
BATTLE_TACTICAL_STATE_AND_BLOCK_REASONS
REVIEW_CAUSAL_SUMMARY
FTUE_STAGE1_TO_5_PROMPTS
MODE_TRANSITION_RULES
ERROR_AND_DISABLED_REASON_LANGUAGE
DEBUG_VS_PLAYER_SURFACE_BOUNDARY
```

## Current GitHub work-item truth

```text
PR175 = CLOSED_UNMERGED_HISTORICAL
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
ISSUE176 = OPEN_HISTORICAL_FOLLOWUP_REQUIRES_RECONCILIATION
PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY
```

## 재개 규칙

1. fresh `main`과 이 인덱스를 먼저 읽는다.
2. 기존 CONFIRMED Decision은 같은 질문을 다시 묻지 않는다.
3. `docs/ACTIVE_CONTEXT.md`와 current GDD/Project Core를 이어서 읽는다.
4. Notion 사람용 표현과 repository owner가 다르면 canon conflict를 먼저 복구한다.
5. 진행 중 open/draft PR은 별도 workstream으로 읽기 전용 처리한다.
6. 실제 runtime/사람 검증을 수행하지 않은 항목은 `NOT_RUN / UNVERIFIED`를 유지한다.
7. historical Phase B/C0/PR175 및 구형 Danger Stage 문서는 current state로 해석하지 않는다.
8. Balance 구현 전에 economy drift를 fresh main/runtime 대상으로 다시 대조한다.
