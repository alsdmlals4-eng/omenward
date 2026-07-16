# OMENWARD 프로젝트 인수인계 컨텍스트

- 갱신일: 2026-07-16
- 현재 단계: **플레이 가능한 수직 슬라이스 구현 완료 / PR 검토·수동 QA 대기**
- 현재 Work Order: `docs/work_orders/0001-phase-0-codex-plan-mode.md`
- 사전 기술 추천안: `docs/design/proposals/0001-phase-0-godot-bootstrap.md`
- 현재 Issue·Goal: Issue #1 / `docs/goals/0001-engine-selection-and-bootstrap.md`
- 다음 행동: PR #37 검토·병합 후 1920×1080·1280×720 수동 QA 수행
- 최신 통합 원본: `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`

## GitHub·로컬 동기화

- 표준 로컬 클론은 GitHub `main`과 같은 추적 파일 구조를 사용한다.
- `docs/issues/`는 열린·닫힌 GitHub Issue의 Markdown 미러이며, 댓글·첨부는 GitHub에서만 확인한다.
- 기획의 책임 원본은 `docs/design/`, Goal, Work Order다. Issue 미러에서 충돌을 해결하지 않고 해당 책임 문서를 먼저 갱신한다.
- GitHub Issue 변경은 동기화 PR로 검토하며, 로컬 갱신은 깨끗한 `main`에서 `tools/sync_repo.ps1`로만 수행한다.

이 문서는 새 ChatGPT, Codex, 기획자, 아티스트 또는 개발자가 이전 대화 없이도 오멘워드의 제품 방향, 데이터 소유, 현재 상태, 금지 범위와 다음 작업을 이해하기 위한 시작점이다. 세부 수치와 규칙은 링크된 책임 원본을 따른다.

---

## 1. 지금 가장 먼저 알아야 할 것

1. Phase 0은 Godot 4.7.1 Standard·Compatibility와 GDScript로 구현됐다.
2. `scenes/main/main.tscn`은 AutoLoad 없이 `GameSession`, WorldRoot 시각 프로브, StatusPanel을 조립한다.
3. `docs/design/proposals/0001-phase-0-godot-bootstrap.md`는 기획 측 사전 기술 추천안이며 Codex 검증 대상이다.
4. 새 Codex 채팅에는 `docs/work_orders/0001-phase-0-codex-plan-mode.md`의 시작 프롬프트를 전달한다.
5. `DataRegistry`, `StageManifest`, `CombatClock`, `DeterminismService`와 공용 Resource 계약은 Goal 0002의 구현 경계다.
6. Issue #32 사용자 승인 전 실제 전투·룰렛·건설·점령·성문·웨이브 구현을 시작하지 않는다.
7. 적군 병종 데이터를 별도로 만들지 않는다.
8. 공용 병종 10개에 아군 이미지 세트 또는 적군 이미지 세트를 연결한다.
9. 다음 구현 단계는 전체 게임이 아니라 Godot 기술 기준선 Phase 0이다.

현재 상태를 혼동하지 않는다.

```text
기획 승인 완료
≠ Work Order 준비 완료
≠ Codex Plan Mode 제안서 제출
≠ 사용자 승인
≠ 구현 완료
≠ 플레이테스트 검증
```

---

## 2. 최초 읽기 순서

```text
1. AGENTS.md
2. docs/BASE_RULES_VERSION.md
3. docs/HANDOFF_CONTEXT.md
4. docs/DOCUMENTATION_MAP.md
5. 현재 Codex 작업이면 docs/work_orders 문서
6. docs/OMENWARD_GAME_DESIGN.md
7. 현재 작업 관련 APPROVED 책임 문서
8. docs/OMENWARD_ROADMAP.md
9. 현재 Issue / Goal
10. 실제 코드·데이터·Scene·테스트
11. 사전 기술 추천 또는 Codex 제출 제안서
12. docs/ACTIVE_CONTEXT.md
```

Phase 0 새 Codex 채팅은 `docs/work_orders/0001-phase-0-codex-plan-mode.md`의 복사 프롬프트를 우선 사용한다.

---

## 3. 제품 약속

### 한 문장

> 건물을 지어 룰렛 확률과 증원 체계를 설계하고, 베일의 징조로 예고된 공세를 세 전선에서 뒤집는 판타지 전략 오토배틀 게임.

### 핵심 플레이 경험

