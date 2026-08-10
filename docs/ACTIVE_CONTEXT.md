# [현행] Active Context

```yaml
updated_at: 2026-08-10T14:08:00+09:00
project: OMENWARD / 오멘워드
main_sha: 87339f87949c8faea0dfe1482c5d0887a04d94f4
active_runtime_branch: runtime/barracks-role-output-implementation-20260809
active_runtime_head: bde85549560fca90f7aa25fc4842bc0a3afb92e7
active_pr: 175
active_issue: 176
handoff_pr: 177
handoff_branch: docs/handoff-pr175-issue176-pause-20260810
handoff_disposition: REFERENCE_ONLY_HANDOFF_DO_NOT_MERGE_NOW
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
base_main_seen: 59aadec796260ae200e776af35954174fc5bda46
base_project_evidence: BCP - OMENWARD
base_project_evidence_pr: 243
base_project_evidence_pr_state: MERGED_PROPOSAL_EVIDENCE_ONLY
base_project_evidence_merge_sha: 59aadec796260ae200e776af35954174fc5bda46
base_project_evidence_post_merge_ci: SUCCESS
base_project_evidence_post_merge_run: 31357359735
base_active_implementation_authority: NOT_GRANTED_IN_THIS_STAGE
```

## 현재 권위

- OMENWARD `main`은 `87339f87949c8faea0dfe1482c5d0887a04d94f4`다.
- 승인된 runtime 구현 권위는 Draft PR #175 / Issue #176이다. 현재 PR #175 exact head는 `bde85549560fca90f7aa25fc4842bc0a3afb92e7`이다.
- PR #177은 continuation locator이며 `REFERENCE_ONLY_HANDOFF / DO_NOT_MERGE_NOW`다. 이 PR의 자체 head SHA는 문서에 고정하지 않고 fresh GitHub truth를 사용한다.
- `HANDOFF_CONTEXT.md`의 2026-08-10 11:57 KST checkpoint는 당시 사실을 보존하는 historical snapshot이다. 이 `ACTIVE_CONTEXT.md`가 mutable live continuation router다.
- Base project evidence `BCP - OMENWARD`는 Base PR #243으로 `main`에 proposal-evidence-only로 병합되었다. 이것은 BCP-013 active 구현 승인이나 Base active behavior 변경을 뜻하지 않는다.

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
- Base PR243 BCP - OMENWARD exact-head validation SUCCESS
- Base PR243 squash merge SUCCESS -> 59aadec796260ae200e776af35954174fc5bda46
- Base post-merge push run 31357359735 SUCCESS
- Base main readback contains BCP-OMENWARD.md

IN_PROGRESS
- Issue #176의 승인된 7개 runtime/fixture gap

BLOCKED_UNVERIFIED
- current agent environment cannot inspect the user's Windows Godot PID/socket/Godot-AI registry or invoke the required HiGodot persistent-authoring route
- therefore mandatory same-snapshot local diagnostic and persistent Godot/GDScript/GUT authoring remain unavailable here

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

- `tests/python/test_barracks_functional_value_combat_numerics_review.py`: runtime을 전체 미구현으로 주장하던 historical assertion을 current partial runtime transition에 맞게 보수.
- `tools/validate_runtime_transition_scope.py` + `tests/python/test_runtime_transition_scope.py`: 승인된 barracks runtime protected-path surface만 fail-closed로 허용하는 전환 판정 추가.
- Base v9 / Project Base Adapter / active v4.4 workflow는 이 판정을 사용해 해당 승인 runtime transition만 통과시키고, 다른 protected/unrelated delta는 계속 실패시킨다.
- generated compatibility view의 변경되지 않은 legacy source hash 두 개를 검증값으로 복원했다.

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

## Base current / `BCP - OMENWARD`

```yaml
base_main_seen: 59aadec796260ae200e776af35954174fc5bda46
base_existing_solution: BCP-2026-013-post-merge-continuation-state-reconciliation
base_existing_solution_pr: 235
base_existing_solution_pr_state: MERGED_PROPOSAL_ONLY
base_existing_solution_merge_sha: 3ff790116bc08f49e126cd286ec453bf6e46376e
base_existing_solution_verdict: REUSE_BCP_2026_013
project_named_evidence_title: BCP - OMENWARD
project_named_evidence_pr: 243
project_named_evidence_pr_state: MERGED_PROPOSAL_EVIDENCE_ONLY
project_named_evidence_premerge_head: f4f42c45342b88072852baa36a65b643890d72a7
project_named_evidence_merge_sha: 59aadec796260ae200e776af35954174fc5bda46
project_named_evidence_scope: ONE_FILE_PROPOSAL_ONLY
project_named_evidence_premerge_validation: SUCCESS
project_named_evidence_post_merge_validation: SUCCESS
project_named_evidence_post_merge_run: 31357359735
proposal_registry_change_from_omenward: NONE
new_canonical_bcp_from_omenward: NO
base_implementation_authority_in_this_stage: NOT_GRANTED_IN_THIS_STAGE
```

`BCP - OMENWARD`는 새 canonical BCP가 아니라 기존 BCP-013의 프로젝트명 corroborating evidence다. 병합된 정확한 경로는 다음이다.

`[수정제안서]/BCP-2026-013-post-merge-continuation-state-reconciliation/evidence/BCP-OMENWARD.md`

PR #243은 최신 Base main `16af66ff...`까지 비충돌 동기화한 뒤 exact-head validation을 통과했고, expected-head 고정 squash merge로 `59aadec...`가 되었다. post-merge push run `31357359735`도 SUCCESS이며 main readback에서 파일 존재를 확인했다.

`PROPOSAL_REGISTRY.json`과 Base active Skill/Method/Template/Test/Workflow는 이 OMENWARD evidence 병합으로 변경되지 않았다. BCP-013 active implementation은 별도 `APPROVED_FOR_IMPLEMENTATION`과 approval ref가 필요하다.

## 재개 시 첫 실행

1. OMENWARD `main`, PR #175, PR #177, Issue #176을 fresh-read한다.
2. Base `main`, BCP-013 상태, open proposal PR, `BCP - OMENWARD` main evidence를 fresh-read한다.
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
