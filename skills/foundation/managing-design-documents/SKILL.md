# 기획 문서와 책임 원본 관리

- Skill ID: `foundation.design-documents`
- Category: `foundation`
- Registry: `docs/base/SKILL_REGISTRY.json`
- Shared contract: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건
- 기획서·GDD·문서
- 승인 문서·정본
- Proposal·Spec

## 사용하지 않는 조건
- 코드만 변경하는 작업
- 일회성 메모

## 고유 책임
- 문서 생명주기
- 승인 상태
- 책임 원본
- 파생본 정합성

## 입력
- `DOCUMENTATION_MAP`
- 승인 문서
- Handoff·Roadmap·Issue

## 절차
1. 주제별 활성 책임 원본을 지정한다.
2. 중복·상충 문서를 분류한다.
3. 승인·보류·백업 상태를 명시한다.
4. 관련 문서의 동기화 범위를 계산한다.
5. 링크와 파생본을 검증한다.

## 출력
- 갱신된 책임 문서
- 중복·충돌 처리표
- 문서 검증 결과

## 고유 검수
- 같은 주제 정본이 둘 이상인가.
- 승인 상태를 파일명만으로 추정하는가.
- 끊긴 링크나 오래된 파생본이 있는가.
