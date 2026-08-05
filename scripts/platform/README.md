# OMENWARD Platform Boundary — Free Local Baseline and Phase 1 Contracts

```yaml
phase0_decision: OMW-DEC-20260806-PC-ANDROID-PHASE0-FREE-LOCAL-V1
phase1_decision: OMW-DEC-20260806-PC-ANDROID-PHASE1-CONTRACTS-V1
parent_architecture_decision: OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1
verification_mode: FREE_LOCAL_ONLY
github_actions: NOT_USED
```

이 디렉터리는 공용 코어 경계를 보호하고 플랫폼별 구현이 따라야 할 계약을 정의한다. GitHub Actions 또는 유료 runner 없이 개발자 PC와 무료 로컬 도구에서 직접 검증한다.

## 무료 로컬 명령

```bash
python -m unittest tests.python.test_platform_boundary_static_guard -v
python tools/platform_boundary_guard.py --root .
godot --headless --path . --editor --quit
godot --headless --path . --script tests/headless/platform_core_characterization_test.gd
godot --headless --path . --script tests/headless/platform_contracts_test.gd
```

## Phase 0 정적 경계

검사 대상은 `scripts/core/**/*.gd`와 `scripts/domain/**/*.gd`다. 다음 직접 참조를 차단한다.

- `Node` 기반 공용 코어 클래스
- SceneTree와 노드 탐색
- `Input`, `DisplayServer`, `FileAccess`
- `OS.has_feature()`
- Steam·Google Play SDK

현재 레거시 허용은 `scripts/core/game_session.gd`의 정확한 세 문장뿐이다. 경로·규칙·정확한 코드가 모두 일치해야 하며 추가 호출과 낡은 허용 목록은 실패한다.

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

## 판정 규칙

```text
PYTHON_STATIC_GUARD_PASS != GODOT_CONTRACT_PASS
GODOT_CONTRACT_PASS != FULL_PROJECT_RUNTIME_PASS
PHASE1_CONTRACT_PASS != COMMON_PLATFORM_GATE_PASS
EXPORT_SUCCESS != PLATFORM_READY
```

Phase 1은 GameSession 분리, 저장 스키마, PC·Android 어댑터, SDK, build 또는 release Gate를 구현하지 않는다.
