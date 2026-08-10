# [현행] 오멘워드 현재 구현 상태

```yaml
updated_at: 2026-08-11
common_work_authority: alsdmlals4-eng/Base/AGENTS.md
base_main_observed: 315c66eea9614c284b9c11c4d522141065dfa4b0
current_decision: OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1
contract_version: 4.5
planning_status: MAIN_CANONICAL_APPROVED_10_OF_10
work_phase: PHASE_A_GPT_CHAT_PLANNING
runtime_status: PR175_DRAFT_7_RUNTIME_GAPS_OPEN
phase_c_gate: BLOCK
product_code_authority: NONE_FOR_THIS_DECISION
human_validation: HUMAN_QA_NOT_RUN
```

공통 운영 규칙은 Base current authority가 책임지고, 이 문서는 OMENWARD의 현재 기획·구현·검증 상태만 기록한다.

현재 시스템 연결 기준선은 `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`다.

최신 버티컬 슬라이스 구현: `NOT_STARTED`

## 1. Planning canon

```text
ONBOARDING_PLANNING = MAIN_CANONICAL_APPROVED_10_OF_10
BARRACKS_TOKEN_SOURCE_AMENDMENT = MAIN_CANONICAL
SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT
FINAL_FUNCTIONAL_VALUE_INDEX = NOT_SELECTED
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

최종 TokenSource owner:

`docs/design/APPROVED_OMENWARD_BARRACKS_AUTO_PRODUCTION_AND_TOKEN_SOURCE_AMENDMENT_2026-08-06.md`

구형 `SPECIAL_T1_TOKEN_SOURCE = NONE`은 implementation input이 아니다.

## 2. Runtime package transition

현재 runtime owner:

`OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1`

```text
PR175 = OPEN_DRAFT
PR175_HEAD_OBSERVED = bde85549560fca90f7aa25fc4842bc0a3afb92e7
PR175_HISTORICAL_EXACT_HEAD_ACTIONS = 11_SUCCESS_0_FAILURE
ISSUE176 = OPEN
ISSUE176_APPROVED_RUNTIME_GAPS = 7
PR175_MERGE = FORBIDDEN
PR177 = REFERENCE_ONLY_DO_NOT_MERGE
```

PR175에서 transition CI 4개 불일치는 해소됐지만 아래 7개 runtime/fixture gap은 여전히 open이다.

1. Priest encouragement +8% attack speed for provisional 5s, start/end events, support uptime, timing regression.
2. Support-role interception이 prior deterministic movement/combat/objective fallback을 제거하지 않음.
3. `flying`은 priority이지 universal target permission이 아님.
4. `cluster` density tie-break = lane order / unit-id semantics.
5. Giant `FRONTLINE_SURVIVAL_TIME` + `STRUCTURE_DAMAGE` collectors.
6. Registered deterministic fixtures `FV-PRIEST/MAGE/FLIER/GIANT/COMMON`.
7. true per-cast `TARGETS_HIT_PER_CAST` with multi-cast coverage.

## 3. v4.5 current phase

```text
PHASE_A_GPT_CHAT_PLANNING
USER_EXPLICIT_PLANNING_COMPLETE_DECLARATION_REQUIRED
PHASE_B_FINAL_PLANNING_REVIEW_NOT_RUN
PHASE_C_BLOCKED
```

현재 canon-freshness Decision은 planning/docs/Sheet 변경만 승인한다. Persistent PowerShell/Codex/Godot authoring과 Issue176 runtime 구현은 이 Decision에서 수행하지 않는다.

`[연속작업 진행해]`는 현재 승인 범위 연속 수행 flag이며 `기획 완료` 선언이 아니다.

## 4. PC·Android 공용 코어

```text
ARCHITECTURE_STATUS = MAIN_CANONICAL
PHASE0_STATIC_GUARD = MAIN_CANONICAL_LOCAL_PASS
PHASE1_COMMAND_EVENT_CONTRACTS = MAIN_CANONICAL_LOCAL_PASS
PHASE2_GAME_SESSION_DECOUPLING = MAIN_CANONICAL_LOCAL_PASS
GAME_COMMAND = IMPLEMENTED
GAME_EVENT = IMPLEMENTED
SEVEN_PLATFORM_CONTRACTS = IMPLEMENTED
GAME_APPLICATION = IMPLEMENTED
SESSION_DRIVER = IMPLEMENTED
SCENE_BINDER = IMPLEMENTED
PLATFORM_BOOTSTRAP = IMPLEMENTED_IDEMPOTENT
GAME_SESSION_COMPATIBILITY_FACADE = IMPLEMENTED
SHARED_SAVE_SCHEMA = NOT_STARTED
PC_ADAPTER_IMPLEMENTATION = NOT_STARTED
ANDROID_ADAPTER_IMPLEMENTATION = NOT_STARTED
STORE_SDK_INTEGRATION = NOT_STARTED
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
EXPORT_PRESETS = ABSENT
REPRESENTATIVE_PC_BUILD = NOT_RUN
REPRESENTATIVE_ANDROID_BUILD = NOT_RUN
```

Phase 0~2의 과거 local-pass는 플랫폼 경계만 증명하며 현재 gameplay runtime package 완료나 출시 readiness를 뜻하지 않는다.

## 5. Durable barracks analysis evidence

```text
ROBUSTNESS_10000 = PASS_FOR_APPROVED_ECONOMY_PRODUCTION_GATES
SPECIAL_TOKEN_SHARE_10_MIN = 0.296265
SPECIAL_TOKEN_SHARE_BURST_MAX = 0.333333
10K_JSON_SHA256 = 1675d5068d6299c618df2f5b27cca4cf6fb06990729d622cedf9c36282c8d3c3
10K_CSV_SHA256 = e7324cb7a46cdab3d765011890d38a234c541c9e28741a2e6af6d3bf2bbc0e8b
IDENTIFIABILITY = DIAGNOSTIC_NON_IDENTIFIABLE
FUNCTIONAL_VALUE_COMPARISON = ROLE_SPECIFIC_VECTOR_NO_SINGLE_WEIGHTED_SCORE
BLOCKED_RUNTIME_OUTPUT = NEVER_SYNTHESIZE_AS_ZERO
```

이는 final product numerics 선택이 아니다.

## 6. Tool authority

```text
GODOT_AI = 3.1.3 / SOLE_PERSISTENT_GODOT_AUTHORING_AUTHORITY_WHEN_PHASE_C_ACTIVE
GUT = 9.7.1 / DETERMINISTIC_GDSCRIPT_TEST_AUTHORITY_WHEN_ADOPTED
HERA = 1.0.0 / LIVE_QA_AND_OBSERVABILITY_ONLY
HERA_PERSISTENT_SOURCE_MUTATION = FORBIDDEN
```

과거 local HiGodot session 진단은 history evidence다. v4.5 Phase C가 열릴 때 fresh local process/session truth를 다시 읽는다.

## 7. 현재 planning/canon PR

```text
PR178 = DRAFT
DECISION = OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1
PURPOSE = CANON_FRESHNESS + V4_5_THIN_ADAPTER + SHEET_SYNC
PRODUCT_MUTATION = NONE
GODOT_MUTATION = NONE
```

TDD RED는 새 v4.5 authority artifact 부재와 active GDD/Workbook/cold-start drift를 실패로 고정한다. Green/merge 완료는 exact-head 검증과 Sheet bounded reread 후에만 기록한다.

## 8. Durable Vertical Slice implementation evidence

아래는 기존 project-core validator와 historical C1/C2/C3 검증이 소비하는 durability block이다. 현재 v4.5 Phase A를 과거 시점으로 되돌리는 것이 아니라 **구현 미완료 경계와 과거 검증 사실을 보존**한다.

```text
VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED
LATEST_AUTOMATED_CONTRACTS_NOT_RUN
HUMAN_QA_NOT_RUN
CORE_LOCK_NOT_ALLOWED
LEGACY_C1_C2_C3_PROVEN
LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
LEGACY_C2_BATTLE_OBJECTIVE_REMOTE_PROVEN
LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN
```

Historical exact evidence:

```text
C1 구현 검증 head: `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9`
C1 최종 검증 run: `29926598807`
C2 최종 검증 run: `29938742864`
C3 검증 head: `1976c5355124b2ce7d7ef77b8835df0c95710038`
C3 최종 검증 run: `29965348284`
```

```text
GAMEPLAY_PRODUCT_IMPLEMENTATION = NOT_STARTED
SCENE_RESOURCE_DATA_CHANGE_BY_PR142 = NONE
EXACT_NUMERICS = PENDING_SIMULATION_OR_LATER_CURRENT_OWNER
TWELVE_SCENARIO_QA = NOT_RUN
FIRST_TIME_HUMAN_QA = NOT_RUN
```

이 C1·C2·C3 증거는 과거 계약 검증 사실만 보존하며 **V2 구현 완료를 뜻하지 않는다**. 또한 현재 PR175 runtime package 완료나 v4.5 Phase C 진입을 뜻하지 않는다.

## 9. 다음 순서

현재 Decision 안에서:

```text
canon repair
→ same Decision Sheet proposed sync
→ bounded reread
→ exact-head CI
→ adversarial review
→ race check
→ eligible planning merge
→ merged-main + Sheet MERGED_CANON readback
```

그 다음에도 Phase C는 자동 시작하지 않는다. 사용자의 `기획 완료` 선언 후 Phase B 최종 planning review가 다음 단계다.
