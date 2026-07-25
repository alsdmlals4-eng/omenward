# 승인된 V2 보상·확정 거래 기반 순서

- 승인일: 2026-07-26
- 상태: `APPROVED_REVIEW_DECISION / V2_IMPLEMENTATION_NOT_STARTED`
- 제품 코드 승인: `NO`
- 상위 책임: 최신 사용자 지시, `docs/PROJECT_CORE.md`, `docs/design/APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md`, 통합 결정 원장
- 관련 검수: `docs/reviews/2026-07-26-v2-r1-r2-planning-review.md`

이 문서는 전체 V2 적대적 검토 중 발견된 R4·U1·S1 순서 충돌을 해결한다. 제품 코드를 구현하지 않으며 각 패키지는 별도 Plan Mode와 사용자 승인 전에는 Build할 수 없다.

## 1. 발견된 충돌

기존 로드맵은 다음 순서였다.

```text
R3
→ R4: 이동·럭키·전설·[확정] 원자 거래
→ U1: 세부 병종·Tier·등급·능력 생성
→ S1: PendingReward·보관·판매·식량
```

그러나 `[확정]`은 최종 보상 payload와 PendingReward를 같은 거래에서 생성해야 한다. R4가 U1과 S1보다 먼저 오면 임시 payload, 확정 후 live 상태 재조회, 보상 없는 확정 중간 상태 또는 중복 지급 위험이 생긴다.

## 2. 승인된 순서

```text
R3
→ U1-F: UnitRewardPayload foundation
→ S1-F: PendingReward foundation
→ R4: 이동·럭키·항상-전설 보상·원자 확정
→ U1-C: unit composition·AI completion
→ S1-C: 보관·판매·배치·식량·전설 배치 제한 completion
```

## 3. U1-F 책임

U1-F는 순수하고 불변인 `UnitRewardPayload` 조합만 소유한다.

필수 데이터:

```text
family_symbol_id
source_building_instance_id
source_completed_tier
selected_unit_variant_id
reward_grade
passive_unlock_ids
passive_upgrade_ids
active_skill_unlock_ids
active_skill_upgrade_ids
active_skill_priority
active_skill_trigger_conditions
```

계약:

- 입력은 `SpinSnapshot`과 최종 확정 보드다.
- snapshot에 동결된 후보·가중치·Tier·세부 병종 데이터만 사용한다.
- 확정 후 live 건물 또는 live 릴을 재조회하지 않는다.
- 전설 결과는 횟수·stage 주기와 무관하게 `reward_grade = legendary`로 동결한다.
- deterministic serialization과 deep-copy/copy-out을 제공한다.
- 전투 유닛 spawn, AI 실행, Scene 연결은 소유하지 않는다.

## 4. S1-F 책임

S1-F는 결과 저장의 최소 기반만 소유한다.

필수 식별자:

```text
spin_session_id
confirm_transaction_id
pending_reward_id
reward_index
```

필수 계약:

- `PendingRewardEnvelope`는 immutable reward payload와 식별자를 보존한다.
- `PendingRewardStore.put_once()`는 같은 `pending_reward_id`의 중복 생성을 거부하고 기존 결과를 반환할 수 있다.
- 같은 `confirm_transaction_id`의 모든 reward를 조회할 수 있다.
- `ConfirmReceipt`를 transaction ID로 다시 조회할 수 있다.
- 전설 PendingReward를 원래 전설 등급 그대로 여러 개 보존할 수 있다.
- 보관함, 판매, 라인 배치, 식량, 실제 spawn은 소유하지 않는다.

## 5. R4 원자 확정 계약

R4는 U1-F와 S1-F를 소비해 다음을 하나의 idempotent transaction으로 처리한다.

```text
최종 보드 평가
→ 출처·Tier·등급·UnitRewardPayload 결정
→ 럭키 실패 카운터 최종화
→ BlankMoveCounter·PendingMoveReward 최종화
→ 전설 결과도 등급 변경 없이 PendingReward put-once
→ 금화 credit 또는 PendingReward put-once
→ transaction 완료 기록
→ SpinSession close
→ ConfirmReceipt 반환
```

