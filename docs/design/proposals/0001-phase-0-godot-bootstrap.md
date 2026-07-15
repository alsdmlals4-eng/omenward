# 제안서: Phase 0 Godot·공용 병종 데이터 부트스트랩

- 작성일: 2026-07-16
- 대응 Issue: #1
- 대응 Goal: `docs/goals/0001-engine-selection-and-bootstrap.md`
- 상태: **제안서 검토 대기 / 사용자 승인 전 구현 금지**
- 이번 문서의 성격: 읽기 전용 조사 결과와 구현 계획. 코드·Scene·Resource·데이터·테스트 구현물이 아니다.

---

## 1. 목적

### 해결할 문제

오멘워드는 프리프로덕션의 제품 방향과 데이터 계약은 승인됐지만, 아직 `project.godot`, Scene, GDScript, Resource와 테스트가 없는 구현 전 저장소다. 기술 기반을 먼저 임의로 만들면 다음 위험이 발생한다.

- 정확한 Godot 버전과 화면 정책이 뒤늦게 바뀜.
- 아군·적군 Unit Scene이나 데이터가 중복 생성됨.
- 공용 전투 데이터와 진영별 Visual Set의 책임이 섞임.
- 전투 시간, 일시정지, 난수와 입력 로그가 서로 다른 기준을 사용함.
- 애니메이션 이벤트가 실제 공격 판정의 원본이 됨.
- 수직 슬라이스 전에 범용 프레임워크와 AutoLoad가 과도하게 증가함.
- headless 검증이 없는 상태에서 다음 단계가 누적됨.

### 플레이어/개발 가치

Phase 0은 게임 콘텐츠를 구현하는 단계가 아니라 다음 수직 슬라이스를 안전하게 만들 수 있는 최소 기술 기반을 합의하는 단계다.

- 같은 공용 병종 데이터가 아군·적군 이미지에서 동일하게 동작한다.
- 전투·경제·웨이브가 일시정지와 시드에 대해 재현 가능하다.
- 잘못된 ID, 누락 참조, 적군 데이터 복사본과 Visual Set 불일치를 실행 전에 검출한다.
- 전체 전장과 HUD를 위한 화면 기준이 한 번만 정의된다.
- 실제 경로와 명령이 확정되어 Issue #32 수직 슬라이스 제안서가 추측 없이 작성된다.

---

## 2. 현재 상태와 근거

### 확인한 프로젝트 문서

- `AGENTS.md`
- `docs/BASE_RULES_VERSION.md`
- `docs/HANDOFF_CONTEXT.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/DOCUMENT_LIFECYCLE.md`
- `docs/PROPOSAL_WORKFLOW.md`
- `docs/OMENWARD_GAME_DESIGN.md`
- `docs/OMENWARD_ROADMAP.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/DECISIONS_PENDING.md`
- `docs/GODOT_PROJECT_STRUCTURE.md`
- `docs/REFERENCE_REPOSITORIES.md`
- `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`
- `docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`
- `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`
- `docs/design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md`
- `docs/design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md`
- `docs/goals/0001-engine-selection-and-bootstrap.md`
- GitHub Issue #1

### 확인한 실제 파일 상태

- 오멘워드 저장소에서 `project.godot`은 존재하지 않는다.
- `.tscn`, GDScript의 `extends Node`와 같은 구현 파일은 현재 검색 결과에서 확인되지 않았다.
- 현재 저장소의 책임 원본은 문서이며 Godot 프로젝트는 아직 생성되지 않았다.
- 따라서 Phase 0 구현은 기존 런타임 구조를 마이그레이션하는 작업이 아니라 최초 기술 기준선을 만드는 작업이다.

### Base에서 참고한 원칙

- 구현 전 사양과 승인 게이트를 분리한다.
- 상태와 책임 원본을 한 곳에 둔다.
- 공용 데이터와 표현 레이어를 분리한다.
- 완료 기준을 파일 존재가 아니라 관찰 가능한 실행 결과로 쓴다.
- 한 프로젝트의 해결안을 바로 보편 규칙으로 만들지 않고 사례와 검증을 거친다.

관련 Base 참고:

- `Base/docs/knowledge/methods/PROJECT_HANDOFF_CONTEXT_METHOD.md`
- `Base/docs/knowledge/methods/ANIMATION_AND_PRESENTATION_METHOD.md`
- `Base/docs/knowledge/research/DESIGN_RESEARCH_AND_EVIDENCE_METHOD.md`
- `Base/docs/knowledge/cases/OMENWARD_SHARED_ARCHETYPE_FACTION_VISUAL_CASE.md`

### urban-legend에서 참고한 구조

확인한 실제 기준:

- `project.godot`에서 Godot 4.7과 GDScript 프로젝트가 운용 중이다.
- `scenes/`, `scripts/`, `data/`, `tests/`, `assets/` 책임 분리가 실제 프로젝트에서 사용된다.
- Windows console 실행 파일과 `--headless --path . --quit` 형태의 검증 명령이 README에 기록되어 있다.

채택:

- 폴더 책임 분리.
- Windows PowerShell에서 console 실행 파일을 사용하는 명령 형식.
- headless 로드와 별도 계약 테스트를 구분하는 방식.

채택하지 않음:

- urban-legend의 두 AutoLoad와 상태 필드.
- 비주얼노벨·사건·조사 전용 Scene과 데이터.
- 1280×720 화면 정책과 Mobile renderer를 그대로 복사하는 방식.
- 프로젝트 고유 저장 스키마와 UI 구조.

### 공식 Godot 근거

확인일: 2026-07-16

- Windows 공식 다운로드의 현재 표준 버전은 Godot 4.7.1이며 2026-07-14 배포된 stable 유지보수 릴리스다.
  - https://godotengine.org/download/windows/
  - https://godotengine.org/download/archive/4.7.1-stable/
