# OMENWARD 프로젝트 인수인계 컨텍스트

- 갱신일: 2026-07-22
- 현재 상태: **기술 기준선 구현 / 핵심 수직 슬라이스 부분 구현 / 코어 루프·사람 플레이 미검증**
- 프로젝트 코어: `docs/PROJECT_CORE.md` (`CORE_CONFIRMED` / `CORE_LOCKED`)
- 실제 구현 상태: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- 전체 기획: `docs/OMENWARD_GAME_DESIGN.md`
- 개발 순서: `docs/OMENWARD_ROADMAP.md`
- 최신 상태: `docs/ACTIVE_CONTEXT.md`
- 시각자료: `docs/images/VISUAL_REFERENCE_INDEX.md`
- 병종 월드 스프라이트 형식: `docs/design/APPROVED_UNIT_VISUAL_FORMAT_AND_REFERENCE_USE_V1.md`

이 문서는 새 ChatGPT, Codex, 기획자, 아티스트와 개발자가 이전 대화 없이도 제품 방향, 불변 조건, 데이터 책임, 시각 기준과 다음 조사 순서를 이해하기 위한 출발점이다. 세부 수치와 구현 완료 여부는 링크된 책임 원본과 실제 파일·테스트를 따른다.

## 1. 가장 먼저 알아야 할 것

1. 오멘워드는 건물로 룰렛의 토큰·확률과 증원 체계를 설계하고 세 전선을 지휘하는 판타지 전략 오토배틀 게임이다.
2. 저장소에는 Phase 0 기술 기준선과 수직 슬라이스 구성요소가 존재하지만 승인 룰렛·전투 목적·코어 UX는 미완결이다.
3. 과거 Phase 0 Work Order의 `구현 전`과 README의 과도한 `수직 슬라이스 완료`를 현재 상태로 재사용하지 않는다.
4. 새 Codex 채팅은 `PROJECT_CORE.md`, `CURRENT_IMPLEMENTATION_STATUS.md`, 실제 main, validation 문서와 Issue·PR을 대조한 뒤 다음 최소 변경을 제안한다.
5. 아군과 적군은 별도 병종 전투 데이터를 만들지 않고 공용 10병종에 서로 다른 FactionVisualProfile을 연결한다.
6. 병종 이미지는 첫 번째 전장 UI 이미지의 **실제 전장 삽입형 소형 고해상도 픽셀 스프라이트 형식**을 따른다.
7. 두 번째 10병종×등급 도감표는 병종 목록과 등급 위계 참고만 유지하며 실제 스프라이트 형식으로 사용하지 않는다.
8. 이미지의 임시 수치·문구·맵 구조와 미니맵 형태는 승인 사양이 아니다.
9. 시각자료의 승인·부분 참고·폐기 상태는 `docs/images/VISUAL_REFERENCE_INDEX.md`에서 확인한다.
10. 사용자가 새 이미지를 제공하면 저장·인덱스·해석·문서 연결을 같은 작업에서 처리한다.

## 2. 최초 읽기 순서

```text
1. 최신 사용자 지시
2. AGENTS.md
3. docs/BASE_RULES_VERSION.md
4. docs/PROJECT_CORE.md
5. docs/CURRENT_IMPLEMENTATION_STATUS.md
6. docs/HANDOFF_CONTEXT.md
7. docs/DOCUMENTATION_MAP.md
8. 현재 작업의 work_orders 문서
9. docs/OMENWARD_GAME_DESIGN.md
10. 관련 APPROVED 책임 문서
11. 시각 작업이면 docs/images/VISUAL_REFERENCE_INDEX.md
12. docs/OMENWARD_ROADMAP.md
13. 현재 Issue / Goal / 승인 제안서
14. project.godot, Scene, scripts, data, tests
15. validation 문서와 실제 실행 결과
16. docs/ACTIVE_CONTEXT.md
```

저장소 조사 순서:

```text
project.godot
→ scenes/main/main.tscn
→ scripts/
→ data/
→ tests/
→ docs/PHASE_0_VALIDATION.md
→ docs/VERTICAL_SLICE_VALIDATION.md
→ 최신 Issue·PR·커밋
```

## 3. 제품 약속

### 한 문장

> 예고된 세 전선의 위협을 읽고, 제한된 건물 노드로 룰렛 확률을 설계한 뒤, 당첨된 증원을 어느 전선에 투입할지 결정해 전황을 뒤집는 실시간 전략 오토배틀 게임.

### 핵심 루프

```text
베일의 징조 확인
→ 건물·토큰·전술 선택
→ 3×3 룰렛
→ 병력 획득·라인 배치
→ 3라인 교전
→ 접전지·중간거점 공방
→ 암살자 우회 또는 성문 공성
→ 다음 공세 준비
```

### 첫 10분 약속

