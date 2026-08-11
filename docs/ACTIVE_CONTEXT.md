# [현행] Active Context

```yaml
updated_at: 2026-08-11T11:21:00+09:00
project: OMENWARD / 오멘워드
current_branch: main
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
main_activation_baseline: 87339f87949c8faea0dfe1482c5d0887a04d94f4
v45_r2_closure_main_observed: 3213b12a9614c755157953aa64a1d4e1666b48ed
base_main_observed: 315c66eea9614c284b9c11c4d522141065dfa4b0
working_branch: RESOLVE_FROM_CURRENT_WORKTREE_OR_DEFAULT_BRANCH
current_decision: OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1
activation_decision: OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1
content_closure_decision: OMW-DEC-20260811-PLANNING-WHOLE-PROJECT-CONTENT-CLOSURE-V1
quality_guardrails_decision: OMW-DEC-20260811-PLANNING-QUALITY-GUARDRAILS-V1
elite_boss_cadence_decision: OMW-DEC-20260811-PLANNING-ELITE-WAVE-BOSS-CADENCE-V1
benchmark_first_decision: OMW-DEC-20260811-OPS-BENCHMARK-INDUSTRY-RESEARCH-FIRST-V1
contract_version: 4.5
work_phase: PHASE_A_GPT_CHAT_PLANNING
continuous_work: ACTIVE_WITHIN_APPROVED_CANON_SCOPE
planning_status: MAIN_CANONICAL_APPROVED_10_OF_10
planning_canon: MAIN_CANONICAL_APPROVED_10_OF_10
current_planning_pr: RESOLVE_FROM_OPEN_PLANNING_PR
current_phase_a_focus: CONTENT_DECISIONS_CLOSED_WAITING_USER_PLANNING_COMPLETE
product_code_authority: NONE
runtime_package: OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
active_runtime_branch: runtime/barracks-role-output-implementation-20260809
active_runtime_head: bde85549560fca90f7aa25fc4842bc0a3afb92e7
active_runtime_pr: 175
active_runtime_issue: 176
runtime_status: PR175_DRAFT_7_RUNTIME_GAPS_OPEN
handoff_pr: 177
handoff_disposition: REFERENCE_ONLY_DO_NOT_MERGE
phase_c_gate: BLOCK
product_mutation_this_decision: NONE
godot_persistent_mutation_this_decision: NONE
```

`current_branch/current_main/context_baseline_commit`은 consumer가 fresh default-branch truth를 다시 resolve하도록 유지하는 dynamic locator다. `main_activation_baseline`과 `v45_r2_closure_main_observed`는 각각 activation 시작점과 evidence-closure 시점의 역사 비교 SHA이며 current main resolver를 대체하지 않는다.

## 현재 작업 기준

v4.5 r2 full canon activation과 machine-evidence closure는 종료됐다. PR185는 Sheet에 잘못 MERGED로 기록됐으나 GitHub authority에서 **closed unmerged / superseded**다. 해당 실패 CI는 historical evidence로 보존한다.

```text
V45_R2_ACTIVATION_EVIDENCE_CLOSURE = MERGED
ACTIVATION_DECISION = OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1
CLOSURE_MAIN_OBSERVED = 3213b12a9614c755157953aa64a1d4e1666b48ed
CANONICAL_V45_R2_BLOB = 45cc0859fbd0b6b46d46924592169164ff133a2e
PR178 / PR179 / PR180 / PR181 / PR182 = MERGED
PR185 = CLOSED_UNMERGED_SUPERSEDED
PR175_PHASE_A_READINESS_REVIEW = COMPLETE_IMPLEMENTATION_COMPLETENESS_NO_NEW_PRODUCT_DECISION
```

PR175 Phase-A readiness와 whole-project semantic inventory 검토 결과, Issue176의 7개 gap은 구현 completeness이고, final FV/numerics는 runtime 후 evidence tuning이며, platform/save/export/store는 후속 release 단계다. 사용자가 Building T3 / Hero·Legendary / Meta·Hub의 권장 9건을 승인하여 기존 semantic open group은 닫혔다.