- Godot 4.7 공식 문서는 `--headless`를 창·오디오 없는 실행과 `--script`에 사용할 수 있다고 설명하고, `--path`로 프로젝트 경로를 지정하는 방식을 제공한다.
  - https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html
- 픽셀 아트에는 `viewport` stretch와 integer scaling이 균일한 픽셀 표시를 제공한다. 960×540은 1920×1080에서 정확히 2배 확대되지만 1280×720에서는 정수 배율로 화면을 가득 채우지 못한다.
  - https://docs.godotengine.org/en/4.7/tutorials/rendering/multiple_resolutions.html
- Compatibility renderer는 폭넓은 하드웨어를 지원하며 고급 렌더링 기능이 필요 없는 2D 게임의 기본 선택으로 적합하다.
  - https://docs.godotengine.org/en/4.7/tutorials/rendering/renderers.html

### 현재 저장소에서 재사용할 구조

- 승인된 공용 아키타입 10개와 ID.
- Tier·Rank·FactionVisual·AnimationContract 책임.
- 세 시간축 분리.
- 3라인 BattlefieldProfile 후보.
- 데이터 검증 목록과 성능 예산.
- `docs/GODOT_PROJECT_STRUCTURE.md`의 상태 소유·Signal·폴더 후보.

---

## 3. 확정 사항과 가정

### 사용자 확정 사항

```text
UnitArchetypeProfile × 10
+ TierProfile
+ RankProfile
+ owner_team_id
+ FactionVisualProfile
```

- 아군과 적군은 능력치·스킬·타기팅·점령·구조물 피해·AnimationContract를 공유한다.
- 별도 `EnemyUnitProfile`, 적군용 Unit Scene, 적군용 전투 데이터와 모션 상태 머신을 만들지 않는다.
- 진영 차이는 소유 팀, 출격 방식과 이미지·초상화·아이콘·팔레트·표시명이다.
- 일반 적 웨이브는 공용 `archetype_id`를 참조한다.
- W15·W20 보스는 공용 base archetype에 행동·페이즈 패키지와 전용 Visual Set을 추가한다.
- 엔진은 Godot, 기본 언어는 GDScript다.
- Windows PC, 16:9, 마우스·키보드, 싱글플레이 PvE다.
- 전장은 좌우 대칭의 독립된 3라인이며 미니맵을 사용하지 않는다.
- 코드·Scene·Resource·데이터 변경은 제안서 승인 후 시작한다.

### 제안서의 추천 가정

| 항목 | 추천안 | 이유 |
|---|---|---|
| Godot | **4.7.1 standard x86_64** | 현재 공식 stable 유지보수 버전, GDScript만 사용하므로 .NET 불필요 |
| Renderer | **Compatibility** | 2D 픽셀 전략 게임, 폭넓은 Windows 하드웨어, 고급 3D 기능 불필요 |
| 기준 출력 | 1920×1080 | 승인된 PC 기준 |
| 내부 해상도 | **960×540** | 전체 3라인과 HUD 정보량, 1080p에서 정확히 2배 확대 |
| Stretch | `viewport` + aspect `keep` | 픽셀 기준을 고정하고 16:9 화면 유지 |
| Scale mode | 1080p 기본 `integer` | 균일한 픽셀 확대 |
| 1280×720 QA | 정수 확대 시 레터박스 허용 후 가독성 확인 | 960×540을 720p에 정수로 채울 수 없음을 명시적으로 검증 |
| 언어 | GDScript 정적 타입 우선 | 프로젝트 계약과 빠른 반복 |
| AutoLoad | **Phase 0에서는 없음** | 실제 다중 Scene 공유 필요가 확인되기 전 전역 상태 방지 |
| Resource | 타입·규칙·에디터 조정 데이터 | 직접 참조와 타입 검증 |
| JSON | StageManifest·재현 로그·대량 생성 결과 | 외부 생성·직렬화·비교 용이 |
| CSV | 런타임 원본으로 사용하지 않음 | 초기 이중 원본 방지; 이후 오프라인 import/export로만 검토 |
| 애니메이션 | AnimatedSprite2D + 제한적 AnimationPlayer | 프레임 표현과 보조 연출을 분리 |
| 테스트 | 외부 플러그인 없는 GDScript headless runner | Phase 0 의존성 최소화 |

### 검토한 대안

#### Godot 4.6.3 stable 고정

장점:

- 4.7.1보다 장기간 사용된 버전일 가능성.

단점:

- 현재 공식 최신 stable보다 뒤처짐.
- 참고 프로젝트와 문서가 이미 4.7 기준.
- 신규 프로젝트가 처음부터 이전 버전에 묶임.

결론: 4.7.1에서 재현 가능한 치명적 회귀가 확인될 때만 4.6.3으로 내려간다.

#### 내부 640×360

장점:

- 1280×720에서 2배, 1920×1080에서 3배 정수 확대.
- 레터박스 없이 여러 16:9 해상도를 지원하기 쉬움.

단점:

- 3라인 전체 전장, 룰렛, 건설·전술, 벨루와 상태 표시를 동시에 보여주기에는 논리 픽셀 공간이 작음.
- 고해상도 픽셀 재질과 긴 한국어 UI의 정보 밀도가 과도해질 수 있음.

결론: 960×540을 추천한다. Phase 0 수동 검증에서 1280×720 레터박스가 제품 기준에 맞지 않거나 HUD가 더 작은 논리 해상도를 요구할 때만 640×360 전환안을 다시 제출한다.

#### 처음부터 DataRegistry·SessionState AutoLoad 사용

장점:

- 모든 Scene에서 접근이 쉬움.

단점:

- Scene이 하나뿐인 Phase 0에서 전역 의존성을 먼저 고정함.
- 테스트 격리와 수직 슬라이스의 상태 소유가 어려워짐.

결론: Main이 GameSession과 DataRegistry를 소유하고 명시적으로 전달한다. 메뉴·전투·결과 전환에서 실제 지속 상태가 필요해질 때 별도 제안으로 AutoLoad 승격을 검토한다.

