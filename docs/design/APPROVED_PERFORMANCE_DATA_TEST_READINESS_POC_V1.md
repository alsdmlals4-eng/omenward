# 승인된 성능·데이터·테스트·Plan Mode 준비 PoC V1

- 상태: **성능 예산·공용 병종 데이터 경계·검증 절차 승인 / 정확한 엔진 설정과 파일 구조는 Plan Mode에서 확정**
- 작성일: 2026-07-16
- 최신 갱신일: 2026-07-16
- 구현 경계: 이 문서는 구현 준비 기준이며 코드 작성 승인 자체가 아니다.
- 연결:
  - `APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`
  - `APPROVED_SHARED_ARCHETYPE_WAVE_1_20_POC_V1.md`
  - `APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md`

## 1. 목표 환경

- Windows PC.
- 1920×1080 출력.
- 내부 960×540 정수 확대 후보.
- 목표 60fps, 프레임타임 16.7ms.
- 30fps는 디버그·저사양 안전선이며 출시 목표가 아니다.
- 정확한 Godot stable 버전은 Issue #1 Plan Mode에서 공식 stable 중 하나를 비교해 고정한다.

## 2. 동시 객체 예산

| 범주 | 정상 목표 | 하드 안전 상한 |
|---|---:|---:|
| 지상 유닛 | 120 | 180 |
| 비행 유닛 | 24 | 40 |
| 보스·거인급 대형 | 8 | 16 |
| 활성 투사체 | 160 | 260 |
| 지속 장판 | 20 | 32 |
| 활성 오라 | 24 | 40 |
| 동시 VFX 인스턴스 | 80 | 140 |
| 전장 건물 | 36 | 48 |

- 하드 상한에 접근하면 소형 군집의 표현 단위를 묶거나 일부 투사체를 히트스캔형으로 단순화한다.
- 게임 규칙상 이미 출격한 유닛을 성능 때문에 임의 삭제하지 않는다.
- 공용 Unit Scene과 UnitArchetype 재사용으로 진영별 Scene·Script·Resource 복제를 막는다.

## 3. 업데이트 빈도 예산

- 물리 이동·충돌: 엔진 물리 틱.
- 타깃 재탐색: 일반 0.25초, 후열 우선 0.15초 첫 가설.
- 오라 대상 갱신: 0.25초.
- 독·출혈·회복: 0.5초 또는 1초 틱.
- 점령 판정: 0.2초.
- UI 숫자: 최대 초당 10회.
- 웨이브·경제·건설: 이벤트와 낮은 주기 갱신.
- 경로는 고정 라인 포인트열을 사용하고 전역 내비게이션 재탐색을 피한다.
- 애니메이션은 프레임 단위로 재생하되 타기팅과 규칙 계산을 매 프레임 반복하지 않는다.

## 4. 결정론적 시간

세 시간축을 분리한다.

```text
real_time
active_combat_time
ui_planning_time
```

- 웨이브, 건설, 업그레이드, 생산, 준비 할인, 수입, 공격·스킬 쿨다운과 암살자 우회 이동은 active_combat_time을 사용한다.
- 일시정지 중 계획 입력과 UI는 동작하지만 active_combat_time은 증가하지 않는다.
- 시드, StageManifest와 입력 로그로 주요 전투를 재현한다.
- 같은 시드에서 대기·이동·승리 모션의 결정론적 프레임 오프셋도 재현한다.
- 히트 스톱이 도입되면 시뮬레이션 시간과 시각 표현 시간을 분리하는 방식을 Plan Mode에서 명시한다.

## 5. 공용 병종 데이터 경계

### UnitArchetypeProfile

전투 규칙의 공용 원본이며 정확히 10개를 사용한다.

```text
archetype_id
role_tags
movement_layer
food_cost
base_hp
armor
magic_resistance
move_speed
attack_profile_id
passive_ids
skill_ids
targeting_profile_id
capture_power
structure_damage_tags
animation_contract_id
threat_cost
```

포함하지 않는 필드:

```text
faction
enemy_only_stats
enemy_skill_ids
enemy_animation_id
```

- 아군과 적군은 같은 UnitArchetypeProfile을 사용한다.
- 표시명·이미지 차이를 이유로 새 archetype ID를 만들지 않는다.
- 같은 archetype·Tier·Rank는 진영과 무관하게 같은 능력치·스킬·판정 결과를 낸다.

### TierProfile

```text
tier_id
production_time_multiplier
food_cost_modifier
stat_modifiers
passive_unlocks
specialization_options
```

- 아군·적군 공용.
- 웨이브가 진행됐다는 이유만으로 숨은 적군 전용 Tier 배율을 적용하지 않는다.

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
- 신화는 일반 Rank가 아니라 W20 보스 행동·페이즈 패키지다.

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

- 아군과 베일종 이미지·초상화·아이콘·팔레트를 분리한다.
- 능력치, 스킬, 타기팅, 공격속도와 애니메이션 이벤트를 변경하지 않는다.
- 첫 PoC에서는 진영별 VFX·오디오 override를 두지 않는 것을 기본으로 한다.

