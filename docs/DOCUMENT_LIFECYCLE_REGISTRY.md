# [현행] OMENWARD 문서 수명주기 레지스트리

```yaml
updated_at: 2026-08-11
policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
common_process_authority: alsdmlals4-eng/Base/AGENTS.md
status: CURRENT_LIFECYCLE_AUTHORITY
current_decision: OMW-DEC-20260811-OPS-CANON-FRESHNESS-V45-ROUTING-V1
planning_status: MAIN_CANONICAL_APPROVED_10_OF_10
contract_version: 4.5
current_phase: PHASE_A_GPT_CHAT_PLANNING
```

이 레지스트리는 파일명·과거 YAML·부분 문구보다 우선한다. `[대체됨]`, `[보류]`, `[폐기]`, history/evidence 문서는 신규 구현 입력으로 사용하지 않는다. 공통 운영 규칙은 Base current authority가 소유하며 이 Registry는 OMENWARD 문서 상태만 판정한다.

## 1. [현행]

### 최상위·운영

- `PROJECT_CORE.md`
- `OMENWARD_GDD_CURRENT_CANON.md`
- `ONBOARDING_PLANNING_CURRENT_AUTHORITY.md`
- `ACTIVE_CONTEXT.md`
- `CURRENT_IMPLEMENTATION_STATUS.md`
- `DECISIONS_PENDING.md`
- `DOCUMENTATION_MAP.md`
- `PROJECT_CANON_DECISION_LEDGER.md`
- `PROJECT_GOOGLE_SHEET_WORKBOOK.md`
- `process/APPROVED_DYNAMIC_CURRENT_MAIN_AND_DOCUMENT_LIFECYCLE_POLICY_2026-08-04.md`
- `process/APPROVED_OMENWARD_CANON_FRESHNESS_AND_V4_5_THIN_ADAPTER_2026-08-11.md`
- `process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md`
- `operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json`
- `operations/CANON_FRESHNESS_V45_SHEET_SYNC_EVIDENCE_2026-08-11.json`

외부 공통 운영 권위:

- `alsdmlals4-eng/Base/AGENTS.md`
- `alsdmlals4-eng/Base/START_HERE.md`
- `alsdmlals4-eng/Base/docs/OPERATING_MODEL.md`
- `alsdmlals4-eng/Base/docs/WORK_MODE_AND_SKILL_ROUTING.md`
- `alsdmlals4-eng/Base/skills/SKILL_REGISTRY.json`

### Planning 1~10/10과 최종 정정

