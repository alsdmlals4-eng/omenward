# Managing Base Change Proposals

- Skill ID: `foundation.base-change-proposals`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

프로젝트 교훈을 Base 공용 원리로 승격하거나 최신 Base를 프로젝트에 명시적으로 채택할 때.

## 사용하지 않는 조건

프로젝트 고유 값만 있거나 승인 없이 Base를 직접 변경할 때.

## 고유 책임

프로젝트 정본 우선 원칙 아래 Base 변경 제안과 프로젝트 채택을 분리하고, 기준 커밋·적용·수정·제외 이유를 기록한다.

## 입력

- 프로젝트 증거·반복 패턴
- Base 기준 커밋·현재 Registry
- 공용/전용 경계
- 사용자 승인·PR 상태

## 절차

- Modes: `extract → submit → review → implement-approved → verify → adopt-project`
- 공용 원리와 프로젝트 고유 값을 분리한다.
- Base 최신 커밋과 프로젝트 기준을 비교한다.
- 제안과 구현 PR을 분리한다.
- 프로젝트 채택 시 적용·수정·제외를 명시한다.
- 승인된 변경과 검증만 완료로 표시한다.

## 출력

- Base change proposal
- 프로젝트 채택 매트릭스
- 기준 커밋 기록
- 검증·미검증
- 다음 승격 후보

## 고유 검수

- Base 원격을 자동 덮어쓰지 않는다.
- 미검증 성공 한 번을 공용 강제 규칙으로 승격하지 않는다.
- 제안 PR과 구현 PR을 섞지 않는다.