### AnimationContract

```text
animation_contract_id
states[]
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

- 같은 archetype의 아군·적군 Visual Set이 공유한다.
- 상태 목록, 프레임 수, 배열, 피벗과 이벤트 프레임이 일치해야 한다.
- 피해량·공격 주기·범위의 원본이 아니라 표현 동기화 계약이다.

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

- 런타임 상태와 참조만 가진다.
- 프로필 전체를 인스턴스에 복사해 진영별로 수정하지 않는다.

### AttackProfile

```text
attack_profile_id
damage_type
base_damage
attack_interval
range
area_shape
max_targets
structure_damage_rule
impact_event_id
projectile_profile_id?
```

- 실제 판정 규칙을 소유한다.
- AnimationContract 이벤트와 한 프레임 이내로 동기화한다.

### BuildingProfile

```text
building_family_id
tier
specialization_id
gold_cost
construction_time
max_hp
production_profile_id
token_contribution
upgrade_options
income_profile_id
aura_profile_ids
visual_state_profile_id
ownership_requirement
```

### BattlefieldProfile

```text
lane_ids
base_ids
gate_profiles
mid_strongpoint_profiles
clash_point_profiles
build_nodes
lane_paths
assassin_bypass_profiles
world_scale
```

### StageManifest

```text
stage_id
seed
wave_schedule
telegraph_entries
spawn_entries[]
  archetype_id
  tier
  rank
  count
  lane_id
  spawn_time
  owner_team_id
  visual_faction_id
