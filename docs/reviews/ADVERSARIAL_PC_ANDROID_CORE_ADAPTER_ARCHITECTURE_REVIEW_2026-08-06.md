# OMENWARD PC·Android 공용 코어·어댑터 적대적 검토

```yaml
updated_at: 2026-08-06
decision_id: OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1
review_status: DESIGN_REVIEW_COMPLETE_IMPLEMENTATION_NOT_RUN
baseline_main: f5e4bcee7f8459fcfeb492f1ebc19ff932a352f0
product_code_authority: NONE
```

## 판정

현재 프로토타입은 전투·경제·룰렛의 결정론 서비스 기반이 있으므로 공용 코어로 발전할 수 있다. 그러나 플랫폼 기능이 아직 없다는 사실을 플랫폼 독립성이 증명됐다고 해석하면 안 된다. `GameSession`의 Scene 결합, 저장 계층 부재, export preset 부재, 모바일 lifecycle 부재를 먼저 경계화해야 한다.

## 위험 원장

### OMW-AUD-PLAT-001 — PLATFORM_API_LEAK_INTO_CORE

- 심각도: P0
- 공격: 입력·표시·파일·상점 API를 편의상 기존 core 서비스에서 직접 호출한다.
- 실패: 테스트 harness에서 코어를 분리할 수 없고 Android 대응 때 조건문이 전투·경제 코드로 확산된다.
- 차단: 금지 API 정적 검사와 adapter interface 주입. domain/core의 `Node`, `Input`, `DisplayServer`, `FileAccess`, SDK 직접 참조를 실패 처리한다.

### OMW-AUD-PLAT-002 — SCENE_TREE_COUPLED_SESSION

- 심각도: P0
- 공격: 현행 `GameSession`처럼 세션 진행, frame tick, 부모 Scene 탐색, HUD binding을 한 Node가 계속 소유한다.
- 실패: headless·deterministic 테스트가 어렵고 PC/Android Scene 차이가 규칙 차이로 번진다.
- 차단: `GameApplication`, `SessionDriver`, `SceneBinder`, `PlatformBootstrap`으로 책임을 분리한다.

### OMW-AUD-PLAT-003 — TOUCH_AS_MOUSE_FALSE_PARITY

- 심각도: P0
- 공격: PC 클릭이 되므로 터치를 마우스로 에뮬레이션해 모바일 입력 완료로 판정한다.
- 실패: drag·scroll·long press·back·다중 접촉·취소가 모호해지고 잘못된 배치가 발생한다.
- 차단: 의미 명령 기반 AndroidInputAdapter와 실제 장치 UX Gate를 요구한다.

### OMW-AUD-PLAT-004 — SAVE_SCHEMA_FORK

- 심각도: P0
- 공격: PC와 Android가 각자 편한 형태로 저장 파일을 만든다.
- 실패: 패치·클라우드·기기 이동·회귀 테스트에서 상태 정본이 분기된다.
- 차단: 하나의 versioned canonical schema, 공용 migration, 플랫폼별 storage adapter만 허용한다.

### OMW-AUD-PLAT-005 — ANDROID_LIFECYCLE_DATA_LOSS

- 심각도: P0
- 공격: PC 종료 저장만 구현하고 Android background·process kill을 일반 종료처럼 취급한다.
- 실패: Stage 진행·구매·룰렛 결과가 일부만 저장되거나 최근 진행이 소실된다.
- 차단: pause/background checkpoint, atomic temp-validate-replace, 마지막 정상본 유지, resume 복구 테스트를 요구한다.

### OMW-AUD-PLAT-006 — STORE_SDK_DOMAIN_OWNERSHIP

- 심각도: P0
- 공격: Steam 또는 Google Play 로그인 객체가 저장·업적·게임 진행의 정본을 소유한다.
- 실패: 오프라인·SDK 장애·STOVE 추가 시 게임 시작과 저장이 상점에 종속된다.
- 차단: offline core 우선, StoreAdapter는 capability와 동기화만 제공하고 로컬 정본을 대체하지 않는다.

### OMW-AUD-PLAT-007 — DUPLICATED_UI_DRIFT

- 심각도: P1
- 공격: PC Scene과 Android Scene을 통째로 복제해 각각 수정한다.
- 실패: 규칙 표시, 버튼 상태, 접근성, 버그 수정이 플랫폼마다 달라진다.
- 차단: shared semantic tree/ViewModel과 responsive variant를 사용한다. 플랫폼 전체 gameplay tree 복제를 금지한다.

