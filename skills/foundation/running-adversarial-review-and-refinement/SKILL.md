# Running Adversarial Review and Refinement

- Skill ID: `foundation.adversarial-review`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

작업물이 실패했다고 가정해 결함을 공격하고 비판을 재검증한 뒤 유효한 문제만 최소 개선할 때.

## 사용하지 않는 조건

칭찬·균형 평가만 필요하거나 실제 diff 실행 증거 검증만 필요할 때.

## 고유 책임

공격·비판 검증·승인된 최소 개선·회귀 재공격을 분리해 코어와 장점을 보호한다.

## 입력

- 작업물·승인 범위
- 프로젝트 코어·보호 장점
- 정본·실제 diff
- 완료 기준·검증 환경·변경 권한

## 절차

- Modes: `attack → validate-critique → refine-approved-findings → regression-recheck → decision-report`
- 실패·모순·누락·악용·경계 조건을 공격한다.
- 각 비판의 사실성·가능성·영향·범위·비용을 재판정한다.
- MUST_FIX와 승인된 SHOULD_FIX만 BUILD에서 최소 수정한다.
- 정상 경로·코어·장점과 새 결함을 다시 공격한다.
- 반영·보류·기각·미검증을 모두 기록한다.

## 출력

- 공격 관점·실패 가정
- finding·근거·심각도
- MUST_FIX/SHOULD_FIX/DEFER/REJECT/UNVERIFIED
- 최소 변경
- 회귀 재검토·남은 위험

## 고유 검수

- 레드팀 지적을 전부 수용하지 않는다.
- 취향·잘못된 전제·범위 밖 요구를 결함으로 반영하지 않는다.
- 개선 뒤 regression-recheck를 생략하지 않는다.
