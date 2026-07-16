# Active Context

- 갱신일: 2026-07-16
- 공식명: **오멘워드 / OMENWARD**
- 저장소 상태: **Godot 프로젝트와 플레이 가능한 수직 슬라이스 코드·데이터가 존재함 / 다음 작업 전 실제 main과 검증 문서 재확인 필수**
- 최초 인수인계: `docs/HANDOFF_CONTEXT.md`
- 최신 통합 기준: `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`
- 시각자료 인덱스: `docs/images/VISUAL_REFERENCE_INDEX.md`
- 병종 비주얼 형식: `docs/design/APPROVED_UNIT_VISUAL_FORMAT_AND_REFERENCE_USE_V1.md`

## 현재 상태를 판단하는 방법

과거 Work Order의 상태 문구를 현재 구현 상태로 사용하지 않는다. 새 작업자는 다음을 직접 확인한다.

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

현재 `project.godot`에는 960×540 논리 화면, 1920×1080 출력, Compatibility renderer와 main Scene이 정의돼 있다. 새 Codex 채팅은 문서 요약만 하지 말고 실제 파일·테스트·실행 결과를 기준으로 다음 제안 범위를 정한다.

## 핵심 정체성

- 장르: 실시간 3라인 전략 오토배틀 + 건물 기반 3×3 룰렛 빌드.
- 핵심 루프: `베일의 징조 → 건물·토큰 선택 → 룰렛 → 라인 배치 → 거점·성문·우회 공방`.
- 플랫폼: Windows PC / 마우스·키보드 / 싱글플레이 PvE.
- 엔진: Godot + GDScript.
- 첫 10분 안에 건설→룰렛→배치→역전 루프를 두 번 체험한다.

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
- 진영당 라인별 성문 3개.
- 중간거점 전방 2·후방 1 건설 노드.
- 점령 시 건설권·기본 생산권 이전.
- 암살자는 적 후방 직접 생성이 아니라 같은 라인의 안개 우회로 사용.
- 전장 전체를 기본 전략 화면에서 보며 미니맵 없음.

책임 원본: `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`

## 공용 병종 데이터

```text
UnitArchetypeProfile 10개
+ TierProfile
+ RankProfile
+ owner_team_id
+ FactionVisualProfile
```

- 아군과 적군의 전투 병종 데이터를 따로 만들지 않는다.
- HP·공격·스킬·타기팅·점령력·구조물 피해·AnimationContract를 공유한다.
- 차이는 팀, 출격 방식, 이미지·초상화·아이콘·팔레트와 표시명이다.
- 일반 적군용 `EnemyUnitProfile`, 별도 Unit Scene, 전용 스탯·스킬·모션 계약 금지.
- W15·W20 보스는 공용 아키타입에 행동·페이즈 패키지와 전용 Visual Set을 추가한다.

책임 원본:

- `docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`
- `docs/design/APPROVED_SHARED_ARCHETYPE_WAVE_1_20_POC_V1.md`

## 공용 10병종

- 기본 병영: 방패병, 대검전사, 암살자, 창병, 궁병, 기병.
- 특수병단: 사제, 마법사, 비행병, 거인.
- 플레이어 등급: 일반·엘리트·영웅·전설.
- 적 신화는 W20 보스 패키지 전용.

## 최신 병종 이미지 형식 결정

### 승인 기준

병종 이미지는 **첫 번째 전장 UI 이미지에 보이는 실제 전장 삽입형 소형 고해상도 픽셀 스프라이트 형식**으로 제작한다.

```text
전장 속 월드 스프라이트
+ 약 2.5~3등신 전술 미니어처 비율
+ 무기·자세·몸통 덩어리 중심 판독
+ 34~40px 인간형 첫 표시 높이 가설
+ 제한된 재질 디테일과 선명한 외곽선
```

- 전략 화면에서 얼굴보다 무기 길이, 자세, 실루엣과 공격 방향이 먼저 읽혀야 한다.
- 아군과 적군은 같은 공용 프레임·피벗·공격 이벤트 계약을 사용한다.
- 진영 차이는 색상만이 아니라 장비·소재·외곽 형태 또는 생물 기관으로 표현한다.
- 일반→엘리트→영웅→전설은 단순 확대가 아니라 기능적인 무기·실루엣·자세·제한적 VFX로 위계를 만든다.

### 과거 도감표의 위치

