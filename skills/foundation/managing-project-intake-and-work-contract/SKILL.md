# Managing Project Intake and Work Contract

- Skill ID: `foundation.project-intake`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

L1 이상 요청의 의도·범위·권한·완료 기준·작업 순서를 한 번만 확정해야 할 때.

## 사용하지 않는 조건

오탈자·동일 검사 재실행처럼 결과와 위험이 명확한 L0 작업.

## 고유 책임

Work Mode와 최소 Skill을 자동 선택하고, 저장소 사실·보호 대상·의존성·검증·롤백이 있는 실행 계약을 만든다.

## 입력

- 사용자 최신 요청과 승인
- 현재 저장소·브랜치·책임 원본
- 보호 경로·제외 범위
- 완료 기준·검증 환경

## 절차

- Modes: `route → clarify → contract → decompose-sequence → execution-report`
- 요청 수준과 현재 단계를 판정한다.
- Registry trigger와 비사용 조건으로 최소 Skill을 선택한다.
- 이미 제공된 사실은 다시 묻지 않고 결과를 바꾸는 누락만 확인한다.
- 단계를 결과·입력·출력·게이트·검증·롤백으로 분해한다.
- 실제 사용 Skill과 증거·미검증을 보고한다.

## 출력

- Work Mode·Skill·mode 선택
- 범위·제외·보호 대상
- 실행 단계·의존성·게이트
- 완료 기준·검증·롤백
- 실행 보고

## 고유 검수

- 사용자에게 Skill 선택을 전가하지 않는다.
- 같은 요청의 범위 판정을 여러 Skill에서 반복하지 않는다.
- 승인되지 않은 제품 변경을 계약에 포함하지 않는다.
