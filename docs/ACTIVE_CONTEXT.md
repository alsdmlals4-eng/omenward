# [현행] Active Context

```yaml
updated_at: 2026-08-10T13:15:00+09:00
project: OMENWARD / 오멘워드
main_sha: 87339f87949c8faea0dfe1482c5d0887a04d94f4
active_runtime_branch: runtime/barracks-role-output-implementation-20260809
active_runtime_head: bde85549560fca90f7aa25fc4842bc0a3afb92e7
active_pr: 175
active_issue: 176
handoff_pr: 177
handoff_branch: docs/handoff-pr175-issue176-pause-20260810
work_mode: RUNTIME_IMPLEMENTATION_TRANSITION
current_decision: OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
approval_reuse: SAME_APPROVED_SCOPE_NO_REAPPROVAL
planning_canon: MAIN_CANONICAL_APPROVED_10_OF_10
runtime_package_status: TRANSITION_CI_GREEN_RUNTIME_GAPS_BLOCKED_EXTERNAL_HIGODOT_OBSERVABILITY
last_known_runtime_blocker: RECOVERABLE_HIGODOT_REGISTRY_OMISSION_AFTER_RECENT_LIVE_WS
current_execution_route_blocker: BLOCKED_UNVERIFIED_LOCAL_HIGODOT_SAME_SNAPSHOT_DIAGNOSTIC_UNAVAILABLE
godot_product_mutation_after_b014: NONE
non_godot_ci_tool_test_reconciliation_after_b014: COMPLETE
exact_head_actions_bde85549: 11_SUCCESS_0_FAILURE
human_qa_after_bde85549: NOT_RUN
full_issue176_child_after_bde85549: NOT_RUN
```

## 현재 권위

- OMENWARD `main`은 `87339f87949c8faea0dfe1482c5d0887a04d94f4`로 유지된다.
- 승인된 runtime 구현 권위는 Draft PR #175 / Issue #176이다. 현재 PR #175 exact head는 `bde85549560fca90f7aa25fc4842bc0a3afb92e7`이다.
- PR #177은 continuation locator이며 `REFERENCE_ONLY_HANDOFF / DO_NOT_MERGE_NOW`다. 이 PR은 fresh GitHub/Sheet truth보다 높은 권위가 아니다.
- `HANDOFF_CONTEXT.md`의 2026-08-10 11:57 KST checkpoint는 당시 사실을 보존하는 historical handoff snapshot이다. 이 `ACTIVE_CONTEXT.md`는 현재 live continuation router다.

## 진행 상태

```text
COMPLETED_VERIFIED
- b014a844 executor content-identical dirty gate recovery
- b014a844 contracts_pr 69/69 PASS
- b014a844 whitespace PASS
- b014a844 Godot 4.7.1 import PASS
- b014a844 headless contracts PASS
- b014a844 runtime smoke PASS
- bde85549 historical functional-value review transition mismatch CLEARED
- bde85549 Base v9 protected-path transition mismatch CLEARED
- bde85549 Project Base Adapter generated-view/runtime-transition mismatch CLEARED
- bde85549 active integrated v4.4 planning-only transition mismatch CLEARED
- bde85549 exact-head GitHub Actions 11 SUCCESS / 0 FAILURE

IN_PROGRESS
- Issue #176의 승인된 7개 runtime/fixture gap

BLOCKED_UNVERIFIED
- current agent environment cannot inspect the user's Windows Godot PID/socket/Godot-AI registry or invoke the required HiGodot persistent-authoring route
- therefore the mandatory same-snapshot local diagnostic and persistent Godot/GDScript/GUT authoring cannot be truthfully executed here

LAST_KNOWN_LOCAL_TECHNICAL_BOUNDARY
- exact OMENWARD GUI PID29616 + console PID10512 were recently proven live on the exact project root
- PID29616 had ESTABLISHED WS9500
- a later session_manage(op=list) returned only GRIMOIRE task7 PID16652 and omitted OMENWARD
- evidence was separated by minutes, so SAME_SERVER_HANDSHAKE_REGISTRATION_FAILURE is not proven

READY_NEXT_WHEN_HIGODOT_LOCAL_OBSERVABILITY_IS_AVAILABLE
- same-snapshot current exact process + WS9500 + Godot-AI handshake/auth/reconnect log + immediate session_manage list
```

## b014 → bde transition CI reconciliation

PR #175의 이전 exact head `b014a844...`에서는 GitHub Actions가 7 SUCCESS / 4 FAILURE였고, 네 실패는 실제 runtime gap이 아니라 과거 planning/transition contract가 승인된 runtime 변경을 stale하게 해석한 문제였다.

같은 승인 범위 안에서 non-Godot CI/tool/test 보수만 수행했다.

- `tests/python/test_barracks_functional_value_combat_numerics_review.py`: runtime을 전체 미구현으로 주장하던 historical assertion을 현재 partial runtime transition에 맞게 보수.
- `tools/validate_runtime_transition_scope.py` + `tests/python/test_runtime_transition_scope.py`: 승인된 barracks runtime protected-path surface만 fail-closed로 허용하는 전환 판정 추가.
- Base v9 / Project Base Adapter / active v4.4 workflow는 이 판정을 사용해 해당 승인 runtime transition만 통과시키고, 다른 protected/unrelated delta는 계속 실패시킨다.
- generated compatibility view의 변경되지 않은 legacy source hash 두 개를 검증값으로 복원했다.

