# 오멘워드 경제·유료 재시도·저장·Checkpoint 기획 계약

- 결정 ID: `OMW-DEC-20260801-ECONOMY-RETRY-SAVE-PLANNING-V1`
- 승인 근거: 2026-08-01 사용자 권장안 일괄 승인
- 상태: `RECOMMENDED_DEFAULT_APPROVED / STRUCTURE_CURRENT / EXACT_VALUES_PENDING / PLANNING_ONLY`
- 제품 코드·Codex: `NOT_AUTHORIZED / BLOCKED`
- 자동 시뮬레이션: `CONTRACT_WRITTEN / NOT_RUN`
- Runtime·사람 검증: `NOT_RUN / NOT_RUN`
- 기계 Registry: `docs/design/OMENWARD_ECONOMY_RETRY_SAVE_PARAMETER_REGISTRY_V1.json`
- 시뮬레이션 계약: `docs/testing/OMENWARD_ECONOMY_META_RETRY_100K_SIMULATION_CONTRACT_2026-08-01.md`

이 문서는 현재 승인된 코어 루프를 경제·메타·저장 거래로 연결한다. 정확한 비용과 획득량을 발명하는 문서가 아니라, **어떤 값이 존재하고 누가 소유하며 어떤 불변 조건과 시뮬레이션을 통과한 뒤 제품 수치가 되는지**를 정한다.

---

## 1. 목표

경제는 다음 선택이 모두 유효하도록 설계한다.

```text
즉시 전선 안정
vs 건물·TokenSource 투자
vs 세 물리 릴 회전
vs 이동권 사용
vs 병력 보관
vs 병력 판매
vs 한 라인 비가역 배치
vs 후반 유료 Retry를 위한 프로필 재화 보존
```

경제의 목적은 플레이 시간을 늘리거나 모든 자원을 소진시키는 것이 아니다. 플레이어가 공개된 공세에 대해 **구조 투자·확률 감수·전선 커밋**의 기회비용을 이해하도록 만드는 것이다.

---

## 2. 권위와 역사 수치 분류

### 2.1 현재 구조 권위

- `docs/PROJECT_CORE.md`
- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- `docs/design/APPROVED_ROULETTE_CORE_RULES.md`
- `docs/design/APPROVED_VERTICAL_SLICE_DEFEAT_AND_PAID_RETRY_PRINCIPLE_2026-07-31.md`
- 이 문서와 연결 Parameter Registry

### 2.2 과거 수치

다음은 삭제하지 않지만 현재 35분·20 Stage·5건물·세 물리 릴 제품의 정확 수치 권위가 아니다.

```text
APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1
PR #92·#97 exact values
기존 15분 Stage 경제
시장 건물 수치
Legacy spin_cost = 20
기존 시작 골드·기본 수입·접전지 수입
70%/50%/40% 환급률
```

분류:

```text
LEGACY_CANDIDATE_H0
HISTORICAL_APPROVED_SOURCE
LATEST_STRUCTURE_OVERRIDES_APPLY
NOT_PRODUCT_EXACT_VALUES
```

보존 가능한 행동 계약:

- 지불 시 실제 지불액 snapshot을 남긴다.
- 환불은 현재 가격이 아니라 실제 지불액을 기준으로 한다.
- 정수 금화는 floor 규칙을 사용한다.
- 같은 거래의 중복 지급·중복 차감을 금지한다.
- 진행률 비례 환불은 별도 명시 승인 없이는 사용하지 않는다.
- 적 공격으로 파괴된 자산에는 플레이어 취소 환불을 지급하지 않는다.

환급 **비율 숫자**는 최신 시뮬레이션 전 확정하지 않는다.

---

## 3. 경제 상태 영역

### 3.1 MapRun 경제

```yaml
MapRunEconomyState:
  gold
  food_cap
  food_reserved
  free_spins
  storage_capacity
  stored_reward_count
  stage_index
  act_index
  difficulty_id
  active_income_sources
  pending_ledger_entries
```

- 골드·식량·무료 회전은 현재 MapRun 안에서만 사용한다.
- MapRun 종료 시 소멸한다.
- 일시정지 중 시간 기반 수입·건설·생산·수리가 진행되지 않는다.
- 패배 확정 뒤 새 시간 수입을 지급하지 않는다.

### 3.2 프로필 경제

