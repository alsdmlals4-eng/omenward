# 승인된 성능·데이터·테스트·Plan Mode 준비 PoC V1

- 상태: **성능 예산·데이터 경계·검증 절차 승인 / 정확한 엔진 설정은 구현 Plan Mode에서 확정**
- 작성일: 2026-07-16
- 구현 경계: 이 문서는 구현 준비 기준이며 코드 작성 승인 자체가 아니다.

## 1. 목표 환경

- Windows PC.
- 1920×1080 출력.
- 목표 60fps, 프레임타임 16.7ms.
- 최소 허용 30fps는 디버그·저사양 안전선이며 출시 목표가 아니다.
- 정확한 Godot stable 버전은 구현 시작 시 공식 stable 중 하나를 고정한다.

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

- 하드 상한에 접근하면 소형 군집을 묶음 표현하거나 투사체를 히트스캔형으로 대체한다.
- 게임 규칙상 유닛을 임의 삭제하지 않는다.

## 3. 업데이트 빈도 예산

- 물리 이동·충돌: 엔진 물리 틱 기준.
- 타깃 재탐색: 일반 0.25초, 후열 우선 병종 0.15초.
- 오라 대상 갱신: 0.25초.
- 독·출혈·회복: 0.5초 또는 1초 틱.
- 점령 판정: 0.2초.
- UI 숫자 갱신: 최대 초당 10회.
- 경로는 고정 라인 포인트열을 사용하고 실시간 전역 내비게이션 재탐색을 피한다.

## 4. 결정론적 시간

세 시간축을 분리한다.

```text
real_time
active_combat_time
ui_planning_time
```

- 웨이브, 건설, 업그레이드, 생산, 준비 할인, 수입, 쿨다운은 active_combat_time을 사용한다.
- 일시정지 중 계획 입력과 UI는 동작하지만 active_combat_time은 증가하지 않는다.
- 시드·Manifest·입력 로그로 주요 전투를 재현할 수 있어야 한다.

## 5. 데이터 리소스 경계

### UnitProfile

```text
unit_family_id
variant_id
tier
rank
faction
movement_layer
role_tags
food_cost
hp
armor
magic_resistance
move_speed
attack_profile_id
passive_ids
skill_ids
targeting_profile_id
threat_cost
visual_profile_id
audio_profile_id
```

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
```

### StageManifest

`APPROVED_TUTORIAL_CAMPAIGN_PROCEDURAL_POC_V1.md`의 필드를 사용한다.

### RankProfile

```text
rank_id
hp_multiplier
damage_multiplier
threat_multiplier
skill_unlock_count
visual_grade_id
```

## 6. 상태 머신

### 건물

```text
Planned
→ Constructing
→ Active
→ Upgrading
→ Active
→ Ruins
```

- 취소는 Constructing/Upgrading에서만 가능하다.
- 특수병단 Tier 1은 Active 상태에서 준비도를 축적한다.
- 파괴 시 생산·준비·토큰 제거 규칙을 데이터 이벤트로 처리한다.

### 생산

```text
Idle
→ Producing
→ ReadyWaitingFood
→ Delivered
→ Producing
```

### 유닛

```text
Reserve
→ Deployed
→ Moving
→ Engaged
→ Casting
→ Recovering
→ Dead
```

- 병종별 특수 상태는 공통 상태를 대체하지 않고 태그·서브상태로 둔다.

## 7. 자동 검증 목록

### 데이터
- 모든 참조 ID 존재.
- 플레이어 신화급 결과 없음.
- 자동생산 결과는 일반 등급.
- 각 계열에 일반·엘리트·영웅·전설 템플릿 존재.
- 모든 스킬 전조와 판정 범위 존재.

### 경제
- 15분 기본 수입 계산.
- 시장 회수시간.
- 특수병단 0~50% 할인 단계.
- 취소·철거 환불.
- 식량 부족 완성 대기.

### 룰렛
- 최소 100,000시드 분포.
- 전설 1회 제한.
- 금화 EV 30% 이하.
- 럭키 6회 실패 확정.
- 건물 파괴 뒤 다음 회전 토큰 제거.

### 전투
- 동일 시드 동일 결과.
- 방어·저항·고정 피해 계산.
- 보스 연속 제어 면역.
- 비행·대공 타기팅.
- 암살자 라인 이탈 금지.
- 거인 비행 공격 불가.

### 웨이브
- 60초 충돌 시계.
- 5·10·15·20 이정표.
- 시설 파괴 공세 감소.
- 안전 Manifest 대체.
- 성능 하드 상한 초과 여부.

## 8. 플레이테스트 계측

- 첫 건물 건설 시간.
- 첫 룰렛과 첫 보상 시간.
- 웨이브별 남은 적 Threat.
- 라인별 병력·건물 투자.
- 금화 수입원·지출원 비율.
- 식량 부족 시간.
- 병종별 생산·배치·사망·피해·치유·지원량.
- 전술 명령 사용 시점과 효율.
- 보스 전투시간.
- 패배 직전 60초의 결정 로그.

## 9. Plan Mode 진입 조건

다음 조건을 모두 충족해야 수직 슬라이스 구현 Plan Mode 제안서를 작성한다.

1. 활성 책임 문서가 최신 10병종 구조와 일치.
2. 레거시 깃발병·대검병·광전사 독립 구조가 로드맵과 GDD에서 제거.
3. 공통 전투·등급·룰렛·경제·웨이브·UI 데이터 필드가 정의됨.
4. 튜토리얼 Manifest와 정규 안전 Manifest 초안 존재.
5. Godot 버전·폴더 구조·테스트 러너를 Plan Mode에서 선택할 수 있음.
6. 구현 범위를 튜토리얼 수직 슬라이스로 제한.

## 10. 첫 구현 범위 권장

구현 승인 후 첫 수직 슬라이스는 다음만 포함한다.

- 한 맵, 3라인.
- 기본 병영과 방패병·대검전사·암살자.
- 특수병단은 사제단 하나만 우선 블록아웃 가능.
- 3×3 룰렛과 일반·엘리트.
- 첫 네 공세.
- 포탑·바리케이드.
- 벨루 HUD 더미.

영웅·전설·절차 생성·전체 10병종은 데이터와 인터페이스만 고려하고 첫 구현 범위에서는 단계적으로 추가한다.

## 11. 실패 기준

- 문서에 없는 하드코딩 수치가 핵심 규칙을 결정.
- 일시정지 중 전투 시간이 일부 진행.
- 룰렛·웨이브 결과가 시드로 재현되지 않음.
- 동일 계열 Tier·등급 비교가 데이터가 아니라 별도 코드 분기로 처리됨.
- 최대 객체 상한에서 30fps 아래로 장시간 하락.
- 전조와 판정이 플레이어가 인지할 정도로 불일치.
