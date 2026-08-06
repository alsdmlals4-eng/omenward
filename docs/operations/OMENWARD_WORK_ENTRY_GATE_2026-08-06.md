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
- Sheet 최신 결정: PR #154 4/10 조건부 실패.
- 이미지 READY: 0.
- 이미지 AWAITING: 0.
- OM-IMG-001: 미생성 `IN_REVIEW`.
- OM-IMG-005~010: `REJECTED_PROJECT_MISMATCH`.

## 예외

`BOOTSTRAP_ONLY_EXCEPTION`은 이 Gate를 처음 기록하고 검증하는 exact allowlist에만 적용한다.

`GATE_REMEDIATION_ONLY_EXCEPTION`은 중앙 정본의 비파괴 교정, GUT vendor manifest 교정, test canary 준비에만 적용한다. 제품 코드·Scene·Resource·게임 데이터 작업으로 확장하지 않는다.

## 명령

```text
python tools/validate_godot_authoring_test_authority.py --contract
python tools/validate_godot_authoring_test_authority.py --entry --changed-file <repository-relative-path>
```

일반 작업에서 두 번째 명령이 1을 반환하면 작업을 시작하지 않는다.
