# [현행] 오멘워드 현재 구현 상태

```yaml
updated_at: 2026-08-10T14:47:00+09:00
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
base_main_seen: 0a7c4a4286b1107b1bfa03dc4b4e4ce88fbbd5b8
base_omenward_proposal: BCP - OMENWARD
base_omenward_proposal_id: BCP-2026-015-external-runtime-session-same-snapshot-recovery
base_omenward_proposal_pr: 246
base_omenward_proposal_state: MERGED_PROPOSAL_ONLY
base_omenward_proposal_merge_sha: 0a7c4a4286b1107b1bfa03dc4b4e4ce88fbbd5b8
base_omenward_post_merge_ci: SUCCESS
base_omenward_post_merge_run: 31359540698
base_active_rule_change: NONE
```

공통 운영 규칙은 Base 책임 원본에서 관리한다. 이 문서는 OMENWARD의 프로젝트별 기획·구현·검증 상태만 기록한다. planning canon은 유지되며, 승인된 bounded runtime package가 Draft PR #175 / Issue #176에서 같은 승인 범위로 진행 중이다.

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

이 exact head에서 이전 `b014a844...`의 네 durable transition failure는 모두 해소됐다. historical FV review, Base v9 protected-path gate, Project Base Adapter generated-view/runtime-transition gate, active integrated v4.4 planning-only gate가 승인된 bounded runtime transition을 정확히 인식하도록 non-Godot CI/tool/test 범위에서 보수됐다. 이 작업은 Issue #176 제품/runtime gap을 닫지 않았다.

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

가장 최근 durable local evidence에서 `session_manage(op=list)`는 GRIMOIRE task7 session 하나만 반환했고 OMENWARD session은 없었다. 직전 재현은 exact OMENWARD GUI PID `29616` + console PID `10512` 생존과 GUI PID `29616`의 ESTABLISHED WS9500을 확인했다. 두 evidence가 동일 시점이 아니므로 현재 판정은 다음과 같다.

```text
LAST_TECHNICAL_CLASSIFICATION = RECOVERABLE_HIGODOT_REGISTRY_OMISSION_AFTER_RECENT_LIVE_WS
SAME_SERVER_HANDSHAKE_REGISTRATION_FAILURE = BLOCKED_UNVERIFIED
CURRENT_AGENT_ROUTE = BLOCKED_UNVERIFIED_LOCAL_HIGODOT_SAME_SNAPSHOT_DIAGNOSTIC_UNAVAILABLE
```

이 agent environment에서는 사용자의 Windows process/socket/Godot-AI session을 직접 관찰하거나 HiGodot persistent-authoring route를 실행할 수 없으므로 same-snapshot local diagnostic과 실제 Issue #176 Godot mutation은 수행하지 않는다.

## 사용자 handoff 요청과 이후 재개 상태

2026-08-10 11:57 KST 사용자는 당시 HiGodot 진단부터 이후 작업을 나중에 다시 진행하고 먼저 인수인계 작업으로 전환하도록 요청했다. 이 사실은 `HANDOFF_CONTEXT.md`의 historical snapshot에 그대로 보존한다.

이후 orchestration을 재개했고, 로컬 HiGodot 작업이 막힌 동안 독립적으로 가능한 transition CI reconciliation, Base 프로젝트 출처형 수정제안서 정정·병합, Sheet/handoff 상태 정합화를 진행했다.

```text
11:57 HANDOFF_SNAPSHOT = VALID_HISTORY
CURRENT_ORCHESTRATION = RESUMED
FULL_ISSUE176_HIGODOT_CHILD = NOT_RUN
GODOT_PRODUCT_MUTATION_AFTER_B014 = NONE
NON_GODOT_TRANSITION_CI_RECONCILIATION = COMPLETE
PR177 = REFERENCE_ONLY_HANDOFF_DO_NOT_MERGE_NOW
```

## Base project learning 상태

Base 활성 규칙은 이번 작업에서 수정하지 않는다. 프로젝트에서 실제 검증된 개선점은 별도 프로젝트 출처형 수정제안서로 저장한다.

```text
Base active rules unchanged
→ [수정제안서]/BCP-<id>/PROPOSAL.md
→ display title: BCP - [프로젝트명]
→ project-verified evidence
→ PROPOSAL_REGISTRY.json registration
→ proposal-only PR
→ exact-head validation
→ merge
→ post-merge readback/CI
```

OMENWARD 적용 결과:

```text
BASE_MAIN = 0a7c4a4286b1107b1bfa03dc4b4e4ce88fbbd5b8
PROJECT_SOURCE_PROPOSAL = BCP - OMENWARD
PROJECT_SOURCE_PROPOSAL_ID = BCP-2026-015-external-runtime-session-same-snapshot-recovery
BASE_PROPOSAL_PR246 = MERGED_PROPOSAL_ONLY
BASE_PROPOSAL_PREMERGE_HEAD = fdb45ecfd3badac0389261d3f61e31de2f277263
BASE_PROPOSAL_MERGE_SHA = 0a7c4a4286b1107b1bfa03dc4b4e4ce88fbbd5b8
BASE_PROPOSAL_PREMERGE_VALIDATION = SUCCESS
BASE_PROPOSAL_POST_MERGE_RUN = 31359540698
BASE_PROPOSAL_POST_MERGE_VALIDATION = SUCCESS
PROPOSAL_REGISTRY_CHANGE = ADD_BCP_2026_015_ONLY
ACTIVE_BASE_RULE_CHANGE = NONE
ACTIVE_BASE_IMPLEMENTATION = NOT_AUTHORIZED_BY_THIS_STAGE
BCP013_WRONG_OMENWARD_EVIDENCE = REMOVED
BCP013_PROPOSAL_BLOB_SHA = 647b3033881d62f8a0cbcb1fdc3f00e3acc41a7d
BCP013_OTHER_PROJECT_EVIDENCE = PRESERVED
```

별도 canonical proposal:

`[수정제안서]/BCP-2026-015-external-runtime-session-same-snapshot-recovery/PROPOSAL.md`

프로젝트에서 실제 관찰·검증한 evidence:

`[수정제안서]/BCP-2026-015-external-runtime-session-same-snapshot-recovery/evidence/OMENWARD_RUNTIME_SESSION_RECOVERY_EVIDENCE.md`

이 제안은 외부 Editor/MCP session에서 current exact process identity, live transport ownership, bounded server handshake/session log, immediate registry read를 같은 짧은 관측창에 묶는 recovery classification을 제안한다. 한 target session omission만으로 shared server나 다른 프로젝트 Editor를 종료하지 않고, 과거 PID/session id를 current mutation authority로 재사용하지 않는 경계도 포함한다.

이전 PR #243의 `BCP-013/evidence/BCP-OMENWARD.md` 배치는 잘못된 소유 위치였으므로 PR #246에서 그 파일만 제거했다. BCP-013 `PROPOSAL.md`는 blob SHA `647b3033881d62f8a0cbcb1fdc3f00e3acc41a7d`로 보존되며 Switchy Express evidence도 유지된다.

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

기존 특수병 T1 자동생산·TokenSource 정정과 온보딩 10/10 canon은 이번 runtime role-output package, transition CI reconciliation, handoff 또는 Base proposal 병합으로 폐기되지 않는다. 상세 제품 정본은 `ONBOARDING_PLANNING_CURRENT_AUTHORITY.md` 및 관련 approved design 문서를 따른다.

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
