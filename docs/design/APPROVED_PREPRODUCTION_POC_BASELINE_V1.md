# 승인된 오멘워드 프리프로덕션 PoC 통합 기준 V1

- 상태: **프리프로덕션 구조 승인 / 기술 기준선 구현 / C1 승인 룰렛 핵심 계약 구현·원격 검증 진행**
- 작성일: 2026-07-16
- 최신 갱신일: 2026-07-22

이 문서는 구현이 뒤집히지 않도록 오멘워드의 승인 구조, 첫 PoC 가설, 책임 문서와 다음 실행 게이트를 통합한다. 최초 인수인계는 `docs/HANDOFF_CONTEXT.md`를 사용한다.

## 1. 완료된 프리프로덕션 범위

1. 핵심 루프와 첫 10분 경험.
2. 세계관·공식 명칭·벨루 단일 안내자.
3. 좌우 대칭 독립 3라인·성문·중간거점·접전지·암살자 우회.
4. 공용 10병종의 생산·Tier·등급·능력 계보.
5. 아군·적군 공용 전투 데이터와 진영별 이미지 세트 분리.
6. 룰렛 가중치·목표 확률·럭키·금화 기대값.
7. 공용 아키타입 기반 W1~20 웨이브와 보스 패키지.
8. 건물 Tier 3·경제·전술 명령·용병.
9. 튜토리얼·약 3시간 캠페인·절차 생성.
10. HUD·아트·애니메이션·오디오 제작 계약.
11. 성능 예산·데이터 구조·검증·Plan Mode 진입 조건.

## 2. 책임 문서

- 인수인계: `docs/HANDOFF_CONTEXT.md`
- 전체 기획: `docs/OMENWARD_GAME_DESIGN.md`
- 전장: `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`
- 공통 전투: `docs/design/APPROVED_COMMON_COMBAT_AND_RANK_BUDGET_POC_V1.md`
- 공용 병종 데이터·진영 이미지: `docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`
- 병종 능력 계보: `docs/design/APPROVED_PLAYER_TEN_UNIT_LINEAGES_POC_V1.md`
- 룰렛 핵심: `docs/design/APPROVED_ROULETTE_CORE_RULES.md`
- 룰렛 확률: `docs/design/APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md`
- C1 구현 증거: `docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md`
- W1~20 웨이브·보스: `docs/design/APPROVED_SHARED_ARCHETYPE_WAVE_1_20_POC_V1.md`
- 건물·전술·용병: `docs/design/APPROVED_BUILDINGS_TACTICAL_MERCENARY_POC_V1.md`
- 튜토리얼·캠페인·절차 생성: `docs/design/APPROVED_TUTORIAL_CAMPAIGN_PROCEDURAL_POC_V1.md`
- UI·오디오: `docs/design/APPROVED_UI_ART_AUDIO_POC_BIBLE_V1.md`
- 아트 제작: `docs/design/APPROVED_ART_DIRECTION_AND_PRODUCTION_GUIDE_V1.md`
- 애니메이션·전투 연출: `docs/design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md`
- 성능·데이터·테스트: `docs/design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md`
- 개발 순서: `docs/OMENWARD_ROADMAP.md`

## 3. 변경 시 사용자 승인이 필요한 구조

- 핵심 루프 `징조 → 건설·룰렛 → 배치 → 3라인 공방`.
- 좌우 대칭 독립 3라인.
- 라인별 성문 3개.
- 중간거점 전방 2·후방 1 건설 노드.
- 점령 시 건설권·기본 생산권 이전.
- 중앙 접전지의 라인 독립과 건설 금지.
- 암살자 같은 라인 안개 우회로와 후방 직접 생성 금지.
- 전장 전체 조망과 미니맵 미사용.
- 공용 UnitArchetype 10개.
- 아군·적군 전투 데이터 공유와 진영별 이미지 분리.
- 플레이어 등급 일반·엘리트·영웅·전설.
- 적 신화급은 W20 보스 패키지 전용.
- 병종별 이동·공격 역할과 판정 동기화.
- 한 주제당 활성 책임 원본 하나와 Plan Mode 승인 게이트.

## 4. 공용 병종 데이터 계약

```text
UnitArchetypeProfile × 10
+ TierProfile
+ RankProfile
+ owner_team_id
+ FactionVisualProfile
= UnitInstance
```

공유:

- 능력치, 스킬, 패시브, 타기팅.
- Tier·등급 적용.
- 점령·구조물 피해 규칙.
- 애니메이션 상태·프레임·판정 이벤트.

분리:

- 팀과 적대 관계.
- 룰렛·생산 또는 웨이브 출격.
- 스프라이트·초상화·아이콘·팔레트·표시명.

금지:

- 별도 `EnemyUnitProfile`.
- 진영별 스탯·스킬·애니메이션 타이밍 복사본.
- 적군 Scene에 공용 전투 규칙 중복.

