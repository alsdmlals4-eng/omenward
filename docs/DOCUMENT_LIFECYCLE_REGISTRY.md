# [현행] OMENWARD 문서 수명주기 레지스트리

```yaml
updated_at: 2026-08-07
policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
common_process_authority: alsdmlals4-eng/Base/AGENTS.md
status: CURRENT_LIFECYCLE_AUTHORITY
current_decision: OMW-DEC-20260806-PLANNING-PR142-LATEST-MAIN-INTEGRATION-V3
latest_amendment: OMW-DEC-20260806-PLANNING-BARRACKS-AUTO-PRODUCTION-AND-TOKEN-SOURCE-AMENDMENT-V1
current_count: APPROVED_10_OF_10_WITH_TOKEN_SOURCE_AMENDMENT
```

이 레지스트리는 파일명·과거 YAML·부분 문구보다 우선한다. `[대체됨]`, `[보류]`, `[폐기]` 문서는 신규 기획·Codex 구현·아트 제작 입력으로 사용하지 않는다. 재사용 가능한 공통 작업 규칙은 Base에서만 관리하며 이 레지스트리는 OMENWARD 문서 상태만 판정한다.

## 1. [현행]

### 최상위·운영

- `PROJECT_CORE.md`
- `OMENWARD_GDD_CURRENT_CANON.md`
- `ONBOARDING_PLANNING_CURRENT_AUTHORITY.md`
- `ACTIVE_CONTEXT.md`
- `CURRENT_IMPLEMENTATION_STATUS.md`
- `DECISIONS_PENDING.md`
- `DOCUMENTATION_MAP.md`
- `process/APPROVED_DYNAMIC_CURRENT_MAIN_AND_DOCUMENT_LIFECYCLE_POLICY_2026-08-04.md`

외부 공통 운영 권위:

- `alsdmlals4-eng/Base/AGENTS.md`
- `alsdmlals4-eng/Base/docs/OPERATING_MODEL.md`
- `alsdmlals4-eng/Base/docs/WORK_MODE_AND_SKILL_ROUTING.md`

### Planning Batch와 후속 정정

- 1/10 `design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md`
- 2/10 `design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- 3/10 계보는 아래 `[대체됨]` 건물 분기 문서가 보존한다. 현행 건물 구조는 `OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1` / `design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md`가 담당한다.
- 4/10 `design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`
- 5/10 `design/APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md`
- 6/10 `design/APPROVED_OMENWARD_STAGE_END_MERCHANT_2026-08-05.md`
- 7~10/10 및 최종 우선순위 `ONBOARDING_PLANNING_CURRENT_AUTHORITY.md`
- 최종 병영 정정 `design/APPROVED_OMENWARD_BARRACKS_AUTO_PRODUCTION_AND_TOKEN_SOURCE_AMENDMENT_2026-08-06.md`

### 현행 시스템

- `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`: 전체 시스템 연결 계보.
- `design/APPROVED_OMENWARD_COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_AND_BUILDING_ROSTER_2026-08-04.md`: HUD·룰렛·기본 건물 역할. 후속 세부 정본이 우선한다.
- `OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1` / `design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md`: 건물별 Tier 구조와 일반·특수병 병영 분리.
- `design/APPROVED_OMENWARD_BARRACKS_AUTO_PRODUCTION_AND_TOKEN_SOURCE_AMENDMENT_2026-08-06.md`: 특수병 T1 자동생산·TokenSource 최종 정정.
- `design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`: 병종 역할·대응망. 병영 배치 구조는 후속 건물 정본이 우선한다.
- `design/APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md`: 전술·마력.
- `design/APPROVED_OMENWARD_STAGE_END_MERCHANT_2026-08-05.md`: Stage 종료 상인.
- `design/APPROVED_PC_ANDROID_CORE_ADAPTER_ARCHITECTURE_2026-08-06.md`: 플랫폼 구조.
- `APPROVED_PC_ANDROID_PHASE0_FREE_LOCAL_BASELINE_2026-08-06.md`: Phase 0 증거.
- `APPROVED_PC_ANDROID_PHASE1_CONTRACTS_2026-08-06.md`: Phase 1 계약.
- `APPROVED_PC_ANDROID_PHASE2_GAME_SESSION_DECOUPLING_2026-08-06.md`: Phase 2 구현·검증 증거.

## 2. [대체됨]

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
LEGACY_INFINITE_MERCHANT_STOCK
status = SUPERSEDED_BY_DECISION_6_OF_10
replacement = four finite visit slots / no infinite purchase or reroll
IMPLEMENTATION_INPUT_FORBIDDEN
```

