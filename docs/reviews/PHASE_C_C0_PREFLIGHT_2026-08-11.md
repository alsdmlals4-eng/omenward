# [현행 검토] OMENWARD Phase C C0 Preflight — 2026-08-11

```yaml
decision_id: OMW-DEC-20260811-OPS-PHASE-C-C0-PREFLIGHT-V1
review_status: C0_REPOSITORY_GATE_IN_PROGRESS
product_mutation: NONE
runtime_resume_authority: NOT_GRANTED_BY_THIS_REVIEW_ALONE
local_live_session: UNVERIFIED_IN_THIS_ENVIRONMENT
```

## 1. Fresh authority read

C0 시작 시 과거 대화/SHA를 current truth로 재사용하지 않고 Base, OMENWARD, Google Sheet를 다시 읽었다.

```text
BASE_MAIN_OBSERVED = 8e7d85b1b1272002a8086c502a41073888cb3318
BASE_CHANGE = docs: add Godot and code engineering sources (#283)
BASE_OPEN_PRS_AT_ENTRY = 0

OMENWARD_MAIN_OBSERVED = 14b0d942e071dc6e823f48c29ac79f0978477d85
OMENWARD_MAIN_PARENT = 91f4aa98c0dea5307c2482aa0f403ce7dd115e40
OMENWARD_DIRECT_MAIN_COMMIT = TRUE
OMENWARD_DIRECT_MAIN_COMMIT_MESSAGE = d
OMENWARD_DIRECT_MAIN_PUSH_WORKFLOW_RUNS = 0
OMENWARD_DIRECT_MAIN_COMMIT_STATUSES = 0

OPEN_PR175 = DRAFT
OPEN_PR177 = DRAFT_REFERENCE_ONLY_DO_NOT_MERGE
```

Base #283은 Godot source repository / proposals / demo / Asset Library와 code-engineering source를 watchlist에 추가하면서 proposal·demo·asset을 자동 권위로 승격하지 않는 증거 경계를 유지한다. OMENWARD C0와 충돌하지 않으며, 오히려 exact version/release/source 검증을 강화하는 방향으로 소비한다.

## 2. GitHub ↔ Google Sheet drift

C0 entry Sheet는 이전 Phase B closure 상태를 가리켰다.

```text
SHEET_OMENWARD_MAIN = 91f4aa98c0dea5307c2482aa0f403ce7dd115e40
ACTUAL_OMENWARD_MAIN = 14b0d942e071dc6e823f48c29ac79f0978477d85

SHEET_BASE_MAIN = 7a49390bd840f5f5dc80fe661b44ad45e9ebeb7f
ACTUAL_BASE_MAIN = 8e7d85b1b1272002a8086c502a41073888cb3318

GITHUB_SHEET_DRIFT = CONFIRMED_AT_C0_ENTRY
```

Sheet는 검증 전 직접 main 변경을 자동 승인 정본으로 해석하지 않는다. PR190 exact-head 검증 후 같은 C0 Decision ID로 current-facing 행을 동기화한다.

## 3. Current toolchain truth

### Godot

```text
GODOT_CI_RUNTIME = 4.7.1-stable
GODOT_PROJECT_FEATURE_LINE = 4.7
GODOT_4_7_1_RELEASE_DATE = 2026-07-14
```

공식 Godot release를 current runtime authority로 사용한다.

### Godot AI / HiGodot

OMENWARD current main:

```text
addons/godot_ai/plugin.cfg version = 3.1.4
PROJECT_GODOT_AI_PLUGIN_CFG_BLOB = fe28f1acfc69f229bc3c2ea55ac5f854924be466
```

공식 upstream `hi-godot/godot-ai` current main의 동일 파일도 `3.1.4`이며 동일 blob SHA를 가진다. GitHub latest release도 확인했다.

```text
GODOT_AI_UPSTREAM_LATEST_RELEASE = v3.1.4
GODOT_AI_UPSTREAM_RELEASE_PUBLISHED_AT = 2026-08-10T04:24:49Z
GODOT_AI_UPSTREAM_VERSION_BUMP_COMMIT = 96cc8b8c3d25ce487e24801d01d5214fea150349
GODOT_AI_PLUGIN_RELEASE_SHA256 = 77d5bc7f8e0062f88aef08f3471cc6e4546a0d71d18813752781689ab6ce4848
PROJECT_UPSTREAM_PLUGIN_CFG_BLOB_MATCH = TRUE
```

