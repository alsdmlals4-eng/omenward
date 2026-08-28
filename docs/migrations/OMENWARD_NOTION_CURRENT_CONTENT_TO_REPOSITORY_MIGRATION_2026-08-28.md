# OMENWARD · Notion 현재 구조·작업물 → Repository 마이그레이션

```yaml
migration_id: OMW-OPS-20260828-NOTION-CURRENT-CONTENT-TO-REPOSITORY-01
completed_at: 2026-08-28 KST
authority_after_migration: REPOSITORY_ONLY
notion_access: USER_APPROVED_READ_ONLY__NO_WRITE_OR_DELETE
scope: CURRENT_STRUCTURE / CURRENT_WORK / CURRENT_ASSET_AND_PRODUCTION_LINKS
legacy_data_handling: HISTORICAL_OR_SUPERSEDED__NOT_COPIED_AS_CURRENT
notion_destination_write: NONE
no_base_promotion: USER_SELECTED_PROJECT_TOOLING_BOUNDARY
```

## 목적과 경계

사용자 요청에 따라 기존 Notion의 **현재 구조와 현재 작업 연결**을 저장소 문서로 옮겼다. Notion에 페이지·첨부·댓글·데이터베이스를 새로 쓰거나 수정하거나 삭제하지 않았다. 오래된 기획, superseded visual lock, 과거 queue는 현재 정본으로 복제하지 않고 lineage로만 분류했다.

이 문서는 Notion의 서버 백업이나 바이너리 복제본이 아니다. 현행 제품 의미·asset provenance·runtime consumer의 owner가 이미 repository에 있을 때는 원문을 중복하지 않고 그 owner를 명시한다.

## 읽기 전용 source identity

| Notion 구조/페이지 | Page ID | fresh fetch as-of | 판정 |
|---|---|---|---|
| `00 · 프로젝트 허브` | `3c01b237-eb1c-8141-93ae-c528c4f3c40c` | 2026-08-28T12:55:58Z | CURRENT_STRUCTURE |
| `오멘워드 · Home` | `3c41b237-eb1c-816f-bbc8-e2dddc18b6eb` | 2026-08-28T10:35:16Z | CURRENT_STRUCTURE_WITH_MIXED_HISTORY |
| `01 · 프로젝트 전체 작업계획` | `3c01b237-eb1c-8119-9eff-d7dd6159ec16` | 2026-08-28T10:35:20Z | CURRENT_WITH_STALE_ADDENDA |
| `03 · UI · 게임플레이 Flow Map` | `3c01b237-eb1c-812b-935f-caefb3290f61` | 2026-08-28T10:35:18Z | CURRENT_WITH_STALE_ADDENDA |
| `02 · 비주얼 바이블` | `3c01b237-eb1c-81c3-8be5-e3ee9f64b59d` | 2026-08-28T01:00:09Z | MIXED_CURRENT_HISTORICAL_SUPERSEDED |
| `13 · 비주얼 컴포넌트 · 전장/룰렛/UI` | `3c21b237-eb1c-81e2-9be2-d6ce397c9c85` | 2026-08-26T05:51:56Z | HISTORICAL_COMPONENT_LINEAGE |
| `04 · 에셋 라이브러리` | `3c01b237-eb1c-818c-a227-ee34eefd4534` | 2026-08-20T12:39:29Z | HISTORICAL_INDEX_STRUCTURE |
| `19 · 이미지 제작 · Runtime Consumer Asset Checklist` | `3c81b237-eb1c-8186-ad5c-f572abcd53f1` | 2026-08-28T01:00:03Z | CURRENT_LINKS_WITH_STALE_QUEUE |
| `06 · Production · Handoff` | `3c01b237-eb1c-810d-b6f9-c5c9046c5e6b` | 2026-08-28T01:00:14Z | MIXED_CURRENT_HISTORICAL_HANDOFF |

위 시간은 fetch 결과가 제공한 as-of 시각이며, source page의 현행 제품 authority를 의미하지 않는다.

## 이전 Notion 구조 → 현재 repository 구조

