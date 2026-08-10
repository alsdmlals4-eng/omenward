# [현행] 오멘워드 현재 구현 상태

```yaml
updated_at: 2026-08-10T11:57:00+09:00
common_work_authority: alsdmlals4-eng/Base/AGENTS.md
planning_canon: MAIN_CANONICAL_APPROVED_10_OF_10
current_runtime_authority: OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
active_pr: 175
active_issue: 176
active_runtime_branch: runtime/barracks-role-output-implementation-20260809
active_runtime_head: b014a8445423fc9a485fb413429a8127991143e4
runtime_package_status: IN_PROGRESS_USER_DEFERRED_FOR_HANDOFF
runtime_blocker: RECOVERABLE_HIGODOT_REGISTRY_OMISSION_AFTER_RECENT_LIVE_WS
human_validation: NOT_RUN
final_weighted_fv_numerics: NOT_SELECTED
```

공통 운영 규칙은 Base 책임 원본에서 관리한다. 이 문서는 OMENWARD의 프로젝트별 기획·구현·검증 상태만 기록한다. 2026-08-10 현재 planning canon은 유지되며, 승인된 bounded runtime package가 Draft PR #175 / Issue #176에서 별도 execution lane으로 진행 중이다.

## 현재 runtime implementation package

```text
DECISION = OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
PR175 = OPEN_DRAFT_PR_REVISE
ISSUE176 = OPEN
RUNTIME_BRANCH = runtime/barracks-role-output-implementation-20260809
CURRENT_HEAD = b014a8445423fc9a485fb413429a8127991143e4
SAME_APPROVED_SCOPE_NO_REAPPROVAL
```

### Current exact-head evidence at `b014a844...`

```text
contracts_pr = 69/69 PASS
whitespace = PASS
Godot 4.7.1 import = PASS
headless contract tests = PASS
runtime smoke = PASS
exact-head Actions = 7 SUCCESS / 4 FAILURE
```

네 failure는 durable transition blockers다.

1. historical Barracks FV Combat Numerics Review가 runtime incompleteness를 계속 주장한다.
2. Base v9 protected-path gate가 이미 승인된 runtime transition을 막는다.
3. Project Base Adapter가 stale/generated-view transition 상태다.
4. active integrated v4.4 planning-only gate가 남아 있다.

이 네 항목은 handoff 작업에서 수정하지 않는다.

## Last completed runtime evidence

`621ae7ce80f24b1e5a9d13ba4fc1962bec42dd96`:

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

Adversarial review가 아래 일곱 package-completeness gap을 발견했으므로 이 evidence는 merge-complete가 아니다.

## Issue #176 남은 승인 gap

1. Priest encouragement: 5s attack-speed +8%, start/end events, support uptime, timing regression.
2. support-role deterministic fallback 보존.
3. `flying` priority와 target permission boundary 분리.
4. `cluster` tie-break를 lane order/unit-id semantics로 수정.
5. Giant `FRONTLINE_SURVIVAL_TIME`, `STRUCTURE_DAMAGE` collector.
6. registered deterministic FV-PRIEST/MAGE/FLIER/GIANT/COMMON fixtures.
7. true `TARGETS_HIT_PER_CAST`와 multi-cast coverage.

## 현재 local/HiGodot precondition 상태

가장 최근 `session_manage(op=list)`는 GRIMOIRE task7 session 하나만 반환했고 OMENWARD session은 없었다.

```text
LATEST_REGISTERED_SESSION = task7-circuit-placement-screen@63aa
LATEST_REGISTERED_EDITOR_PID = 16652
LATEST_REGISTERED_READINESS = ready
OMENWARD_SESSION = ABSENT
```

직전 재현은 exact OMENWARD GUI PID `29616` + console PID `10512` 생존과 GUI PID `29616`의 ESTABLISHED WS9500을 확인했다. 두 evidence가 동일 시점이 아니므로 현재 판정은:

```text
RECOVERABLE_HIGODOT_REGISTRY_OMISSION_AFTER_RECENT_LIVE_WS
SAME_SERVER_HANDSHAKE_REGISTRATION_FAILURE = BLOCKED_UNVERIFIED
```

## 사용자 요청에 따른 현재 중지 상태

2026-08-10 11:57 KST 사용자가 이 HiGodot 진단부터 이후 작업을 나중에 다시 진행하고 현재는 인수인계 작업으로 전환하도록 요청했다.

```text
RUNTIME_EXECUTION = PAUSED_BY_USER
FULL_ISSUE176_CHILD_AFTER_PAUSE = NOT_RUN
PRODUCT_MUTATION_AFTER_PAUSE = NONE
RUNTIME_BRANCH_MUTATION_BY_HANDOFF = NONE
```

## 재개 시 next executable step

full executor보다 먼저 하나의 same-snapshot read-only 진단을 실행한다.

1. PID `29616` current process + exact OMENWARD command line.
2. PID `29616` current ESTABLISHED WS9500.
3. Godot-AI connection/handshake/auth/4003/reconnect/session log lines.
4. 즉시 `session_manage(op=list)`.

```text
LIVE_EXACT_OMENWARD + WS9500 + REGISTRY_OMISSION
=> RECOVERABLE_HIGODOT_SAME_SERVER_HANDSHAKE_REGISTRATION_BLOCKER

PROCESS_OR_WS_MISSING
=> current process/transport blocker로 재분류

EXACT_OMENWARD_SESSION_PRESENT
=> Issue176 NonInteractive executor 재개
```

## 보호 경계

- shared Godot-AI server와 다른 프로젝트 editor를 종료하지 않는다.
- root-cause 증거 전에 executor/session-selection logic을 패치하지 않는다.
- `core.autocrlf`, `.gitattributes`, PowerShell ExecutionPolicy, sandbox/permission, Godot version gate를 변경/우회하지 않는다.
- persistent Godot/GDScript/GUT authoring은 HiGodot/Godot AI MCP만 사용한다.
- GUT RED→GREEN 이후에 Hera live QA를 실행하고 tracked-source delta NONE을 요구한다.
- unavailable metric은 literal `BLOCKED_RUNTIME_OUTPUT`을 유지한다.
- final weighted FV scalar/vector/product numerics를 선택하지 않는다.

## 플랫폼·출시 경계

기존 Phase 0~2 platform-contract evidence와 planning canon은 이 runtime package/handoff로 변경되지 않는다. 대표 PC/Android build, export, store integration, human QA는 별도 증거가 없는 한 `NOT_RUN` 상태를 유지한다.
