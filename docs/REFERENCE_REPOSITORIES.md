# 참고 저장소 적용 기준

- 갱신일: 2026-07-16
- 현재 프로젝트: 오멘워드 / OMENWARD

이 문서는 `Base`와 `urban-legend`에서 오멘워드에 활용할 작업 방법, 지식과 Godot 구조를 기록한다. 참고 저장소의 코드를 통째로 복사하거나 변경을 자동 병합하지 않는다.

## 기준 버전

- Base: `alsdmlals4-eng/Base` 기준 커밋 `b6b51509a8f6b841ddfafe44ddfd1539ba443a03`
- urban-legend: `alsdmlals4-eng/urban-legend` 검토 커밋 `b36c82c3a44cc4104295766e1f32c93274001ad4`
- 검토일: `2026-07-16`

참고 저장소가 변경되어도 이 문서의 적용 결론은 자동 변경되지 않는다. 새 기준을 가져올 때는 프로젝트 책임 문서와 충돌을 확인하고 별도 문서 커밋으로 갱신한다.

## 우선순위

```text
오멘워드 최신 사용자 결정
→ AGENTS.md
→ HANDOFF_CONTEXT.md
→ 프로젝트 승인 책임 문서
→ 현재 Issue·Goal·승인 제안서
→ 실제 파일과 테스트
→ 고정된 Base·urban-legend 참고
```

Base와 urban-legend는 프로젝트 최신 결정을 덮어쓸 수 없다.

## Base에서 채택

### Spec-first와 승인 게이트

- 사용자 의견→사양 구체화→책임 문서→Issue/Goal→Plan Mode→승인→구현→검증 순서.
- 코드·Scene·Resource·데이터 구조는 제안서 승인 뒤 변경.
- 관찰 가능한 완료 기준과 실제 실행 명령 사용.
- 테스트하지 않은 결과를 완료로 보고하지 않음.

### 문서 인수인계

참고:

- `docs/knowledge/methods/PROJECT_HANDOFF_CONTEXT_METHOD.md`
- `docs/knowledge/skills/DESIGN_HANDOFF_AND_REVIEW_SKILL_MATRIX.md`

채택:

- `docs/HANDOFF_CONTEXT.md`를 콜드 스타트 시작점으로 사용.
- Handoff, GDD, Roadmap, Documentation Map, Active Context와 현재 Issue를 동기화.
- 승인·PoC·미확정·구현·검증 상태를 분리.
- 한 주제당 활성 책임 원본 하나.
- 콜드 스타트 질문으로 인수인계 품질 검수.

### 아트 디렉션

참고:

- `docs/knowledge/methods/ART_DIRECTION_METHOD.md`
- `docs/knowledge/skills/ART_DIRECTION_SKILL_MATRIX.md`

채택:

- 콘셉트 크기보다 실제 전략 줌과 화면 픽셀 크기 우선.
- 실루엣→축소→다수 겹침→HUD·VFX 포함 순서로 검수.
- 진영·병종·등급을 색상만으로 구분하지 않음.
- 생성형 콘셉트는 탐색용이며 픽셀·손·관절·무기·문자·광원 후처리 필수.

### 애니메이션·전투 연출

참고:

- `docs/knowledge/methods/ANIMATION_AND_PRESENTATION_METHOD.md`
- `docs/knowledge/skills/ANIMATION_PRESENTATION_SKILL_MATRIX.md`

채택:

- 공격 준비→판정→회복 분리.
- 판정과 접촉·투사체 이벤트 동기화.
- 이동 위치는 코드가 소유하고 루트 모션 사용 안 함.
- 다수 유닛에서 큰 피격·히트 스톱·화면 흔들림 제한.
- 공용 전투·AnimationContract와 진영별 Visual Set 분리.

### 조사·벤치마킹

참고:

- `docs/knowledge/research/DESIGN_RESEARCH_AND_EVIDENCE_METHOD.md`
- `docs/BENCHMARKING_REFERENCE_GUIDE.md`

채택:

- 결정할 질문과 종료 조건을 먼저 작성.
- 1차 출처·직접 관찰을 우선.
- 사례의 표면보다 해결한 문제와 전제를 분석.
- 반드시 반영, PoC 검증, 조건부 참고, 제외로 결론 분류.
- 공용 가치가 있는 결과는 Base cases로 일반화.

### Base 사례

오멘워드에서 추출되어 Base에 기록된 사례:

- `OMENWARD_SHARED_ARCHETYPE_FACTION_VISUAL_CASE.md`
- `OMENWARD_TACTICAL_VISIBILITY_WITHOUT_MINIMAP_CASE.md`
- `OMENWARD_FOGGED_SPECIALIST_ROUTE_CASE.md`
- `OMENWARD_CANONICAL_HANDOFF_CONTEXT_CASE.md`

