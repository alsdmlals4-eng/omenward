# Codex 새 채팅 작업 제안서 — Phase 0 Godot·공용 병종 데이터 Plan Mode

- 작성일: 2026-07-16
- 대응 Issue: #1
- 대응 Goal: `docs/goals/0001-engine-selection-and-bootstrap.md`
- 상태: **새 Codex 채팅 Plan Mode 실행 준비 완료 / 구현 금지**
- 목적: Codex가 새 채팅에서 이전 대화를 몰라도 저장소의 기획서·책임 문서·참고 사례를 읽고, Phase 0 구현을 위한 검토 가능한 계획을 작성하게 한다.

이 문서는 **Codex가 작성할 최종 Plan Mode 제안서가 아니다.**
사용자와 기획 AI가 Codex에 전달하는 작업 요청서이자 컨텍스트 패키지다.

`docs/design/proposals/0001-phase-0-godot-bootstrap.md`는 사전 기술 추천안이다. Codex는 이를 그대로 승인하거나 복사하지 말고 실제 저장소와 공식 근거를 확인해 채택·수정·기각 이유를 제시한다.

---

## 1. 새 Codex 채팅에 붙여 넣을 시작 프롬프트

아래 블록을 새 Codex 채팅의 첫 메시지로 사용한다.

```text
저장소: alsdmlals4-eng/omenward
작업 모드: Codex Plan Mode / 읽기 전용 조사
현재 작업: Issue #1 — Phase 0 Godot·공용 병종 데이터 부트스트랩 계획

이번 실행에서는 구현하지 마세요.
project.godot, Scene, GDScript, Resource, 데이터, 테스트, 자산을 생성·수정하지 말고 브랜치·커밋·PR도 만들지 마세요.

먼저 다음 순서로 읽으세요.

1. AGENTS.md
2. docs/BASE_RULES_VERSION.md
3. docs/HANDOFF_CONTEXT.md
4. docs/DOCUMENTATION_MAP.md
5. docs/PROPOSAL_WORKFLOW.md
6. docs/work_orders/0001-phase-0-codex-plan-mode.md
7. docs/OMENWARD_GAME_DESIGN.md
8. docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md
9. docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md
10. docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md
11. docs/design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md
12. docs/design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md
13. docs/GODOT_PROJECT_STRUCTURE.md
14. docs/DECISIONS_PENDING.md
15. docs/OMENWARD_ROADMAP.md
16. docs/goals/0001-engine-selection-and-bootstrap.md
17. GitHub Issue #1
18. docs/design/proposals/0001-phase-0-godot-bootstrap.md

그 다음 실제 저장소 파일을 조사해 현재 구현 유무, 기존 경로, 충돌, 누락을 확인하세요.
참고 저장소는 필요한 파일만 읽으세요.

- alsdmlals4-eng/Base
- alsdmlals4-eng/urban-legend

Base는 방법·검수·사례 참고이며 오멘워드의 승인 사양을 대체하지 않습니다.
urban-legend는 실제 Godot 프로젝트 구조와 검증 사례 참고이며 코드를 그대로 복사하지 않습니다.

최종 산출물은 docs/PROPOSAL_WORKFLOW.md 형식의 Phase 0 구현 제안서입니다.
추천안 하나를 중심으로 필요한 대안만 비교하고, 정확한 예상 파일·Scene 트리·Resource 구조·상태 소유·Signal 흐름·구현 단계·검증 명령·위험·사용자 결정 요청을 작성하세요.

특히 다음을 반드시 검토하세요.

- 현재 사용 가능한 공식 Godot stable 버전과 renderer
- 1920×1080 출력, 내부 논리 해상도, stretch, 픽셀 스냅
- Phase 0의 최소 Scene·Script·Resource·Test 구조
- AutoLoad를 사용하지 않는 안과 필요한 경우의 대안
- 공용 UnitArchetypeProfile 10개와 양 진영 FactionVisualProfile
- 별도 EnemyUnitProfile·Enemy Unit Scene·진영별 전투 데이터 복사 방지
- AnimationContract와 실제 공격 판정 이벤트의 책임 분리
- active_combat_time, planning, 결정론적 seed·RNG stream·input log
- Resource·JSON·CSV 경계
- BattlefieldProfile의 독립 3라인·성문·거점·노드·암살자 우회 계약
- headless 로드·GDScript 테스트·수동 화면 검증
- Phase 0 종료 후 Goal 0002와 Issue #32로 넘길 실제 경로·명령

사전 추천안인 docs/design/proposals/0001-phase-0-godot-bootstrap.md를 검토하되 그대로 확정하지 마세요.
근거가 약하거나 과도한 범위는 줄이고, 누락된 위험은 추가하세요.
확인하지 못한 사실은 추정하지 말고 확인 필요로 표시하세요.

제안서 마지막에는 반드시 다음을 적으세요.

현재 상태: 제안서 검토 대기
사용자 승인 전 구현 금지
```