```yaml
ProfileEconomyState:
  permanent_currency_balance
  settled_permanent_currency_total
  unlocks
  storage_starting_capacity_tier
  cosmetics
  discoveries
  achievements
  transaction_journal_head
```

- 영구재화는 **정산 완료된 프로필 잔액**만 제품 Retry에 사용할 수 있다.
- 현재 런에서 아직 정산되지 않은 예상 영구재화는 잔액이 아니다.
- 현재 런 골드·식량·무료 회전으로 Retry 비용을 대체하지 않는다.
- 메타 진행의 기본 방향은 기록·선택 폭·장식이다.
- 강한 영구 전투 능력치 상승은 별도 승인 전 금지한다.

### 3.3 설정·접근성

조작·그래픽·오디오·접근성 설정은 프로필 경제와 분리된 설정 저장 영역이 소유한다. 경제 거래 실패가 설정 파일을 손상시키지 않아야 한다.

---

## 4. 경제 Parameter 영역

모든 실제 값은 Parameter Registry ID로 참조한다.

### 4.1 런 시작·기본 수입

- `RUN_START_GOLD`
- `RUN_START_FOOD_CAP`
- `BASE_INCOME_AMOUNT`
- `BASE_INCOME_INTERVAL_SECONDS`
- `CLASH_CONTROL_INCOME_AMOUNT`
- `CLASH_CONTROL_INCOME_INTERVAL_SECONDS`
- `FREE_SPIN_START_COUNT`

불변 조건:

1. 적 개별 처치 금화와 무제한 파밍 수입을 기본값으로 사용하지 않는다.
2. 공세 지연이 경제적으로 유리한 무한 파밍이 되지 않는다.
3. 접전지 수입은 전선 우위를 보상하되, 한 번의 선취가 나머지 런을 자동 승리로 만드는 폭발적 복리를 만들지 않는다.
4. 기본 수입과 접전지 수입은 결정론적 simulation tick을 사용한다.

### 4.2 유료 회전

- `PAID_SPIN_BASE_COST`
- `PAID_SPIN_ACT_MULTIPLIER_A1..A4`
- `FREE_SPIN_GOLD_REFERENCE_COST_POLICY`

권장 구조:

```text
paid_spin_cost(stage)
= integer_rounding(PAID_SPIN_BASE_COST × current_act_multiplier)
```

- 기본 승격은 Act 단위 비감소 multiplier를 사용한다.
- Stage마다 가격을 요동시키지 않는다.
- 실제 multiplier 값은 시뮬레이션 전 미정이다.
- 금화 결과 75% / 200% / 500%는 **현재 회전의 canonical reference cost**에 floor를 적용한다.
- 무료 회전도 같은 Stage·Act의 유료 회전 reference cost를 사용하며 0원 기준으로 계산하지 않는다.
- 금고 Tier가 지속 수입과 금화 당첨 보상을 동시에 증폭하지 않는다.

### 4.3 이동권

- `REEL_MOVE_BASE_COST_P`
- `REEL_MOVE_SESSION_USE_COUNT`
- `REEL_MOVE_SESSION_COST_CAP` 선택적 안전장치

승인 구조:

```text
n번째 실행 이동 비용 = n × P
```

- preview는 비용을 소비하지 않는다.
- live 이동 실행 시 즉시 비용을 소비한다.
- 세로·가로 이동은 같은 세션 비용 카운터를 공유한다.
- 실행된 이동은 undo/reset할 수 없다.
- 정확한 `P`와 cap 사용 여부는 시뮬레이션 결과로 결정한다.

### 4.4 PendingReward 판매

- `UNIT_SELL_VALUE_BY_TIER_AND_GRADE`
- `UNIT_SELL_SOURCE_MODIFIER_POLICY`

규칙:

1. 판매가는 TokenSource 투자·회전·이동 비용을 안정적으로 무한 복제하는 차익거래를 만들지 않는다.
2. 등급·Tier가 오르면 판매가는 비감소한다.
3. source 종류만으로 임의 보너스를 주지 않는 것을 기본값으로 한다.
4. 판매 preview와 실제 정산은 같은 canonical 정수 결과를 사용한다.
5. 판매 확정은 멱등 거래다.

### 4.5 보관함

권장 기본 구조:

```text
런 상태: 현재 보관 칸과 stored rewards
프로필 상태: 시작 보관 용량을 올리는 제한된 unlock tier
런 골드로 무제한 보관함 확장: 기본 금지
```

