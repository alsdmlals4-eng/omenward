# OMENWARD Godot 프로젝트 구조

- 상태: **기술 기준선·C1 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN**
- 갱신일: 2026-07-22
- 상위 기준: `docs/HANDOFF_CONTEXT.md`, `docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`

이 문서는 오멘워드의 Godot 구조, 상태 소유와 데이터 경계의 책임 원본이다. Phase 0의 실제 경로와 headless 명령은 `docs/PHASE_0_VALIDATION.md`에서 검증한다.

## 1. 기술 기준

- 엔진: Godot 4.7.1 Standard x86_64.
- 기본 언어: GDScript.
- renderer: Compatibility.
- 플랫폼: Windows PC, 마우스·키보드.
- 기준 출력: 1920×1080.
- 내부 논리 해상도: 960×540, viewport/keep/integer scaling.
- 카메라: 2D 픽셀 Camera2D 후보.

C#, GDExtension, 외부 ECS와 대형 애드온은 기본 선택이 아니다. Godot 기본 노드와 데이터 구조로 성능 목표를 달성하기 어렵다는 측정 근거가 있을 때 별도 승인으로 검토한다.

## 2. 현재 폴더 구조

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
resources/
  units/
  buildings/
  battlefields/
  roulette/
  waves/
  presentation/
data/
tests/
assets/
  units/
  buildings/
  environments/
  ui/
  audio/