---

## 2. Codex가 먼저 이해해야 하는 제품 컨텍스트

### 한 문장

> 건물을 지어 룰렛 확률과 증원 체계를 설계하고, 예고된 공세를 세 전선에서 뒤집는 판타지 전략 오토배틀 게임.

### 핵심 루프

```text
베일의 징조
→ 건물·토큰 선택
→ 3×3 룰렛
→ 병력 획득·라인 배치
→ 3라인 교전
→ 접전지·중간거점 공방
→ 암살자 우회 또는 성문 공성
→ 다음 공세 준비
```

Phase 0은 이 루프를 구현하는 단계가 아니다. 이 루프를 중복 없이 안전하게 구현하기 위한 **Godot 기술 기준선, 데이터 계약과 검증 골격**을 계획하는 단계다.

---

## 3. 변경하면 안 되는 승인 불변 조건

### 전장

- 좌우 대칭 독립 상·중·하 3라인.
- 각 라인은 `본진 → 성문 → 중간거점 → 중앙 접전지 → 적 중간거점 → 적 성문 → 적 본진`.
- 일반 라인 횡단 없음.
- 진영당 라인별 성문 3개.
- 중간거점마다 전방 2·후방 1 건설 노드.
- 점령 시 건설권과 기본 생산권 이전.
- 중앙 접전지 건설 불가.
- 암살자는 적 후방 직접 생성이 아니라 같은 라인의 안개 우회로 사용.
- 기본 전략 화면에서 전장 전체 조망, 미니맵 없음.

### 공용 병종 데이터

```text
UnitArchetypeProfile × 10
+ TierProfile
+ RankProfile
+ owner_team_id
+ FactionVisualProfile
```

- 아군·적군 별도 전투 병종 데이터를 만들지 않는다.
- 같은 아키타입·Tier·Rank는 진영과 무관하게 같은 수치·스킬·타기팅·점령력·구조물 피해·AnimationContract를 사용한다.
- 차이는 팀, 출격 방식, 이미지·초상화·아이콘·팔레트·표시명이다.
- 별도 `EnemyUnitProfile`, Enemy Unit Scene, enemy 전용 스탯·스킬·모션 타이밍 금지.
- 일반 적 웨이브는 공용 `archetype_id`를 참조한다.
- 보스는 공용 base archetype에 행동·페이즈 패키지와 전용 Visual Set을 추가한다.

### 애니메이션·판정

- 공용 상태·프레임·피벗·이벤트 계약에 양 진영 이미지 시트를 맞춘다.
- 공격은 준비→판정→회복으로 구분한다.
- 실제 전투 판정이 권위 원본이며 애니메이션 method track이 피해의 유일한 원본이 되지 않는다.
- 이동 위치는 코드가 소유하며 루트 모션을 사용하지 않는다.

### 구현 게이트

- 이번 작업은 Plan Mode다.
- 사용자 승인 전 구현 파일, 브랜치, 커밋, PR을 만들지 않는다.
- 사전 추천과 승인된 사양을 구분한다.

---

## 4. Codex가 조사해야 하는 실제 상태

Codex는 다음을 직접 확인하고 제안서에 근거를 남긴다.

1. 현재 `main`에 `project.godot`이 실제로 존재하는가.
2. 기존 `.tscn`, `.gd`, `.tres`, 테스트와 실행 명령이 있는가.
3. 기획 문서가 서로 다른 상태·경로·데이터 소유를 설명하는 충돌이 있는가.
4. 예상 경로가 실제 저장소 규칙과 맞는가.
5. Base에서 재사용할 방법과 오멘워드에 적용하지 않을 부분은 무엇인가.
6. urban-legend의 Godot 버전·폴더·AutoLoad·headless 방식 중 채택·제외할 것은 무엇인가.
7. 공식 Godot 자료 기준 현재 stable 버전, CLI와 화면 정책은 무엇인가.
8. Phase 0에서 반드시 필요한 최소 파일과 수직 슬라이스까지 미뤄야 할 파일은 무엇인가.

