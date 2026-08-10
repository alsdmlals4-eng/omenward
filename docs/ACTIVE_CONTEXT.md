# [현행] Active Context

```yaml
updated_at: 2026-08-10T11:57:00+09:00
project: OMENWARD / 오멘워드
main_sha: 87339f87949c8faea0dfe1482c5d0887a04d94f4
active_runtime_branch: runtime/barracks-role-output-implementation-20260809
active_runtime_head: b014a8445423fc9a485fb413429a8127991143e4
active_pr: 175
active_issue: 176
handoff_branch: docs/handoff-pr175-issue176-pause-20260810
work_mode: RUNTIME_IMPLEMENTATION_TRANSITION
current_decision: OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
approval_reuse: SAME_APPROVED_SCOPE_NO_REAPPROVAL
planning_canon: MAIN_CANONICAL_APPROVED_10_OF_10
runtime_package_status: USER_DEFERRED_FOR_HANDOFF
current_blocker: RECOVERABLE_HIGODOT_REGISTRY_OMISSION_AFTER_RECENT_LIVE_WS
product_mutation_after_b014: NONE
human_qa_after_b014: NOT_RUN
full_issue176_child_after_b014: NOT_RUN
```

## 현재 작업 기준

사용자가 2026-08-10 11:57 KST에 Issue #176의 HiGodot 진단부터 이후 runtime 실행을 나중에 다시 하기로 하고 인수인계 전환을 요청했다. 이 중지는 제품 방향 변경이 아니며 기존 Decision과 승인 범위를 그대로 보존한다.

현재 제품/runtime 작업의 권위는 Draft PR #175와 follow-up Issue #176이다. PR #175의 runtime head `b014a8445423fc9a485fb413429a8127991143e4`는 인수인계 작업에서 수정하지 않는다. 이 문서 동기화는 별도 docs-only branch에서만 수행한다.

## 완료·진행·차단 분류

```text
COMPLETED_VERIFIED
- executor content-identical dirty gate recovery at b014a844
- fast contracts_pr 69/69 at b014a844
- Godot 4.7.1 import PASS at b014a844
- headless contract tests PASS at b014a844
- runtime smoke PASS at b014a844

COMPLETED_NOT_MERGED
- PR #175 remains Draft and open
- last completed runtime evidence at 621ae7ce80f24b1e5a9d13ba4fc1962bec42dd96 is evidence only, not merge-complete

IN_PROGRESS
- Issue #176 approved seven runtime/fixture gaps remain to be closed through HiGodot

BLOCKED
- RECOVERABLE_HIGODOT_REGISTRY_OMISSION_AFTER_RECENT_LIVE_WS
- latest session_manage(op=list) returned only GRIMOIRE task7 `task7-circuit-placement-screen@63aa`, Godot 4.7.1, editor PID 16652, ready/active
- no OMENWARD session was present
- immediately prior reproduction had OMENWARD GUI PID 29616 alive on exact project root with ESTABLISHED WS9500
- those proofs were minutes apart, so SAME_SERVER_HANDSHAKE_REGISTRATION_FAILURE is not yet claimed

READY_NEXT_WHEN_RESUMED
- one combined read-only same-snapshot process + WS9500 + Godot-AI connection log + immediate session_manage list diagnostic
```

## Issue #176 승인된 7개 gap

1. Priest encouragement: provisional 5s attack-speed +8%, start/end events, support uptime, timing regression.
2. Preserve deterministic fallback instead of intercepting every support-role unit.
3. `flying` is priority, not a universal target permission boundary.
4. `cluster` density tie-break uses lane order/unit-id semantics.
5. Giant collectors: `FRONTLINE_SURVIVAL_TIME` and `STRUCTURE_DAMAGE`, without fake-zero blocked values.
6. Registered deterministic fixtures: FV-PRIEST/MAGE/FLIER/GIANT/COMMON.
7. True `TARGETS_HIT_PER_CAST` semantics with multi-cast coverage.

## 검증 경계

