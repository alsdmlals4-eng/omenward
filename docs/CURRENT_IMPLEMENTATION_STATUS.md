# [현행] 오멘워드 현재 구현 상태

```yaml
updated_at: 2026-08-10T13:15:00+09:00
common_work_authority: alsdmlals4-eng/Base/AGENTS.md
planning_canon: MAIN_CANONICAL_APPROVED_10_OF_10
current_runtime_authority: OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
active_pr: 175
active_issue: 176
active_runtime_branch: runtime/barracks-role-output-implementation-20260809
active_runtime_head: bde85549560fca90f7aa25fc4842bc0a3afb92e7
runtime_package_status: TRANSITION_CI_GREEN_RUNTIME_GAPS_IN_PROGRESS_EXTERNAL_HIGODOT_BLOCKED
runtime_blocker: RECOVERABLE_HIGODOT_REGISTRY_OMISSION_AFTER_RECENT_LIVE_WS
execution_route_blocker: BLOCKED_UNVERIFIED_LOCAL_HIGODOT_SAME_SNAPSHOT_DIAGNOSTIC_UNAVAILABLE
human_validation: NOT_RUN
final_weighted_fv_numerics: NOT_SELECTED
```

공통 운영 규칙은 Base 책임 원본에서 관리한다. 이 문서는 OMENWARD의 프로젝트별 기획·구현·검증 상태만 기록한다. 2026-08-10 현재 planning canon은 유지되며, 승인된 bounded runtime package가 Draft PR #175 / Issue #176에서 같은 승인 범위로 진행 중이다.

## 현재 runtime implementation package

```text
DECISION = OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
PR175 = OPEN_DRAFT_PR_REVISE
ISSUE176 = OPEN
RUNTIME_BRANCH = runtime/barracks-role-output-implementation-20260809
CURRENT_HEAD = bde85549560fca90f7aa25fc4842bc0a3afb92e7
SAME_APPROVED_SCOPE_NO_REAPPROVAL
```

### Current exact-head evidence at `bde85549...`

```text
GitHub Actions triggered workflows = 11
GitHub Actions SUCCESS = 11
GitHub Actions FAILURE = 0
Validate Omenward Core = SUCCESS
Validate Base v9 adoption = SUCCESS
Validate Project Base Adapter = SUCCESS
Validate active integrated contract v4.4 = SUCCESS
Validate Barracks Functional Value Combat Numerics Review = SUCCESS
Validate Omenward GDD Sheet Adoption = SUCCESS
Godot product/runtime path mutation by transition-CI reconciliation = NONE
```

이 exact head에서 이전 `b014a844...`의 네 durable transition failure는 모두 해소됐다.

1. historical Barracks FV Combat Numerics Review의 stale runtime-incompleteness assertion을 current partial runtime transition에 맞게 보수했다.
2. Base v9 protected-path gate는 정확한 승인 runtime surface만 fail-closed로 허용한다.
3. Project Base Adapter generated compatibility view의 unchanged legacy-source hash를 복원하고 승인 runtime transition을 별도 판정한다.
4. active integrated v4.4는 normal PR에는 planning-only gate를 유지하고 승인 runtime transition에만 bounded exception을 허용한다.

이 네 CI transition blocker의 해소는 Issue #176 제품/runtime gap 완료가 아니다.

## Last completed Godot runtime evidence

Godot/GUT/Hera를 실제로 완료 실행한 마지막 runtime evidence는 `621ae7ce80f24b1e5a9d13ba4fc1962bec42dd96`이다.

```text
GUT RED = 10 discovered / 1 pass / 9 intended fail
Godot 4.7.1 import = PASS
GUT GREEN = 10/10 / 52 assertions
existing headless regressions = 13/13 PASS
five FV-labelled smoke scenarios x2 = identical raw outputs
CONTROL_TARGET_SECONDS = BLOCKED_RUNTIME_OUTPUT
AIR_TARGETABILITY_EXPOSURE = BLOCKED_RUNTIME_OUTPUT
Hera tracked-source delta = NONE
simulation sidecars = NONE
final weighted FV scalar/vector/product numerics = NOT_SELECTED
```

