# 승인된 V2 전설 획득·배치 제한 계약

- 승인일: 2026-07-26
- 상태: `APPROVED_POST_LEDGER_AMENDMENT / V2_IMPLEMENTATION_NOT_STARTED`
- 제품 코드 승인: `NO`
- 승인 근거: 사용자 확정 — 전설 결과는 항상 전설로 보유하고, 플레이어 전장에는 생존 전설 최대 1기, 충돌 배치는 경고 후 영웅 2기로 변환, 배치 커밋 순간 재검증
- 상위 책임: 최신 사용자 지시, `docs/PROJECT_CORE.md`
- 관련 거래 순서: `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`

이 문서는 2026-07-25 통합 결정 원장 이후 승인된 후속 수정이다. 아래에 명시한 전설 관련 규칙은 기존 문서와 충돌할 때 이 문서가 우선한다. 제품 구현이나 사람 검증 완료를 의미하지 않는다.

## 1. 대체되는 기존 규칙

다음 규칙은 현재 V2 정본이 아니다.

- 5스테이지 위험 주기마다 병종 공용 전설 1회.
- 룰렛 `[확정]` 시 전설 한도를 소비하는 처리.
- 이미 한도를 사용한 주기의 전설 결과를 즉시 영웅 2기로 변환하는 처리.
- `legendary_cycle_id`, `legendary_cycle_used`, 주기별 `0/1` 표시.
- 스테이지 경계를 넘는 미확정 SpinSession에 전설 주기 문맥을 동결하는 요구.

이 문서는 다음 기존 위치를 명시적으로 대체한다.

- `docs/PROJECT_CORE.md`의 5스테이지 전설 주기 시스템 코어 문구.
- `docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md`의 전설 위험 주기·확정 시 변환 관련 문구.
- `docs/design/APPROVED_ROULETTE_CORE_RULES.md`의 `전설 위험 주기` 절과 관련 검증 항목.
- `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`의 R4 전설 주기 소비 단계.
- 로드맵·상태·역사 계획의 동일 취지 문구.

## 2. 전설 획득 계약

룰렛 최종 보드가 전설 등급을 만들면 항상 전설 보상을 생성한다.

```text
SpinSession [확정]
→ reward_grade = legendary
→ immutable UnitRewardPayload
→ PendingRewardStore.put_once()
```

- 전설 획득 횟수에 주기·스테이지·맵런 상한을 두지 않는다.
- 전설 결과는 룰렛 확정 시 영웅으로 강등하지 않는다.
- 전설 PendingReward는 결과 대기나 보관함에 여러 개 존재할 수 있다.
- 전설 PendingReward의 보관·판매는 전장 생존 전설 제한에 포함하지 않는다.
- 전설 판매·보관·사망은 별도 획득 한도를 복구하거나 소비하지 않는다. 획득 한도 자체가 없다.
- 스테이지 전환은 전설 보상의 등급을 변경하지 않는다.

## 3. 전장 생존 전설 제한

플레이어 진영 전장에는 동시에 생존 중인 전설 유닛을 최대 1기만 허용한다.

생존 전설 판정 조건:

```text
owner_team_id == PLAYER_TEAM_ID
AND reward_grade == legendary
AND deployment_state == deployed
AND is_alive == true
```

다음 대상은 생존 전설 수에 포함하지 않는다.

- PendingReward.
- 보관함 병력.
- 아직 실제 spawn되지 않은 예약 또는 preview.
- 사망한 전설.
- 판매된 전설.
- 적 진영 전설.
- 영웅 이하 등급.

기존 전설이 사망하면 보유 중인 다른 전설을 전설 그대로 배치할 수 있다.

## 4. 배치 의도와 경고

플레이어가 전설 PendingReward를 배치하려 할 때 현재 생존 전설을 조회한다.

### 생존 전설이 없는 경우

- 일반 전설 배치 경로를 사용한다.
- 경고를 표시하지 않는다.
- 실제 커밋 순간에도 생존 전설이 0명이어야 한다.

