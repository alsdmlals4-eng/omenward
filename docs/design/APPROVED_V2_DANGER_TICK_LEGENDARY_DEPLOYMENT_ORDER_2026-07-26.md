# 승인된 V2 위험 전투 tick 전설 배치 순서 계약

- 승인일: 2026-07-26
- 상태: `APPROVED_POST_LEDGER_AMENDMENT / V2_IMPLEMENTATION_NOT_STARTED`
- 제품 코드 승인: `NO`
- 승인 근거: 사용자 확정 — 위험 전투 동일 tick에서 전투 피해·사망을 먼저 확정하고, 생존 전설 index를 갱신한 뒤 플레이어 배치 transaction을 커밋
- 상위 책임: 최신 사용자 지시, `docs/PROJECT_CORE.md`
- 부모 계약: `APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md`
- 시간 계약: `APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`
- 일반 전술계획 예약 계약: `APPROVED_V2_TACTICAL_LEGENDARY_RESERVATION_ORDER_2026-07-26.md`

이 문서는 위험 전투의 실시간 조작 중 전설 사망과 새 전설 배치가 같은 렌더 프레임 또는 simulation tick 경계에 겹칠 때의 결정론적 순서를 소유한다. 제품 구현이나 사람 검증 완료를 의미하지 않는다.

## 1. 적용 범위

적용:

- `DANGER_COMBAT`에서 전설 PendingReward 배치 명령과 기존 전설의 피해·사망이 겹치는 경우.
- 시스템 정지 없이 전투가 계속되는 동안의 배치 command queue.
- 전설 그대로 배치 또는 영웅 2기 변환 여부를 결정하는 생존 전설 재검증.

비적용:

- 일반 `TACTICAL_PLANNING` 예약 batch. 해당 순서는 별도 승인 문서를 따른다.
- 룰렛 `[확정]`과 PendingReward 생성.
- 위험 전투의 건설·스킬 즉시 실행 규칙.
- 한 commit phase에 새 전설 배치 명령이 둘 이상 존재할 때의 상호 우선순위. 이 항목은 별도 검수 결정으로 남긴다.

## 2. 승인된 tick 순서 — A안

위험 전투의 fixed simulation tick은 다음 논리 순서를 따른다.

```text
1. 이전 tick에서 예약된 이동·공격·피해·상태 효과를 계산
2. 치명 피해·사망·제거·식량 반환을 authoritative 상태로 정산
3. 플레이어 생존 전설 index를 새 revision으로 재구축
4. 해당 command cutoff까지 수집된 플레이어 배치 명령을 검증
5. 전설 1기 또는 영웅 2기 배치 transaction을 원자 커밋
6. receipt·인과 로그 기록
7. 새로 spawn된 유닛은 다음 simulation tick부터 전투 행동 가능
```

정본 마커:

```text
DANGER_TICK_LEGENDARY_ORDER: COMBAT_SETTLEMENT_BEFORE_DEPLOYMENT_COMMIT
ALIVE_LEGENDARY_INDEX: POST_SETTLEMENT_REVISION
DANGER_DEPLOYMENT_INPUT: QUEUED_NOT_DIRECT_SPAWN
WALL_CLOCK_ORDERING: FORBIDDEN
RENDER_CALLBACK_ORDERING: FORBIDDEN
NEW_SPAWN_COMBAT_ACTIVATION: NEXT_SIMULATION_TICK
```

## 3. 사망 확정의 의미

전설 유닛은 다음 조건이 모두 정산된 뒤에만 생존 index에서 제거된다.

```text
lethal_result_committed == true
AND is_alive == false
AND deployment_state != pending_spawn
AND death_settlement_tick_id <= current_settled_tick_id
```

다음은 판정 근거가 아니다.

- 사망 애니메이션 시작·종료 시점.
- 렌더 노드가 화면에서 사라진 시점.
- 입력 콜백이 호출된 실제 OS 시각.
- 프레임 내 signal 연결 순서.
- UI가 마지막으로 표시한 HP.

피해 계산은 끝났지만 사망 정산이 아직 커밋되지 않았다면 해당 전설은 현재 commit phase에서 생존으로 본다. 반대로 사망 애니메이션이 남아 있어도 authoritative `is_alive == false`가 정산됐다면 생존 전설로 세지 않는다.

## 4. 배치 입력 경계

위험 전투의 UI 입력은 직접 PendingReward·식량·전장을 변경하지 않는다.

```text
UI input
→ DeploymentCommand enqueue
→ stable command_sequence 부여
→ fixed tick combat settlement
→ command_cutoff_sequence 캡처
→ cutoff 이하 command 검증·커밋
```

- `command_sequence`는 런 내부에서 안정적으로 증가한다.
- wall-clock timestamp는 판정이나 우선순위에 사용하지 않는다.
- cutoff 캡처 뒤 도착한 명령은 다음 simulation tick의 commit phase로 넘어간다.
- replay는 `simulation_tick_id`, `command_sequence`, `command_cutoff_sequence`를 기록한다.
- 입력 콜백은 spawn, 식량 차감, PendingReward 소비를 직접 호출하지 않는다.

## 5. 전설 충돌 재검증

배치 command를 커밋할 때는 3단계에서 생성한 동일 revision의 생존 전설 index만 읽는다.

### 생존 전설 0기

- 새 PendingReward를 전설 1기로 배치한다.
- 과거에 변환 경고를 확인했더라도 현재 충돌이 사라졌다면 영웅 변환을 수행하지 않는다.
- 결과 안내는 기존 전설 사망으로 전설 상태 배치가 선택됐음을 표시한다.

### 생존 전설 1기 + 유효한 변환 동의