플레이어는 다음 공세의 라인과 위협 태그를 미리 읽고, 제한된 금화·식량·건설 노드 안에서 건물과 룰렛 확률을 설계한다. 룰렛으로 획득한 병력을 원하는 라인에 배치하고, 거점·성문·암살자 우회로를 이용해 예고된 위기를 역전한다.

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

---

## 4. 변경 시 사용자 승인이 필요한 불변 구조

### 전장

```text
아군 본진
→ 라인별 아군 성문
→ 아군 중간거점
→ 중앙 접전지
→ 적 중간거점
→ 라인별 적 성문
→ 적 본진
```

- 좌우 대칭의 독립된 상·중·하 3라인.
- 일반 유닛의 라인 간 횡단과 기본 라인 변경 없음.
- 각 라인에 독립 성문 1개씩, 진영당 총 3개.
- 각 중간거점에 전방 건설 노드 2개와 후방 노드 1개.
- 중간거점 점령 시 건설권과 기본 생산권 이전.
- 중앙 접전지는 다른 라인과 연결되지 않고 건설 불가.
- 암살자는 적 후방 직접 배치가 아니라 같은 라인의 안개 우회로 사용.
- 전장이 기본 전략 화면에 들어오므로 미니맵 없음.

책임 원본: `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`

### 병종과 데이터

```text
UnitArchetypeProfile × 10
+ TierProfile
+ RankProfile
+ owner_team_id
+ FactionVisualProfile
```

- 전투 규칙 기준 병종은 공용 아키타입 10개뿐이다.
- 아군·적군 별도 스탯·스킬·타기팅·애니메이션 데이터를 만들지 않는다.
- 같은 공용 병종 데이터에 아군 이미지 세트 또는 적군 이미지 세트를 연결한다.
- 차이는 소유 팀, 출격 방식, 이미지·초상화·아이콘·팔레트·표시명이다.
- 일반 적군 난이도는 수량, Tier, Rank, 라인 편성, 출격 시점으로 만든다.
- W15·W20 보스는 공용 아키타입에 BossBehaviorPackage와 전용 Visual Set을 추가한다.
- 별도 `EnemyUnitProfile`, Enemy Unit Scene, 적군 전용 모션 상태 머신 금지.

책임 원본: `docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`

### 등급과 Tier

- 플레이어 등급: 일반·엘리트·영웅·전설.
- 플레이어 신화급 없음.
- 적군 신화는 W20 보스 전용 패키지.
- Tier는 생산시설·병종 전문화, Rank는 룰렛 결과와 스킬 성장.

### 문서와 구현

- 한 주제당 활성 책임 원본 하나.
- 이전 버전은 일반적으로 Git 이력에서 보존.
- Work Order는 Codex 입력이고 Codex Plan Mode 제안서는 조사 결과다.
- 코드·Scene·Resource·데이터 변경은 Codex 제안서의 사용자 승인 후 시작.
- 문서 승인 상태를 구현 완료로 보고하지 않는다.

---

## 5. 공용 10병종

### 기본 병영 6종

- 방패병 — 전열·원거리 대응.
- 대검전사 — 정면 범위·파쇄.
- 암살자 — 안개 우회로와 후열 제거.
- 창병 — 돌진·대형 저지.
- 궁병 — 지속 원거리·대공.
- 기병 — 기동·돌진·후열 압박.

### 특수병단 4종

- 사제 — 치유·전투 지원.
- 마법사 — 광역 마법·제어.
- 비행병 — 지상 전열 우회·후열 압박.
- 거인 — 대형 범위·방어·공성.

---

## 6. 승인된 수직 슬라이스 초기값

### 중간거점

```text
중립화 10초 + 점령 10초 at 점령력 1.0
최대 유효 점령력 2.0
진행 유지 3초
복귀 속도 초당 10%
점령 완료 후 안정화 5초
소유 수입 금화 +2 / 30초
```

- 방패·수호형 1.25.
- 일반 근접·기병 1.0.
- 원거리·지원·거인 0.5.
- 암살자·비행·순수 공성 0.
- 점령 시도 중 생산·신규 건설·업그레이드 정지.
- 중립화 시 기존 건물 비활성.
- 점령 완료 시 기존 건물 폐허화, 환불 없음.
- 5초 안정화 후 새 소유자의 건설·생산 활성.

### 성문