검색 결과가 없다는 이유만으로 존재하지 않는다고 단정하지 말고 저장소 트리와 알려진 경로를 함께 확인한다.

---

## 5. Codex Plan Mode에 포함할 작업 묶음

### A. 엔진·화면 기준선

- 정확한 Godot stable 버전과 standard/.NET 선택.
- Compatibility, Mobile, Forward+ 중 추천 renderer.
- 출력·내부 논리 해상도·stretch·aspect·integer scaling.
- nearest filtering과 픽셀 정렬.
- 1920×1080 및 1280×720 검증 정책.
- 카메라 기능을 Phase 0에 넣을지 probe만 둘지.

### B. 프로젝트·Scene·상태 소유

- 최소 폴더와 파일.
- Main, GameSession, Clock, Determinism, Registry, Visual Probe, Status UI의 책임.
- Phase 0 AutoLoad 미사용 추천안 검토.
- UI·도메인·데이터 사이 Signal과 의존성 주입.
- 전역 이벤트 버스와 범용 프레임워크를 만들지 않는 경계.

### C. 공용 병종·진영 표현 데이터

- UnitArchetype, Tier, Rank, FactionVisual, AnimationContract의 typed Resource 구조.
- 정확히 10개 아키타입을 생성할지, 스키마와 소수 fixture만 만들지 비교.
- 양 진영 Visual Profile의 파일·ID·참조 규칙.
- Visual 변경이 전투 결과를 바꾸지 않는 자동 검사.
- Enemy 데이터 복제를 탐지하는 정적·런타임 검사.
- 보스 패키지는 인터페이스만 둘지 Phase 0에서 스키마까지 만들지.

### D. 시간·결정론·로그

- `real_time`, `active_combat_time`, `ui_planning_time` 소유.
- fixed tick 또는 physics tick 사용 방식.
- planning 중 전투 시간 정지와 UI 반응.
- master seed와 도메인별 RNG stream.
- 입력 로그의 최소 스키마와 재생 테스트.
- 시각 랜덤이 전투 랜덤에 영향을 주지 않는 구조.

### E. 전장·StageManifest 데이터 계약

- BattlefieldProfile의 라인·성문·거점·노드·우회 필드.
- StageManifest의 JSON 책임과 typed loader.
- spawn entry가 전투 수치를 복사하지 않고 공용 ID를 참조하는 규칙.
- Resource와 JSON의 중복 원본 방지.
- CSV를 Phase 0 런타임에서 배제할지.

### F. 애니메이션·판정 연결

- AnimatedSprite2D, AnimationPlayer 또는 조합.
- AnimationContract의 프레임·피벗·impact/projectile event.
- AttackProfile과 active tick이 판정을 소유하는 방식.
- Phase 0 Visual Contract probe 범위.
- 실제 공격·Unit Scene은 수직 슬라이스까지 미룬다는 경계.

### G. 자동·수동 검증과 인수인계

- 실제 Windows Godot console 경로를 하드코딩하지 않는 명령.
- editor/headless load.
- 외부 플러그인 없는 GDScript test runner 또는 더 나은 대안.
- 올바른 fixture와 의도적으로 잘못된 fixture.
- 1080p·720p 화면, 픽셀, 한국어 UI와 Visual Set 수동 검수.
- Phase 0 완료 뒤 README, Handoff, Active Context, Roadmap, Goal 0002, Issue #32 갱신.

---

## 6. 사전 기술 추천안 — 검증 대상

다음은 Codex가 검토할 추천값이지 이미 승인된 구현 결정이 아니다.

| 항목 | 사전 추천 |
|---|---|
| Godot | 4.7.1 standard x86_64 |
| 언어 | 정적 타입을 우선한 GDScript |
| Renderer | Compatibility |
| 기준 출력 | 1920×1080 |
| 내부 해상도 | 960×540 |
| Stretch | viewport / keep / integer |
| 720p | 레터박스 상태로 우선 QA |
| AutoLoad | Phase 0 미사용 |
| 데이터 | typed `.tres` 중심 |
| JSON | StageManifest와 replay/input log |
| CSV | Phase 0 런타임 미사용 |
| 애니메이션 | AnimatedSprite2D + 제한적 AnimationPlayer |
| 테스트 | 외부 의존성 없는 headless GDScript runner |

Codex는 다음을 명확히 판단한다.

- 그대로 채택.
- 일부 수정.
- 범위 축소.
- 다른 대안 추천.

