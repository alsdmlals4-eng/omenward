# OMENWARD Incident · v6 planning-lock Godot CI 종료 오류 재검증

```yaml
incident_id: OMW-INC-20260829-CI-GODOT-TEARDOWN-RERUN-01
date: 2026-08-29
class: PROJECT_INCIDENT / CI_VALIDATION
status: RESOLVED_BY_SAME_HEAD_RERUN__NO_PRODUCT_CHANGE
affected_scope: PR_253_DOCUMENTATION_AND_PLANNING_LOCK_ONLY
initial_evidence: GitHub Actions run 33186479230 / godot job 98900684192 / exit 134
resolution_evidence: GitHub Actions run 33186479230 rerun / godot job 98901645155 / success
owner: docs/reviews/ADVERSARIAL_OPEN_BATTLEFIELD_V6_VISUAL_LOCK_REVIEW_2026-08-29.md
```

## Incident

PR #253의 첫 Godot job은 Godot 4.7.1 headless `--editor --quit` import가 완료된 뒤, Hera 종료와 함께 `double free or corruption (out)` 및 core dump(exit 134)로 끝났다. 이 PR은 `project.godot`, `scenes/`, `scripts/`, `assets/`, `data/`, `addons/`를 변경하지 않는 v6 planning-lock 문서·검증 범위다.

## Diagnosis and solution

바로 전 main 검증(run 33184615347)의 Godot job은 성공했다. 동일한 PR head `0d95a49d36a133d48874e4dd9cf8de5062871a3d`에서 실패 job만 재실행했고, import·모든 headless contract test·runtime smoke가 모두 성공했다. 따라서 이번에는 제품 코드나 CI 설정을 바꾸지 않았다.

```text
DIAGNOSIS = NON_REPRODUCIBLE_HEADLESS_GODOT_TEARDOWN_FAILURE__CI_ENVIRONMENT_OR_TOOLCHAIN_SUSPECTED
SOLUTION = VERIFY_DIFF_SCOPE + COMPARE_PREVIOUS_SUCCESS + SAME_HEAD_FAILED_JOB_RERUN
REJECTED = UNRELATED_RUNTIME_FIX / CI_GUARD_WEAKENING / CLAIMING_HUMAN_OR_PLAYER_PASS
```

## Lesson / disposition

문서 전용 변경에서 Godot 종료 오류가 한 번 발생해도, 즉시 게임 구현을 수정하지 않는다. 먼저 보호된 product path diff, 직전 성공 run, 같은 SHA 재실행으로 원인 범위를 좁힌다. 동일 SHA에서 재발하면 별도 runtime/CI 결함으로 승격해 재현·수정 task를 열어야 한다.

```text
NEXT_VALIDATION = MONITOR_NEXT_INDEPENDENT_GODOT_CI_RUN__OPEN_RUNTIME_CI_ISSUE_IF_RECURS
NO_BASE_PROMOTION = SINGLE_NON_REPRODUCIBLE_PROJECT_CI_OBSERVATION__BASE_POLICY_ALREADY_REQUIRES_EVIDENCE
RUNTIME_HUMAN_PLAYER_RIGHTS = NOT_RUN__UNCHANGED
```