```text
Notion Project Hub
└─ OMENWARD Home
   ├─ Direction / 전체 작업계획
   ├─ Visual / UX / Components
   │  ├─ Visual Bible
   │  ├─ Flow Map
   │  ├─ Visual Components
   │  ├─ Asset Library
   │  └─ Runtime Consumer Asset Checklist
   └─ Production / Validation
      └─ Production / Handoff

Repository Project Home
├─ docs/PROJECT_HOME.md
├─ Current Canon: Current Decisions / Active Context / GDD / Project Core
├─ Direction / Flow: docs/design/, Roadmap, Decisions Pending
├─ Visual / UX / Asset: visual spec, planning records, approved manifests, provenance
├─ Production / Validation: Handoff, implementation, QA, actual project files/tests
└─ Migration / Historical: this report and docs/archive/
```

## 마이그레이션 대장

| Notion source | 보존한 현재 의미 또는 구조 | Repository owner | 상태 |
|---|---|---|---|
| Project Hub + OMENWARD Home | 사람용 Project Home → domain → detail 탐색 구조 | `docs/PROJECT_HOME.md`, `docs/DOCUMENTATION_MAP.md`, `docs/DOCUMENT_LIFECYCLE_REGISTRY.md` | MIGRATED |
| Home / Direction | 제품 정의, Player Promise, roadmap와 current decision routing | `README.md`, `docs/PROJECT_CORE.md`, `docs/OMENWARD_GDD_CURRENT_CANON.md`, `docs/CURRENT_CONFIRMED_DECISIONS.md`, `docs/ACTIVE_CONTEXT.md` | ALREADY_CURRENT_REPOSITORY_OWNER |
| Flow Map | `PREPARE → COMMIT → BATTLE → REVIEW`, atomic irreversible commit, Stage 1~5 learning flow | `docs/design/APPROVED_OMENWARD_RUN_COMMAND_SCREEN_FOCUS_MODES_2026-08-20.md`, `docs/design/APPROVED_OMENWARD_FIRST5_FTUE_MASTERY_LADDER_2026-08-20.md`, current GDD/Core | ALREADY_CURRENT_REPOSITORY_OWNER |
| Flow Map / current Stage 1 addendum | prebuilt defense system의 역할을 현재 바리케이드 + 자동공격탑으로 구체화하고 construction node lifecycle로 분리 | `docs/design/APPROVED_OMENWARD_FORWARD_DEFENSE_AND_OCCUPATION_NODE_CONTRACT_2026-08-28.md` | MIGRATED_AND_CORRECTED |
| Visual Bible | 현재 전략 지도 topology, 3전선 동시 가독성, map-only board boundary, style keep/avoid/drift | `docs/superpowers/specs/2026-08-28-storybook-sd-three-front-strategic-map-design.md`, `docs/images/planning/OMENWARD_FORWARD_DEFENSE_OCCUPATION_NODE_STRATEGIC_MAP_CANDIDATE_2026-08-28.md` | ALREADY_CURRENT_REPOSITORY_OWNER |
| Visual Components | 3×3 exposure, direct row/column control, focus-adaptive lower deck, silhouette-first token grammar | current GDD/Core + relevant `docs/design/APPROVED_OMENWARD_*` component owners | ALREADY_CURRENT_REPOSITORY_OWNER |
| Asset Library | 재사용 asset을 consumer·style·approval·provenance로 연결하는 구조 | `docs/images/approved/*MANIFEST*.json`, `docs/images/approved/*.md`, `.asset-vault/`, `docs/ASSET_RIGHTS_AND_PROVENANCE_RECORD.md` | MIGRATED_STRUCTURE__LOCAL_ASSET_OWNER_RETAINED |
| Runtime Consumer Asset Checklist | current consumer ↔ source ↔ derivative 관계와 evidence ceiling | `docs/images/approved/OMENWARD_RUN_COMMAND_VISUAL_ASSET_MANIFEST_2026-08-27.json`, `docs/images/approved/OMENWARD_RUN_COMMAND_VISUAL_ASSET_RUN_RECORD_2026-08-27.json`, `docs/CURRENT_IMPLEMENTATION_STATUS.md` | ALREADY_CURRENT_REPOSITORY_OWNER |
| Production / Handoff | production boundary, active handoff, implementation/QA evidence paths | `docs/HANDOFF_CONTEXT.md`, `docs/implementation/`, `docs/qa/`, `docs/CURRENT_IMPLEMENTATION_STATUS.md` | ALREADY_CURRENT_REPOSITORY_OWNER |