결과:

```text
PR175_HEAD = bde85549560fca90f7aa25fc4842bc0a3afb92e7
TRIGGERED_ACTIONS = 11
SUCCESS = 11
FAILURE = 0
GODOT_PRODUCT_PATH_MUTATION_BY_THIS_RECONCILIATION = NONE
ISSUE176_RUNTIME_GAPS_CLOSED_BY_THIS_RECONCILIATION = 0
```

CI Green은 Issue #176 runtime 구현 완료를 뜻하지 않는다. 실제 제품/runtime gap 7개와 HiGodot/GUT/Hera 검증은 그대로 남는다.

## Issue #176 승인된 7개 gap

1. Priest encouragement: provisional 5s attack-speed +8%, start/end events, support uptime, timing regression.
2. Preserve deterministic fallback instead of intercepting every support-role unit.
3. `flying` is priority, not a universal target permission boundary.
4. `cluster` density tie-break uses lane order/unit-id semantics.
5. Giant collectors: `FRONTLINE_SURVIVAL_TIME` and `STRUCTURE_DAMAGE`, without fake-zero blocked values.
6. Registered deterministic fixtures: FV-PRIEST/MAGE/FLIER/GIANT/COMMON.
7. True `TARGETS_HIT_PER_CAST` semantics with multi-cast coverage.

## Base current / project-named BCP evidence

```yaml
base_main_seen: d5cfcfa96fcf33bf7e01dc617d7f68e8d5bbbeaf
base_existing_solution: BCP-2026-013-post-merge-continuation-state-reconciliation
base_existing_solution_pr: 235
base_existing_solution_pr_state: MERGED_PROPOSAL_ONLY
base_existing_solution_merge_sha: 3ff790116bc08f49e126cd286ec453bf6e46376e
base_existing_solution_verdict: REUSE_BCP_2026_013
project_named_evidence_title: BCP - OMENWARD
project_named_evidence_pr: 243
project_named_evidence_pr_state: OPEN_DRAFT
project_named_evidence_branch_creation_base: c14e4e841171a98e2471cbe7ff94afe4d55501fb
project_named_evidence_refreshed_base: d5cfcfa96fcf33bf7e01dc617d7f68e8d5bbbeaf
project_named_evidence_head: 0fc5c6d193c26f1cc6145e29b5dbfe1141c9ded8
project_named_evidence_scope: ONE_FILE_PROPOSAL_ONLY
project_named_evidence_validation: SUCCESS
base_race_change: PR244_BCP014_WORDING_PROPOSAL_ONLY_NONOVERLAP
new_canonical_bcp_from_omenward: NO
proposal_registry_change_from_omenward: NONE
base_implementation_authority_in_this_stage: NOT_GRANTED_IN_THIS_STAGE
other_project_changes_preserved: true
```

Base PR #235의 BCP-013은 이미 proposal-only로 main에 병합되었다. 사용자 규칙에 따라 OMENWARD의 human/project evidence는 `BCP - OMENWARD`로 이름 붙였고, 새 canonical BCP를 만들지 않고 기존 BCP-013 evidence에 연결했다.

Base Draft PR #243의 정확한 diff는 다음 한 파일뿐이다.

`[수정제안서]/BCP-2026-013-post-merge-continuation-state-reconciliation/evidence/BCP-OMENWARD.md`

PR #243 생성 직후 Base main은 `c14e4e84...`에서 `d5cfcfa9...`로 전진했다. 새 main 변화는 PR #244의 `[수정제안서]/BCP-2026-014-handoff-machine-consumer-compatibility-closeout/PROPOSAL.md` 한 파일 proposal-only 문구 정정이며 PR #243의 BCP-013 evidence 파일과 경로가 겹치지 않았다. 현재 main을 PR #243 branch에 비충돌 통합한 뒤에도 diff는 BCP-OMENWARD evidence 한 파일이고 exact-head Base validation은 SUCCESS다.

OMENWARD가 추가로 제공하는 reusable use-condition은 다음이다: continuation locator 자체를 병합하면 active exact-head implementation PR이 불필요하게 stale/behind가 되는 경우 locator를 `REFERENCE_ONLY / DO_NOT_MERGE`로 유지하고, live router는 fresh repository truth에서 reconcile할 수 있다.

Base PR #243은 active Base implementation을 승인하거나 수행하지 않는다. 다른 프로젝트의 proposal PR/Registry를 수정·병합하지 않는다.

## 재개 시 첫 실행

1. OMENWARD `main`, PR #175, PR #177, Issue #176을 fresh-read한다.
2. Base `main`, BCP-013 상태, open proposal PR, `BCP - OMENWARD` PR #243을 fresh-read한다.
3. Google Sheet hub/latest audit/latest history/Base candidate row를 fresh-read한다.
4. full executor보다 먼저 한 시점에서 current exact OMENWARD process/command line + ESTABLISHED WS9500 + Godot-AI connection/handshake/auth/4003/reconnect/session log + immediate `session_manage(op=list)`를 확인한다.
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
