# 승인된 공용 병종 아키타입·진영 비주얼 데이터 계약 V1

- 상태: **아군·적군 공용 10병종 데이터 구조 승인 / 진영별 차이는 이미지 세트와 소유권·출격 방식으로 제한 / 정확한 Godot Resource 형태는 Plan Mode에서 확정**
- 작성일: 2026-07-16
- 적용 범위: 플레이어 유닛, 일반 적 웨이브 유닛, Tier·등급, 전투 능력, 애니메이션 상태·타이밍, 진영별 스프라이트·초상화·아이콘
- 연결 문서:
  - `APPROVED_PLAYER_TEN_UNIT_LINEAGES_POC_V1.md`
  - `APPROVED_SHARED_ARCHETYPE_WAVE_1_20_POC_V1.md`
  - `APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md`
  - `APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md`

## 1. 핵심 결정

오멘워드에는 전투 규칙 기준으로 **10개의 병종 아키타입만 존재한다.**

```text
아군 병종 데이터 10개
+
적군 병종 데이터 10개
```

처럼 별도 제작하지 않는다.

대신 다음 구조를 사용한다.

```text
공용 UnitArchetype 10개
+
아군 Visual Set
+
적군 Visual Set
+
런타임 소유 진영·출격 방식
```

- HP, 공격력, 방어, 사거리, 이동, 스킬, 패시브, 타기팅, Tier·등급 규칙은 공용 데이터 하나를 사용한다.
- 공격 준비·판정·회복 시간, 애니메이션 상태 ID와 이벤트 프레임도 공용 계약을 사용한다.
- 아군과 적군은 사용 이미지, 초상화, 아이콘, 팔레트와 진영 표시만 다르게 만든다.
- 첫 PoC에서는 진영별 VFX·오디오도 별도 복제하지 않고 공용 사용을 기본으로 한다.
- 적군은 룰렛을 사용하지 않고 웨이브와 생산시설을 통해 같은 아키타입을 출격시킨다.

## 2. 공용 10병종

| archetype_id 후보 | 공용 역할 | 아군 이미지·표시명 | 적군 이미지·표시명 후보 |
|---|---|---|---|
| `shield_guard` | 전열·원거리 대응 | 방패병 | 베일 갑각수 |
| `greatsword_warrior` | 정면 범위·파쇄 | 대검전사 | 균열도살자 |
| `assassin` | 같은 라인 후열 제거 | 암살자 | 그림자갈퀴 |
| `spearman` | 돌진·대형 저지 | 창병 | 가시창병 |
| `archer` | 지속 원거리·대공 | 궁병 | 침사수 |
| `cavalry` | 기동·돌진·후열 압박 | 기병 | 균열기수 |
| `priest` | 치유·전투 지원 | 사제 | 베일 표식자 |
| `mage` | 광역 마법·제어 | 마법사 | 공허주술사 |
| `flying_lancer` | 지상 전열 우회·후열 압박 | 비행병 | 베일익수 |
| `giant` | 대형 범위·방어·공성 | 거인 | 파성거체 |

표시명은 세계관과 로컬라이징을 위한 별칭이다. 별칭이 달라도 전투 데이터 ID를 새로 만들지 않는다.

## 3. 데이터 책임 구조

### UnitArchetypeProfile

진영과 무관한 공용 전투 원본이다.

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

### Tier·Rank 적용

```text
UnitArchetypeProfile
+ TierProfile
+ RankProfile
= 최종 전투 데이터
```

Tier와 등급 적용도 진영별 복사본을 만들지 않는다.

### FactionVisualProfile

진영별 이미지 원본이다.

```text
visual_faction_id
archetype_id
sprite_atlas_id
portrait_id
icon_id
palette_or_material_id
selection_marker_id
```

첫 PoC에서는 다음을 진영별로 분리하지 않는다.

- 공격 판정 시간.
- 프레임 수와 상태 순서.
- 스킬 규칙.
- VFX 이벤트 ID.
- 오디오 이벤트 ID.

실제 화면 검증에서 진영 판독이 부족할 때만 VFX·오디오 표현 override를 별도 승인한다.

### UnitInstance

런타임 개체는 데이터 복사본이 아니라 참조와 현재 상태를 가진다.

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

`owner_team_id`가 적대 관계, 점령 기여, 공격 대상을 결정한다. `visual_faction_id`는 표시 자산을 결정하며 능력치를 변경하지 않는다.

## 4. 아군과 적군의 차이

공유:

- 병종 능력치와 상성.
- 스킬·패시브와 타기팅 규칙.
- Tier·등급 적용.
- 공격·이동·피격·사망 상태.
- 애니메이션 프레임 수와 판정 이벤트.
- 점령력과 구조물 피해 규칙.

분리:

- 팀과 적대 관계.
- 룰렛·생산·웨이브 등 출격 경로.
- 배치 권한과 AI 명령 출처.
- 스프라이트·초상화·아이콘·팔레트.
- 세계관 표시명과 설명 문구.

