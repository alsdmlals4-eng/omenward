# [적대적 검토] Actions 예산 차단 fallback

```yaml
decision_id: OMW-DEC-20260807-PROCESS-ACTIONS-BUDGET-LOCAL-EXACT-HEAD-FALLBACK-V1
status: REVIEWED_WITH_BOUNDARIES
```

## 공격 1 — 로컬 PASS를 Actions Green으로 가장

위험: sandbox에서 명령이 통과했다는 사실을 GitHub Actions Required Check 성공으로 표현할 수 있다.

대응: policy와 validator가 `github_actions_green=false`를 강제한다. evidence에는 기존 run/job의 `steps=0`, `runner_id=0`, billing classification을 그대로 남긴다.

판정: `MITIGATED`.

## 공격 2 — process 검증으로 Godot·GUT·플랫폼을 통과

위험: Python 문서 계약 PASS를 Godot import, GUT CLI/JUnit, Windows/Android runtime 증거로 확장할 수 있다.

대응: fallback eligible class에서 runtime·product·asset·export를 제외하고, evidence limitations가 `NOT_RUN` 또는 `BLOCKED_UNVERIFIED`인지 검사한다.

판정: `MITIGATED`.

## 공격 3 — 임의 로컬 파일을 테스트하고 exact HEAD라고 주장

위험: 원격 PR과 다른 파일을 실행할 수 있다.

대응: GitHub remote file content로 재구성하고 Git blob SHA를 계산해 원격 blob과 비교한다. PR #157의 실행 파일 3개는 모두 exact match다.

판정: `MITIGATED_FOR_RECONSTRUCTED_EXECUTABLES`.

## 공격 4 — branch protection 우회

위험: Actions unavailable을 이유로 저장소 정책을 무시할 수 있다.

대응: `repository_policy_bypass=FORBIDDEN`, `branch_protection_bypass=FORBIDDEN`, `normal_merge_only=true`를 validator가 강제한다. GitHub가 정상 merge를 거부하면 병합하지 않는다.

판정: `MITIGATED`.

## 공격 5 — 동일 에이전트 자기검증 과대평가

위험: connector readback, 재구성, 테스트, 검토를 같은 에이전트가 수행한다.

대응: 원격 blob SHA, 명령, exit code, 파일 allowlist, Sheet readback을 기계 판독 manifest로 남긴다. 다만 외부 독립 리뷰라고 주장하지 않는다.

판정: `RESIDUAL_P2_SELF_REVIEW_LIMITATION`.

## 최종 판정

```text
FALLBACK_POLICY = ACCEPTABLE_FOR_PROCESS_DOC_PYTHON_DATA_CONTRACT_ONLY
PR157_LOCAL_EXACT_HEAD = PASS_PROCESS_ONLY
GITHUB_ACTIONS_GREEN = FALSE
RUNTIME_VALIDATION = NOT_PROVEN
P0_OPEN = 0
P1_OPEN = 0
```