이유:

- 보관은 식량을 사용하지 않는 안전 옵션이므로 무제한 확장은 배치·판매의 기회비용을 제거한다.
- 프로필 확장은 선택 폭을 늘리되 hard cap을 가진다.
- 실제 기본 용량·tier 수·비용·상한은 미정이다.

### 4.6 식량

- `STARTING_FOOD_CAP`
- `FARM_FOOD_CAP_BY_TIER`
- `UNIT_FOOD_COST_BY_ARCHETYPE_TIER`

규칙:

- 보관 병력은 식량을 사용하지 않는다.
- 배치 성공 시 식량을 예약한다.
- 농장 파괴·소유권 상실로 cap이 감소해도 기존 배치 병력을 제거·약화하지 않는다.
- 신규 배치·생산만 차단한다.
- 사망·영구 소멸 시 예약 식량을 반환한다.
- 같은 PendingReward를 두 번 배치해 식량을 중복 예약할 수 없다.

### 4.7 건물·업그레이드·수리·철거

건물별 Parameter:

```text
BUILD_COST
CONSTRUCTION_TIME
BASE_HP
TIER_UPGRADE_COST
TIER_UPGRADE_TIME
TIER_HP_DELTA
REPAIR_HP_PER_SECOND
REPAIR_GOLD_PER_HP
DEMOLITION_TIME
DEMOLITION_REFUND_RATE
CANCEL_CONSTRUCTION_REFUND_RATE
CANCEL_UPGRADE_REFUND_RATE
```

규칙:

- 건설·업그레이드는 명시적 quote와 payment snapshot을 생성한다.
- quote가 stale이면 0 mutation으로 거부하고 다시 preview한다.
- 건설 중 건물 효과와 타워 공격은 비활성이다.
- 수리는 실제 회복된 HP 단위로 실시간 정산한다.
- 수리 중 골드가 부족하면 추가 회복 전 정지한다.
- 완료 건물 철거와 진행 중 작업 취소는 다른 거래다.
- 적 파괴·점령 BLOCKED 처리와 플레이어 철거·취소는 다른 거래다.
- 환불은 `floor(actual_paid_gold × rate)`이며 actual paid를 초과할 수 없다.
- 정확한 rate는 미정이다.

---

## 5. 제품 유료 Retry

상위 원칙은 기존 `OMW-DEC-20260731-DEFEAT-RETRY-V1`을 유지한다.

```yaml
paid_retry:
  available_from_stage: 5
  maximum_per_maprun: 1
  currency_domain: settled_profile_permanent_currency
  restore_point: failed_stage_preparation_checkpoint
  same_rng_lineage: true
  exact_costs: pending_simulation
```

### 5.1 비용 Tier

```text
Stage 1~4  = 제품 유료 Retry 불가
Stage 5~10 = RETRY_COST_TIER_1
Stage 11~15 = RETRY_COST_TIER_2
Stage 16~20 = RETRY_COST_TIER_3
```

불변 조건:

```text
0 < TIER_1 < TIER_2 < TIER_3
```

정확한 값·배율·영구재화 명칭은 시뮬레이션과 사람 플레이 전 확정하지 않는다.

### 5.2 Retry 기회비용

Retry 비용은 다음과 경쟁해야 한다.

- 프로필 선택지 해금.
- 제한된 보관 시작 용량 확장.
- 장식·문양.
- 향후 승인될 기타 비전투 메타 소비.

Retry가 항상 최적이거나 사실상 사용 불가능하지 않도록 한다. 강한 영구 능력치 구매와 같은 지갑에서 경쟁시키는 안은 별도 승인 전 사용하지 않는다.

### 5.3 Retry 원자 거래

```text
1. 패배 상태와 retry 자격 확인
2. checkpoint 존재·schema·checksum·lineage 검증
3. 프로필 정산 잔액 확인
4. retry transaction PREPARED journal 기록
5. checkpoint를 임시 복원 영역에 역직렬화
6. 전체 불변 조건 검증
7. 프로필 비용 차감과 retry_used=true를 하나의 commit으로 준비
8. 복원 상태 원자 승격
9. profile·run·journal commit
10. 성공 receipt 반환
```

실패 시:

- 영구재화 차감 0 또는 journal 기반 완전 복구.
- 무료 복원 0.
- 기존 패배 상태와 last-known-good save 보존.
- 같은 idempotency key는 같은 receipt를 반환.

