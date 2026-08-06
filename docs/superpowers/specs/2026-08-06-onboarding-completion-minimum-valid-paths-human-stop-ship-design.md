# OMENWARD 온보딩 완료·최소 유효 경로·사람 검증 설계

```yaml
decision_id: OMW-DEC-20260806-PLANNING-ONBOARDING-COMPLETION-MINIMUM-VALID-PATHS-HUMAN-STOP-SHIP-V1
status: APPROVED_DESIGN_10_OF_10 / NOT_IMPLEMENTED
```

## 완료 상태기계

```text
IN_PROGRESS
→ Stage 1 milestone committed
→ Stage 2 milestone committed
→ Stage 3 milestone committed
→ Stage 4 milestone committed
→ Stage 5 Boss result committed
→ post-Boss summary acknowledged
→ ATOMIC_FIRST_CLEAR_COMMIT
→ COMPLETE
```

`ATOMIC_FIRST_CLEAR_COMMIT`은 다음 상태를 함께 저장한다.

- `onboarding_first_clear = true`
- 첫 클리어 보상 지급 완료
- 표준 Run 해금
- 전체 온보딩 스킵 해금
- 재학습 모드 해금

중간 단계에서 완료 플래그나 보상 일부를 먼저 저장하지 않는다.

## 필수 이벤트 기록

### Stage 1

- 여섯 필수 T1 건설 완료.
- Foundation 세팅 확인.
- 첫 룰렛 확인.
- 첫 비가역 배치.
- 실제 전투 종료.
- 인과 복기와 첫 상인 확인.

### Stage 2

- 방패병 또는 궁병 T2 선택 확정.
- 생산 병종·TokenSource 변화 확인.
- 룰렛 통제 직접 사용.
- 전선 판단과 비가역 배치.

### Stage 3

- 마력탑 전술 연구.
- 전술을 유효한 전투 상황에서 수동 시전.

### Stage 4

- Danger 예고 확인.
- 플레이어가 대응 조정 하나 이상 실행.

### Stage 5

- 실제 규칙으로 Boss 처치.
- 결과 요약 확인.

## 최소 플레이 경로

```text
PATH_A = SHIELD / NO_SPECIAL_REQUIRED
PATH_B = ARCHER / NO_SPECIAL_REQUIRED
```

두 경로는 다음 조건을 만족해야 한다.

- 디버그·치트·진행자 지시 없이 완료 가능.
- 특정 특수병 결과를 요구하지 않음.
- Boss가 한 경로만 하드 카운터하지 않음.
- 선택하지 않은 T2 경로를 전역 잠금하지 않음.

## 내부 QA 행렬

```text
BASELINE
1. Shield / no Special Barracks
2. Archer / no Special Barracks

SPECIAL MATRIX
3~7. Shield × Mage/Priest/Assassin/Flying/Giant
8~12. Archer × Mage/Priest/Assassin/Flying/Giant
```

각 시나리오는 고정 seed QA와 정상 seed QA를 구분해 기록한다. 고정 seed는 재현성 검사용이며 플레이어 제품 경로의 무작위 조작을 의미하지 않는다.

## 사람 검증 계획

### 표본

- 첫 플레이어 최소 20명.
- 방패병·궁병 각 10명 이상.
- 이전 OMENWARD 플레이 경험자는 첫 플레이어 표본에서 제외.

### 진행 원칙

- 플레이 중 정답·건설 위치·분기·전술 지시 금지.
- 기술 오류 확인을 위한 중단만 허용.
- 관찰 기록과 세션 후 인터뷰 허용.

### 수집 지표

- 무개입 완료 여부.
- 소요 시간.
- 실패 횟수와 힌트 단계.
- 선택한 T2 경로.
- 각 Stage에서 막힌 지점.
- 사후 인과 설명 정답 여부.
- 온보딩 재시도와 표준 Run 실패 규칙 구분 여부.

### 합격선

```text
FIRST_TIME_HUMAN_SAMPLE_MINIMUM = TWENTY
PER_T2_PATH_SAMPLE_MINIMUM = TEN
OVERALL_UNASSISTED_COMPLETION_RATE_MINIMUM = 0.85
PER_PATH_UNASSISTED_COMPLETION_RATE_MINIMUM = 0.80
PATH_COMPLETION_RATE_GAP_MAXIMUM = 0.20
TARGET_MEDIAN_DURATION_MINUTES = 10_TO_15
DURATION_P90_MAXIMUM_MINUTES = 20
CORE_CAUSAL_UNDERSTANDING_RATE_MINIMUM = 0.80
```

## 제품 RED 테스트 요구

- 필수 마일스톤 누락 시 완료 플래그가 켜지지 않는다.
- Boss 처치 전 완료 플래그와 첫 보상이 커밋되지 않는다.
- Boss 처치 뒤 요약 미확인 상태에서는 완료 거래가 보류된다.
- 완료 거래 중 실패하면 모든 완료 관련 상태를 롤백한다.
- 재시도 뒤 seed·예고·특수병 결과·Stage 시작 자원이 유지된다.
- 실패 시도 보상·골드·상점 갱신이 남지 않는다.
- 첫 클리어 전 필수 행동을 스킵할 수 없다.
- 첫 클리어 후 전체 스킵은 중복 보상 없이 표준 Run으로 진입한다.
- 온보딩 체크포인트 복구 규칙이 표준 Run에 적용되지 않는다.

## 제품 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

이 명세는 구현 순서와 검증 계약만 정의한다. 실제 GDScript·Scene·Resource·저장 포맷은 별도 구현 계획과 제품 RED 테스트 승인 뒤 변경한다.
