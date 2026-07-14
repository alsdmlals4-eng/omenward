# Godot 프로젝트 구조

이 문서는 Roulettebound의 Godot 구조와 상태 소유 기준의 책임 원본이다. 실제 코드가 생기면 검증된 경로에 맞춰 갱신한다.

## 기술 기준

- 엔진: Godot
- 기본 언어: GDScript
- 정확한 minor 버전: Phase 0에서 확정
- 렌더링·카메라: 2D 또는 2.5D 방향 확정 전
- 기본 입력: PC 마우스·키보드 후보, 사용자 승인 필요

C#, GDExtension, 외부 ECS와 대형 애드온은 기본 선택이 아니다. Godot 기본 노드와 데이터 구조로 성능 목표를 달성하기 어렵다는 측정 근거가 있을 때 별도 Issue로 검토한다.

## 예정 폴더 구조

```text
project.godot
scenes/
  main/
  battle/
  buildings/
  units/
  roulette/
  waves/
  ui/
scripts/
  core/
  battle/
  buildings/
  units/
  roulette/
  waves/
  ui/
data/
resources/
tests/
assets/
docs/
```

Phase 0에서는 최소 구조만 생성한다. 실제 파일이 없는 도메인의 빈 폴더를 유지하기 위해 불필요한 placeholder를 대량 생성하지 않는다.

## Scene 책임

### Main

- 게임 진입과 최상위 화면 조합
- 전투 세션 생성·종료
- HUD와 전장 Scene 연결
- 세부 전투 규칙을 직접 계산하지 않음

### Battle

- 상·중·하 라인 공간
- 본진, 전방 건설 거점, 중앙 접전지 배치
- 전투 시간 진행과 전장 객체 조합
- 룰렛 확률이나 건물 데이터의 책임 원본이 되지 않음

### Unit

- 자신의 위치, 현재 체력, 이동·공격 상태
- 타기팅 결과에 따른 행동 수행
- 병종 기본 수치와 상성표를 코드에 중복 저장하지 않음

### Building

- 현재 체력, 티어, 건설·파괴 상태
- 생산 타이머와 공격 등 건물별 런타임 행동
- 건물 정의 데이터와 룰렛 토큰 계산을 직접 중복 소유하지 않음

### UI

- 받은 상태를 표시하고 사용자 의도를 Signal로 반환
- 금화 차감, 건설 확정, 유닛 생성 같은 게임 규칙을 직접 실행하지 않음

## AutoLoad 후보

AutoLoad는 반드시 필요한 공유 서비스만 사용한다. 이름은 Phase 0 또는 첫 기능 구현에서 확정한다.

### SessionState 후보

- 현재 금화와 식량 한도
- 대기 유닛 목록
- 한 게임 동안 적용되는 스킬북·장비 효과
- 현재 세션의 건물·토큰 구성 요약

전투 객체의 체력·위치와 UI 선택 상태는 저장하지 않는다.

### DataRegistry 후보

- 병종, 건물, 티어, 상성, 룰렛 보상, 웨이브 정의 로딩
- id 기반 조회
- 잘못된 id와 중복 정의 검증

데이터 규모가 작으면 첫 vertical slice에서는 AutoLoad 없이 명시적으로 주입하고, 여러 Scene에서 중복 로딩이 생길 때 도입한다.

### SceneRouter 후보

메뉴·전투·결과 등 여러 최상위 Scene 전환이 실제로 필요해질 때만 도입한다. 첫 테스트 맵 하나뿐이면 만들지 않는다.

## 데이터 구분

### Godot Resource / `.tres` 우선 후보

- 병종 정의
- 건물 정의와 티어별 수치
- 포탑 공격·사거리 수치
- 상성 배율
- 룰렛 토큰 정의

장점은 타입 지정, 에디터 편집과 직접 참조다.

### JSON 또는 CSV 후보

- 대량 적 웨이브 일정
- 외부 스프레드시트에서 관리할 밸런스 테이블
- 디자이너가 Godot 없이 수정해야 하는 데이터

초기 vertical slice에서 데이터 형식을 여러 개 섞지 않는다. 한 시스템의 책임 원본은 하나만 둔다.