## 분류와 교정 finding

| 분류 | finding | 처리 |
|---|---|---|
| CURRENT | 제품 core, Run Command 4단계, 3×3 룰렛, 세 전선 동시 인지, 실제 consumer manifest와 evidence ceiling | repository current owner에 연결해 보존 |
| HISTORICAL | 예전 main SHA, PR 상태, old runtime capture, past asset queue와 Notion server readback | historical evidence로 남기며 current source로 사용 금지 |
| SUPERSEDED | `ANIME_PIXEL_ART + CLEAN_PIXEL_ART`, 전선별 독립 minimap, 긴 병렬 road 기본 구도, 하단 룰렛이 포함된 planning board | current 2026-08-28 storybook strategic-map owner로 대체 |
| CONFLICT | Notion addendum의 `방어탑 효과 미결정` / stage-1 tower-only 설명 / 이미지 생성 중단·명시 승인 요구 | user-approved forward-defense contract와 자동 생성 정책으로 교정; Notion 원문은 수정하지 않음 |
| CONFLICT | Notion 일부 current 문구의 `세 전선 = 병렬 lane` 또는 각각의 전선별 미니맵 | `ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT`, `PER_FRONT_MINIMAP = ABSORBED_INTO_PRIMARY_STRATEGIC_MAP`으로 교정 |
| UNKNOWN_UNVERIFIED | Notion에 보이는 old attachment의 현재 로컬 binary 존재, style fit, rights final review, target-resolution human readability | 현행 product asset으로 승격하지 않음; existing provenance/evidence owner에서만 추적 |

## 자산 보존 경계

- 현재 repository-local source/derivative와 consumer는 approved manifest와 `.asset-vault/`가 소유한다. Notion 목록을 별도 asset master로 복제하지 않는다.
- `OM-IMG-023`과 Notion inline preview는 historical/reference lineage다. 현재 visual direction이나 runtime asset으로 승격하지 않는다.
- 현재 `OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v5_FORWARD_DEFENSE_OCCUPATION_NODES.png`은 `GENERATED_EXPLORATION__USER_LOCK_PENDING`이며 planning visualization이다. runtime asset·Godot Scene·Human usability·Player Experience PASS가 아니다.
- user-provided reference와 Notion attachment는 rights/provenance review 전 release asset으로 간주하지 않는다.

## 완료 readback

```text
REPOSITORY_PROJECT_HOME = docs/PROJECT_HOME.md
NOTION_MIGRATION_REPORT = docs/migrations/OMENWARD_NOTION_CURRENT_CONTENT_TO_REPOSITORY_MIGRATION_2026-08-28.md
NOTION_MIGRATION_READ = COMPLETE__USER_APPROVED_READ_ONLY
NOTION_WRITE_OR_DELETE = NOT_PERFORMED
NOTION_AFTER_MIGRATION = HISTORICAL_REFERENCE_ONLY__NO_FUTURE_READ_OR_WRITE
```

## Migration validation incident / solution / lesson

```text
INCIDENT = LEGACY_PHASE_B_TEST_EXPECTED_NOTION_READBACK_AFTER_REPOSITORY_ONLY_RETIREMENT
SOLUTION = CURRENT_MAIN_POINTER_RECONCILIATION_REQUIRES_FRESH_GITHUB_AND_REPOSITORY_READBACK
LESSON = CURRENT_ROUTER_TESTS_MUST_FOLLOW_THE_ACTIVE_AUTHORITY_BOUNDARY_NOT_A_RETIRED_TOOL
NO_BASE_PROMOTION = PROJECT_SPECIFIC_NOTION_RETIREMENT_BOUNDARY
```

이 migration은 프로젝트별 문서 도구 전환이므로 Base 공용 규칙으로 승격하지 않는다.