사례는 현재 프로젝트 기획서의 복사본이 아니라 문제·판단·재사용 원칙을 설명한다.

## Base에서 그대로 가져오지 않음

- 다른 프로젝트의 세계관·밸런스·엔진 파일·저장 스키마.
- 프로젝트에 없는 도구·플러그인 강제.
- 작은 작업에도 과도한 산출물과 gate를 요구하는 운영.
- Base 원격 변경 자동 병합.
- 사례 문서의 프로젝트 특화 수치와 표면 디자인.
- 아직 검증되지 않은 Base 가설을 오멘워드 승인 규칙으로 자동 채택.

## urban-legend에서 채택

### Godot 기본 폴더 분리

- Scene: `scenes/`.
- Script: `scripts/`.
- 정적·대량 데이터: `data/`.
- 공유 Resource: `resources/`.
- 검증: `tests/`.
- 자산: `assets/`.

실제 필요한 폴더만 Phase 0에서 생성한다.

### 상태 소유자 단일화

- 여러 Scene이 공유하는 세션 상태·서비스만 AutoLoad 후보.
- Unit·Building·Gate·Strongpoint 런타임 상태는 해당 인스턴스가 소유.
- UI 임시 선택 상태는 UI가 소유.
- 같은 값을 AutoLoad와 Scene이 동시에 원본으로 관리하지 않음.

### 데이터 기반 설계

urban-legend의 콘텐츠·상태 분리 사례를 다음 오멘워드 구조에 적용한다.

- UnitArchetypeProfile.
- TierProfile·RankProfile.
- FactionVisualProfile·AnimationContract.
- BuildingProfile·BattlefieldProfile.
- StageManifest·WavePatternCard.
- 공격·스킬·패시브·타기팅.

Godot에서 자주 조정할 타입 데이터는 Resource를 우선 검토하고, 대량 웨이브·외부 표 편집이 필요한 경우만 JSON/CSV를 비교한다.

### 네이티브 UI

- `Control`, `Container`, `Theme`, 재사용 Scene.
- 표시 데이터를 입력받고 사용자 의도를 Signal로 반환.
- UI가 전역 게임 상태와 규칙을 직접 수정하지 않음.
- 룰렛 칸, 결과 카드, 건설 상품, 웨이브 징조 같은 반복 단위만 컴포넌트화.
- 별도 CSS·가상 DOM·범용 데이터 바인딩 프레임워크를 만들지 않음.

### 검증 순서

1. 데이터 파싱·참조·중복 정적 검사.
2. `git diff --check`.
3. Godot headless 파싱·실행.
4. 변경 Scene 단독 확인.
5. 같은 시드 재현.
6. 실제 플레이 경로와 화면·모션 검수.

### 보호 경로 후보

- `project.godot`.
- 핵심 AutoLoad.
- UnitArchetype·Tier·Rank·공통 전투 데이터.
- FactionVisual·AnimationContract 스키마.
- BattlefieldProfile.
- 룰렛·경제·웨이브 원본.
- 저장 스키마가 생긴 뒤 저장 코드.

## urban-legend에서 그대로 가져오지 않음

- 비주얼노벨·조사·에피소드 전용 Scene과 데이터.
- urban-legend의 세계관·대사·자산.
- F2 UI 편집기와 콘텐츠 override 구조.
- 기존 AutoLoad 이름·게임 상태 필드.
- 현재 오멘워드에 필요 없는 대형 에디터·프레임워크.

## 오멘워드 전용 확장

- 공용 UnitArchetype 10개와 진영별 Visual Set.
- 다수 유닛의 3라인 이동·타기팅·교전.
- 라인별 성문과 중간거점 권한 이전.
- 건물 노드·폐허·생산·토큰 연쇄.
- 건물 개수 기반 룰렛 풀.
- 공용 archetype 기반 적 웨이브.
- 암살자 오프맵 우회.
- 공격 판정과 AnimationContract 이벤트 동기화.
- 공용 데이터·양 진영 이미지 호환 검사.
- 동시 객체·투사체·VFX 성능 예산.

## 작업별 참고 절차

1. `docs/HANDOFF_CONTEXT.md`에서 현재 방향과 불변 조건을 확인한다.
2. Documentation Map에서 프로젝트 책임 원본을 선택한다.
3. 현재 Issue/Goal의 문제와 완료 기준을 확인한다.
4. Base에서는 방법·스킬·유사 사례만 찾는다.
5. urban-legend에서는 같은 Godot 문제를 해결한 실제 파일만 확인한다.
6. 오멘워드의 화면·성능·공용 데이터 요구와 맞지 않는 구조를 제외한다.
7. 채택·제외·위험·검증을 제안서에 기록한다.
8. 구현 뒤 실제 이득이 확인된 교훈만 프로젝트 규칙 또는 Base 사례·방법 승격 후보로 남긴다.
