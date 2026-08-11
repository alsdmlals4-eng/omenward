# [현행 검토] OMENWARD Phase C C0 Preflight — 2026-08-11

```yaml
decision_id: OMW-DEC-20260811-OPS-PHASE-C-C0-PREFLIGHT-V1
review_status: C0_REPOSITORY_PR_GATE_PASS_PENDING_MERGE
product_mutation: NONE
runtime_resume_authority: NOT_GRANTED_BY_THIS_REVIEW_ALONE
local_live_session: UNVERIFIED_IN_THIS_ENVIRONMENT
```

## 1. Fresh authority and drift

C0 시작 시 Base, OMENWARD, Google Sheet를 fresh-read했다.

```text
BASE_MAIN_AT_ENTRY = 8e7d85b1b1272002a8086c502a41073888cb3318
BASE_CHANGE = docs: add Godot and code engineering sources (#283)
OMENWARD_MAIN_AT_ENTRY = 14b0d942e071dc6e823f48c29ac79f0978477d85
OMENWARD_MAIN_PARENT = 91f4aa98c0dea5307c2482aa0f403ce7dd115e40
DIRECT_MAIN_COMMIT = TRUE
DIRECT_MAIN_PUSH_WORKFLOW_RUNS = 0
DIRECT_MAIN_COMMIT_STATUSES = 0
```

C0 entry Sheet는 `OMENWARD=91f4aa98...`, `Base=7a49390b...`를 가리켜 GitHub current truth와 drift가 있었다. 같은 Decision ID로 current hub/work-order/current-decision/audit/history를 갱신했고 bounded reread를 통과했다.

```text
GITHUB_SHEET_DRIFT_AT_ENTRY = CONFIRMED
SHEET_PREMERGE_SYNC = COMPLETE
SHEET_PREMERGE_REREAD = PASS
```

pre-merge race 재검증에서 OMENWARD main은 `14b0d942...`, Base main은 `8e7d85b1...`로 유지됐다. Base Draft PR #284는 아직 main authority가 아니며 이 C0 변경과 충돌하지 않는다.

## 2. Current toolchain truth

### Godot

```text
GODOT_CI_RUNTIME = 4.7.1-stable
GODOT_PROJECT_FEATURE_LINE = 4.7
GODOT_4_7_1_RELEASE_DATE = 2026-07-14
```

### Godot AI / HiGodot

OMENWARD current source와 official upstream을 대조했다.

```text
PROJECT_GODOT_AI_VERSION = 3.1.4
PROJECT_GODOT_AI_PLUGIN_CFG_BLOB = fe28f1acfc69f229bc3c2ea55ac5f854924be466
UPSTREAM_GODOT_AI_LATEST_RELEASE = v3.1.4
UPSTREAM_RELEASE_PUBLISHED_AT = 2026-08-10T04:24:49Z
UPSTREAM_VERSION_BUMP_COMMIT = 96cc8b8c3d25ce487e24801d01d5214fea150349
UPSTREAM_PLUGIN_RELEASE_SHA256 = 77d5bc7f8e0062f88aef08f3471cc6e4546a0d71d18813752781689ab6ce4848
PROJECT_UPSTREAM_PLUGIN_CFG_BLOB_MATCH = TRUE
```

따라서 Godot AI `3.1.4`는 current project source와 official upstream release가 모두 확인된 current tool source truth다.

아래 live local 상태는 별개이며 이 환경에서 확인할 수 없었다.

```text
LOCAL_GODOT_PROCESS = UNVERIFIED
LOCAL_WS9500 = UNVERIFIED
LOCAL_GODOT_AI_HANDSHAKE = UNVERIFIED
LOCAL_SESSION_REGISTRY = UNVERIFIED
```

### Historical 3.1.3 evidence

2026-08-09의 3.1.3 승인/sync owner는 당시 exact sync를 증명하는 history로 유지한다.

```text
HISTORICAL_GODOT_AI_3_1_3_APPROVAL = PRESERVED
HISTORICAL_REMOTE_SYNC_SHA = f1bf8939208a864bce1f99eea0555f05369dc9d6
HISTORICAL_OWNER_REWRITE_TO_3_1_4 = FORBIDDEN
CURRENT_FILE_MUST_REMAIN_3_1_3_FOREVER = FALSE
```

PR190은 current-file assertion만 3.1.4 truth로 분리했다.

