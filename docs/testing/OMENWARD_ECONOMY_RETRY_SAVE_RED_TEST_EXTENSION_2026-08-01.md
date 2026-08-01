# 오멘워드 경제·Retry·저장 Red 테스트 확장

- 결정 ID: `OMW-DEC-20260801-ECONOMY-RETRY-SAVE-PLANNING-V1`
- 상위 Red Gate: `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1`
- 상태: `CURRENT_RED_EXTENSION / TEST_FILES_NOT_CREATED / NOT_RUN`
- 제품 코드 권한: `NONE`

이 문서는 최신 Vertical Slice Red 명세의 경제·Retry 영역을 확장한다. 정확한 미확정 수치를 assertion에 넣지 않고, Parameter Registry의 승인 상태·수식·거래·save 불변 조건을 검증한다.

## 1. Parameter Registry Gate

| ID | 계약 |
|---|---|
| `RED-PARAM-001` | Registry JSON이 parse되고 schema_version·Decision ID·authority 경로가 유효하다 |
| `RED-PARAM-002` | 모든 parameter ID가 유일하다 |
| `RED-PARAM-003` | `null` 승인값은 제품 default로 사용되지 않는다 |
| `RED-PARAM-004` | legacy H0 값은 `HISTORICAL_ONLY/LEGACY_PROVEN_ONLY`로만 소비된다 |
| `RED-PARAM-005` | `STARTING_FOOD_CAP`은 compatibility alias이며 신규 data는 `RUN_START_FOOD_CAP`을 사용한다 |
| `RED-PARAM-006` | Retry Tier는 값 미정이어도 `0<T1<T2<T3` constraint를 가진다 |
| `RED-PARAM-007` | exact value 파일은 simulation evidence·Decision ID·config hash 없이는 CURRENT가 될 수 없다 |

## 2. 경제 거래

| ID | 계약 |
|---|---|
| `RED-ECO-001` | 같은 quote·transaction 재실행은 이중 차감·지급이 없다 |
| `RED-ECO-002` | stale quote는 골드·건물·릴 상태 0 mutation으로 실패한다 |
| `RED-ECO-003` | 일시정지 중 수입·건설·수리·생산 시간이 진행되지 않는다 |
| `RED-ECO-004` | 패배 확정 후 시간 수입을 지급하지 않는다 |
| `RED-ECO-005` | 무료 회전 금화 보상은 현재 Act 유료 회전 reference cost를 사용한다 |
| `RED-ECO-006` | 금고 수입은 룰렛 금화 보상을 이중 증폭하지 않는다 |
| `RED-ECO-007` | 접전지 수입은 소유 접전지 수와 결정론적 tick을 사용한다 |
| `RED-ECO-008` | 판매 preview와 commit 결과가 같은 정수값이다 |
| `RED-ECO-009` | 판매된 PendingReward는 보관·배치할 수 없다 |
| `RED-ECO-010` | 판매 거래 중복 호출은 이중 수입을 만들지 않는다 |

## 3. 이동·보관·식량

| ID | 계약 |
|---|---|
| `RED-ECO-011` | n번째 live 이동 비용은 `n×P`이며 preview 비용은 0이다 |
| `RED-ECO-012` | 세로·가로 이동은 같은 session use counter를 공유한다 |
| `RED-ECO-013` | 실행 뒤 undo/reset API가 없다 |
| `RED-ECO-014` | 보관 병력 식량 비용은 0이다 |
| `RED-ECO-015` | 배치 성공만 식량을 예약한다 |
| `RED-ECO-016` | 농장 손실로 cap이 감소해도 기존 배치 병력을 제거·약화하지 않는다 |
| `RED-ECO-017` | 식량 부족은 신규 배치만 0 mutation으로 차단한다 |
| `RED-ECO-018` | 같은 reward의 중복 배치는 불가능하다 |
| `RED-ECO-019` | 영구 소멸한 병력만 예약 식량을 반환한다 |

## 4. 건물 비용·환불·수리

| ID | 계약 |
|---|---|
| `RED-ECO-020` | 건설·업그레이드는 actual paid snapshot을 저장한다 |
| `RED-ECO-021` | 취소 환불은 `floor(actual_paid×rate)`이고 actual paid를 초과하지 않는다 |
| `RED-ECO-022` | 적 파괴·점령 BLOCKED는 플레이어 취소 환불을 지급하지 않는다 |
| `RED-ECO-023` | 완료 건물 철거와 진행 중 건설/업그레이드 취소를 다른 거래로 처리한다 |
| `RED-ECO-024` | 수리비는 실제 회복 HP만큼만 정산한다 |
| `RED-ECO-025` | 골드 부족 시 추가 HP 회복 전에 수리가 정지한다 |
| `RED-ECO-026` | 환불 transaction replay가 이중 골드를 만들지 않는다 |

