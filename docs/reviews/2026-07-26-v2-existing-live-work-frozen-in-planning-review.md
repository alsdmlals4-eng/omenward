# V2 기존 live 작업 전술계획 정지 적대적 검수

- 검수일: 2026-07-26
- 검수 번호: `F-25`
- 대상 문서: `APPROVED_V2_EXISTING_LIVE_WORK_FROZEN_IN_PLANNING_2026-07-26.md`
- 결과: `F-25: RESOLVED`
- 결정: `FREEZE_EXISTING_LIVE_WORK_AT_ENTRY_PROGRESS`
- 제품 코드 승인: `NO`

## 1. 검수 질문

전술계획 진입 전에 이미 live world에서 진행 중이던 시간 기반 작업이 공유 1초 planning horizon을 받아야 하는가?

## 2. 검토한 대안

### A. 기존 live 작업은 entry progress에서 정지

- 현재 planning session에서 새로 생성된 작업만 공유 horizon 사용.
- 기존 작업은 진입 시 progress와 remaining duration 유지.
- 반복 진입으로 무료 진행 불가.

### B. planning 진입마다 기존 작업도 1초 진행

- 반복 진입으로 무료 가속 가능.
- global simulation 정지 계약과 충돌.
- rejected.

### C. 작업 생애 동안 한 번만 headstart 제공

- 영구 eligibility와 사용 session 기록 필요.
- 상태 복잡도와 stale basis가 증가.
- rejected.

## 3. 공격 시나리오

### F-25-A: 반복 진입 가속

```text
작업 elapsed 6초
→ planning 진입
→ 종료
→ 재진입
```

통과 조건:

- 모든 진입에서 기존 작업 elapsed는 6초.
- entry/exit 횟수로 progress 증가 0.

### F-25-B: 남은 0.2초 자동 완료

기존 live 작업 remaining이 0.2초인 상태로 planning 진입한다.

통과 조건:

- planning 중 완료되지 않음.
- 완료 capability를 새로 노출하지 않음.
- 전투 재개 후 실제 0.2초가 경과해야 완료.

### F-25-C: 신규 작업과 기존 작업 혼합

```text
기존 A elapsed 6초
신규 B duration 3초
```

통과 조건:

- A elapsed 6초.
- B elapsed 1초.
- A가 horizon time을 소비하거나 받지 않음.

### F-25-D: replay 누적

명령 추가·취소로 queue replay를 여러 번 수행한다.

통과 조건:

- 기존 A는 entry progress 유지.
- 신규 B도 공유 horizon 결과 이상으로 누적되지 않음.

### F-25-E: confirm 이중 진행

통과 조건:

- confirm에서 기존 작업에 1초를 추가하지 않음.
- timer epoch 재설정으로 progress를 보정하지 않음.
- receipt 이후 다음 live tick부터 진행.

### F-25-F: 명시적 철거와 passive progress 혼동

통과 조건:

- 철거·취소는 command contract에 따른 명시적 transition.
- 해당 transition 전에 기존 작업을 1초 진행하지 않음.
- command transition과 horizon progress를 혼합하지 않음.

### F-25-G: confirm 실패

통과 조건:

- 기존 progress·timer·completion mutation 0.
- 신규 작업 promotion·resource debit·time resume 0.

### F-25-H: duplicate transaction

통과 조건:

- 같은 receipt 반환.
- progress·timer·completion·resource·resume 중복 0.

## 4. 불변식 검토

승인 문서는 다음을 명시한다.

```text
EXISTING_LIVE_WORK_HEADSTART_ELIGIBILITY: NOT_ELIGIBLE
PLANNING_SESSION_CREATED_WORK_HEADSTART: ELIGIBLE
PLANNING_ENTRY_LIVE_WORK_PROGRESS_SNAPSHOT: PRESERVED
EXISTING_LIVE_WORK_PROGRESS_DURING_PLANNING: FROZEN
EXISTING_LIVE_WORK_COMPLETION_DURING_PLANNING_HORIZON: FORBIDDEN
PLANNING_REENTRY_FREE_PROGRESS: FORBIDDEN
EXISTING_LIVE_WORK_TIMER_REBASE_ON_CONFIRM: FORBIDDEN
POST_CONFIRM_EXISTING_LIVE_WORK_RESUME: FROM_ENTRY_PROGRESS
```

## 5. 범위 검토

이번 검수는 다음을 승인하지 않는다.

- 기존 live 작업 취소 시 환불률.
- 수리·생산 queue 상세 정책.
- 위험 전투 실시간 처리 변경.
- 제품 코드·Scene·Resource·게임 데이터 구현.
- 최종 Codex 인계.

## 6. 최종 판정

```text
F-25_RESULT: APPROVED
EXISTING_LIVE_WORK_HEADSTART_POLICY: RESOLVED_FROZEN_AT_ENTRY_PROGRESS
EXISTING_LIVE_WORK_CANCELLATION_ECONOMICS: REVIEW_PENDING
PRODUCT_CODE_AUTHORIZED: NO
```

기존 live 작업은 planning entry progress에서 고정한다. 공유 1초 horizon은 현재 planning session에서 새로 생성된 작업에만 적용한다.
