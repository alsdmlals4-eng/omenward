# Goal 0001 — Phase 0 Godot 부트스트랩 제안서 검토

> 상태: **제안서 작성 완료 / 사용자 검토 대기 / 구현 금지**

현재 제안서:

- `docs/design/proposals/0001-phase-0-godot-bootstrap.md`

현재 Issue:

- GitHub Issue #1 `[Proposal Review][Phase 0] Godot·공용 병종 데이터 부트스트랩`

@Superpowers Use this repository's spec-first workflow.
Use Codex Plan Mode for review-only work until the user explicitly approves the proposal.
Do not create or modify `project.godot`, Scene, script, Resource, data, asset, test, branch, commit, or pull request as an implementation action.

## Goal

현재 Phase 0 제안서가 오멘워드의 최신 승인 구조, 실제 저장소 상태, 공용 병종 데이터 계약과 검증 요구를 정확히 반영하는지 검토하고, 사용자가 승인하거나 수정할 수 있는 상태를 유지한다.

이번 단계의 산출물은 구현물이 아니다.

```text
제안서 검토
→ 사용자 수정 요청 또는 명시적 승인
→ 승인 뒤 Goal 0001을 구현 실행 지시서로 갱신
→ 별도 구현 브랜치·PR
```

## 먼저 읽을 문서

1. `AGENTS.md`
2. `docs/BASE_RULES_VERSION.md`
3. `docs/HANDOFF_CONTEXT.md`
4. `docs/DOCUMENTATION_MAP.md`
5. `docs/PROPOSAL_WORKFLOW.md`
6. `docs/OMENWARD_GAME_DESIGN.md`
7. `docs/OMENWARD_ROADMAP.md`
8. `docs/ACTIVE_CONTEXT.md`
9. `docs/DECISIONS_PENDING.md`
10. `docs/GODOT_PROJECT_STRUCTURE.md`
11. `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`
12. `docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`
13. `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`
14. `docs/design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md`
15. `docs/design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md`
16. `docs/design/proposals/0001-phase-0-godot-bootstrap.md`
17. GitHub Issue #1
18. 실제 저장소 파일 상태

Base와 `urban-legend`는 제안서에 이미 정리된 적용·제외 결론을 검증할 때 필요한 파일만 확인한다.

## 실제 저장소 상태

- `project.godot` 없음.
- 구현된 `.tscn`·GDScript 프로젝트 구조 없음.
- 현재는 문서 중심 프리프로덕션 저장소.
- 사용자 승인 전 최초 Godot 프로젝트를 생성하지 않음.

## 승인된 불변 조건

### 공용 병종 데이터

```text
UnitArchetypeProfile × 10
+ TierProfile
+ RankProfile
+ owner_team_id
+ FactionVisualProfile
```

- 아군·적군은 능력치·스킬·타기팅·점령·구조물 피해·AnimationContract를 공유한다.
- 별도 `EnemyUnitProfile`, 적군용 Unit Scene, 적군 전용 stats·skills·targeting·animation을 만들지 않는다.
- 차이는 팀, 출격 방식과 이미지·초상화·아이콘·팔레트·표시명이다.
- 일반 적 웨이브는 공용 `archetype_id`를 참조한다.
- W15·W20 보스는 공용 base archetype에 BossBehaviorPackage·BossPhaseProfile·전용 Visual Set을 추가한다.

### 전장

- 좌우 대칭 독립 상·중·하 3라인.
- 라인별 양 진영 성문 총 6개.
- 중간거점 전방 2·후방 1 노드.
- 점령 시 건설권·생산권 이전.
- 중앙 접전지 라인 독립·건설 불가.
- 암살자 후방 직접 생성 금지, 같은 라인의 안개 우회로.
- 기본 전략 화면 전체 전장 조망, 미니맵 없음.

### 애니메이션

- 한 archetype은 AnimationContract 하나를 사용한다.
- 양 진영 Visual Set은 상태·프레임 수·배열·피벗·이벤트 프레임을 공유한다.
- 이동 위치는 코드가 소유하며 루트 모션을 사용하지 않는다.
- 공격은 준비→판정→회복.

## 제안서 추천안 요약

### 엔진·화면

```text
Godot 4.7.1 standard x86_64
GDScript
Compatibility renderer
1920×1080 출력
960×540 내부 viewport
viewport stretch / keep aspect / integer scale
```

