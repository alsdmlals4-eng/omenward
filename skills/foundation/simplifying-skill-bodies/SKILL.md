# Simplifying Skill Bodies

- Skill ID: `foundation.skill-simplification`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

비대해진 SKILL.md·라우터를 항상 필요한 계약과 조건부 reference로 분리할 때.

## 사용하지 않는 조건

안전 규칙·핵심 절차를 숨기거나 일반 문장만 교정할 때.

## 고유 책임

항상 필요한 목적·권한·입력·절차·출력·게이트만 본문에 남기고 조건부 상세를 발견 가능한 reference로 이동한다.

## 입력

- 대상 Skill·라우터
- 호출 빈도·조건부 세부
- 기존 references·링크
- 기능 보존 사례·검증

## 절차

- Modes: `inventory → classify-always-vs-conditional → extract-references → rewrite-router → validate-disclosure`
- 각 문단이 매 호출의 행동을 바꾸는지 판정한다.
- 항상 필요한 계약과 조건부 지식을 분리한다.
- 긴 예시·템플릿·상세 판정표를 의미 있는 reference로 묶는다.
- 본문에 읽는 조건과 정확한 경로를 남긴다.
- 대표·예외 요청에서 발견성과 기능 보존을 검증한다.

## 출력

- 전후 본문 크기
- 유지 계약
- 이동 reference·호출 조건
- 중복 통합
- 기능 보존·링크 결과

## 고유 검수

- 목차만 남긴 빈 라우터로 만들지 않는다.
- 중요 안전 규칙을 깊은 reference에 숨기지 않는다.
- 이동한 세부를 본문에서 연결하지 않는 상태를 허용하지 않는다.