```text
WHOLE_PROJECT_CONTENT_DECISION_GROUPS_OPEN = 0
WHOLE_PROJECT_CONTENT_DECISIONS = CLOSED_PENDING_USER_PLANNING_COMPLETE_DECLARATION
CONTENT_CLOSURE_AUTHORITY = docs/design/APPROVED_OMENWARD_WHOLE_PROJECT_CONTENT_CLOSURE_2026-08-11.md
BENCHMARK_AND_INDUSTRY_RESEARCH_REQUIRED_BEFORE_WORK = TRUE
BENCHMARK_PROCESS_AUTHORITY = docs/process/APPROVED_OMENWARD_BENCHMARK_INDUSTRY_RESEARCH_FIRST_2026-08-11.md
```

## 2026-08-11 Quality Guardrails + Elite/Boss cadence current override

사용자는 benchmark-first 검토 뒤 Quality Guardrail 6개를 승인했고, 이어 Stage cadence를 직접 변경 승인했다. 아래 sibling Decision이 충돌하는 과거 Stage cadence보다 우선한다.

- `docs/design/APPROVED_OMENWARD_QUALITY_GUARDRAILS_2026-08-11.md`
- `docs/design/APPROVED_OMENWARD_ELITE_WAVE_AND_BOSS_CADENCE_2026-08-11.md`

```text
OMW-DEC-20260811-PLANNING-QUALITY-GUARDRAILS-V1
OMW-DEC-20260811-PLANNING-ELITE-WAVE-BOSS-CADENCE-V1
QUALITY_GUARDRAILS = APPROVED
DANGER_STAGE_TYPE = REMOVED
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
ELITE_PRESENCE_REQUIRED = TRUE
BOSS_STAGES = 5 / 10 / 15 / 20
BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED = TRUE
LEGACY_DANGER_STAGES_4_9_14_19 = SUPERSEDED_FOR_CURRENT_CADENCE
ELITE_EXACT_COUNT = POST_RUNTIME_EVIDENCE_TUNING
ELITE_EXACT_NUMERICS = POST_RUNTIME_EVIDENCE_TUNING
```

과거 `APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`의 세부 pressure/Route 아이디어는 historical authored lineage로 보존할 수 있으나 `Danger Stage = 4/9/14/19`는 current implementation input이 아니다. 다섯 pressure taxonomy는 유지한다.

Quality Guardrail 핵심:

```text
RNG_CAN_REMOVE_ALL_VALID_RESPONSES = FORBIDDEN
FORECASTED_PRESSURE_MULTIPLE_RESPONSE_AXES_REQUIRED = TRUE
SOFT_SYNERGY_DISCOVERY = PREFERRED
POST_STAGE_CAUSAL_REVIEW = FORECAST -> KEY_EVENTS -> PLAYER_RESPONSE_OUTCOME
HORIZONTAL_CHALLENGE_EXPANSION = ALLOWED
ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE
GAMBLING_FANTASY_POSITIONING = FORBIDDEN
```

## v4.5 단계 Gate

```text
PHASE_A_GPT_CHAT_PLANNING
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION = NOT_RECEIVED
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED
PHASE_B_FINAL_PLANNING_REVIEW = NOT_RUN
PHASE_B_FINAL_PLANNING_REVIEW_NOT_RUN
PHASE_C_BLOCKED
```

사용자의 `[연속작업 진행해]`, 개별 제품 승인, 이번 Quality/Cadence 승인 모두 Phase A 제품 Decision 승인이다. 별도 literal `기획 완료` 선언이 아니다.

따라서 현재 금지:

```text
PERSISTENT_POWERSHELL_CODEX_BUILD
PERSISTENT_HIGODOT_GODOT_AUTHORING
ISSUE176_RUNTIME_GAP_IMPLEMENTATION
PR175_MERGE
PR177_MERGE
```

## 작업 전 benchmark-first Gate

모든 비사소 작업은 다음 순서를 먼저 따른다.

