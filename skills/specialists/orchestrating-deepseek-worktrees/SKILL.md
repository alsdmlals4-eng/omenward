# 외부 분석 작업트리 오케스트레이션

- Skill ID: `specialist.deepseek-worktrees`
- Category: `specialists`
- Registry: `docs/base/SKILL_REGISTRY.json`
- Shared contract: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건
- DeepSeek·외부 에이전트
- Worktree·병렬 분석·분석 위임

## 사용하지 않는 조건
- 단일 에이전트로 충분한 작은 작업
- 비공개 자료를 권한 없이 외부로 보내는 경우

## 고유 책임
- 분석 분할
- 입력 최소화
- 결과 검증
- 브랜치 격리

## 입력
- 작업 계약
- 공개 가능한 자료
- 저장소 상태
- 검증 기준

## 절차
1. 독립적인 읽기 전용 과제로 분할한다.
2. 각 작업트리의 보호 경로를 지정한다.
3. 결과를 주장·근거·불확실성으로 받는다.
4. 중복과 충돌을 통합 검토한다.
5. 최종 변경은 주 작업자가 재검증한다.

## 출력
- 위임 패키지
- 결과 통합표
- 채택·기각 근거

## 고유 검수
- 외부 결과를 검증 없이 적용했는가.
- 두 작업자가 같은 파일을 소유하는가.
