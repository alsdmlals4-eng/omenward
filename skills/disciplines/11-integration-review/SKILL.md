# Omenward Integration Review

- Skill ID: `discipline.integration-review`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

분야 간 누락·중복·정본 충돌·출시 gate·PR 전체 범위를 검수할 때.

## 사용하지 않는 조건

한 분야 내부의 작은 편집만 확인할 때.

## 고유 책임

11개 분야·Base capability·실제 구현·문서·자산·테스트의 연결을 no-loss 기준으로 검수한다.

## 입력

- 승인 계약·프로젝트 코어
- 분야 책임 원본·Registry
- 실제 diff·테스트·발행본
- 보류·백업·제거 후보·롤백

## 절차

- Modes: `cross-discipline → no-loss → release-gate → pr-check`
- 주 책임과 실제 영향 분야를 확인한다.
- 변경됐어야 하지만 untouched인 문서·코드·테스트·파생본을 찾는다.
- 중복 정본·고아 경로·Alias·coverage·호환성을 검사한다.
- 게임 코드·문서·Skill 변경의 범위 혼합을 분리한다.
- P0·P1·P2와 미검증·롤백을 기록한다.

## 출력

- 누락·중복·충돌 finding
- 기능 보존·coverage 판정
- PR 범위·체크 결과
- release gate·미검증·롤백

## 고유 검수

- 변경 파일만 보고 untouched 소비자를 놓치지 않는다.
- 서로 다른 범위의 PR을 합쳐 검증을 흐리지 않는다.
- CI 성공을 사람 플레이·시각 QA로 오인하지 않는다.