docs/
```

- Phase 0에서는 실제 필요한 최소 폴더만 만든다.
- 빈 도메인을 표현하기 위한 placeholder를 대량 생성하지 않는다.
- 정확한 경로는 Plan Mode 제안서와 구현 결과를 기준으로 갱신한다.

## 3. Scene 책임

### Main

- 게임 진입과 최상위 화면 조합.
- 전투 세션 생성·종료.
- HUD, 전장, 결과 화면 연결.
- 세부 전투·경제 규칙을 직접 계산하지 않는다.

### Battle

- 상·중·하 라인과 전장 객체 조합.
- 본진, 성문, 중간거점, 중앙 접전지, 건설 노드, 우회 출입구 배치.
- 전투 시간과 월드 이벤트 진행.
- 병종·건물·룰렛 데이터의 책임 원본이 되지 않는다.

### Unit

Unit Scene은 아군용과 적군용으로 복제하지 않는다.

- 하나의 공용 Unit Scene 후보를 사용한다.
- `UnitArchetypeProfile`, Tier, Rank와 Visual Set을 주입받는다.
- 자신의 현재 체력, 위치, 라인, 상태, 타깃과 상태이상을 소유한다.
- `owner_team_id`로 적대·점령 관계를 결정한다.
- `visual_faction_id`로 스프라이트·초상화·아이콘을 결정한다.
- 병종 기본 수치, 스킬과 애니메이션 타이밍을 코드에 중복 저장하지 않는다.

### Building

- 현재 체력, Tier, 건설·활성·비활성·업그레이드·폐허 상태.
- 생산 타이머, 수입과 공격 같은 런타임 행동.
- BuildingProfile과 룰렛 토큰 규칙을 중복 소유하지 않는다.
- 중간거점 소유권 변화에 따른 사용 가능 상태를 반영한다.

### UI

- 받은 상태를 표시하고 사용자 의도를 Signal로 반환한다.
- 금화 차감, 건설 확정, 유닛 생성, 점령 판정을 직접 실행하지 않는다.
- 성문·거점·접전지 정보는 실제 월드 위치에 연결한다.
- 미니맵은 만들지 않는다.

## 4. 핵심 데이터 책임

### UnitArchetypeProfile

전투 규칙 기준 병종 원본이며 정확히 공용 10개를 사용한다.

```text
archetype_id
role_tags
movement_layer
food_cost
base_stats
attack_profile_id
passive_ids
skill_ids
targeting_profile_id
capture_power
structure_damage_tags
animation_contract_id
threat_cost
```

- `faction` 필드를 넣어 별도 아군·적군 데이터를 만들지 않는다.
- 같은 archetype·Tier·Rank는 진영과 무관하게 같은 전투 결과를 낸다.

### TierProfile

- 생산시설 성장과 병종 전문화.
- 패시브 강화와 추가 패시브.
- 생산시간·식량·전투 배율 후보.

### RankProfile

```text
rank_id
hp_multiplier
damage_multiplier
threat_multiplier
skill_unlock_count
visual_grade_id
```

- 일반·엘리트·영웅·전설 공용.
- 적 신화는 일반 Rank가 아니라 보스 패키지다.

### FactionVisualProfile

```text
visual_faction_id
archetype_id
sprite_atlas_id
portrait_id
icon_id
palette_or_material_id
pivot_profile_id
```

- 아군·적군 이미지 차이를 소유한다.
- 능력치, 타기팅, 공격 주기와 스킬을 변경하지 않는다.
- 첫 PoC에서는 VFX·Audio override를 두지 않는 것을 기본으로 한다.

### AnimationContract

```text
animation_contract_id
state_id
frame_count
playback_duration_or_fps
loop
impact_frame
projectile_spawn_frame
cancel_window
recovery_duration
vfx_event_ids
audio_event_ids
camera_impulse_id
```

- 같은 archetype의 아군·적군 이미지 시트가 공유한다.
- 상태, 프레임 수, 배열, 피벗과 이벤트 프레임이 일치해야 한다.
- 공격 판정과 애니메이션 표현을 동기화하지만 피해량·범위 원본이 되지 않는다.

### UnitInstance

```text
instance_id
archetype_id
owner_team_id
visual_faction_id
tier
rank
current_hp
lane_id
runtime_state
current_target_id
status_effects
```

런타임 상태만 소유하며 공용 프로필을 복사해 변경하지 않는다.

### StageManifest

- 시드와 스테이지 설정.
- 공세 시계와 징조.
- 공용 `archetype_id`, Tier, Rank, 수량, 라인, 출격 시간.
- owner team과 visual faction.
- 생산시설 연결과 보스 패키지.

일반 웨이브 항목에 적군 전용 스탯·스킬 필드를 넣지 않는다.

### BattlefieldProfile

- 3라인 토폴로지.
- 본진·성문·중간거점·접전지 ID와 좌표.
- 전방 2·후방 1 건설 노드.
- 암살자 우회 입구·도착 영역과 시간.
- 도로 폭, 이동 포인트, 포탑 거리 검증 값.

### BuildingProfile

- 비용, 시간, 체력, Tier, 생산, 토큰, 수입, 사거리, 업그레이드.
- 거점 소유권 요구와 상태별 작동 조건.

### BossBehaviorPackage / BossPhaseProfile

- 공용 base archetype 위에 보스 패턴과 페이즈를 추가한다.
- 일반 적군 데이터 복사본으로 만들지 않는다.

## 5. 데이터 형식 후보

### Godot Resource / `.tres` 우선

- UnitArchetypeProfile.
- TierProfile과 RankProfile.
- FactionVisualProfile.
- AnimationContract.
- BuildingProfile.
- BattlefieldProfile.
- 공격·스킬·패시브·타기팅.

장점은 타입 지정, 에디터 검증과 직접 참조다.

### JSON 또는 CSV 후보

- 대량 웨이브 일정.
- 외부 표 계산과 대량 밸런스 테이블.
- Godot 없이 편집할 필요가 있는 데이터.

첫 수직 슬라이스에서 한 시스템의 원본 형식을 여러 개로 섞지 않는다. 정확한 경계는 Plan Mode에서 비교한다.

## 6. 주요 시스템 경계 후보

```text
GameSession
 ├─ CombatClock
 ├─ EconomyService
 ├─ BuildingRegistry
 ├─ RouletteService
 ├─ DeploymentService
 ├─ CaptureService
 ├─ WaveService
 └─ VictoryService

Data access
 ├─ UnitArchetypeRegistry
 ├─ PresentationRegistry
 ├─ BuildingRegistryData
 ├─ BattlefieldData
 └─ StageManifestLoader