Adversarial review가 아래 일곱 package-completeness gap을 발견했으므로 이 evidence는 merge-complete가 아니다. `bde85549...`에서 추가된 것은 non-Godot transition CI/tool/test reconciliation이며 새로운 Godot runtime Green 증거가 아니다.

## Issue #176 남은 승인 gap

1. Priest encouragement: 5s attack-speed +8%, start/end events, support uptime, timing regression.
2. support-role deterministic fallback 보존.
3. `flying` priority와 target permission boundary 분리.
4. `cluster` tie-break를 lane order/unit-id semantics로 수정.
5. Giant `FRONTLINE_SURVIVAL_TIME`, `STRUCTURE_DAMAGE` collector.
6. registered deterministic FV-PRIEST/MAGE/FLIER/GIANT/COMMON fixtures.
7. true `TARGETS_HIT_PER_CAST`와 multi-cast coverage.

## 현재 local/HiGodot precondition 상태

가장 최근 local evidence에서 `session_manage(op=list)`는 GRIMOIRE task7 session 하나만 반환했고 OMENWARD session은 없었다.

```text
LATEST_REGISTERED_SESSION = task7-circuit-placement-screen@63aa
LATEST_REGISTERED_EDITOR_PID = 16652
LATEST_REGISTERED_READINESS = ready
OMENWARD_SESSION = ABSENT_IN_LAST_LIST
```

직전 재현은 exact OMENWARD GUI PID `29616` + console PID `10512` 생존과 GUI PID `29616`의 ESTABLISHED WS9500을 확인했다. 두 evidence가 동일 시점이 아니므로 현재 판정은:

```text
LAST_TECHNICAL_CLASSIFICATION = RECOVERABLE_HIGODOT_REGISTRY_OMISSION_AFTER_RECENT_LIVE_WS
SAME_SERVER_HANDSHAKE_REGISTRATION_FAILURE = BLOCKED_UNVERIFIED
CURRENT_AGENT_ROUTE = BLOCKED_UNVERIFIED_LOCAL_HIGODOT_SAME_SNAPSHOT_DIAGNOSTIC_UNAVAILABLE
```

이 agent environment에서는 사용자의 Windows process/socket/Godot-AI session을 직접 관찰하거나 HiGodot persistent-authoring route를 실행할 수 없으므로 same-snapshot local diagnostic과 실제 Issue #176 Godot mutation은 수행하지 않는다.

## 사용자 handoff 요청과 이후 재개 상태

2026-08-10 11:57 KST 사용자는 당시 HiGodot 진단부터 이후 작업을 나중에 다시 진행하고 먼저 인수인계 작업으로 전환하도록 요청했다. 이 사실은 `HANDOFF_CONTEXT.md`의 historical snapshot에 그대로 보존한다.

이후 새 single-file execution contract에 따라 orchestration을 재개했고, 로컬 HiGodot 작업이 막힌 동안 독립적으로 가능한 transition CI reconciliation과 Base/Sheet/handoff 상태 정합화를 진행했다.

```text
11:57 HANDOFF_SNAPSHOT = VALID_HISTORY
CURRENT_ORCHESTRATION = RESUMED
FULL_ISSUE176_HIGODOT_CHILD = NOT_RUN
GODOT_PRODUCT_MUTATION_AFTER_B014 = NONE
NON_GODOT_TRANSITION_CI_RECONCILIATION = COMPLETE
```

## Base project learning 상태

Fresh Base truth:

```text
BASE_MAIN = d5cfcfa96fcf33bf7e01dc617d7f68e8d5bbbeaf
BCP013 = BCP-2026-013-post-merge-continuation-state-reconciliation
BCP013_PR235 = MERGED_PROPOSAL_ONLY
BCP013_MERGE_SHA = 3ff790116bc08f49e126cd286ec453bf6e46376e
EXISTING_SOLUTION_VERDICT = REUSE_BCP_2026_013
PROJECT_EVIDENCE_NAME = BCP - OMENWARD
BASE_EVIDENCE_PR243 = OPEN_DRAFT
BASE_EVIDENCE_BRANCH_CREATION_BASE = c14e4e841171a98e2471cbe7ff94afe4d55501fb
BASE_EVIDENCE_REFRESHED_BASE = d5cfcfa96fcf33bf7e01dc617d7f68e8d5bbbeaf
BASE_EVIDENCE_HEAD = 0fc5c6d193c26f1cc6145e29b5dbfe1141c9ded8
BASE_EVIDENCE_CHANGED_FILES = 1
BASE_EVIDENCE_VALIDATION = SUCCESS
BASE_RACE_AFTER_PR243_CREATION = PR244_BCP014_WORDING_PROPOSAL_ONLY_NONOVERLAP
PROPOSAL_REGISTRY_CHANGE = NONE
ACTIVE_BASE_IMPLEMENTATION = NOT_AUTHORIZED_BY_THIS_STAGE
```

사용자의 `BCP - 프로젝트 이름` 규칙을 적용해 OMENWARD evidence는 `BCP - OMENWARD`로 기록했다. 새 canonical BCP는 만들지 않고 기존 BCP-013을 재사용한다.

Base Draft PR #243의 정확한 파일은 다음 하나다.

`[수정제안서]/BCP-2026-013-post-merge-continuation-state-reconciliation/evidence/BCP-OMENWARD.md`

PR #243 생성 이후 Base main이 `d5cfcfa9...`로 전진했고, 새 변화는 다른 프로젝트 BCP-014의 proposal-only 문구 정정 한 파일이었다. 경로 비중첩을 확인한 뒤 current main을 evidence branch에 통합했으며, current PR #243 diff는 계속 한 파일이고 exact-head Base validation은 SUCCESS다.

다른 프로젝트의 open proposal PR과 `PROPOSAL_REGISTRY.json`은 변경하지 않는다. Base active Skill/Method/Template/Test/Workflow 구현은 별도 승인 단계다.

## 보존되는 planning canon 상태

```text
FIRST_10_15_MINUTES_PLANNING = MAIN_CANONICAL_APPROVED_10_OF_10
BARRACKS_TOKEN_SOURCE_AMENDMENT = MAIN_CANONICAL
PR142_MERGED = TRUE
PR142_MERGE_SHA = 1c646c2d764d0df43545e00b914189ed46cf1bd4
PR142_PRODUCT_PATHS_CHANGED = 0
PR142_SHEET_BOUNDED_READBACK = PASS
PR142_BOUNDED_CANON_TESTS = PASS_AS_RECORDED
PR142_FULL_PYTHON_SUITE = NOT_RUN
PR142_GODOT_TESTS = NOT_RUN
PR142_RUNTIME = NOT_RUN
PR142_HUMAN_QA = NOT_RUN
EXACT_BUILD_AND_ECONOMY_NUMERICS = PENDING_SIMULATION_UNLESS_SUPERSEDED_BY_APPROVED_RUNTIME_MEASUREMENT_CONTRACT
```

기존 특수병 T1 자동생산·TokenSource 정정과 온보딩 10/10 canon은 이번 runtime role-output package, transition CI reconciliation 또는 handoff로 폐기되지 않는다. 상세 제품 정본은 `ONBOARDING_PLANNING_CURRENT_AUTHORITY.md` 및 관련 approved design 문서를 따른다.

## 보존되는 PC·Android 공용 코어 상태

