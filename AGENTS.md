# OMENWARD 프로젝트 AI 작업 규칙

```yaml
updated_at: 2026-08-11
common_work_authority: alsdmlals4-eng/Base/AGENTS.md
base_main_observed: 315c66eea9614c284b9c11c4d522141065dfa4b0
current_decision: OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1
contract_version: 4.5
contract_adapter: THIN_ADAPTER_DO_NOT_DUPLICATE_BASE_CANON
planning_status: MAIN_CANONICAL_APPROVED_10_OF_10
work_phase: PHASE_A_GPT_CHAT_PLANNING
phase_c_gate: BLOCK
product_code_authority: NONE
runtime_package: OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
runtime_pr: 175
runtime_issue: 176
runtime_gap_count: 7
handoff_pr: 177
handoff_disposition: REFERENCE_ONLY_DO_NOT_MERGE
```

공통 작업·검증·TDD·벤치마킹·PR·적대적 검토·승인 배치·Base 개선 절차는 **fresh `alsdmlals4-eng/Base` current authority**를 따른다. 이 파일은 Base 절차를 복제하지 않고 OMENWARD 고유의 읽기 순서, 현재 Decision, 제품 경계와 단계 Gate만 책임진다.

## 1. 작업 시작 순서

1. Base `START_HERE.md`·`AGENTS.md`와 current main/open PR을 fresh-read한다.
2. `docs/PROJECT_CORE.md`
3. `docs/ACTIVE_CONTEXT.md`
4. `docs/DOCUMENTATION_MAP.md`
5. `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
6. `docs/OMENWARD_GDD_CURRENT_CANON.md`
7. 현재 Decision 책임 원본·실제 코드/데이터/테스트
8. `docs/CURRENT_IMPLEMENTATION_STATUS.md`
9. 연결 Google Sheet의 현재 Decision·감사·관련 시스템 탭

과거 채팅·Handoff·업로드 파일·오래된 SHA를 current truth로 사용하지 않는다. 대상 파일이 `[현행]`인지 Lifecycle Registry로 확인한다.

## 2. v4.5 현재 단계

현재 바인딩:

- `docs/process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md`
- `docs/operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json`
- `docs/process/APPROVED_OMENWARD_CANON_FRESHNESS_AND_V4_5_THIN_ADAPTER_2026-08-11.md`

```text
PHASE_A_GPT_CHAT_PLANNING
→ GitHub 정본·기획 데이터·Sheet 같은 Decision ID 동기화
→ planning PR 검증·적대적 검토·필요 시 병합
→ 사용자의 명시적 "기획 완료" 선언
→ PHASE_B_FINAL_PLANNING_REVIEW
→ Definition of Ready 종료
→ PHASE_C_POWERSHELL_CODEX_GODOT_BUILD
```

`[연속작업 진행해]`는 승인된 현재 작업을 연속 수행하는 flag이지 `기획 완료` 선언이 아니다.

따라서 현재:

```text
PHASE_C_BLOCKED
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED
PHASE_B_FINAL_PLANNING_REVIEW_NOT_RUN
PERSISTENT_POWERSHELL_CODEX_BUILD = FORBIDDEN
PERSISTENT_HIGODOT_GODOT_AUTHORING = FORBIDDEN
```

## 3. 현행 병영 TokenSource 계약

최종 정정 owner:

`docs/design/APPROVED_OMENWARD_BARRACKS_AUTO_PRODUCTION_AND_TOKEN_SOURCE_AMENDMENT_2026-08-06.md`

```text
GENERAL_T1_AUTO_PRODUCTION = BASIC_INFANTRY
GENERAL_T1_TOKEN_SOURCE = BASIC_INFANTRY
GENERAL_T2_AUTO_PRODUCTION = SELECTED_GENERAL_UNIT
GENERAL_T2_TOKEN_SOURCE = SELECTED_GENERAL_UNIT

SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT
SPECIAL_T1_SELECTED_UNIT_PERSISTENCE = FIXED_WHILE_BUILDING_REMAINS_T1
SPECIAL_T1_AUTO_PRODUCTION = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_AUTO_PRODUCTION_AND_TOKEN_SOURCE = SAME_SELECTED_UNIT_SEPARATE_ACQUISITION_PATHS
SPECIAL_T1_SAVE_RELOAD_RESELECT = FORBIDDEN
SPECIAL_T1_FREE_REROLL = FORBIDDEN

SPECIAL_T2_AUTO_PRODUCTION = SELECTED_SPECIAL_UNIT
SPECIAL_T2_TOKEN_SOURCE = SELECTED_SPECIAL_UNIT
TOKEN_SOURCE_WEIGHT_AND_COUNT = PENDING_SIMULATION
```

`SPECIAL_T1_TOKEN_SOURCE = NONE`과 “T2에서 처음 TokenSource 해금”은 historical/superseded 문맥 외 구현 입력 금지다.

## 4. 현재 runtime package

```text
PR175 = OPEN_DRAFT
PR175_HEAD_OBSERVED = bde85549560fca90f7aa25fc4842bc0a3afb92e7
PR175_HISTORICAL_EXACT_HEAD_ACTIONS = 11_SUCCESS_0_FAILURE
ISSUE176 = OPEN
ISSUE176_APPROVED_RUNTIME_GAPS = 7
PR175_MERGE = FORBIDDEN
PR177 = REFERENCE_ONLY_DO_NOT_MERGE
```

PR175의 일곱 gap은 승인된 동일 runtime package 범위지만, v4.5 Phase C가 열리기 전에는 구현하지 않는다. 이 planning/canon 변경으로 `main`이 전진하면 기존 11/11은 새 base에 대한 strict up-to-date 증거로 간주하지 않는다.

## 5. 프로젝트 경로

```text
project_local_path = C:/Users/user/Documents/GitHub/Ninza/omenward
godot_project_path = C:/Users/user/Documents/GitHub/Ninza/omenward
```

사용자 제공 v4.5 r2 원문의 Switchy Express 경로는 OMENWARD 바인딩에 사용하지 않는다.

## 6. OMENWARD 보호 경계

- planning canon은 `MAIN_CANONICAL_APPROVED_10_OF_10`이다.
- 정확 final functional-value scalar/vector/parameter vector/product numerics는 아직 승인되지 않았다.
- 승인되지 않은 자동화·하드카운터·직접 핵심 보상 판매를 추가하지 않는다.
- 이미지 생성은 사용자 지시에 따라 중단 상태다.
- PR177은 현재 정본보다 높은 권위를 갖지 않는다.
- historical v4.4 binding/state/test/workflow는 당시 사실 증거로 보존한다.
- Google Sheet는 사용자 GDD workspace/mirror이며 GitHub 권위 문서와 같은 Decision ID로 동기화한다.

## 7. PC·Android 공용 코어 상태

```text
ARCHITECTURE_STATUS = MAIN_CANONICAL
PHASE0_STATIC_GUARD = MAIN_CANONICAL_LOCAL_PASS
PHASE1_COMMAND_EVENT_CONTRACTS = MAIN_CANONICAL_LOCAL_PASS
PHASE2_GAME_SESSION_DECOUPLING = MAIN_CANONICAL_LOCAL_PASS
SHARED_SAVE_SCHEMA = NOT_STARTED
PC_ADAPTER_IMPLEMENTATION = NOT_STARTED
ANDROID_ADAPTER_IMPLEMENTATION = NOT_STARTED
STORE_SDK_INTEGRATION = NOT_STARTED
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
EXPORT_PRESETS = ABSENT
```

플랫폼 Phase 0~2의 과거 local-pass는 해당 구조 경계만 증명하며 현재 gameplay runtime package 완료나 출시 준비를 뜻하지 않는다.
