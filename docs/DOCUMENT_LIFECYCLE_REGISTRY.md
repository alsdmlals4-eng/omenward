# [현행] OMENWARD 문서 수명주기 레지스트리

```yaml
updated_at: 2026-08-05
policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
status: CURRENT_LIFECYCLE_AUTHORITY
current_decision: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
current_count: 4_OF_10
```

이 레지스트리는 파일명·과거 YAML보다 우선한다. `[대체됨]`, `[보류]`, `[폐기]` 문서는 신규 기획·Codex 구현·아트 제작 입력으로 사용하지 않는다.

## 1. [현행]

### 최상위·운영

- `docs/PROJECT_CORE.md`
- `docs/OMENWARD_GDD_CURRENT_CANON.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/process/APPROVED_DYNAMIC_CURRENT_MAIN_AND_DOCUMENT_LIFECYCLE_POLICY_2026-08-04.md`
- `docs/process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md`

### 현재 Planning Batch

- 1/10 `docs/design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md`
- 2/10 `docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- 3/10 `docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`
- 4/10 `docs/design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`
- 병종 Spec `docs/superpowers/specs/2026-08-05-troop-roles-synergies-counters-design.md`
- 병종 계획 `docs/superpowers/plans/2026-08-05-troop-roles-synergies-counters.md`
- 병종 검토 `docs/reviews/ADVERSARIAL_TROOP_ROLE_SYNERGY_AND_COUNTER_REVIEW_2026-08-05.md`

### 현행 시스템

- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`: 전체 시스템 연결 계보.
- `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`: 최신 Stage 정본 우선 조건으로 용어·연결 승계.
- `docs/design/APPROVED_OMENWARD_COMBAT_SPACE_ROUTE_AND_TARGETING_EXPERIENCE_2026-08-04.md`: 전투 공간·Route의 플레이어 의미.
- `docs/design/APPROVED_OMENWARD_COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_AND_BUILDING_ROSTER_2026-08-04.md`: HUD·룰렛·자원·기본 건물 역할.
- `docs/design/APPROVED_OMENWARD_HUD_ROULETTE_LAYOUT_AND_BATTLEFIELD_VIEW_AMENDMENT_2026-08-04.md`: HUD 레이아웃·자산 재사용.
- `docs/design/APPROVED_OMENWARD_PIXEL_ILLUSTRATION_HYBRID_ART_DIRECTION_2026-08-04.md`: 최종 아트 방향.

## 2. [대체됨]

- `docs/OMENWARD_GAME_DESIGN.md`: `docs/OMENWARD_GDD_CURRENT_CANON.md`이 승계.
- `docs/design/APPROVED_DOPAMINE_DRIVEN_DESIGN_AND_FIRST_10_MINUTES.md`: 핵심 원칙만 core-fun 정본이 승계.
- `docs/design/APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md`: 20 Stage·3 Wave Beat 정본으로 대체.
- `docs/process/POST_MERGE_PIXEL_ILLUSTRATION_HYBRID_CANON_SYNC_2026-08-04.md`: 과거 병합 증거만 보존.
- `docs/design/proposals/0011-korean-natural-fantasy-names-law-and-mascot.md`: 세계관·명칭·벨루 정본에 반영 완료.

## 3. [보류]

### 첫 10~15분·튜토리얼

- `docs/design/APPROVED_BELLU_SINGLE_GUIDE_AND_FIRST_10_MINUTE_FLOW.md`
- `docs/design/APPROVED_TUTORIAL_FIRST_FOUR_WAVES_BALANCE_V1.md`

구형 식량·바리케이드·병영 자동생산·HUD 순서를 포함하므로 7/10에서 재설계 전 사용 금지.

### Hero·Legendary

`docs/design/APPROVED_OMENWARD_HERO_*`, `docs/design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md`, `docs/design/APPROVED_OMENWARD_REPEAT_LEGENDARY_RESULT_HIGH_GRADE_SLOT_RESOLUTION_2026-08-02.md`는 8/10 재조정 전 구현 입력 금지.

### Meta·Hub

- `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md`

9/10 재조정 전 구현 입력 금지.

### 구형 구현 계획

완료·병합된 과거 계획은 재실행하지 않고 Git 이력과 결정 근거로만 사용한다.

## 4. [폐기]

- 식량을 현행 핵심 HUD 자원으로 사용.
- 기본 건물 5종.
- 지휘소 주변 범위 오라.
- `15웨이브=1스테이지`·고정 60초.
- Danger에서 핵심 UI·정보 차단.
- Stage 중 숨은 필수 카운터 변경.
- 룰렛 전용 금화·병종 상징 아이콘.
- T3 병종 룰렛 토큰.
- 동일 건물 인스턴스 교차 분기·양쪽 T3.
- 건물 또는 병종 하나로 다섯 압력 전부 해결.
- 병종 수집량 기반 단순 세트 보너스를 기본 시너지로 사용.
- 반대 병영 계열 영구 삭제.
- 특정 병종이 없으면 통과 불가능한 단일 하드키 Stage.

## 5. [증거]

### Legacy Prototype 병종 데이터

```text
[증거] data/units/*.tres
status = LEGACY_PROTOTYPE_UNIT_DATA
authority = historical runtime/bootstrap evidence only
IMPLEMENTATION_INPUT_FORBIDDEN
```

`data/units/*.tres`의 이름·수치·태그는 현재 프로토타입이 존재했다는 사실만 증명한다. Decision 4/10 병종 정본, Decision 5/10 전술 정본, 수치 시뮬레이션, 별도 Codex 구현 계획과 제품 RED 테스트 전에는 신규 구현 입력으로 사용할 수 없다.

기타 증거:

- `docs/reviews/**`의 과거 PR·적대적 검토 기록.
- `docs/benchmarks/**`의 실험·Evidence Pilot.
- `docs/archive/**`.
- 완료된 PR·commit·CI run·Sheet 변경 이력.

`[증거]`는 사실을 증명하지만 현재 기획 규칙을 자동 변경하지 않는다.

## 6. 신규 작업자 규칙

1. `PROJECT_CORE.md`와 `DOCUMENTATION_MAP.md`를 먼저 읽는다.
2. 대상 파일이 `[현행]`인지 이 레지스트리에서 확인한다.
3. `[대체됨]`, `[보류]`, `[폐기]`를 구현 입력으로 사용하지 않는다.
4. 병종 작업은 4/10 책임 원본을 우선하고 `data/units/*.tres`를 정본으로 역추론하지 않는다.
5. 병종 수 변경은 역할 공백·중복·룰렛 학습량·아트 비용을 기록하고 별도 승인한다.
6. 제품 구현은 5/10 전술·수치 시뮬레이션·Codex 계획·제품 RED 테스트 뒤에만 시작한다.

## 7. 완료 이력 보존

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
```