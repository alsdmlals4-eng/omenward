# 적대적 검토 — 벨루 개입·실패·재시도·스킵

```yaml
decision_id: OMW-DEC-20260806-PLANNING-BELU-INTERVENTION-FAILURE-RETRY-SKIP-RULES-V1
reviewed_at: 2026-08-06 KST
result: CONDITIONALLY_ACCEPTABLE / HUMAN_QA_AND_PRODUCT_VALIDATION_PENDING
product_code_authority: NONE
```

## 검토 대상

```text
짧은 기본 설명
→ 플레이어 직접 판단
→ 유효하지 않은 행동은 규칙만 교정
→ 첫 실패 뒤 원인 1개 + 방향 1개
→ 같은 Stage 반복 실패 때만 선택형 확장 힌트
→ 같은 Stage 시작 상태로 복구
```

## 주요 위험

### BELU_OVERCOACHING

벨루가 최적 건물·분기·배치·전술을 직접 말하면 플레이어 선택이 사라진다.

완화: 자동 선택·건설·배치·시전과 최적답 공개를 금지하고 힌트는 관찰 가능한 원인과 방향으로 제한한다.

### RETRY_FARMING

실패 시도의 골드·보상·소모품을 유지하면 반복 실패가 파밍 수단이 된다.

완화: 실패 시도 보상 커밋과 중복 보상을 금지하고 Stage 시작 스냅샷을 복원한다.

### SEED_REROLL_EXPLOIT

재시도마다 seed·예고·특수병 결과·상점 재고가 바뀌면 실패가 무료 재추첨이 된다.

완화: 같은 Run seed와 확정된 무작위 결과를 보존하고 상점 갱신과 재선정을 금지한다.

### MANDATORY_ACTION_SKIP

첫 클리어 전에 설명과 함께 실전 행동까지 건너뛰면 건물→룰렛→배치→전투 인과를 배우지 못한다.

완화: 대사·반복 설명·연출 축약만 허용하고 필수 건설·배치·T2·전술·Danger·Boss 판단 스킵을 금지한다.

### FAKE_RULE_PARITY

체크포인트 복구가 일반 Run에도 적용되는 것으로 오해되면 본편 실패 규칙 기대가 왜곡된다.

완화: 첫 클리어 전 온보딩 전용 안전장치임을 고지하고 첫 클리어 후에는 표준 Run 실패 규칙을 사용한다.

### LEARNED_HELPLESSNESS

실패할수록 벨루가 정답을 더 직접 알려주면 플레이어가 스스로 관찰하지 않고 지시를 기다리게 된다.

완화: 첫 실패는 원인 하나와 방향 하나만 제공하고 확장 힌트도 선택형으로 유지한다. 자동 조작과 승리 보장은 금지한다.

### CHECKPOINT_STATE_DRIFT

복구 시 골드·건물·생산 타이머·확정 선택 일부만 이전 상태로 돌아가면 중복 지급이나 진행 불능이 생길 수 있다.

완화: Stage 시작 스냅샷을 원자적으로 복원하고 정확한 직렬화·마이그레이션은 제품 RED 테스트 뒤 확정한다.

## Stop-ship

다음 중 하나라도 사람 QA에서 반복되면 구현 승인을 중단한다.

1. 벨루가 선택을 사실상 대신한다.
2. 첫 실패 힌트만 읽어도 정답 절차가 완성된다.
3. 실패·재시도로 경제 또는 무작위 이득을 얻는다.
4. 복구 뒤 예고·특수병 결과·확정 선택이 달라진다.
5. 첫 클리어 전 필수 실전 행동을 스킵할 수 있다.
6. 첫 클리어 후 스킵으로 보상을 다시 받는다.
7. 온보딩 복구가 일반 Run 규칙으로 오해된다.
8. 반복 힌트가 자율 판단을 감소시킨다.

## 검증 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
FULL_PLANNING_SUITE = NOT_RUN
```

## 결론

선택을 대신하지 않는 짧은 설명과 동일 Stage 시작점 복구는 첫 학습의 좌절을 낮추면서 핵심 인과를 유지할 수 있다. 다만 체크포인트 상태 무결성, 파밍 차단, 힌트가 자율 판단에 미치는 영향은 제품 구현과 사람 플레이 전까지 미검증이다.
