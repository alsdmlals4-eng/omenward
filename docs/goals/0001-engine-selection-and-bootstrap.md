# Goal 0001 — Codex Phase 0 Plan Mode 제안서

> 상태: **새 Codex 채팅 작업 패키지 준비 완료 / Codex Plan Mode 실행 대기 / 구현 금지**

@Superpowers Use this repository's spec-first workflow.
Use Codex Plan Mode for this pass.
Do not create or modify `project.godot`, Scene, script, Resource, data, asset, test, branch, commit, or pull request.
First inspect the repository and submit a proposal using `docs/PROPOSAL_WORKFLOW.md`.

## Goal

새 Codex 채팅에서 오멘워드의 승인 기획서, 공용 지식, 참고 프로젝트와 실제 저장소 상태를 읽기 전용으로 조사하고, Godot + GDScript 기반 Phase 0 기술 기준선을 위한 구현 제안서를 작성한다.

이번 실행의 산출물은 구현물이 아니라 **Codex가 실제 조사 후 제출하는 Plan Mode 제안서**다.

## 현재 작업 입력

- 작업 요청·복사 프롬프트: `docs/work_orders/0001-phase-0-codex-plan-mode.md`
- 사전 기술 추천안: `docs/design/proposals/0001-phase-0-godot-bootstrap.md`
- 제안서 형식: `docs/PROPOSAL_WORKFLOW.md`
- 현재 Issue: #1

사전 기술 추천안은 이미 승인된 Plan Mode 결과가 아니다. Codex는 실제 저장소와 공식 근거를 확인해 채택·수정·기각 이유를 제시한다.

## 사용자 가치

Codex가 이전 대화 없이도 다음을 정확히 이해하고 계획하게 한다.

- 오멘워드의 핵심 플레이 경험과 전장 구조.
- 공용 10병종 데이터와 진영별 이미지 분리.
- 적군 전용 데이터·Scene·모션을 만들지 않는 원칙.
- 시간·결정론·애니메이션 판정의 책임 경계.
- 현재 저장소의 실제 구현 유무.
- Phase 0과 수직 슬라이스의 범위 차이.
- 사용자 승인 전 구현 금지.

## 새 Codex 채팅 읽기 순서

1. `AGENTS.md`
2. `docs/BASE_RULES_VERSION.md`
3. `docs/HANDOFF_CONTEXT.md`
4. `docs/DOCUMENTATION_MAP.md`
5. `docs/PROPOSAL_WORKFLOW.md`
6. `docs/work_orders/0001-phase-0-codex-plan-mode.md`
7. `docs/OMENWARD_GAME_DESIGN.md`
8. `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`
9. `docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`
10. `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`
11. `docs/design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md`
12. `docs/design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md`
13. `docs/GODOT_PROJECT_STRUCTURE.md`
14. `docs/DECISIONS_PENDING.md`
15. `docs/OMENWARD_ROADMAP.md`
16. 이 Goal과 Issue #1
17. 실제 저장소 파일·테스트
18. `docs/design/proposals/0001-phase-0-godot-bootstrap.md`

## 참고 저장소

필요한 파일만 읽는다.

### Base

- `AGENTS.md`
- `docs/knowledge/README.md`
- `docs/knowledge/methods/PROJECT_HANDOFF_CONTEXT_METHOD.md`
- `docs/knowledge/methods/CODEX_PLAN_MODE_WORK_PACKAGE_METHOD.md`
- `docs/knowledge/methods/ANIMATION_AND_PRESENTATION_METHOD.md`
- `docs/knowledge/research/DESIGN_RESEARCH_AND_EVIDENCE_METHOD.md`
- `docs/knowledge/cases/OMENWARD_SHARED_ARCHETYPE_FACTION_VISUAL_CASE.md`

### urban-legend

- `AGENTS.md`
- `project.godot`
- README의 실제 폴더·실행·검증 구조
- 상태 소유·데이터 로딩·네이티브 UI·headless 검증 관련 실제 파일

Base와 urban-legend는 방법·사례 참고다. 오멘워드의 최신 사용자 지시와 승인 책임 문서를 덮어쓸 수 없다.

## 승인된 결정

- 프로젝트명: 오멘워드 / OMENWARD.
- 엔진 계열: Godot, 기본 언어 GDScript.
- Windows PC / 마우스·키보드 / 싱글플레이 PvE.
- Godot 기본 Scene, Node, Resource, Signal, Control/Container/Theme 우선.
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

