# [현행] OMENWARD 문서 수명주기 레지스트리

```yaml
updated_at: 2026-08-05
policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
status: CURRENT_LIFECYCLE_AUTHORITY
current_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
current_count: 7_OF_10_IN_PROGRESS
approval_checkpoint: PARTIAL_APPROVAL_1_OF_10
```

이 레지스트리는 파일명·과거 YAML·부분 문구보다 우선한다. `[대체됨]`, `[보류]`, `[폐기]` 문서는 신규 기획·Codex 구현·아트 제작 입력으로 사용하지 않는다.

## 1. [현행]

### 최상위·운영

- `PROJECT_CORE.md`
- `OMENWARD_GDD_CURRENT_CANON.md`
- `ACTIVE_CONTEXT.md`
- `CURRENT_IMPLEMENTATION_STATUS.md`
- `DOCUMENTATION_MAP.md`
- `process/APPROVED_DYNAMIC_CURRENT_MAIN_AND_DOCUMENT_LIFECYCLE_POLICY_2026-08-04.md`
- `process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md`

### Planning Batch

- 1/10 `design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md`
- 2/10 `design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- 3/10 `design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`
- 4/10 `design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`
- 5/10 `design/APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md`
- 6/10 `design/APPROVED_OMENWARD_STAGE_END_MERCHANT_2026-08-05.md`
- 6/10 Spec `superpowers/specs/2026-08-05-stage-end-merchant-design.md`
- 6/10 Amendment `superpowers/specs/2026-08-05-stage-end-merchant-design-amendment.md`
- 6/10 Plan `superpowers/plans/2026-08-05-stage-end-merchant.md`
- 6/10 Review `reviews/ADVERSARIAL_STAGE_END_MERCHANT_ECONOMY_AND_INVENTORY_REVIEW_2026-08-05.md`
- 7/10 partial `design/APPROVED_OMENWARD_FIRST_10_15_MINUTES_FLOW_2026-08-05.md`
- 7/10 partial Spec `superpowers/specs/2026-08-05-first-10-15-minutes-flow-checkpoint-1.md`
- 7/10 partial Plan `superpowers/plans/2026-08-05-first-10-15-minutes-flow-checkpoint-1.md`
- 7/10 partial Review `reviews/ADVERSARIAL_FIRST_10_15_MINUTES_FLOW_FORMAT_REVIEW_2026-08-05.md`

```text
OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
7_OF_10_IN_PROGRESS
PARTIAL_APPROVAL_1_OF_10
```

### 현행 시스템

- `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`: 전체 시스템 연결 계보.
- `design/APPROVED_OMENWARD_COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_AND_BUILDING_ROSTER_2026-08-04.md`: HUD·룰렛·기본 건물 역할. 상인 세부 규칙은 6/10 우선.
- `design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`: 다섯 분기 건물과 과거 결정 계보. 마력탑 부분은 5/10 우선.
- `design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`: 병종 대응망.
- `design/APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md`: 전술·마력.

## 2. [대체됨]

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

```text
LEGACY_SEPARATE_TUTORIAL
status = SUPERSEDED_BY_DECISION_7_OF_10_PARTIAL_1
replacement = real MapRun in-run progressive disclosure
IMPLEMENTATION_INPUT_FORBIDDEN
```

```text
LEGACY_STAGE1_FULL_SYSTEM_DUMP
status = SUPERSEDED_BY_DECISION_7_OF_10_PARTIAL_1
replacement = objective-relevant progressive disclosure
IMPLEMENTATION_INPUT_FORBIDDEN
```

```text
LEGACY_SCRIPTED_TUTORIAL_VICTORY
status = SUPERSEDED_BY_DECISION_7_OF_10_PARTIAL_1
replacement = real economy and combat result rules
IMPLEMENTATION_INPUT_FORBIDDEN
```

대체되는 과거 규칙:

- 유량 계열과 저장 계열 마력탑 분기.
- 상시 HUD 상점·전투 중 구매·무한 재고·무한 reroll.
- 병종·T3·Hero·Legendary·전술스킬·마력·건물 분기 직접 판매.
- 별도 연습장 튜토리얼·Stage 1 전체 시스템 덤프·보장된 튜토리얼 승리.

기타 대체 문서:

- `OMENWARD_GAME_DESIGN.md`: `OMENWARD_GDD_CURRENT_CANON.md`이 승계.
- `design/APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md`: 20 Stage 정본으로 대체.
- 과거 post-merge Sync 문서: 당시 증거만 보존.

## 3. [보류]

- 7/10 시스템 노출 순서·첫 실질 선택·최소 유효 경로·벨루 개입 수준·Danger/Boss·상인 노출·실패/재시도·사람 QA 기준: 후속 GrillMe 승인 전 구현 입력 금지.
- Hero·Legendary 문서군: 8/10 재조정 전 구현 입력 금지.
- Meta·Hub 문서군: 9/10 재조정 전 구현 입력 금지.
- 구형 구현 계획: 재실행 금지, 과거 결정·검증 증거로만 사용.

## 4. [폐기]

- 식량을 현행 핵심 HUD 자원으로 사용.
- 기본 건물 5종.
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

`[증거]`는 과거 사실을 증명하지만 현재 규칙을 자동 변경하지 않는다.

## 6. 신규 작업자 규칙

1. `PROJECT_CORE.md`와 `DOCUMENTATION_MAP.md`를 먼저 읽는다.
2. 대상 파일이 `[현행]`인지 확인한다.
3. 온보딩 작업은 7/10 부분 승인 책임 원본을 우선하되 `PENDING_GRILLME`를 임의 해소하지 않는다.
4. 상인 작업은 완료된 6/10 책임 원본을 우선한다.
5. 정확 수치는 시뮬레이션·Codex 계획·제품 RED 테스트 뒤에만 확정한다.

## 7. 완료 이력

```text
OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
6_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
LEGACY_C1_C2_C3_PROVEN
```