따라서 `3.1.4`는 더 이상 `USER_REPORTED_ONLY`가 아니다. 현재 project vendored source와 upstream release가 모두 확인된 current tool source truth다.

단, 아래는 별개다.

```text
LOCAL_GODOT_PROCESS = UNVERIFIED_IN_THIS_ENVIRONMENT
LOCAL_WS9500 = UNVERIFIED_IN_THIS_ENVIRONMENT
LOCAL_GODOT_AI_HANDSHAKE = UNVERIFIED_IN_THIS_ENVIRONMENT
LOCAL_SESSION_REGISTRY = UNVERIFIED_IN_THIS_ENVIRONMENT
```

source/release 검증을 live local session 검증으로 오인하지 않는다.

### Historical 3.1.3 owner

`docs/process/APPROVED_OMENWARD_GODOT_AI_3_1_3_HERA_GUT_USER_APPROVAL_AND_REMOTE_SYNC_RECONCILIATION_2026-08-09.md`는 당시 사용자 승인과 exact 3.1.3 remote sync를 증명하는 역사 정본으로 보존한다.

```text
HISTORICAL_GODOT_AI_3_1_3_APPROVAL = PRESERVED
HISTORICAL_REMOTE_SYNC_SHA = f1bf8939208a864bce1f99eea0555f05369dc9d6
HISTORICAL_OWNER_REWRITE_TO_3_1_4 = FORBIDDEN
CURRENT_FILE_MUST_REMAIN_3_1_3_FOREVER = FALSE
```

PR190은 durable test를 역사 증거와 current-file truth로 분리한다.

### GUT / Hera

```text
GUT_PROJECT_VERSION = 9.7.1
GUT_ROLE = DETERMINISTIC_GDSCRIPT_TEST_AUTHORITY
HERA_PROJECT_VERSION = 1.0.0
HERA_ROLE = LIVE_QA_AND_OBSERVABILITY_ONLY
HERA_PERSISTENT_SOURCE_MUTATION = FORBIDDEN
```

GUT 9.7.1은 Godot 4.7 계열 테스트 권위로 유지한다. Godot 4.7 return-type/double 동작 변화 때문에 runtime/GUT regression은 exact engine line에서 다시 검증한다.

## 4. Benchmark / industry / source disposition

```text
BASE_GODOT_CODE_ENGINEERING_SOURCE_REFRESH = ADOPT
GODOT_4_7_1_OFFICIAL_RELEASE = ADOPT
GODOT_AI_V3_1_4_OFFICIAL_RELEASE_AND_SOURCE = ADOPT
GUT_9_7_1_GODOT_4_7_LINE = ADOPT_WITH_EXACT_VERSION_VERIFY
GODOT_DEMO_MASTER_AS_EXACT_4_7_AUTHORITY = AVOID
GODOT_DEMO_4_7_RELEASE_AS_REFERENCE = ADAPT
COMPETITOR_OR_THIRD_PARTY_BEHAVIOR_AUTOMATIC_AUTHORITY = FORBIDDEN
```

업로드된 demo `master` snapshot은 참고자료일 뿐 exact 4.7 구현 권위가 아니다.

## 5. Direct-main CI blind spot

`14b0d942...`는 Godot AI 3.1.4 source 변경을 포함하지만 당시 `Validate Omenward Core` path filter가 `addons/**`를 감시하지 않았다.

```text
DIRECT_MAIN_ADDON_CHANGE_WITHOUT_CORE_CI = TRUE
ROOT_CAUSE = OMENWARD_CORE_PATH_FILTER_OMITTED_ADDONS
```

PR190의 TDD RED에서 이를 먼저 고정했다.

RED 결과:

```text
ADDON_TRIGGER_EXPECTED = 2
ADDON_TRIGGER_ACTUAL_BEFORE_FIX = 0
VALIDATOR_ADDON_TRIGGER_GUARD_BEFORE_FIX = ABSENT
GODOT_4_7_1_IMPORT_HEADLESS_RUNTIME_SMOKE_ON_RED_HEAD = SUCCESS
```

같은 full Python suite는 current plugin 3.1.4에 대해 current-file test가 3.1.3을 요구하던 stale regression도 발견했다.

GREEN correction:

```text
OMENWARD_CORE_PULL_REQUEST_ADDONS_TRIGGER = REQUIRED
OMENWARD_CORE_MAIN_PUSH_ADDONS_TRIGGER = REQUIRED
CI_USAGE_VALIDATOR_REQUIRES_TWO_ADDON_TRIGGERS = TRUE
CURRENT_GODOT_AI_FILE_ASSERTION = 3.1.4
HISTORICAL_3_1_3_AUTHORITY_ASSERTIONS = PRESERVED
```

## 6. PR175 current-main divergence

Fresh compare against `14b0d942...`:

```text
PR175_HEAD = bde85549560fca90f7aa25fc4842bc0a3afb92e7
PR175_MERGE_BASE = 87339f87949c8faea0dfe1482c5d0887a04d94f4
PR175_AHEAD_CURRENT_MAIN = 43
PR175_BEHIND_CURRENT_MAIN = 14
PR175_STATUS = DIVERGED
PR175_HISTORICAL_GREEN_AS_CURRENT_EVIDENCE = FORBIDDEN
```

Issue176의 7개 gap은 계속 implementation completeness다. C0는 새 product decision을 만들지 않는다.

## 7. C0 exact fail-closed surface

PR190은 최종적으로 아래 8개 비제품 파일만 변경하도록 잠근다.

```text
.github/workflows/validate-omenward-core.yml
docs/reviews/PHASE_C_C0_PREFLIGHT_2026-08-11.md
docs/superpowers/plans/2026-08-11-phase-c-c0-toolchain-ci-gate.md
tests/python/test_phase_c_c0_toolchain_ci_gate.py
tests/python/test_tool_state_user_approval_remote_sync.py
tools/validate_ci_usage_contract.py
tests/python/test_canon_freshness_v45_scope.py
tools/validate_canon_freshness_v45_scope.py
```

```text
PR190_PRODUCT_PATH_MUTATION = 0_REQUIRED
PR190_GODOT_SOURCE_MUTATION = 0_REQUIRED
PR190_SCOPE_FILE_COUNT = 8_REQUIRED
```

v4.5가 이 exact surface를 PASS하면 historical active-v4.4 workflow는 별도 allowlist 확장 없이 v4.5 PASS를 소비해야 한다.

## 8. C0 gate classification

현재 review 작성 시점의 분류:

```text
C0_REPOSITORY_GATE = IN_PROGRESS_PENDING_EXACT_HEAD_GREEN
LOCAL_LIVE_SESSION_GATE = UNVERIFIED
PR175_RUNTIME_RESUME = NOT_AUTHORIZED_YET
PR175_MERGE = FORBIDDEN
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

PR190 exact head의 full Python + Godot + v4.5 + active-v4.4 등 모든 관련 CI, adversarial surface review, Sheet sync/readback, main-push verification까지 끝난 뒤 repository-side C0를 닫는다.

live local session 증거가 이 환경에서 확보되지 않는다면 최종 분류는 다음으로 제한한다.

```text
C0_PARTIAL_PASS_REPOSITORY_TOOLCHAIN_VERIFIED_LOCAL_LIVE_SESSION_UNVERIFIED
```

## 9. Next runtime boundary

PR175 구현을 재개하기 전 같은 snapshot에서 반드시 확인할 항목:

1. exact OMENWARD Godot process + command line;
2. 해당 process의 ESTABLISHED WS9500;
3. current Godot AI connection / handshake / auth / 4003 / reconnect logs;
4. 즉시 실행한 session registry/list 결과.

그 후 current main에 맞춰 PR175를 rebase/revalidate하고 Issue176 7개 runtime gap을 approved HiGodot → GUT RED/GREEN → Godot import/headless → deterministic FV → Hera live QA 순서로 수행한다.