```text
FRESH_BASE_PROJECT_SHEET_READ
→ TARGETED_BENCHMARK_AND_INDUSTRY_RESEARCH
→ ADOPT / ADAPT / AVOID / TEST / IGNORE
→ PROJECT_CANON_CONFLICT_CHECK
→ WORK
```

현재 장르 분류:

```text
PRIMARY_GENRE = ROGUELITE_STRATEGY_AUTO_BATTLER
MECHANICAL_SUBGENRE = ROULETTE_PROBABILITY_BUILDER
MARKETING_SHORT = 룰렛을 설계해 군대를 만드는 로그라이트 전략 오토배틀러
```

## 현행 병영 TokenSource

```text
SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT
SPECIAL_T1_SELECTED_UNIT_PERSISTENCE = FIXED_WHILE_BUILDING_REMAINS_T1
SPECIAL_T1_AUTO_PRODUCTION = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_AUTO_PRODUCTION_AND_TOKEN_SOURCE = SAME_SELECTED_UNIT_SEPARATE_ACQUISITION_PATHS
SPECIAL_T1_SAVE_RELOAD_RESELECT = FORBIDDEN
SPECIAL_T1_FREE_REROLL = FORBIDDEN
```

기존 `SPECIAL_T1_TOKEN_SOURCE = NONE`은 history/superseded evidence이며 current implementation input이 아니다.

## Tool version note

```text
USER_REPORTED_GODOT_AI_CURRENT_VERSION = 3.1.4
GODOT_AI_3_1_4_HOST_VERIFICATION = NOT_RUN
GODOT_AI_3_1_4_CANON_AUTHORITY_RECONCILIATION = DEFER_TO_PHASE_C_FRESH_VERIFY
```

2026-08-11 사용자가 Godot AI가 3.1.4로 업데이트됐다고 직접 알렸다. 이 사용자 사실은 현재 작업 컨텍스트에 기록하되, 이번 Phase A 제품 Decision이 tool-authority Decision을 자동 변경하거나 Phase C 실행 권한을 부여하지 않는다.

## PR #175 현재 의미

```text
PR175 = OPEN_DRAFT
HEAD_OBSERVED = bde85549560fca90f7aa25fc4842bc0a3afb92e7
HISTORICAL_EXACT_HEAD_ACTIONS = 11_SUCCESS_0_FAILURE
STRICT_UP_TO_DATE_AGAINST_CURRENT_MAIN = NOT_REVALIDATED_DUE_PHASE_C_BLOCK
ISSUE176_GAPS = 7
ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS
MERGE = FORBIDDEN
```

7개 gap:

1. Priest 5s +8% attack-speed encouragement + start/end/support uptime/timing regression.
2. Support-role units가 prior deterministic fallback을 전부 가로채지 않도록 보존.
3. `flying`은 priority이며 universal permission boundary가 아님.
4. `cluster` density tie는 lane order/unit-id semantics 사용.
5. Giant `FRONTLINE_SURVIVAL_TIME` + `STRUCTURE_DAMAGE` collector.
6. Registered deterministic FV-PRIEST/MAGE/FLIER/GIANT/COMMON fixtures.
7. multi-cast를 포함한 true per-cast `TARGETS_HIT_PER_CAST`.

현재 승인 문서와 Issue176 기준으로 이 7개는 구현 completeness gap으로 추적한다. 이 문장은 Phase C 실행 권한을 부여하지 않는다.

## PR #177

PR177은 `REFERENCE_ONLY_HANDOFF / DO_NOT_MERGE_NOW`다. `HANDOFF_CONTEXT`는 역사 snapshot이고, current truth는 fresh repository/Sheet + 이 Active Context + v2 machine state가 소유한다.

## 다음 Gate

```text
WHOLE_PROJECT_CONTENT_DECISIONS_CLOSED
NEXT_USER_GATE = USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION
PHASE_B_FINAL_PLANNING_REVIEW = NOT_RUN
PHASE_C_BLOCKED
```

사용자가 명시적으로 `기획 완료`를 선언하기 전에는 Phase B로 전환하지 않으며, Phase C는 계속 차단된다.