- 세계관과 전선 위기를 짧게 이해한다.
- 건설→룰렛→배치→역전을 두 번 체험한다.
- 이동권과 상위 등급의 강함을 체감한다.
- 방패병·대검전사·암살자 중 첫 전문화를 선택한다.
- 설명보다 행동과 즉시 반응으로 시스템을 학습한다.

## 3.1 현재 구현 판정

- 프로젝트 코어 책임 원본: `docs/PROJECT_CORE.md`
- 구현 증거 책임 원본: `docs/CURRENT_IMPLEMENTATION_STATUS.md`

```text
TECHNICAL_BASELINE_IMPLEMENTED
+ CORE_VERTICAL_SLICE_PARTIAL
+ CORE_LOOP_NOT_PROVEN
+ HUMAN_QA_NOT_RUN
```

현재 Godot 프로젝트는 기술·데이터 그레이박스와 여러 수직 슬라이스 구성요소를 포함한다. 그러나 승인 룰렛 판정, 전투 상태 기반 승패, 접전지·거점·성문 연결과 승인 UX 6종이 닫히지 않았으므로 “핵심 수직 슬라이스 완료”로 부르지 않는다.

다음 순서는 정본 복구 뒤 승인 룰렛 계약, 전투 목적 루프, 코어 UX, 사람 플레이 검증이다.

## 4. 전장 불변 구조

```text
아군 본진
→ 라인별 아군 성문
→ 아군 중간거점
→ 중앙 접전지
→ 적 중간거점
→ 라인별 적 성문
→ 적 본진
```

- 좌우 대칭 독립 상·중·하 3라인.
- 일반 유닛의 라인 간 횡단과 기본 라인 변경 없음.
- 각 라인에 독립 성문 1개, 진영당 총 3개.
- 각 중간거점에 전방 건설 노드 2개와 후방 노드 1개.
- 중간거점 점령 시 건설권과 기본 생산권 이전.
- 중앙 접전지는 다른 라인과 연결되지 않으며 건설 불가.
- 암살자는 적 후방 직접 배치가 아니라 같은 라인의 안개 우회로 사용.
- 전장을 기본 전략 화면에서 보므로 미니맵 없음.

책임 원본: `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`

## 5. 공용 병종 데이터

```text
UnitArchetypeProfile × 10
+ TierProfile
+ RankProfile
+ owner_team_id
+ FactionVisualProfile
```

- 전투 규칙 기준 병종은 공용 아키타입 10개뿐이다.
- 같은 아키타입·Tier·Rank는 진영과 관계없이 같은 능력치, 스킬, 타기팅, 점령력, 구조물 피해와 AnimationContract를 사용한다.
- 차이는 소유 팀, 출격 방식, 스프라이트·초상화·아이콘·팔레트와 표시명이다.
- 일반 적군 전용 `EnemyUnitProfile`, 별도 Unit Scene, 스탯·스킬·모션 계약을 만들지 않는다.
- 일반 적군 난이도는 수량, Tier, Rank, 라인 편성, 출격 시점으로 만든다.
- W15·W20 보스는 공용 아키타입에 BossBehaviorPackage·BossPhaseProfile과 전용 Visual Set을 추가한다.

책임 원본:

- `docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`
- `docs/design/APPROVED_SHARED_ARCHETYPE_WAVE_1_20_POC_V1.md`

## 6. 공용 10병종

### 기본 병영

- 방패병 — 전열·원거리 대응.
- 대검전사 — 정면 범위·파쇄.
- 암살자 — 안개 우회로와 후열 제거.
- 창병 — 돌진·대형 저지.
- 궁병 — 지속 원거리·대공.
- 기병 — 기동·돌진·후열 압박.

### 특수병단

- 사제 — 치유·전투 지원.
- 마법사 — 광역 마법·제어.
- 비행병 — 지상 전열 우회·후열 압박.
- 거인 — 대형 범위·방어·공성.

- 플레이어 등급은 일반·엘리트·영웅·전설.
- 플레이어 신화급은 없다.
- 적 신화는 W20 보스 패키지 전용이다.

## 7. 최신 병종 비주얼 계약

### 실제 제작 형식

병종의 기준 이미지는 전장 UI 시안 안에서 전투 중인 소형 픽셀 유닛이다.

```text
실제 전장 삽입형 월드 스프라이트
+ 약 2.5~3등신 전술 미니어처
+ 일반 인간형 34~40px 첫 표시 높이
+ 무기·자세·몸통 덩어리 우선
+ 제한된 고해상도 픽셀 재질 표현
```

- 얼굴과 장식보다 병종 실루엣과 공격 방향을 먼저 읽는다.
- 밝고 어두운 전장 모두에서 외곽선이 읽혀야 한다.
- 아군과 적군은 동일한 상태·프레임·피벗·공격 이벤트 계약을 공유한다.
- 진영은 팔레트뿐 아니라 장비·소재·외곽 형태와 생물 기관으로 구분한다.
- 일반→엘리트→영웅→전설은 단순 확대가 아니라 기능적인 무기, 자세, 실루엣 부속과 제한적 VFX로 위계를 만든다.

