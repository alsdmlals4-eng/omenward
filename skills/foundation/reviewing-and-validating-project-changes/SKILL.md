# Reviewing and Validating Project Changes

- Skill ID: `foundation.validation-review`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

코드·데이터·문서·자산 변경을 계약·정본·정적·런타임·접근성·성능·회귀 증거로 판정할 때.

## 사용하지 않는 조건

변경이 없는 아이디어 비교 또는 같은 입력의 단순 검사 재실행.

## 고유 책임

실제 diff와 실행 증거를 기준으로 완료·부분·실패·미검증을 판정하고, 정본 변경의 untouched 소비자와 파생본까지 감사한다.

## 입력

- 승인 계약·보호 대상
- 실제 diff·정본·참조
- 테스트·런타임·렌더 환경
- 접근성·성능·호환성 기준

## 절차

- Modes: `contract-check → external-source-review → reference-freshness → static-validation → runtime-validation → accessibility-review → performance-profile → regression → evidence-report`
- 계약·범위와 실제 diff를 대조한다.
- 경로·ID·Schema·생성기 변경 시 untouched 소비자를 포함해 최신성을 감사한다.
- 정적 검사와 관련 자동 테스트를 실행한다.
- 가능한 실제 런타임·렌더·빌드·저장 경로를 확인한다.
- 대표·실패·경계·인접 회귀를 검사한다.
- 실행한 것과 미실행을 분리해 증거 등급을 보고한다.

## 출력

- finding·심각도·근거
- 정적·런타임·접근성·성능 결과
- 정본·참조 전파 결과
- 회귀·호환성 판정
- 미검증·롤백

## 고유 검수

- 파일 존재를 실행 성공으로 보지 않는다.
- 평균 FPS 하나로 성능을 통과시키지 않는다.
- 접근성 옵션 존재를 실제 장벽 해소로 오인하지 않는다.
