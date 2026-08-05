# [승인 설계] OMENWARD PC·Android 공용 코어·플랫폼 어댑터 아키텍처

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1
decision_status: APPROVED_DESIGN_NOT_IMPLEMENTED
parent_platform_decision: OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1
baseline_main: f5e4bcee7f8459fcfeb492f1ebc19ff932a352f0
architecture_scope: COMMON_CORE_AND_PC_ANDROID_ADAPTER_BOUNDARIES
product_code_authority: NONE
runtime_validation: NOT_RUN
```

## 1. 판정

```text
ARCHITECTURE_STATUS = APPROVED_DESIGN_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
PC_ANDROID_ADAPTER_IMPLEMENTATION = NOT_STARTED
RUNTIME_VALIDATION = NOT_RUN
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
GATE_TRANSFER_POLICY = PASS_DOES_NOT_TRANSFER
```

이 문서는 제품 구현 승인이 아니라, Codex가 이후 제품 RED 테스트와 구현 계획을 작성할 때 따라야 할 구조적 책임 원본이다. 현재 프로토타입을 PC 완성 뒤 Android로 복제하지 않고, 게임 규칙과 상태를 하나의 공용 코어로 유지하면서 플랫폼 차이를 어댑터로 격리한다.

## 2. 저장소 현행 감사

```text
CURRENT_ENGINE = GODOT_4_7
CURRENT_MAIN_SCENE = res://scenes/main/main.tscn
CURRENT_VIEWPORT = 960x540
CURRENT_STRETCH_MODE = VIEWPORT_INTEGER_SCALE
CURRENT_RENDERER = GL_COMPATIBILITY
CURRENT_EXPORT_PRESETS = ABSENT
CURRENT_PLATFORM_ADAPTER_ROOT = ABSENT
CURRENT_SAVE_ADAPTER = ABSENT
CURRENT_LIFECYCLE_ADAPTER = ABSENT
CURRENT_STORE_ADAPTER = ABSENT
```

### 유지할 강점

- `scripts/core`, `scripts/battle`, `scripts/buildings`, `scripts/roulette`에 규칙·상태·결정론 서비스가 이미 분리되어 있다.
- `RouletteService`처럼 `RefCounted` 기반이며 입력 Dictionary와 상태 서비스를 받아 결과를 반환하는 코드는 공용 코어 후보로 유지한다.
- `DeterminismService`, `StageManifest`, 입력 로그는 플랫폼 간 동일 결과 검증의 기반으로 재사용한다.
- `CoreUxService.snapshot()`처럼 화면이 소비할 읽기 전용 스냅샷을 만드는 방향은 공유 ViewModel 경계로 발전시킨다.

### 현재 결합과 공백

- `GameSession`은 `Node`, `_process(delta)`, 부모 Scene의 `Battlefield`·`UI/StageHud` 탐색을 동시에 담당한다. 세션 규칙, Godot 프레임 구동, Scene 조립 책임이 한 파일에 섞여 있다.
- 프로젝트 설정은 단일 viewport와 renderer만 정의한다. PC 창·전체화면 정책, Android safe area·밀도·백 버튼·가상 키보드 정책은 없다.
- 제품 스크립트에는 `FileAccess`와 `user://` 저장 경로가 없고, 버전 저장 스키마·원자 쓰기·모바일 백그라운드 저장도 없다.
- Steam·STOVE·Google Play SDK를 감싸는 저장소 내부 어댑터가 없다.
- `export_presets.cfg`가 없으므로 PC/Android 대표 export 구성과 재현 가능한 빌드 증거가 없다.
- 현재 상태는 플랫폼 독립 코어가 완성된 것이 아니라, 플랫폼 기능을 아직 붙이지 않은 프로토타입이다.

## 3. 목표 구조

```text
scenes / controls
        │ semantic UI intent
        ▼
scripts/application
  GameApplication / SessionDriver / CommandRouter
        │ commands, queries, events, snapshots
        ▼
scripts/domain + scripts/core
  deterministic rules / state / simulation / save DTO
        ▲
        │ interfaces only
        │
scripts/platform/contracts
  InputAdapter
  DisplayAdapter
  SaveAdapter
  LifecycleAdapter
  PerformanceAdapter
  StoreAdapter
  PlatformCapabilities
        ▲
        ├─ scripts/platform/pc
        └─ scripts/platform/android
```

