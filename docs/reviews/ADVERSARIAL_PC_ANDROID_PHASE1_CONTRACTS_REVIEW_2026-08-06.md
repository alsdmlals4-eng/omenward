# OMENWARD PC·Android Phase 1 계약 적대적 검토

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PC-ANDROID-PHASE1-CONTRACTS-V1
review_status: COMPLETE_WITH_TWO_FOUND_AND_FIXED_DEFECTS
base_main: aea0cf667e7c6fc5d4b9924cf9bb1ffc9eeddbe6
```

## 판정

명령·이벤트와 7개 플랫폼 계약은 기존 게임 동작을 바꾸지 않는 최소 경계로 구성됐다. 검토 중 자기참조 payload 재귀 오류와 공개 payload 변조 가능성을 실제 RED 테스트로 발견해 수정했다. 남은 계약은 실패 폐쇄형이며 플랫폼 구현 완료를 주장하지 않는다.

## 위험 원장

### OMW-AUD-P1-001 — DEVICE_OBJECT_LEAK
- 공격: `InputEvent`, Node 또는 SDK 객체를 command payload에 넣는다.
- 차단: 중첩 `Object`, `Callable`, `Signal`, `RID`를 invalid 처리한다.
- 상태: BLOCKED_BY_TEST.

### OMW-AUD-P1-002 — CYCLIC_PAYLOAD_RECURSION
- 공격: 자기참조 Dictionary·Array가 deep duplicate와 검증을 재귀 폭발시킨다.
- 실제 발견: 초기 구현은 `Max recursion reached`를 출력한 뒤 valid로 판정했다.
- 차단: 복사 전에 active-container identity stack으로 cycle을 탐지한다.
- 상태: FOUND_AND_FIXED.

### OMW-AUD-P1-003 — MUTABLE_PAYLOAD_ALIAS
- 공격: 생성 뒤 공개 Dictionary를 수정해 이미 발행된 command/event 의미를 바꾼다.
- 실제 발견: 초기 getter가 내부 Dictionary를 그대로 노출했다.
- 차단: 내부 `_payload`를 보존하고 getter·dictionary 변환은 deep copy를 반환한다.
- 상태: FOUND_AND_FIXED.

### OMW-AUD-P1-004 — EMPTY_SEMANTIC_ID
- 공격: 의미가 없는 빈 command/event를 전달한다.
- 차단: 빈 `StringName`은 invalid다.
- 상태: BLOCKED_BY_TEST.

### OMW-AUD-P1-005 — BASE_ADAPTER_FALSE_AVAILABILITY
- 공격: 구현되지 않은 base adapter가 성공 또는 store available을 반환한다.
- 차단: 빈 입력·unknown device, 명시적 `not_implemented`, store unavailable을 기본값으로 사용한다.
- 상태: BLOCKED_BY_TEST.

### OMW-AUD-P1-006 — CAPABILITY_STATE_MUTATION
- 공격: 반환된 capability 배열을 수정해 내부 지원 기능을 변경한다.
- 차단: 중복 제거된 새 PackedStringArray snapshot만 반환한다.
- 상태: BLOCKED_BY_TEST.

### OMW-AUD-P1-007 — CONTRACT_LOGIC_CREEP
- 공격: base contract에 OS 분기, 파일 접근, 플랫폼 singleton 또는 SDK 호출을 넣는다.
- 차단: 모든 contract는 RefCounted 기본값만 제공하며 domain 정적 guard를 유지한다.
- 상태: BLOCKED_BY_SCOPE_AND_STATIC_GUARD.

### OMW-AUD-P1-008 — PHASE1_EQUALS_PLATFORM_READY
- 공격: contract test PASS를 PC·Android 기능 또는 출시 Gate PASS로 기록한다.
- 차단: full runtime, composition, save, platform adapter, build, export, 세 Release Gate를 모두 NOT_RUN/NOT_STARTED로 유지한다.
- 상태: FAIL_CLOSED.

## 검증 경계

```text
COMMAND_EVENT_CONTRACT_TEST = LOCAL_PASS
STATIC_BOUNDARY_GUARD = LOCAL_PASS
FULL_PRIVATE_REPOSITORY_RUNTIME = NOT_RUN
SCENE_ASSEMBLY = NOT_RUN
PC_BUILD = NOT_RUN
ANDROID_BUILD = NOT_RUN
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
```
