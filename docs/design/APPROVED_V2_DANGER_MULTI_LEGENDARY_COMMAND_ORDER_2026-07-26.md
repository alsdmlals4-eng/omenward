# 승인된 위험 전투 복수 전설 배치 명령 순서

- 작성일: 2026-07-26
- 상태: `V2_SPEC_APPROVED / PRODUCT_CODE_NOT_AUTHORIZED`
- 승인 근거: 사용자 권장안 승인
- 상위 책임:
  - `docs/design/APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md`
  - `docs/design/APPROVED_V2_DANGER_TICK_LEGENDARY_DEPLOYMENT_ORDER_2026-07-26.md`
  - `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`

이 문서는 위험 전투의 한 deployment commit phase에 신규 전설 배치 명령이 둘 이상 포함될 때의 순서, 원자성, 동의와 receipt 계약을 소유한다.

## 1. 승인된 핵심 결정

```text
DANGER_MULTI_LEGENDARY_COMMAND_ORDER: COMMAND_SEQUENCE_SERIAL_COMMIT
COMMAND_ATOMICITY: PER_COMMAND
ALIVE_LEGENDARY_INDEX_REFRESH_AFTER_SUCCESS: REQUIRED
EARLIER_SUCCESS_ROLLBACK_ON_LATER_FAILURE: FORBIDDEN
FAILED_COMMAND_RESERVES_LEGENDARY_SLOT: NO
STALE_CONSENT_AUTO_DOWNGRADE: FORBIDDEN
DUPLICATE_COMMAND_SEQUENCE: INVARIANT_VIOLATION
NEW_SPAWN_COMBAT_ACTIVATION: NEXT_SIMULATION_TICK
```

같은 `command_cutoff_sequence` 이하의 명령은 `command_sequence` 오름차순으로 하나씩 처리한다.

각 명령은 다음 순서를 가진다.

```text
최신 AliveLegendaryIndexRevision 읽기
→ 해당 명령의 동의·자원·라인·pending 상태 검증
→ 단일 deployment transaction 원자 커밋 또는 무변경 실패
→ 성공 시 생존 전설 index revision 갱신
→ 다음 command_sequence 처리
```

한 commit phase 전체를 하나의 batch transaction으로 묶지 않는다.

## 2. 순서의 권위

전설 배치 우선순위는 authoritative command queue가 발급한 `command_sequence`만 소유한다.

다음 값은 우선순위 근거가 아니다.

- wall-clock 입력 timestamp.
- 렌더 callback 도착 순서.
- UI 카드 위치.
- 라인 번호.
- PendingReward 생성 시각.
- unit ID 또는 reward ID의 사전식 순서.
- spawn 함수 호출이 우연히 시작된 순서.

`command_sequence`는 한 MapRun 안에서 중복되지 않는 단조 증가 정수여야 한다.

같은 sequence가 둘 이상 발견되면 임의 tie-break를 적용하지 않고 해당 commit phase를 invariant violation으로 중단한다.

## 3. 대표 사례 — 둘 다 초기에는 전설 충돌 없음

초기 authoritative 상태:

```text
alive_legendary_count = 0
command_cutoff_sequence = 102
```

대기 명령:

```text
command 101: 전설 A 배치
command 102: 전설 B 배치
```

처리:

```text
command 101
→ alive = 0
→ 전설 A 원자 배치 성공
→ AliveLegendaryIndexRevision r40 → r41
→ alive = 1

command 102
→ r41 기준 재검증
→ 전설 충돌 발견
→ r41에 유효한 변환 동의가 없으면 CONSENT_REQUIRED
→ command 102는 무변경 종료
```

전설 A의 성공은 유지한다. B의 동의 부족 때문에 A를 롤백하지 않는다.

## 4. 후속 명령의 변환 동의

후속 명령을 영웅 2기로 변환하려면 동의가 현재 충돌 근거와 일치해야 한다.

동의 근거에는 최소 다음이 포함된다.

```text
command_sequence
pending_reward_id
deployment_transaction_id
target_lane_id
alive_legendary_index_revision
alive_legendary_unit_ids
conflict_basis_hash
```

앞선 명령 성공으로 revision 또는 생존 전설 집합이 바뀌면 이전 동의는 stale이다.

stale 동의가 있는 후속 명령은 자동으로 영웅 2기로 변환하지 않는다.

```text
상태 변경 없음
→ CONSENT_REQUIRED
→ 최신 충돌 근거로 경고 재표시
```

최신 revision에 유효한 동의가 있으면 부모 계약에 따라 같은 출처·Tier·세부 병종의 영웅 2기를 같은 라인에 원자 배치한다.

## 5. 앞선 명령 실패

앞선 명령이 다음 이유로 실패할 수 있다.

- PendingReward가 이미 소비됨.
- 식량 부족.
- 라인 또는 spawn 조건 불충족.
- transaction ID 충돌.
- spawn 준비 실패.
- 유효하지 않은 동의.