### GUT / Hera

```text
GUT_VERSION = 9.7.1
GUT_ROLE = DETERMINISTIC_GDSCRIPT_TEST_AUTHORITY
HERA_VERSION = 1.0.0
HERA_ROLE = LIVE_QA_AND_OBSERVABILITY_ONLY
HERA_PERSISTENT_SOURCE_MUTATION = FORBIDDEN
```

## 3. Source / benchmark disposition

```text
BASE_GODOT_CODE_ENGINEERING_SOURCE_REFRESH = ADOPT
GODOT_4_7_1_OFFICIAL_RELEASE = ADOPT
GODOT_AI_V3_1_4_OFFICIAL_RELEASE_AND_SOURCE = ADOPT
GUT_9_7_1_GODOT_4_7_LINE = ADOPT_WITH_EXACT_VERSION_VERIFY
GODOT_DEMO_MASTER_AS_EXACT_4_7_AUTHORITY = AVOID
GODOT_DEMO_4_7_RELEASE_AS_REFERENCE = ADAPT
COMPETITOR_OR_THIRD_PARTY_BEHAVIOR_AUTOMATIC_AUTHORITY = FORBIDDEN
```

업로드된 `godot-demo-projects-master.zip`은 master/dev reference일 뿐 exact 4.7 implementation authority가 아니다.

## 4. Direct-main CI blind spot and TDD

`14b0d942...`는 addon source를 변경했지만 당시 `Validate Omenward Core`의 path filter에 `addons/**`가 없어 full Python/Godot validation이 trigger되지 않았다.

```text
ROOT_CAUSE = OMENWARD_CORE_PATH_FILTER_OMITTED_ADDONS
```

TDD RED:

```text
ADDON_TRIGGER_EXPECTED = 2
ADDON_TRIGGER_ACTUAL_BEFORE_FIX = 0
VALIDATOR_ADDON_TRIGGER_GUARD_BEFORE_FIX = ABSENT
RED_HEAD_GODOT_4_7_1_IMPORT_HEADLESS_RUNTIME = SUCCESS
```

같은 full Python RED는 current 3.1.4 plugin에 대해 current file도 3.1.3이어야 한다고 검사하던 stale regression을 추가로 발견했다.

GREEN:

```text
OMENWARD_CORE_PR_ADDONS_TRIGGER = REQUIRED
OMENWARD_CORE_PUSH_ADDONS_TRIGGER = REQUIRED
CI_USAGE_VALIDATOR_REQUIRES_TWO_ADDON_TRIGGERS = TRUE
CURRENT_GODOT_AI_FILE_ASSERTION = 3.1.4
HISTORICAL_3_1_3_ASSERTIONS = PRESERVED
```

v4.5 C0 exact-surface contract도 RED-first로 추가했고, C0 paths가 unapproved라 실패한 것을 확인한 뒤 정확한 eight-file mode만 등록했다. active-v4.4는 별도 fallback 확장 없이 v4.5 PASS를 소비해 Green으로 복구됐다.

## 5. PR175 current-main boundary

```text
PR175 = OPEN_DRAFT
PR175_HEAD = bde85549560fca90f7aa25fc4842bc0a3afb92e7
PR175_MERGE_BASE = 87339f87949c8faea0dfe1482c5d0887a04d94f4
PR175_AHEAD_CURRENT_MAIN = 43
PR175_BEHIND_CURRENT_MAIN = 14
PR175_STATUS = DIVERGED
PR175_HISTORICAL_GREEN_AS_CURRENT_EVIDENCE = FORBIDDEN
ISSUE176_7_GAPS = IMPLEMENTATION_COMPLETENESS
```

C0는 새 product decision을 만들지 않으며 PR175 merge를 승인하지 않는다.

## 6. Exact fail-closed PR190 surface

```text
.github/workflows/validate-omenward-core.yml
docs/reviews/PHASE_C_C0_PREFLIGHT_2026-08-11.md
docs/superpowers/plans/2026-08-11-phase-c-c0-toolchain-ci-gate.md
tests/python/test_canon_freshness_v45_scope.py
tests/python/test_phase_c_c0_toolchain_ci_gate.py
tests/python/test_tool_state_user_approval_remote_sync.py
tools/validate_canon_freshness_v45_scope.py
tools/validate_ci_usage_contract.py
```