```text
ARCHITECTURE_STATUS = MAIN_CANONICAL
PHASE0_STATIC_GUARD = MAIN_CANONICAL_LOCAL_PASS
PHASE1_COMMAND_EVENT_CONTRACTS = MAIN_CANONICAL_LOCAL_PASS
PHASE2_GAME_SESSION_DECOUPLING = MAIN_CANONICAL_LOCAL_PASS
GAME_COMMAND = IMPLEMENTED
GAME_EVENT = IMPLEMENTED
SEVEN_PLATFORM_CONTRACTS = IMPLEMENTED
GAME_APPLICATION = IMPLEMENTED
SESSION_DRIVER = IMPLEMENTED
SCENE_BINDER = IMPLEMENTED
PLATFORM_BOOTSTRAP = IMPLEMENTED_IDEMPOTENT
GAME_SESSION_COMPATIBILITY_FACADE = IMPLEMENTED
SHARED_SAVE_SCHEMA = NOT_STARTED
PC_ADAPTER_IMPLEMENTATION = NOT_STARTED
ANDROID_ADAPTER_IMPLEMENTATION = NOT_STARTED
STORE_SDK_INTEGRATION = NOT_STARTED
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
EXPORT_PRESETS = ABSENT
REPRESENTATIVE_PC_BUILD = NOT_RUN
REPRESENTATIVE_ANDROID_BUILD = NOT_RUN
```

Phase 0~2 local-pass는 platform boundary evidence만 증명하며 현재 runtime package, vertical slice 전체 구현, 출시 준비 완료를 뜻하지 않는다.

## 보존되는 과거 C1·C2·C3 증거

```text
C1_ROULETTE_CORE_REMOTE_PROVEN
C1_HEAD = 19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9
C1_RUN = 29926598807
C2_BATTLE_OBJECTIVE_REMOTE_PROVEN
C2_RUN = 29938742864
C3_AUTOMATED_CONTRACTS_PROVEN
C3_HEAD = 1976c5355124b2ce7d7ef77b8835df0c95710038
C3_RUN = 29965348284
```

이 증거는 과거 계약 검증 사실이며 PR #175의 Issue #176 gap 완료나 현재 제품 Green을 의미하지 않는다.

## 재개 시 next executable step

full executor보다 먼저 하나의 same-snapshot read-only local 진단을 실행한다.

1. current exact OMENWARD Godot process + command line을 확인한다. 과거 PID `29616`이 재사용되었다고 가정하지 않는다.
2. 해당 current process의 ESTABLISHED WS9500을 확인한다.
3. current Godot-AI connection/handshake/auth/4003/reconnect/session log lines를 확인한다.
4. 같은 snapshot에서 즉시 `session_manage(op=list)`를 실행한다.

```text
LIVE_EXACT_OMENWARD + WS9500 + REGISTRY_OMISSION
=> RECOVERABLE_HIGODOT_SAME_SERVER_HANDSHAKE_REGISTRATION_BLOCKER

PROCESS_OR_WS_MISSING
=> current process/transport blocker로 재분류, reason은 검증 전 추정하지 않음

EXACT_OMENWARD_SESSION_PRESENT
=> current PR175 head를 fresh-read한 뒤 Issue176 NonInteractive executor 재개
```

## 보호 경계

- shared Godot-AI server와 다른 프로젝트 editor를 종료하지 않는다.
- root-cause 증거 전에 executor/session-selection logic을 패치하지 않는다.
- `core.autocrlf`, `.gitattributes`, PowerShell ExecutionPolicy, sandbox/permission, Godot version gate를 변경/우회하지 않는다.
- persistent Godot/GDScript/GUT authoring은 HiGodot/Godot AI MCP만 사용한다.
- GUT RED→GREEN 이후에 Hera live QA를 실행하고 tracked-source delta NONE을 요구한다.
- unavailable metric은 literal `BLOCKED_RUNTIME_OUTPUT`을 유지한다.
- final weighted FV scalar/vector/product numerics를 선택하지 않는다.
