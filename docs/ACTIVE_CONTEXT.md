# [현행] Active Context

```yaml
updated_at: 2026-08-10T12:33:00+09:00
project: OMENWARD / 오멘워드
main_sha: 87339f87949c8faea0dfe1482c5d0887a04d94f4
active_runtime_branch: runtime/barracks-role-output-implementation-20260809
active_runtime_head: b014a8445423fc9a485fb413429a8127991143e4
active_pr: 175
active_issue: 176
handoff_pr: 177
handoff_branch: docs/handoff-pr175-issue176-pause-20260810
work_mode: RUNTIME_IMPLEMENTATION_TRANSITION
current_decision: OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
approval_reuse: SAME_APPROVED_SCOPE_NO_REAPPROVAL
planning_canon: MAIN_CANONICAL_APPROVED_10_OF_10
runtime_package_status: RESUMED_ORCHESTRATION_BLOCKED_EXTERNAL_HIGODOT_OBSERVABILITY
last_known_runtime_blocker: RECOVERABLE_HIGODOT_REGISTRY_OMISSION_AFTER_RECENT_LIVE_WS
current_execution_route_blocker: BLOCKED_UNVERIFIED_LOCAL_HIGODOT_SAME_SNAPSHOT_DIAGNOSTIC_UNAVAILABLE
product_mutation_after_b014: NONE
human_qa_after_b014: NOT_RUN
full_issue176_child_after_b014: NOT_RUN
```

## 현재 권위

- OMENWARD `main`은 `87339f87949c8faea0dfe1482c5d0887a04d94f4`로 유지된다.
- 승인된 runtime 구현 권위는 Draft PR #175 / Issue #176이다. PR #175 head `b014a8445423fc9a485fb413429a8127991143e4`는 handoff/Base-learning bookkeeping 때문에 변경하지 않는다.
- PR #177은 continuation locator이며 `REFERENCE_ONLY_HANDOFF / DO_NOT_MERGE_NOW`다. 병합하면 `main`이 전진하여 보존 중인 PR #175 exact head가 behind가 되므로 현재 병합하지 않는다.
- `HANDOFF_CONTEXT.md`의 11:57 KST checkpoint는 당시 사실을 보존하는 handoff snapshot/locator로 읽고, 이 `ACTIVE_CONTEXT.md`를 현재 live continuation router로 사용한다.

## 진행 상태

```text
COMPLETED_VERIFIED
- PR175 executor content-identical dirty gate recovery at b014a844
- contracts_pr 69/69 PASS at b014a844
- whitespace PASS at b014a844
- Godot 4.7.1 import PASS at b014a844
- headless contracts PASS at b014a844
- runtime smoke PASS at b014a844

IN_PROGRESS
- Issue #176의 승인된 7개 runtime/fixture gap

BLOCKED_UNVERIFIED
- current agent environment cannot inspect the user's Windows Godot PID/socket/Godot-AI registry or invoke the required HiGodot persistent-authoring route
- therefore the mandatory same-snapshot local diagnostic cannot be truthfully executed here

LAST_KNOWN_LOCAL_TECHNICAL_BOUNDARY
- exact OMENWARD GUI PID29616 + console PID10512 were recently proven live on the exact project root
- PID29616 had ESTABLISHED WS9500
- a later session_manage(op=list) returned only GRIMOIRE task7 PID16652 and omitted OMENWARD
- evidence was separated by minutes, so SAME_SERVER_HANDSHAKE_REGISTRATION_FAILURE is not proven

READY_NEXT_WHEN_HIGODOT_LOCAL_OBSERVABILITY_IS_AVAILABLE
- same-snapshot process + WS9500 + Godot-AI handshake/auth/reconnect log + immediate session_manage list
```

## Issue #176 승인된 7개 gap

1. Priest encouragement: provisional 5s attack-speed +8%, start/end events, support uptime, timing regression.
2. Preserve deterministic fallback instead of intercepting every support-role unit.
3. `flying` is priority, not a universal target permission boundary.
4. `cluster` density tie-break uses lane order/unit-id semantics.
5. Giant collectors: `FRONTLINE_SURVIVAL_TIME` and `STRUCTURE_DAMAGE`, without fake-zero blocked values.
6. Registered deterministic fixtures: FV-PRIEST/MAGE/FLIER/GIANT/COMMON.
7. True `TARGETS_HIT_PER_CAST` semantics with multi-cast coverage.

