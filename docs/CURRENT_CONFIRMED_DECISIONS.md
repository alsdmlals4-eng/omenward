# OMENWARD · Current Confirmed Decisions

```yaml
updated_at: 2026-08-20
status: CURRENT_DECISION_RECOVERY_INDEX
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
planning_reopened_at: 2026-08-20
current_planning_track: WORLD_STORY_CONTENT_BALANCE_TEXT_UX_REPLAN
adversarial_review_decisions_1_to_6: CLEAN_REVIEW_EXIT
adversarial_review_owner: docs/reviews/ADVERSARIAL_REPLAN_DECISIONS_1_TO_6_AND_CANON_RECONCILIATION_2026-08-20.md
runtime_evidence_ceiling: NOT_CHANGED_BY_THIS_INDEX
human_play_evidence: NOT_RUN
visual_generation: PAUSED_PENDING_USER_REFERENCE_FILES
```

이 문서는 현재 승인 Decision을 새 채팅에서 빠르게 복원하기 위한 인덱스다. 상세 규칙은 각 Decision owner가 책임지며, Notion은 사람이 읽는 전체 그림·Flow·비교표를 책임진다. 구현·runtime truth는 repository code/data/scene/test/evidence가 책임진다.

## 2026-08-20 재기획 현재 Decision

| Decision ID | 승인 핵심 | Repository structured owner | Notion human-facing owner | 상태 |
|---|---|---|---|---|
| `OMW-PLAN-20260820-WORLD-ROLE-01` | 플레이어는 세 전선을 지키는 `징조수호관(Omen Warden)`이며 룰렛은 도박이 아니라 군사적 확률/동원 장치다. | `docs/design/APPROVED_OMENWARD_WORLD_ROLE_AND_OMEN_WARD_IDENTITY_2026-08-20.md` | Project Home · 세계관/플레이어 역할 | CONFIRMED |
| `OMW-PLAN-20260820-MAPRUN-WORLD-01` | 한 MapRun은 하나의 수호성이 버티는 20 Stage `Omen Cycle`; 세계에는 여러 수호성이 존재한다. | `docs/design/APPROVED_OMENWARD_OMEN_CYCLE_MAPRUN_WORLD_2026-08-20.md` | Project Home + `08 · 핵심 시스템 · 상세` | CONFIRMED |
| `OMW-PLAN-20260820-PRESSURE-LANGUAGE-01` | 5 Pressure는 적 종족이 아니라 복합 가능한 `Omen Signature`; 세 전선도 특정 Pressure 전용이 아니다. | `docs/design/APPROVED_OMENWARD_PRESSURE_LANGUAGE_AND_OMEN_SIGNATURES_2026-08-20.md` | Project Home + `다섯 압력 모델` + `08` | CONFIRMED |
| `OMW-PLAN-20260820-MOBILIZATION-REGISTRY-01` | 자동생산은 직접 훈련, TokenSource는 동원 인장 등록. 세 징조륜은 세 전선과 1:1 대응하지 않는다. | `docs/design/APPROVED_OMENWARD_MOBILIZATION_REGISTRY_AND_TRIPLE_OMEN_WHEELS_2026-08-20.md` | Project Home + `자동생산 ≠ TokenSource` + `세 원형 릴` + `08` | CONFIRMED |
| `OMW-PLAN-20260820-FIRST5-FTUE-01` | Stage 1~5를 `인과 이해 → 미래 수정 → 순간 개입 → 응용 시험 → 첫 결산`의 숙련 사다리로 운영한다. | `docs/design/APPROVED_OMENWARD_FIRST5_FTUE_MASTERY_LADDER_2026-08-20.md` + `docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md` | Project Home + `03 · UI · 게임플레이 Flow Map` + `08` | CONFIRMED |
| `OMW-PLAN-20260820-RUN-COMMAND-SHELL-01` | 하나의 Run Command Screen에서 `PREPARE → COMMIT → BATTLE → REVIEW` Focus Mode를 사용하고 debug/raw 정보는 player HUD에서 분리한다. | `docs/design/APPROVED_OMENWARD_RUN_COMMAND_SCREEN_FOCUS_MODES_2026-08-20.md` | Project Home + `03 · UI · 게임플레이 Flow Map` + `08` | CONFIRMED |

## Adversarial review result

2026-08-20 Decision 1~6과 현행 routing을 Base `running-adversarial-review-and-refinement` 규칙으로 5회의 full-scope loop로 다시 공격했다.

```text
FULL_LOOP_COUNT = 5
DECISION_1_TO_6_REGRESSION = NONE_FOUND
CURRENT_ROUTING_CONFLICT = NONE_FOUND_AFTER_FIXES
CURRENT_RUNTIME_PASS_CLAIM = NONE
HUMAN_PASS_CLAIM = NONE
PR197_MUTATION = NONE
CLEAN_REVIEW_EXIT = PASS_FOR_DECISIONS_1_TO_6_AND_CURRENT_ROUTING_SCOPE
WHOLE_PROJECT_PLANNING_COMPLETE = FALSE
```

Review owner:
`docs/reviews/ADVERSARIAL_REPLAN_DECISIONS_1_TO_6_AND_CANON_RECONCILIATION_2026-08-20.md`

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
- Forecast는 대응 가능한 정보를 주되 정답 카운터를 직접 지시하지 않음
- 자동생산과 TokenSource는 별도 획득 경로
- 세 릴 ↔ 세 전선 고정 대응 금지
- Stage 5/10/15/20 Boss cadence
- every-stage final-wave Elite
- Stage 1 필수 T1 6종은 현재 유지; 실제 FTUE 과부하 관측 시 축소안을 재검토
- player-experience PASS는 release-near Vertical Slice 사람 플레이 전까지 금지

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
CURRENT_REVIEW = COMPLETE_CLEAN_FOR_DECISION_1_TO_6_AND_ROUTING
CURRENT_NEXT_PRODUCT_DECISION = WORLD_CONFLICT_AND_CORE_STORY
AFTER_WORLD_STORY = 20_STAGE_CONTENT_AND_BOSS_STRUCTURE
AFTER_CONTENT = BALANCE_BUDGET
AFTER_BALANCE = TEXT_UX_AND_STATE_TRANSITION_SPEC
IMPLEMENTATION_START = NOT_AUTHORIZED
CURRENT_GODOT_RUNTIME = NOT_RUN
OPEN_DRAFT_PR_197 = READ_ONLY_OTHER_WORKSTREAM
```

World/story 미확정:

```text
CAUSE_OF_OMEN_CYCLE
HIGH_LEVEL_ENEMY_OR_VEIL_IDENTITY
STAGE_20_NARRATIVE_RESOLUTION
INTER_RUN_WORLD_PROGRESS_MEANING
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
7. historical Phase B/C0/PR175 문자열은 current state로 해석하지 않는다.