boss_package_id?
production_facility_links
```

- 일반 적 웨이브에 별도 HP·공격력·스킬 필드를 넣지 않는다.
- `archetype_id`와 공용 Tier·Rank를 참조한다.

### BossBehaviorPackage / BossPhaseProfile

- 공용 base archetype에 보스 패턴·페이즈·보정과 전용 Visual Set을 추가한다.
- 일반 적군 UnitArchetype 복사본을 만들지 않는다.

## 6. 상태 머신 후보

### 건물

```text
Planned
→ Constructing
→ Active
→ Upgrading
→ Active
→ Inactive
→ Ruins
```

- 취소는 Constructing/Upgrading에서만 가능.
- 특수병단 Tier 1은 Active에서 준비도 축적.
- 중간거점 중립화 시 Inactive, 적 점령 완료 시 Ruins.
- 파괴·비활성 시 생산·준비·토큰 제거를 데이터 이벤트로 처리한다.

### 생산

```text
Idle
→ Producing
→ ReadyWaitingFood
→ Delivered
→ Producing
```

### 유닛 런타임

```text
Reserve
→ Deploying
→ Moving
→ Engaged
→ Casting
→ Recovering
→ Dead
```

역할별 행동 상태:

- 암살자: BypassEntering → BypassTravel → BypassExiting.
- 기병: Charging → TurnRecover.
- 비행병: Cruising → Diving → AirRecover.
- 거인: StructureAttacking → HeavyRecover.

- 아군과 적군이 같은 런타임 상태와 행동 코드를 사용한다.
- 특수 상태는 진영별 별도 클래스가 아니라 공용 아키타입의 행동 계약이다.

## 7. 자동 검증 목록

### 공용 병종 데이터

- UnitArchetypeProfile 수가 정확히 10개.
- 별도 `EnemyUnitProfile` 없음.
- 진영별 HP·공격·스킬·타기팅·AnimationContract 복사본 없음.
- 모든 archetype에 아군·적군 FactionVisualProfile 존재.
- 양 Visual Set의 필수 상태, 프레임 수, 피벗과 이벤트 프레임 일치.
- `visual_faction_id` 변경이 능력치와 스킬 결과를 변경하지 않음.
- 같은 archetype·Tier·Rank의 양 진영 유닛이 동일 입력에서 같은 피해·쿨다운 결과를 냄.
- 공용 수치 하나를 바꾸면 양 진영에 함께 반영됨.
- 플레이어 신화 Rank 없음.
- 자동생산 결과는 일반 Rank.

### 애니메이션·전투

- 모든 AttackProfile에 대응하는 impact 또는 projectile event 존재.
- 실제 판정과 접촉·발사 이벤트 오차 한 프레임 이내.
- 판정 전 취소와 판정 후 취소 결과가 정의됨.
- 누락된 Visual Set 상태를 조용히 대체하지 않고 실패 처리.
- 가벼운 피격이 공격 이벤트를 계속 중단하지 않음.
- 동일 시드의 시각 오프셋 재현.
- 방어·저항·고정 피해 계산.
- 비행·대공 타기팅.
- 암살자 라인 이탈·직접 후방 생성 금지.
- 거인의 비행 공격 금지.
- 보스 연속 제어 면역.

### 전장

- 상·중·하 일반 이동 그래프가 서로 연결되지 않음.
- 라인별 양 진영 성문 6개.
- 양 진영·라인별 중간거점과 전방 2·후방 1 노드.
- 중앙 접전지 건설 금지.
- 건물 점유 영역이 주 도로를 막지 않음.
- 암살자만 우회로 사용.
- 중간거점 상태 전환과 건설·생산권 이전.
- 성문 독립 HP·붕괴·통로 개방.

### 경제

- 15분 기본 수입.
- 시장 회수시간.
- 접전지·중간거점 수입.
- 특수병단 0~50% 할인.
- 취소·철거 환불.
- 식량 부족 완성 대기.
- 점령 중 거점 생산 정지와 안정화 뒤 재개.

### 룰렛

- 최소 100,000시드 분포.
- 전설 1회 제한.
- 금화 EV 30% 이하.
- 럭키 6회 실패 뒤 확정.
- 건물 파괴·비활성 후 다음 회전 토큰 제거.
- 룰렛 결과가 공용 archetype ID를 생성.

### 웨이브

- 모든 일반 spawn entry가 공용 10개 archetype만 참조.
- 60초 충돌 시계.
- W5·W10·W15·W20 이정표.
- 시설 파괴로 예약 공세 감소.
- 보스가 base archetype + BossBehaviorPackage로 구성됨.
- 안전 Manifest 대체.
- 성능 하드 상한 초과 여부.

### 문서·참조

- Documentation Map의 책임 경로가 존재.
- 폐기된 적군 전용 병종 문서를 활성 문서가 참조하지 않음.
- Handoff, GDD, Roadmap, Goal과 Issue가 같은 데이터 소유 구조를 설명함.

## 8. 플레이테스트 계측

- 첫 건물 건설 시간.
- 첫 룰렛과 첫 보상 시간.
- 웨이브별 남은 Threat.
- 라인별 병력·건물 투자.
- 금화 수입원·지출원 비율.
- 식량 부족 시간.
- archetype별 생산·배치·사망·피해·치유·지원량.
- 팀별 같은 archetype 성능 차이 여부.
- 중간거점 점령 시간·보유 시간·수입.
- 성문 생존·붕괴 시간.
- 암살자 우회 성공률·도착 후 생존·후열 피해.
- 공격 이벤트와 시각 접촉 오차.
- 전술 명령 사용 시점과 효율.
- 보스 전투시간.
- 패배 직전 60초 결정 로그.

## 9. 현재 기술 기준선

확인된 구조:

1. Godot 4.7.1 프로젝트와 main Scene.
2. 공용 10병종·양 진영 Visual·AnimationContract.
3. 결정론·StageManifest·input log·DataRegistry.
4. 실제 Scene·Script·Resource·Test 경로.
5. headless 테스트와 CI.

## 10. C1 원격 검증 결과

GitHub Actions run `29919925777`에서 Godot 4.7.1 editor import·전체 headless·runtime smoke와 4환경 계약 검증을 통과했다.

검증 조건:

1. 중앙 판정 줄이 실패하면 다른 완성선을 무시한다.
2. 1/2/3~7/8줄 등급이 정확하다.
3. X는 보상하지 않고 금화는 75%/200%/500%를 지급한다.
4. 기본 병영만 유닛 토큰을 제공한다.
5. 같은 시드·건물 스냅샷·최종 보드가 같은 결과를 만든다.
6. 결과 보관 중 다음 회전만 차단하고 라인 배치가 가능하다.
7. 모든 기존 headless 테스트와 editor import가 통과한다.

## 11. 첫 수직 슬라이스 권장 범위

- 한 맵, 3라인.
- 성문·중간거점·접전지.
- 최소 건물 2종.
- 최소 3×3 룰렛과 일반·엘리트.
- 첫 네 공세.
- 공용 archetype 대표 3~5종.
- 각 대표 archetype의 아군·적군 이미지 세트.
- 암살자 우회 또는 공성 역할 포함.
- deploy, idle, move, attack, hit, death, victory.
- 포탑·바리케이드.
- 벨루 HUD 더미.

전체 10병종·영웅·전설·절차 생성·최종 자산은 인터페이스만 고려하고 단계적으로 추가한다.

## 12. 실패 기준

- 적군용 별도 UnitProfile·스탯·스킬·타기팅 데이터가 생성됨.
- 아군 Unit Scene을 복사한 Enemy Unit Scene이 같은 규칙을 중복 소유.
- Visual Set 변경이 능력치나 쿨다운을 변경.
- 양 진영 이미지의 프레임·피벗·이벤트가 어긋남.
- 문서에 없는 하드코딩 수치가 핵심 규칙을 결정.
- 일시정지 중 active_combat_time이 진행.
- 룰렛·웨이브·전투가 시드로 재현되지 않음.
- Tier·Rank 비교가 데이터가 아니라 진영별 코드 분기로 처리됨.
- 최대 객체 상한에서 30fps 아래로 장시간 하락.
- 전조와 판정, 공격 모션과 실제 피해가 인지 가능한 수준으로 불일치.
- Handoff·GDD·Roadmap·Issue가 서로 다른 데이터 구조를 설명함.