멱등성 키:

```text
profile_id + run_id + checkpoint_id + retry_index
```

---

## 6. Save 영역 분리

최소 논리 파일·레코드 영역:

```text
ProfileSave
RunCheckpoint
SettingsSave
TransactionJournal
LastKnownGoodBackup
```

### 6.1 ProfileSave

소유:

- 정산 영구재화.
- 해금·도감·기록·업적·장식.
- 프로필 보관 시작 용량 tier.
- 누적 통계.
- 현재 활성 run ID와 checkpoint pointer.
- 마지막 commit ID.

MapRun 골드·식량·건물·릴 배열을 직접 소유하지 않는다.

### 6.2 RunCheckpoint

소유:

- run/Stage/Act/difficulty/seed lineage.
- 공세·미션·보스 package와 RNG stream state.
- 세 물리 릴 전체 TokenInstance 배열·cursor·source 결속.
- 골드·식량·무료 회전·보관 용량·PendingReward.
- 배치 병력·HP·라인·식량 예약.
- 30개 건설 노드·건물·Tier·HP·lifecycle.
- 건설·업그레이드·수리·철거 project state와 payment snapshot.
- 거점·접전지·본진 소유권·HP.
- 미션·정산 event ID.
- `retry_used`.
- schema version·content manifest version·checksum.

### 6.3 SettingsSave

- 입력·오디오·그래픽·접근성·언어.
- 경제 transaction과 독립적으로 저장·복구한다.

### 6.4 TransactionJournal

최소 거래 유형:

```text
SPIN_CONFIRM
PENDING_REWARD_STORE
PENDING_REWARD_SELL
PENDING_REWARD_DEPLOY
CONSTRUCTION_START_OR_CANCEL
UPGRADE_START_OR_CANCEL
REPAIR_TICK_SETTLEMENT
DEMOLITION_COMPLETE
STAGE_SETTLEMENT
PAID_RETRY
PROFILE_UNLOCK
```

상태:

```text
PREPARED → APPLIED → COMMITTED
                   ↘ ROLLED_BACK
```

- 이미 `COMMITTED`인 idempotency key는 같은 receipt를 반환한다.
- `PREPARED/APPLIED`가 남으면 부팅 시 거래별 복구 정책을 실행한다.
- journal은 영구 gameplay log 전체를 대체하지 않는다.

---

## 7. Checkpoint 생성 시점

제품 checkpoint는 안정 경계에서만 생성한다.

```text
1. 새 MapRun 초기 준비 진입
2. 각 Stage 준비 단계 진입
3. Stage 정산 완료 후 다음 준비 상태
4. 명시적 저장·종료가 허용된 안정 planning 상태
```

금지:

- 활성 전투 임의 프레임 저장.
- transaction 중간 상태를 정상 checkpoint로 승격.
- 미확정 SpinSession preview를 live run state로 저장.
- PendingReward 거래의 절반만 적용된 상태 저장.

Stage 준비 checkpoint는 Retry 복원의 제품 권위다.

---

## 8. Save 원자성·손상 복구

권장 쓰기 절차:

```text
canonical state serialize
→ schema·manifest·lineage validation
→ checksum 생성
→ temporary file/record write
→ temporary read-back validation
→ transaction journal update
→ current를 last-known-good backup으로 보존
→ temporary를 current로 원자 교체
→ commit receipt 기록
```

규칙:

- checksum은 손상 탐지용이며 보안 서명으로 과장하지 않는다.
- 부분 write를 current save로 사용하지 않는다.
- future schema는 추정 로드하지 않고 안전하게 차단한다.
- 지원되는 과거 schema는 순차 migrator를 거쳐 새 임시 상태로 변환한 뒤 검증한다.
- migration 실패 시 원본과 backup을 변경하지 않는다.
- load 실패 시 current → backup 순으로 검증하며, 둘 다 실패하면 복구 UI와 진단 정보를 제공한다.
- 저장 실패를 성공 toast로 표시하지 않는다.

---

## 9. Schema·Manifest 버전

필수 필드:

```yaml
schema_version:
content_manifest_version:
created_at_utc:
last_committed_at_utc:
profile_id:
run_id:
checkpoint_id:
commit_id:
parent_commit_id:
checksum_algorithm:
checksum:
```

