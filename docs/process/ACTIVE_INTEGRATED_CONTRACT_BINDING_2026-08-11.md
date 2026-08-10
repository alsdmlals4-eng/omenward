# [현행] OMENWARD 통합 작업지시문 v4.5 Thin Adapter 바인딩

```yaml
updated_at: 2026-08-11
decision_id: OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1
instruction_canon_activation_decision_id: OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1
contract_name: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION
contract_version: "4.5"
contract_revision: 2026-08-11-r2
contract_status: ACTIVE_BASE_CURRENT_MAIN_THIN_ADAPTER_GODOT_DELIVERY_CONTRACT
binding_status: ACTIVE
adapter_policy: THIN_ADAPTER_DO_NOT_DUPLICATE_BASE_CANON
canonical_instruction_source: docs/process/PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5_r2.md
common_work_authority: alsdmlals4-eng/Base@315c66eea9614c284b9c11c4d522141065dfa4b0
project_activation_baseline: 87339f87949c8faea0dfe1482c5d0887a04d94f4
project_local_path: C:/Users/user/Documents/GitHub/Ninza/omenward
godot_project_path: C:/Users/user/Documents/GitHub/Ninza/omenward
current_phase: PHASE_A_GPT_CHAT_PLANNING
planning_status: MAIN_CANONICAL_APPROVED_10_OF_10
completion_trigger: USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION
phase_c_status: PHASE_C_BLOCKED
continuous_work: ACTIVE_WITHIN_APPROVED_CANON_SCOPE
```

## 1. 권위 합성

이 파일은 Base current canon을 복제하지 않는다.

```text
Base 공통 운영 절차·Skill·검증 규칙
→ fresh alsdmlals4-eng/Base current authority

OMENWARD 고유 경로·Decision·게임 정본·Sheet·보호 경계
→ OMENWARD current canon

GitHub full canonical v4.5 r2
→ docs/process/PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5_r2.md
→ 프로젝트 단계·Thin Adapter·승인/동기화/Phase Gate
```

업로드된 v4.5 r2 원문의 조직·용어·세부 계약을 GitHub full canonical source로 보존한다. 원문에 남아 있던 Switchy Express 프로젝트 경로 3곳은 사용자의 최신 OMENWARD 프로젝트 입력과 충돌했으므로 다음 값으로만 교정했다.

```text
project_local_path = C:/Users/user/Documents/GitHub/Ninza/omenward
canonical_local_checkout = C:/Users/user/Documents/GitHub/Ninza/omenward
godot_project_path = C:/Users/user/Documents/GitHub/Ninza/omenward
```

이 교정의 승인 Decision은 `OMW-DEC-20260811-OPS-ACTIVATE-INTEGRATED-CONTRACT-V4-5-R2-V1`이다.

Base와 충돌하는 공통 절차는 Base current가 우선한다. OMENWARD 고유 값과 사용자 승인 범위는 이 바인딩과 프로젝트 정본이 우선한다.

## 2. 현재 단계

```text
PHASE_A_GPT_CHAT_PLANNING
→ current canon freshness repair
→ same Decision GitHub + Sheet sync
→ planning PR exact-head validation
→ adversarial review
→ eligible planning merge
→ remaining planning closure
→ USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION
→ PHASE_B_FINAL_PLANNING_REVIEW
→ PHASE_C only after Phase B DoR closes
```

현재 사용자의 `[연속작업 진행해]`는 승인된 canon/planning 작업을 중간 승인 대기 없이 계속하라는 실행 flag다. 이것은 `기획 완료` 선언이 아니다.

따라서 다음 표면은 현재 금지한다.

```text
PHASE_C_BLOCKED
PERSISTENT_POWERSHELL_CODEX_BUILD = FORBIDDEN
PERSISTENT_HIGODOT_GODOT_AUTHORING = FORBIDDEN
PRODUCT_RUNTIME_GAP_IMPLEMENTATION = PAUSED_BY_PHASE_GATE
```

## 3. 현재 제품·runtime owner

```text
planning_canon = MAIN_CANONICAL_APPROVED_10_OF_10
runtime_package = OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
runtime_pr = 175
runtime_pr_head = bde85549560fca90f7aa25fc4842bc0a3afb92e7
runtime_issue = 176
approved_runtime_gap_count = 7
runtime_pr_merge = FORBIDDEN
handoff_pr = 177
handoff_pr_role = REFERENCE_ONLY_HANDOFF
handoff_pr_merge = DO_NOT_MERGE_NOW
```

PR175의 11/11 Actions SUCCESS는 당시 exact-head/base에 대한 역사 증거다. 이 planning/canon Decision이 `main`을 전진시키면 새 base 기준 strict up-to-date 검증으로 승격하지 않는다.

## 4. 현행 병영 TokenSource 정정

```text
SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT
SPECIAL_T1_SELECTED_UNIT_PERSISTENCE = FIXED_WHILE_BUILDING_REMAINS_T1
SPECIAL_T1_AUTO_PRODUCTION = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_AUTO_PRODUCTION_AND_TOKEN_SOURCE = SAME_SELECTED_UNIT_SEPARATE_ACQUISITION_PATHS
SPECIAL_T1_SAVE_RELOAD_RESELECT = FORBIDDEN
SPECIAL_T1_FREE_REROLL = FORBIDDEN
```

`SPECIAL_T1_TOKEN_SOURCE = NONE`은 historical/superseded 문맥 외에는 구현 입력 금지다.

## 5. v4.4 역사 경계

다음 v4.4 표면은 당시 사실을 검증하는 history/compatibility evidence이며 current binding이 아니다.

```text
docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-06.md
docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json
tools/validate_active_integrated_contract_v4_4.py
tests/python/test_active_integrated_contract_v4_4.py
.github/workflows/validate-active-integrated-contract-v4-4.yml
```

v4.5 activation은 이들의 과거 SHA·Gate를 소급 수정하지 않는다.

## 6. Current state owner

Full instruction canon:

`docs/process/PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.5_r2.md`

Machine-readable current routing:

`docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json`

Decision rationale:

`docs/process/APPROVED_OMENWARD_CANON_FRESHNESS_AND_V4_5_THIN_ADAPTER_2026-08-11.md`

Sheet sync evidence:

`docs/operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json`

## 7. 현재 Gate

```text
ENTRY_GATE = BLOCK
PHASE_C_GATE = BLOCK
BLOCKER = USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED
BLOCKER = PHASE_B_FINAL_PLANNING_REVIEW_NOT_RUN
BLOCKER = ISSUE176_7_RUNTIME_GAPS_OPEN
```

이 바인딩의 승인·병합은 기획 정본화를 닫는 것이며 Godot BUILD 시작 승인이 아니다.