```text
PR175_HEAD = b014a8445423fc9a485fb413429a8127991143e4
PR175_STATE = OPEN_DRAFT_PR_REVISE
EXACT_HEAD_ACTIONS = 7_SUCCESS_4_FAILURE
CONTRACTS_PR = 69_OF_69_PASS
GODOT_4_7_1_IMPORT = PASS
HEADLESS_CONTRACTS = PASS
RUNTIME_SMOKE = PASS
LAST_COMPLETED_RUNTIME_EVIDENCE_HEAD = 621ae7ce80f24b1e5a9d13ba4fc1962bec42dd96
HERA_TRACKED_SOURCE_DELTA_AT_621AE7CE = NONE
REGISTERED_ISSUE176_FIXTURE_RUN = NOT_RUN
HUMAN_QA = NOT_RUN
FINAL_WEIGHTED_FV_NUMERICS = FORBIDDEN_NOT_SELECTED
BLOCKED_METRICS = KEEP_LITERAL_BLOCKED_RUNTIME_OUTPUT
```

네 개의 exact-head transition failures는 historical combat-numerics incompleteness assertion, Base v9 protected-path transition gate, stale/generated Project Base Adapter transition, integrated v4.4 planning-only gate다. 이 인수인계 작업은 그 네 failure를 수정하지 않는다.

## Base 현재 상태

```text
BASE_MAIN = 637dad32c773c56a27d44d847518580848dee493
BCP_011_PR231 = MERGED
BCP_011_PR232 = MERGED
BCP_011 = IMPLEMENTED
BASE_OPEN_RELEVANT_TO_CURRENT_HANDOFF = NONE_IDENTIFIED
BASE_OPEN_OTHER = PR137_DRAFT / PR136_READY / dependency PR backlog
```

Base 최신 BCP-011 변경은 OMENWARD Issue #176의 승인된 runtime 범위와 충돌하지 않는다.

## 재개 시 첫 실행

1. GitHub에서 OMENWARD `main`, PR #175 head/state, Issue #176, Base `main`을 fresh-read한다.
2. Google Sheet `00_프로젝트_허브!J2:L2`, 최신 `04_누락_충돌_감사`, 최신 `99_변경이력`을 fresh-read한다.
3. 이 문서와 `HANDOFF_CONTEXT.md`의 저장 SHA가 current GitHub truth와 다르면 먼저 stale state를 교정한다.
4. full executor를 먼저 실행하지 않는다.
5. PID 29616의 현재 존재/정확 command line, PID 29616의 ESTABLISHED WS9500, Godot-AI connection/handshake/auth/reconnect 로그, 즉시 `session_manage(op=list)`를 한 스냅샷으로 확인한다.
6. exact OMENWARD session이 나타나면 Issue #176 NonInteractive executor를 재개한다.
7. PID 29616 live + WS9500 established + registry omission이 동시에 확인되면 `RECOVERABLE_HIGODOT_SAME_SERVER_HANDSHAKE_REGISTRATION_BLOCKER`로 확정하고 handshake/auth/registration 경계만 진단한다.
8. process 또는 WS가 사라졌다면 해당 process/transport blocker로 재분류한다.

## 보호 경계

- shared Godot-AI server나 다른 프로젝트 editor를 OMENWARD 복구 목적으로 종료하지 않는다.
- executor/session matching logic을 증거 없이 패치하지 않는다.
- `core.autocrlf`, `.gitattributes`, PowerShell ExecutionPolicy, sandbox/permission, version gate 우회를 변경하지 않는다.
- persistent Godot/GDScript/GUT authoring은 HiGodot/Godot AI MCP를 통해서만 수행한다.
- GUT RED→GREEN 뒤에만 Hera live QA를 실행하고 tracked-source delta NONE을 요구한다.
- FV 최종 weighted scalar/vector/product numerics를 선택하지 않는다.
- unavailable metric은 숫자 0이 아니라 literal `BLOCKED_RUNTIME_OUTPUT`을 유지한다.
