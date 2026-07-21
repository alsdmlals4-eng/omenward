# 게임 프로젝트 운영체계 관리

- Skill ID: `foundation.project-operating-system`
- Category: `foundation`
- Registry: `docs/base/SKILL_REGISTRY.json`
- Shared contract: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건
- 운영체계
- 폴더 구조
- 워크플로
- Registry·Schema·자동화

## 사용하지 않는 조건
- 개별 게임 기능 구현
- 단일 문구 수정

## 고유 책임
- 저장소 운영 규칙
- 책임 경로
- 자동화 경계
- Work Mode 연결

## 입력
- `AGENTS.md`
- `docs/BASE_RULES_VERSION.md`
- 문서 지도
- CI·도구 구조

## 절차
1. 현재 운영체계의 책임 원본을 찾는다.
2. 중복 라우터와 고아 경로를 식별한다.
3. 최소 구조로 통합안을 만든다.
4. 자동 검증 가능 지점을 연결한다.
5. 이전 경로의 호환·폐기 상태를 기록한다.

## 출력
- 운영체계 변경안 또는 반영
- 경로·책임 매트릭스
- 회귀 검증

## 고유 검수
- 활성 책임 원본이 하나인가.
- 이전 경로가 조용히 깨지지 않는가.
- 프로젝트 규칙이 Base보다 우선하는가.
