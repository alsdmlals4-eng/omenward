# PC·Android Phase 0 Free Local Baseline Implementation Plan

> **For agentic workers:** Execute only with repository-local Python, a user-provided or already-installed local Godot executable, GitHub connector reads/writes, and bounded Google Sheet reads/writes. Do not add, edit, or require GitHub Actions for this Decision.

**Goal:** 플랫폼 공용 코어에 새 플랫폼 API가 침투하는 것을 무료 로컬 정적 검사로 차단하고, 현행 결정론 동작을 Godot headless 특성화 테스트로 고정한다.

**Architecture:** Python 표준 라이브러리 검사기가 `scripts/core`와 이후의 `scripts/domain`을 스캔한다. 현행 `GameSession`의 정확한 세 문장만 레거시 허용하며 파일·토큰 전체 허용은 금지한다. Godot 테스트는 제품 코드를 바꾸지 않고 StageManifest·StageEconomy·RouletteService의 현재 동작을 기록한다.

**Tech Stack:** Python 3.11+ standard library, `unittest`, Godot 4.7 headless, GitHub PR, Google Sheet bounded read-back.

## Global Constraints

- Decision ID: `OMW-DEC-20260806-PC-ANDROID-PHASE0-FREE-LOCAL-V1`
- Parent: `OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1`
- GitHub Actions: `NOT_USED_BY_USER_CONSTRAINT`
- External paid CI/build service: `FORBIDDEN`
- Product scripts, Scene, Resource, data, export preset, SDK: `UNCHANGED`
- Python GREEN does not imply Godot GREEN or COMMON_PLATFORM_GATE PASS.
- Godot characterization GREEN does not imply full project runtime or export GREEN.
- Every PASS claim requires a fresh local command result and exit code 0.

---

### Task 1: Static Guard RED

**Files:**
- Create: `tests/python/test_platform_boundary_static_guard.py`

- [x] Write tests that import the missing scanner, detect real code, ignore comments and strings, enforce exact allowances, and scan the repository boundary.
- [x] Run `python -m unittest tests.python.test_platform_boundary_static_guard -v`.
- [x] Record expected RED: `ModuleNotFoundError`, exit 1.
- [x] Commit before scanner implementation: `a9b300be50a8344e53ac73cbf04bfe2707f0fd26`.

### Task 2: Minimal Python Scanner GREEN

**Files:**
- Create: `tools/__init__.py`
- Create: `tools/platform_boundary_guard.py`

- [x] Detect `Node`, `SceneTree`, node lookup, `Input`, `DisplayServer`, `FileAccess`, `OS.has_feature`, Steam, and Google Play references.
- [x] Ignore comments and string literals.
- [x] Match allowances by repository path + rule ID + normalized exact code.
- [x] Fail on new unapproved findings and stale allowances.
- [x] Run unit tests: 3 tests PASS, exit 0.
- [x] Run CLI: unapproved 0, stale allowances 0, exit 0.
- [x] Run `python -m py_compile` on scanner and test.

### Task 3: Repository Baseline Cross-Check

**Evidence:**
- GitHub code search under `scripts/core`
- Exact `scripts/core/game_session.gd` connector read

- [x] Confirm `Input.`, `DisplayServer`, `FileAccess`, `OS.has_feature`, Steam, and Google Play direct references return zero queried matches.
- [x] Confirm `extends Node` occurs only in `game_session.gd`.
- [x] Confirm `get_node_or_null` occurs only in `game_session.gd`.
- [x] Preserve exactly three legacy allowances: Node host, Battlefield lookup, StageHud lookup.

### Task 4: Godot Characterization Test

**Files:**
- Create: `tests/headless/platform_core_characterization_test.gd`

- [x] Author deterministic StageManifest serialization fixture.
- [x] Author StageEconomy 160/12 → 183-after-60-seconds fixture.
- [x] Author deterministic full-board RouletteService fixture.
- [x] Run with user-provided Godot 4.7.1 locally.
- [x] Verify editor class scan exit 0.
- [x] Verify characterization test exit 0 and expected success output.
- [x] Verify the test file and six dependency Git blob SHAs match PR #147 exact source blobs.

Run:

```bash
godot --headless --path . --script tests/headless/platform_core_characterization_test.gd
```

Recorded evidence:

```text
GODOT_VERSION = 4.7.1.stable.official.a13da4feb
EDITOR_CLASS_SCAN = EXIT_0
CHARACTERIZATION_OUTPUT = Platform-neutral core characterization checks passed
GODOT_CHARACTERIZATION = EXIT_0 / LOCAL_PASS_ISOLATED_EXACT_SOURCE_HARNESS
```

Boundary: the assistant reconstructed the exact test and dependency source files in a minimal local harness, not a full private-repository checkout. Unrelated autoload and editor plugin settings were omitted. Full project runtime, Scene assembly, build, and export remain `NOT_RUN`.

### Task 5: Free-Only Documentation and Sync

**Files:**
- Create: `scripts/platform/README.md`
- Create: `docs/APPROVED_PC_ANDROID_PHASE0_FREE_LOCAL_BASELINE_2026-08-06.md`
- Preserve: product implementation status and all product paths unchanged
- Sync: Google Sheet with the same Decision ID

- [x] Document free local commands and honest Gate semantics.
- [x] Record RED/GREEN and Godot execution evidence.
- [x] Open stacked Draft PR #147 against the PR #146 architecture branch.
- [x] Write exact head and bounded read-back status to Sheet.
- [x] Verify changed files, mergeability, review threads, comments, and reviews.

## Completion Boundary

```text
PYTHON_STATIC_GUARD = LOCAL_3_PASS
GODOT_CHARACTERIZATION = LOCAL_PASS_ISOLATED_EXACT_SOURCE_HARNESS
FULL_PROJECT_RUNTIME = NOT_RUN
PRODUCT_RUNTIME = UNCHANGED
PHASE_1_IMPLEMENTATION = NOT_AUTHORIZED
COMMON_PLATFORM_GATE = NOT_RUN
```

Phase 0 static guard and isolated exact-source characterization evidence may be reviewed without GitHub Actions. This does not authorize Phase 1 or represent a full project/runtime/export verification.
