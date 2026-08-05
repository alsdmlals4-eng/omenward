# OMENWARD PC·Android Phase 1 명령·이벤트·플랫폼 계약

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PC-ANDROID-PHASE1-CONTRACTS-V1
parent_architecture_decision: OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1
parent_phase0_decision: OMW-DEC-20260806-PC-ANDROID-PHASE0-FREE-LOCAL-V1
base_main: aea0cf667e7c6fc5d4b9924cf9bb1ffc9eeddbe6
phase_status: IMPLEMENTED_LOCAL_PASS_CANDIDATE
product_code_authority: PHASE1_CONTRACT_TYPES_ONLY
verification_mode: FREE_LOCAL_ONLY
```

## 1. 승인 범위

Phase 1은 플랫폼 구현이 아니라 이후 구현이 따라야 할 타입과 실패 폐쇄형 기본 동작을 추가한다.

```text
GAME_COMMAND = IMPLEMENTED
GAME_EVENT = IMPLEMENTED
INPUT_ADAPTER_CONTRACT = IMPLEMENTED
DISPLAY_ADAPTER_CONTRACT = IMPLEMENTED
SAVE_ADAPTER_CONTRACT = IMPLEMENTED
LIFECYCLE_ADAPTER_CONTRACT = IMPLEMENTED
PERFORMANCE_ADAPTER_CONTRACT = IMPLEMENTED
STORE_ADAPTER_CONTRACT = IMPLEMENTED
PLATFORM_CAPABILITIES = IMPLEMENTED
PRODUCT_BEHAVIOR_CHANGE = NONE
```

기존 전투·경제·룰렛·건물 서비스와 Scene, Resource, 데이터, export preset, store SDK는 변경하지 않는다.

## 2. Domain 값 객체

### GameCommand

```gdscript
GameCommand.action_id: StringName
GameCommand.payload: Dictionary
GameCommand.is_valid() -> bool
GameCommand.to_dictionary() -> Dictionary
```

### GameEvent

```gdscript
GameEvent.event_id: StringName
GameEvent.payload: Dictionary
GameEvent.is_valid() -> bool
GameEvent.to_dictionary() -> Dictionary
```

명령과 이벤트는 다음 규칙을 따른다.

- 비어 있는 의미 ID는 invalid다.
- 생성자 입력 Dictionary를 deep copy한다.
- `payload` getter와 `to_dictionary()`는 매번 격리된 복사본을 반환한다.
- 중첩 `Object`, `Callable`, `Signal`, `RID`를 거부한다.
- 자기참조 Array·Dictionary를 복사하기 전에 탐지하고 거부한다.
- 키·마우스·터치 index, Scene 노드, SDK 객체를 domain payload 정본으로 사용하지 않는다.

## 3. 플랫폼 계약

모든 계약은 `RefCounted`이며 실제 PC·Android 로직을 포함하지 않는다.

```gdscript
InputAdapter.poll_commands() -> Array[GameCommand]
InputAdapter.active_device() -> StringName

DisplayAdapter.display_snapshot() -> Dictionary
DisplayAdapter.apply_settings(settings: Dictionary) -> Dictionary

SaveAdapter.load_payload(slot_id: StringName) -> Dictionary
SaveAdapter.write_payload_atomic(slot_id: StringName, payload: Dictionary) -> Dictionary

LifecycleAdapter.lifecycle_event(event_id: StringName)

PerformanceAdapter.budget_snapshot() -> Dictionary

StoreAdapter.capabilities() -> PackedStringArray
StoreAdapter.is_available() -> bool

PlatformCapabilities.has_capability(capability_id: StringName) -> bool
PlatformCapabilities.all_capabilities() -> PackedStringArray
```

기본값:

- Input: 빈 명령 목록, active device `unknown`.
- Display·Save·Performance: `{"ok": false, "error": "not_implemented"}`.
- Store: unavailable, capability 없음.
- PlatformCapabilities: 생성 시 받은 ID만 중복 제거해 보존하고 외부 mutator를 제공하지 않는다.

## 4. TDD 증거

```text
PLAN_COMMIT = 55957ab3bc056f069c64ba4e2c83b72568838f2f
INITIAL_RED_COMMIT = b81acf6d5d841d959a32e01f5606f4f13f90f35a
INITIAL_RED = MISSING_9_CONTRACT_PATHS / EXIT_1
INITIAL_GREEN_COMMIT = 85ccd00849851b55b0048521814759e9a281353c
CYCLE_RED_COMMIT = dd2d5a1e7e93950e49d547d6b49c91111e526827
CYCLE_RED = MAX_RECURSION_AND_2_ASSERTION_FAILURES / EXIT_1
CYCLE_FIX_COMMIT = e890b7a7a34d83e3d1a1d2149085241a0e216c8f
PAYLOAD_ALIAS_RED_COMMIT = f7e52b718945d913a659046c5890c942d407a398
PAYLOAD_ALIAS_RED = 2_ASSERTION_FAILURES / EXIT_1
PAYLOAD_ISOLATION_FIX_COMMIT = 63f571bc5741a28020d5a49bad0938a7c774375f
```

무료 로컬 GREEN:

```text
GODOT_VERSION = 4.7.1.stable.official.a13da4feb
EDITOR_CLASS_SCAN = EXIT_0
PLATFORM_CONTRACT_TEST = EXIT_0
PLATFORM_CONTRACT_OUTPUT = Platform contract checks passed
PYTHON_STATIC_UNITTEST = 3_PASS / EXIT_0
STATIC_GUARD = ALLOWED_LEGACY_3 / UNAPPROVED_0 / STALE_0 / EXIT_0
PY_COMPILE = PASS
```

실행은 사용자 제공 Godot 4.7.1과 exact Phase 1 파일을 포함한 최소 격리 harness에서 수행했다. 전체 비공개 저장소 checkout·main Scene 실행·build·export 증거로 확대하지 않는다.

## 5. 변경 경계

```text
GAME_SESSION_DECOUPLING = NOT_STARTED
GAME_APPLICATION = NOT_STARTED
SESSION_DRIVER = NOT_STARTED
SCENE_BINDER = NOT_STARTED
PLATFORM_BOOTSTRAP = NOT_STARTED
SHARED_SAVE_SCHEMA = NOT_STARTED
PC_ADAPTER_IMPLEMENTATION = NOT_STARTED
ANDROID_ADAPTER_IMPLEMENTATION = NOT_STARTED
STORE_SDK_INTEGRATION = NOT_STARTED
EXPORT_PRESETS = ABSENT
FULL_PROJECT_RUNTIME = NOT_RUN
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
RELEASE_BLOCKED_UNVERIFIED
```

Phase 1 통과는 계약 타입의 로컬 동작만 증명한다. 플랫폼 지원 완료, 저장 완료, PC·Android 빌드 완료 또는 출시 가능 상태를 의미하지 않는다.
