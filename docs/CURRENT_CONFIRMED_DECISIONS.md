# OMENWARD · Current Confirmed Decisions

```yaml
updated_at: 2026-08-20
status: CURRENT_DECISION_RECOVERY_INDEX
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
planning_reopened_at: 2026-08-20
current_planning_track: WORLD_STORY_CONTENT_BALANCE_TEXT_UX_VISUAL_REPLAN
adversarial_review_decisions_1_to_6: CLEAN_REVIEW_EXIT
adversarial_review_full_loop_count: 6
runtime_evidence_ceiling: NOT_CHANGED_BY_THIS_INDEX
human_play_evidence: NOT_RUN
visual_reference_files_received: true
visual_reference_status: REFERENCE_ONLY_NOT_CANON
visual_generation: PAUSED_UNTIL_VISUAL_DIRECTION_REAPPROVAL
```

이 문서는 현재 승인 Decision을 새 채팅에서 빠르게 복원하기 위한 인덱스다. 상세 규칙은 각 Decision owner가 책임지고, Notion은 사람용 전체 그림/Flow/비교표를 책임진다. code/data/scene/test/runtime evidence는 repository truth가 책임진다.

## 2026-08-20 재기획 승인 Decision

| Decision ID | 승인 핵심 | Repository owner | 상태 |
|---|---|---|---|
| `OMW-PLAN-20260820-WORLD-ROLE-01` | 플레이어는 `징조수호관(Omen Warden)`이며 룰렛은 도박이 아니라 군사적 확률/동원 장치다. | `docs/design/APPROVED_OMENWARD_WORLD_ROLE_AND_OMEN_WARD_IDENTITY_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-MAPRUN-WORLD-01` | 한 MapRun = 한 Ward Citadel + 20 Stage Omen Cycle. | `docs/design/APPROVED_OMENWARD_OMEN_CYCLE_MAPRUN_WORLD_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-PRESSURE-LANGUAGE-01` | 5 Pressure는 적 종족이 아니라 복합 가능한 Omen Signature다. | `docs/design/APPROVED_OMENWARD_PRESSURE_LANGUAGE_AND_OMEN_SIGNATURES_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-MOBILIZATION-REGISTRY-01` | 자동생산과 TokenSource는 별도 획득 경로이며 세 징조륜은 세 전선과 1:1 대응하지 않는다. | `docs/design/APPROVED_OMENWARD_MOBILIZATION_REGISTRY_AND_TRIPLE_OMEN_WHEELS_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-FIRST5-FTUE-01` | Stage 1~5 = 인과 이해 → 미래 수정 → 순간 개입 → 응용 시험 → 첫 결산. | `docs/design/APPROVED_OMENWARD_FIRST5_FTUE_MASTERY_LADDER_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-RUN-COMMAND-SHELL-01` | Run Command Screen = PREPARE → COMMIT → BATTLE → REVIEW Focus Mode. | `docs/design/APPROVED_OMENWARD_RUN_COMMAND_SCREEN_FOCUS_MODES_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-WORLD-CONFLICT-STORY-01` | Veil은 적 종족이 아닌 적대적 경계현상이며 20 Stage는 지역 수렴기다. | `docs/design/APPROVED_OMENWARD_VEIL_CONVERGENCE_FRONT_AND_CORE_STORY_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-CONTENT-BOSS-ARC-01` | 20 Stage = 4×5 authored spine; Boss 5/10/15/20 = Priority/Route/Stance/Sequential Synthesis. | `docs/design/APPROVED_OMENWARD_20_STAGE_CONTENT_AND_BOSS_ARC_2026-08-20.md` | CONFIRMED |
| `OMW-PLAN-20260820-BALANCE-BUDGET-01` | 최종 숫자보다 `SE / ME / TU + Threat Vector` normalized envelope를 먼저 사용한다. | `docs/design/APPROVED_OMENWARD_NORMALIZED_BALANCE_BUDGET_2026-08-20.md` + `docs/analysis/balance/current_normalized_balance_budget.v1.json` | CONFIRMED |
| `OMW-PLAN-20260820-TEXT-UX-STATE-01` | 각 Mode는 하나의 질문/Primary CTA를 우선하고, COMMIT은 staged plan 후 한 번의 atomic irreversible confirm을 사용한다. raw debug reason은 player UI에서 분리한다. | `docs/design/APPROVED_OMENWARD_TEXT_UX_AND_STATE_TRANSITION_2026-08-20.md` + `docs/analysis/ui/current_text_ux_state_contract.v1.json` | CONFIRMED |

