# 변경 검토와 검증

- Skill ID: `foundation.validation-review`
- Category: `foundation`
- Registry: `docs/base/SKILL_REGISTRY.json`
- Shared contract: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건
- 검토·검수·PR·리뷰·감사
- Adversarial Review
- Red Teaming
- Critique–Refine

## 사용하지 않는 조건
- 아이디어 발산만 필요한 초기 탐색

## 고유 책임
- 증거 기반 판정
- 적대적 검토
- 레드팀 검증
- 비평–개선 루프
- 병합 게이트

## 입력
- 변경 diff
- 책임 원본
- 테스트·CI 상태
- 실행·시각 증거

## 절차
1. 정상 경로와 실패 경로를 분리한다.
2. Adversarial Review로 숨은 가정·누락·중복을 찾는다.
3. Red Teaming으로 오용·우회·권한·경계 조건을 공격한다.
4. P0·P1부터 수정한다.
5. Critique–Refine을 최대 3회 반복한다.
6. 독립 근거로 재검증하고 잔여 위험을 기록한다.

## 출력
- 심각도별 검토 결과
- 수정 내역
- 검증 증거
- 병합 가능 판정

## 고유 검수
- P0·P1이 남았는가.
- 테스트가 구현을 그대로 복제해 거짓 양성을 만드는가.
- 주장과 실제 diff가 일치하는가.