```text
COMMON_CORE_BOUNDARY = PLATFORM_NEUTRAL_DOMAIN_AND_SIMULATION
COMMON_CORE_GODOT_NODE_DEPENDENCY = FORBIDDEN
COMMON_CORE_SCENE_TREE_LOOKUP = FORBIDDEN
COMMON_CORE_DIRECT_INPUT_API = FORBIDDEN
COMMON_CORE_DIRECT_DISPLAY_API = FORBIDDEN
COMMON_CORE_DIRECT_FILE_API = FORBIDDEN
COMMON_CORE_DIRECT_STORE_SDK = FORBIDDEN
COMMAND_EVENT_BOUNDARY = REQUIRED
```

`RefCounted`, `Resource`, `StringName`, `Vector2`처럼 직렬화·결정론을 해치지 않는 Godot 값 타입은 단계적으로 허용할 수 있다. 그러나 공용 코어가 `Node`, SceneTree, `Input`, `DisplayServer`, `FileAccess`, 플랫폼 SDK를 직접 호출해서는 안 된다.

## 4. 계층별 책임

### 4.1 공용 Domain/Core

소유:

- 전투·경제·건물·룰렛·Stage 진행 규칙
- 결정론적 RNG와 입력 로그
- 플랫폼과 무관한 명령, 이벤트, 오류 코드
- 저장 가능한 정본 상태와 스키마 버전
- 화면에 필요한 의미 기반 snapshot/ViewModel

소유하지 않음:

- 마우스 좌표·터치 index·키 코드
- 창 크기·safe area·노치·DPI
- 파일 경로와 Android 앱 생명주기
- Steam·STOVE·Google Play 객체
- 진동·가상 키보드·OS 종료 요청

### 4.2 Application/Composition

`GameSession`을 다음 책임으로 분해한다.

- `GameApplication`: 명령을 공용 코어에 전달하고 이벤트를 배포한다.
- `SessionDriver`: Godot `_process`와 lifecycle 신호를 platform-neutral tick/pause/resume 명령으로 변환한다.
- `SceneBinder`: `Battlefield`, HUD, 메뉴 Scene을 찾아 ViewModel과 이벤트를 연결한다.
- `PlatformBootstrap`: 실행 환경에 맞는 어댑터 묶음을 생성해 Application에 주입한다.

Scene 노드 탐색은 `SceneBinder`에서만 허용하며 domain/core에서는 금지한다.

### 4.3 필수 계약

```text
INPUT_ADAPTER_INTERFACE = REQUIRED
DISPLAY_ADAPTER_INTERFACE = REQUIRED
SAVE_ADAPTER_INTERFACE = REQUIRED
LIFECYCLE_ADAPTER_INTERFACE = REQUIRED
PERFORMANCE_ADAPTER_INTERFACE = REQUIRED
STORE_ADAPTER_INTERFACE = REQUIRED
PLATFORM_CAPABILITIES_INTERFACE = REQUIRED
```

권장 인터페이스 의미:

- `InputAdapter`: 장치 입력을 `GameCommand`로 정규화하고 활성 장치·포인터 모드를 보고한다.
- `DisplayAdapter`: viewport, window, safe-area, scale category를 반환하고 표시 설정을 적용한다.
- `SaveAdapter`: byte/text payload를 원자적으로 읽고 쓰며 저장 위치를 소유한다.
- `LifecycleAdapter`: foreground, pause, background, resume, quit 의도를 이벤트로 제공한다.
- `PerformanceAdapter`: 품질 tier, frame budget, low-memory·thermal 힌트를 제공한다.
- `StoreAdapter`: 로그인, 업적, 클라우드 저장 등 지원 capability만 노출한다. 게임 규칙을 소유하지 않는다.
- `PlatformCapabilities`: 현재 실행 환경에서 실제 가능한 기능 집합을 읽기 전용으로 제공한다.

## 5. 입력 경계

### PC

```text
PC_INPUT = KEYBOARD_MOUSE_GAMEPAD
PC_POINTER = MOUSE_AND_OPTIONAL_GAMEPAD_FOCUS
PC_BACK_INTENT = ESCAPE_OR_GAMEPAD_CANCEL
```

- 키보드·마우스와 게임패드는 동일한 의미 명령을 생성한다.
- UI focus navigation과 포인터 입력을 모두 제공한다.
- 장치 전환 시 도움말 glyph만 바꾸고 게임 상태를 변경하지 않는다.

