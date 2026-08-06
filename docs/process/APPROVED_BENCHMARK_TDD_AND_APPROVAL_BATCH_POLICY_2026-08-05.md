# [현행] OMENWARD 벤치마킹·TDD·승인 배치 운영 정책

```yaml
policy_id: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
approved_at: 2026-08-05 00:41 KST
approval: USER_DIRECT_APPROVAL
status: CURRENT_PROCESS_AUTHORITY
counter_effect: NON_COUNTER_POLICY
```

## 1. 필수 정책 표식

```text
BENCHMARK_REQUIRED
INDUSTRY_COMPARISON_REQUIRED
MAX_APPROVAL_BATCH: 10
EARLY_CHECKPOINT_ON_HIGH_RISK_CONFLICT
EARLY_CHECKPOINT_ON_SESSION_END
EARLY_CHECKPOINT_ON_LARGE_CANON_IMPACT
TDD_MANDATORY
RED → GREEN → REFACTOR
EXPLICIT_BRANCH_REQUIRED_FOR_GITHUB_MUTATION
DIRECT_MAIN_WRITE: FORBIDDEN
```

## 2. 벤치마킹과 현업 비교

질문·기획·검수·구현 계획에서 외부 사례가 판단을 개선할 수 있으면 관련 벤치마크와 현업 관행을 조사한다.

기본 출력 구조:

```text
비교 대상
→ 가져올 원칙
→ 오멘워드와 다른 조건
→ 그대로 복제하지 않을 부분
→ 권장안
```

규칙:

- 최신성이 중요한 사례는 현재 공식 자료를 우선 확인한다.
- 게임 규칙·도구·엔진·API처럼 정확성이 중요한 내용은 공식 문서·개발사 자료·원 논문을 우선한다.
- 커뮤니티 자료는 공식 근거가 없거나 플레이어 반응을 비교할 때만 보조 근거로 사용한다.
- 관련성이 낮은 벤치마크를 형식적으로 끼워 넣지 않는다.
- 유명 게임의 기능을 프로젝트 핵심 재미와 검증 없이 복제하지 않는다.
- 권장안은 반드시 오멘워드의 `예고된 압력 → 제작한 확률 → 비가역 커밋 → 복기` 인과에 맞는지 평가한다.

## 3. 승인 배치

```text
MAX_APPROVAL_BATCH: 10
```

- 승인 10건은 한 정본 배치의 최대 크기다.
- 10건에 도달하면 GitHub 책임 원본·중앙 라우터·Google Sheet를 동기화하고 fresh preflight 뒤 병합한다.
- 10건 미만이어도 다음 조건이면 조기 체크포인트를 허용한다.

```text
EARLY_CHECKPOINT_ON_HIGH_RISK_CONFLICT
= P0/P1 정본 충돌, 구현 입력 오염, 데이터 손실·권위 역전 위험

EARLY_CHECKPOINT_ON_SESSION_END
= 세션 종료·컨텍스트 손실 전에 안전한 인수인계가 필요

EARLY_CHECKPOINT_ON_LARGE_CANON_IMPACT
= 여러 핵심 문서·Sheet 탭·후속 결정 의존성을 동시에 바꿈
```

조기 체크포인트는 배치 카운터를 임의 초기화하지 않는다. 병합 목적과 다음 카운터 상태를 명시한다.

## 4. TDD

모든 기능·버그 수정·검증 규칙·행동 변경은 다음 순서를 따른다.

```text
TDD_MANDATORY
RED → GREEN → REFACTOR
```

### RED

- 변경 전 실패 조건을 테스트·검증 규칙·수용 기준으로 먼저 작성한다.
- 반드시 예상 이유로 실패하는 것을 확인한다.
- 문서 기획은 책임 원본 부재, 금지 규칙 누락, 중앙 라우팅 충돌, Sheet 불일치를 자동 검증한다.
- 제품 구현은 실제 코드 행동을 재현하는 자동 테스트를 먼저 작성한다.

### GREEN

- 실패를 통과시키는 최소 변경만 한다.
- unrelated refactor와 추가 기능을 섞지 않는다.
- 정확 수치가 승인되지 않은 기획에서 임의 수치를 구현하지 않는다.

### REFACTOR

- Green 뒤 중복·모호성·불필요한 장문을 정리한다.
- 정본 의미와 테스트 결과를 바꾸지 않는다.
- 리팩터링 뒤 전체 검증을 다시 실행한다.

예외는 사용자가 명시적으로 승인한 throwaway prototype·자동 생성 파일·순수 구성 변경뿐이며, 예외 여부도 기록한다.

## 5. GitHub 변경 안전

```text
EXPLICIT_BRANCH_REQUIRED_FOR_GITHUB_MUTATION
DIRECT_MAIN_WRITE: FORBIDDEN
```

- 파일 생성·수정·삭제 요청은 PR 작업 중 반드시 명시적 비기본 branch를 전달한다.
- `branch=null`, branch 생략, default-branch 암묵 해석으로 쓰기 작업을 수행하지 않는다.
- main 변경은 검증된 PR의 merge action으로만 수행한다.
- 실수로 main에 직접 기록되면 해당 결과를 정본으로 취급하지 않고, 원인 기록→복구 PR→CI→병합 후 정상 작업을 재개한다.
- 제품 코드·Scene·Resource·게임 데이터는 별도 사용자 승인 없이 병합하지 않는다.

## 6. 질문과 권장안

질문이 필요한 경우 한 번에 핵심 질문 하나만 제시한다. 선택지가 있다면 2~3개 접근을 비교하고 다음을 포함한다.

```text
권장안
장점
포기 비용
벤치마크·현업 차이
핵심 재미 적합성
적대적 검토 결과
```

사용자가 `권장안대로 진행`을 승인하면 승인 범위 안에서 설계 문서·계획·TDD·정본 동기화·PR 검증을 계속한다. 새로운 핵심 규칙이나 제품 구현 권한까지 자동 확장하지 않는다.

## 7. 완료 기준

작업 완료 보고에는 다음을 분리한다.

- 실제 변경 파일과 Decision/Policy ID.
- RED 실패 증거와 GREEN 검증 증거.
- 벤치마크와 현업 비교에서 채택·비채택한 원칙.
- GitHub·Sheet bounded read-back.
- 제품 구현·시뮬레이션·런타임·사람 QA의 실행 여부.
- 남은 위험과 다음 승인 Gate.