일반 적군을 차별화하기 위해 별도 스탯, 스킬, AI 프로필을 만들지 않는다. 난이도와 위협은 다음으로 만든다.

- 웨이브 수량과 라인 편성.
- Tier·등급 조합.
- 출격 시점.
- 생산시설 상태.
- 보스 행동 패키지.

## 5. 애니메이션 제작 계약

10개 아키타입마다 하나의 공용 상태·타이밍 계약을 만든다.

```text
animation_contract_id
state_id
frame_count
playback_duration_or_fps
impact_frame
projectile_spawn_frame
cancel_window
recovery_duration
```

아군 이미지 세트와 적군 이미지 세트는 다음을 동일하게 유지한다.

- 상태 목록.
- 상태별 프레임 수.
- 프레임 배열 순서.
- 피벗과 기준선.
- 무기 접촉·투사체 발사 이벤트 프레임.
- 좌우 방향 규칙.

따라서 적군 10병종의 이동·공격 모션을 별도 기획하거나 별도 상태 머신으로 제작하지 않는다. 같은 모션 계약에 맞춘 다른 이미지 시트를 제작한다.

체형 차이 때문에 동일 프레임 계약을 지키기 어렵다면 이미지 디자인을 먼저 조정한다. 전투 규칙을 바꿀 정도의 예외는 사용자 승인 대상이다.

## 6. 웨이브 사용 방식

StageManifest와 WavePatternCard는 적군 전용 데이터 ID가 아니라 공용 `archetype_id`를 참조한다.

```text
wave_spawn_entry
- archetype_id
- tier
- rank
- count
- lane_id
- owner_team_id = enemy
- visual_faction_id = veil
- spawn_time
```

적 생산시설도 어떤 공용 archetype의 출격량을 제공·감소시키는지만 기록한다.

## 7. 보스 예외

W15 전설 보스와 W20 신화 보스는 일반 적군 아키타입 데이터 복사본을 만들지 않는다.

```text
공용 base_archetype_id
+
BossBehaviorPackage
+
BossPhaseProfile
+
전용 Visual Set
```

보스 패키지는 다음을 추가할 수 있다.

- 전용 패턴과 페이즈.
- 보스 제어 보정.
- 구조물 우선 행동.
- 보스 전용 체력·Threat 배율.
- 전용 이미지와 연출.

일반 웨이브 병종의 데이터 공유 원칙을 깨는 근거로 사용하지 않는다.

## 8. 데이터 검증

- 공용 아키타입 수가 정확히 10개인지 확인.
- 아군·적군별 별도 스탯·스킬 복사본이 없는지 확인.
- 모든 아키타입에 아군·적군 Visual Set이 존재하는지 확인.
- 두 Visual Set의 상태·프레임 수·피벗·이벤트 프레임이 일치하는지 확인.
- 웨이브가 유효한 공용 `archetype_id`만 참조하는지 확인.
- `visual_faction_id` 변경이 능력치를 변경하지 않는지 확인.
- 같은 아키타입·Tier·등급의 양 진영 유닛이 동일 입력에서 동일 피해·쿨다운 결과를 내는지 확인.
- 공용 수치 하나를 변경했을 때 양 진영에 함께 반영되는지 확인.

## 9. 금지 사항

- `EnemyUnitProfile`처럼 공용 데이터와 동일한 필드를 다시 가진 별도 적군 원본.
- 적군 이미지를 붙이기 위해 병종 코드와 Scene을 통째로 복제.
- 진영별 스탯·스킬·애니메이션 이벤트를 별도 파일에 복사.
- 표시명 차이를 데이터 ID 차이로 사용.
- 이미지 프레임 수가 달라 판정 이벤트가 어긋나는 상태.
- 웨이브 난이도를 숨은 적군 전용 능력치로 조정.

## 10. 수직 슬라이스 최소 검증

최소 두 공용 아키타입을 양 진영 이미지로 각각 생성한다.

1. 전열 인간형 또는 갑각형 이미지 세트.
2. 원거리 또는 지원 이미지 세트.
3. 가능하면 암살자·거인 중 하나의 특수 상태.

검증할 것:

- 같은 전투 데이터 사용.
- 다른 이미지와 팀 표시.
- 같은 공격 이벤트 타이밍.
- 적군 웨이브 출격과 아군 배치가 같은 아키타입을 생성.
- 별도 적군 병종 코드가 생기지 않음.

## 11. 변경 규칙

- 공용 10병종을 아군·적군 별도 데이터로 분리하는 변경은 사용자 승인 대상이다.
- 진영별 이미지·표시명 변경은 공용 전투 계약을 훼손하지 않는 범위에서 가능하다.
- 실제 검증으로 프레임 호환이 어려운 경우 Visual Set 규격을 조정하고, 전투 데이터 분리는 마지막 수단으로 검토한다.
- 신규 진영이 추가되어도 기존 아키타입 데이터 복제보다 새 Visual Set 추가를 우선한다.