### 과거 도감표

두 번째 도감표는 다음에만 사용한다.

- 10병종의 관계를 한눈에 비교.
- 같은 병종의 일반·엘리트·영웅·전설 상승 관계.
- 상위 등급에서 무기와 역할 실루엣이 강화되는 방향.

도감표의 큰 전신 캐릭터 비율, 렌더링 밀도와 세부 디자인은 월드 스프라이트 기준이 아니다.

책임 원본:

- `docs/design/APPROVED_UNIT_VISUAL_FORMAT_AND_REFERENCE_USE_V1.md`
- `docs/images/VISUAL_REFERENCE_INDEX.md`
- `docs/design/APPROVED_ART_DIRECTION_AND_PRODUCTION_GUIDE_V1.md`

## 8. 참고 이미지 사용 경계

첫 번째 전장 UI 이미지에서 참고할 것:

- 전장에 배치된 유닛의 크기와 픽셀 디테일 균형.
- 무기·자세·덩어리로 병종을 구분하는 방식.
- 아군·적군의 색·소재·실루엣 구분.
- 전장, 전투, HUD, 건설·전술 패널과 벨루의 정보 계층.

참고하지 않을 것:

- 임시 세력명·건물명·대사와 한글 문구.
- 금화·식량·체력·비용·웨이브 수치.
- 이미지 안의 맵 연결, 요새·거점 배치와 건설 노드 수.
- 좌하단 전장 요약 UI와 미니맵처럼 보이는 구성.

현재 전장·경제·룰렛 책임 문서가 이미지보다 우선한다.

## 9. 애니메이션·연출 계약

공통 필수 상태:

```text
deploy / idle / move / attack_basic / skill_1 / hit_light / death / victory
```

- 공격은 준비→판정→회복으로 구분한다.
- 무기 접촉·투사체 발사와 실제 판정 오차는 한 프레임 이내다.
- 이동 위치는 코드가 소유하며 루트 모션을 사용하지 않는다.
- 같은 병종의 아군·적군 이미지 시트는 동일 AnimationContract에 맞춘다.
- 스테이지 승리 연출은 2.5~4초 뒤 결과 UI로 연결한다.

책임 원본: `docs/design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md`

## 10. 승인된 전장 초기값

### 중간거점

```text
중립화 10초 + 점령 10초 at 점령력 1.0
최대 유효 점령력 2.0
진행 유지 3초
복귀 속도 초당 10%
안정화 5초
소유 수입 금화 +2 / 30초
```

### 성문

```text
HP 5000
방어·마법저항 80
일반 구조물 피해 40%
공성 태그 피해 200%
고정 피해 50%
붕괴 2초
```

### 암살자 우회

```text
진입 준비 1초
우회 이동 9초
도착 경고 2.5초 전
출현 준비 0.6초
적 중간거점 뒤 120 units
도착 영역 160 × 120
점령력 0
```

## 11. 시각자료 감사와 누락 방지

`docs/images/VISUAL_REFERENCE_INDEX.md`에는 다음 자료가 기록돼 있다.

- 최신 전장 UI·병종 스프라이트 방향 이미지.
- 과거 10병종×등급 도감표.
- 스타일 후보 6안 비교표.
- 환경 콘셉트 이미지 묶음.
- 전술 지도·전장·하단 UI 탐색 시안.
- 전장 맵 툴과 사용법.
- 레거시 GDD와 제작 방법 메모.

바이너리 파일 이동이 끝나지 않은 자료는 `MIGRATION_PENDING`이다. 인덱스 등록과 실제 파일 이동을 혼동하지 않는다.

새 시각자료 처리 절차:

```text
원본·변환본 저장
→ Visual Reference Index 등록
→ 참고 / 비참고 / 변경점 기록
→ APPROVED 문서와 Work Order 연결
→ 기존 기준을 SUPERSEDED로 표시
```

## 12. 새 Codex 채팅의 행동 규칙

- 과거 대화와 Work Order의 상태 문구보다 실제 저장소를 우선한다.
- 현재 구현을 읽기 전에 새 프레임워크·병종 데이터·Scene 구조를 제안하지 않는다.
- 시각 작업에서는 `APPROVED_UNIT_VISUAL_FORMAT_AND_REFERENCE_USE_V1.md`와 `VISUAL_REFERENCE_INDEX.md`를 반드시 읽는다.
- 이미지에 없는 내용을 승인된 것으로 추정하지 않는다.
- Base는 범용 방법·검수·사례를 제공하며 오멘워드의 책임 원본을 덮어쓰지 않는다.
- 변경 범위와 완료 기준을 제안한 뒤 사용자 승인 전에는 구현하지 않는다.