```text
LEGACY_DIRECT_CORE_REWARD_SALES
status = SUPERSEDED_BY_DECISION_6_OF_10
replacement = repair/research/roulette/build discount support only
IMPLEMENTATION_INPUT_FORBIDDEN
```

기타 대체 문서:

- `OMENWARD_GAME_DESIGN.md`: `OMENWARD_GDD_CURRENT_CANON.md`이 승계.
- `design/APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md`: 20 Stage 정본으로 대체.
- 과거 post-merge Sync 문서: 당시 증거만 보존.

## 3. [보류]

- Hero·Legendary 문서군: 후속 재조정 전 구현 입력 금지.
- Meta·Hub 문서군: 후속 재조정 전 구현 입력 금지.
- 정확 경제·생산·TokenSource 수치: 시뮬레이션 전 확정 금지.
- 구형 구현 계획: 재실행 금지, 과거 결정·검증 증거로만 사용.

## 4. [폐기]

- 식량을 현행 핵심 HUD 자원으로 사용.
- 기본 건물 5종.
- 모든 건물에 공통 A/B 분기 문법 적용.
- 지휘소 주변 범위 오라.
- `15웨이브=1스테이지`·고정 60초.
- Stage 중 숨은 필수 카운터 변경.
- 룰렛 전용 상징 아이콘과 T3 병종 룰렛 토큰.
- 병종 보유량 기반 기본 세트 보너스.
- 반대 병영 계열 영구 삭제.
- 특정 병종·전술·상인 상품 미보유 시 통과 불가능한 단일 하드키.
- Stage 전 전술 편성 슬롯.
- 자동 전술 시전·자동 대상 확정.
- 연구에 마력 소비.
- 마력탑 복수 활성·병렬 연구.
- T3 전술의 부활·완전 회복·전면 정지·전선 자유 이동.
- 상시 접근 상점·무한 재고·무한 새로고침·할인 중첩.
- 상인의 병종·전술·마력·분기 직접 판매.

## 5. [증거]

```text
[증거] data/units/*.tres
status = LEGACY_PROTOTYPE_UNIT_DATA
IMPLEMENTATION_INPUT_FORBIDDEN
```

- `reviews/**`의 과거 PR·적대적 검토 기록.
- `benchmarks/**`의 Evidence Pilot.
- `archive/**`.
- 완료된 PR·commit·CI run·Sheet 변경 이력.
- `superpowers/plans/**`의 완료·대체된 계획은 당시 실행 계약 증거이며 공통 운영 권위가 아니다.

`[증거]`는 과거 사실을 증명하지만 현재 규칙을 자동 변경하지 않는다.

## 6. 신규 작업자용 프로젝트 확인

1. `PROJECT_CORE.md`, `DOCUMENTATION_MAP.md`, `ONBOARDING_PLANNING_CURRENT_AUTHORITY.md`를 먼저 읽는다.
2. 대상 파일이 `[현행]`인지 확인한다.
3. 건물 작업은 Tier 재정렬과 병영 TokenSource 정정 문서를 함께 읽고 앞선 정정을 우선한다.
4. 상인 작업은 6/10 책임 원본을 우선한다.
5. 정확 수치는 시뮬레이션·Codex 계획·제품 RED 테스트 뒤에만 확정한다.
6. 공통 작업 절차는 프로젝트 내부 과거 정책이 아니라 Base 책임 원본을 따른다.

## 7. 완료 이력

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1 / 3_OF_10 / SUPERSEDED_LINEAGE
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1 / 4_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1 / 5_OF_10
OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1 / 6_OF_10
OMW-DEC-20260806-PLANNING-PR142-LATEST-MAIN-INTEGRATION-V3 / APPROVED_10_OF_10
LEGACY_C1_C2_C3_PROVEN
```
