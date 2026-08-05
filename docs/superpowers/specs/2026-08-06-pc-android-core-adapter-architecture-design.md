# OMENWARD PC·Android 공용 코어·어댑터 설계 명세

```yaml
status: APPROVED_DESIGN_NOT_IMPLEMENTED
decision_id: OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1
parent_decision: OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1
baseline_main: f5e4bcee7f8459fcfeb492f1ebc19ff932a352f0
product_code_authority: NONE
```

## 목적

Godot 프로토타입의 전투·경제·건물·룰렛 규칙을 PC와 Android에서 하나의 정본으로 사용하고, 입력·표시·저장·수명주기·성능·상점 차이를 교체 가능한 어댑터로 분리한다.

## 현행 근거

- Godot 4.7, main scene `res://scenes/main/main.tscn`.
- 960×540 viewport, viewport stretch, integer scale, GL Compatibility.
- `scripts/core`, `scripts/battle`, `scripts/buildings`, `scripts/roulette`에 결정론·상태 서비스가 존재한다.
- `GameSession`이 Node frame tick, Stage 시작, Scene lookup, HUD binding을 함께 담당한다.
- `export_presets.cfg`, 제품 SaveAdapter, LifecycleAdapter, StoreAdapter는 없다.
- 플랫폼 지원 범위만 승인됐으며 세 Gate는 모두 NOT_RUN이다.

## 설계 결정

### 1. 공용 코어

공용 코어는 deterministic domain state, commands, events, simulation, canonical save DTO, ViewModel snapshot을 소유한다. SceneTree, Node lifecycle, Input, DisplayServer, FileAccess, store SDK를 직접 참조하지 않는다.

### 2. 조립 계층

`GameApplication`, `SessionDriver`, `SceneBinder`, `PlatformBootstrap`을 분리한다. PlatformBootstrap만 실행 환경에 따라 adapter bundle을 선택한다.

### 3. 계약

- InputAdapter
- DisplayAdapter
- SaveAdapter
- LifecycleAdapter
- PerformanceAdapter
- StoreAdapter
- PlatformCapabilities

계약은 의미 기반이며 Godot 장치 이벤트와 SDK 타입을 domain에 노출하지 않는다.

### 4. 저장

한 개의 versioned canonical schema를 사용한다. 저장 경로는 adapter가 소유하고, temp-write → readback validation → atomic replace를 요구한다. Android pause/background checkpoint와 마지막 정상본 복구를 필수로 한다.

### 5. UI

게임 화면의 semantic tree와 ViewModel은 공유한다. PC/Android 전체 Scene 복제를 금지하고 responsive layout, density token, safe-area wrapper, input hint만 변형한다. touch-as-mouse만으로 모바일 대응을 완료할 수 없다.

### 6. 상점

Steam, STOVE, Google Play는 공용 StoreAdapter의 별도 구현이다. SDK 장애·로그아웃·오프라인이어도 로컬 싱글플레이 코어와 저장은 동작해야 한다.

## 구현 단계

1. 현행 characterization tests와 금지 API baseline.
2. platform contract와 command/event 모델.
3. GameSession 책임 분리.
4. canonical save schema와 atomic adapter.
5. shared ViewModel·responsive UI·입력 adapter.
6. PC representative build.
7. Android lifecycle·성능·representative build.
8. offline core 뒤 store adapters.

## 검증 요구사항

- 동일 seed·동일 command log → adapter harness 간 동일 state hash.
- domain/core 금지 API 정적 검사.
- save fixture round-trip·migration·손상 복구.
- PC keyboard/mouse/gamepad 의미 명령 parity.
- Android touch/back/background/resume 실제 장치 검증.
- safe area, 화면비, 글자, 터치 대상 검증.
- store capability가 없는 test harness에서 offline core 시작.
- COMMON/PC/MOBILE Gate 결과 독립.

## 비범위

- 이번 PR에서 제품 코드 리팩터링
- export preset 생성
- Steam·STOVE·Google Play SDK 설치
- 정확한 성능 budget·touch target 수치 확정
- 저장 데이터 마이그레이션 실행
- PC·Android 대표 빌드 또는 상점 제출

## 완료 조건

- 책임 원본·적대적 검토·실행 계획이 같은 Decision ID를 사용한다.
- 기존 플랫폼 책임 원본과 중앙 운영 문서가 본 설계를 라우팅한다.
- 계약 테스트가 경계·금지 사항·미구현 상태를 검증한다.
- Google Sheet가 NON_COUNTER 병렬 Decision으로 동기화되고 read-back 된다.
