# OMENWARD · Project Home

```yaml
updated_at: 2026-08-31
status: CURRENT_REPOSITORY_PROJECT_HOME
source_migration: docs/migrations/OMENWARD_NOTION_CURRENT_CONTENT_TO_REPOSITORY_MIGRATION_2026-08-28.md
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
current_gdd: docs/OMENWARD_GDD_CURRENT_CANON.md
```

이 문서는 기존 Notion Project Home의 사람용 진입 구조를 저장소로 옮긴 **현재 단일 시작점**이다. 상세 규칙은 아래 owner를 따르며, 이 페이지는 그것을 중복해서 새 정본으로 만들지 않는다.

## 지금의 게임

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

플레이어는 징조수호관으로서 하나의 전진 전선의 압력을 읽고, 전장 밖의 건물 목록과 TokenSource로 동원 확률을 설계한다. 3×3 징조륜을 제한적으로 조작해 얻은 병력은 단일 전선에 비가역 커밋되며, 전투 뒤에는 인과 Review로 다음 설계를 고친다.

Stage 1은 `전장 우선 교전 관측 → 전진기지/접전지의 점령 효과를 미니맵에서 확인 → 3×3 룰렛 → 비가역 단일 전선 커밋`을 설명하는 첫 학습이다. 전장에는 가까운 교전 지형, 유닛, 목표와 고정 방어탑 한 개만 보인다. 다섯 구간의 행군 상태는 읽기 전용 미니맵으로 압축하고, 건설 패드·건설 노드·건물 지도 배치는 없다. 건물은 플레이어 전용 목록에서만 올리고, 활성 건물 상한은 기본 6칸에 안정적으로 보유한 전진기지와 접전지 수를 더한 값이다. 화면 계층은 `docs/design/APPROVED_OMENWARD_BATTLE_PRIMARY_MARCH_MINIMAP_2026-08-30.md`, 도메인은 `docs/design/APPROVED_OMENWARD_SINGLE_MARCH_FRONT_AND_THREE_TAB_COMMAND_2026-08-30.md`가 소유한다.

## 현재 상태와 증거 한계

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 31
CURRENT_VISUAL_DECISION = OMW-PLAN-20260830-BATTLE-PRIMARY-MARCH-MINIMAP-01
CURRENT_NEXT = RUNTIME_TECHNICAL_SMOKE_OF_SEQUENTIAL_FRONT_TRANSITION__THEN_USER_VISUAL_CONFIRMATION
FORWARD_DEFENSE_OCCUPATION_NODES = SUPERSEDED_IN_SCOPE__GLOBAL_ROSTER_IMPLEMENTED__MACHINE_VERIFIED
OPEN_BATTLEFIELD_TOWER_ONLY_LAYOUT = GLOBAL_ROSTER_AND_FIXED_TOWERS__IMPLEMENTED__RUNTIME_TECHNICAL_SMOKE_PASS
CURRENT_TARGET_RUNTIME_ASSET = OMW-IMG-20260831-CLOSE-FRONT-BATTLEFIELD-MODULAR-V1__CANON_REGISTERED__IMPLEMENTED
CURRENT_RUNTIME_UNIT_PAIR = OMW-IMG-20260830-STORYBOOK-SD-SHIELD-GUARD-PAIR-V1__IMPLEMENTED__RUNTIME_TECHNICAL_SMOKE_PASS__HUMAN_NOT_RUN
CURRENT_RUNTIME_EVIDENCE = PARTIAL__BATTLE_PRIMARY_MACHINE_VERIFIED__MODULAR_CLOSE_BATTLEFIELD_RUNTIME_TECHNICAL_SMOKE_PASS
HUMAN_USABILITY_AND_PLAYER_EXPERIENCE = NOT_RUN
```

새 전장 방향은 Ward 본진에서 Veil 본진으로 넓고 매끄럽게 이어지는 하나의 전진 경로다. 경로 위에는 Ward 전진기지, 접전지, Veil 전진기지, 관문이 순서대로 있고, 방어탑은 Ward 전진기지를 안정적으로 지배할 때만 플레이어 소유가 되는 한 개의 고정 시설이다. 전장에는 정본 등록된 modular foundation과 양 진영 terrain props를 사용하며, props는 병사의 중앙 이동 통로와 겹치지 않고 양쪽 외곽 상·하단에만 배치된다. Shield Guard pair는 기존 승인 범위에서 런타임에 연결되어 단일 전선 technical smoke를 통과했지만, 사람 검증은 `NOT_RUN`이다.

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
│  ├─ docs/design/APPROVED_OMENWARD_BATTLE_PRIMARY_MARCH_MINIMAP_2026-08-30.md
│  ├─ docs/superpowers/plans/2026-08-30-battle-primary-march-minimap.md
│  ├─ docs/design/APPROVED_OMENWARD_SINGLE_MARCH_FRONT_AND_THREE_TAB_COMMAND_2026-08-30.md
│  ├─ docs/images/candidates/OMENWARD_SINGLE_MARCH_FRONT_TERRAIN_CANDIDATE_2026-08-30.md
│  ├─ docs/images/planning/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28.md
│  ├─ docs/images/approved/OMENWARD_STORYBOOK_SD_SHIELD_GUARD_TRUE_ALPHA_PAIR_V1.md
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
