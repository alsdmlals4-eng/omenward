# OMENWARD Platform Boundary — Free Local Baseline through Phase 2

```yaml
phase0_decision: OMW-DEC-20260806-PC-ANDROID-PHASE0-FREE-LOCAL-V1
phase1_decision: OMW-DEC-20260806-PC-ANDROID-PHASE1-CONTRACTS-V1
phase2_decision: OMW-DEC-20260806-PC-ANDROID-PHASE2-GAME-SESSION-DECOUPLING-V1
parent_architecture_decision: OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1
verification_mode: FREE_LOCAL_ONLY
github_actions: NOT_USED
```

이 디렉터리는 공용 코어 경계를 보호하고 플랫폼별 구현이 따라야 할 계약을 정의한다. GitHub Actions 또는 유료 runner 없이 개발자 PC와 무료 로컬 도구에서 직접 검증한다.

## 무료 로컬 명령

```bash
python -m unittest \
  tests.python.test_game_session_decoupling_contract \
  tests.python.test_platform_boundary_static_guard -v
python tools/platform_boundary_guard.py --root .
godot --headless --path . --editor --quit
godot --headless --path . --script tests/headless/platform_core_characterization_test.gd
godot --headless --path . --script tests/headless/platform_contracts_test.gd
godot --headless --path . --script tests/headless/game_session_decoupling_test.gd
godot --headless --path . --script tests/headless/platform_bootstrap_idempotence_test.gd
```

## Phase 0 정적 경계

검사 대상은 `scripts/core/**/*.gd`와 `scripts/domain/**/*.gd`다. 다음 직접 참조를 차단한다.

- `Node` 기반 공용 코어 클래스
- SceneTree와 노드 탐색
- `Input`, `DisplayServer`, `FileAccess`
- `OS.has_feature()`
- Steam·Google Play SDK

Phase 2에서 구형 `scripts/core/game_session.gd`를 제거했으므로 현재 legacy allowance는 0건이다. 새 위반과 낡은 allowlist 항목은 모두 실패한다.

## Phase 1 계약 구조

```text
scripts/domain/commands/game_command.gd
scripts/domain/events/game_event.gd
scripts/platform/contracts/input_adapter.gd
scripts/platform/contracts/display_adapter.gd
scripts/platform/contracts/save_adapter.gd
scripts/platform/contracts/lifecycle_adapter.gd
scripts/platform/contracts/performance_adapter.gd
scripts/platform/contracts/store_adapter.gd
scripts/platform/contracts/platform_capabilities.gd
```

명령과 이벤트는 의미 ID와 플랫폼 중립 payload만 보존한다. 생성자 입력·getter·dictionary 변환은 서로 alias되지 않으며, Object 계열과 순환 컨테이너는 invalid다.

계약 base class는 실제 플랫폼 동작을 하지 않는다.

- Input: 빈 command 목록, unknown device.
- Display·Save·Performance: `not_implemented` 실패 결과.
- Lifecycle: `lifecycle_event` signal 선언.
- Store: unavailable, capability 없음.
- PlatformCapabilities: 생성 시 제공한 capability의 읽기 전용 snapshot.

## Phase 2 조립 구조

```text
scripts/application/game_application.gd
scripts/application/game_session.gd
scripts/application/session_driver.gd
scripts/application/platform_bootstrap.gd
scripts/presentation/scene_binder.gd
```

- `GameApplication`: platform-neutral 상태·bootstrap·stage start/retry·advance.
- `SessionDriver`: `_process(delta)`와 deferred stage start.
- `SceneBinder`: Battlefield·StageHud lookup과 run binding.
- `PlatformBootstrap`: driver·binder를 host당 정확히 하나 구성하고 재조립 시 재사용.
- `GameSession`: 기존 Scene API를 보존하는 thin facade.

Main Scene은 기존 UID를 유지하며 `res://scripts/application/game_session.gd`를 사용한다.

## 판정 규칙

```text
PYTHON_STATIC_GUARD_PASS != GODOT_CONTRACT_PASS
GODOT_CONTRACT_PASS != FULL_PROJECT_RUNTIME_PASS
PHASE2_SESSION_PASS != COMMON_PLATFORM_GATE_PASS
EXPORT_SUCCESS != PLATFORM_READY
```

Phase 2는 GameSession 책임만 분리한다. 공용 save schema, PC·Android adapter 구현, 반응형 UI, SDK, build 또는 release Gate는 구현하지 않는다.