BattleScene
 ├─ Lane ×3
 ├─ Gate ×6
 ├─ MidStrongpoint ×6
 ├─ ClashPoint ×3
 ├─ BuildNode
 ├─ Unit instances
 └─ Building instances

HUD
 ├─ Resource display
 ├─ Roulette panel
 ├─ Bench/deployment panel
 ├─ World objective status
 ├─ Wave telegraph
 └─ Bellu guide
```

이름과 구현 형태는 후보다. 실제 의존성을 보기 전에 범용 프레임워크로 확대하지 않는다.

## 7. AutoLoad 후보

### SessionState

- 현재 금화와 식량.
- 대기 유닛 목록.
- 스테이지 전체의 건물·토큰 구성 요약.
- 스테이지 seed와 진행 메타데이터.

전투 객체의 현재 HP·위치와 UI 선택 상태를 저장하지 않는다.

### DataRegistry

- 공용 archetype, Tier, Rank, Visual, Animation, Building, Stage 데이터 로딩.
- ID 기반 조회.
- 중복 ID와 누락 참조 검증.

데이터가 작고 한 Scene에서만 사용된다면 첫 단계에서 명시적 주입을 우선하고 중복 로딩이 확인될 때 AutoLoad를 도입한다.

### SceneRouter

메뉴·전투·결과 등 여러 최상위 Scene 전환이 실제로 생길 때만 도입한다.

## 8. 시간과 결정론

세 시간축을 분리한다.

```text
real_time
active_combat_time
ui_planning_time
```

- 웨이브, 건설, 생산, 수입, 쿨다운과 우회 이동은 active_combat_time을 사용한다.
- 일시정지 중 UI와 계획 입력은 가능하지만 active_combat_time은 증가하지 않는다.
- 시드, StageManifest와 입력 로그로 주요 결과를 재현한다.
- 대기·이동·승리 루프의 시각 오프셋도 동일 시드에서 재현되게 한다.

## 9. 유닛 상태 후보

```text
Reserve
→ Deploying
→ Moving
→ Engaged
→ Casting
→ Recovering
→ Dead
```

병종 특수 상태는 별도 Unit 클래스를 만들기보다 명시적 서브상태 또는 행동 상태로 관리한다.

- 암살자: BypassEntering, BypassTravel, BypassExiting.
- 기병: Charging, TurnRecover.
- 비행병: Cruise, Diving, AirRecover.
- 거인: StructureAttacking, HeavyStagger.

런타임 행동 상태와 애니메이션 상태 ID의 매핑을 데이터로 검증한다.

## 10. Signal 원칙

- 자식 Scene은 부모·서비스의 깊은 경로를 탐색하지 않는다.
- 사용자 입력과 도메인 이벤트는 명시적 Signal 또는 좁은 메서드 계약으로 전달한다.
- 전역 이벤트 버스는 초기 기본값이 아니다.
- payload는 ID와 필요한 최소 값만 전달한다.

후보:

```gdscript
signal build_requested(node_id: StringName, building_id: StringName)
signal deployment_requested(reserve_id: int, lane_id: StringName)
signal roulette_spin_requested(reference_row: int)
signal strongpoint_owner_changed(strongpoint_id: StringName, owner_team_id: int)
signal gate_destroyed(gate_id: StringName)
signal unit_spawn_requested(archetype_id: StringName, owner_team_id: int, visual_faction_id: StringName)
```

## 11. 좌표와 라인

- 라인은 enum 또는 `StringName` ID를 사용한다.
- 이동 경로, 건설 노드와 목표는 라인 ID와 월드 좌표를 분리해 가진다.
- 우회로는 일반 이동 그래프와 분리하고 암살자 행동만 접근한다.
- 기본 포탑 사거리와 접전지·도로 거리를 데이터와 테스트에서 비교할 수 있어야 한다.
- UI 픽셀과 월드 단위를 혼용하지 않는다.

## 12. 다수 유닛 성능

- 정상 목표: 지상 120, 비행 24, 투사체 160, VFX 80.
- 모든 유닛이 매 프레임 전체 적을 검색하지 않고 라인·공간 후보 목록을 사용한다.
- 복잡한 rigid-body 군중 시뮬레이션을 기본으로 사용하지 않는다.
- 이동·표현은 프레임, 타깃 재탐색·오라·점령·경제는 낮은 고정 주기를 검토한다.
- 동일 Unit Scene과 공용 데이터 재사용으로 노드·스크립트·Resource 중복을 줄인다.
- 최적화 전 재현 가능한 객체 수 테스트와 프로파일링을 만든다.

## 13. UI 원칙

- HUD는 `Control`, `Container`, `Theme`로 구성한다.
- 룰렛 칸, 대기 유닛 카드, 건설 상품과 징조 행처럼 반복 단위만 재사용 Scene으로 분리한다.
- 전장 목표 상태는 실제 위치에 표시한다.
- 미니맵은 만들지 않는다.
- 한국어 확장, 1920×1080과 1280×720을 검증한다.
- 아군·적군 이미지는 팀 마커와 실루엣으로 구분하고 색만 의존하지 않는다.

## 14. 보호 경로 후보

프로젝트 생성 후 다음은 고위험 경로다.

- `project.godot`.
- 핵심 AutoLoad.
- UnitArchetypeProfile·Tier·Rank와 공통 전투 데이터.
- FactionVisualProfile·AnimationContract 스키마.
- BattlefieldProfile.
- 룰렛 확률·경제·웨이브 책임 원본.
- 저장 스키마가 생긴 이후 저장 코드.

변경 시 호출 위치, 데이터 호환, headless 결과와 실제 플레이를 함께 검증한다.

## 15. 자동 검증 후보

### 공용 병종

- UnitArchetypeProfile이 정확히 10개.
- 별도 EnemyUnitProfile과 진영별 스탯·스킬 복사본 없음.
- 모든 archetype에 아군·적군 FactionVisualProfile 존재.
- 두 이미지 세트의 상태, 프레임 수, 피벗과 이벤트 프레임 일치.
- `visual_faction_id` 변경이 능력치를 바꾸지 않음.
- 같은 archetype·Tier·Rank의 양 진영 전투 결과 동일.

### 전장

- 상·중·하 일반 이동 그래프 비연결.
- 성문, 거점, 노드 수와 연결 순서.
- 건물 점유 영역의 도로 침범 없음.
- 암살자만 우회 경로 사용.

### 시간·전투

- 일시정지 중 active_combat_time 정지.
- 동일 시드·입력 로그 결과 재현.
- 공격 판정과 애니메이션 이벤트 오차 한 프레임 이내.
- 성능 하드 상한과 갱신 주기.

## 16. 기본 검증 명령

Phase 0에서 실제 Godot 경로와 정확한 명령을 README에 확정한다.

후보:

```bash
git diff --check
godot --headless --path . --editor --quit
```

기능 작업은 다음을 추가한다.

- 데이터·참조 정적 검증.
- 변경 Scene 단독 실행.
- 관련 시스템 경계 테스트.
- 동일 시드 재현.
- 실제 메인 플레이 경로.
- 화면·모션·성능 수동 검수.

실행하지 않은 명령을 통과했다고 보고하지 않는다.

---

## C2 전투 목적 런타임

- `BattleSimulator`: 고정 0.1초 틱, 3라인, 접전지 3·중간거점 6·성문 6·본진 2와 목적 순서·이벤트 로그.
- `OutpostState`: 중립화·점령·교착·이탈 유지·복귀·안정화·capture revision.
- `GateState` / `BaseState`: 구조물 피해·붕괴·종료 상태.
- `BuildingService`: 거점 revision과 건물 ACTIVE/DISABLED/RUINED·식량 효과 동기화.
- `StageRun`: 실제 소유 수 경제, 적 본진·W15 보스 승리, 아군 본진 패배.
- `UnitArchetypeProfile`: 공용 점령력과 구조물 피해 태그.

본진 방어 프로필·중앙 접전지 점령 시간·0~100 목적 좌표는 승인값 부재를 드러낸 가역 fallback이며 최종 시각·밸런스 계약이 아니다.