```text
HP 5000
방어 80
마법저항 80
일반 구조물 피해 40%
공성 태그 피해 200%
고정 피해 50%
붕괴 2초
```

- 아군 통과, 적은 파괴 전까지 차단.
- 군중제어·밀쳐내기·비율 피해 면역.
- 폐허는 길을 막지 않음.
- 수직 슬라이스에서 수리·재건 없음.

### 암살자 우회

```text
진입 준비 1초
오프맵 이동 9초
도착 2.5초 전 수비 경고
출현 후 준비 0.6초
적 중간거점에서 본진 방향 120 units
도착 영역 160 × 120 units
막힘 보정 반경 80 units
점령력 0
```

- 진입 확정 후 취소·후퇴 불가.
- 우회 중 전투·피격·점령·버프 없음.
- 경로는 암살자 선택·배치 중에만 표시.
- 탐지 전용 건물은 수직 슬라이스 제외.

위 값은 PoC 초기값이며 플레이테스트 근거로 같은 구조 안에서 조정할 수 있다.

---

## 7. 애니메이션·전투 연출 계약

공통 필수 상태:

```text
deploy / idle / move / attack_basic / skill_1 / hit_light / death / victory
```

역할별 추가:

- 점령 가능 병종: `capture`.
- 암살자: `bypass_enter`, `bypass_exit`.
- 기병: `charge`, `turn_recover`.
- 비행병: 상승·순항·급강하·회복.
- 거인: `structure_attack`, `heavy_stagger`.

핵심 원칙:

- 공격은 준비→판정→회복.
- 무기 접촉·투사체 발사와 실제 판정은 한 프레임 이내로 동기화.
- 이동 위치는 코드가 소유하며 루트 모션을 사용하지 않음.
- 한 아키타입의 공용 상태·프레임·피벗·이벤트 계약에 양 진영 이미지 시트를 맞춘다.
- 적군 모션을 별도 상태 머신이나 별도 타이밍 데이터로 제작하지 않는다.
- 스테이지 승리 연출은 2.5~4.0초 뒤 결과 UI로 연결한다.

책임 원본: `docs/design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md`

---

## 8. 경제·공세 기준

```text
시작 금화 160
시작 식량 12
기본 수입 +5 / 20초
중앙 접전지 +4 / 60초 / 소유 지점
중간거점 +2 / 30초 / 소유 지점
룰렛 비용 20
```

- 적 처치·웨이브 클리어 고정 금화 없음.
- 활성 전투 시간 기준 60초마다 공세 충돌.
- W5 엘리트, W10 영웅, W15 전설 보스, W20 신화 보스.
- W15 보스 처치 표준 승리, 이전 적 본진 파괴는 조기 승리.
- 적 웨이브는 공용 10병종을 Tier·Rank·수량·라인으로 조합.

---

## 9. 현재 실행 순서

### Gate 1 — 새 Codex 채팅 Phase 0 Plan Mode

책임:

- `docs/work_orders/0001-phase-0-codex-plan-mode.md`
- Issue #1
- Goal 0001

Codex는 다음을 수행한다.

- 저장소·Base·urban-legend·공식 근거 읽기 전용 조사.
- 사전 기술 추천안의 채택·수정·기각 판단.
- 정확한 예상 파일·Scene·Resource·상태 소유·검증 계획 작성.
- `docs/PROPOSAL_WORKFLOW.md` 형식의 제안서 제출.

구현 파일과 브랜치는 만들지 않는다.

### Gate 2 — 사용자 검토·승인

사용자가 Codex 제안서를 수정하거나 명시적으로 승인한다.

### Gate 3 — Phase 0 구현

승인된 범위만 별도 구현 실행과 PR로 진행한다.

완료 조건:

- Godot 프로젝트 headless 로드.
- 데이터 참조·중복·Visual·전장 계약 검증.
- 동일 시드 재현 골격.
- 공용 아키타입과 진영 Visual 분리 골격.
- 수직 슬라이스가 사용할 실제 파일 경로와 명령 확정.

### Gate 4 — 수직 슬라이스 Plan Mode

책임: Issue #32, Goal 0002.

실제 Phase 0 파일을 기반으로 3라인·거점·성문·우회·최소 룰렛·대표 모션 구현을 계획한다.

---

## 10. 사전 기술 추천안의 위치

`docs/design/proposals/0001-phase-0-godot-bootstrap.md`에는 다음 추천이 기록돼 있다.