- 부모 계약에 따라 동일 세부 병종 영웅 2기로 원자 변환·배치한다.
- 동의가 참조한 PendingReward·라인·변환 payload와 현재 command가 일치해야 한다.

### 생존 전설 1기 + 변환 동의 없음

- 자동 강등하지 않는다.
- 아무 상태도 변경하지 않고 command를 `CONSENT_REQUIRED`로 종료한다.
- 최신 생존 전설 revision을 근거로 경고를 표시한다.
- 위험 전투는 계속 진행된다.

### 생존 전설 2기 이상

- invariant violation이다.
- 배치를 거부하고 상태를 임의 수정하지 않는다.

## 6. 동일 tick 예시

### 예시 A — 기존 전설의 사망이 해당 tick에 정산됨

```text
tick 410 전투 계산
→ 전설 A 치명 피해
→ A 사망·식량 반환 정산
→ alive legendary index = 0, revision 410
→ 전설 B 배치 command 검증
→ B를 전설 1기로 원자 배치
→ B는 tick 411부터 행동
```

### 예시 B — 치명 피해가 다음 tick에 정산될 예정

```text
tick 410 commit phase 시점
→ 전설 A is_alive == true
→ alive legendary index = 1, revision 410
→ 유효한 변환 동의가 있는 전설 B command
→ 영웅 2기로 원자 배치
→ 이후 tick 411에서 A 사망 정산 가능
```

### 예시 C — 렌더 프레임 순서가 반대

UI 클릭 signal이 사망 애니메이션 signal보다 먼저 호출됐더라도 결과는 바뀌지 않는다. 두 signal의 호출 순서는 authoritative simulation settlement와 command cutoff를 대체하지 않는다.

## 7. 원자성·idempotency

배치 command의 허용 결과:

```text
전체 성공 + DeploymentReceipt
또는
아무 상태도 변경되지 않은 명시적 실패 receipt
```

금지 상태:

- 사망 index는 갱신됐지만 식량 반환이 누락됨.
- PendingReward만 소비되고 spawn 실패.
- 영웅 1기만 spawn.
- 전설 spawn은 성공했지만 receipt 누락.
- 같은 `deployment_transaction_id` 재요청으로 중복 spawn.
- 배치 결과가 렌더 FPS에 따라 달라짐.

동일 `deployment_transaction_id` 재요청은 기존 `DeploymentReceipt`를 반환한다.

## 8. 상태·소유권 경계

### Battle / L1

- tick 피해·상태 효과·사망·제거를 정산한다.
- `CombatSettlementReceipt`와 `settled_tick_id`를 제공한다.
- 사망 애니메이션은 도메인 판정을 소유하지 않는다.

### MapRun / StageFlow

- fixed simulation tick과 command cutoff를 소유한다.
- `AliveLegendaryIndexRevision`을 전투 정산 뒤 한 번 생성한다.
- 위험 전투 배치 command queue를 commit phase로 전달한다.

### S1-C Deployment transaction

- 동일 alive index revision으로 경고 동의와 충돌을 재검증한다.
- PendingReward·식량·spawn·receipt를 원자 커밋한다.
- 전투 정산 도중 직접 실행되지 않는다.

### UI / X1

- command 접수 상태와 실제 commit 결과를 구분한다.
- `전설 배치됨`, `영웅 2기로 변환됨`, `동의 필요`, `기존 전설 사망으로 전설 배치됨`을 receipt에 따라 표시한다.
- 클릭 시점의 추정 상태를 확정 결과로 먼저 표시하지 않는다.

## 9. 검증 계약

자동 검증은 최소 다음을 포함한다.

1. 같은 seed·입력 로그·tick sequence는 동일 결과.
2. 같은 tick에 기존 전설 사망 정산 + 새 전설 배치 → 전설 1기.
3. 기존 전설 사망 미정산 + 유효한 동의 → 영웅 2기.
4. 기존 전설 사망 미정산 + 동의 없음 → 무변경 `CONSENT_REQUIRED`.
5. 사망 애니메이션 잔존 + authoritative 사망 → 전설 1기.
6. HP 0 표시지만 사망 정산 전 → 생존 전설 1기로 판정.
7. cutoff 이후 입력 → 다음 tick까지 상태 불변.
8. 렌더 FPS 30/60/144에서 동일 replay 결과.
9. 동일 deployment transaction 재요청 → 중복 0.
10. spawn 실패 → PendingReward·식량·alive index·로그 rollback.
11. 새 spawn 유닛은 같은 tick에 공격·피해 계산에 참여하지 않음.
12. 생존 전설 2기 이상 비정상 상태 → 배치 거부.

사람 검증은 전설 사망과 배치 클릭이 거의 동시에 일어났을 때 결과 안내를 플레이어가 이해할 수 있는지 확인한다.

## 10. 현재 상태

```text
DANGER_TICK_LEGENDARY_ORDER: COMBAT_SETTLEMENT_BEFORE_DEPLOYMENT_COMMIT
ALIVE_LEGENDARY_INDEX: POST_SETTLEMENT_REVISION
DANGER_DEPLOYMENT_INPUT: QUEUED_NOT_DIRECT_SPAWN
WALL_CLOCK_ORDERING: FORBIDDEN
RENDER_CALLBACK_ORDERING: FORBIDDEN
NEW_SPAWN_COMBAT_ACTIVATION: NEXT_SIMULATION_TICK
MULTIPLE_NEW_LEGENDARY_COMMANDS_SAME_COMMIT_PHASE: REVIEW_PENDING
PRODUCT_CODE_AUTHORIZED: NO
V2_IMPLEMENTATION: NOT_STARTED
HUMAN_QA: NOT_RUN
CORE_LOCK_V2: PENDING
```