### 확인이 필요한 항목

사용자 승인으로 확정할 항목:

1. Godot 4.7.1 standard와 Compatibility renderer 채택.
2. 960×540 내부 해상도와 1280×720 정수 확대 레터박스 허용.
3. Phase 0에서 AutoLoad를 사용하지 않는 구조.
4. Resource/JSON/CSV 경계.
5. Phase 0에서 10개 공용 아키타입과 양 진영 Visual Profile 골격을 모두 생성하는 범위.

구현 중 측정 후 다시 결정할 항목:

- 실제 placeholder의 픽셀 크기와 전략 줌 가독성.
- AnimationPlayer가 필요한 보조 연출 범위.
- JSON Schema 파일을 별도 둘지 GDScript validator를 책임 원본으로 둘지.
- 수직 슬라이스 진입 후 DataRegistry를 AutoLoad로 승격할지.

---

## 4. 제안 구조

### 4.1 Godot 프로젝트 설정

추천:

```text
Godot: 4.7.1 standard x86_64
Language: GDScript
Renderer: Compatibility
Output target: 1920 × 1080
Logical viewport: 960 × 540
Stretch mode: viewport
Stretch aspect: keep
Stretch scale mode: integer
Pixel texture filtering: nearest
```

운영 규칙:

- `project.godot`은 Godot 에디터가 생성한 값을 기준으로 커밋한다.
- 사용자별 Godot 설치 경로를 저장소에 하드코딩하지 않는다.
- README에서는 `$env:GODOT_BIN` 환경 변수와 실제 예시를 함께 제공한다.
- 1280×720에서는 정수 확대 레터박스 상태와 UI 읽기 여부를 수동 검증한다.
- Phase 0에서는 카메라 확대·이동 기능을 구현하지 않고, 화면 기준과 픽셀 정렬 probe만 둔다.

### 4.2 최소 Scene 구조

```text
Main (Node)
├─ GameSession (Node)
│  ├─ CombatClock (Node)
│  ├─ DeterminismService (Node)
│  └─ DataRegistry (Node)
├─ WorldRoot (Node2D)
│  └─ BootstrapVisualProbe (Node2D)
└─ UI (CanvasLayer)
   └─ BootstrapStatusPanel (Control)
```

책임:

- `Main`: 부트스트랩 순서와 오류 표시. 게임 규칙을 직접 계산하지 않는다.
- `GameSession`: 현재 실행 세션의 시간·시드·명령 로그 참조를 소유한다.
- `CombatClock`: `real_time`, `active_combat_tick`, `ui_planning_time`을 분리한다.
- `DeterminismService`: master seed와 이름이 있는 RNG stream을 제공한다.
- `DataRegistry`: 명시된 catalog를 로드하고 ID·참조·중복·Visual 호환을 검증한다.
- `BootstrapVisualProbe`: 같은 archetype을 allied/veil Visual Set으로 나란히 표시하는 배선 검증용이다. 전투하지 않는다.
- `BootstrapStatusPanel`: 엔진 버전, catalog 검사, seed, active tick과 테스트 상태를 표시한다.

Phase 0에서 만들지 않는 Scene:

- Battle Scene.
- 별도 Ally Unit / Enemy Unit Scene.
- 룰렛·건물·거점·성문·웨이브 Scene.
- 메뉴·결과·설정 Scene.

이 Scene들은 Phase 0 기준선이 검증된 뒤 Issue #32에서 실제 경로와 책임을 제안한다.

### 4.3 상태 소유

```text
Main
└─ GameSession
   ├─ current_seed
   ├─ active_combat_tick
   ├─ planning_state
   ├─ input_log
   └─ registry references
```

원칙:

- Phase 0에서는 AutoLoad 없음.
- 런타임 서비스는 GameSession 자식으로 생성해 테스트마다 새 인스턴스로 격리한다.
- Unit·Building·Gate·Strongpoint 런타임 상태는 향후 각 인스턴스가 소유한다.
- UI의 선택·포커스·열림 상태는 UI가 소유한다.
- Resource는 정적 정의이며 런타임 체력·타깃·타이머를 저장하지 않는다.
- 같은 값을 Resource, GameSession과 Scene이 동시에 원본으로 관리하지 않는다.

### 4.4 시간과 일시정지

고정 시뮬레이션 기준:

```text
simulation_hz = 60
active_combat_tick: int
active_combat_time = active_combat_tick / simulation_hz
```

- `real_time`: 엔진의 실제 경과 시간과 디버그 표시만 담당하며 게임 결과의 원본이 아니다.
- `active_combat_tick`: 웨이브·생산·건설·수입·쿨다운·암살자 우회의 권위 시간이다.
- `ui_planning_time`: 계획 화면의 애니메이션·입력 대기 계측이며 게임 결과를 진행시키지 않는다.
- 계획 모드에서는 SceneTree 전체를 멈추기보다 GameSession의 active tick 증가를 중단한다.
- UI는 계속 반응한다.
- 시각 히트 스톱이 도입되더라도 simulation tick을 역으로 변경하지 않는다. 정확한 표현 시간 분리는 수직 슬라이스 제안서에서 결정한다.

### 4.5 결정론적 난수와 입력 로그

```text
master_seed
├─ roulette stream
├─ wave stream
├─ combat stream
└─ presentation stream
```

- 전역 `rand*` 호출을 게임 규칙에서 사용하지 않는다.
- stream 이름과 master seed에서 안정적인 정수 seed를 생성한다.
- stream 분리는 룰렛의 호출 수 변화가 웨이브·전투 결과를 흔들지 않게 한다.
- 프레젠테이션 오프셋은 별도 stream을 사용하고 전투 규칙에 영향을 주지 않는다.

입력 로그 최소 항목:

```text
schema_version
stage_id
master_seed
commands[]
  active_tick
  sequence
  command_id
  payload_ids
```

