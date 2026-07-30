# 오멘워드 버티컬 슬라이스 패배·영구재화 재시도 계약

- 결정 ID: `OMW-DEC-20260731-DEFEAT-RETRY-V1`
- 승인일: `2026-07-31`
- 상세 승인 시각: `2026-07-31T08:42:00+09:00`
- 상태: `USER_APPROVED_DETAIL / EXACT_COST_VALUES_PENDING`
- Work Mode: `PLAN / PLANNING_ONLY_PROFILE`
- 제품 구현 권한: `NONE`
- Benchmark: `docs/benchmarks/OMENWARD_DEFEAT_RETRY_CHECKPOINT_META_BENCHMARK_2026-07-31.md`

## 1. 제품 패배 계약

1. 본진 HP가 0이 되면 현재 MapRun은 패배 상태가 된다.
2. 유료 재시도를 선택하지 않으면 현재 MapRun은 종료된다.
3. 체크포인트는 저장·종료·복귀와 승인된 재시도 복원의 안전 경계다.
4. 활성 전투 임의 프레임 저장·복원은 버티컬 슬라이스 범위가 아니다.
5. 패배 종료는 런 내 자원과 빌드의 소멸을 수반하지만, 이미 정산된 프로필 진행은 보존한다.

## 2. 유료 재시도 계약

```yaml
paid_retry:
  currency: permanent_meta_currency
  available_from_stage: 5
  maximum_per_maprun: 1
  restore_point: failed_stage_preparation_checkpoint
  same_rng_lineage: true
  current_run_pending_currency_usable: false
  exact_costs: pending_simulation
```

세부 규칙:

1. 유료 재시도는 Stage 5부터 사용할 수 있다.
2. 하나의 MapRun에서 최대 1회만 사용할 수 있다.
3. 실패한 Stage의 준비 단계 진입 checkpoint로 복원한다.
4. 같은 Stage, 같은 공세 구성·출격 시각, 같은 보스 행동 seed, 같은 룰렛 RNG 계보, 같은 미션 상태를 복원한다.
5. 플레이어는 복원된 준비 단계에서 건설·룰렛 이동·배치 선택을 바꿀 수 있지만 seed·공세·미션 후보를 바꿔 재굴림할 수 없다.
6. 현재 MapRun에서 아직 정산되지 않은 영구재화는 재시도 비용에 사용할 수 없다.
7. 런 시작 전에 프로필에 적립된 사용 가능 영구재화만 비용으로 사용할 수 있다.
8. 현재 런 골드·식량·무료 회전으로 비용을 대체할 수 없다.
9. 재시도 비용은 Stage 5~10, 11~15, 16~20의 세 비용 등급을 사용한다.
10. 정확한 수치와 배율은 메타 경제·100,000 seed 시뮬레이션과 사람 플레이 승인 전 확정하지 않는다.

## 3. 비용 등급

| 실패 Stage | 비용 등급 | 수치 상태 |
|---|---|---|
| 1~4 | 재시도 불가 | 확정 |
| 5~10 | `RETRY_COST_TIER_1` | 수치 미정 |
| 11~15 | `RETRY_COST_TIER_2` | 수치 미정 |
| 16~20 | `RETRY_COST_TIER_3` | 수치 미정 |

불변 조건:

```text
RETRY_COST_TIER_1 < RETRY_COST_TIER_2 < RETRY_COST_TIER_3
```

Stage 1~4에서는 손실 시간이 짧고 신규 플레이어가 비용의 가치를 판단하기 어려우므로 유료 재시도를 제공하지 않는다.

## 4. 복원 상태

유료 재시도는 다음 상태를 실패 Stage 준비 checkpoint 값으로 복원한다.

- Stage·Act·difficulty·run seed
- 적 공세 패키지, 라인, 수량, 출격 시각과 특수 행동
- 보스 행동 패키지와 phase seed
- 룰렛 RNG stream과 TokenInstance 배열
- TokenSource 결속·BLOCKED·파괴 상태
- 미션 제시·수락·진행 상태
- 보유 골드·식량·무료 회전
- 보관 병력·배치 병력·병력 HP와 라인
- 건물·업그레이드·수리·건설 작업
- 거점·중앙 지역·본진 HP와 소유권
- PendingReward와 정산 사건 ID
- `retry_used` 이전 상태와 checkpoint schema version

실패한 전투에서 새로 발생한 피해, 사망, 점령 변화, 자원 소비, 미션 진행과 미정산 보상은 폐기한다.

## 5. 패배 종료 시 보존과 소멸

### 영구 보존

- 이미 정산된 영구재화
- 도감·기록·첫 발견
- 해금된 선택지
- 업적
- 장식·문양
- 접근성·조작·환경설정
- 누적 플레이 통계

