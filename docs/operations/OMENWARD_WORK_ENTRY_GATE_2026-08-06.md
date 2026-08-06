# OMENWARD 필수 작업 진입 Gate

```yaml
decision_id: OMW-DEC-20260806-TOOLS-HIGODOT-GUT-AUTHORITY-AND-WORK-ENTRY-GATE-V1
WORK_ENTRY_GATE: FAIL_CLOSED
current_status: BLOCKED
```

## 입력 Surface

작업 전에 다음을 같은 시점의 증거로 읽는다.

1. Base `main`과 HiGodot·addon 정책.
2. OMENWARD `main`, 열린 PR, 최신 커밋.
3. `docs/PROJECT_CANON_DECISION_LEDGER.md`.
4. `docs/DECISIONS_PENDING.md`.
5. Google Sheet `02_현재_확정결정`.
6. Google Sheet `71_이미지기획_생성목록`과 `72_이미지검수_승인로그`.

## 판정

```text
WORK_ENTRY_GATE = FAIL_CLOSED
READY_WITH_CONFLICT = FORBIDDEN
AWAITING_WITH_REJECTED_EVIDENCE = FORBIDDEN
```

현재 실제 상태:

- 결정 원장: `STALE_CANON_CONFLICT`.
- 미확정 목록: `STALE_RELATIVE_TO_PR154_4_OF_10`.
- Sheet 최신 countable 기획 결정: PR #154 4/10 조건부 실패.
- Sheet 최신 NON_COUNTER 결정: HiGodot·GUT 권위 분리와 작업 진입 Gate.
- 이미지 READY: 0.
- 이미지 AWAITING: 0.
- OM-IMG-001: 미생성 `IN_REVIEW`.
- OM-IMG-005~010: `REJECTED_PROJECT_MISMATCH`.

## 예외

`BOOTSTRAP_ONLY_EXCEPTION`은 PR #155, 브랜치 `planning/gut-9-7-1-adoption-work-entry-gate-20260806`, base `7588317f294d602cfad5f7f15bfebcf849b8a77b`, 10개 exact allowlist가 모두 일치할 때만 적용한다. 다른 PR·브랜치·base에서는 validator 자체만 바꾸는 변경도 차단한다.

`GATE_REMEDIATION_ONLY_EXCEPTION`은 별도 승인 Decision과 exact PR number·branch·base SHA·changed-file 목록을 먼저 기록한 경우에만 적용한다.

```text
BROAD_REMEDIATION_PREFIX = FORBIDDEN
```

`addons/gut/**`, `tests/gut/**`, `scripts/tests/**` 전체를 포괄 허용하지 않는다. 제품 코드·Scene·Resource·게임 데이터 작업으로 확장하지 않는다. Godot authoring surface와 GUT test surface를 한 변경 묶음에 섞지 않으며, authoring 변경은 exact HiGodot manifest가 필요하다.

## 명령

```text
python tools/validate_godot_authoring_test_authority.py --contract
python tools/validate_godot_authoring_test_authority.py --entry --changed-file <repository-relative-path>

# PR155 bootstrap 전용
python tools/validate_godot_authoring_test_authority.py --entry --pr-number 155 --head-branch planning/gut-9-7-1-adoption-work-entry-gate-20260806 --base-sha 7588317f294d602cfad5f7f15bfebcf849b8a77b --changed-file <exact-bootstrap-path>
```

일반 작업에서 두 번째 명령이 1을 반환하면 작업을 시작하지 않는다.