- Phase 0에서는 배치·건설·룰렛의 실제 명령을 구현하지 않는다.
- `bootstrap_toggle_planning`과 같은 테스트 명령으로 기록→재생→동일 tick 결과를 검증한다.
- 저장 위치는 테스트에서는 메모리, 디버그 출력이 필요한 경우 `user://replays/`를 사용한다.
- 실제 캠페인 저장 스키마는 Phase 0 범위 밖이다.

### 4.6 공용 데이터 구조

#### UnitArchetypeProfile

진영과 무관한 전투 규칙의 원본이다.

```text
archetype_id: StringName
role_tags: Array[StringName]
movement_layer: StringName
food_cost: int
base_stats
attack_profile_id: StringName
passive_ids: Array[StringName]
skill_ids: Array[StringName]
targeting_profile_id: StringName
capture_power: float
structure_damage_tags: Array[StringName]
animation_contract_id: StringName
threat_cost: float
```

정확히 다음 10개 ID를 만든다.

```text
shield_guard
greatsword_warrior
assassin
spearman
archer
cavalry
priest
mage
flying_lancer
giant
```

Phase 0 수치는 스키마와 참조 검증용 중립 placeholder다. 승인된 전투 수치처럼 취급하지 않는다.

#### TierProfile

```text
tier_id
production_time_multiplier
food_cost_modifier
stat_modifiers
passive_unlocks
specialization_options
```

- `tier_1`, `tier_2`, `tier_3` 골격을 만든다.
- 수치는 기본 1.0 중심 placeholder로 두고 실제 병종 분화는 구현하지 않는다.

#### RankProfile

```text
rank_id
hp_multiplier
damage_multiplier
threat_multiplier
skill_unlock_count
visual_grade_id
```

- `normal`, `elite`, `hero`, `legendary` 골격만 만든다.
- `mythic` Rank는 만들지 않는다.
- W20 신화는 향후 BossBehaviorPackage에서 처리한다.

#### FactionVisualProfile

```text
visual_faction_id
archetype_id
sprite_frames
portrait
icon
palette_or_material_id
pivot_profile_id
```

- 각 archetype에 `allied`와 `veil` 두 프로필을 둔다.
- Phase 0에서는 두 placeholder 이미지 세트를 여러 프로필이 공유할 수 있다.
- 프로필은 20개로 분리해 누락 여부와 참조를 검증한다.
- `visual_faction_id`는 전투 수치와 타이밍 필드를 가지지 않는다.

#### AnimationContract

```text
animation_contract_id
states[]
  state_id
  frame_count
  playback_fps
  loop
  impact_frame
  projectile_spawn_frame
  cancel_window
  recovery_duration
```

Phase 0 필수 상태:

```text
deploy
idle
move
attack_basic
skill_1
hit_light
death
victory
```

- 10 archetype에 계약 하나씩 둔다.
- allied/veil Visual Set이 같은 계약을 참조한다.
- Phase 0 placeholder는 실제 공격·피해를 만들지 않고 프레임·피벗·이벤트 호환만 검증한다.

#### BattlefieldProfile

Phase 0에서는 전체 맵 Scene을 만들지 않고 데이터 스키마와 topology validator를 준비한다.

```text
lane_ids = [top, middle, bottom]
base_ids
gate_profiles
mid_strongpoint_profiles
clash_point_profiles
build_nodes
lane_paths
assassin_bypass_profiles
world_scale
```

bootstrap profile은 다음 구조만 검증한다.

- 독립 라인 3개.
- 성문 6개.
- 중간거점 6개.
- 중앙 접전지 3개.
- 중간거점마다 전방 2·후방 1 노드.
- 일반 라인 간 연결 없음.
- 우회 경로는 assassin 접근 태그만 가짐.

실제 좌표와 이동 곡선은 Issue #32에서 전장 블록아웃과 함께 확정한다.

#### StageManifest

JSON을 사용한다.

```text
schema_version
stage_id
seed
battlefield_profile_id
wave_schedule
spawn_entries
telegraph_entries
boss_package_id?
```

- Phase 0의 bootstrap manifest는 빈 공세 또는 검증용 한 항목만 가진다.
- 일반 spawn entry는 공용 `archetype_id`, Tier, Rank, count, lane, time, owner team, visual faction만 참조한다.
- HP·공격력·스킬·AnimationContract를 spawn entry에 복사하지 않는다.

### 4.7 Resource·JSON·CSV 경계

| 형식 | 책임 | Phase 0 |
|---|---|---|
| `.tres` typed Resource | 사람이 조정하는 타입·규칙·시각 계약 | 사용 |
| JSON | 생성된 StageManifest, replay/input log, 외부 비교 가능한 데이터 | 사용 |
| CSV | 대량 표의 오프라인 import/export | 사용 안 함 |

규칙:

- 같은 시스템의 활성 원본을 `.tres`와 JSON 두 곳에 중복하지 않는다.
- JSON은 loader가 타입과 ID를 검증한 뒤 런타임 구조로 변환한다.
- CSV를 향후 사용하더라도 빌드 시 검증된 Resource/JSON으로 변환하고 런타임에서 직접 해석하지 않는다.
- `DataRegistry`는 폴더 전체를 암묵적으로 스캔하지 않고 `BootstrapCatalog`의 명시적 참조 목록을 로드한다.

### 4.8 애니메이션과 판정 연결

추천 조합:

- `AnimatedSprite2D`: 상태별 SpriteFrames 재생.
- `AnimationPlayer`: 선택 마커, 작은 보조 VFX, UI/재질 변화처럼 전투 규칙이 아닌 연출.
- `AnimationContract`: 프레임 수, impact/projectile frame과 회복 시간의 데이터 계약.
- 향후 `UnitActionController`: active tick을 기준으로 공격 이벤트를 예약.

권위 규칙:

```text
AttackProfile·행동 상태
→ active tick에서 판정 예약
→ AnimationContract 이벤트와 일치 검증
→ AnimatedSprite2D/AnimationPlayer는 결과를 표현
```

- AnimationPlayer의 method track을 피해 판정의 유일한 원본으로 사용하지 않는다.
- 프레임 드롭이나 재생 속도 변경이 전투 결과를 바꾸지 않게 한다.
- Phase 0에서는 실제 공격을 구현하지 않고 Visual Probe에서 상태 전환과 프레임 계약만 확인한다.

### 4.9 예상 파일 경로

```text
project.godot
README.md

scenes/main/main.tscn

scripts/main/main.gd
scripts/core/game_session.gd
scripts/core/combat_clock.gd
scripts/core/determinism_service.gd
scripts/core/input_log.gd
scripts/data/data_registry.gd
scripts/data/stage_manifest_loader.gd
scripts/data/resources/unit_archetype_profile.gd
scripts/data/resources/tier_profile.gd
scripts/data/resources/rank_profile.gd
scripts/data/resources/faction_visual_profile.gd
scripts/data/resources/animation_contract.gd
scripts/data/resources/battlefield_profile.gd
scripts/data/resources/bootstrap_catalog.gd
scripts/presentation/bootstrap_visual_probe.gd
scripts/ui/bootstrap_status_panel.gd

resources/bootstrap/bootstrap_catalog.tres
resources/units/archetypes/*.tres                 # 10
resources/units/tiers/*.tres                      # 3
resources/units/ranks/*.tres                      # 4
resources/presentation/animation_contracts/*.tres # 10
resources/presentation/factions/allied/*.tres     # 10
resources/presentation/factions/veil/*.tres       # 10
resources/battlefields/bootstrap_battlefield.tres

data/stages/bootstrap_stage_manifest.json

assets/bootstrap/allied_placeholder.svg
assets/bootstrap/veil_placeholder.svg

tests/run_all.gd
tests/support/test_case.gd
tests/test_catalog_validation.gd
tests/test_clock_and_replay.gd
tests/test_visual_contract.gd
tests/test_battlefield_contract.gd
```

파일 수가 늘어나는 이유는 별도 적군 전투 데이터를 만드는 것이 아니라, 공용 archetype 10개에 양 진영 Visual Profile이 빠짐없이 존재하는지 실제 파일 단위로 검증하기 위해서다. 두 진영의 placeholder texture는 각각 한 파일을 공유한다.

### 4.10 Signal과 의존성

Phase 0 최소 Signal:

```gdscript
signal bootstrap_completed(report: Dictionary)
signal bootstrap_failed(errors: Array[String])
signal planning_state_changed(is_planning: bool)
signal active_tick_advanced(active_tick: int)
```

- 자식 Node가 `/root` 경로로 서비스를 찾지 않는다.
- Main이 의존성을 주입한다.
- 전역 Event Bus를 만들지 않는다.
- Signal payload는 ID와 최소 값만 전달한다.

---

## 5. 단계별 작업 계획

### 1. Phase 0.1 — 프로젝트와 화면 기준선

변경 내용:

- Godot 4.7.1 standard로 프로젝트 생성.
- Compatibility renderer 설정.
- 960×540 viewport, 1920×1080 window, stretch·nearest 기준 설정.
- `.gitignore`에 `.godot/`, 사용자 캐시와 빌드 산출물 제외.
- 최소 Main Scene과 status panel 생성.

예상 파일:

- `project.godot`
- `.gitignore`
- `scenes/main/main.tscn`
- `scripts/main/main.gd`
- `scripts/ui/bootstrap_status_panel.gd`
- `README.md`

관찰 가능한 결과:

- Godot editor와 headless에서 프로젝트가 오류 없이 열린다.
- 창에 OMENWARD Phase 0 상태, 논리 해상도와 renderer가 표시된다.
- 1920×1080에서 픽셀 probe가 정확히 2배 정수 확대된다.

### 2. Phase 0.2 — 시간·시드·입력 로그

변경 내용:

- GameSession, CombatClock, DeterminismService와 InputLog 골격.
- 60Hz active tick과 planning pause.
- 이름 기반 RNG stream.
- 테스트 명령 기록과 재생.

예상 파일:

- `scripts/core/game_session.gd`
- `scripts/core/combat_clock.gd`
- `scripts/core/determinism_service.gd`
- `scripts/core/input_log.gd`

관찰 가능한 결과:

- planning 중 active tick은 증가하지 않고 UI 상태는 바뀐다.
- 같은 seed와 입력 로그를 두 번 재생하면 같은 tick·난수 표본을 출력한다.
- 다른 RNG stream의 호출 수가 다른 stream 결과를 바꾸지 않는다.

### 3. Phase 0.3 — typed Resource 스키마

변경 내용:

- UnitArchetype, Tier, Rank, FactionVisual, AnimationContract, Battlefield와 BootstrapCatalog Resource 클래스.
- 명시적 ID와 참조 필드.
- 런타임 상태가 Resource에 들어가지 않도록 경계 설정.

예상 파일:

- `scripts/data/resources/*.gd`

관찰 가능한 결과:

- Godot Inspector에서 타입이 표시된다.
- 잘못된 ID 타입과 필수 참조 누락을 validator가 보고한다.

### 4. Phase 0.4 — 공용 10병종·양 진영 Visual 골격

변경 내용:

- 공용 archetype 10개.
- Tier 3개, Rank 4개.
- AnimationContract 10개.
- allied/veil Visual Profile 각각 10개.
- 두 placeholder 이미지.

예상 파일:

- `resources/units/**`
- `resources/presentation/**`
- `assets/bootstrap/**`

관찰 가능한 결과:

- archetype 수가 정확히 10개다.
- 모든 archetype에 allied와 veil Visual Profile이 하나씩 있다.
- `EnemyUnitProfile`, enemy 전용 stat/skill/animation 파일이 없다.
- `visual_faction_id`를 바꿔도 계산된 공용 데이터가 변하지 않는다.

