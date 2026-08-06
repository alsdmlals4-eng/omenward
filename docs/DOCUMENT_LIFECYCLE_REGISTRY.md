# [현행] OMENWARD 문서 수명주기 레지스트리

```yaml
updated_at: 2026-08-06
policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
status: CURRENT_LIFECYCLE_AUTHORITY
approved_planning_status: MAIN_CANONICAL_APPROVED_10_OF_10
latest_approved_decision: OMW-DEC-20260806-PLANNING-CURRENT-MAPRUN-ECONOMY-AND-PRESSURE-BASELINE-V1
current_count: 3_OF_10
```

이 레지스트리는 파일명·과거 YAML·부분 문구보다 우선한다. 시뮬레이션 기준선은 제품 구현 권위가 아니다.

## [현행]

### 최상위 라우터

- `PROJECT_CORE.md`
- `ACTIVE_CONTEXT.md`
- `CURRENT_IMPLEMENTATION_STATUS.md`
- `DOCUMENTATION_MAP.md`
- `PROJECT_CANON_DECISION_LEDGER.md`
- `DECISIONS_PENDING.md`
- `HANDOFF_CONTEXT.md`
- `ONBOARDING_PLANNING_CURRENT_AUTHORITY.md`

### 승인 기획·분석 입력

- `design/APPROVED_OMENWARD_BARRACKS_AUTO_PRODUCTION_AND_TOKEN_SOURCE_AMENDMENT_2026-08-06.md`
- `design/APPROVED_ROULETTE_CORE_RULES.md`
- `design/APPROVED_OMENWARD_ONBOARDING_COMPLETION_MINIMUM_VALID_PATHS_AND_HUMAN_STOP_SHIP_2026-08-06.md`
- `design/APPROVED_OMENWARD_FIRST_10_15_MINUTES_FLOW_2026-08-05.md`
- `design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md`
- `design/APPROVED_OMENWARD_STAGE2_FIRST_T2_CANDIDATES_AND_GOLD_RULES_2026-08-06.md`
- `design/APPROVED_OMENWARD_SPECIAL_T1_RANDOM_SELECTION_AND_PREVIEW_TIMING_2026-08-06.md`
- `design/APPROVED_OMENWARD_BELU_INTERVENTION_FAILURE_RETRY_SKIP_RULES_2026-08-06.md`
- `design/APPROVED_OMENWARD_UNIT_BUILDING_TIER_MATRIX_AND_ARCHER_T3_CORRECTION_2026-08-06.md`
- `design/APPROVED_OMENWARD_BARRACKS_ECONOMY_PRODUCTION_TOKEN_SOURCE_SIMULATION_CONTRACT_2026-08-06.md`
- `design/APPROVED_OMENWARD_BARRACKS_SIMULATION_INPUT_PROVENANCE_MANIFEST_2026-08-06.md`
- `design/APPROVED_OMENWARD_CURRENT_MAPRUN_ECONOMY_AND_PRESSURE_BASELINE_2026-08-06.md`
- `analysis/barracks_simulation/input_provenance_manifest.v1.json`
- `analysis/barracks_simulation/current_maprun_economy_pressure_baseline.v1.json`

## [승인]

```text
decision = OMW-DEC-20260806-PLANNING-CURRENT-MAPRUN-ECONOMY-AND-PRESSURE-BASELINE-V1
status = APPROVED / 3_OF_10
simulation_runnable = TRUE_FOR_SMOKE_ONLY
smoke_sweep = READY_NOT_RUN
decision_sweep = BLOCKED_UNTIL_SMOKE_PASS
next_gate = BARRACKS_SMOKE_SWEEP_EXECUTION
```

## [제안]

- 현재 없음.

## [부분 대체됨]

- 2/10 manifest의 여섯 `MISSING_BLOCKER`: 3/10 smoke 기준값으로 `RESOLVED_FOR_SMOKE` 처리. 최종 제품 수치로 대체된 것은 아니다.
- `APPROVED_OMENWARD_BARRACKS_ECONOMY_PRODUCTION_TOKEN_SOURCE_SIMULATION_CONTRACT_2026-08-06.md`의 fractional TokenSource weight 축: 물리 릴 TokenInstance 축으로 대체.
- 7월 정규 15분 Stage 경제·특수병 생산 수치: 현행 절대값이 아니라 legacy PoC 후보로 강등.

## [대체됨]

- `design/PROPOSED_OMENWARD_BARRACKS_ECONOMY_PRODUCTION_TOKEN_SOURCE_SIMULATION_CONTRACT_2026-08-06.md`: 승인 계약으로 대체.
- 과거 모든 특수병 T1 TokenSource 무공급 조항: 병영 자동생산·TokenSource 정정으로 대체.
- 구형 6종 건물 공통 A/B 분기: 건물 Tier 재정렬로 대체.
- 대공궁병 T3 독립 분기: 궁병 T3 2분기 정정으로 대체.
- 로컬 공통 작업 정책: Base `AGENTS.md`로 대체.

## [보류]

- 2,000-seed smoke 결과와 판정.
- 10,000-seed decision 및 50,000-seed confirmation sweep.
- 최종 제품 비용·생산시간·Threat 수치.
- Stage 6~20 수치 확장.
- 최종 레벨 노드 좌표와 노드 수.
- 방어탑 T3 상세 효과.
- 승인된 수치의 제품 구현·데이터 마이그레이션.
- 12개 온보딩 시나리오와 첫 사용자 20명 검증.

## [폐기]

- fractional TokenInstance와 legacy board weight의 V2 확률 입력 사용.
- Foundation 지급 surplus.
- 정비시간 passive gold·자동생산 AFK 파밍.
- Stage 9 이전 강제 Wave overlap.
- 무료 재추첨·저장 재추첨.
- T3 병종 룰렛 토큰.
- 단일 하드키로만 통과 가능한 압력.
- 자동 전술 시전·복수 활성 마력탑·상시 무한 상점.

## [증거]

- 과거 PR·commit·CI·Sheet 이력.
- 대체된 승인 문서의 당시 결정 기록.
- `scripts/roulette/roulette_service.gd` legacy weighted-board 비교 증거.
- `data/units/*.tres` legacy prototype unit data.
- 완료·대체된 `superpowers/plans/**`.

## 제품·검증 경계

```text
PRODUCT_CODE = UNCHANGED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
SMOKE_SWEEP = READY_NOT_RUN
DECISION_SWEEP = BLOCKED_UNTIL_SMOKE_PASS
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
LOCAL_GODOT_PROJECT = UNCHANGED
```
