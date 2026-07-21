# Base Skill 통합 감사 — 2026-07-21

## 기준

- Omenward 기준 브랜치: `main@4cb0ae4b144f41597b0731a8cf26affff9713b13`
- Base 기준: `alsdmlals4-eng/Base@ee265576da7f67d3278f8099dd97d4e714ef0651`
- 통합 방식: 최신 Omenward `main`을 보존하고 Skill·운영체계만 추가
- 제외 범위: 게임 코드, Scene, 데이터, 시각자료, 대규모 문서 이주

## 범위

| 분류 | 수량 | 상태 |
|---|---:|---|
| Foundation | 7 | Registry 등록·패키지 존재 |
| Omenward Discipline | 11 | 전 분야 선택 |
| Specialist | 6 | 명시 트리거 선택 |
| 총 Skill | 24 | 1 ID : 1 경로 |
| 공통 실행 계약 | 1 | 모든 패키지가 참조 |
| 실행 Router | 1 | PLAN·BUILD·REVIEW 자동 판정 |
| CI Workflow | 1 | 무결성·라우팅·적대적 검토 계약 검사 |

## 채택한 Base 원칙

- PLAN / BUILD / REVIEW 분리
- 트리거 기반 자동 Skill 선택
- Foundation과 Specialist의 책임 분리
- Skill 패키지와 Registry의 1대1 무결성
- 프로젝트 정본 우선
- 검증하지 않은 결과의 완료 보고 금지

## Omenward 어댑터

- 11개 실제 프로젝트 분야를 `selected_disciplines`로 유지
- 주 책임 Discipline 1개, 지원 Discipline 최대 2개
- REVIEW에 통합 검수와 검증 Skill 강제
- 공통 규칙을 Shared Contract로 이동해 패키지 중복 축소
- 기존 `docs/` 구조를 유지하고 `[기획서]` 대규모 이주는 포함하지 않음

## 제외

- 과거 Base PR #18의 비병합 분기 내용을 현행 Base로 취급하지 않음
- Base 파일의 자동 복제·자동 덮어쓰기
- Omenward 승인 게임 규칙 변경
- 기존 시각자료의 상태 변경

## 판정

구조 검증은 CI와 `tools/validate_skill_system.py`가 담당한다. 실제 GitHub Actions 결과가 성공하기 전 증거 등급은 `PARTIAL`이다.