- 1280×720은 정수 확대 레터박스 상태로 QA.
- 레터박스가 허용 불가하면 640×360 대안을 다시 검토.

### 상태·결정론

```text
Main
└─ GameSession
   ├─ CombatClock
   ├─ DeterminismService
   └─ DataRegistry
```

- Phase 0 AutoLoad 없음.
- 60Hz `active_combat_tick`.
- planning 중 active tick 정지, UI 계속 동작.
- master seed와 이름 기반 RNG stream.
- input log 기록·재생 골격.

### 데이터

- typed `.tres`: UnitArchetype·Tier·Rank·FactionVisual·AnimationContract·Battlefield.
- JSON: StageManifest·replay/input log.
- CSV: Phase 0 런타임 원본으로 사용하지 않음.
- 공용 archetype 10개.
- Tier 3개, player Rank 4개.
- AnimationContract 10개.
- allied Visual Profile 10개, veil Visual Profile 10개.
- placeholder 이미지는 진영별 두 장을 공유.

### 검증

```powershell
$env:GODOT_BIN = "C:\Tools\Godot\Godot_v4.7.1-stable_win64_console.exe"
& $env:GODOT_BIN --version
& $env:GODOT_BIN --headless --path . --editor --quit
& $env:GODOT_BIN --headless --path . --script res://tests/run_all.gd
& git diff --check
```

## 현재 검토 범위

- 제안서 내부 모순과 누락.
- 승인 책임 문서와의 충돌.
- 실제 저장소 상태를 잘못 가정한 경로.
- 공용 10병종·양 진영 Visual 구조의 중복 위험.
- Godot 버전·renderer·화면 정책의 장단점.
- AutoLoad 미사용과 상태 소유.
- Resource·JSON·CSV 경계.
- 시간·시드·입력 로그와 headless 테스트 계획.
- Phase 0과 수직 슬라이스 범위의 분리.

## 현재 제외 범위

- `project.godot` 생성·수정.
- Scene, GDScript, Resource, 데이터, 자산, 테스트 생성·수정.
- 구현 브랜치·커밋·PR.
- 실제 전투·룰렛·건설·점령·성문·우회로·웨이브 구현.
- 적군 전용 병종 데이터 또는 Scene.
- 최종 스프라이트·VFX·오디오.

## 제안서 검토 완료 기준

- [x] 현재 저장소에 Godot 프로젝트가 없음을 근거로 기록했다.
- [x] 공식 Godot stable 버전과 문서 근거를 기록했다.
- [x] 추천안과 대안을 분리했다.
- [x] 예상 Scene·Script·Resource·Data·Test 경로를 제시했다.
- [x] 공용 10병종과 양 진영 Visual Set 계약을 유지했다.
- [x] 적군 전용 데이터 복제를 막는 자동 검증을 포함했다.
- [x] 시간·시드·입력 로그·planning pause 구조를 제시했다.
- [x] headless와 수동 검증 명령을 제시했다.
- [x] Phase 0 구현 단계와 Goal 0002 진입 조건을 제시했다.
- [x] 마지막 상태를 `제안서 검토 대기 / 승인 전 구현 금지`로 유지했다.

## 사용자 결정 요청

추천안 전체로 구현 준비를 승인할 경우:

```text
제안서 승인
```

변경이 필요하면 다음 중 항목을 지정한다.

- Godot 버전·renderer.
- 960×540과 1280×720 레터박스 정책.
- Phase 0 AutoLoad 미사용.
- Resource·JSON·CSV 경계.
- 공용 10개 archetype·20개 Visual Profile 골격 범위.

## 승인 뒤 처리

사용자가 명시적으로 승인한 뒤에만:

1. Goal 0001을 구현 실행 프롬프트로 갱신한다.
2. Issue #1을 구현 준비 상태로 갱신한다.
3. `codex/issue-1-phase-0-bootstrap` 형태의 브랜치를 생성한다.
4. 제안서 단계 순서로 작은 커밋을 만든다.
5. 자동·수동 검증 증거와 함께 PR을 만든다.

승인 전에는 위 작업을 하지 않는다.

```text
현재 상태: 제안서 검토 대기
사용자 승인 전 구현 금지
```