- 아군과 적군은 스탯·스킬·타기팅·점령·구조물 피해·애니메이션 상태·판정 타이밍을 공유한다.
- 별도 `EnemyUnitProfile`, 적군용 Unit Scene, 적군 전용 전투 데이터·모션 상태 머신을 만들지 않는다.
- 아군·적군 차이는 팀, 출격 방식과 이미지·초상화·아이콘·팔레트·표시명이다.
- 일반 적 웨이브는 공용 `archetype_id`를 참조한다.
- 보스는 공용 base archetype에 행동·페이즈 패키지와 전용 Visual Set을 추가한다.

## Codex가 검토할 결정

각 항목에 추천안, 이유와 필요한 대안의 장단점을 제시한다.

### 엔진·화면

- 현재 공식 Godot stable 버전과 standard/.NET.
- renderer.
- 1920×1080 출력과 내부 논리 해상도·stretch.
- 픽셀 스냅과 1280×720 QA.

### 폴더·Scene·상태

- 최소 Scene·Script·Resource·Data·Test 구조.
- Main, GameSession, 시간·난수·Registry의 상태 소유.
- AutoLoad 사용 여부.
- Signal·의존성 주입과 전역 이벤트 버스 경계.

### 데이터

- UnitArchetypeProfile, TierProfile, RankProfile.
- FactionVisualProfile, AnimationContract.
- BuildingProfile, BattlefieldProfile, StageManifest.
- BossBehaviorPackage와 BossPhaseProfile의 Phase 0 범위.
- Resource·JSON·CSV 경계.
- 공용 데이터·진영 이미지·런타임 인스턴스 참조 흐름.

### 애니메이션·자산

- AnimatedSprite2D, AnimationPlayer 또는 조합.
- 상태·프레임·피벗·impact/projectile 이벤트 데이터.
- 양 진영 Visual Set 호환 검사.
- 전투 판정과 시각 이벤트의 권위 분리.

### 시간·결정론·검증

- real_time / active_combat_time / ui_planning_time.
- 고정 tick과 planning 정지.
- seed·RNG stream·input log.
- headless 명령과 Windows 실행 경로 처리.
- ID·참조·중복·Visual·전장 계약 검사.

## Plan Mode 포함 범위

- 현재 저장소와 문서의 실제 상태 조사.
- Base와 urban-legend의 적용 가능한 방법·구조 분석.
- 사전 기술 추천안의 비판적 검토.
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

## Codex 제안서 필수 내용

- 확인한 실제 파일과 근거.
- 추천 Godot 버전 및 대안.
- 예상 Scene 트리와 파일 경로.
- 공용 Unit Scene·UnitArchetype·FactionVisual·AnimationContract 책임.
- AutoLoad와 런타임 상태 소유.
- 데이터 형식과 Resource 경계.
- 전장·시간·결정론 구조.
- 양 진영 Visual Set 호환 자동 검사.
- headless와 수동 검증 명령.
- 단계별 구현·커밋 계획.
- Goal 0002 진입 조건.
- 사용자 결정 목록.

## 이번 Goal 완료 기준

- [ ] 새 Codex 채팅이 작업 요청서를 읽었다.
- [ ] 실제 저장소와 참고 자료를 읽기 전용으로 조사했다.
- [ ] 코드와 데이터 변경 없이 Codex Plan Mode 제안서가 작성됐다.
- [ ] 사전 추천안의 채택·수정·기각 이유가 명확하다.
- [ ] 예상 파일·Scene·Resource 책임이 실제 저장소 기준으로 제시됐다.
- [ ] 공용 10병종과 진영별 Visual Set 구조가 유지된다.
- [ ] 적군 전용 데이터·Scene 복제를 방지하는 검증이 있다.
- [ ] 최신 전장·UI·애니메이션·성능 계약을 반영한다.
- [ ] headless와 수동 확인 순서가 있다.
- [ ] 위험과 미확정이 분리된다.
- [ ] 마지막 상태가 `제안서 검토 대기 / 사용자 승인 전 구현 금지`다.

## 승인 후 예상 Phase 0 구현

아래는 Codex 제안서를 사용자가 승인한 뒤 별도 실행에서만 수행한다.

- `project.godot`과 최소 Main Scene.
- 승인된 폴더·상태·시간·결정론 골격.
- 승인된 공용 병종·Visual·Animation 데이터 골격.
- 승인된 참조·중복·전장·Visual 검증기.
- 승인된 headless 테스트 러너.
- README 실행·검증 명령.
- Goal 0002와 Issue #32의 실제 경로 갱신.

## 제출 상태

```text
현재 상태: 새 Codex 채팅 Plan Mode 실행 대기
Codex 제안서 미제출
사용자 승인 전 구현 금지
```
