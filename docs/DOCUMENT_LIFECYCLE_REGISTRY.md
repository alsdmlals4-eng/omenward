# [현행] OMENWARD 문서 수명주기 레지스트리

```yaml
updated_at: 2026-08-05
policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
status: CURRENT_LIFECYCLE_AUTHORITY
current_decision: OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
current_count: 3_OF_10
```

이 레지스트리는 파일명·과거 YAML보다 우선한다. `[대체됨]`, `[보류]`, `[폐기]` 문서는 신규 기획·Codex 구현·아트 제작 입력으로 사용하지 않는다.

## 1. [현행]

### 최상위·운영

| 주제 | 파일 |
|---|---|
| 프로젝트 코어 | `docs/PROJECT_CORE.md` |
| 현행 GDD | `docs/OMENWARD_GDD_CURRENT_CANON.md` |
| 현재 상태 | `docs/ACTIVE_CONTEXT.md` |
| 구현 경계 | `docs/CURRENT_IMPLEMENTATION_STATUS.md` |
| 문서 지도 | `docs/DOCUMENTATION_MAP.md` |
| 동적 main·수명주기 정책 | `docs/process/APPROVED_DYNAMIC_CURRENT_MAIN_AND_DOCUMENT_LIFECYCLE_POLICY_2026-08-04.md` |
| 벤치마킹·TDD·승인 배치 정책 | `docs/process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md` |
| GPT·Codex 역할 경계 | `docs/process/APPROVED_PLANNING_VISUALS_AND_CODEX_IMPLEMENTATION_BOUNDARY_2026-08-04.md` |

### 현재 Planning Batch

| 주제 | 파일 |
|---|---|
| 핵심 재미·콘텐츠 가드레일 1/10 | `docs/design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md` |
| Stage·Wave·Danger·Boss 압력 2/10 | `docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md` |
| 건물 6종 T2/T3 분기·카운터 3/10 | `docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md` |
| 건물 분기 설계 Spec | `docs/superpowers/specs/2026-08-05-six-building-t2-t3-branches-design.md` |
| 건물 분기 작업 계획 | `docs/superpowers/plans/2026-08-05-six-building-t2-t3-branches-implementation.md` |
| 핵심 재미 적대적 검토 | `docs/reviews/ADVERSARIAL_CORE_FUN_CANON_AND_LEGACY_CONFLICT_REVIEW_2026-08-04.md` |
| Stage 적대적 검토 | `docs/reviews/ADVERSARIAL_STAGE_PRESSURE_REPLAYABILITY_AND_FAIRNESS_REVIEW_2026-08-04.md` |
| 건물 분기 적대적 검토 | `docs/reviews/ADVERSARIAL_BUILDING_BRANCH_COUNTER_AND_OPPORTUNITY_COST_REVIEW_2026-08-05.md` |

### 현행 시스템