판단에는 근거, 비용, 이후 수직 슬라이스에 미치는 영향을 포함한다.

---

## 7. Codex가 제안서에 반드시 적을 예상 산출물

### 정확한 Scene 트리 후보

노드 이름뿐 아니라 각 노드의 상태 소유, 생성·주입 방식과 제거 기준을 설명한다.

### 정확한 파일 목록

각 파일에 대해 다음을 적는다.

```text
경로
신규/수정
책임
참조 대상
자동 검증
```

### 단계별 구현 순서

각 단계는 다음을 포함한다.

```text
변경 내용
예상 파일
관찰 가능한 결과
자동 검증
수동 검증
독립 커밋 가능 여부
```

### 위험·대안

최소한 다음 위험을 다룬다.

- 최신 Godot 버전의 회귀.
- 960×540과 720p 정수 확대.
- 초기 Resource 파일 과다 생성.
- DataRegistry 비대화.
- AutoLoad를 너무 일찍 또는 늦게 도입.
- 비결정적 RNG 호출 순서.
- AnimationPlayer가 게임 판정을 소유.
- 양 진영 이미지 체형·피벗 불일치.
- 적군 데이터 복제.
- 테스트가 실제 화면 검수를 대체하는 문제.

### 사용자 결정 요청

Codex는 승인해야 할 선택만 3~6개로 압축하고 각 항목에 추천안과 대안을 붙인다.

---

## 8. 포함 범위

- Phase 0 기술 기준선의 구현 계획.
- 엔진·화면·상태·데이터·결정론·검증 구조.
- 공용 아키타입과 진영별 Visual 계약.
- 전장·Manifest의 최소 데이터 계약.
- Visual Contract probe.
- headless 테스트와 문서 인수인계 계획.

---

## 9. 제외 범위

- 실제 Godot 파일 생성·수정.
- 실제 전투·이동·타기팅·공격 AI.
- 룰렛·건설·경제·점령·성문·웨이브 구현.
- 3라인 Battle Scene.
- 실제 Unit 전투 Scene.
- 최종 아트·VFX·오디오.
- 전체 10병종의 완성 밸런스.
- 적군 전용 데이터·Scene·모션.
- 저장·Steam·배포.
- 승인되지 않은 외부 플러그인·애드온.

---

## 10. 좋은 제안서의 완료 기준

- [ ] 실제 저장소를 읽고 현재 구현 유무를 근거와 함께 설명한다.
- [ ] 프로젝트 문서, Base, urban-legend, 공식 Godot 근거의 우선순위를 지킨다.
- [ ] 사전 기술 추천안을 비판적으로 검토한다.
- [ ] 추천 구조가 최소 Phase 0인지 설명한다.
- [ ] 공용 10병종과 진영 Visual 분리를 유지한다.
- [ ] 별도 적군 데이터가 생기지 않도록 검증한다.
- [ ] Scene·상태·Resource·Signal 책임이 중복되지 않는다.
- [ ] 예상 파일과 단계가 구체적이다.
- [ ] headless와 수동 검증이 모두 있다.
- [ ] Goal 0002에 넘길 실제 결과를 정의한다.
- [ ] 미확정과 사용자 결정 요청을 분리한다.
- [ ] 마지막 상태가 `제안서 검토 대기 / 사용자 승인 전 구현 금지`다.

---

## 11. Plan Mode가 중단하고 확인해야 하는 경우

다음 상황에서는 임의 결정하지 않는다.

- 승인 책임 문서끼리 제품 구조가 충돌한다.
- 실제 저장소에 예상하지 못한 Godot 구현이 이미 존재한다.
- 공용 병종 계약을 지키기 위해 데이터 분리가 필요하다고 판단된다.
- 공식 stable 버전 또는 CLI가 사전 추천과 다르다.
- Phase 0 범위 안에서 전투·룰렛·건설 구현이 필수라고 판단된다.
- 외부 애드온이 없으면 테스트가 불가능하다고 판단된다.
- 960×540 정책이 제품 요구를 만족할 수 없다고 판단된다.

이 경우 제안서의 `확인 필요`와 `사용자 결정 요청`에 근거와 대안을 적는다.

---

## 12. 작업 종료 상태

Codex의 이번 채팅은 다음 상태로 끝나야 한다.

```text
저장소 조사 완료
→ Phase 0 구현 제안서 제출
→ 사용자 검토 대기
→ 구현 파일 변경 없음
→ 브랜치·커밋·PR 없음
```
