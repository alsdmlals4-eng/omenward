# Phase C C0 Toolchain CI Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: use superpowers TDD, systematic debugging, and verification-before-completion while executing this plan.

**Decision:** `OMW-DEC-20260811-OPS-PHASE-C-C0-PREFLIGHT-V1`

**Goal:** Re-establish a fail-closed Phase C C0 validation path after the direct-main Godot AI 3.1.4 update, validate the current repository/toolchain baseline, reconcile stale historical-vs-current tool tests, and leave PR175 blocked from runtime continuation until current-main revalidation plus live local HiGodot session evidence exists.

## C0 entry truth

```text
BASE_MAIN_AT_C0_ENTRY = 8e7d85b1b1272002a8086c502a41073888cb3318
OMENWARD_MAIN_AT_C0_ENTRY = 14b0d942e071dc6e823f48c29ac79f0978477d85
VALIDATED_PHASE_B_PARENT = 91f4aa98c0dea5307c2482aa0f403ce7dd115e40
DIRECT_MAIN_GODOT_AI_UPDATE = TRUE
DIRECT_MAIN_PUSH_WORKFLOW_RUNS = 0
DIRECT_MAIN_COMMIT_STATUSES = 0
GODOT_AI_PROJECT_VERSION = 3.1.4
GODOT_AI_UPSTREAM_LATEST_RELEASE = v3.1.4
GUT_PROJECT_VERSION = 9.7.1
GODOT_PROJECT_FEATURE_LINE = 4.7
LOCAL_LIVE_GODOT_AI_SESSION = UNVERIFIED_IN_THIS_ENVIRONMENT
PR175 = OPEN_DRAFT
PR175_MERGE_BASE = 87339f87949c8faea0dfe1482c5d0887a04d94f4
PR175_AHEAD_CURRENT_MAIN = 43
PR175_BEHIND_CURRENT_MAIN = 14
```

The prior `3.1.3` approval/sync owner remains historical evidence for that exact sync. It is not rewritten. Current project source and upstream release truth are separately validated as 3.1.4.

## Protection boundary

- No gameplay `scripts/`, `scenes/`, `data/`, `assets/`, `addons/`, `resources/`, or `project.godot` mutation in PR190.
- Workflow path text may reference `addons/**`; the PR itself must not mutate an addon file.
- No final FV, parameter vector, or product numerics.
- No PR175 merge or runtime-resume claim from repository CI alone.

## Exact C0 GitHub surface

The final fail-closed C0 surface is exactly eight files:

1. `.github/workflows/validate-omenward-core.yml`
2. `docs/reviews/PHASE_C_C0_PREFLIGHT_2026-08-11.md`
3. `docs/superpowers/plans/2026-08-11-phase-c-c0-toolchain-ci-gate.md`
4. `tests/python/test_phase_c_c0_toolchain_ci_gate.py`
5. `tests/python/test_tool_state_user_approval_remote_sync.py`
6. `tools/validate_ci_usage_contract.py`
7. `tests/python/test_canon_freshness_v45_scope.py`
8. `tools/validate_canon_freshness_v45_scope.py`

## Task 1 — TDD addon-trigger regression

- [x] Create dedicated `tests/python/test_phase_c_c0_toolchain_ci_gate.py`.
- [x] Require exactly two `- "addons/**"` path entries: PR + main push.
- [x] Require validator mutation failure if one addon trigger is missing.
- [x] Verify RED on PR190: both addon-trigger tests failed on the pre-fix workflow.
- [x] Confirm same RED run's Godot 4.7.1 import/headless/runtime smoke was Green.

The RED full suite also exposed one pre-existing current-state regression: a durable test incorrectly required the live plugin file to remain 3.1.3 after main had moved to 3.1.4.

## Task 2 — Minimal addon trigger + tool-state reconciliation

- [x] Add `addons/**` once to `pull_request.paths` and once to `push.paths` in Omenward Core.
- [x] Require the two entries in `tools/validate_ci_usage_contract.py`.
- [x] Preserve the 2026-08-09 3.1.3 authority/state assertions as historical exact-sync evidence.
- [x] Change only the current-file assertion to Godot AI 3.1.4; keep GUT 9.7.1 and Hera 1.0.0.
- [x] Verify Omenward Core full PR Python suite Green after the fix.
- [x] Verify Tool State User Approval Remote Sync workflow Green after the split.

## Task 3 — TDD v4.5 C0 exact scope

- [x] Add C0 exact-surface and missing-anchor tests first.
- [x] Verify RED: v4.5 rejected the new C0 paths as unapproved.
- [x] Register `PHASE_C_C0_TOOLCHAIN_GATE_ALLOWED_FILES` and exact required anchors in the v4.5 scope validator.
- [ ] Create the C0 review owner.
- [ ] Require the complete eight-file branch diff to pass the v4.5 scope validator.
- [ ] Confirm active v4.4 accepts the C0 transition by consuming the v4.5 PASS, without widening its historical fallback allowlist.

## Task 4 — Review, Sheet sync, merge gate

- [ ] Record fresh Base, OMENWARD, Sheet, benchmark/tool evidence in `docs/reviews/PHASE_C_C0_PREFLIGHT_2026-08-11.md`.
- [ ] Verify PR190 exact eight-file surface, protected product paths = 0, review threads = 0.
- [ ] Re-read Base/main/open PRs immediately before merge and report races.
- [ ] Sync Google Sheet current hub/work order/current decision/audit/history under the same C0 Decision ID.
- [ ] Bounded Sheet reread must PASS.
- [ ] Require all exact-head PR workflows Green, including Omenward Core full Python suite and Godot 4.7.1 import/headless/runtime smoke.
- [ ] Use expected-head merge only.
- [ ] On merged main, require Omenward Core Ubuntu/Windows × Python 3.11/3.12/3.13 full matrix plus Godot success.
- [ ] Final repository-side classification, absent live local session evidence: `C0_PARTIAL_PASS_REPOSITORY_TOOLCHAIN_VERIFIED_LOCAL_LIVE_SESSION_UNVERIFIED`.

## Next executor boundary

Repository-side C0 completion does not itself resume PR175. The next runtime executor must first obtain same-snapshot local evidence for:

1. exact OMENWARD Godot process and command line;
2. that process's ESTABLISHED WS9500 connection;
3. current Godot AI connection/handshake/auth/4003/reconnect logs;
4. immediate session registry/list result.

Then PR175 must be rebased/revalidated against current main before the seven Issue176 runtime gaps are implemented through the approved HiGodot/GUT/Hera route.