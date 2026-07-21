# Skill 통합 적대적 검토·레드팀·비평–개선 기록

## Cycle 1 — Adversarial Review

### 공격 질문

- 오래된 브랜치가 최신 승인 파일을 덮는가?
- 문서 이주와 게임 코드가 Skill 통합에 불필요하게 섞였는가?
- 24개 Skill이 공통 규칙을 반복해 서로 다른 규칙으로 변질될 수 있는가?
- Registry가 존재해도 실제 패키지와 1대1인지 증명하는가?
- REVIEW에서 검증 Skill을 사용자가 실수로 빼도 되는가?

### 발견

- 기존 대형 PR은 최신 `main`과 diverged였고 게임·문서·시각자료까지 혼합됐다.
- 개별 Skill에 공통 규칙을 반복하면 유지보수 중 드리프트가 발생한다.
- 문서만으로는 Skill이 실제 선택되는지 증명할 수 없다.
- 테스트 이름의 존재가 실행 성공으로 오인될 수 있다.

### 개선

- 최신 `main`에서 슬림 브랜치를 새로 만들었다.
- 공통 규칙을 `SHARED_EXECUTION_CONTRACT.md` 하나로 통합했다.
- 기계 판독 Registry와 실행 가능한 Router를 추가했다.
- REVIEW 강제 스택과 증거 등급을 계약으로 고정했다.

## Cycle 2 — Red Teaming

### 공격 시나리오

1. 중복 ID 또는 중복 경로를 Registry에 삽입한다.
2. Registry에 없는 `SKILL.md`를 추가한다.
3. 존재하지 않는 Skill을 수동 지정한다.
4. “검토” 요청에서 통합 검수 Skill을 제거한다.
5. Specialist 트리거를 너무 넓혀 모든 요청에서 켠다.
6. Base 커밋을 오래된 PR SHA로 바꾼다.
7. `TODO`, `TBD`, `FIXME`가 남은 패키지를 완료로 보고한다.
8. 테스트를 실행하지 않고 파일 존재만으로 `PROVEN`을 주장한다.

### 방어

- Validator가 ID·경로 중복, 고아·누락 패키지, 의존성 오류를 실패 처리한다.
- Router가 미등록 수동 Skill을 거부한다.
- REVIEW 강제 스택을 테스트한다.
- Specialist는 양수 트리거 점수일 때만 선택한다.
- Base 기준 SHA와 프로젝트 우선 채택 정책을 Validator가 확인한다.
- 미완성 표식을 CI가 거부한다.
- Shared Contract가 `NOT_RUN`과 `PROVEN`을 분리한다.

## Cycle 3 — Critique–Refine

### 비평

- 키워드 Router는 의미론 모델보다 단순하며 동음이의어에 약하다.
- 지원 Discipline 선택은 점수 기반이라 복잡한 요청에서 사람이 조정해야 할 수 있다.
- CI 성공은 실제 게임 실행을 증명하지 않는다.

### 개선

- 수동 `--mode`, `--skill` 오버라이드를 제공하되 등록 ID만 허용한다.
- 선택 이유와 경로를 JSON으로 출력한다.
- Skill CI와 게임 CI를 분리해 증거 범위를 명확히 한다.
- 사람 판단이 필요한 경우 `확인 필요`로 중단하도록 Shared Contract에 남겼다.

## Cycle 4 — Schema·실행 순서 레드팀

### 추가 발견

- 초기 Schema는 Registry에 없던 `policy`를 요구했지만 Validator가 Schema 계약을 읽지 않아 거짓 통과할 수 있었다.
- Specialist 의존 Skill이 출력에서 Specialist 뒤에 배치되면 실행 순서가 역전될 수 있었다.

### 추가 개선

- Registry에 프로젝트 우선·자동 덮어쓰기 금지 정책을 명시했다.
- Validator가 Registry·Schema의 필수·허용 필드를 직접 대조하도록 강화했다.
- 의존성 순환을 차단하고 의존 Skill을 대상 Skill보다 먼저 정렬한다.
- 중복 ID 변조, 의존 순서, Specialist 과선택을 실제 테스트로 공격한다.

## 잔여 위험

- 자연어 라우팅은 모든 문맥을 완벽히 해석하지 못한다.
- GitHub Actions가 실제 성공하기 전 구조 판정은 `PARTIAL`이다.
- Skill 시스템은 프로젝트 작업 방법을 관리하며 게임 기능 자체의 정상 작동을 대신 증명하지 않는다.
