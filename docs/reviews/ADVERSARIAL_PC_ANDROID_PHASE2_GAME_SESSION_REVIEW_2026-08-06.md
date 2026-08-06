# PC·Android Phase 2 GameSession 적대적 검토

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PC-ANDROID-PHASE2-GAME-SESSION-DECOUPLING-V1
baseline_main: 32e4482119812c1da62bb909350d2f87087785b3
review_scope: GAME_SESSION_DECOUPLING
verification_mode: FREE_LOCAL_ONLY
```

## 결론

`GameSession` 책임 분리는 승인 아키텍처와 일치한다. 기존 Scene 노드명·signal·메서드·읽기 속성을 보존하면서 상태·tick·Scene binding·composition을 분리했다. 적대적 검토 중 실제 결함 두 건과 테스트 결함 두 건을 발견해 각각 재현·수정했다.

```text
REVIEW_RESULT = ACCEPTABLE_FOR_PHASE2_MAIN
PRODUCT_BEHAVIOR_CHANGE = NONE_INTENDED
PHASE3_SAVE = NOT_AUTHORIZED
PLATFORM_READY = FALSE
RELEASE_READY = FALSE
```

## 확인한 책임 경계

- `GameApplication`: `RefCounted`, bootstrap·stage start/retry·advance·상태 소유.
- `SessionDriver`: `_process(delta)`와 deferred initial stage만 소유.
- `SceneBinder`: Battlefield·StageHud lookup과 `bind_run()`만 소유.
- `PlatformBootstrap`: application·driver·binder 조립과 재조립 재사용.
- `GameSession`: Scene 호환 facade와 signal/method/property 위임만 소유.
- `scripts/core/game_session.gd`: 제거.
- Phase 0 legacy allowlist: 0건.

## 실제로 발견·수정한 결함

### P2-AUD-001 — 중복 조립

**증상:** 같은 host에 `compose()`를 두 번 호출하면 driver와 binder가 두 개씩 생성됐다. 이중 tick과 이중 Scene binding으로 확대될 수 있었다.

**RED:** `tests/headless/platform_bootstrap_idempotence_test.gd`가 child 4개와 서로 다른 조립 객체를 확인하고 EXIT 1.

**수정:** host metadata에 driver·binder를 저장하고 유효한 기존 객체를 재구성해 재사용한다.

**결과:** child 수 2, 첫 번째와 두 번째 조립 객체 동일, EXIT 0.

### P2-AUD-002 — metadata 첫 조회 오류 로그

**증상:** `get_meta(key, null)`이 Godot 4.7.1에서 누락 key 오류 로그를 남기면서 테스트 자체는 EXIT 0이었다.

**수정:** `has_meta()` 확인 후에만 `get_meta()`를 호출한다.

**결과:** editor·행동·idempotence 테스트 모두 오류·경고 없이 EXIT 0.

## 테스트 자체에서 발견·수정한 결함

### P2-TEST-001 — lambda 지역 정수 캡처

GDScript lambda에서 지역 정수 카운터가 기대대로 갱신되지 않아 정상 signal을 실패로 판정했다. mutable Dictionary 카운터로 교체했다.

### P2-TEST-002 — detached Node 누수

facade fake bootstrapper가 의도적으로 비부착 driver·binder를 반환하면서 종료 시 orphan Node 경고가 발생했다. 테스트가 생성한 detached fixture를 명시적으로 해제했다.

## 추가 검토 결과

| 위험 | 판정 | 근거 |
|---|---|---|
| facade가 gameplay state를 다시 소유 | 차단 | 모든 공개 상태는 application getter 위임 |
| `GameSession._process()` 잔존 | 차단 | 구조 테스트 및 소스 검사 |
| Scene lookup의 application/core 누출 | 차단 | 승인 두 경로는 SceneBinder에만 존재 |
| 초기 stage 이중 시작 | 차단 | 성공 bootstrap 뒤 driver 한 번 호출 |
| bootstrap 실패 뒤 stage 시작 | 차단 | errors가 있으면 즉시 return |
| signal 중복 연결 | 차단 | facade와 binder 모두 `is_connected()` 검사 |
| 구형 Scene UID 손실 | 차단 | `uid://pxcknk84fcxk` 유지 |
| StageSelect API 파손 | 차단 | 노드명·start/retry·progression getter 유지; 파일 변경 없음 |
| Phase 2를 플랫폼 준비 완료로 오판 | 차단 | PC/Android adapter·save·build·Gate 모두 미실행 명시 |

## 검증 증거

```text
GODOT_VERSION = 4.7.1.stable.official.a13da4feb
EDITOR_CLASS_SCAN = EXIT_0
PHASE2_BEHAVIOR_TEST = EXIT_0 / GameSession decoupling checks passed
BOOTSTRAP_IDEMPOTENCE_TEST = EXIT_0 / PlatformBootstrap idempotence checks passed
PHASE1_EXACT_CONTRACT_REGRESSION = EXIT_0 / Platform contract checks passed
PYTHON_PHASE2_AND_STATIC_TESTS = 9_PASS
STATIC_GUARD = ALLOWED_0 / UNAPPROVED_0 / STALE_0
PY_COMPILE = PASS
ERROR_LOGS = 0
WARNING_LOGS = 0
```

Phase 2 신규 소스·테스트와 Phase 1 회귀 파일은 GitHub blob SHA와 로컬 실행 파일 SHA를 대조했다. 전체 private repository Scene 실행·대표 build·export는 이 증거에 포함하지 않는다.

## 남은 경계

```text
SHARED_VERSIONED_SAVE = NOT_STARTED
PC_ADAPTERS = NOT_STARTED
ANDROID_ADAPTERS = NOT_STARTED
RESPONSIVE_UI = NOT_STARTED
STORE_SDK = NOT_STARTED
FULL_PROJECT_RUNTIME = NOT_RUN
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
```
