# 벨루 개입·실패·재시도·스킵 설계

```yaml
decision_id: OMW-DEC-20260806-PLANNING-BELU-INTERVENTION-FAILURE-RETRY-SKIP-RULES-V1
status: USER_APPROVED_DESIGN / NOT_IMPLEMENTED
```

## 목표 흐름

```text
짧은 설명
→ 플레이어 직접 행동
→ 잘못된 입력은 해당 규칙만 교정
→ 첫 실패는 원인 1개 + 방향 1개
→ 같은 Stage 시작점 복구
→ 반복 실패 시 선택형 확장 힌트
```

벨루는 정답 제공자가 아니라 플레이어가 결과를 해석하도록 돕는 관찰 보조자다.

## 힌트 계층

1. 기본: 시스템 목적 한 문장과 UI 강조.
2. 유효하지 않은 행동: 위반한 규칙만 짧게 교정.
3. 첫 실패: 관찰 가능한 실패 원인 하나와 대응 방향 하나.
4. 같은 Stage 반복 실패: 선택형 확장 힌트.
5. 모든 단계: 자동 선택·자동 조작·승리 보장 금지.

정확한 실패 횟수와 문구는 사람 QA에서 결정한다.

## 재시도 상태 모델

```text
STAGE_START_SNAPSHOT
→ PLAYER_ACTIONS
→ COMBAT_ATTEMPT
→ SUCCESS: 결과 커밋
→ FAILURE: 임시 결과 폐기
→ STAGE_START_SNAPSHOT 복원
```

스냅샷에는 Run seed, 예고, 확정된 건물·분기·특수병 T1 결과, Stage 시작 골드·재고·건물·생산 상태가 포함된다.

실패 시도에서 발생한 보상·골드·소모품·상점 갱신·무작위 재선정은 커밋하지 않는다.

## 스킵 상태

```text
FIRST_CLEAR_NOT_DONE
= 대사·반복 설명·연출 축약 가능
= 필수 행동·Stage·결정 자동 해결 금지

FIRST_CLEAR_DONE
= 전체 온보딩 스킵 가능
= 표준 Run 시작
= 튜토리얼 지급·첫 클리어 보상 재지급 금지
= 설정에서 보상 없는 재학습 가능
```

## 첫 클리어 전 필수 행동

- 여섯 필수 T1 건설과 세팅 확인.
- 첫 룰렛 확인과 비가역 배치.
- Stage 2 방패병·궁병 T2 선택.
- 마력탑 연구와 첫 수동 전술.
- 첫 Danger와 Boss의 핵심 판단.

## 구현 전 검증

### 제품 RED 테스트

- 실패 복구 뒤 seed와 확정 무작위 결과가 같은지.
- 실패 시도 보상과 골드가 남지 않는지.
- Stage 시작 건물·생산 타이머·재고가 정확히 복원되는지.
- 첫 클리어 전 필수 행동을 스킵할 수 없는지.
- 첫 클리어 후 전체 스킵이 표준 Run과 중복 보상 없이 시작되는지.

### 사람 QA

- 벨루가 선택을 대신한다고 느끼지 않는지.
- 첫 실패 힌트가 원인을 이해시키되 정답을 직접 주지 않는지.
- 복구 규칙과 일반 Run 실패 규칙을 구분하는지.
- 반복 실패에도 스스로 계획을 바꾸는지.

## 범위 밖

- 실제 GDScript·Scene·Resource 구현.
- 체크포인트 직렬화 포맷과 저장 마이그레이션.
- 정확한 힌트 문구·횟수·노출 시간.
- 일반 Run의 최종 실패·부활·종료 경제.

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