- 1/10 `design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md`
- 2/10 `design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- 3/10 역사 분기보다 `design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md`가 우선한다.
- 4/10 `design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`
- 5/10 `design/APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md`
- 6/10 `design/APPROVED_OMENWARD_STAGE_END_MERCHANT_2026-08-05.md`
- 7~10/10 및 최종 온보딩 우선순위 `ONBOARDING_PLANNING_CURRENT_AUTHORITY.md`
- 최종 병영 TokenSource 정정 `design/APPROVED_OMENWARD_BARRACKS_AUTO_PRODUCTION_AND_TOKEN_SOURCE_AMENDMENT_2026-08-06.md`

### 현행 runtime planning

- `design/APPROVED_OMENWARD_BARRACKS_10000_SEED_ROBUSTNESS_EXECUTION_RESULTS_2026-08-09.md`
- `design/APPROVED_OMENWARD_BARRACKS_FUNCTIONAL_VALUE_COMBAT_NUMERICS_DEFINITION_REVIEW_2026-08-09.md`
- `design/APPROVED_OMENWARD_BARRACKS_FUNCTIONAL_VALUE_MEASUREMENT_SCENARIOS_2026-08-09.md`
- `design/APPROVED_OMENWARD_BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_PACKAGE_2026-08-09.md`
- `process/APPROVED_OMENWARD_GODOT_AI_3_1_3_HERA_GUT_USER_APPROVAL_AND_REMOTE_SYNC_RECONCILIATION_2026-08-09.md`

현재 runtime package는 승인 범위이지만 v4.5 `PHASE_C_BLOCKED` 때문에 persistent implementation은 아직 실행하지 않는다.

### 플랫폼

- `design/APPROVED_PC_ANDROID_CORE_ADAPTER_ARCHITECTURE_2026-08-06.md`
- `APPROVED_PC_ANDROID_PHASE0_FREE_LOCAL_BASELINE_2026-08-06.md`
- `APPROVED_PC_ANDROID_PHASE1_CONTRACTS_2026-08-06.md`
- `APPROVED_PC_ANDROID_PHASE2_GAME_SESSION_DECOUPLING_2026-08-06.md`

## 2. [역사 / compatibility evidence]

```text
path = process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-06.md
status = HISTORICAL_V4_4_BINDING
replacement_for_current_routing = process/ACTIVE_INTEGRATED_CONTRACT_BINDING_2026-08-11.md
retention = HISTORICAL_RUNTIME_TRANSITION_AND_CONTRACT_EVIDENCE
IMPLEMENTATION_INPUT_FOR_CURRENT_PHASE = FORBIDDEN
```

```text
path = operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v1.json
status = HISTORICAL_V4_4_BINDING
replacement_for_current_routing = operations/ACTIVE_INTEGRATED_CONTRACT_STATE.v2.json
retention = HISTORICAL_RUNTIME_TRANSITION_AND_VALIDATOR_COMPATIBILITY
IMPLEMENTATION_INPUT_FOR_CURRENT_PHASE = FORBIDDEN
```

연결된 v4.4 validator/test/workflow는 당시 contract를 검증하는 regression evidence로 보존한다.

- `tools/validate_active_integrated_contract_v4_4.py`
- `tests/python/test_active_integrated_contract_v4_4.py`
- `.github/workflows/validate-active-integrated-contract-v4-4.yml`

## 3. [대체됨]

```text
LOCAL_COMMON_PROCESS_POLICY
path = process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md
status = SUPERSEDED_BY_BASE_COMMON_AUTHORITY
replacement = alsdmlals4-eng/Base/AGENTS.md
retention = HISTORICAL_PATH_POINTER_ONLY
IMPLEMENTATION_INPUT_FORBIDDEN
```

```text
LEGACY_UNIVERSAL_BUILDING_BRANCHES
path = design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md
status = SUPERSEDED_BY_BUILDING_TIER_REALIGNMENT
replacement = design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md
retention = HISTORICAL_DECISION_3_OF_10
IMPLEMENTATION_INPUT_FORBIDDEN
```

```text
LEGACY_SPECIAL_T1_NO_TOKEN_SOURCE
status = SUPERSEDED_BY_BARRACKS_TOKEN_SOURCE_AMENDMENT
replacement = SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT
IMPLEMENTATION_INPUT_FORBIDDEN
```

```text
LEGACY_TERM_MASOK
status = SUPERSEDED_TERMINOLOGY
replacement = 마력
IMPLEMENTATION_INPUT_FORBIDDEN
```

```text
LEGACY_MANA_TOWER_BRANCHES
status = SUPERSEDED_BY_DECISION_5_OF_10
replacement = 마력탑 T1 → T2 → T3 / one active instance / no branch
IMPLEMENTATION_INPUT_FORBIDDEN
```

```text
LEGACY_ALWAYS_AVAILABLE_SHOP
status = SUPERSEDED_BY_DECISION_6_OF_10
replacement = Stage 1~19 종료 정비시간 방문 / Stage 20 상인 금지
IMPLEMENTATION_INPUT_FORBIDDEN
```

```text
LEGACY_DIRECT_CORE_REWARD_SALES
status = SUPERSEDED_BY_DECISION_6_OF_10
replacement = support-only finite merchant inventory
IMPLEMENTATION_INPUT_FORBIDDEN
```

기타 대체 문서:

- `OMENWARD_GAME_DESIGN.md`: `OMENWARD_GDD_CURRENT_CANON.md`이 승계.
- `design/APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md`: 20 Stage 정본으로 대체.
- 과거 post-merge Sync 문서: 당시 증거만 보존.

## 4. [보류]

- 정확 경제·생산·TokenSource 수치: final 승인 전 확정 입력 금지.
- final functional-value scalar/vector/parameter vector/product numerics: 미선택/미승인.
- 구형 구현 계획: 재실행 금지, 당시 결정·검증 증거로만 사용.
- PR #175 runtime implementation: 승인 범위지만 v4.5 Phase C 전환 전 persistent execution 보류.
- PR #177: reference-only handoff, merge 금지.

## 5. [폐기]

- 식량을 현행 핵심 HUD 자원으로 사용.
- 기본 건물 5종.
- 모든 건물에 공통 A/B 분기 문법 적용.
- 지휘소 주변 범위 오라.
- `15웨이브=1스테이지`·고정 60초.
- Stage 중 숨은 필수 카운터 변경.
- 룰렛 전용 상징 아이콘과 T3 병종 룰렛 토큰.
- 병종 보유량 기반 기본 세트 보너스.
- 특정 병종·전술·상인 상품 미보유 시 통과 불가능한 단일 하드키.
- Stage 전 전술 편성 슬롯.
- 자동 전술 시전.
- 연구에 마력 소비.
- 마력탑 복수 활성·병렬 연구.
- 상시 접근 상점·무한 재고·무한 새로고침·직접 핵심 보상 판매.

## 6. [증거]

```text
[증거] data/units/*.tres
status = LEGACY_PROTOTYPE_UNIT_DATA
IMPLEMENTATION_INPUT_FORBIDDEN
```

- `reviews/**`의 과거 검토 기록.
- `benchmarks/**`의 Evidence Pilot.
- `archive/**`.
- 완료된 PR·commit·CI run·Sheet 변경 이력.
- `superpowers/plans/**`의 계획/실행 이력.

`[증거]`는 과거 사실을 증명하지만 현재 규칙을 자동 변경하지 않는다.

## 7. 신규 작업자 확인

1. Base current main/open PR을 fresh-read한다.
2. `PROJECT_CORE.md`, `ACTIVE_CONTEXT.md`, `DOCUMENTATION_MAP.md`를 읽는다.
3. 이 Registry에서 대상 파일 lifecycle을 확인한다.
4. 병영 TokenSource는 final amendment를 우선한다.
5. 현재 v4.5 phase가 `PHASE_A_GPT_CHAT_PLANNING`이고 Phase C가 BLOCK인지 확인한다.
6. PR175/Issue176을 읽더라도 사용자의 명시적 `기획 완료` 전 persistent runtime authoring을 시작하지 않는다.
7. 같은 Decision ID의 GitHub canon과 Google Sheet가 일치하는지 확인한다.
