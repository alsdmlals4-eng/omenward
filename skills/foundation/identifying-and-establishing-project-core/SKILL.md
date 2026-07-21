# Identifying and Establishing Project Core

- Skill ID: `foundation.project-core`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

기존 프로젝트 코어를 근거로 판정하거나 PLAN에서 새 코어 계약을 제안·승인·기록할 때.

## 사용하지 않는 조건

단순 기능 브레인스토밍 또는 사용자 승인 없는 코어 확정.

## 고유 책임

기획·시스템·기술 코어와 MVP 지원·콘텐츠·외피를 분리하고, 읽기 전용 판정과 사용자 승인 기반 확정을 mode로 엄격히 분리한다.

## 입력

- 프로젝트 정체성·대상 플레이어
- 승인 문서·실제 코드·데이터·자산·테스트
- 핵심 행동·선택·피드백·루프
- 제약·PoC·플레이테스트·대안
- 승인 권한

## 절차

- Modes: `identify-existing → propose → stress-test → confirm → lock → reopen → record`
- 기존 프로젝트는 제거·대체·변경 테스트로 읽기 전용 판정한다.
- PROJECT_CORE·CORE_SUPPORT·MVP_SUPPORT·CONTENT_VARIANT·PRESENTATION_SHELL·TECHNICAL_FOUNDATION으로 분류한다.
- 새 코어는 정체성·행동·루프·불변·변경 가능 외피를 제안한다.
- 실패·제거·대체·확장 반례로 최소성을 공격한다.
- confirm·lock은 명시적 사용자 승인 뒤에만 실행한다.
- 승인된 코어만 정본·게이트·검수 기준에 기록한다.

## 출력

- 코어 판정 상태
- 정체성 한 문장
- 기획·시스템·기술 코어
- MVP 지원·변경 가능 외피
- 반례·근거·미검증
- 승인·재개 기록

## 고유 검수

- 기능 목록 전체를 코어로 만들지 않는다.
- 기술 의존성과 제품 정체성을 혼동하지 않는다.
- 사용자 승인 없이 CORE_CONFIRMED/RECORDED로 전환하지 않는다.