### OMW-AUD-PLAT-008 — EXPORT_PRESET_EQUALS_PLATFORM_READY_FALLACY

- 심각도: P0
- 공격: Windows·Android export가 성공하면 플랫폼 대응 완료로 기록한다.
- 실패: 입력, safe area, lifecycle, 저장, 성능, 상점 설문 문제를 놓친다.
- 차단: export success를 build evidence 중 하나로만 취급하고 COMMON/PC/MOBILE Gate를 독립 판정한다.

### OMW-AUD-PLAT-009 — PLATFORM_SWITCH_SPRAWL

- 심각도: P1
- 공격: `if OS.has_feature(...)`가 여러 UI·게임 서비스에 흩어진다.
- 실패: 새 상점·기기·테스트 환경 추가 시 조합 폭발이 발생한다.
- 차단: PlatformBootstrap 한 곳에서 adapter 묶음을 선택한다.

### OMW-AUD-PLAT-010 — MOBILE_INTEGER_SCALE_USABILITY

- 심각도: P1
- 공격: 현행 960×540 integer scale을 모바일에도 그대로 적용하면 픽셀 정합성이 곧 UX 적합성이라고 본다.
- 실패: 작은 글자, 작은 터치 대상, tall 화면의 빈 공간 또는 잘림이 발생한다.
- 차단: logical viewport는 유지 가능하되 UI density·safe area·touch target을 MOBILE Gate에서 별도 검증한다.

### OMW-AUD-PLAT-011 — GAME_SESSION_DELTA_NONDETERMINISM

- 심각도: P1
- 공격: device frame delta를 그대로 simulation에 전달하고 플랫폼별 frame pacing 차이를 무시한다.
- 실패: 같은 seed·명령으로 PC와 Android 결과 hash가 달라질 수 있다.
- 차단: fixed-step 또는 명시적 simulation tick 정책을 Phase 0 characterization으로 측정하고 결정한다. 자동으로 수치를 확정하지 않는다.

### OMW-AUD-PLAT-012 — STOVE_SCOPE_CREEP

- 심각도: P1
- 공격: Steam 어댑터에 STOVE 조건을 추가해 두 상점을 한 구현으로 관리한다.
- 실패: SDK 요구사항·빌드·설문 차이가 뒤섞여 회귀 원인을 분리할 수 없다.
- 차단: 공용 StoreAdapter 계약 아래 SteamStoreAdapter와 StoveStoreAdapter를 분리하고 STOVE Gate 전 구현 우선순위를 부여하지 않는다.

## 적대적 시나리오

1. Google Play 로그인이 실패한 Android 기기에서도 새 로컬 게임이 시작되고 저장되는가.
2. 앱이 룰렛 결과 직후 background로 이동하고 process kill되어도 골드 차감과 보상이 원자적으로 복구되는가.
3. 동일 seed와 command log를 PC harness와 Android harness에 넣었을 때 state hash가 같은가.
4. PC mouse drag와 Android touch drag가 같은 `MoveRouletteSlotCommand`를 만드는가.
5. Android back을 누르면 현재 overlay만 닫히며 무조건 앱이 종료되지 않는가.
6. Steam cloud 데이터가 손상됐을 때 로컬 마지막 정상본을 덮어쓰지 않는가.
7. 20:9 cutout 화면에서 중요한 HUD가 safe area 밖으로 나가지 않는가.
8. 저메모리 신호 뒤 품질 저하가 게임 규칙·RNG·보상에 영향을 주지 않는가.
9. Steam adapter를 제거한 test harness에서도 공용 코어 계약이 실행되는가.
10. STOVE 구현이 없어도 PC core와 Steam 대표 build가 영향을 받지 않는가.

## 승인·차단 경계

```text
DESIGN_REVIEW = COMPLETE
PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED
DATA_MIGRATION = NOT_AUTHORIZED
EXPORT_PRESETS = NOT_CREATED
REPRESENTATIVE_PC_BUILD = NOT_RUN
REPRESENTATIVE_ANDROID_BUILD = NOT_RUN
RUNTIME_QA = NOT_RUN
HUMAN_QA = NOT_RUN
```

이 검토가 통과시킨 것은 구조 방향뿐이다. 제품 코드, export preset, SDK, 데이터 마이그레이션, 실제 빌드가 완료됐다는 의미가 아니다.
