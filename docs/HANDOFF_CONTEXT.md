# [현행] OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-10T11:57:00+09:00
project: OMENWARD / 오멘워드
handoff_reason: USER_REQUESTED_DEFER_RUNTIME_DIAGNOSIS_AND_RESUME_LATER
main_sha: 87339f87949c8faea0dfe1482c5d0887a04d94f4
active_runtime_branch: runtime/barracks-role-output-implementation-20260809
active_runtime_head: b014a8445423fc9a485fb413429a8127991143e4
active_pr: 175
active_issue: 176
handoff_branch: docs/handoff-pr175-issue176-pause-20260810
current_decision: OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
approval_state: SAME_APPROVED_SCOPE_NO_REAPPROVAL
planning_canon: MAIN_CANONICAL_APPROVED_10_OF_10
runtime_status: PAUSED_BY_USER_FOR_HANDOFF
blocker: RECOVERABLE_HIGODOT_REGISTRY_OMISSION_AFTER_RECENT_LIVE_WS
next_executable_step: SAME_SNAPSHOT_HIGODOT_PROCESS_WS_REGISTRY_DIAGNOSTIC
user_decision_needed: NO_FOR_SAME_APPROVED_SCOPE
```

## 먼저 읽을 순서

새 세션에서는 이 문서를 과거 사실의 locator로 사용하되 GitHub/Sheet보다 높은 정본으로 취급하지 않는다.

1. OMENWARD repository default branch와 최신 `main` SHA
2. open PR 전체, 특히 Draft PR #175
3. Issue #176 본문과 최신 댓글
4. Base repository root/current `main`/open PR
5. 프로젝트 Google Sheet `00_프로젝트_허브!J2:L2`, 최신 `04_누락_충돌_감사`, 최신 `99_변경이력`
6. `PROJECT_CORE.md`
7. `ACTIVE_CONTEXT.md`
8. `DOCUMENT_LIFECYCLE_REGISTRY.md`
9. `CURRENT_IMPLEMENTATION_STATUS.md`
10. PR #175 changed files/CI/review state가 필요할 때만 추가 확인

저장된 SHA나 PID가 current truth와 다르면 먼저 stale state를 교정하고 과거 명령을 그대로 재실행하지 않는다.

## 현재 baseline

```text
OMENWARD_MAIN = 87339f87949c8faea0dfe1482c5d0887a04d94f4
OMENWARD_DEFAULT_BRANCH = main
ACTIVE_RUNTIME_BRANCH = runtime/barracks-role-output-implementation-20260809
ACTIVE_RUNTIME_HEAD = b014a8445423fc9a485fb413429a8127991143e4
PR175 = OPEN / DRAFT / PR_REVISE
ISSUE176 = OPEN
BASE_MAIN = 637dad32c773c56a27d44d847518580848dee493
BASE_BCP011 = IMPLEMENTED / PR231+PR232 MERGED
```

현재 OMENWARD open PR은 #175 하나다. Base의 현재 open backlog에는 #137 Draft, #136 Ready 및 dependency PR들이 있으며 현재 Issue #176 handoff와 직접 같은 Goal의 Base open PR은 확인되지 않았다.

## 승인·권위

```text
DECISION = OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
PARENT_EXECUTOR = #174
FOLLOW_UP_PACKET = #176
IMPLEMENTATION_PR = #175
SAME_APPROVED_SCOPE = REUSE_APPROVAL
NEW_PRODUCT_DECISION = NONE
```

Issue #176의 일곱 runtime/fixture gap은 이미 승인된 동일 package다. 재개할 때 같은 범위에 대해 재승인을 요청하지 않는다.

## 지금까지 완료된 검증

### Current tooling/executor head `b014a844...`

```text
contracts_pr = 69/69 PASS
whitespace = PASS
Godot 4.7.1 import = PASS
headless contract tests = PASS
runtime smoke = PASS
exact-head Actions = 7 SUCCESS / 4 FAILURE
product/Godot-path delta from c30935df to b014a844 = NONE
```

네 failure는 현재 승인된 runtime 전환을 막는 durable transition gate이며 이 handoff에서 수정하지 않는다.

### Last completed runtime evidence head `621ae7ce...`

```text
GUT RED = 10 discovered / 1 pass / 9 intended fail
Godot 4.7.1 import = PASS
GUT GREEN = 10/10 / 52 assertions
existing headless regressions = 13/13 PASS
five FV-labelled smoke scenarios x2 = identical raw outputs
blocked metrics = literal BLOCKED_RUNTIME_OUTPUT
Hera tracked-source delta = NONE
simulation sidecars = NONE
final weighted FV scalar/vector/product numerics = NOT_SELECTED
```

이 evidence는 `621ae7ce80f24b1e5a9d13ba4fc1962bec42dd96`에 대한 과거 evidence이며 adversarial review에서 일곱 package-completeness gap이 발견되었으므로 merge-complete 증거가 아니다.

## 남은 승인된 7개 runtime/fixture gap

1. Priest encouragement: provisional 5s attack-speed +8%, start/end events, support uptime, timing regression.
2. deterministic fallback 보존; 모든 support-role을 일괄 intercept하지 않는다.
3. `flying`은 priority이며 universal permission boundary가 아니다.
4. `cluster` density tie-break는 lane order/unit-id를 사용한다.
5. Giant collector에 `FRONTLINE_SURVIVAL_TIME`, `STRUCTURE_DAMAGE`; unavailable을 fake-zero로 만들지 않는다.
6. registered fixtures FV-PRIEST/MAGE/FLIER/GIANT/COMMON.
7. true `TARGETS_HIT_PER_CAST` + multi-cast coverage.

## 현재 HiGodot blocker까지의 사실

가장 최근 lightweight `session_manage(op=list)` 결과:

```text
session = task7-circuit-placement-screen@63aa
project = C:/Users/user/Documents/GitHub/Ninza/GRIMOIRE-/.worktrees/task7-circuit-placement-screen/
Godot = 4.7.1-stable (official)
editor_pid = 16652
readiness = ready
is_active = true
OMENWARD_SESSION = ABSENT
```

그 직전 exact OMENWARD 재현에서는 GUI PID `29616`과 console PID `10512`가 15초 이상 살아 있었고 exact OMENWARD project root를 대상으로 했으며 GUI PID `29616`에 ESTABLISHED WS9500 연결이 확인됐다. Godot stdout에는 Godot AI/GUT/OMENWARD resource loading이 보였고 stderr tail은 비어 있었다.

두 증거가 몇 분 떨어져 있으므로 현재 판정은 다음이다.

```text
RECOVERABLE_HIGODOT_REGISTRY_OMISSION_AFTER_RECENT_LIVE_WS
SAME_SERVER_HANDSHAKE_REGISTRATION_FAILURE = NOT_YET_CONFIRMED
```

## 재개 시 첫 실행 — full executor보다 먼저

한 시점에서 다음 네 가지를 묶어 read-only로 확인한다.

1. PID `29616`이 여전히 존재하는지와 exact OMENWARD `--editor --path` command line.
2. PID `29616`이 WS9500 ESTABLISHED connection을 소유하는지.
3. 최근 Godot-AI connection/handshake/auth/4003/reconnect/session 로그.
4. 즉시 `godot-ai session_manage(op=list)` 전체 결과.

판정:

```text
PID29616 live + exact root + WS9500 established + OMENWARD registry absent
=> RECOVERABLE_HIGODOT_SAME_SERVER_HANDSHAKE_REGISTRATION_BLOCKER