### 5. Phase 0.5 — DataRegistry·Manifest·전장 계약 검증

변경 내용:

- BootstrapCatalog 명시적 로딩.
- StageManifest JSON loader.
- ID·중복·참조·금지 필드 검사.
- 3라인 topology bootstrap profile과 validator.

예상 파일:

- `scripts/data/data_registry.gd`
- `scripts/data/stage_manifest_loader.gd`
- `resources/bootstrap/bootstrap_catalog.tres`
- `resources/battlefields/bootstrap_battlefield.tres`
- `data/stages/bootstrap_stage_manifest.json`

관찰 가능한 결과:

- 유효 catalog와 manifest는 PASS.
- 존재하지 않는 archetype, 중복 ID와 spawn entry의 직접 HP 필드는 명시적으로 FAIL.
- 3라인, 성문 6개, 거점·노드 수와 우회 접근 태그를 검사한다.

### 6. Phase 0.6 — Visual Contract probe

변경 내용:

- 같은 archetype을 allied/veil Visual Profile로 나란히 생성.
- 공용 AnimationContract 상태를 순환.
- pivot, frame count와 이벤트 frame 비교.

예상 파일:

- `scripts/presentation/bootstrap_visual_probe.gd`
- Main Scene 연결.

관찰 가능한 결과:

- `visual_faction_id`만 바꾸면 이미지가 바뀐다.
- 두 Visual Profile이 같은 AnimationContract를 사용한다.
- 필수 상태나 피벗·프레임 계약이 다르면 조용히 대체하지 않고 실패를 표시한다.

### 7. Phase 0.7 — headless 테스트·문서·다음 Gate 갱신

변경 내용:

- 외부 의존성 없는 GDScript test runner.
- catalog, clock/replay, visual, battlefield 계약 테스트.
- README에 실제 Godot 경로 변수와 검증 명령.
- 실제 생성된 경로를 Goal 0002와 Issue #32에 반영.

예상 파일:

- `tests/**`
- `README.md`
- `docs/GODOT_PROJECT_STRUCTURE.md`
- `docs/goals/0002-core-vertical-slice.md`
- Issue #32
- `docs/HANDOFF_CONTEXT.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/OMENWARD_ROADMAP.md`

관찰 가능한 결과:

- headless 프로젝트 로드와 계약 테스트가 모두 exit code 0.
- 일부러 만든 잘못된 fixture가 예상 오류로 실패한다.
- 다음 수직 슬라이스 제안서가 실제 경로와 명령을 참조한다.

### 권장 구현 커밋 단위

사용자 승인 후 별도 구현 브랜치에서 다음 단위로 커밋한다.

1. `chore: bootstrap Godot 4.7.1 project`
2. `feat(core): add deterministic session clock and input log`
3. `feat(data): add shared unit resource contracts`
4. `data: add ten archetype and faction visual bootstrap catalog`
5. `test: add catalog visual and battlefield contract validation`
6. `docs: record Phase 0 paths commands and handoff`

각 커밋은 독립적으로 headless 로드 또는 관련 테스트를 통과해야 한다.

---

## 6. 포함 범위

- Godot 4.7.1 standard 프로젝트 기준선.
- Compatibility renderer와 960×540 화면 정책.
- 최소 Main Scene과 상태 표시 probe.
- GameSession, 세 시간축, planning pause.
- 결정론적 seed, RNG stream과 입력 로그 골격.
- 공용 UnitArchetype·Tier·Rank typed Resource.
- FactionVisualProfile·AnimationContract typed Resource.
- 정확히 10개의 공용 archetype 골격.
- 각 archetype의 allied/veil Visual Profile 골격.
- BattlefieldProfile topology 골격.
- bootstrap StageManifest JSON.
- DataRegistry와 참조·중복·금지 필드 검증.
- Visual Contract probe.
- 외부 플러그인 없는 headless 테스트 runner.
- README 실행·검증 명령.
- Phase 0 완료 후 Goal 0002·Issue #32 실제 경로 동기화.

---

## 7. 제외 범위

- 실제 전투와 피해 계산 실행.
- 유닛 이동·타기팅·공격 AI.
- 룰렛·건설·생산·경제·점령·성문·웨이브 구현.
- 3라인 전장 Scene과 Camera2D 조작.
- 암살자 우회 동작.
- 실제 Unit Scene과 UnitInstance 전투 상태 머신.
- 최종 스프라이트·초상화·아이콘·VFX·오디오.
- 적군 전용 UnitProfile·Unit Scene·스킬·애니메이션 데이터.
- 실제 밸런스 수치 확정.
- 캠페인 저장·불러오기.
- UI 프레임워크·이벤트 버스·ECS·GDExtension.
- 외부 테스트 플러그인과 애드온.
- 배포·Steam 패키징.
- Issue #32 수직 슬라이스의 실제 구현.

---

## 8. 위험과 대응