### Android

```text
ANDROID_INPUT = TOUCH_BACK_GESTURE_VIRTUAL_KEYBOARD
ANDROID_POINTER = MULTI_TOUCH_WITH_EXPLICIT_GESTURE_POLICY
ANDROID_BACK = NAVIGATION_INTENT_NOT_UNCONDITIONAL_QUIT
TOUCH_AS_MOUSE_ONLY = FORBIDDEN
```

- 터치 입력을 마우스 클릭으로만 치환하지 않는다.
- 탭, drag, long-press, 스크롤, 취소 의도를 명시적 명령으로 변환한다.
- Android back은 현재 UI 계층을 닫거나 일시정지 메뉴를 여는 의미 명령이며 즉시 종료로 고정하지 않는다.
- 게임 규칙은 입력 장치 종류를 알지 못한다.

## 6. UI·표시 경계

```text
GAMEPLAY_VIEW_MODEL = SHARED
PLATFORM_UI_POLICY = SHARED_SEMANTIC_TREE_WITH_RESPONSIVE_VARIANTS
DUPLICATE_PC_ANDROID_GAMEPLAY_SCENE_TREES = FORBIDDEN
MINIMUM_TOUCH_TARGET_POLICY = REQUIRED_BEFORE_MOBILE_GATE
```

- 전투·룰렛·건설·상인 화면의 의미 구조와 ViewModel은 공유한다.
- PC/Android 전체 화면을 복제하지 않고 responsive container, density token, input hint, safe-area wrapper를 교체한다.
- PC는 16:9를 기준으로 하되 창 크기와 화면비 변경을 검증한다.
- Android는 wide·tall 화면비, cutout, gesture inset, 작은 화면을 검증한다.
- 현재 960×540 정수 배율 정책은 픽셀 아트 기준점으로 보존할 수 있지만, 모바일에서 글자·터치 대상이 지나치게 작아지는지 별도 Gate에서 검증한다.

## 7. 저장·수명주기 경계

```text
SAVE_SCHEMA = SHARED_VERSIONED_CANONICAL_SCHEMA
SAVE_MIGRATION = FORWARD_MIGRATION_WITH_ROLLBACK_GUARD
SAVE_WRITE = ATOMIC_TEMP_VALIDATE_REPLACE
SAVE_STORAGE_PATH = ADAPTER_OWNED
ANDROID_BACKGROUND_SAVE = REQUIRED
CLOUD_SAVE = OPTIONAL_SEPARATE_CAPABILITY
```

공용 저장 payload는 플랫폼과 무관한 `schema_version`, `content_version`, `run_state`, `meta_state`, `settings`, `determinism_manifest`를 가진다.

저장 순서:

1. 공용 코어가 immutable save snapshot을 생성한다.
2. schema validator가 필수 필드와 버전을 확인한다.
3. SaveAdapter가 임시 파일에 쓴다.
4. 다시 읽어 hash·schema를 검증한다.
5. 마지막 정상본을 보존한 뒤 원자 교체한다.

Android에서는 pause/background 진입 때 debounce된 checkpoint를 요청한다. 저장 완료 전 긴 작업을 시작하지 않으며, 앱 강제 종료에도 마지막 정상본을 유지한다. Steam/Google Play cloud save는 로컬 정본 위에 추가되는 capability이며 기본 저장 규칙을 대체하지 않는다.

## 8. 플랫폼 어댑터

### PC 어댑터

```text
PC_INPUT = KEYBOARD_MOUSE_GAMEPAD
PC_DISPLAY = WINDOW_FULLSCREEN_RESOLUTION
PC_STORAGE = DESKTOP_LOCAL_ATOMIC_SAVE
PC_STORE_PRIMARY = STEAM
STOVE = SEPARATE_SECONDARY_STORE_ADAPTER
```

- `PcInputAdapter`
- `PcDisplayAdapter`
- `DesktopSaveAdapter`
- `DesktopLifecycleAdapter`
- `PcPerformanceAdapter`
- `SteamStoreAdapter`
- 추후 별도 Gate의 `StoveStoreAdapter`

Steam과 STOVE를 하나의 조건문 파일에 섞지 않는다. 공용 `StoreAdapter` 계약을 각각 구현한다.

### Android 어댑터