### 생존 전설이 있는 경우

배치 전에 다음 의미의 경고를 표시한다.

```text
현재 전장에 생존 중인 전설 유닛이 있습니다.
전장에는 생존 전설 유닛을 한 기만 배치할 수 있습니다.
이 유닛을 배치하면 동일한 세부 병종의 영웅 유닛 2기로 변환됩니다.

[취소] [영웅 2기로 배치]
```

경고 표시만으로 다음 상태를 변경하지 않는다.

- PendingReward 상태.
- 식량.
- 배치 라인.
- 유닛 등급과 수량.
- 전투 spawn.
- 로그와 transaction 완료 상태.

## 5. 배치 커밋 순간 재검증 — 승인된 A안

경고 표시 시점의 전장 상태를 고정하지 않는다. 실제 배치 transaction을 커밋하는 순간 생존 전설 수를 다시 검사한다.

### 경고를 확인했고 커밋 순간에도 생존 전설이 1기인 경우

- 원래 전설 PendingReward 1기를 영웅 2기 배치 결과로 변환한다.
- 두 영웅은 같은 라인에 하나의 원자 transaction으로 배치한다.

### 경고를 확인했지만 커밋 전에 기존 전설이 사망한 경우

- 원래 PendingReward를 전설 상태 그대로 1기 배치한다.
- 영웅 변환을 수행하지 않는다.
- UI는 `기존 전설이 사망하여 전설 상태로 배치되었습니다`와 동등한 결과 안내를 표시한다.

### 경고 없이 시작했지만 커밋 순간 생존 전설이 새로 존재하는 경우

- 자동으로 영웅 2기로 변환하지 않는다.
- transaction은 아무 상태도 변경하지 않고 중단한다.
- 최신 전장 상태를 기준으로 변환 경고를 새로 표시한다.
- 사용자의 명시적 변환 동의 없이 전설을 강등하지 않는다.

### 커밋 순간 생존 전설이 2기 이상인 경우

- 승인된 정상 상태가 아니다.
- 배치를 거부하고 invariant violation으로 기록한다.
- 임의로 추가 변환하거나 한 기를 제거하지 않는다.

## 6. 영웅 2기 변환 규칙

변환 결과는 원래 전설 보상의 동일 출처와 세부 병종을 유지한다.

예:

```text
Tier 3 철벽병 전설 1기
→ Tier 3 철벽병 영웅 2기
```

유지 데이터:

- `family_symbol_id`.
- `source_building_instance_id`.
- `source_completed_tier`.
- `selected_unit_variant_id`.
- Tier 기반 패시브 구성.
- 플레이어 진영과 선택 라인.

변경 데이터:

- `reward_grade`: `legendary` → `hero`.
- 수량: 1 → 2.
- 액티브 구성: 전설 등급 구성이 아니라 영웅 등급 규칙으로 각각 재조합.
- 각 영웅은 서로 다른 안정적 unit/reward instance ID를 가진다.

전설 객체를 단순 복제한 뒤 수치만 낮추는 방식은 허용하지 않는다. U1-C의 동일 병종·영웅 등급 조합 규칙으로 두 payload를 생성한다.

## 7. 원자적 배치 거래

전설 그대로 배치와 영웅 2기 변환 배치는 모두 idempotent transaction이어야 한다.

영웅 변환 배치의 성공 단위:

```text
전설 PendingReward 1기 소비
+ 영웅 payload 2개 생성
+ 영웅 2기분 식량 검증·예약
+ 같은 라인에 영웅 2기 spawn
+ pending 상태 전이
+ 배치 receipt·로그 기록
```

허용 결과:

```text
전체 성공
또는
아무 상태도 변경되지 않음
```

금지되는 부분 상태:

- 영웅 1기만 spawn.
- 전설 PendingReward만 소비.
- 식량만 소비.
- 영웅 payload는 생성됐지만 pending이 남음.
- spawn은 성공했지만 receipt가 없어 재요청 시 중복 배치.

