# 오멘워드 버티컬 슬라이스 패배·영구재화 재시도 원칙

- 결정 ID: `OMW-DEC-20260731-DEFEAT-RETRY-V1`
- 승인일: `2026-07-31`
- 상태: `USER_APPROVED_PRINCIPLE / DETAIL_VALUES_PENDING`
- Work Mode: `PLAN / PLANNING_ONLY_PROFILE`
- 제품 구현 권한: `NONE`
- Benchmark: `docs/benchmarks/OMENWARD_DEFEAT_RETRY_CHECKPOINT_META_BENCHMARK_2026-07-31.md`

## 1. 승인된 제품 원칙

1. 본진 HP가 0이 되면 기본적으로 현재 MapRun은 패배 상태가 된다.
2. 패배는 원칙적으로 현재 MapRun 종료로 이어진다.
3. 플레이어는 영구재화를 소모해 재시도를 선택할 수 있다.
4. 재시도는 무료 기본권이 아니라 패배 종료를 막는 선택형 예외다.
5. 영구재화의 공식 명칭, 정확 비용, 횟수 제한과 막별 가중치는 후속 경제·메타 설계에서 확정한다.
6. checkpoint는 저장·종료·복귀와 유료 재시도 복원의 안전 경계로 사용하되, 활성 전투 임의 프레임 저장은 범위가 아니다.
7. 개발·플레이테스트에서는 같은 seed Stage 재시도를 무료로 제공할 수 있지만 제품 규칙, 메타 보상과 기록에서 분리한다.

## 2. 현재 설계 방향

다음은 후속 상세 계약의 기본 방향이며 아직 수치 정본이 아니다.

- 유료 재시도는 가장 최근의 유효한 Stage 준비 checkpoint를 사용한다.
- 같은 Stage, 같은 공세 정보, 같은 RNG 계보와 같은 미션 상태를 복원해 재굴림을 막는다.
- 영구재화 차감과 checkpoint 복원은 원자 거래여야 한다.
- 로드 실패 시 영구재화가 손실되지 않아야 한다.
- 현재 실패한 Stage의 미정산 보상은 중복 지급되지 않아야 한다.

## 3. 미확정 상세 항목

- MapRun당 재시도 허용 횟수.
- Stage 또는 Act에 따른 비용 곡선.
- 현재 런에서 새로 획득한 영구재화를 즉시 재시도 비용으로 사용할 수 있는지.
- 패배 시 보존되는 기록·도감·해금·메타 재화의 정확한 범위.
- 유료 재시도 후 미션 진행도와 보상 판정 복원 규칙.
- checkpoint 직렬화 필드와 재화 차감 transaction ID.
- 저장 손상·호환 불가 버전의 안전 처리.

## 4. 금지 규칙

- 무료 무제한 제품 재시도.
- 재시도 시 seed·공세·미션 후보 변경을 통한 결과 재굴림.
- 재시도 비용을 현재 런 골드·식량·무료 회전으로 대체.
- 재화 차감 성공과 checkpoint 복원을 별도 비원자 거래로 처리.
- 개발용 무료 재시도 기록을 정상 플레이 완료·메타 획득 증거로 사용.

## 5. 상태 경계

```text
USER_APPROVED_PRINCIPLE
!= EXACT_COST_APPROVED
!= RETRY_LIMIT_APPROVED
!= META_ECONOMY_APPROVED
!= SAVE_SCHEMA_APPROVED
!= PRODUCT_CODE_AUTHORIZED
```

이 계약은 제품 패배 철학과 영구재화 재시도 존재를 확정한다. 정확한 비용·횟수·복원 필드는 후속 상세 설계와 시뮬레이션 승인 전 구현 사양이 아니다.
