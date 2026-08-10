# [현행] OMENWARD 정본 최신성 복구·v4.5 Thin Adapter 결정

```yaml
updated_at: 2026-08-11
decision_id: OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1
approval: USER_APPROVED_RECOMMENDED_OPTION_A
continuous_work: ACTIVE_WITHIN_APPROVED_CANON_SCOPE
status: APPROVED_CANON_RECONCILIATION_IN_PROGRESS
counter: NON_COUNTER
product_code_authority: NONE
godot_persistent_authoring: BLOCKED_BY_V4_5_PHASE_GATE
```

## 1. 승인된 결정

사용자는 2026-08-11 현재 정본 충돌을 먼저 복구한 뒤 후속 runtime 작업을 새 `main` 기준으로 재검증하는 권장안 A를 승인했다.

이 Decision은 새 게임 기능이나 새 제품 수치를 승인하지 않는다. 목적은 이미 승인된 프로젝트 사실이 활성 소비자마다 다르게 노출되는 상태를 제거하고, 사용자 제공 `PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION` v4.5 r2를 OMENWARD용 Thin Adapter로 활성화하는 것이다.

## 2. Fresh baseline

```text
Base default branch = main
Base current main = 315c66eea9614c284b9c11c4d522141065dfa4b0
Base open PRs = 0
OMENWARD default branch = main
OMENWARD activation baseline = 87339f87949c8faea0dfe1482c5d0887a04d94f4
OMENWARD open Draft PRs = #175 / #177
PR175 head = bde85549560fca90f7aa25fc4842bc0a3afb92e7
PR175 approved runtime/fixture gaps = 7
PR177 disposition = REFERENCE_ONLY_HANDOFF / DO_NOT_MERGE_NOW
Google Sheet = 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw / 31 tabs
```

Base는 이 Decision의 프로젝트 고유 내용을 소유하지 않는다. 공통 Work Mode·Skill·검증·PR·적대적 검토 절차는 fresh Base current authority를 따른다.

## 3. 확인된 정본 충돌

### 3.1 Special T1 TokenSource

최종 승인 정정 문서:

`docs/design/APPROVED_OMENWARD_BARRACKS_AUTO_PRODUCTION_AND_TOKEN_SOURCE_AMENDMENT_2026-08-06.md`

현행 값:

```text
SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT
SPECIAL_T1_SELECTED_UNIT_PERSISTENCE = FIXED_WHILE_BUILDING_REMAINS_T1
SPECIAL_T1_AUTO_PRODUCTION = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_AUTO_PRODUCTION_AND_TOKEN_SOURCE = SAME_SELECTED_UNIT_SEPARATE_ACQUISITION_PATHS
SPECIAL_T1_SAVE_RELOAD_RESELECT = FORBIDDEN
SPECIAL_T1_FREE_REROLL = FORBIDDEN
```

따라서 다음 표현은 활성 구현 입력으로 사용할 수 없다.

```text
SPECIAL_T1_TOKEN_SOURCE = NONE
T1 TokenSource 없음
T2에서 처음 TokenSource 해금
```

구형 Tier·Spec·Review 내부의 당시 문구는 역사 증거로 보존할 수 있다. 그러나 `[현행]` GDD, Sheet 동기화 계약, Sheet current-facing tab, cold-start router가 그 문구를 현재값처럼 재발행해서는 안 된다.

### 3.2 Cold-start routing

`AGENTS.md`, `PROJECT_CORE.md`, `DOCUMENTATION_MAP.md`, `ACTIVE_CONTEXT.md`, `CURRENT_IMPLEMENTATION_STATUS.md`, `PROJECT_CANON_DECISION_LEDGER.md`가 서로 6/10·7/10·10/10 및 다른 runtime 시점을 가리키고 있었다.

현행 planning canon은 `MAIN_CANONICAL_APPROVED_10_OF_10`이며, 제품 후속 owner는 승인된 `BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE`다. 다만 v4.5 단계 Gate 때문에 현재 persistent implementation은 실행하지 않는다.

## 4. v4.5 Thin Adapter 활성화

사용자 제공 v4.5 r2의 핵심 경계만 OMENWARD에 바인딩한다.