PID29616 missing or WS9500 absent
=> current process/transport blocker로 재분류

exact OMENWARD root + PID29616 + Godot4.7.1 session present
=> blocker self-recovered; Issue176 NonInteractive executor 재개
```

## 재개 후 runtime 실행 순서

세션 blocker가 해소된 경우에만:

```text
Issue176 NonInteractive executor
→ exact-project HiGodot/Godot4.7.1 preflight
→ actual GUT RED (>0 tests)
→ HiGodot-only persistent runtime/GUT fixes
→ GUT GREEN
→ existing regressions
→ registered FV fixtures x2 identical raw outputs
→ Hera live QA with tracked-source delta NONE
→ structured READY_TO_COMMIT
→ parent commit/push on runtime branch
```

## 변경 금지·보호 경계

- shared Godot-AI server를 OMENWARD 복구 목적으로 종료하지 않는다.
- 다른 live Godot/GRIMOIRE/urban-legend editor를 OMENWARD 복구 목적으로 종료하지 않는다.
- root-cause evidence 전에 executor/session-selection/product logic을 패치하지 않는다.
- `core.autocrlf`, `.gitattributes`, PowerShell ExecutionPolicy, sandbox/permission, Base worktree gate, Godot version gate를 우회하지 않는다.
- persistent Godot/GDScript/GUT authoring은 HiGodot/Godot AI MCP만 사용한다.
- Hera는 Green 이후 live QA에만 사용하고 tracked-source delta NONE을 요구한다.
- final weighted FV scalar/vector/product numerics를 선택하지 않는다.
- unavailable metric은 숫자 0 대신 literal `BLOCKED_RUNTIME_OUTPUT`을 유지한다.
- simulation CSV `.csv.import`/`.translation` sidecar를 만들지 않는다.

## 현재 중단 사유와 종료 상태

```text
USER_REQUEST = 이 부분부터는 나중에 다시 작업하고 지금은 인수인계 진행
TECHNICAL_WORK_AFTER_REQUEST = STOPPED
RUNTIME_BRANCH_MUTATION_BY_HANDOFF = NONE
PRODUCT_MUTATION_BY_HANDOFF = NONE
HANDOFF_DOCS = SEPARATE_DOCS_ONLY_BRANCH
FULL_EXECUTOR_AFTER_HANDOFF = NOT_RUN
HUMAN_QA = NOT_RUN
```

다음 세션은 사용자가 이전 진단 내용을 다시 설명하도록 요구하지 말고 위 fresh-read 순서로 현재 truth를 재구성한 뒤, 새 사용자 Decision이 없다면 승인된 동일 범위의 first executable diagnostic부터 이어서 진행한다.