### MapRun 종료 시 소멸

- 골드
- 식량
- 무료 회전
- 보관·배치 병력
- 건물과 업그레이드
- 영토 점령 상태
- 릴 배열과 TokenSource
- 진행 중 미션
- 실패 Stage의 미정산 보상

강한 영구 능력치 상승은 이 계약에서 승인하지 않는다. 메타 진행은 우선 기록·해금 선택 폭·장식 중심으로 설계한다.

## 6. 패배 화면 UX

패배 화면은 두 선택만 제공한다.

1. `런 종료`
2. `영구재화로 재시도`

재시도 선택에는 다음을 사전 표시한다.

- 정확한 비용
- 차감 후 잔액
- 복원 Stage와 checkpoint
- 같은 seed·공세·룰렛 계보 유지
- 이번 MapRun의 남은 재시도 횟수
- 실패 Stage의 미정산 결과가 폐기됨

벨루는 선택을 대신하지 않고 복원 범위와 비용만 요약한다.

## 7. 원자 거래와 실패 처리

```text
checkpoint 유효성 확인
→ 프로필 영구재화 잔액 확인
→ retry transaction 예약
→ checkpoint 복원
→ 영구재화 차감 확정
→ retry_used = true 저장
```

멱등성 키는 다음 조합을 사용한다.

```text
profile_id + run_id + checkpoint_id + retry_index
```

복원 실패 시:

- 영구재화를 차감하지 않는다.
- 기존 패배 상태를 유지한다.
- 이전 정상 profile·checkpoint를 파괴하지 않는다.
- 같은 transaction의 중복 실행을 막는다.

재화 차감 뒤 최종 저장이 실패한 경우에는 transaction journal을 기준으로 재개하거나 롤백하며, 이중 차감과 무료 복원을 모두 금지한다.

## 8. 개발·플레이테스트 재시도

```yaml
development_retry:
  cost: 0
  limit: test_configuration
  same_seed: true
  meta_rewards: disabled
  achievements: disabled
  official_records: disabled
  result_label: NON_PRODUCT_TEST_RUN
```

개발용 무료 재시도는 보스·밸런스·checkpoint 검증을 위한 도구다. 제품 완주율, 정상 메타 획득, 업적과 공식 기록의 증거로 사용할 수 없다.

## 9. 검증 계약

자동 검증:

- Stage 1~4에서 제품 유료 재시도 비활성
- MapRun당 1회 상한
- 같은 seed·공세·미션·룰렛 계보 복원
- 미정산 보상 중복 지급 0
- 프로필 영구재화 이중 차감 0
- 복원 실패 시 재화 손실 0
- 개발 재시도에서 메타 보상·업적·공식 기록 0

사람 플레이:

- 비용과 복원 범위를 선택 전에 설명할 수 있음
- 재시도가 결과 재굴림이 아니라 같은 문제 재도전임을 이해함
- 후반 피로 완화와 패배 긴장감의 균형
- 재시도 선택 후 후회·불공정 체감
- 재시도 선택률·재실패율·완주율

## 10. 미확정 수치

- 영구재화 공식 명칭
- 영구재화 획득 공식과 런 정산량
- `RETRY_COST_TIER_1/2/3` 실제값
- 비용 등급 간 정확한 배율
- 메타 해금·장식과 재시도 비용의 경제적 기회비용
- 반복 클리어 보상 점감

## 11. 금지 규칙

- 무료 무제한 제품 재시도
- MapRun당 두 번 이상 제품 재시도
- Stage 1~4 유료 재시도 유도
- 재시도 시 seed·공세·미션 후보·룰렛 계보 변경
- 현재 런 미정산 영구재화로 자기 재시도 비용 충당
- 현재 런 골드·식량·무료 회전으로 비용 대체
- 재화 차감과 checkpoint 복원을 비원자 거래로 처리
- 개발 재시도 결과를 정상 제품 플레이 증거로 사용

## 12. 상태 경계

```text
USER_APPROVED_DETAIL
!= EXACT_COST_VALUES_APPROVED
!= META_CURRENCY_NAME_APPROVED
!= META_ECONOMY_PROVEN
!= SAVE_SCHEMA_IMPLEMENTED
!= PRODUCT_CODE_AUTHORIZED
```

이 계약은 패배 종료, Stage 5 이후 MapRun당 1회 유료 재시도, 준비 checkpoint 복원, 동일 RNG 계보, 미정산 재화 사용 금지와 원자 거래를 확정한다. 정확한 영구재화 명칭·획득량·비용 수치는 후속 시뮬레이션 승인 전 구현 사양이 아니다.