- Godot 4.7.1 standard.
- Compatibility renderer.
- 1920×1080 출력과 960×540 내부 viewport.
- Phase 0 AutoLoad 미사용.
- typed Resource와 JSON 분리.
- AnimatedSprite2D + 제한적 AnimationPlayer.
- 60Hz active combat tick과 RNG stream·input log.
- 공용 10 archetype과 allied/veil Visual Profile 골격.
- headless GDScript test runner.

이는 사용자 승인 완료 기술 사양이 아니다. Codex는 실제 저장소와 공식 근거를 확인해 최종 Plan Mode 제안서에서 판단한다.

---

## 11. 구현 전 반드시 확인할 미확정

Codex Plan Mode에서 결정:

- 정확한 Godot stable 버전과 renderer.
- 내부 논리 해상도와 stretch.
- AutoLoad 사용 여부.
- Resource·JSON·CSV 경계.
- AnimatedSprite2D·AnimationPlayer 구조.
- 공용 Resource 스키마와 실제 경로.
- 시간·tick·RNG·로그 구조.
- headless 테스트 러너와 실제 명령.

PoC·플레이테스트에서 조정:

- 유닛·건물·룰렛·웨이브 수치.
- 점령·성문·우회 시간과 대응성.
- 애니메이션 FPS와 정확한 프레임 수.
- 카메라 흔들림·히트 스톱 강도.
- 최종 팔레트·스프라이트·아이콘·오디오.

---

## 12. Base 공용 지식 사용

Base 저장소는 프로젝트 규칙보다 낮은 공용 참고자료다.

- 인수인계: `Base/docs/knowledge/methods/PROJECT_HANDOFF_CONTEXT_METHOD.md`
- Codex Work Order: `Base/docs/knowledge/methods/CODEX_PLAN_MODE_WORK_PACKAGE_METHOD.md`
- 아트 디렉션: `Base/docs/knowledge/methods/ART_DIRECTION_METHOD.md`
- 애니메이션·연출: `Base/docs/knowledge/methods/ANIMATION_AND_PRESENTATION_METHOD.md`
- 조사·벤치마킹: `Base/docs/knowledge/research/DESIGN_RESEARCH_AND_EVIDENCE_METHOD.md`
- 실무 검수: `Base/docs/knowledge/skills/`
- 일반화 사례: `Base/docs/knowledge/cases/`

적용 순서:

```text
오멘워드 최신 사용자 결정·책임 문서
→ 현재 Work Order·Issue·Goal
→ 실제 파일
→ Base 공용 방법·스킬·사례
→ 외부 벤치마킹·공식 자료
```

---

## 13. 하지 말아야 할 것

- Work Order를 Codex 최종 제안서로 오인.
- 사전 기술 추천안을 승인 완료 사양으로 오인.
- 적군 10병종의 별도 스탯·스킬·애니메이션 데이터 제작.
- 아군 Scene을 복사해 Enemy Scene으로 분기.
- 미니맵 추가.
- 암살자 적 후방 직접 생성.
- 라인 간 일반 횡단로 추가.
- 중간거점 노드 구조 변경.
- 일반 공격마다 큰 화면 흔들림·히트 스톱 사용.
- 문서의 PoC 수치를 최종 밸런스로 고정.
- 사용자 승인 없이 Godot 코드·Scene·Resource 생성.
- Base 또는 사례가 최신 사용자 결정을 덮어쓰게 함.

---

## 14. 콜드 스타트 확인 질문

새 작업자는 10분 안에 다음을 답해야 한다.

1. 오멘워드의 핵심 루프는 무엇인가?
2. 현재 코드를 바로 수정해도 되는가?
3. 현재 입력 문서는 Work Order인가 Codex 최종 제안서인가?
4. 새 Codex 채팅에서 가장 먼저 사용할 파일은 무엇인가?
5. 전장 불변 구조는 무엇인가?
6. 아군과 적군은 몇 개의 전투 병종 데이터를 사용하는가?
7. 진영 차이는 어디에 저장하는가?
8. 애니메이션 판정은 어떻게 분리하는가?
9. 어떤 수치는 PoC 조정 가능하고 어떤 구조는 승인 대상인가?
10. Base 공용 지식과 프로젝트 책임 문서가 충돌하면 무엇이 우선하는가?

정확히 답하지 못하면 이 문서와 Documentation Map, Work Order의 링크·상태·용어를 먼저 보강한다.
