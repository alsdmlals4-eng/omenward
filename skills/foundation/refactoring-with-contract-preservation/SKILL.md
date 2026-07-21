# Refactoring with Contract Preservation

- Skill ID: `foundation.contract-refactor`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

코드·문서·자동화·Skill 구조의 중복과 복잡성을 승인 동작·인터페이스·데이터 호환성을 유지하며 줄일 때.

## 사용하지 않는 조건

기능·정책·Schema 변경이 목적이거나 baseline 없이 구조를 바꿀 때.

## 고유 책임

정상·실패·경계·인터페이스·데이터 baseline을 고정한 뒤 가장 작은 단계로 구조를 개선하고 회귀를 증명한다.

## 입력

- 승인 동작·범위
- 공개 인터페이스·출력
- Schema·호환성
- 현 구현·baseline 테스트
- 보호 경로·검증 환경

## 절차

- Modes: `baseline-contract → smell-audit → refactor → regression-validate → report`
- 동작·API·파일·Schema·출력·성능 baseline을 고정한다.
- 중복·긴 책임·강결합·잘못된 추상화를 근거로 찾는다.
- 가장 작은 이동·추출·명명·중복 통합을 수행한다.
- 단계마다 baseline과 실제 결과를 비교한다.
- 구조 개선과 의도적 동작 변경을 분리 보고한다.

## 출력

- 보존 계약·baseline
- 구조 문제·근거
- 리팩토링 diff
- 기능·인터페이스·데이터 보존 증거
- 회귀·미검증

## 고유 검수

- 테스트를 삭제해 통과시키지 않는다.
- 리팩토링 명목으로 기능·정책·Schema를 바꾸지 않는다.
- 불필요한 추상화와 파일 수만 늘리지 않는다.
