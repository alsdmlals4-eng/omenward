# [적대적 검토] 병영 시뮬레이션 입력 출처·룰렛 축

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PLANNING-BARRACKS-SIMULATION-INPUT-PROVENANCE-AND-ROULETTE-AXIS-CORRECTION-V1
status: ADVERSARIAL_REVIEW_FOR_APPROVED_PROVENANCE
approval_count: 2_OF_10
product_code_authority: NONE
```

## 결론

출처를 합치기만 하면 거짓 정밀도가 생긴다. 가장 큰 결함은 현행 물리 릴 정본과 legacy 가중치 보드 구현을 같은 확률 모델로 취급하는 것이다.

```text
FILENAME_APPROVED_IS_NOT_CURRENT_AUTHORITY
LEGACY_15_MIN_STAGE_CONTEXT_RISK
PHYSICAL_REEL_VS_WEIGHTED_BOARD_CONFLICT
MISSING_ASSASSIN_NUMERIC_RISK
QUALITATIVE_PRESSURE_AS_NUMERIC_TIMELINE_RISK
SHEET_REVISION_DRIFT_RISK
FALSE_GREEN_FROM_DIMENSIONLESS_ONLY_RISK
LEGACY_WEIGHTED_BOARD_CODE = NOT_V2_SIMULATION_AUTHORITY
PRODUCT_CODE = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
```

## 공격 시나리오

1. `APPROVED_STAGE_ECONOMY...`의 40금화를 현재 확정값으로 사용하면 20 Stage 구조와 정비 Clock을 무시한다.
2. `roulette_service.gd`의 `board_weight`를 사용하면 각 릴에 실제 TokenInstance가 들어가는 V2 확률과 전혀 다른 결과를 만든다.
3. 4종 특수병 생산시간 평균을 5종에 적용하면 암살자 결과의 기대값을 임의로 만든다.
4. 압력명만으로 Threat Budget을 생성하면 경로 유효율과 후회율이 설계자의 임의 점수에 종속된다.
5. `0.35~0.80` fractional weight를 물리 토큰으로 변환하면서 숨은 확률 보정 규칙을 추가하면 룰렛 핵심 계약을 우회한다.
6. Google Sheet 최신 revision이 바뀐 뒤 revision 386 결과를 현행이라고 부르면 provenance가 깨진다.

## 강제 규칙

```text
NO_ABSOLUTE_VALUE_WITHOUT_CURRENT_CONTEXT = TRUE
NO_FRACTIONAL_TOKEN_INSTANCE = TRUE
NO_LEGACY_BOARD_WEIGHT_AS_V2_INPUT = TRUE
NO_AVERAGE_ONLY_SPECIAL_BALANCE = TRUE
NO_ASSASSIN_VALUE_IMPUTATION = TRUE
NO_PRESSURE_TIMELINE_FABRICATION = TRUE
NO_SIMULATION_GREEN_WITH_BLOCKERS = TRUE
```

## 데이터 품질 판정

| 항목 | 판정 | 심각도 |
|---|---|---|
| 비용·생산 배수 | 승인된 무차원 가설 | 낮음 |
| 물리 릴 TokenSource 수 | 현행 정본 | 낮음 |
| 절대 건설비·회전비 | 구형 PoC 후보 | 높음 |
| 일반병 생산 초 | 누락 | 치명 |
| 암살자 생산 초 | 누락 | 치명 |
| MapRun 골드 시간축 | 구조 충돌·누락 | 치명 |
| 압력 Threat Budget·등장 초 | 누락 | 치명 |
| 정비시간 Clock | 누락 | 치명 |
| legacy board weight | 현행 V2와 충돌 | 치명 |

## Stop-ship

다음 중 하나라도 참이면 simulation sweep를 실행하지 않는다.

```text
GENERAL_PRODUCTION_INTERVAL_SECONDS_MISSING
ASSASSIN_PRODUCTION_INTERVAL_SECONDS_MISSING
CURRENT_MAPRUN_GOLD_TIMELINE_MISSING
ENEMY_THREAT_BUDGET_AND_TIMELINE_MISSING
MAINTENANCE_CLOCK_MATRIX_MISSING
FRACTIONAL_TOKEN_WEIGHT_USED
LEGACY_WEIGHTED_BOARD_USED_AS_V2
SOURCE_VERSION_OR_UNIT_MISSING
```
