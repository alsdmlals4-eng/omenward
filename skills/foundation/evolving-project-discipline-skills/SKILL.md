# Evolving Project Discipline Skills

- Skill ID: `foundation.skill-evolution`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

Skill을 생성·통합·가지치기하거나 Registry·라우팅·Learning Log를 개선할 때.

## 사용하지 않는 조건

Skill 구조에 영향 없는 일반 구현.

## 고유 책임

consolidation-first로 기존 mode 확장을 우선하고 독립 입력·산출물·검증·승인 경계가 있을 때만 Skill을 분리한다.

## 입력

- Registry·entrypoint·실제 패키지
- 기존 modes·references·scripts
- 실패·교훈·작업 사례
- alias·coverage·검증 경로

## 절차

- Modes: `inventory → decide-boundary → create-or-integrate → register → verify → learn`
- Registry와 실제 패키지·entrypoint를 대조한다.
- 중복·과분할·누락·죽은 자료를 판정한다.
- 고유 기능·검증·호환성을 먼저 보존한다.
- Skill·mode·reference 중 가장 작은 단위로 통합한다.
- Alias·coverage·라우팅·테스트를 동기화한다.
- 실제 증거가 있는 교훈만 학습한다.

## 출력

- 통합 전후 구조
- 책임 보존표
- Registry·alias·coverage
- 라우팅·콜드 스타트 결과
- Learning Log 후보

## 고유 검수

- 기존 mode 검토 없이 새 Skill을 만들지 않는다.
- 이름만 합치며 기능·검증을 잃지 않는다.
- 전체 skills 폴더를 기본 로드하지 않는다.
