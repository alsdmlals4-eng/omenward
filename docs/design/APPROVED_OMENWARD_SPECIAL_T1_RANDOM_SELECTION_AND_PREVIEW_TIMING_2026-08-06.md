# OMENWARD 특수병 병영 T1 무작위 선정·공개 시점 승인 계약

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PLANNING-SPECIAL-T1-RANDOM-SELECTION-AND-PREVIEW-TIMING-V1
parent_decision_id: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
approval: USER_APPROVED_RECOMMENDED_OPTION_B
status: USER_APPROVED_PLANNING_CANON / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 목적

특수병 병영 T1이 마도사·사제·암살자·비행병·거인 중 무엇을 생산할지 정하는 시점과, 그 결과를 플레이어에게 공개하는 시점을 소유한다.

```text
DECISION_STATUS = PARTIAL_APPROVAL_8_OF_10
APPROVAL_CHECKPOINT = SPECIAL_T1_RANDOM_SELECTION_AND_PREVIEW_TIMING
```

건물 Tier·자동생산·TokenSource의 상위 계약은 다음을 따른다.

- `docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md`
- `docs/design/APPROVED_OMENWARD_UNIT_BUILDING_TIER_MATRIX_AND_ARCHER_T3_CORRECTION_2026-08-06.md`

## 2. T1 무작위 선정 계약

```text
SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT
SPECIAL_T1_SELECTION_POOL = MAGE / PRIEST / ASSASSIN / FLYING_UNIT / GIANT
SPECIAL_T1_SELECTION_COUNT = ONE
SPECIAL_T1_SELECTION_SCOPE = PER_BUILDING_INDEPENDENT
SPECIAL_T1_SELECTED_UNIT_PERSISTENCE = FIXED_WHILE_BUILDING_REMAINS_T1
SPECIAL_T1_REPEATED_PRODUCTION = SELECTED_UNIT_ONLY
SPECIAL_T1_TOKEN_SOURCE = NONE
```

- 특수병 병영 건설 거래가 성공적으로 확정되는 순간 해당 병영의 T1 생산 병종을 한 번 추첨한다.
- 한 병영은 T1 상태를 유지하는 동안 처음 선정된 병종만 반복 자동생산한다.
- 매 생산 주기마다 병종을 다시 추첨하지 않는다.
- 여러 특수병 병영은 서로 독립적으로 한 번씩 추첨한다.
- T1 특수병 병영은 룰렛 TokenSource를 제공하지 않는다.

## 3. 결과 공개와 생산 타이머

```text
SPECIAL_T1_RESULT_REVEAL = IMMEDIATELY_AFTER_CONSTRUCTION_COMMIT
SPECIAL_T1_PRECOMMIT_RESULT_PREVIEW = FORBIDDEN
SPECIAL_T1_PRODUCTION_TIMER_START = AFTER_RESULT_REVEAL
REVEAL_NAME_ICON_ROLE = REQUIRED
REVEAL_FIRST_PRODUCTION_COUNTDOWN = REQUIRED
```

건설 비용 지불·노드 점유·건물 생성이 모두 확정된 직후 결과를 공개한다. 결과 공개 뒤 첫 자동생산 타이머를 시작한다.

공개 UI는 최소한 다음을 표시한다.

- 선정된 특수병의 이름과 아이콘.
- 한 문장 역할 설명.
- 첫 생산까지 남은 시간.
- T1에서는 해당 병종을 반복 생산하며 TokenSource는 없다는 사실.
- T2에서 플레이어가 원하는 특수병 계열로 전문화할 수 있다는 사실.

건설 확정 전 결과를 미리 보여주거나, 결과를 보고 무료로 건설을 취소하는 방식은 허용하지 않는다.

## 4. 저장·재추첨 방지 계약

```text
SPECIAL_T1_SELECTION_SAVE_PERSISTENCE = REQUIRED
SPECIAL_T1_SAVE_RELOAD_RESELECT = FORBIDDEN
SPECIAL_T1_FREE_REROLL = FORBIDDEN
SPECIAL_T1_REVEAL_THEN_FREE_CANCEL = FORBIDDEN
SPECIAL_T1_FAILED_CONSTRUCTION_SELECTION = NOT_COMMITTED
```

