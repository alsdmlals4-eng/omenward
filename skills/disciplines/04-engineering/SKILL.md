# 개발·엔지니어링

- Skill ID: `discipline.engineering`
- Category: `disciplines`
- Registry: `docs/base/SKILL_REGISTRY.json`
- Shared contract: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건
- Godot·GDScript·코드
- 버그·성능·저장·데이터 구조

## 사용하지 않는 조건
- 승인되지 않은 제품 방향 변경

## 고유 책임
- 코드 구조
- 상태 소유
- 성능
- 테스트 seam

## 입력
- 승인 사양
- 코드·Scene·Resource
- 기존 테스트

## 절차
1. 호출 흐름과 상태 소유를 찾는다.
2. 최소 diff로 구현한다.
3. 정상·경계·실패 경로를 테스트한다.

## 출력
- 코드 변경
- 자동 테스트
- 실행 결과

## 고유 검수
- 상태가 중복 소유되는가.
- 테스트가 실제 공개 동작을 검증하는가.