실패 명령은 아무 상태도 변경하지 않는다.

```text
pending 유지
식량 불변
spawn 0
receipt는 실패 사유 기록
AliveLegendaryIndexRevision 불변
```

따라서 다음 명령은 변경되지 않은 최신 revision에서 다시 평가한다.

예:

```text
alive = 0
command 101 실패
→ 전설 슬롯 점유 없음
command 102 재검증
→ 다른 조건이 유효하면 전설 그대로 배치 가능
```

실패한 명령이 숨은 예약 슬롯을 점유하거나 후속 명령을 강제로 영웅으로 바꾸는 것은 금지한다.

## 6. 성공 뒤 index 갱신

전설 1기 배치가 성공하면 다음 명령 전에 index를 즉시 갱신한다.

```text
DeploymentReceipt 기록
→ spawned unit authoritative 등록
→ is_alive = true
→ AliveLegendaryIndexRevision +1
→ 후속 명령 검증
```

영웅 2기 변환 배치는 전설 생존 수를 늘리지 않지만 전장·식량·receipt revision은 갱신한다.

새로 spawn된 유닛은 같은 commit phase의 후속 전설 판정에는 존재하지만 전투 행동은 다음 simulation tick부터 시작한다.

## 7. 명령별 원자성과 rollback

각 명령의 허용 결과는 다음 두 가지뿐이다.

```text
해당 명령 전체 성공
또는
해당 명령 상태 변경 0
```

금지되는 상태:

- 전설 PendingReward만 소비.
- 식량만 소비.
- 영웅 1기만 spawn.
- spawn 성공 후 receipt 누락.
- 후속 명령 실패 때문에 앞선 성공 rollback.
- 앞선 실패가 후속 명령까지 batch rollback.

후속 명령의 `CONSENT_REQUIRED`, 자원 부족 또는 spawn 실패는 앞선 명령의 이미 완료된 receipt를 취소하지 않는다.

## 8. idempotency

각 명령은 안정적인 다음 ID를 가진다.

```text
command_sequence
deployment_transaction_id
pending_reward_id
```

동일 `deployment_transaction_id` 재요청은 새 유닛을 만들지 않고 기존 `DeploymentReceipt`를 반환한다.

재요청된 앞선 명령의 기존 성공 receipt를 읽은 뒤에도 후속 명령은 현재 authoritative index를 사용한다.

중복 receipt 재조회가 index를 추가 증가시키거나 전설을 다시 spawn해서는 안 된다.

## 9. 위험 전투 tick 계약과의 관계

상위 tick 순서는 유지한다.

```text
전투 피해·사망 정산
→ AliveLegendaryIndexRevision 생성
→ cutoff 이하 배치 명령을 command_sequence 순차 처리
→ 각 성공 뒤 revision 갱신
→ receipt·인과 로그 완료
→ 다음 simulation tick
```

combat settlement 이후 commit phase 안에서 새 사망 판정을 끼워 넣지 않는다.

명령 처리 중 이미 존재한 전설이 공격받거나 사망하는 것처럼 보이는 애니메이션은 다음 combat simulation tick 전까지 authoritative 생존 상태를 바꾸지 않는다.

## 10. UI 계약

같은 commit phase에 둘 이상의 전설 명령이 대기 중이면 UI는 sequence를 표시하거나 최소한 처리 순서를 설명할 수 있어야 한다.

후속 명령이 `CONSENT_REQUIRED`로 멈추면 다음을 보여준다.

- 앞선 전설 배치 성공.
- 현재 생존 전설의 식별 가능한 정보.
- 해당 후속 명령이 영웅 2기로 바뀌는 이유.
- `[취소]`와 `[영웅 2기로 배치]`.

앞선 성공을 되돌리는 것처럼 보이는 표현은 금지한다.

## 11. 자동 검증 계약

최소 다음 사례를 검증한다.

1. 초기 생존 전설 0, 전설 명령 2개 → 첫 전설 성공, 둘째 `CONSENT_REQUIRED`.
2. 둘째가 최신 revision 동의 보유 → 첫 전설 1기 + 둘째 영웅 2기.
3. 첫 명령 식량 부족 실패 → 둘째가 전설로 성공 가능.
4. 첫 성공 뒤 둘째 stale 동의 → 자동 강등 없이 무변경.
5. 둘째 실패 → 첫 성공 유지.
6. 동일 첫 transaction 재요청 → 중복 spawn 0, 후속 판정 동일.
7. command sequence 중복 → invariant violation, 임의 순서 없음.
8. cutoff 이후 명령 → 다음 tick으로 이월.
9. 새 전설은 후속 명령 판정에는 포함되지만 같은 tick 전투 행동 0.
10. 서로 다른 렌더 프레임률에서도 동일 command log가 동일 receipt sequence 생성.

## 12. 현재 상태

```text
DANGER_MULTI_LEGENDARY_COMMAND_ORDER: APPROVED
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```
