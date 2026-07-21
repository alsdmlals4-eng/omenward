# 통합 검수

- Skill ID: `discipline.integration-review`
- Category: `disciplines`
- Registry: `docs/base/SKILL_REGISTRY.json`
- Shared contract: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건
- 통합·전체 검수
- 출시·병합 게이트
- 누락·중복·정합성

## 사용하지 않는 조건
- 초기 아이디어만 필요한 단계

## 고유 책임
- 분야 간 충돌
- 누락·중복
- 최종 병합 준비도

## 입력
- 모든 변경
- 책임 문서
- 테스트·CI
- Handoff

## 절차
1. 변경 지도를 만든다.
2. 분야별 소유권을 대조한다.
3. Adversarial Review와 Red Teaming을 수행한다.
4. Critique–Refine 뒤 잔여 위험을 판정한다.

## 출력
- 통합 검수표
- 병합 판정
- 후속 작업

## 고유 검수
- 문서·코드·테스트가 같은 규칙을 말하는가.
- 범위 밖 변경이 섞였는가.
