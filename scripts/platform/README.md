# OMENWARD Platform Boundary — Free Local Phase 0

```yaml
decision_id: OMW-DEC-20260806-PC-ANDROID-PHASE0-FREE-LOCAL-V1
parent_architecture_decision: OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1
verification_mode: FREE_LOCAL_ONLY
github_actions: NOT_USED
product_behavior_change: NONE
```

이 디렉터리는 PC·Android 구현 자체가 아니라 공용 코어 경계를 보호하는 Phase 0 기준선이다. GitHub Actions 또는 유료 runner 없이 개발자 PC와 무료 로컬 도구에서 직접 실행한다.

## 무료 로컬 명령

Python 3.11 이상:

```bash
python -m unittest tests.python.test_platform_boundary_static_guard -v
python tools/platform_boundary_guard.py --root .
```

Godot 4.7이 설치된 환경:

```bash
godot --headless --path . --script tests/headless/platform_core_characterization_test.gd
godot --headless --path . --script tests/headless/phase_0_contract_test.gd
godot --headless --path . --script tests/headless/economy_roulette_test.gd
```

Windows에서 실행 파일명이 `godot4`라면 명령의 `godot`만 `godot4`로 바꾼다.

## 확인된 무료 실행 증거

사용자 제공 Godot Linux 실행 파일을 사용해 다음 Phase 0 특성화 테스트를 무료로 실행했다.

```text
GODOT_VERSION = 4.7.1.stable.official.a13da4feb
EDITOR_CLASS_SCAN = EXIT_0
CHARACTERIZATION_OUTPUT = Platform-neutral core characterization checks passed
CHARACTERIZATION_RESULT = EXIT_0
```

테스트 파일과 StageManifest·StageEconomy·DeterminismService·UnitSpawnDefinition·RouletteSpinResult·RouletteService의 Git blob SHA는 PR #147 exact source와 모두 일치했다. 실행은 관련 exact 파일만 포함한 최소 격리 harness에서 수행했으므로 다음 판정을 사용한다.

```text
GODOT_CHARACTERIZATION = LOCAL_PASS_ISOLATED_EXACT_SOURCE_HARNESS
FULL_PROJECT_RUNTIME = NOT_RUN
```

## 정적 경계

검사 대상:

- `scripts/core/**/*.gd`
- 이후 생성되는 `scripts/domain/**/*.gd`

금지 대상:

- `Node` 기반 공용 코어 클래스
- `SceneTree`와 노드 탐색
- `Input` singleton
- `DisplayServer`
- `FileAccess`
- `OS.has_feature()` 분기
- Steam·Google Play 직접 참조

현재 레거시 허용은 `scripts/core/game_session.gd`의 정확한 3개 문장뿐이다.

1. `extends Node`
2. `Battlefield` 노드 조회
3. `UI/StageHud` 노드 조회

허용 목록은 파일 단위나 토큰 단위가 아니라 **경로+규칙+정확한 코드 문장**으로 일치한다. 같은 파일에 동일 API 호출을 하나 더 추가하면 실패한다. 기존 문장이 제거되거나 변경되어 허용 목록이 낡아도 실패한다.

## 판정 규칙

```text
PYTHON_STATIC_GUARD_PASS != GODOT_HEADLESS_PASS
GODOT_CHARACTERIZATION_PASS != FULL_PROJECT_RUNTIME_PASS
GODOT_HEADLESS_PASS != COMMON_PLATFORM_GATE_PASS
EXPORT_SUCCESS != PLATFORM_READY
```

Python 검사 통과는 정적 경계만 증명한다. 특성화 테스트 통과는 해당 exact-source fixture가 Godot 4.7.1에서 실행된 사실만 증명한다. Phase 0은 제품 코드·Scene·저장·입력·상점 SDK를 변경하거나 승인하지 않는다.
