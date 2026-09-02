# OMENWARD Approved Protected-Change CI Routing Incident — 2026-08-31

```yaml
incident_id: OMW-CI-20260831-APPROVED-PROTECTED-CHANGE-ROUTING
status: LOCAL_AND_REMOTE_CI_PASS__REPAIR_HEAD_RECORDED
scope: PR_257_APPROVED_SINGLE_FRONT_IMPLEMENTATION
approval_reference: USER_CONTINUATION_AND_CLEANUP_AUTHORIZATION_2026-08-31
protected_baseline: 9a67a267a69c80fba6f25d5a37e360a15dcc2419
base_gate_commit: 928f8ed44f2f8f84859834b229cb8321d716e9f6
base_gate_role: APPROVED_PROTECTED_CHANGE_RECONCILIATION_ONLY
runtime_evidence: NOT_APPLICABLE
human_evidence: NOT_APPLICABLE
remote_ci_evidence: PASS
remote_ci_head: 0b045c5ddeb1193333565cc11438acd120796339
rollback: REVERT_THIS_CI_ROUTING_CHANGE_FROM_PR_257
```

## What failed before the repair

PR #257 contains approved Godot source, scene, data, and asset changes. Three
historical planning/document workflows rejected the entire pull request solely
because protected product paths existed. Their fail-closed behavior was valid
for documentation-only scopes, but they had no route for a product change
already covered by an exact `PROJECT_PROTECTED_CHANGE_APPROVAL` manifest.

The first Base commit that introduced the approved protected-change command
(`4ec410e6`) was tested and rejected for this project because its older
generated-artifact and Sheet-evidence rules no longer matched current
Omenward. That candidate is not used.

## Adopted repair

`tools/validate_approved_protected_change_ci.py` owns only pull-request-local
manifest selection:

1. no protected path changed: leave historical documentation workflows in
   charge;
2. protected paths changed: require exactly one changed approval manifest;
3. invoke Base's exact approval validator with the immutable PR baseline;
4. preserve all unrelated Base-contract failures as fatal.

`validate-base-v9-adoption.yml` pins Base commit `928f8ed4`, the earliest
tested compatible revision, for this narrow outer gate. It does not change
the project's adopted Base v9.4.3 release lock. The historical v4.4 and v4.5
workflows continue to run their own tests, but skip only their final
documentation-surface assertion when the approved protected-change gate is
the actual owner.

## Local evidence

| Check | Result | Meaning |
| --- | --- | --- |
| Bridge fixture: exact manifest | PASS | Base gate receives the sole changed manifest and trusted baseline. |
| Bridge fixture: no manifest | PASS | Fails before the Base gate; no bypass. |
| Bridge fixture: two manifests | PASS | Fails closed as ambiguous. |
| Bridge fixture: docs-only | PASS | Does not substitute for historical document validation. |
| Base `928f8ed4` exact gate against PR #257 | PASS | Current approval manifest and generated artifacts reconcile. |
| Remote GitHub workflow run at `0b045c5d` | PASS | `ci-gate`, `adversarial-gate`, v4.4/v4.5 routing, and Godot all passed on PR #257. |

## Retention and learning

The historical v4.4/v4.5 validators remain retained as documentation-scope
contracts. The repair removes only their false ownership claim over an
approved protected implementation. Future protected implementation PRs must
still carry one exact changed approval manifest; multiple, missing, stale, or
non-exact manifests fail closed.
