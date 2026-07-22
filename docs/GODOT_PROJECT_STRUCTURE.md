# OMENWARD Godot 프로젝트 구조

- 상태: **기술 기준선·C1 REMOTE_PROVEN / C2 전투 목적 REMOTE_PROVEN / C3 코어 UX IMPLEMENTED·원격 검증 대기**
- 갱신일: 2026-07-23
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

- `StageRun.core_ux_snapshot()`으로 받은 상태를 표시하고 사용자 의도를 Signal로 반환한다.
- 확률, 경제, 원인 코드, 금화 차감, 건설 확정, 유닛 생성, 점령 판정을 직접 계산·실행하지 않는다.
- C3 HUD는 토큰·확률·징조·사거리/대상·웨이브 원인·건설 비교를 표시한다.
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
counter_tags
target_priority_tags
capture_power
structure_damage_tags
animation_contract_id
threat_cost
```

- `faction` 필드를 넣어 별도 아군·적군 데이터를 만들지 않는다.
- 같은 archetype·Tier·Rank는 진영과 무관하게 같은 전투 결과를 낸다.
- `counter_tags`와 `target_priority_tags`는 C3 표시용 공용 전술 메타데이터이며 진영별로 복제하지 않는다.

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