| 주제 | 파일 | 승계 경계 |
|---|---|---|
| 전체 시스템 연결 | `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | 시스템 연결 계보만 부분 승계 |
| MapRun·Stage·Wave | `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md` | 최신 20 Stage 압력 정본 우선 |
| Stage 정비시간·상인 | `docs/design/APPROVED_OMENWARD_MAPRUN_STAGE_WAVE_MAINTENANCE_2026-08-02.md` | 흐름·용어 승계 |
| 전투 공간·Route | `docs/design/APPROVED_OMENWARD_COMBAT_SPACE_ROUTE_AND_TARGETING_EXPERIENCE_2026-08-04.md` | 플레이어 의미 승계 |
| 전장 시각 계층 | `docs/design/APPROVED_OMENWARD_BATTLEFIELD_VISUAL_HIERARCHY_AND_CAMERA_2026-08-04.md` | 현행 |
| HUD·룰렛·자원·기본 건물 역할 | `docs/design/APPROVED_OMENWARD_COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_AND_BUILDING_ROSTER_2026-08-04.md` | 기본 역할은 현행, 세부 분기는 2026-08-05 건물 정본이 확장 |
| HUD 레이아웃·자산 재사용 | `docs/design/APPROVED_OMENWARD_HUD_ROULETTE_LAYOUT_AND_BATTLEFIELD_VIEW_AMENDMENT_2026-08-04.md` | 현행 |
| 최종 아트 방향 | `docs/design/APPROVED_OMENWARD_PIXEL_ILLUSTRATION_HYBRID_ART_DIRECTION_2026-08-04.md` | 현행 |
| 세계관·명칭 | `docs/design/APPROVED_OMENWARD_WORLD_AND_NAMING.md` | 현행 |
| 벨루 정체성 | `docs/design/APPROVED_BELLU_MASCOT_AND_GUIDE_CONTRACT.md` | 현행 |

전투 결정 문서의 플레이어 의미·공정성은 현행이다. 좌표·Tick·정렬 키·Resolver 구조 같은 구현 방식은 Codex 참고안이며 강제 구현 권위가 아니다.

## 2. [대체됨]

| 파일 | 승계 문서·이유 |
|---|---|
| `docs/OMENWARD_GAME_DESIGN.md` | `docs/OMENWARD_GDD_CURRENT_CANON.md`; 식량·건물 5종·주변 지휘소 포함 |
| `docs/design/APPROVED_DOPAMINE_DRIVEN_DESIGN_AND_FIRST_10_MINUTES.md` | 핵심 원칙은 core-fun 정본으로 승계, 구형 흐름·수치는 분리 |
| `docs/design/APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md` | 20 Stage·3 Wave Beat 압력 매트릭스로 대체 |
| `docs/process/POST_MERGE_PIXEL_ILLUSTRATION_HYBRID_CANON_SYNC_2026-08-04.md` | 과거 병합 증거만 보존 |
| `docs/operations/PR121_POST_MERGE_SYNC_2026-08-02.md` | 과거 PR 증거만 보존 |
| `docs/design/proposals/0011-korean-natural-fantasy-names-law-and-mascot.md` | 세계관·명칭·벨루 정본에 반영 완료 |
| `docs/archive/2026-07/pre-v2-canon/DOCUMENTATION_MAP_PRE_V2.md` | archive 역사 자료 |

## 3. [보류]

### 첫 10~15분·튜토리얼

- `docs/design/APPROVED_BELLU_SINGLE_GUIDE_AND_FIRST_10_MINUTE_FLOW.md`
- `docs/design/APPROVED_TUTORIAL_FIRST_FOUR_WAVES_BALANCE_V1.md`

식량·바리케이드·병영 자동생산·구형 HUD 공개 순서를 포함한다. 7/10에서 최신 Stage 1~5와 건물 전문화에 맞춰 재설계하기 전 사용 금지.

### 메타·허브

- `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md`

재화·시설·Retry 구조가 최신 Run 경제와 재검증되지 않았다.

### Hero·Legendary

`docs/design/APPROVED_OMENWARD_HERO_*`, `docs/design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md`, `docs/design/APPROVED_OMENWARD_REPEAT_LEGENDARY_RESULT_HIGH_GRADE_SLOT_RESOLUTION_2026-08-02.md` 파일군은 과거 승인 근거다. 최신 Stage 압력·건물·병종·전술·HUD와 재조정 전 구현 권위가 없다.

### 구형 구현 계획

- `docs/superpowers/plans/2026-07-24-omenward-core-v2-implementation.md`
- `docs/superpowers/plans/2026-08-02-omenward-grillme-bundle-merge-plan.md`
- 완료·병합된 과거 Issue/Goal 계획

재실행하지 않고 Git 이력·결정 근거로만 사용한다.

## 4. [폐기]

| 파일·가정 | 이유 |
|---|---|
| `docs/design/proposals/0009-world-naming-directions.md` | 미채택 명명안 |
| `docs/design/proposals/0010-english-world-names-and-game-title.md` | 미채택 영문 음차안 |
| 식량을 현행 핵심 HUD 자원으로 사용 | 골드·마석·배치 병력/한도로 대체 |
| 기본 건물 5종 | 현재 6종으로 대체 |
| 지휘소 주변 범위 오라 | 현재 MapRun 전역 군단 오라로 대체 |
| `15웨이브=1스테이지`·고정 60초 | 20 Stage·3 Wave Beat로 대체 |
| Danger에서 핵심 UI·정보 차단 | 공개된 한 규칙 변형으로 대체 |
| Stage 중 숨은 필수 카운터 변경 | Stage 시작 전 공개로 대체 |
| 룰렛 전용 금화·병종 상징 아이콘 | 인게임 자산 재사용으로 폐기 |
| T3 병종 룰렛 토큰 | 금지 |
| 동일 건물 인스턴스의 교차 분기 | `CROSS_BRANCH: FORBIDDEN` |
| 동일 건물 인스턴스의 양쪽 T3 | `DUAL_T3: FORBIDDEN` |
| 건물 분기만으로 다섯 압력 전부 해결 | 병종·전술 의존성을 제거하므로 폐기 |

## 5. [증거]

- `docs/reviews/**`의 과거 PR·적대적 검토 기록.
- `docs/benchmarks/**`의 실험·Evidence Pilot.
- `docs/archive/**`.
- 완료된 PR·commit·CI run·Sheet 변경 이력.

`[증거]`는 사실을 증명하지만 현재 기획 규칙을 자동 변경하지 않는다.

## 6. 신규 작업자 규칙

1. `PROJECT_CORE.md`와 `DOCUMENTATION_MAP.md`를 먼저 읽는다.
2. 이 레지스트리에서 대상 파일이 `[현행]`인지 확인한다.
3. `[대체됨]`, `[보류]`, `[폐기]`를 구현 입력으로 사용하지 않는다.
4. 건물 작업은 기본 역할 문서와 2026-08-05 분기 정본을 함께 읽되 분기 충돌 시 최신 건물 정본을 우선한다.
5. 병종·전술 작업은 건물 압력 의존성을 채우되 건물 정본을 만능 카운터로 확대하지 않는다.
6. 필요한 과거 아이디어는 새 Decision에서 재검토·재승인한 뒤 승계한다.