## 보호되는 제품 정체성

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
- 자동생산과 TokenSource 별도 경로.
- 세 릴 ↔ 세 전선 고정 대응 금지.
- 최종 commit 이후 recall/sell/cross-lane 이동 금지.
- `Veil ≠ Pressure ≠ 단일 적 종족`.
- Boss Stage = 5/10/15/20.
- 모든 Stage final-wave Elite.
- `DANGER_STAGE_TYPE = REMOVED`.
- Final Boss 다섯 Pressure 동시 난사 금지.
- Forecast가 정답 빌드를 지시하지 않음.
- REVIEW가 prescriptive next-build를 지시하지 않음.
- 최종 제품 수치는 simulation/runtime/human evidence 전 승인하지 않음.
- player-experience PASS는 release-near Vertical Slice 사람 플레이 전까지 금지.

## Text UX current contract

```text
PREPARE = problem / change
COMMIT = staged assignment / atomic irreversible confirm
BATTLE = tactical intervention only
REVIEW = causal explanation
```

`REVIEW.RESULT / REVIEW.MAINTENANCE`는 REVIEW 내부 substate이며 다섯 번째 top-level mode가 아니다.

## Balance open reconciliation

```text
analysis baseline = base 3/20s + Vault 3/20s + foundation 250
current main observation = base 5/20s + control 4/60s + outpost 2/30s + StageDefinition default 160
ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

## Visual reference intake

사용자가 2026-08-20 제공한 6개 시안은 **예시이며 미확정**이다.

```text
USER_REFERENCE_FILES_RECEIVED = TRUE
REFERENCE_COUNT = 6
REFERENCE_STATUS = REFERENCE_ONLY_NOT_CANON
REFERENCE_OWNER = docs/design/REFERENCE_OMENWARD_USER_MOCKUP_INTAKE_2026-08-20.md
FIRST_GENERATED_CANDIDATE = REJECTED_NOT_CANON
VISUAL_DIRECTION_FINAL = NOT_SELECTED
IMAGE_GENERATION = PAUSED_UNTIL_VISUAL_DIRECTION_REAPPROVAL
```

현재 reference에서 재사용 후보로 본 것은 3전선 좌→우 공간 문법, blue/ivory/gold vs violet/crimson 진영 대비, SD 실루엣/Tier 진화, dark navy+gold UI frame이다. 3×3 grid/gacha-like reward emphasis, 높은 동시 HUD 밀도, painterly-only rendering은 current canon으로 승격하지 않는다.

## Current next Decision

```text
CURRENT_NEXT_PRODUCT_DECISION = VISUAL_REFERENCE_RECONCILIATION
AFTER_VISUAL_DIRECTION = EXACTLY_ONE_NEW_NORTH_STAR_IF_USER_APPROVES_GENERATION
AFTER_VISUAL_APPROVAL = FINAL_PLANNING_ADVERSARIAL_REVIEW
IMPLEMENTATION_START = NOT_AUTHORIZED
CURRENT_GODOT_RUNTIME = NOT_RUN
HUMAN_PLAYER_EVIDENCE = NOT_RUN
OPEN_DRAFT_PR_197 = READ_ONLY_OTHER_WORKSTREAM
```

Visual reconciliation에서 최소 3안을 비교한다.

```text
A = PIXEL_ILLUSTRATION_HYBRID
B = FULL_TACTICAL_PIXEL
C = WATERCOLOR_ILLUSTRATION_WITH_PIXEL_UI_ACCENTS
```

아직 어느 안도 확정하지 않는다.

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
3. `docs/ACTIVE_CONTEXT.md`를 읽는다.
4. Visual 작업 시 `REFERENCE_OMENWARD_USER_MOCKUP_INTAKE_2026-08-20.md`를 읽되 reference를 canon으로 오인하지 않는다.
5. 진행 중 open/draft PR은 별도 workstream으로 읽기 전용 처리한다.
6. runtime/사람 검증을 수행하지 않은 항목은 `NOT_RUN / UNVERIFIED`를 유지한다.
7. Balance 구현 전에 economy drift를 fresh main/runtime 대상으로 재대조한다.
