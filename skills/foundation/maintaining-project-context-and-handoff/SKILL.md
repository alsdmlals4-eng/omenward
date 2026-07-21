# Maintaining Project Context and Continuity

- Skill ID: `foundation.context-handoff`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

현재 상태·다음 작업·위험을 압축하거나 긴 작업을 checkpoint로 중단·재개해야 할 때.

## 사용하지 않는 조건

상태 변화가 없는 짧은 대화.

## 고유 책임

Active Context·Handoff와 장기 작업 checkpoint를 구분해, 실제 결과·증거·다음 정확한 행동으로 재개 가능성을 유지한다.

## 입력

- 현재 목표·범위
- 완료 결과·변경 파일
- 검증·미검증·차단
- 보호 결정·남은 완료 기준

## 절차

- Modes: `active-context → handoff → initialize → checkpoint → resume → partial-delivery → close`
- 책임 원본 전문을 복제하지 않고 현재 차이만 압축한다.
- 큰 작업을 독립 검증 가능한 결과로 나눈다.
- 의미 있는 단계마다 완료 결과·증거·다음 행동을 기록한다.
- 중단 시 완료·미완료·차단 원인·재개 입력을 분리한다.
- 재개 시 최신 checkpoint와 정본만 읽는다.

## 출력

- Active Context 갱신
- Handoff 스냅샷
- checkpoint
- 부분 산출물과 재개 지점
- 완료·미완료 판정

## 고유 검수

- 진행 중을 완료로 표시하지 않는다.
- 백그라운드 완료나 시간 예측을 약속하지 않는다.
- 같은 질문을 반복하거나 전문을 복제하지 않는다.