일반 적군 위협은 수량, Tier, Rank, 라인, 출격 시점으로 만든다. 보스는 공용 base archetype에 BossBehaviorPackage와 전용 Visual Set을 추가한다.

## 5. 승인된 전장 초기값

### 중간거점

- 점령력 1.0 기준 중립화 10초 + 점령 10초.
- 유효 점령력 최대 2.0, 최소 완전 점령 10초.
- 소유 중간거점 한 곳당 금화 +2/30초.
- 점령 시도 중 생산·신규 건설·업그레이드 정지.
- 중립화 시 기존 건물 비활성.
- 점령 완료 시 기존 건물 폐허화, 환불 없음.
- 5초 안정화 뒤 새 소유자의 노드와 생산 활성.

### 성문

- HP 5,000, 방어 80, 마법저항 80.
- 일반 구조물 피해 40%, 공성 태그 200%, 고정 피해 50%.
- 0 HP 뒤 2초 붕괴.
- 수직 슬라이스에서는 자동 수리와 재건 없음.

### 암살자 우회

- 진입 준비 1초, 오프맵 이동 9초.
- 진입 확정 뒤 취소·후퇴 불가.
- 우회 중 전투·점령·피격·버프 없음.
- 적 중간거점 뒤 120 units의 160×120 도착 영역.
- 도착 2.5초 전 수비 경고, 출현 후 0.6초 준비.
- 암살자 점령력 0.
- 탐지 전용 건물은 수직 슬라이스 제외.

## 6. 애니메이션·연출 계약

공통 필수 상태:

```text
deploy / idle / move / attack_basic / skill_1 / hit_light / death / victory
```

- 공격은 준비→판정→회복으로 분리.
- 접촉·투사체 생성과 실제 판정 오차 한 프레임 이내.
- 이동 위치는 코드가 소유하고 루트 모션을 사용하지 않음.
- 한 아키타입의 공용 상태·프레임·이벤트 계약에 아군·적군 이미지 시트를 맞춤.
- 적군 전용 모션 상태 머신과 별도 타이밍 데이터 없음.
- 가벼운 연속 피격은 플래시·미세 반동.
- 스테이지 승리는 2.5~4초 병종별 승리 시퀀스 뒤 결과 UI.

일반 인간형 첫 가설:

```text
idle 4~6
move 6~8
attack_basic 6~10
skill_1 8~14
hit_light 2~3
death 6~10
victory 8~14 frames
```

## 7. 경제·공세 첫 기준

```text
시작 금화 160
시작 식량 12
기본 수입 +5 / 20초
중앙 접전지 +4 / 60초
중간거점 +2 / 30초
룰렛 20
```

- 60초마다 공세 충돌.
- W5 엘리트, W10 영웅, W15 전설 보스, W20 신화 보스.
- 적 일반 웨이브는 공용 10병종의 Tier·등급·수량·라인 조합.
- 적 처치·웨이브 클리어 고정 금화 없음.

## 8. 첫 구현에 사용할 수 있으나 조정 가능한 값

- 유닛 HP·공격력·방어·사거리·쿨다운.
- 생산시간·식량·Threat.
- 건물 비용과 Tier 3 효과.
- 룰렛 릴 가중치와 목표 분포.
- 웨이브 수량과 예산.
- 전술 명령 피해·지속.
- 성능 상한과 갱신 주기.
- 중간거점·성문·암살자 초기값.
- 최종 팔레트·캔버스·이미지 프레임.
- 애니메이션 FPS, 프레임 수, 이벤트 프레임.
- 카메라 흔들림·히트 스톱.

이 값은 플레이테스트와 측정 근거로 같은 승인 구조 안에서 변경할 수 있다.

## 9. 현재 기술·구현 경계

확인됨:

- Godot 4.7.1 Standard, Compatibility renderer.
- 960×540 논리 화면, 1920×1080 출력, viewport/keep/integer scale.
- 실제 Scene·Script·Resource·Test 경로.
- typed Resource·StageManifest·input log 경계.
- headless 테스트 명령과 GitHub Actions.

남은 결정·증거:

- C1 이동권·럭키 규칙 통합과 100,000시드 검증.
- 전투 목적 루프·코어 UX·사람 플레이.
- 최종 자산·VFX·오디오·성능 계측.

## 10. 현재 실행 게이트

```text
C0 프로젝트 코어·정본 복구 완료
→ [현재] C1 승인 룰렛 핵심 계약
→ C1U 이동권·럭키·분포
→ C2 전투 목적 루프
→ C3 코어 UX
→ C4 사람 플레이
```

- 현재 구현 근거는 `PROJECT_CORE.md`, `CURRENT_IMPLEMENTATION_STATUS.md`, 관련 APPROVED 문서와 실제 코드·테스트다.
- 과거 Work Order·Goal·Proposal은 활성 실행 입력으로 참조하지 않는다.
- 새로운 대형 시스템보다 잠긴 코어 인과의 구현·계측·검증을 우선한다.
