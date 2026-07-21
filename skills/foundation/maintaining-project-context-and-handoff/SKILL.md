# 프로젝트 컨텍스트와 인수인계 유지

- Skill ID: `foundation.context-handoff`
- Category: `foundation`
- Registry: `docs/base/SKILL_REGISTRY.json`
- Shared contract: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건
- Handoff·인수인계
- Active Context
- 작업 재개·상태 캡슐

## 사용하지 않는 조건
- 장기 상태와 무관한 단일 작업

## 고유 책임
- 현재 방향
- 완료·미완료
- 다음 행동
- 보호 대상·재개 절차

## 입력
- `HANDOFF_CONTEXT`
- `ACTIVE_CONTEXT`
- Roadmap
- 최근 PR·Issue·실행 증거

## 절차
1. 정본에서 현재 상태를 재구성한다.
2. 완료와 주장만 있는 항목을 분리한다.
3. 다음 행동과 선행 조건을 기록한다.
4. 오래된 경로·브랜치를 제거한다.
5. 새 작업자가 재개 가능한지 역검증한다.

## 출력
- Handoff 갱신
- 재개 체크리스트
- 불확실성 목록

## 고유 검수
- 실행하지 않은 검증을 완료로 썼는가.
- 로컬 전용 경로를 정본으로 썼는가.
- 다음 행동이 구체적인가.
