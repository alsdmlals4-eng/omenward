# Goal 0001 — Godot 프로젝트 부트스트랩 제안서

> 상태: **Codex Plan Mode 제안서 검토 대기 / 구현 금지**

@Superpowers Use this repository's spec-first workflow.
Use Codex Plan Mode for this pass.
Do not create or modify `project.godot`, Scene, script, Resource, data, asset, test, branch, commit, or pull request.
First inspect the repository and submit a proposal using `docs/PROPOSAL_WORKFLOW.md`.

## Goal

Godot + GDScript 기반 최소 실행 프로젝트를 어떤 버전·구조·데이터 계약·검증 방식으로 부트스트랩할지 제안하고, 사용자가 검토할 수 있는 구현 계획을 작성한다.

이번 실행의 산출물은 구현물이 아니라 **Phase 0 제안서**다. 사용자가 명시적으로 승인한 뒤 별도의 구현 실행으로 전환한다.

## 사용자 가치

Codex가 임의의 엔진 버전, 폴더, Unit Scene과 데이터를 먼저 고정하지 않고, 오멘워드의 최신 전장·룰렛·공용 병종·진영 Visual Set·애니메이션·성능 계약을 검토한 뒤 중복 없이 확장 가능한 기술 기반을 합의한다.

## 먼저 읽을 문서

1. `AGENTS.md`
2. `docs/BASE_RULES_VERSION.md`
3. `docs/HANDOFF_CONTEXT.md`
4. `docs/DOCUMENTATION_MAP.md`
5. `docs/DOCUMENT_LIFECYCLE.md`
6. `docs/PROPOSAL_WORKFLOW.md`
7. `docs/OMENWARD_GAME_DESIGN.md`
8. `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`
9. `docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`
10. `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`
11. `docs/design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md`
12. `docs/design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md`
13. `docs/GODOT_PROJECT_STRUCTURE.md`
14. `docs/REFERENCE_REPOSITORIES.md`
15. `docs/DECISIONS_PENDING.md`
16. `docs/OMENWARD_ROADMAP.md`
17. `docs/ACTIVE_CONTEXT.md`
18. GitHub Issue #1

참고 저장소는 필요한 파일만 읽는다.

### Base

- `AGENTS.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/knowledge/methods/PROJECT_HANDOFF_CONTEXT_METHOD.md`
- `docs/knowledge/methods/ANIMATION_AND_PRESENTATION_METHOD.md`
- `docs/knowledge/research/DESIGN_RESEARCH_AND_EVIDENCE_METHOD.md`
- `docs/knowledge/cases/OMENWARD_SHARED_ARCHETYPE_FACTION_VISUAL_CASE.md`

### urban-legend

- `AGENTS.md`
- `project.godot`
- README의 실제 폴더 구조
- Godot 상태 소유·데이터 로딩·네이티브 UI·headless 검증 관련 문서

Base와 참고 저장소는 방법·사례 참고이며 프로젝트 최신 승인 문서를 덮어쓸 수 없다.

## 승인된 결정

- 프로젝트명: 오멘워드 / OMENWARD.
- 엔진: Godot, 기본 언어 GDScript.
- Windows PC / 마우스·키보드 / 싱글플레이 PvE.
- Godot 기본 Scene, Node, Resource, Signal, Control/Container/Theme 우선.
- `.godot/`과 로컬 생성물 제외.
- 코드 작업 전 Plan Mode 제안서와 사용자 승인 필수.
- 좌우 대칭 독립 3라인, 라인별 성문·중간거점·중앙 접전지.
- 중간거점 전방 2·후방 1 노드와 점령 시 건설권·생산권 이전.
- 암살자 같은 라인 안개 우회로, 적 후방 직접 생성 금지.
- 기본 전략 화면 전체 전장 조망, 미니맵 없음.

### 공용 병종 데이터

```text
UnitArchetypeProfile × 10
+ TierProfile
+ RankProfile
+ owner_team_id
+ FactionVisualProfile
```

- 아군과 적군은 스탯·스킬·타기팅·애니메이션 상태·판정 타이밍을 공유한다.
- 별도 `EnemyUnitProfile`을 만들지 않는다.
- 아군·적군 차이는 팀, 출격 방식과 이미지·초상화·아이콘·팔레트·표시명이다.
- 일반 적 웨이브는 공용 `archetype_id`를 참조한다.
- 보스는 공용 base archetype에 행동·페이즈 패키지를 추가한다.

### 공용 애니메이션

- 한 archetype은 AnimationContract 하나를 사용한다.
- 아군·적군 시트는 같은 상태, 프레임 수, 배열, 피벗과 이벤트 프레임을 사용한다.
- 적군 전용 모션 상태 머신과 공격 타이밍 데이터는 만들지 않는다.
- 이동 위치는 코드가 소유하며 루트 모션을 사용하지 않는다.

## 제안서에서 검토할 결정

각 항목에 추천안, 이유와 대안의 장단점을 제시한다.

### 엔진·화면

