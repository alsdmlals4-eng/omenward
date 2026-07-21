# Base 변경 제안과 동기화 관리

- Skill ID: `foundation.base-change-proposals`
- Category: `foundation`
- Registry: `docs/base/SKILL_REGISTRY.json`
- Shared contract: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건
- Base·공용 규칙·상위 템플릿
- Base Sync·공용 Skill·승격

## 사용하지 않는 조건
- 프로젝트 고유 사양만 바꾸는 작업

## 고유 책임
- Base 기준 커밋
- 채택·제외 근거
- 프로젝트 어댑터
- 역승격 후보

## 입력
- Base 최신 main
- 프로젝트 승인 규칙
- 기존 Base 버전 문서

## 절차
1. Base 최신 커밋과 프로젝트 기준을 비교한다.
2. 프로젝트 규칙과 충돌하는 항목을 제외한다.
3. 공용 원칙을 로컬 어댑터로 변환한다.
4. 복제·자동 덮어쓰기를 막는다.
5. Base 승격 후보는 별도 제안으로 분리한다.

## 출력
- Base 동기화 기록
- 채택·제외 표
- 로컬 어댑터 변경

## 고유 검수
- Base가 프로젝트 정본을 덮는가.
- 오래된 PR 커밋을 main으로 오인했는가.
- 원본 커밋이 기록됐는가.
