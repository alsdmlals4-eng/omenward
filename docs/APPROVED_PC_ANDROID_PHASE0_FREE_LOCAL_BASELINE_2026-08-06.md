# OMENWARD PC·Android Phase 0 무료 로컬 기준선

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PC-ANDROID-PHASE0-FREE-LOCAL-V1
parent_architecture_decision: OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1
baseline_architecture_head: 533eb18d04fd1f203a35e16ee2f8e6634014a3ff
phase_status: STATIC_GUARD_AND_CHARACTERIZATION_LOCAL_PASS
verification_mode: FREE_LOCAL_ONLY
github_actions: NOT_USED_BY_USER_CONSTRAINT
product_code_authority: PHASE0_TEST_INFRASTRUCTURE_ONLY
```

## 1. 승인 범위

사용자 지시에 따라 GitHub Actions와 유료 runner를 사용하지 않는다. 다음 무료 작업만 승인한다.

- GitHub 커넥터를 통한 명시적 브랜치·PR 작업
- Python 표준 라이브러리 `unittest`
- 저장소 내부 Python 정적 검사기
- 사용자 제공 또는 개발자 PC에 이미 설치된 Godot의 headless 실행
- GitHub·Google Sheet bounded read-back

다음은 이 Decision에서 승인하지 않는다.

- GitHub Actions workflow 추가·수정·재실행을 완료 증거로 사용
- 외부 유료 CI·빌드 서비스
- 제품 게임 코드·Scene·Resource·데이터 변경
- PC·Android 어댑터 구현
- export preset·SDK·상점 제출

## 2. TDD 및 무료 로컬 증거

```text
RED_COMMIT = a9b300be50a8344e53ac73cbf04bfe2707f0fd26
RED_COMMAND = python -m unittest tests.python.test_platform_boundary_static_guard -v
RED_RESULT = MODULE_NOT_FOUND / EXIT_1
GREEN_COMMAND = python -m unittest tests.python.test_platform_boundary_static_guard -v
GREEN_RESULT = 3_TESTS_PASS / EXIT_0
CLI_COMMAND = python tools/platform_boundary_guard.py --root .
CLI_RESULT = UNAPPROVED_0 / STALE_ALLOWANCES_0 / EXIT_0
PY_COMPILE = PASS
```

Python GREEN은 무료 로컬 재구성 환경에서 검사기의 동작과 정확한 허용 목록 정책을 검증한 결과다.

## 3. 정적 경계 검사

검사 규칙:

```text
NODE_BASE_CLASS
SCENE_TREE_TYPE
SCENE_TREE_LOOKUP
INPUT_SINGLETON
DISPLAY_SERVER
FILE_ACCESS
OS_FEATURE_SWITCH
STEAM_SDK
GOOGLE_PLAY_SDK
```

현재 `scripts/core`의 승인된 레거시 예외는 `game_session.gd`의 정확한 세 문장이다.

- `extends Node`
- `Battlefield` 조회
- `UI/StageHud` 조회

파일 전체나 토큰 전체를 허용하지 않는다. 경로·규칙·정확한 코드가 모두 일치해야 하며, 추가 호출과 낡은 허용 목록은 실패한다.

GitHub 코드 검색에서 현행 `scripts/core`의 `Input.`, `DisplayServer`, `FileAccess`, `OS.has_feature`, Steam, Google Play 직접 참조는 0건이었다. `extends Node`와 `get_node_or_null`은 `game_session.gd` 한 파일에서만 확인됐다.

## 4. Godot 특성화 기준선

`tests/headless/platform_core_characterization_test.gd`는 다음 현행 동작을 고정한다.

- 동일 StageManifest의 동일 JSON 직렬화
- regular stage 시작 골드 160·food cap 12
- 60초, controlled clash 1, stable outpost 1에서 골드 183
- 동일 3×3 board·source·seed의 룰렛 결과 동일성
- 전체 8 line 완료 시 Legendary 판정

사용자가 제공한 Linux 실행 파일로 무료 headless 검증을 수행했다.

```text
GODOT_VERSION = 4.7.1.stable.official.a13da4feb
EDITOR_CLASS_SCAN_COMMAND = Godot --headless --path <local-harness> --editor --quit
EDITOR_CLASS_SCAN_RESULT = EXIT_0
CHARACTERIZATION_COMMAND = Godot --headless --path <local-harness> --script tests/headless/platform_core_characterization_test.gd
CHARACTERIZATION_OUTPUT = Platform-neutral core characterization checks passed
GODOT_CHARACTERIZATION_RESULT = EXIT_0 / LOCAL_PASS
```

실행 전에 테스트 파일과 의존 스크립트 6개의 로컬 Git blob SHA를 PR #147 exact source blob SHA와 대조했으며 7개 모두 일치했다.

```text
stage_manifest.gd = d8a2812caa5e53e1339d7ac5d25a052447e57264
stage_economy.gd = e9003ec0bd52a0e5474a8be300357d0a8617e8b8
determinism_service.gd = 8ba056f4467416040a0b4e11013dafa9cda60e09
unit_spawn_definition.gd = 16ac39fa74c5417c3c051fa351fafd932351ad01
roulette_spin_result.gd = df4bb2d81391383efe306f9a2e1fc0a7ec1c44c8
roulette_service.gd = d52f02c56a6454220fbff042e1b751ea751c7bfb
platform_core_characterization_test.gd = 45558bdc73e2ec94a11bf21ac29422dfaaf0faaf
```

검증은 전체 비공개 저장소 checkout이 아니라 위의 exact 파일과 최소 프로젝트 설정을 재구성한 격리 harness에서 수행했다. 테스트와 무관한 autoload·editor plugin 설정은 포함하지 않았다. 따라서 이 증거는 특성화 테스트의 Godot 4.7.1 실행 성공을 증명하지만 전체 게임 프로젝트 실행·Scene 조립·export 성공을 증명하지 않는다.

일반 로컬 저장소 실행 명령:

```bash
godot --headless --path . --script tests/headless/platform_core_characterization_test.gd
```

## 5. Gate 판정

```text
PYTHON_STATIC_GUARD = LOCAL_3_PASS
GITHUB_CONNECTOR_CODE_SEARCH = PASS_FOR_QUERIED_TOKENS
GODOT_CHARACTERIZATION = LOCAL_PASS_ISOLATED_EXACT_SOURCE_HARNESS
FULL_PROJECT_RUNTIME = NOT_RUN
PRODUCT_RUNTIME = UNCHANGED
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
RELEASE_BLOCKED_UNVERIFIED
```

이 기준선은 이후 Phase 1에서 플랫폼 계약을 추가할 때 기존 공용 코어에 플랫폼 API가 새로 침투하는 것을 무료 로컬 검사로 차단한다. 제품 크로스플랫폼 구현 완료를 의미하지 않는다.