- 정확한 Godot stable 버전.
- 1920×1080 출력과 내부 논리 해상도·stretch.
- 2D 픽셀 Camera2D, 확대·이동·픽셀 스냅.
- 첫 프로토타입 객체 수와 성능 검증.

### 폴더·Scene·상태

- 최소 Scene·Script·Resource·Data·Test 구조.
- 공용 Unit Scene과 UnitInstance 책임.
- Main, Battle, UI와 서비스의 상태 소유.
- AutoLoad를 처음부터 둘지 실제 공유 상태가 생길 때 추가할지.
- real_time / active_combat_time / ui_planning_time.
- 결정론적 난수·StageManifest·입력 로그.

### 데이터

- UnitArchetypeProfile, TierProfile, RankProfile.
- FactionVisualProfile, AnimationContract.
- Attack·Skill·Passive·Targeting Profile.
- BuildingProfile, BattlefieldProfile, StageManifest.
- BossBehaviorPackage와 BossPhaseProfile.
- Resource·JSON·CSV 경계.
- 공용 데이터·진영 이미지·런타임 인스턴스의 참조 흐름.

### 애니메이션·자산

- AnimatedSprite2D, AnimationPlayer 또는 조합 방식.
- 상태·프레임·피벗·이벤트 데이터 위치.
- 아군·적군 Visual Set 호환 검사.
- 공격 판정과 impact/projectile event 연결.
- 결정론적 루프 시작 오프셋.

### 검증

- headless 명령과 Windows Godot 경로.
- ID·참조·중복 데이터 검사.
- UnitArchetype 정확히 10개인지 검사.
- EnemyUnitProfile과 진영별 전투 데이터 복사본 금지 검사.
- 양 Visual Set의 프레임·피벗·이벤트 호환 검사.
- 일시정지·시드 재현·전장 불변 조건 검사.

## Plan Mode 포함 범위

- 현재 저장소와 문서의 실제 상태 조사.
- Base와 urban-legend에서 적용 가능한 방법·Godot 구조 분석.
- 예상 파일 목록과 책임.
- Scene 트리, 상태 소유와 Signal 흐름.
- 데이터·Resource 경계와 검증 seam.
- Phase 0을 작은 구현 단계로 나눈 계획.
- headless·에디터·수동 검증 순서.
- 위험, 대안, 미확정과 사용자 결정 요청.
- Goal 0002로 넘어가기 위한 종료 조건.

## Plan Mode 제외 범위

- `project.godot` 생성·수정.
- Scene, GDScript, Resource, 데이터와 테스트 생성·수정.
- 실제 스프라이트·애니메이션·VFX·오디오 제작.
- 외부 애드온·에셋·의존성 설치.
- 구현 브랜치·커밋·PR 생성.
- 전투·룰렛·건설·점령·성문·우회로·웨이브 구현.
- 적군 전용 병종 데이터 또는 Scene 생성.
- 미확정 기술 선택을 구현으로 고정.

## 제안서 필수 내용

- 확인한 실제 파일과 근거.
- 추천 Godot 버전 및 대안.
- 예상 Scene 트리와 파일 경로.
- 공용 Unit Scene·UnitArchetype·FactionVisual·AnimationContract 책임.
- AutoLoad와 런타임 상태 소유.
- 데이터 형식과 Resource 경계.
- 전장·시간·결정론 구조.
- 아군·적군 Visual Set 호환 자동 검사.
- headless와 수동 검증 명령.
- 단계별 구현·커밋 계획.
- Goal 0002 진입 조건.
- 사용자 결정 목록.

## 이번 Goal 완료 기준

- [ ] 코드와 데이터 변경 없이 제안서가 작성된다.
- [ ] 추천안과 선택하지 않은 대안의 이유가 명확하다.
- [ ] 실제 저장소 기준 예상 파일·Scene·Resource 책임이 제시된다.
- [ ] 공용 10병종과 진영별 Visual Set 구조가 유지된다.
- [ ] 적군 전용 데이터·Scene 복제를 방지하는 검증이 있다.
- [ ] 최신 전장·UI·애니메이션·성능 계약을 반영한다.
- [ ] headless와 수동 확인 순서가 있다.
- [ ] 위험과 미확정이 분리된다.
- [ ] 마지막 상태가 `제안서 검토 대기 / 승인 전 구현 금지`다.

## 승인 후 예상 Phase 0 구현

- `project.godot`.
- 최소 메인 Scene과 진입 Script.
- 필요한 최소 폴더.
- 해상도·Camera2D 기본 설정.
- 시간·시드·입력 로그 골격.
- 공용 UnitArchetype·Tier·Rank·FactionVisual·AnimationContract 골격.
- 참조·중복·Visual 호환 검증기.
- headless 테스트 러너.
- README 실행·검증 명령.
- Goal 0002와 Issue #32의 실제 경로 갱신.

## 제안서 제출 상태

```text
현재 상태: 제안서 검토 대기
사용자 승인 전 구현 금지
```