정확한 cost·time·HP·rate는 별도 exact-value Decision 전 assertion하지 않는다.

## 5. Profile·정산

| ID | 계약 |
|---|---|
| `RED-META-001` | MapRun 골드·식량·무료 회전은 런 종료 시 프로필 잔액으로 이전되지 않는다 |
| `RED-META-002` | 정산 완료 영구재화만 spendable balance가 된다 |
| `RED-META-003` | 현재 런 예상·미정산 영구재화는 Retry 비용에 사용할 수 없다 |
| `RED-META-004` | 프로필 보관 확장은 시작 용량 tier와 hard cap만 변경한다 |
| `RED-META-005` | 런 골드로 무제한 보관함 확장을 구매할 수 없다 |
| `RED-META-006` | 프로필 경제 실패가 SettingsSave를 변경하지 않는다 |

## 6. 제품 유료 Retry

| ID | 계약 |
|---|---|
| `RED-RETRY-EXT-001` | Stage 1~4에서 제품 Retry offer가 없다 |
| `RED-RETRY-EXT-002` | Stage 5~10/11~15/16~20가 T1/T2/T3에 매핑된다 |
| `RED-RETRY-EXT-003` | 하나의 MapRun에서 최대 1회다 |
| `RED-RETRY-EXT-004` | 비용은 정산 프로필 영구재화만 사용한다 |
| `RED-RETRY-EXT-005` | checkpoint·schema·checksum·lineage 검증 전 비용을 commit하지 않는다 |
| `RED-RETRY-EXT-006` | 복원 실패 시 잔액·retry_used·run state가 원래 패배 상태로 남는다 |
| `RED-RETRY-EXT-007` | 같은 idempotency key는 같은 receipt를 반환한다 |
| `RED-RETRY-EXT-008` | retry transaction replay가 이중 차감·무료 복원을 만들지 않는다 |
| `RED-RETRY-EXT-009` | 복원 뒤 seed·공세·미션·룰렛 RNG lineage가 같다 |
| `RED-RETRY-EXT-010` | 플레이어 입력 변경만 이후 결과를 바꿀 수 있다 |

## 7. Save Schema·Checkpoint

| ID | 계약 |
|---|---|
| `RED-SAVE-001` | ProfileSave·RunCheckpoint·SettingsSave·Journal·Backup이 논리적으로 분리된다 |
| `RED-SAVE-002` | schema_version·manifest_version·run/checkpoint/commit ID·checksum이 필수다 |
| `RED-SAVE-003` | Stage 준비 안정 경계에서 checkpoint를 생성한다 |
| `RED-SAVE-004` | 활성 전투 임의 프레임을 제품 checkpoint로 승격하지 않는다 |
| `RED-SAVE-005` | 미확정 preview·부분 reward transaction을 checkpoint에 기록하지 않는다 |
| `RED-SAVE-006` | temp write 후 read-back 검증 전 current를 교체하지 않는다 |
| `RED-SAVE-007` | 원자 교체 전 last-known-good backup을 보존한다 |
| `RED-SAVE-008` | checksum 실패 current는 정상 load되지 않는다 |
| `RED-SAVE-009` | current 실패 시 유효 backup을 복원 후보로 사용한다 |
| `RED-SAVE-010` | future schema를 추정 load하지 않는다 |
| `RED-SAVE-011` | migration 실패 시 원본·backup이 변경되지 않는다 |
| `RED-SAVE-012` | 동일 checkpoint와 입력 로그는 동일 final hash를 만든다 |

## 8. Journal fault injection

모든 transaction type에 다음 중단 지점을 적용한다.

```text
BEFORE_PREPARED
AFTER_PREPARED
AFTER_DOMAIN_APPLY
BEFORE_ATOMIC_REPLACE
AFTER_ATOMIC_REPLACE_BEFORE_RECEIPT
AFTER_COMMITTED
```

필수 결과:

- COMMITTED는 정확히 한 번 반영.
- PREPARED/APPLIED 잔여 상태는 거래별 정책으로 rollback 또는 finish.
- 잔액·reward·building·checkpoint가 서로 다른 commit을 가리키지 않음.
- current와 backup 동시 손상 0.

## 9. Expected Red 조건

현재 Legacy에서 예상되는 정상 Red:

```text
Parameter Registry consumer 없음
ProfileSave·RunCheckpoint·Journal 없음
제품 paid retry transaction 없음
atomic checkpoint restore 없음
latest physical reel economy 없음
```

허용되지 않는 실패:

- JSON/문법 오류.
- 파일 경로 오타.
- Godot import 실패.
- timeout/hang.
- 테스트 자체의 임의 exact value assertion.

## 10. 현재 상태

```text
RED_EXTENSION: WRITTEN
TEST_FILES: NOT_CREATED
EXPECTED_RED: NOT_RUN
FAULT_INJECTION_HARNESS: NOT_CREATED
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
```