R4는 다음을 하지 않는다.

- 5스테이지 전설 주기 조회·소비.
- 전설 결과의 확정 시 영웅 2기 변환.
- live 전장 생존 전설 조회.
- 배치 경고와 배치 동의 처리.

원자성:

```text
전체 성공
또는
아무 상태도 변경되지 않음
```

두 번째 동일 확정 요청은 새 보상이나 금화를 만들지 않고 기존 `ConfirmReceipt`를 반환한다.

## 6. U1-C 책임

- payload를 실제 `UnitSpawnDefinition` 또는 후속 V2 유닛 생성 데이터로 조합한다.
- Tier 패시브와 등급 액티브를 실제 전투 유닛에 적용한다.
- 작성된 AI 우선순위와 trigger를 연결한다.
- R4의 확정 결과를 변경하지 않는다.
- S1-C의 전설 충돌 배치가 승인되면 원래 전설과 같은 출처·Tier·세부 병종의 영웅 등급 payload 2개를 결정론적으로 조합한다.

## 7. S1-C 책임

- PendingReward의 보관·판매·라인 배치 상태 전이.
- 보관함 4칸과 초과 결과 전체 대기.
- 식량 예약·반환.
- 플레이어 전장에 실제 생존 전설 최대 1기 적용.
- 전설 PendingReward 배치 시 현재 생존 전설 충돌 경고와 명시적 동의.
- 실제 배치 커밋 순간 생존 전설 수 재검증.
- 경고 확인 뒤 기존 전설이 사망했으면 원래 전설 그대로 배치.
- 경고 없이 시작했지만 커밋 순간 새 충돌이 생기면 무변경 중단 후 경고를 새로 요구.
- 충돌이 계속되면 동일 세부 병종 영웅 2기를 같은 라인에 원자 배치.
- 실제 spawn 실패 시 식량·pending 상태·로그를 함께 rollback하는 원자 배치 거래.
- 배치·판매의 중복 처리 방지와 `DeploymentReceipt` 재조회.

## 8. 금지된 중간 상태

다음 상태는 허용하지 않는다.

- 전설 결과가 룰렛 확정 시 사용자 동의 없이 영웅으로 강등됨.
- 경고만 표시됐는데 PendingReward·식량·등급이 변경됨.
- 경고 없이 커밋 충돌이 생겼는데 자동 영웅 변환됨.
- 기존 전설이 이미 사망했는데 이전 경고를 이유로 영웅 2기로 강등됨.
- 영웅 변환 배치에서 한 기만 spawn됨.
- 금화가 지급됐지만 SpinSession이 열려 있음.
- PendingReward가 생성됐지만 transaction 완료 기록이 없음.
- 확정됐지만 보상 payload가 아직 미정임.
- 배치 spawn 실패 후 식량만 소비됨.
- 같은 transaction 재호출로 보상이나 배치가 중복 생성됨.

## 9. R1+R2 영향

```text
TRANSACTION_SEQUENCE_APPROVAL
≠ R1_R2_SCOPE_EXPANSION
≠ PRODUCT_CODE_AUTHORIZATION
```

현재 Issue #69의 R1+R2 구현 범위는 변경하지 않는다. 이 결정은 R3 이후 후속 패키지의 순서와 거래 의존성만 고정한다.

## 10. 현재 판정

```text
TRANSACTION_FOUNDATION_SEQUENCE: APPROVED
ORDER: R3_TO_U1F_TO_S1F_TO_R4_TO_U1C_TO_S1C
LEGENDARY_CONFIRM_RESULT: ALWAYS_LEGENDARY_PENDING_REWARD
LEGENDARY_CONFLICT_CONVERSION_OWNER: S1C_DEPLOYMENT_TRANSACTION
COMMIT_TIME_REVALIDATION: REQUIRED
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
FINAL_CODEX_HANDOFF: BLOCKED_UNTIL_EXACT_REVIEW_COMPLETE_COMMAND
```