- schema version은 구조 호환성을 소유한다.
- content manifest version은 병종·건물·Stage 데이터 정합성을 소유한다.
- RNG algorithm/version이 결과에 영향을 주면 별도 버전 필드를 둔다.
- 실제 첫 schema 번호와 지원 migration 범위는 구현 Plan에서 정하되, `버전 없음`은 허용하지 않는다.

---

## 10. 결정론·Lineage

Retry와 save/load는 다음을 바꾸지 않는다.

- run seed.
- Stage manifest.
- 공세·보스 행동 seed.
- 룰렛 RNG stream state.
- 미션 후보·수락 상태.
- checkpoint 이전 입력·정산 사건.

복원 뒤 플레이어가 건설·릴 이동·배치 선택을 바꾸면 **같은 문제에 대한 다른 입력**으로 이후 상태가 달라질 수 있다. 이것은 재굴림이 아니다.

재현 증거:

```text
initial checkpoint hash
+ ordered player input log after restore
+ deterministic tick sequence
= final state hash
```

---

## 11. 시뮬레이션 전 확정된 구조와 보류 값

### 확정 구조

- 경제 영역과 프로필 영역 분리.
- Act 단위 비감소 회전가 구조.
- 이동 `n × P`.
- 무료 회전 금화의 canonical reference cost.
- 보관 병력 식량 0, 배치 시 예약.
- limited profile storage unlock, unlimited in-run expansion 금지.
- Retry Stage 5+, MapRun당 1회, 세 비용 Tier, 동일 RNG lineage.
- Profile/Checkpoint/Settings/Journal/Backup 분리.
- 안정 경계 checkpoint와 원자 save/restore.
- exact value는 Parameter Registry·시뮬레이션·사람 플레이 전 미확정.

### 보류 값

- 시작 골드·식량·무료 회전.
- 기본·접전지·금고 수입.
- 회전 base cost·Act multiplier.
- 이동 `P`·cap.
- 병력 판매가.
- 보관 기본 용량·unlock tier·비용·상한.
- 5건물 비용·시간·HP·Tier·수리·철거·취소 환불률.
- 영구재화 이름·획득 공식·반복 정산 점감.
- Retry T1/T2/T3 실제값.
- 최초 schema 번호·지원 migration 범위.

---

## 12. 적대적 검토 Gate

다음 실패 가설을 시뮬레이션·테스트해야 한다.

1. 회전가 증가가 릴 사용을 사실상 봉쇄한다.
2. 금고가 지속 수입과 금화 결과를 이중 증폭한다.
3. 접전지 선취가 복구 불가능한 경제 스노우볼을 만든다.
4. 보관함이 비가역 배치의 위험을 제거한다.
5. 판매가가 회전·이동 차익거래를 만든다.
6. 식량 cap 감소가 기존 병력을 제거한다.
7. 수리·취소·철거가 중복 환불 또는 무한 골드를 만든다.
8. Retry가 추가 생명처럼 항상 구매되거나 너무 비싸 사용되지 않는다.
9. 현재 런 미정산 영구재화로 자기 Retry를 충당한다.
10. checkpoint load가 seed·미션·룰렛 계보를 바꾼다.
11. 차감 후 load 실패가 재화 손실을 만든다.
12. journal replay가 이중 지급·이중 차감·무료 복원을 만든다.
13. save migration 실패가 current와 backup을 모두 훼손한다.

한 건이라도 재현되면 exact values와 구현 Gate를 닫지 않는다.

---

## 13. 다음 Gate

```text
PARAMETER_REGISTRY: CURRENT_NO_EXACT_VALUES
100K_SIMULATION_CONTRACT: CURRENT_NOT_RUN
SIMULATOR_AND_DATASET: NOT_CREATED
EXACT_VALUE_CANDIDATES: NOT_APPROVED
LATEST_RED_TESTS: NOT_CREATED
PRODUCT_SAVE_SCHEMA: NOT_IMPLEMENTED
PRODUCT_CODE: NOT_AUTHORIZED
CODEX: BLOCKED
```

다음 실행 순서:

```text
Parameter Registry·Sheet 동기화
→ 100,000-seed simulator Work Order
→ Candidate H0/H1/H2 생성
→ 자동 invariant·분포 보고
→ 사람 플레이 후보 축소
→ exact value Approval Bundle
→ 최신 Red tests
→ 제품 구현 Plan
```
