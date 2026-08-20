# [현행] 오멘워드 현재 구현 상태

```yaml
updated_at: 2026-08-20
status: CURRENT_IMPLEMENTATION_STATUS
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
planning_status: REOPENED_REVIEW_IN_PROGRESS
implementation_authorized: false
current_runtime_status: NOT_RUN
human_player_evidence: NOT_RUN
```

## 1. Current high-level state

2026-08-20 재기획 채팅에서는 current `main`의 Godot/Windows runtime을 실행하지 않았다. 따라서 과거 signal11 진단을 현재 blocker로 재주장하지 않는다.

```text
PRODUCT_IMPLEMENTATION_COMPLETION = FALSE
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_UI_EVIDENCE = NOT_RUN
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
CURRENT_RUNTIME_BLOCKER = UNVERIFIED_UNTIL_FRESH_EXECUTION
```

## 2. Existing main foundations

Repository `main`에는 다음 계열의 foundation이 존재한다.

```text
roulette service / three-reel probability flow
battle simulator / lane + gate + base + clash state
building / economy / production foundations
stage HUD / stage select prototype UI
data / domain / presentation / wave / tactical structure
```

이 존재 사실은 기능 완성·재미·현재 runtime PASS를 뜻하지 않는다.

## 3. Current GitHub work-item truth

2026-08-20 fresh readback:

```text
PR175 = CLOSED_UNMERGED_HISTORICAL
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
ISSUE176 = OPEN_HISTORICAL_FOLLOWUP_REQUIRES_RECONCILIATION
PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY
```

### PR #175

- closed 2026-08-18
- merged = false
- 47 commits / 19 changed files의 historical runtime/evidence work
- unmerged 변경은 current `main` 제품 truth가 아니다.

### PR #177

- closed 2026-08-18
- merged = false
- historical handoff/reference only.

### Issue #176

과거 PR175 package의 7개 role-output/FV gap을 기록한다. parent PR이 closed-unmerged이고 프로젝트 기획이 다시 열렸으므로 미래 구현 때 그대로 실행하지 않는다.

Future rule:

```text
fresh current main
+ current confirmed planning Decisions
+ actual current runtime
+ current implementation scope
→ reconcile Issue176
→ keep / rewrite / close / supersede
```

### PR #197

- OPEN / DRAFT
- reusable candidate draft engine sidecar pilot
- 현재 채팅의 다른 workstream이므로 read-only.
- 수정·retarget·merge·unmerged 내용의 product-canon 승격 금지.

## 4. Historical runtime evidence

2026-08-11~12에는 PR175 exact-head / disposable archive / HiGodot 관련 signal11 진단이 기록됐다. 해당 기록은 **HISTORICAL_EVIDENCE**로 보존한다.

```text
HISTORICAL_SIGNAL11_DIAGNOSTIC = RETAINED
HISTORICAL_HIGODOT_C0_EVIDENCE = RETAINED
HISTORICAL_GUT_AND_FV_EVIDENCE = RETAINED
CURRENT_CRASH_REPRODUCTION = NOT_RUN
```

과거 원인 가설이나 A/B autoload isolation 계획은 새 current-main 실행 없이 current next step으로 사용하지 않는다.

## 5. Current planning/implementation boundary

현재는 GPT-first planning 단계다.

```text
CURRENT_CONFIRMED_REPLAN_DECISIONS = 6
ADVERSARIAL_REVIEW_AND_CANON_RECONCILIATION = IN_PROGRESS
WORLD_STORY_CORE = NEXT_PRODUCT_DECISION
20_STAGE_CONTENT_AND_BOSS_STRUCTURE = AFTER_WORLD_STORY
BALANCE_BUDGET = AFTER_CONTENT_STRUCTURE
TEXT_UX_SPEC = AFTER_BALANCE_BUDGET
VISUAL_WORK = PAUSED_PENDING_USER_REFERENCE_FILES
IMPLEMENTATION_START = NOT_AUTHORIZED
```

## 6. Durable product/evidence boundaries

```text
FINAL_FUNCTIONAL_VALUE = POST_RUNTIME_EVIDENCE_TUNING
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
SPECIAL_T1_SELECTION_DISTRIBUTION = POST_RUNTIME_EVIDENCE_TUNING
BLOCKED_RUNTIME_OUTPUT = NEVER_SYNTHESIZE_AS_ZERO
```

기존 10,000-seed robustness 등 과거 evidence는 해당 실험 범위에서만 유효하다. 새로운 재기획 의미나 현재 runtime을 자동 PASS시키지 않는다.

## 7. Platform/release boundary

```text
PC / Steam = PRIMARY_PLANNING_AND_VALIDATION_TARGET
Android / Google Play = COMMITTED_RELEASE_TARGET_EXECUTION_DEFERRED_RELEASE_NEAR
SHARED_SAVE_SCHEMA = NOT_STARTED
EXPORT_PRESETS = ABSENT
```

## 8. Resume order for implementation work

실제 구현이 다시 열릴 때:

1. fresh Base current authority.
2. fresh OMENWARD main/open PR inventory.
3. `docs/CURRENT_CONFIRMED_DECISIONS.md`.
4. `docs/ACTIVE_CONTEXT.md`.
5. current GDD/Project Core.
6. PR197 보호 여부 재확인.
7. fresh local Godot/runtime execution.
8. 그 뒤에만 historical Issue176/PR175 evidence와 비교.

## 9. Historical compatibility markers

아래는 과거 validator/lineage를 위한 `ALLOWED_LEGACY`이며 current state가 아니다.

```text
MAIN_CANONICAL_APPROVED_10_OF_10 = HISTORICAL_2026_08_11
PHASE_B_FINAL_PLANNING_REVIEW = HISTORICAL_PASS
PHASE_C_C0_OVERALL = HISTORICAL_PASS
PR175 = OPEN_DRAFT = HISTORICAL_LABEL_ONLY
PR175_DRAFT_7_RUNTIME_GAPS_OPEN = HISTORICAL_LABEL_ONLY
PR175_CURRENT_MAIN_REVALIDATION_NEXT = HISTORICAL_LABEL_ONLY
CURRENT_BLOCKER = CANONICAL_EXACT_HEAD_PROJECT_BOOT_BOUNDARY = HISTORICAL_LABEL_ONLY
NEXT_EXECUTABLE_STEP = DISPOSABLE_AUTOLOAD_AB_ISOLATION = HISTORICAL_LABEL_ONLY
LEGACY_C1_C2_C3_PROVEN
HUMAN_QA_NOT_RUN
```