- 선정 결과와 생산 타이머 상태는 저장 데이터에 보존한다.
- 저장·불러오기, 체크포인트 복구, Scene 재진입으로 결과를 다시 뽑지 않는다.
- 건설 거래가 실패하거나 원자적으로 롤백되면 선정 결과도 확정되지 않는다.
- 결과 공개 뒤 무료 취소·무료 철거·전액 환급으로 새 결과를 반복 뽑는 경로를 만들지 않는다.
- 철거와 재건설 자체가 허용되는 경우에도 본편의 실제 비용·환불·시간 규칙을 적용한다. 정확 환불률은 별도 경제 결정과 시뮬레이션 대상으로 남긴다.

## 5. T2 전문화 연결

```text
SPECIAL_T2_SPECIALIZATION_OVERRIDES_T1_SELECTION = TRUE
SPECIAL_T2_SELECTED_UNIT_TOKEN_SOURCE = ENABLED
SPECIAL_T2_SELECTION = PLAYER_CHOSEN
```

T2 업그레이드에서는 T1의 무작위 결과와 무관하게 마도사·사제·암살자·비행병·거인 중 하나를 플레이어가 선택한다.

T2 전문화가 완료되면 다음이 적용된다.

- 자동생산 병종을 선택한 T2 특수병으로 교체.
- 선택 특수병 TokenSource 해금.
- T1 무작위 결과는 더 이상 생산 정체성을 결정하지 않음.

업그레이드 중 이미 진행 중인 T1 생산 타이머의 취소·전환·보상 규칙은 제품 구현 전에 별도 원자적 거래 계약으로 확정한다.

## 6. 전투·온보딩 가드레일

```text
SPECIAL_T1_RESULT_HARD_COUNTER_REQUIREMENT = FORBIDDEN
ALL_SPECIAL_T1_RESULTS_MUST_HAVE_VALID_USE = REQUIRED
SCRIPTED_SPECIAL_T1_RESULT = FORBIDDEN
```

- 다섯 결과 중 특정 결과가 없으면 다음 전투를 정상 진행할 수 없는 구조를 금지한다.
- 무작위 결과는 플레이 방식을 바꾸는 기회여야 하며 성공·실패를 미리 결정하는 하드키가 되어서는 안 된다.
- 첫 건설에서 특정 병종이 반드시 나오도록 결과를 각본으로 조작하지 않는다.
- 특수병 병영은 Stage 1 의무 건물이 아니므로, 플레이어는 무작위성과 긴 생산시간을 감수할지 선택한 뒤 건설한다.

## 7. 정확 수치 경계

```text
SPECIAL_T1_SELECTION_WEIGHTS = PENDING_SIMULATION
SPECIAL_T1_PRODUCTION_INTERVAL = PENDING_SIMULATION
SPECIAL_T1_BUILD_COST = PENDING_SIMULATION
SPECIAL_T1_DEMOLITION_REFUND = PENDING_SIMULATION
```

다섯 병종의 추첨 가중치, 생산시간, 건설비용, 철거 환급률은 이번 승인으로 확정하지 않는다. 초기 시뮬레이션에서는 동일 가중치를 기준선으로 비교할 수 있지만 제품 확정값으로 간주하지 않는다.

## 8. 금지 규칙

```text
SPECIAL_T1_REROLL_EVERY_PRODUCTION = FORBIDDEN
SPECIAL_T1_HIDDEN_UNTIL_FIRST_PRODUCTION = FORBIDDEN
SPECIAL_T1_PRECOMMIT_RESULT_PREVIEW = FORBIDDEN
SPECIAL_T1_SAVE_SCUM_REROLL = FORBIDDEN
SPECIAL_T1_FREE_CANCEL_REROLL = FORBIDDEN
SPECIAL_T1_TOKEN_SOURCE = NONE
```

## 9. 제품 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
ART_ASSETS = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

이 결정은 기획 정본만 승인한다. 실제 난수 시드, 저장 스키마, 건설 거래, UI, 생산 타이머 구현은 별도 제품 계획과 RED 테스트가 필요하다.

## 10. 다음 GrillMe

다음 결정은 **벨루의 온보딩 개입 수준과 실패·재시도·스킵 규칙**이다.