```text
adapter_policy = THIN_ADAPTER_DO_NOT_DUPLICATE_BASE_CANON
current_phase = PHASE_A_GPT_CHAT_PLANNING
planning_completion_trigger = USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION
PHASE_B = FINAL_PLANNING_REVIEW_AFTER_EXPLICIT_DECLARATION
PHASE_C = POWERSHELL_CODEX_GODOT_BUILD_AFTER_PHASE_A_AND_B
```

`[연속작업 진행해]`는 승인된 현재 범위의 연속 실행 flag이며 `기획 완료` 선언과 동일하지 않다.

따라서 이 Decision에서 허용되는 것은 정본·기획 데이터·Sheet·planning PR·검증·적대적 검토·병합뿐이다. PowerShell/Codex/Godot persistent implementation은 금지한다.

## 5. 프로젝트 경로 정정

v4.5 r2 원문에 남은 Switchy Express 경로는 OMENWARD 프로젝트 고유값이 아니다. 이 프로젝트 바인딩은 다음 값만 사용한다.

```text
project_local_path = C:/Users/user/Documents/GitHub/Ninza/omenward
godot_project_path = C:/Users/user/Documents/GitHub/Ninza/omenward
```

## 6. v4.4 보존 정책

다음 파일은 당시 v4.4 activation과 runtime transition 검증의 역사 증거로 보존한다.

- `docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-06.md`
- `docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json`
- `tools/validate_active_integrated_contract_v4_4.py`
- `tests/python/test_active_integrated_contract_v4_4.py`
- `.github/workflows/validate-active-integrated-contract-v4-4.yml`

v4.5 current routing을 위해 v4.4의 당시 SHA·Decision·Gate 사실을 소급 수정하지 않는다. 문서 수명주기 Registry에서 v4.4 binding/state를 `HISTORICAL_V4_4_BINDING`으로 분류한다.

## 7. Open PR disposition

### PR #175

```text
status = OPEN_DRAFT
head = bde85549560fca90f7aa25fc4842bc0a3afb92e7
historical_exact_head_ci = 11_SUCCESS_0_FAILURE
runtime_gap_count = 7
merge = FORBIDDEN
phase_c_execution = BLOCKED_UNTIL_EXPLICIT_PLANNING_COMPLETE_AND_PHASE_B
```

11/11은 기존 base에 대한 exact-head 역사 증거다. 이 canon PR이 `main`을 전진시키면 strict up-to-date runtime 검증으로 간주하지 않는다.

### PR #177

```text
status = OPEN_DRAFT
role = REFERENCE_ONLY_HANDOFF
merge = DO_NOT_MERGE_NOW
```

live continuation truth는 fresh `main`과 current state가 소유하며 PR177은 locator/history만 담당한다.

## 8. Sheet 동기화

같은 Decision ID로 최소 다음 surface를 동기화한다.

```text
00_프로젝트_허브
01_작업순서
02_현재_확정결정
04_누락_충돌_감사
15_조작_게임규칙
99_변경이력
```

과거 행은 덮어쓰지 않는다. 구형 `SPECIAL_T1_TOKEN_SOURCE = NONE` row는 historical Decision으로 남기되, 새 current correction row가 amendment와 현행 구현 입력을 명시한다.

Draft PR 동안 상태는 `PROPOSED_SHEET_CHANGE`, 병합 후 같은 Decision row를 `MERGED_CANON`으로 갱신한다.

## 9. 검증·종료 Gate

```text
TDD_RED = REQUIRED_AND_OBSERVED
TDD_GREEN = REQUIRED
SHEET_BOUNDED_REREAD = REQUIRED
EXACT_HEAD_CI = REQUIRED
ADVERSARIAL_P0_P1 = 0_REQUIRED
UNRESOLVED_REVIEW_THREADS = 0_REQUIRED
BASE_MAIN_RACE_RECHECK = REQUIRED
PROJECT_MAIN_RACE_RECHECK = REQUIRED
PRODUCT_MUTATION = NONE
GODOT_PERSISTENT_MUTATION = NONE
```

이 Decision이 병합돼도 PHASE C는 자동으로 열리지 않는다. 다음 단계 전환에는 사용자의 명시적 `기획 완료` 선언이 필요하다.