```text
ANDROID_INPUT = TOUCH_BACK_GESTURE_VIRTUAL_KEYBOARD
ANDROID_DISPLAY = SAFE_AREA_ASPECT_DENSITY
ANDROID_LIFECYCLE = PAUSE_BACKGROUND_RESUME
ANDROID_PERFORMANCE = MEMORY_THERMAL_BATTERY_BUDGET
ANDROID_STORE_PRIMARY = GOOGLE_PLAY
```

- `AndroidInputAdapter`
- `AndroidDisplayAdapter`
- `AndroidSaveAdapter`
- `AndroidLifecycleAdapter`
- `AndroidPerformanceAdapter`
- `GooglePlayStoreAdapter`

Google Play 연결 실패·오프라인·로그아웃 상태에서도 싱글플레이 공용 코어가 시작 가능해야 한다.

## 9. 폴더 목표

```text
scripts/
  domain/                  # 규칙·상태·명령·이벤트·save DTO
  application/             # application, session driver, composition
  presentation/            # shared ViewModel and binders
  platform/
    contracts/
    pc/
    android/
    stores/
  core/                    # 기존 코어를 단계적으로 domain/application으로 분리
```

전면 이동을 한 번에 수행하지 않는다. 신규 경계부터 추가하고, 기존 서비스는 회귀 테스트를 유지하면서 단계적으로 이전한다.

## 10. 구현 순서

```text
PHASE_0 = BASELINE_AND_CHARACTERIZATION_TESTS
PHASE_1 = COMMAND_EVENT_AND_PLATFORM_CONTRACTS
PHASE_2 = GAME_SESSION_DECOUPLING
PHASE_3 = SHARED_VERSIONED_SAVE
PHASE_4 = RESPONSIVE_UI_AND_INPUT_ADAPTERS
PHASE_5 = PC_ADAPTERS_AND_REPRESENTATIVE_BUILD
PHASE_6 = ANDROID_LIFECYCLE_PERFORMANCE_AND_BUILD
PHASE_7 = STORE_ADAPTERS_AFTER_OFFLINE_CORE
```

각 Phase는 별도 제품 RED 테스트와 검토 가능한 PR로 진행한다. PC/Android 제품 코드를 한 번에 구현하는 대형 PR은 금지한다.

## 11. Gate 증거

### COMMON_PLATFORM_GATE

- 동일 seed·동일 command log가 PC/Android adapter harness에서 동일 state hash를 생성
- domain/core에서 금지 API 정적 검사
- 공용 save fixture의 round-trip과 migration
- shared ViewModel snapshot 계약
- 플랫폼 capability가 없어도 offline core 시작

### PC_RELEASE_GATE

- 키보드·마우스·게임패드 입력 parity
- 창·전체화면·해상도·focus 복귀
- 대표 Steam build와 설정·상점 설명 일치
- STOVE는 독립 adapter·build·상점 증거

### MOBILE_RELEASE_GATE

- touch/back/gesture UX
- safe area·화면비·글자·터치 대상
- pause/background/resume 저장 원자성
- 저메모리·발열·배터리 budget
- 대표 Android build와 Google Play 설정·개인정보·등급 일치

```text
GATE_TRANSFER_POLICY = PASS_DOES_NOT_TRANSFER
EXPORT_SUCCESS = NOT_EQUAL_TO_PLATFORM_READY
```

## 12. 금지 사항

```text
PLATFORM_SWITCH_STATEMENTS_SPREAD_ACROSS_DOMAIN = FORBIDDEN
STORE_SDK_OWNS_GAME_STATE = FORBIDDEN
PC_AND_ANDROID_SAVE_SCHEMA_FORK = FORBIDDEN
DUPLICATED_UI_TREES = FORBIDDEN
TOUCH_AS_MOUSE_FALSE_PARITY = FORBIDDEN
ANDROID_BACKGROUND_WITHOUT_CHECKPOINT = FORBIDDEN
EXPORT_PRESET_EQUALS_PLATFORM_READY_FALLACY = FORBIDDEN
STOVE_SCOPE_CREEP_IN_STEAM_ADAPTER = FORBIDDEN
```

## 13. 다음 제품 작업

이 설계 병합 뒤에도 제품 구현은 시작되지 않는다. 다음 단계는 Codex가 **Phase 0 기준선·characterization test 계획**을 작성하고 사용자 승인을 받은 뒤, 제품 RED 테스트부터 시작하는 것이다.
