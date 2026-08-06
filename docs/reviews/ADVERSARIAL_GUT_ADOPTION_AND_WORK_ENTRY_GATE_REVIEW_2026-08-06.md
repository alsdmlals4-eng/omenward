# [적대적 검토] GUT 채택·HiGodot 경계·작업 진입 Gate

```yaml
decision_id: OMW-DEC-20260806-TOOLS-HIGODOT-GUT-AUTHORITY-AND-WORK-ENTRY-GATE-V1
status: DRAFT_REVIEW / ACTIVATION_BLOCKED
```

## 유효 Finding

1. GUT 9.7.1의 Godot 4.7.x 문서 호환성은 확인됐지만 실제 OMENWARD runtime은 미실행이다.
2. 프로젝트 vendor subtree가 reviewed upstream subtree와 달라 package integrity를 아직 증명하지 못했다.
3. Decision Ledger는 PR #142 진행 상태를 가리키고, Pending 문서는 PR #154 4/10보다 뒤처져 있다.
4. 이미지 검수 Sheet에는 READY/AWAITING 승인이 없다. 미생성 `IN_REVIEW`와 명시적 `REJECTED`만 존재한다.
5. Gate가 차단 중인 상황에서 모든 변경을 금지하면 Gate 자체를 복구할 수 없으므로 exact bootstrap/remediation allowlist만 허용한다.

## 공격과 방어

- **공격:** GUT을 테스트 권위라 부르면 test fixture가 Scene을 저장할 수 있다.
  - **방어:** 테스트 실행 중 생성한 임시 fixture는 test-owned temp 경로에만 두며 제품 Scene·Resource·설정 변경은 금지한다.
- **공격:** vendor mismatch를 단순 `.import` 차이로 치부할 수 있다.
  - **방어:** manifest diff 전에는 원인을 추정하지 않고 activation을 차단한다.
- **공격:** `IN_REVIEW`를 사실상 AWAITING으로 해석할 수 있다.
  - **방어:** 미생성 `IN_REVIEW`는 승인 대기 자산이 아니며 READY/AWAITING count 0을 계약으로 고정한다.
- **공격:** Bootstrap 예외가 일반 작업 우회로가 될 수 있다.
  - **방어:** exact allowlist와 PR·branch·base SHA가 모두 일치하지 않으면 실패한다.

## 수정 후 재공격 — PR155 self-bypass

- bootstrap 예외를 PR #155·branch·base SHA에 고정하지 않으면 후속 PR이 validator 자체를 약화할 수 있음: **VALID_P1 / FIXED_BY_CONTEXT_BINDING**.
- `addons/gut/**` 포괄 허용은 임의 plugin 변경 우회가 됨: **VALID_P1 / FIXED_BY_EXACT_PATH_AUTHORIZATION_ONLY**.
- Godot authoring 파일과 GUT test 파일을 한 PR에 섞을 수 있음: **VALID_P1 / FIXED_BY_CHANGED_FILE_AUTHORITY_GATE**.
- Sheet에 NON_COUNTER Decision이 추가된 뒤 `sheet_latest_decision=4/10` 표현이 낡음: **VALID_P1 / FIXED_BY_COUNTED_VS_NON_COUNTER_SPLIT**.

```text
BOOTSTRAP_EXCEPTION = PR155_ONLY
BROAD_REMEDIATION_PREFIX = FORBIDDEN
AUTHORING_AND_GUT_CHANGESET_OVERLAP = FORBIDDEN
```

## 판정

```text
SPEC_REVIEW = PASS_WITH_BLOCKERS
ACTIVATION = FAIL
NORMAL_WORK_ENTRY = FAIL
BOOTSTRAP_PR155_SCOPE = ALLOWED
GENERAL_REMEDIATION = NOT_AUTHORIZED
MERGE = BLOCKED_UNTIL_EXACT_HEAD_REVIEW_AND_REQUIRED_CHECKS
```