## 주요 시스템 경계

```text
GameSession
 ├─ Resource/Economy
 ├─ BuildingRegistry
 ├─ RouletteService
 ├─ DeploymentService
 ├─ CaptureService
 └─ EnemyWaveService

BattleScene
 ├─ Lane ×3
 ├─ BuildNode
 ├─ CapturePoint
 ├─ Unit instances
 └─ Building instances

HUD
 ├─ Resource display
 ├─ Roulette panel
 ├─ Bench/deployment panel
 ├─ Lane status
 └─ Wave telegraph
```

서비스 이름과 구현 형태는 예시다. 첫 기능에서 실제 의존성을 확인하기 전에 범용 프레임워크로 만들지 않는다.

## Signal 원칙

- 자식 Scene은 부모나 서비스의 구체 경로를 깊게 탐색하지 않는다.
- 사용자 입력과 도메인 이벤트는 명시적 Signal 또는 좁은 메서드 계약으로 전달한다.
- 전역 이벤트 버스는 초기 기본값이 아니다. 이벤트 출처와 소비자가 직접 연결 가능하면 직접 Signal을 사용한다.
- Signal payload는 id와 필요한 최소 값만 전달하고, 거대한 Dictionary를 관행적으로 넘기지 않는다.

예시:

```gdscript
signal build_requested(node_id: StringName, building_id: StringName)
signal lane_deployment_requested(unit_instance_id: int, lane_id: StringName)
signal roulette_spin_requested(reference_row: int)
signal capture_owner_changed(lane_id: StringName, owner_id: int)
```

## 좌표와 라인

- 라인은 문자열 비교보다 enum 또는 `StringName` id를 사용한다.
- 이동 경로와 건설 노드는 전장 좌표와 라인 id를 분리해 가진다.
- 기본 포탑의 최대 사거리 원과 중앙 접전지의 최소 거리는 데이터와 테스트에서 비교 가능해야 한다.
- 맵을 확대하더라도 UI 픽셀과 월드 단위를 혼용하지 않는다.

## 다수 유닛 성능 원칙

- 첫 프로토타입에서 목표 최대 동시 유닛 수를 먼저 정한다.
- 모든 유닛이 매 프레임 전체 적 목록을 검색하지 않도록 공간·라인 단위 후보 목록을 사용한다.
- 물리 충돌이 핵심 재미가 아니라면 복잡한 rigid-body 군중 시뮬레이션을 기본 선택으로 삼지 않는다.
- 업데이트 주기를 분리한다: 이동·애니메이션은 프레임, 타깃 재탐색과 경제·점령 계산은 더 낮은 고정 주기를 검토한다.
- 최적화 전 실제 프로파일링과 재현 가능한 유닛 수 테스트를 만든다.

## UI 원칙

- HUD 배치는 `Control`과 `Container`로 구성한다.
- 룰렛 칸, 대기 유닛 카드, 건설 상품, 웨이브 행처럼 반복 단위만 재사용 Scene으로 분리한다.
- Theme에서 공통 폰트·패널·버튼·팀 상태를 관리한다.
- 3라인 전장 가독성을 해치지 않도록 슬롯 UI와 건설 UI가 월드 화면을 과도하게 가리지 않게 한다.
- 한국어 텍스트 확장과 16:9 해상도 변화를 검증한다.

## 보호 경로 후보

프로젝트 생성 후 다음 파일은 고위험 경로로 지정한다.

- `project.godot`
- 핵심 AutoLoad
- 병종·건물·상성·룰렛 확률의 책임 원본 데이터
- 세션 저장 코드가 생긴 이후의 저장 스키마

이 경로의 변경은 관련 호출 위치, 데이터 호환성, headless 결과와 실제 플레이 경로를 함께 검증한다.

## 기본 검증

Phase 0에서 정확한 명령을 README에 확정한다.

```bash
git diff --check
godot --headless --path . --editor --quit
```

기능 작업은 추가로 다음을 확인한다.

- 변경 데이터 로딩
- 변경 Scene 단독 실행
- 관련 시스템 경계 테스트
- 실제 메인 플레이 경로
- 기본 포탑 사거리와 접전지 거리 같은 프로젝트 불변 조건