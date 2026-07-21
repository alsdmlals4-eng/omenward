# Omenward Skill 공통 실행 계약

모든 `skills/**/SKILL.md`는 이 계약을 상속한다. 개별 Skill은 고유 판단만 정의하며 공통 안전·검증 규칙을 반복하지 않는다.

## 우선순위

1. 사용자의 최신 지시
2. 승인된 Plan·Issue·Goal
3. `AGENTS.md`와 프로젝트 책임 원본
4. 실제 코드·데이터·Scene·실행 증거
5. `docs/BASE_RULES_VERSION.md`가 고정한 Base 원칙
6. 외부 참고 자료

Skill은 프로젝트 정본을 덮어쓰는 권한이 없다.

## Work Mode

- `PLAN`: 읽기·분석·제안만 수행한다. 제품 코드·Scene·Resource·데이터를 수정하지 않는다.
- `BUILD`: 승인된 범위만 최소 변경으로 구현한다.
- `REVIEW`: 증거를 수집하고 병합 가능 여부를 판정한다. 명백한 결함 수정은 승인 범위 안에서만 수행한다.

모드가 불명확하면 `PLAN`으로 시작한다.

## 자동 라우팅

1. `foundation.project-intake`는 모든 프로젝트 작업에 항상 선택한다.
2. 주 책임 Discipline은 최대 1개, 지원 Discipline은 최대 2개다.
3. Specialist는 명시적 트리거가 있을 때만 선택한다.
4. `REVIEW`에는 `foundation.validation-review`와 `discipline.integration-review`를 항상 추가한다.
5. 같은 산출물을 둘 이상의 Skill이 동시에 소유하지 않는다. 주 책임 Skill이 편집하고 지원 Skill은 검토만 한다.
6. 사용자가 Skill을 직접 지정하면 Registry에 존재하는 ID만 허용한다.

## 공통 실행 순서

1. 요청을 목표·범위·제외 범위·완료 기준으로 정규화한다.
2. 책임 원본과 실제 파일을 찾는다.
3. 변경 지도와 보호 경로를 만든다.
4. 선택된 Skill의 고유 절차를 수행한다.
5. `Adversarial Review`로 숨은 가정, 누락, 중복, 잘못된 완료 주장을 찾는다.
6. `Red Teaming`으로 실패 경로, 악의적 입력, 권한 우회, 오래된 파일, 부분 적용을 공격한다.
7. `Critique–Refine`을 최대 3회 반복한다. P0·P1이 남으면 완료하지 않는다.
8. 독립된 검증으로 결과를 확인한다.
9. 실행·미실행·잔여 위험을 분리해 보고한다.

## 심각도

- `P0`: 데이터 손실, 정본 파괴, 보안·권한 우회, 빌드 불가, 핵심 규칙 반전
- `P1`: 주요 기능 오동작, 잘못된 병합 판정, 반복 가능한 누락·중복
- `P2`: 제한된 경로의 오류, 유지보수 위험, 검증 공백
- `P3`: 표현·정리·후속 개선

## 증거 등급

- `PROVEN`: 자동 검사와 실제 실행 또는 독립된 근거가 일치
- `PARTIAL`: 일부 검사만 완료
- `NOT_RUN`: 실행하지 않음
- `FAILED`: 검사 실패
- `BLOCKED`: 선행 조건이 없어 실행 불가

문서에 테스트 이름이 존재한다는 사실은 `PROVEN`이 아니다.

## 완료 보고

- 선택한 Work Mode와 Skill
- 변경 파일과 이유
- Adversarial Review·Red Teaming에서 발견한 문제
- Critique–Refine 수정 회차
- 실행한 검증과 결과
- 미검증 항목
- 잔여 위험과 병합 판정