영웅 2기분 식량이나 필수 배치 조건을 만족하지 못하면 전설 PendingReward를 그대로 유지하고 자원을 소비하지 않는다.

동일 `deployment_transaction_id` 재요청은 새로운 유닛을 만들지 않고 기존 `DeploymentReceipt`를 반환한다.

## 8. 패키지 책임 변경

### R4

- 전설 결과를 항상 전설 `UnitRewardPayload`와 PendingReward로 확정한다.
- 전설 주기·확정 시 영웅 변환을 소유하지 않는다.

### U1-F / U1-C

- U1-F는 전설 payload를 원래 등급 그대로 동결한다.
- U1-C는 배치 변환이 승인된 경우 같은 세부 병종의 영웅 등급 payload 2개를 결정론적으로 조합한다.

### S1-F / S1-C

- S1-F는 원래 전설 PendingReward와 transaction identity를 보존한다.
- S1-C는 경고 동의, 커밋 시 재검증, 전설 1기 또는 영웅 2기 원자 배치, rollback과 receipt를 소유한다.

### L1 / Battle

- 실제 spawn 결과와 `is_alive`가 생존 전설 판정의 근거다.
- UI 추정값이나 pending 상태를 생존 전설로 계산하지 않는다.

## 9. UI 계약

전설 PendingReward 카드에는 전설 등급을 그대로 표시한다.

- 보관·판매 화면에서 미리 영웅 2기로 표시하지 않는다.
- 배치 대상 라인 선택 시 현재 생존 전설 충돌 여부를 표시할 수 있다.
- 실제 변환은 경고 동의와 커밋 시 재검증 뒤에만 표시·수행한다.
- 경고를 본 뒤 기존 전설이 사망해 전설 배치로 바뀐 경우 결과 변경을 명시한다.
- 경고 없이 커밋 충돌이 새로 발생한 경우 자동 강등하지 않고 경고 단계로 되돌린다.

## 10. 검증 계약

자동 검증은 최소 다음 사례를 포함한다.

1. 전설 결과 여러 번 확정 → 모두 전설 PendingReward.
2. 생존 전설 0기 → 전설 그대로 1기 배치.
3. 생존 전설 1기 → 경고 전 상태 변화 없음.
4. 경고 취소 → pending·식량·전장 불변.
5. 경고 확인, 기존 전설 생존 → 같은 병종 영웅 2기 원자 배치.
6. 경고 확인 중 기존 전설 사망 → 전설 그대로 배치.
7. 경고 없이 시작 후 커밋 전 다른 전설 생존 → 무변경 중단·새 경고 요구.
8. 영웅 2기분 식량 부족 → 원래 전설 pending 유지.
9. 두 번째 영웅 spawn 실패 → 첫 spawn·식량·pending·로그 rollback.
10. 동일 deployment transaction 재요청 → 중복 0, 기존 receipt 반환.
11. 기존 전설 사망 후 다른 보관 전설 → 전설 그대로 배치.
12. 적 전설·보관 전설·사망 전설은 플레이어 생존 전설 수에서 제외.
13. 비정상 생존 전설 2기 이상 → 배치 거부·invariant violation.
14. stage 전환 전후에도 전설 PendingReward 등급 불변.

사람 검증은 경고 문구, 취소 가능성, 커밋 중 상태 변화 결과, 식량 부족 이유를 플레이어가 설명할 수 있는지 확인한다.

## 11. 현재 상태

```text
LEGENDARY_ACQUISITION_CAP: REMOVED
LEGENDARY_PENDING_REWARD: ALWAYS_LEGENDARY
PLAYER_ALIVE_LEGENDARY_BATTLEFIELD_CAP: 1
SECOND_LEGENDARY_DEPLOYMENT: WARN_THEN_TWO_HEROES_IF_CONFLICT_STILL_EXISTS
COMMIT_TIME_REVALIDATION: REQUIRED
AUTO_DOWNGRADE_WITHOUT_CONSENT: FORBIDDEN
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```
