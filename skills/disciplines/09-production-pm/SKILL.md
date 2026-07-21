# Omenward Production PM

- Skill ID: `discipline.production-pm`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

범위·우선순위·의존성·마일스톤·Vertical Slice gate·위험을 운영할 때.

## 사용하지 않는 조건

일정·범위 영향 없는 단일 문구 수정.

## 고유 책임

활동 목록이 아니라 검증 가능한 결과·선행 조건·게이트·롤백으로 작업을 순서화한다.

## 입력

- 승인 목표·범위·제외
- 작업 결과·의존성·공유 자원
- 위험·가치·피드백 속도
- 마일스톤·완료 증거

## 절차

- Modes: `scope → dependencies → sequence → vertical-slice-gate → risk → milestone`
- 결과 단위로 작업을 분해한다.
- BLOCKS·INFORMS·USES_OUTPUT·SHARES_RESOURCE·VALIDATES를 구분한다.
- 위험·가치·피드백 속도로 순서를 정한다.
- 안전한 병렬 묶음과 단계별 검증·롤백을 정의한다.
- 새 사실에 따라 재계획한다.

## 출력

- 범위·제외
- 의존성 그래프·실행 순서
- 병렬 묶음·게이트
- 위험·롤백
- 마일스톤·Vertical Slice 판정

## 고유 검수

- 근거 없는 일정 숫자를 만들지 않는다.
- 같은 파일·Schema를 무분별하게 병렬화하지 않는다.
- 한 기능 Done을 프로젝트 gate 통과로 오인하지 않는다.
