# 오멘워드 V2 전설 획득·배치 제한 적대적 검수

- 검수일: 2026-07-26
- 상태: `REVIEW_DECISION_APPROVED / DOCUMENTATION_SYNC_IN_PROGRESS`
- 제품 구현: `V2_IMPLEMENTATION_NOT_STARTED`
- 제품 코드 승인: `NO`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- 상위 정본: `docs/PROJECT_CORE.md`
- 승인 문서: `docs/design/APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md`
- 관련 거래 순서: `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`

## F-10 — 전설 제한의 적용 시점이 잘못됨

### 기존 위험

기존 정본은 5스테이지 위험 주기마다 전설 획득을 1회로 제한하고, 추가 전설 결과를 룰렛 `[확정]` 시 영웅 2기로 변환했다.

이 구조는 다음 문제를 만들었다.

- 좋은 룰렛 결과 자체가 주기 상태 때문에 즉시 강등됨.
- 전설을 보관·판매·배치하는 전략 판단 전에 결과가 변함.
- 미확정 SpinSession이 stage 경계를 넘을 때 어느 주기를 소비하는지 추가 문맥이 필요함.
- 획득 제한과 전장 밸런스 제한이 하나의 규칙에 섞임.

### 사용자 승인 결정

```text
전설 획득 제한 없음
→ 전설 결과는 항상 전설 PendingReward
→ 보관·판매 가능
→ 플레이어 전장에는 생존 전설 최대 1기
→ 두 번째 전설 배치 시 경고
→ 충돌이 실제 커밋 순간에도 존재하면 같은 세부 병종 영웅 2기로 원자 배치
```

### 커밋 순간 재검증 — A안

- 경고 확인 뒤 기존 전설이 사망했으면 새 보상을 전설 그대로 배치한다.
- 경고 없이 시작했지만 커밋 순간 다른 생존 전설이 생겼으면 자동 강등하지 않는다.
- 해당 transaction은 무변경으로 중단하고 최신 상태를 기준으로 경고를 새로 표시한다.
- 사용자의 명시적 동의 없이 전설을 영웅으로 바꾸지 않는다.

### 패키지 영향

- R4: 전설 결과를 항상 전설 PendingReward로 확정. 주기 소비와 영웅 변환 제거.
- U1-F: 전설 payload를 원래 등급 그대로 동결.
- U1-C: 승인된 배치 충돌에 한해 동일 세부 병종 영웅 payload 2개 조합.
- S1-F: 전설 PendingReward 여러 개 보존.
- S1-C: 생존 전설 조회, 경고 동의, 커밋 재검증, 원자 변환 배치와 rollback.
- L1/Battle: 실제 spawn과 `is_alive`를 생존 전설 판정 근거로 제공.

### 판정

```text
LEGENDARY_ACQUISITION_CAP: REMOVED
LEGENDARY_BATTLEFIELD_LIMIT: PLAYER_ALIVE_MAX_ONE
SECOND_DEPLOYMENT: EXPLICIT_WARNING_REQUIRED
COMMIT_TIME_REVALIDATION: REQUIRED
NO_CONSENT_AUTO_DOWNGRADE: FORBIDDEN
R1_R2_SCOPE: UNCHANGED
PRODUCT_CODE_AUTHORIZED: NO
```

## 다음 적대적 검토 항목

일반 전술계획에서 전설 배치 명령 두 개를 동시에 예약했을 때 첫 번째 적용 후 두 번째 명령이 생존 전설 제한과 충돌할 수 있다.

현재 미결정:

- 전투 재개를 중단하고 두 번째 명령에 경고를 요구할지.
- 두 번째 명령만 보류하고 나머지 예약 명령은 적용할지.
- 계획 단계에서 전설 배치 예약을 순서 의존적으로 검증할지.

이 항목은 사용자에게 별도 질문하기 전까지 구현 결정을 내리지 않는다.

## 현재 게이트

```text
DOCUMENTATION_DECISION: APPROVED
DOCUMENTATION_CI: PENDING
FINAL_CODEX_HANDOFF: BLOCKED_UNTIL_EXACT_REVIEW_COMPLETE_COMMAND
V2_IMPLEMENTATION: NOT_STARTED
CORE_LOCK_V2: PENDING
```
