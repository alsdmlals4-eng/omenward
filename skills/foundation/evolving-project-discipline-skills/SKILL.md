# 프로젝트 Skill 진화와 최적화

- Skill ID: `foundation.skill-evolution`
- Category: `foundation`
- Registry: `docs/base/SKILL_REGISTRY.json`
- Shared contract: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건
- Skill 추가·통합·최적화
- 라우팅 개선
- 중복 Skill

## 사용하지 않는 조건
- 한 번만 쓰는 임시 절차

## 고유 책임
- Skill 경계
- 트리거
- 중복 제거
- 학습 반영
- Registry 정합성

## 입력
- `SKILL_REGISTRY.json`
- Skill 패키지
- 실행 보고
- 반복 실패 사례

## 절차
1. 기존 Skill로 해결 가능한지 먼저 확인한다.
2. 책임·입력·출력이 겹치는 Skill을 통합한다.
3. 공통 규칙은 Shared Contract로 이동한다.
4. 개별 Skill에는 고유 판단만 남긴다.
5. Registry·테스트·문서를 함께 갱신한다.

## 출력
- 최적화된 Skill 패키지
- 변경 이유
- 호환·별칭 처리
- 무결성 검사

## 고유 검수
- 새 Skill이 기존 Skill과 중복되는가.
- 트리거가 너무 넓어 항상 선택되는가.
- 패키지와 Registry가 1대1인가.
