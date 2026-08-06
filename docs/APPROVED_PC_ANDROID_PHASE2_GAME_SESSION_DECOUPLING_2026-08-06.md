# [승인] PC·Android Phase 2 GameSession 책임 분리

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PC-ANDROID-PHASE2-GAME-SESSION-DECOUPLING-V1
parent_architecture: OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1
phase1_decision: OMW-DEC-20260806-PC-ANDROID-PHASE1-CONTRACTS-V1
baseline_main: 32e4482119812c1da62bb909350d2f87087785b3
status: IMPLEMENTED_LOCAL_PASS_CANDIDATE
verification_mode: FREE_LOCAL_ONLY
product_behavior_change: NONE_INTENDED
phase3_shared_save: NOT_AUTHORIZED
```

## 1. 승인 결정

기존 `GameSession`의 상태·프레임 구동·Scene 탐색·조립 책임을 다음 네 구성 요소로 분리한다.

```text
GameApplication  = deterministic application state and stage orchestration
SessionDriver    = process delta and deferred stage start
SceneBinder      = Battlefield and StageHud binding
PlatformBootstrap = composition and idempotent recomposition
GameSession      = Scene compatibility facade only
```

기존 `GameSession` Scene 노드와 외부 API를 유지해 현재 StageSelect와 Main Scene의 행동을 바꾸지 않는다.

## 2. 구현된 경로

```text
scripts/application/game_application.gd
scripts/application/game_session.gd
scripts/application/game_session.gd.uid
scripts/application/session_driver.gd
scripts/application/platform_bootstrap.gd
scripts/presentation/scene_binder.gd
```

제거한 구형 경로:

```text
scripts/core/game_session.gd
scripts/core/game_session.gd.uid
```

Main Scene은 동일한 script UID `uid://pxcknk84fcxk`를 유지하면서 application facade 경로를 참조한다.

## 3. 호환 계약

다음 surface는 유지한다.

```text
NODE_NAME = GameSession
SIGNALS = bootstrap_ready, bootstrap_failed, stage_started
METHODS = start_stage, retry_stage
STATE_GETTERS = clock, registry, determinism, validator, progression, stage_run, current_stage_id
DEFAULT_STAGE = tutorial_stage
BATTLEFIELD_PATH = Battlefield
HUD_PATH = UI/StageHud
```

`StageSelect`와 gameplay service 파일은 수정하지 않는다.

## 4. 책임 규칙

### GameApplication

- `RefCounted`.
- registry·determinism·validator·progression·stage run 상태 소유.
- bootstrap catalog load와 validation.
- stage start·retry·advance.
- Node·SceneTree·input·display·file·store SDK 직접 참조 금지.

### SessionDriver

- `Node`.
- `_process(delta)`에서 application advance만 호출.
- 초기 stage를 deferred 호출.
- gameplay state와 Scene lookup 금지.

### SceneBinder

- `Node`.
- application의 `stage_started`를 한 번만 연결.
- host 부모에서 `Battlefield`, `UI/StageHud`만 조회.
- 두 대상은 독립적으로 존재 가능하며 `bind_run()`이 있을 때만 호출.

### PlatformBootstrap

- application을 생성하거나 주입받음.
- driver·binder를 host에 각각 정확히 하나만 구성.
- 같은 host 재조립 시 metadata의 유효 객체를 재사용.
- PC·Android adapter 선택은 아직 하지 않음.

### GameSession facade

- `_ready()`에서 조립·signal forwarding·bootstrap만 수행.
- `_process()`와 직접 Scene lookup 없음.
- 공개 상태와 start/retry를 application에 위임.

## 5. 정적 경계 변화

Phase 0의 정확한 legacy allowance 세 건을 모두 제거했다.

```text
DEFAULT_LEGACY_ALLOWLIST = ()
ALLOWED_LEGACY_FINDINGS = 0
UNAPPROVED_FINDINGS = 0
STALE_ALLOWANCES = 0
```

스캐너 규칙이나 검사 대상은 약화하지 않았다.

## 6. TDD 이력

```text
STRUCTURAL_RED = target files absent / old core file present / old Scene path / allowlist 3
GODOT_RED = five target preload paths absent
GREEN_EXTRACTION = GameApplication + SessionDriver + SceneBinder
GREEN_COMPOSITION = PlatformBootstrap + compatibility facade + Scene path migration
ADVERSARIAL_RED = duplicate composition children
ADVERSARIAL_FIX = metadata-backed idempotent composition
LOG_CLEANUP = has_meta before get_meta
```

세부 commit과 RED/Green 실행 결과는 PR 본문과 적대적 검토 문서에 기록한다.

## 7. 검증 상태

```text
GODOT_VERSION = 4.7.1.stable.official.a13da4feb
EDITOR_CLASS_SCAN = EXIT_0
PHASE2_BEHAVIOR_TEST = EXIT_0
BOOTSTRAP_IDEMPOTENCE_TEST = EXIT_0
PHASE1_EXACT_CONTRACT_REGRESSION = EXIT_0
PYTHON_PHASE2_AND_STATIC_TESTS = 9_PASS
STATIC_GUARD = ALLOWED_0 / UNAPPROVED_0 / STALE_0
PY_COMPILE = PASS
EXACT_SOURCE_BLOB_MATCH = PASS
```

검증은 connector에서 읽은 exact GitHub source와 무료 로컬 Godot·Python 격리 harness를 사용했다. 전체 private repository runtime·전체 Scene assembly·대표 build·export는 실행하지 않았다.

## 8. 명시적 비범위

```text
SHARED_SAVE_SCHEMA = NOT_STARTED
SAVE_ADAPTER_IMPLEMENTATION = NOT_STARTED
PC_INPUT_DISPLAY_ADAPTERS = NOT_STARTED
ANDROID_INPUT_LIFECYCLE_PERFORMANCE_ADAPTERS = NOT_STARTED
RESPONSIVE_UI = NOT_STARTED
STORE_SDK = NOT_STARTED
EXPORT_PRESETS = ABSENT
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
RELEASE_READY = FALSE
```

## 9. 다음 단계

다음 제품 단계는 별도 Decision과 RED 테스트를 가진 Phase 3 공용 versioned save다. 본 문서는 Phase 3 구현을 승인하지 않는다.

## 10. 관련 문서

- `docs/design/APPROVED_PC_ANDROID_CORE_ADAPTER_ARCHITECTURE_2026-08-06.md`
- `docs/superpowers/specs/2026-08-06-pc-android-phase2-game-session-decoupling-design.md`
- `docs/superpowers/plans/2026-08-06-pc-android-phase2-game-session-decoupling.md`
- `docs/reviews/ADVERSARIAL_PC_ANDROID_PHASE2_GAME_SESSION_REVIEW_2026-08-06.md`