| 위험 | 영향 | 예방 또는 검증 방법 |
|---|---|---|
| Godot 4.7.1 신규 회귀 | 프로젝트 로드·픽셀 렌더링 문제 | Phase 0 첫 단계에서 editor/headless 확인, 재현 가능한 치명적 문제만 4.6.3 대안 제출 |
| 960×540이 1280×720을 정수 배율로 채우지 못함 | 레터박스 또는 fractional artifact | 1080p를 제품 기준으로 고정하고 720p 레터박스 수동 QA; 불가 시 640×360 전환을 별도 승인 |
| Compatibility 기능 한계 | 후속 VFX 표현 제약 | Phase 0은 core 2D만 사용; 실제 필요한 고급 기능이 생기면 비교 측정 후 renderer 변경 제안 |
| Resource 파일 수 증가 | 초기 관리 부담 | catalog 명시 참조와 규칙적인 경로; 이미지 texture는 공유하고 데이터 책임만 분리 |
| placeholder 수치가 승인 밸런스로 오해됨 | 잘못된 구현 고착 | 모든 bootstrap Resource에 `bootstrap_only`/문서 상태 표시, 테스트는 구조와 동일성만 확인 |
| DataRegistry가 거대한 서비스가 됨 | 결합도와 테스트 어려움 | 로딩·검증·조회만 담당, 전투·경제·생성 규칙 금지 |
| AutoLoad를 쓰지 않아 전달 코드가 늘어남 | 초기 보일러플레이트 | Phase 0에서는 명시적 주입으로 책임 검증; 실제 Scene 전환 필요가 확인된 뒤 승격 |
| 난수 호출 순서에 따른 비결정성 | 재현 실패 | 이름 기반 RNG stream 분리, global rand 금지, 같은 seed·log 회귀 테스트 |
| AnimationPlayer가 게임 판정을 소유함 | 프레임 드롭·속도 변경으로 결과 변화 | active tick과 AttackProfile을 권위 원본으로 유지, AnimationContract는 동기화 검증 |
| Visual Set 체형 차이 | 피벗·접촉 프레임 불일치 | Phase 0 정적 validator와 probe; 계약을 못 맞추면 이미지 디자인을 먼저 수정 |
| 적군 데이터 복제 재발 | 밸런스·테스트·자산 비용 증가 | 파일명·클래스·필드 금지 검사와 같은 archetype 양 진영 결과 테스트 |
| 폴더 스캔 순서 의존 | 플랫폼별 로드 차이 | BootstrapCatalog의 명시적 참조 목록 사용 |
| headless 테스트가 수동 가독성을 대체 | 실제 화면 문제 누락 | 자동 계약과 1080p/720p 수동 화면 검수를 별도 완료 기준으로 유지 |

---

## 9. 검증 제안

### 정적 검사

```powershell
& git diff --check
```

추가 validator:

- ID 형식과 중복.
- 필수 참조 존재.
- UnitArchetype 수 정확히 10개.
- `EnemyUnitProfile`, enemy 전용 stats/skills/targeting/animation 필드 없음.
- 각 archetype에 allied/veil Visual Profile 하나씩.
- 두 Visual Profile이 같은 AnimationContract를 참조.
- 필수 상태·프레임 수·피벗·이벤트 frame 일치.
- player mythic Rank 없음.
- StageManifest spawn entry가 공용 archetype만 참조.
- StageManifest에 직접 HP·damage·skill 필드 없음.
- BattlefieldProfile의 3라인·성문·거점·노드·우회 계약.

### Godot 실행 환경

README 권장 형태:

```powershell
$env:GODOT_BIN = "C:\Tools\Godot\Godot_v4.7.1-stable_win64_console.exe"
& $env:GODOT_BIN --version
```

사용자 설치 경로가 다르면 환경 변수만 변경한다.

### Godot headless

```powershell
& $env:GODOT_BIN --headless --path . --editor --quit
& $env:GODOT_BIN --headless --path . --script res://tests/run_all.gd
```

첫 명령:

- project 설정, Scene와 script 파싱.
- import와 Resource 참조 오류 확인.

두 번째 명령:

- catalog·clock/replay·visual·battlefield 계약 테스트.
- 실패 시 non-zero exit code.

### 테스트 항목

#### Catalog

- 정확히 10개의 archetype.
- Tier 3개, player Rank 4개.
- 각 archetype에 두 진영 visual.
- 누락·중복·잘못된 ID fixture가 예상대로 실패.

#### Clock and replay

- 60 active tick 뒤 1초.
- planning 상태에서 active tick 정지.
- planning 해제 뒤 같은 순서로 진행.
- 같은 seed와 log 결과 동일.
- roulette stream 추가 호출이 wave stream 결과에 영향 없음.

#### Visual contract

- allied/veil이 동일 AnimationContract 참조.
- 상태·프레임·피벗·event mismatch 실패.
- visual faction 변경 전후 계산된 archetype·Tier·Rank 데이터 동일.

#### Battlefield contract

- lane 3개.
- gate 6개.
- mid strongpoint 6개.
- clash point 3개.
- strongpoint당 전방 2·후방 1 노드.
- 일반 경로 간 lane 연결 없음.
- 우회 접근 archetype tag가 assassin으로 제한.

### Scene 실행과 수동 확인

1920×1080:

1. bootstrap status가 정상과 오류를 구분한다.
2. allied/veil placeholder가 같은 기준선과 프레임으로 보인다.
3. 1px probe가 2×2 균일 픽셀로 확대된다.
4. 한국어 상태 문구가 잘리지 않는다.
5. planning toggle 중 active tick이 멈추고 UI는 반응한다.

1280×720:

1. 정수 배율 레터박스 크기를 확인한다.
2. UI와 probe가 흐려지거나 불균일해지지 않는다.
3. 레터박스가 제품 최소 해상도로 허용 가능한지 기록한다.
4. 허용 불가하면 구현을 확장하지 않고 640×360 또는 fractional 대안을 다시 검토한다.

### 성능 또는 경계 조건

Phase 0은 실제 유닛 120기를 생성하지 않는다. 대신 다음을 확인한다.

- 부트스트랩 실행과 catalog 검증 시간이 개발 PC에서 즉시 완료된다.
- 데이터 로딩이 매 frame 반복되지 않는다.
- Resource와 JSON loader가 경고를 조용히 무시하지 않는다.
- 실제 객체 성능 부하는 Issue #32 수직 슬라이스에서 승인된 목표 수량으로 계측한다.

### 실행 결과 보고 형식

```md
## 실행 환경
- Godot 버전:
- 실행 파일:
- OS:

## 자동 검증
- git diff --check:
- headless editor load:
- tests/run_all.gd:

## 수동 검증
- 1920×1080:
- 1280×720:
- allied/veil probe:
- planning pause:

## 실패·미검증
-
```

