# Active Context

- 갱신일: 2026-07-16
- 공식명: **오멘워드 / OMENWARD**
- 상태: **프리프로덕션 구조 승인 완료 / 새 Codex 채팅용 Phase 0 Plan Mode 작업 패키지 준비 완료 / 게임 구현 전**
- 최초 인수인계: `docs/HANDOFF_CONTEXT.md`
- 현재 Codex 작업 요청: `docs/work_orders/0001-phase-0-codex-plan-mode.md`
- 사전 기술 추천안: `docs/design/proposals/0001-phase-0-godot-bootstrap.md`
- 최신 통합 기준: `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`
- 다음 작업: 새 Codex 채팅에서 Issue #1을 Plan Mode로 조사하고 Codex 제안서 제출

## 현재 상태 구분

```text
기획 승인 완료
→ Codex Work Order 준비 완료
→ [현재] 새 Codex 채팅 Plan Mode 실행 대기
→ Codex 제안서 제출
→ 사용자 검토·승인
→ Phase 0 구현
```

- 현재 Codex가 작성한 최종 Plan Mode 제안서는 아직 없다.
- `docs/design/proposals/0001-phase-0-godot-bootstrap.md`는 기획 측 사전 추천안이며 Codex가 검증할 입력이다.
- 사용자 승인 전 `project.godot`, Scene, GDScript, Resource, 데이터, 테스트, 브랜치와 PR을 만들지 않는다.

## 핵심 정체성

- 장르: 실시간 3라인 전략 오토배틀 + 건물 기반 3×3 룰렛 빌드.
- 핵심 루프: `베일의 징조 → 건물·토큰 선택 → 룰렛 → 라인 배치 → 거점·성문·우회 공방`.
- 플랫폼: Windows PC / 마우스·키보드 / 싱글플레이 PvE.
- 엔진: Godot + GDScript. 정확한 stable 버전은 Codex Plan Mode와 사용자 승인으로 결정한다.

## 전장 불변 구조

```text
아군 본진
→ 아군 성문
→ 아군 중간거점
→ 중앙 접전지
→ 적 중간거점
→ 적 성문
→ 적 본진
```

- 좌우 대칭, 상·중·하 독립 3라인.
- 라인 간 일반 횡단과 기본 라인 변경 없음.
- 라인별 성문 3개.
- 중간거점 전방 2·후방 1 건설 노드.
- 점령 시 건설권·기본 생산권 이전.
- 암살자는 적 후방 직접 생성이 아니라 같은 라인 안개 우회로 사용.
- 전장 전체를 기본 전략 화면에서 보며 미니맵 없음.

## 공용 병종 데이터 결정

```text
UnitArchetypeProfile 10개
+ TierProfile
+ RankProfile
+ owner_team_id
+ FactionVisualProfile
```

- 아군 10병종과 적군 10병종을 별도 전투 데이터로 만들지 않는다.
- HP·공격·스킬·패시브·타기팅·애니메이션 상태·판정 타이밍을 공유한다.
- 아군과 적군은 사용 이미지, 초상화, 아이콘, 팔레트, 표시명과 출격 방식만 다르다.
- 일반 적군 전용 `EnemyUnitProfile`, 별도 스탯·스킬·AI·모션 데이터 금지.
- 적 웨이브는 공용 `archetype_id`에 enemy 팀과 veil 이미지 세트를 지정한다.
- W15·W20 보스는 공용 아키타입에 BossBehaviorPackage·BossPhaseProfile·전용 Visual Set을 추가한다.

책임 원본:

- `docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`
- `docs/design/APPROVED_SHARED_ARCHETYPE_WAVE_1_20_POC_V1.md`

## 공용 10병종

- 기본 병영: 방패병, 대검전사, 암살자, 창병, 궁병, 기병.
- 특수병단: 사제, 마법사, 비행병, 거인.
- 플레이어 등급: 일반·엘리트·영웅·전설.
- 적 신화: W20 보스 패키지 전용.

## 승인된 전장 초기값

### 중간거점

```text
중립화 10초 + 점령 10초 at 점령력 1.0
최대 점령력 2.0
진행 유지 3초
복귀 초당 10%
안정화 5초
금화 +2 / 30초
```

- 점령 시도 중 생산·건설·업그레이드 정지.
- 중립화 시 건물 비활성.
- 점령 완료 시 건물 폐허화, 환불 없음.
- 안정화 후 새 소유자의 권한 활성.

### 성문

```text
HP 5000
방어·마법저항 80
일반 구조물 피해 40%
공성 200%
고정 피해 50%
붕괴 2초
```

- 세 라인 독립.
- 수직 슬라이스에서 수리·재건 없음.

### 암살자

```text
진입 1초
우회 이동 9초
도착 경고 2.5초 전
출현 준비 0.6초
적 중간거점 뒤 120 units
도착 영역 160 × 120
점령력 0
```

- 진입 후 취소·후퇴 불가.
- 우회 중 전투·피격·점령·버프 없음.
- 경로는 선택·배치 중에만 표시.

## 애니메이션·연출

공통 필수 상태:

```text
deploy / idle / move / attack_basic / skill_1 / hit_light / death / victory
```

- 공격은 준비→판정→회복.
- 접촉·투사체 발사와 실제 판정 오차 한 프레임 이내.
- 이동 위치는 코드가 소유, 루트 모션 사용 안 함.
- 한 아키타입의 공용 상태·프레임·이벤트 계약에 아군·적군 이미지 시트를 맞춘다.
- 적군 전용 모션 기획과 상태 머신을 별도 제작하지 않는다.
- 스테이지 승리 연출은 2.5~4초 뒤 결과 UI로 연결한다.

책임 원본: `docs/design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md`

## 경제·공세

```text
시작 금화 160
시작 식량 12
기본 수입 +5 / 20초
중앙 접전지 +4 / 60초
중간거점 +2 / 30초
룰렛 20
```

- 활성 전투 시간 기준 60초 공세.
- W5 엘리트, W10 영웅, W15 전설 보스, W20 신화 보스.
- 적 일반 웨이브는 공용 10병종의 Tier·등급·수량·라인 조합.

## 새 Codex 채팅 실행 순서

1. 새 Codex 채팅을 연다.
2. `docs/work_orders/0001-phase-0-codex-plan-mode.md`의 시작 프롬프트를 전달한다.
3. Codex는 Plan Mode로 저장소·Base·urban-legend·공식 근거를 읽기 전용 조사한다.
4. Codex는 `docs/PROPOSAL_WORKFLOW.md` 형식의 Phase 0 제안서를 제출한다.
5. 사용자가 수정 또는 승인한다.
6. 승인된 뒤에만 별도 구현 실행에서 Phase 0 브랜치·PR을 만든다.
7. Phase 0 완료 뒤 Issue #32 수직 슬라이스 Plan Mode로 이동한다.

## 구현 경계

- 현재 Godot 코드, Scene, Resource, 테스트는 구현 전이다.
- 새 Codex 채팅의 첫 실행은 계획 작성이며 구현이 아니다.
- Issue #1과 #32 모두 사용자 명시적 승인 전 구현 금지.
- 새로운 대형 시스템보다 승인된 구조의 데이터화·구현·계측이 우선이다.
- Base 공용 지식은 작업 방법과 사례 참고용이며 프로젝트 책임 문서를 덮어쓰지 않는다.