## Base current / concurrency

```yaml
base_main_seen: 49f6190b9b5a535ceb7986755c1b68b221754cf5
base_latest_merged_proposal: BCP-2026-012-serial-fiction-canon-migration-debt
base_open_same_goal_proposal_pr: 235
base_open_same_goal_proposal_id: BCP-2026-013-post-merge-continuation-state-reconciliation
base_same_goal_state: CONCURRENT_SAME_GOAL
base_existing_solution_verdict: ABSORB / REUSE_EXISTING_BCP
new_base_bcp_from_omenward: NO
base_proposal_branch_owned_by_other_project: PRESERVE_READ_ONLY
base_implementation_authority_in_this_stage: NOT_GRANTED_IN_THIS_STAGE
other_project_changes_preserved: true
```

Base PR #235는 Ninja Survival 출처의 proposal-only PR이며 live continuation state의 post-merge reconciliation을 기존 `maintaining-project-context-and-handoff` owner에 흡수하는 같은 공용 Goal을 이미 다룬다. OMENWARD는 중복 BCP를 만들거나 다른 프로젝트의 #235 branch/PR을 수정·병합하지 않는다.

OMENWARD가 추가로 제공하는 reusable evidence는 다음 use-condition이다: continuation locator PR 자체를 병합하면 active exact-head implementation PR이 stale/behind가 되는 경우, locator를 `REFERENCE_ONLY / DO_NOT_MERGE`로 유지하고 fresh GitHub truth를 우선한다. 이 증거는 프로젝트 Sheet/Handoff에 연결하고 BCP #235의 향후 검토 근거로만 보존한다.

## Base / Sheet 충돌

Google Sheet의 12:06 KST handoff checkpoint는 Base main을 `637dad32...`로 기록하고 있으나 fresh Base `main`은 `49f6190...`로 전진했다. OMENWARD runtime SHA/PR 상태는 Sheet와 일치한다. 따라서 이번 checkpoint에서 Sheet의 Base baseline/concurrency locator만 최신화해야 한다.

## 재개 시 첫 실행

1. OMENWARD `main`, PR #175, PR #177, Issue #176을 fresh-read한다.
2. Base `main`, open proposal PR, Proposal Registry를 fresh-read한다.
3. Google Sheet hub/latest audit/latest history/Base candidate row를 fresh-read한다.
4. full executor보다 먼저 한 시점에서 exact OMENWARD process/command line + ESTABLISHED WS9500 + Godot-AI connection/handshake/auth/4003/reconnect/session log + immediate `session_manage(op=list)`를 확인한다.
5. exact OMENWARD session present → Issue #176 NonInteractive executor 재개.
6. live exact OMENWARD + WS9500 + registry omission → `RECOVERABLE_HIGODOT_SAME_SERVER_HANDSHAKE_REGISTRATION_BLOCKER`로 확정하고 handshake/registration만 진단.
7. process/WS missing → current process/transport blocker로 재분류하고 사유는 검증 전 추정하지 않는다.

## 보호 경계

- shared Godot-AI server나 다른 프로젝트 editor를 OMENWARD 복구 목적으로 종료하지 않는다.
- root-cause evidence 전에 executor/session-selection logic을 패치하지 않는다.
- `core.autocrlf`, `.gitattributes`, PowerShell ExecutionPolicy, sandbox/permission, Godot version gate를 변경/우회하지 않는다.
- persistent Godot/GDScript/GUT authoring은 HiGodot/Godot AI MCP만 사용한다.
- GUT RED→GREEN 뒤에만 Hera live QA를 실행하고 tracked-source delta NONE을 요구한다.
- FV 최종 weighted scalar/vector/product numerics를 선택하지 않는다.
- unavailable metric은 숫자 0이 아니라 literal `BLOCKED_RUNTIME_OUTPUT`을 유지한다.
