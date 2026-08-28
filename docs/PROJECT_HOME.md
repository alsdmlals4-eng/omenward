# OMENWARD · Project Home

```yaml
updated_at: 2026-08-28
status: CURRENT_REPOSITORY_PROJECT_HOME
source_migration: docs/migrations/OMENWARD_NOTION_CURRENT_CONTENT_TO_REPOSITORY_MIGRATION_2026-08-28.md
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
current_gdd: docs/OMENWARD_GDD_CURRENT_CANON.md
```

이 문서는 기존 Notion Project Home의 사람용 진입 구조를 저장소로 옮긴 **현재 단일 시작점**이다. 상세 규칙은 아래 owner를 따르며, 이 페이지는 그것을 중복해서 새 정본으로 만들지 않는다.

## 지금의 게임

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

플레이어는 징조수호관으로서 세 전선의 압력을 읽고, Stage 2부터 건물과 TokenSource로 동원 확률을 설계한다. 3×3 징조륜을 제한적으로 조작해 얻은 병력은 한 전선에 비가역 커밋되며, 전투 뒤에는 인과 Review로 다음 설계를 고친다.

Stage 1은 직접 건설이 아니라 `열린 전장의 본진 지휘·방어 → 전진기지의 자동공격탑과 잠긴 건설 패드 발견 → 3×3 룰렛 → 비가역 전선 커밋`을 설명하는 첫 학습이다. 양쪽 본진에는 생산 건물·울타리 없이 패드 4개·고정탑 2개, 각 전진기지에는 패드 2개·고정탑 1개가 열린 지형 landmark로 있다. 고정 전진 바리케이드는 없으며, 점령 중인 전진기지의 건설 노드는 안정적으로 아군이 소유한 때만 활성화된다. 상세는 `docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_TOWER_ONLY_FORWARD_LAYOUT_2026-08-28.md`가 소유한다.

## 현재 상태와 증거 한계

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 27
CURRENT_NEXT = USER_CONFIRM_OPEN_BATTLEFIELD_TOWER_ONLY_PLANNING_BOARD
FORWARD_DEFENSE_OCCUPATION_NODES = CONFIRMED__PLANNING_ONLY__NOT_IMPLEMENTED
OPEN_BATTLEFIELD_TOWER_ONLY_LAYOUT = CONFIRMED__PLANNING_ONLY__NOT_IMPLEMENTED
CURRENT_TARGET_RUNTIME_ASSET = NOT_CREATED
CURRENT_RUNTIME_EVIDENCE = PARTIAL__TECHNICAL_ONLY
HUMAN_USABILITY_AND_PLAYER_EXPERIENCE = NOT_RUN
```

새 전장 방향은 하나의 Ward 본진에서 상·중·하 세 shared front로 갈라져 하나의 Veil 본진으로 수렴하는 전략 지도다. 세 전선은 한 화면에서 동시에 읽혀야 하며, 전선별 미니맵은 주 전략 지도에 흡수된다. 현재 v6 보드는 생성 탐색물일 뿐 runtime asset, Godot 적용, 사람 검증 결과가 아니다.

## 저장소 탐색 구조

```text
Project Home
├─ Current Canon / 현재 상태
│  ├─ docs/CURRENT_CONFIRMED_DECISIONS.md
│  ├─ docs/ACTIVE_CONTEXT.md
│  ├─ docs/PROJECT_CORE.md
│  └─ docs/OMENWARD_GDD_CURRENT_CANON.md
├─ Direction / Flow / Work Plan
│  ├─ docs/design/APPROVED_OMENWARD_*
│  ├─ docs/OMENWARD_ROADMAP.md
│  └─ docs/DECISIONS_PENDING.md
├─ Visual / UX / Asset
│  ├─ docs/superpowers/specs/2026-08-28-storybook-sd-three-front-strategic-map-design.md
│  ├─ docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_TOWER_ONLY_FORWARD_LAYOUT_2026-08-28.md
│  ├─ docs/images/planning/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28.md
│  ├─ docs/images/approved/OMENWARD_RUN_COMMAND_VISUAL_ASSET_MANIFEST_2026-08-27.json
│  └─ docs/ASSET_RIGHTS_AND_PROVENANCE_RECORD.md
├─ Production / Validation
│  ├─ docs/HANDOFF_CONTEXT.md
│  ├─ docs/CURRENT_IMPLEMENTATION_STATUS.md
│  ├─ docs/implementation/
│  └─ docs/qa/
└─ Migration / Historical compatibility
   ├─ docs/migrations/OMENWARD_NOTION_CURRENT_CONTENT_TO_REPOSITORY_MIGRATION_2026-08-28.md
   └─ docs/archive/
```

## 운영 원칙

- 현재 사람용·구조화 정본은 repository이다.
- Notion은 이번 읽기 전용 마이그레이션 이후 historical reference로만 보존한다. 새 기록·수정·삭제는 하지 않는다.
- 이미지 안의 문구·수치·pseudo-text는 정본이 아니다. 정확한 규칙은 Markdown/JSON/code/data/Scene/Resource/test/runtime evidence owner가 소유한다.
- 현재 목적에 필요 없는 구형 Notion 데이터는 이 Home으로 옮기지 않고 migration 대장에 historical/superseded로만 기록한다.

## 빠른 시작 순서

1. `README.md`와 `AGENTS.md`.
2. `docs/CURRENT_CONFIRMED_DECISIONS.md`와 `docs/ACTIVE_CONTEXT.md`.
3. 위 GDD/Project Core와 해당 작업의 current owner.
4. 실제 code/data/Scene/Resource/test/runtime evidence.
5. GitHub의 open/draft PR·Issue는 매번 fresh 조회한다.
