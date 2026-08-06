# [현행 프로세스] GitHub Actions 예산 차단 시 로컬 exact-HEAD 검증 fallback

```yaml
decision_id: OMW-DEC-20260807-PROCESS-ACTIONS-BUDGET-LOCAL-EXACT-HEAD-FALLBACK-V1
status: ACTIVE_TEMPORARY_FALLBACK
authority: USER_DIRECT_APPROVAL_IN_CURRENT_CONVERSATION
trigger: BILLING_OR_SPENDING_LIMIT_PRE_START
github_actions_green: false
```

## 목적

GitHub Actions job이 계정 결제 또는 spending limit 때문에 `steps=0`, `runner_id=0`으로 시작되지 못하는 동안, 검증 가능한 작업을 멈추지 않기 위한 비용 0 fallback이다.

이 fallback은 GitHub Actions를 성공으로 꾸미지 않는다. 대신 GitHub의 현재 exact PR HEAD에서 파일 목록과 Git blob SHA를 읽고, 실행 파일을 별도 sandbox에 재구성한 뒤 같은 명령을 새로 실행한다.

## 허용 범위

```text
PROCESS_ONLY
DOCUMENTATION_ONLY
PYTHON_VALIDATOR_ONLY
DATA_CONTRACT_ONLY
```

필수 증거:

```text
exact PR HEAD와 base SHA
→ 전체 changed-file allowlist
→ 각 파일 Git blob SHA readback
→ 실행 파일의 remote blob과 reconstructed blob 일치
→ fresh py_compile/test/validator 명령과 exit code
→ 적대적 검토 P0/P1 0
→ 동일 Decision ID와 exact HEAD의 Google Sheet readback
```

## 금지 범위

다음은 이 fallback으로 통과시킬 수 없다.

```text
PRODUCT_IMPLEMENTATION
GODOT_AUTHORING
FORMAL_GUT_RUNTIME
WINDOWS_ANDROID_RUNTIME
ASSET_IMPORT_OR_RUNTIME
EXPORT_OR_PACKAGE
```

Godot, GUT CLI/JUnit, Windows, Android, 실제 사용자 로컬 checkout 증거가 없으면 해당 상태는 계속 `NOT_RUN` 또는 `BLOCKED_UNVERIFIED`다.

## 병합 경계

- GitHub가 정상 merge를 받아들이는 경우만 허용한다.
- repository policy 또는 branch protection bypass는 금지한다.
- fallback-eligible PR이고 exact-head evidence와 P0/P1 0이 확인된 경우에만 정상 merge 후보가 된다.
- 이 문서는 체크 실행 결과를 생성하지 않으며 `GITHUB_ACTIONS_GREEN`을 주장하지 않는다.

## PR #157 첫 적용

PR #157 exact head `c27715cfb7f161854fd994711a6859ee23a68fac`의 7개 변경 파일을 원격에서 읽었다. 테스트·validator·state 파일은 Git blob SHA가 정확히 일치하도록 재구성했다.

```text
py_compile = PASS
focused unittest = 8 PASS / 0 FAIL / 0 ERROR
contract validator = PASS
GitHub Actions = BILLING_OR_SPENDING_LIMIT_PRE_START / steps 0 / runner 0 / NOT_GREEN
Godot/GUT/Windows/Android = NOT_RUN
```

정확한 파일 SHA와 명령 결과는 `docs/evidence/PR157_LOCAL_EXACT_HEAD_VERIFICATION_2026-08-07.json`에 기록한다.
