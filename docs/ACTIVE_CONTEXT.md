# [현행] Active Context

```yaml
updated_at: 2026-08-11T06:14:00+09:00
project: OMENWARD / 오멘워드
main_activation_baseline: 87339f87949c8faea0dfe1482c5d0887a04d94f4
base_main_observed: 315c66eea9614c284b9c11c4d522141065dfa4b0
current_decision: OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1
contract_version: 4.5
work_phase: PHASE_A_GPT_CHAT_PLANNING
continuous_work: ACTIVE_WITHIN_APPROVED_CANON_SCOPE
planning_canon: MAIN_CANONICAL_APPROVED_10_OF_10
current_planning_pr: 178
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

## 현재 작업 기준

이 context의 우선 작업은 제품 runtime 구현이 아니라 **정본 최신성 복구와 v4.5 Thin Adapter 활성화**다.

사용자 승인 Decision:

`OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1`

현재 실행 순서:

```text
fresh Base / OMENWARD / Sheet
→ TDD RED
→ current canon propagation repair
→ same Decision Sheet proposed sync + bounded reread
→ exact-head CI
→ adversarial review
→ eligible planning merge
→ merged-main + Sheet MERGED_CANON readback
```

## v4.5 단계 Gate

```text
PHASE_A_GPT_CHAT_PLANNING
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED
PHASE_B_FINAL_PLANNING_REVIEW_NOT_RUN
PHASE_C_BLOCKED
```

사용자의 `[연속작업 진행해]`는 현재 승인된 canon/planning scope를 연속 수행하라는 뜻이다. 이것은 `기획 완료` 선언이 아니다.

따라서 현재 금지:

```text
PERSISTENT_POWERSHELL_CODEX_BUILD
PERSISTENT_HIGODOT_GODOT_AUTHORING
ISSUE176_RUNTIME_GAP_IMPLEMENTATION
PR175_MERGE
PR177_MERGE
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

## PR #175 현재 의미

```text
PR175 = OPEN_DRAFT
HEAD_OBSERVED = bde85549560fca90f7aa25fc4842bc0a3afb92e7
HISTORICAL_EXACT_HEAD_ACTIONS = 11_SUCCESS_0_FAILURE
ISSUE176_GAPS = 7
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

이 planning/canon PR이 `main`을 전진시키면 기존 11/11을 새 base의 strict up-to-date Green으로 부르지 않는다.

## PR #177

PR177은 `REFERENCE_ONLY_HANDOFF / DO_NOT_MERGE_NOW`다. `HANDOFF_CONTEXT`는 역사 snapshot이고, current truth는 fresh repository/Sheet + 이 Active Context + v2 machine state가 소유한다.

## 다음 Gate

현재 planning/canon Decision의 종료 Gate:

```text
SHEET_SAME_DECISION_SYNC_AND_REREAD
EXACT_HEAD_GREEN
ADVERSARIAL_P0_P1_0
UNRESOLVED_THREADS_0
BASE_AND_PROJECT_RACE_RECHECK
MERGED_MAIN_READBACK
```

그 이후에도 Phase C는 열리지 않는다. 다음 단계 전환은 사용자의 명시적 `기획 완료` 선언부터 시작한다.