실행하지 않은 명령은 PASS로 기록하지 않는다.

---

## 10. 완료 기준

### 프로젝트 기준선

- [ ] Godot 4.7.1 standard에서 프로젝트가 editor와 headless로 열린다.
- [ ] renderer가 Compatibility로 확인된다.
- [ ] 960×540 viewport와 1920×1080 기준이 실제 설정과 README에 일치한다.
- [ ] `.godot/`과 로컬 생성물이 Git 추적 대상이 아니다.

### 시간·결정론

- [ ] 조건: active tick 진행 중 → 행동: planning 진입 → 결과: UI는 반응하고 active tick은 증가하지 않는다.
- [ ] 조건: 같은 seed와 input log → 행동: 두 번 재생 → 결과: tick과 RNG 표본 결과가 동일하다.
- [ ] 조건: 한 RNG stream의 호출 수 변경 → 행동: 다른 stream 비교 → 결과: 다른 stream 결과가 변하지 않는다.

### 공용 병종 데이터

- [ ] 공용 UnitArchetypeProfile이 정확히 10개 존재한다.
- [ ] 같은 archetype에 allied/veil Visual Profile이 각각 하나 존재한다.
- [ ] 두 진영은 같은 Tier·Rank·AnimationContract를 참조한다.
- [ ] `visual_faction_id`만 변경했을 때 계산된 능력치·스킬 참조·타이밍이 동일하다.
- [ ] 별도 `EnemyUnitProfile`, Enemy Unit Scene, enemy 전용 stat/skill/targeting/animation 데이터가 없다.
- [ ] `mythic` player Rank가 없다.

### 데이터·전장 계약

- [ ] 잘못된 ID, 중복과 누락 참조가 시작 전에 실패한다.
- [ ] StageManifest가 공용 archetype을 참조하고 직접 전투 수치를 복제하지 않는다.
- [ ] BattlefieldProfile validator가 독립 3라인, 성문 6개, 거점·노드 구조와 assassin 우회를 확인한다.

### Visual Contract

- [ ] 같은 archetype을 allied/veil 이미지로 각각 표시할 수 있다.
- [ ] 상태·프레임·피벗·이벤트 불일치는 자동 실패한다.
- [ ] placeholder Visual Set이 실제 전투 데이터의 진영별 복사본을 만들지 않는다.

### 검증·인수인계

- [ ] `git diff --check`가 통과한다.
- [ ] Godot headless editor load가 통과한다.
- [ ] `tests/run_all.gd`가 통과하고 실패 fixture는 예상대로 실패한다.
- [ ] 1920×1080과 1280×720 수동 결과가 기록된다.
- [ ] README에 실제 실행·검증 명령이 있다.
- [ ] `docs/GODOT_PROJECT_STRUCTURE.md`, Handoff, Active Context와 Roadmap이 실제 구현 경로를 설명한다.
- [ ] Goal 0002와 Issue #32가 실제 파일·명령으로 갱신된다.

### Phase 0 종료 상태

```text
Godot 기술 기준선 구현·검증 완료
→ Issue #32 수직 슬라이스 Plan Mode 준비
→ 사용자 승인 전 수직 슬라이스 구현 금지
```

---

## 11. 사용자 결정 요청

### 결정 A — 엔진과 renderer

추천:

```text
Godot 4.7.1 standard x86_64
+ GDScript
+ Compatibility renderer
```

대안:

- 4.7.1의 치명적 회귀가 재현될 때만 Godot 4.6.3 stable.
- 고급 렌더링 기능의 구체적 필요가 생길 때만 Mobile 또는 Forward+ 재검토.

### 결정 B — 화면

추천:

```text
1920×1080 기준 출력
960×540 내부 viewport
viewport stretch
keep aspect
integer scale
1280×720은 레터박스 허용 상태로 QA
```

대안:

- 1280×720 무레터박스 정수 확대가 필수면 640×360.
- fractional scaling은 픽셀 균일성 문제를 감수할 때만 사용.

### 결정 C — 상태 소유

추천:

- Phase 0 AutoLoad 없음.
- Main의 GameSession 자식이 Clock·Determinism·Registry를 소유.
- 수직 슬라이스에서 실제 다중 Scene 지속 필요가 확인되면 AutoLoad 승격 제안.

### 결정 D — 데이터 경계

추천:

- typed `.tres`: UnitArchetype·Tier·Rank·Visual·Animation·Battlefield.
- JSON: StageManifest와 input/replay log.
- CSV: Phase 0 런타임에서 사용하지 않음.

### 결정 E — Phase 0 데이터량

추천:

- 10개 공용 archetype 골격을 모두 생성.
- allied/veil Visual Profile을 archetype별로 각각 생성.
- 실제 이미지는 진영별 placeholder 두 장을 공유.
- 실제 능력·밸런스·개별 아트는 수직 슬라이스 이후.

### 승인 문구

위 추천안 전체로 진행할 경우:

```text
제안서 승인
```

일부를 바꿀 경우 엔진·화면·상태 소유·데이터 경계·Phase 0 데이터량 중 변경할 항목을 지정한다. 수정된 제안서는 다시 검토 상태로 둔다.

---

## 12. 승인 게이트

- 현재 상태: **제안서 검토 대기**
- 사용자 승인 전 `project.godot`, Scene, GDScript, Resource, 데이터, 자산과 테스트 생성 금지.
- 사용자 승인 전 구현 브랜치·커밋·Pull Request 생성 금지.
- 이번 제안서 파일과 인수인계 문서 갱신은 기획·문서 작업이며 Phase 0 구현 완료를 의미하지 않는다.
- 승인 뒤에도 이 문서의 포함 범위만 구현한다.
- 구현 중 범위 밖 기술 필요가 발견되면 중단하고 제안서 수정안으로 돌아간다.

```text
현재 상태: 제안서 검토 대기
사용자 승인 전 구현 금지
```