```text
PR190_CHANGED_FILE_COUNT = 8
PR190_PROTECTED_PRODUCT_OR_ADDON_SOURCE_MUTATION = 0
PR190_PROJECT_GODOT_MUTATION = 0
PR190_REVIEW_THREADS = 0
```

## 7. Pre-final verified evidence head

Evidence-owner/checkpoint 문서를 쓰기 직전의 검증 head는 다음과 같다.

```text
PRE_FINAL_VERIFIED_HEAD = e3100bcfe6ed3e69c3bb3aba2774261751eae42e
TRIGGERED_WORKFLOWS = 7
TRIGGERED_WORKFLOWS_SUCCESS = 7
OMENWARD_CORE_FULL_PYTHON_SUITE = SUCCESS
GODOT_4_7_1_IMPORT = SUCCESS
GODOT_HEADLESS_CONTRACTS = SUCCESS
GODOT_RUNTIME_SMOKE = SUCCESS
CANON_V45 = SUCCESS
ACTIVE_V44 = SUCCESS
TOOL_STATE_SYNC = SUCCESS
BASE_V9 = SUCCESS
PROJECT_CORE = SUCCESS
GDD_SHEET_ADOPTION = SUCCESS
```

이 문서/plan checkpoint 갱신 자체가 PR head를 바꾸므로 `PRE_FINAL_VERIFIED_HEAD`를 final merge SHA라고 부르지 않는다. 실제 merge gate는 이 문서 갱신 후 GitHub가 반환하는 **현재 PR head**에 대해 다시 모든 관련 CI를 확인하며, 그 SHA를 이 파일에 재기록해 자기참조 head churn을 만들지 않는다.

## 8. Sheet pre-merge evidence

같은 Decision ID로 동기화했다.

```text
SHEET_DECISION = OMW-DEC-20260811-OPS-PHASE-C-C0-PREFLIGHT-V1
SHEET_CURRENT_OMENWARD_MAIN = 14b0d942e071dc6e823f48c29ac79f0978477d85
SHEET_CURRENT_BASE_MAIN = 8e7d85b1b1272002a8086c502a41073888cb3318
SHEET_PR190_EVIDENCE = e3100bcf / 7_OF_7_SUCCESS
SHEET_PR175 = DIVERGED_AHEAD43_BEHIND14
SHEET_GODOT_AI = 3.1.4_UPSTREAM_RELEASE_VERIFIED
SHEET_GUT = 9.7.1
SHEET_LOCAL_LIVE_SESSION = UNVERIFIED
SHEET_PREMERGE_REREAD = PASS
```

## 9. Merge gate and final C0 classification

현재 상태:

```text
C0_REPOSITORY_PR_GATE = PASS_PENDING_FINAL_HEAD_RERUN_AND_MERGE
LOCAL_LIVE_SESSION_GATE = UNVERIFIED
PR175_RUNTIME_RESUME = NOT_AUTHORIZED
PR175_MERGE = FORBIDDEN
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

남은 repository-side gate:

1. evidence-owner 갱신 후의 actual PR190 head를 fresh-read한다.
2. exact 8 files / threads0 / main race 없음 확인.
3. actual head의 관련 workflow 전부 Green을 확인한다.
4. expected-head merge한다.
5. merged main의 Omenward Core full matrix Ubuntu/Windows × Python 3.11/3.12/3.13 + Godot를 확인한다.
6. Sheet에 merge SHA와 post-merge evidence를 final sync/readback한다.

live local session 증거가 여전히 없다면 repository-side 완료 후 최종 C0 분류는 다음으로 제한한다.

```text
C0_PARTIAL_PASS_REPOSITORY_TOOLCHAIN_VERIFIED_LOCAL_LIVE_SESSION_UNVERIFIED
```

## 10. Next runtime boundary

PR175 구현 재개 전 같은 snapshot에서 반드시 확인한다.

1. exact OMENWARD Godot process + command line;
2. 해당 process의 ESTABLISHED WS9500;
3. current Godot AI connection / handshake / auth / 4003 / reconnect logs;
4. 즉시 실행한 session registry/list 결과.

그 후 current main에 맞춰 PR175를 rebase/revalidate하고 Issue176 7개 runtime gap을 approved HiGodot → GUT RED/GREEN → Godot import/headless → deterministic FV → Hera live QA 순서로 수행한다.