두 번째 `10병종 × 일반·엘리트·영웅·전설` 도감표는 다음만 참고한다.

- 공용 10병종 목록.
- 같은 병종의 등급 상승 관계.
- 상위 등급에서 역할 실루엣과 무기가 강화되는 방향.

도감표의 큰 전신 캐릭터 비율과 렌더링 밀도는 실제 월드 스프라이트 형식으로 사용하지 않는다.

책임 원본:

- `docs/design/APPROVED_UNIT_VISUAL_FORMAT_AND_REFERENCE_USE_V1.md`
- `docs/images/VISUAL_REFERENCE_INDEX.md`
- `docs/design/APPROVED_ART_DIRECTION_AND_PRODUCTION_GUIDE_V1.md`

## 참고 이미지 해석 금지 사항

첫 번째 이미지도 전체 게임 사양을 그대로 복사하는 화면이 아니다.

- 이미지 안의 임시 수치, 비용, 체력, 웨이브와 문구를 확정값으로 사용하지 않는다.
- 이미지 안의 거점·요새·길 연결을 현재 전장 토폴로지로 복사하지 않는다.
- 좌하단 전장 요약 UI는 현재 기획의 `미니맵 없음` 규칙을 바꾸지 않는다.
- 화면은 유닛 크기·픽셀 밀도·전장과 HUD의 정보 계층을 참고하는 방향 이미지다.

## 애니메이션·연출

공통 필수 상태:

```text
deploy / idle / move / attack_basic / skill_1 / hit_light / death / victory
```

- 공격은 준비→판정→회복으로 구분.
- 접촉·투사체 발사와 실제 판정 오차는 한 프레임 이내.
- 이동 위치는 코드가 소유하며 루트 모션을 사용하지 않는다.
- 아군·적군 이미지는 같은 AnimationContract에 맞춘다.
- 스테이지 승리 연출은 2.5~4초 뒤 결과 UI로 연결한다.

책임 원본: `docs/design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md`

## 승인된 전장 초기값 요약

### 중간거점

```text
중립화 10초 + 점령 10초 at 점령력 1.0
최대 점령력 2.0
진행 유지 3초
복귀 초당 10%
안정화 5초
금화 +2 / 30초
```

### 성문

```text
HP 5000
방어·마법저항 80
일반 구조물 피해 40%
공성 200%
고정 피해 50%
붕괴 2초
```

### 암살자 우회

```text
진입 1초
이동 9초
도착 경고 2.5초 전
출현 준비 0.6초
적 중간거점 뒤 120 units
도착 영역 160 × 120
점령력 0
```

## 시각자료 누락 감사

`docs/images/VISUAL_REFERENCE_INDEX.md`에 다음 자료의 존재와 처리 상태를 기록했다.

- 스타일 후보 6안 비교표.
- 환경 콘셉트 `image-gen-1/3/4/5`.
- 전술 지도·전장·하단 UI 탐색 이미지 3종.
- 과거 유닛 도감.
- 전장 맵 툴과 사용법.
- 레거시 GDD와 제작 방법 메모.

저장소 바이너리 이동이 끝나지 않은 자료는 `MIGRATION_PENDING`이며, 이동이 확인되기 전 완료로 보고하지 않는다.

## 새 이미지 유입 규칙

사용자가 이미지를 제공한 작업은 다음 네 항목을 모두 처리한다.

1. 저장 가능한 원본 또는 변환본을 프로젝트 경로에 배치.
2. `docs/images/VISUAL_REFERENCE_INDEX.md`에 상태와 경로 등록.
3. 참고할 것·참고하지 않을 것·현재 기획과 달라진 것을 기록.
4. 관련 APPROVED 문서·Work Order·Documentation Map에 연결.

기존 기준이 바뀌면 이미지를 조용히 교체하지 않고 `SUPERSEDED` 상태와 변경 이유를 남긴다.

## 다음 작업 원칙

- 새 Codex 채팅은 현재 저장소가 구현 전이라는 과거 문구를 믿지 말고 실제 main을 먼저 조사한다.
- 시각·병종·UI 작업은 새 병종 비주얼 책임 문서와 시각자료 인덱스를 반드시 읽는다.
- 실제 아트 제작 전 대표 병종 5종을 1080p·720p 전장에 삽입해 축소 가독성을 검증한다.
- Base 공용 지식은 방법과 사례 참고용이며 오멘워드 책임 문서를 덮어쓰지 않는다.
