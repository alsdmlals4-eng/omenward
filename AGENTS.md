# OMENWARD 프로젝트 AI 작업 규칙

```yaml
updated_at: 2026-08-25
common_work_authority: alsdmlals4-eng/Base/AGENTS.md
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
contract_adapter: THIN_ADAPTER_DO_NOT_DUPLICATE_BASE_CANON
planning_status: RESOLVE_FROM_CURRENT_DECISION_INDEX
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
current_gdd: docs/OMENWARD_GDD_CURRENT_CANON.md
implementation_authorized: RESOLVE_FROM_CURRENT_DECISION_INDEX_AND_ACTIVE_CONTEXT
visual_generation: USER_REQUEST_ONLY
```

공통 TDD·벤치마킹·PR·적대적 검토·정본 freshness는 매 작업 시작 시 fresh `alsdmlals4-eng/Base` current authority를 따른다. 이 문서는 OMENWARD의 **영구 routing과 보호 경계**만 소유하며, PR 번호·HEAD·Decision 개수·현재 작업 단계처럼 자주 변하는 live 상태를 복제하지 않는다.

## 1. 매 작업 시작 read order

1. fresh Base `START_HERE.md` / `AGENTS.md` / relevant Skill / main.
2. fresh OMENWARD `main`, open/draft PR, Issue, target files.
3. `docs/CURRENT_CONFIRMED_DECISIONS.md`.
4. `docs/ACTIVE_CONTEXT.md`.
5. `docs/OMENWARD_GDD_CURRENT_CANON.md` + `docs/PROJECT_CORE.md` + relevant owner.
6. Project Notion Home + relevant human-facing page.
7. 실제 code/data/scene/test/runtime evidence는 해당 scope가 열렸을 때만 current evidence로 판정한다.

과거 채팅·Handoff·오래된 SHA·closed-unmerged PR을 current product truth로 사용하지 않는다. GitHub work-item 상태는 매번 fresh 조회한다.

## 2. Current planning route

현재 승인 상태와 exact 작업 순서의 복원 owner는 `docs/CURRENT_CONFIRMED_DECISIONS.md`와 `docs/ACTIVE_CONTEXT.md`다.

```text
CURRENT_ROUTE = RESOLVE_FROM_CURRENT_DECISION_INDEX_AND_ACTIVE_CONTEXT
VISUAL_GENERATION = USER_REQUEST_ONLY
IMPLEMENTATION_START = RESOLVE_FROM_CURRENT_DECISION_INDEX_AND_ACTIVE_CONTEXT
RUNTIME_EVIDENCE = RESOLVE_FROM_ACTIVE_CONTEXT_AND_ACTUAL_EXECUTION
```

이미 승인 owner가 존재하는 질문을 다시 열지 않는다. 각 개별 Decision owner 안의 과거 `CURRENT_NEXT / THEN` 블록은 **그 Decision 승인 당시의 local sequence**로 읽고 current router로 사용하지 않는다. 특정 구현 패킷이 승인되었다면 그 패킷의 명시 범위만 구현 권한으로 읽고, 프로젝트 전체 구현 권한으로 확대하지 않는다.

## 3. Protected product identity

```text
ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE
GAMBLING_FANTASY_POSITIONING = FORBIDDEN
SCRIPTED_FAKE_NEAR_MISS = FORBIDDEN
RNG_CAN_REMOVE_ALL_VALID_RESPONSES = FORBIDDEN
FORECASTED_PRESSURE_MULTIPLE_RESPONSE_AXES_REQUIRED = TRUE
AUTO_PRODUCTION_AND_TOKEN_SOURCE = SEPARATE_ACQUISITION_PATHS
TOKEN_INSTANCES_PER_REEL_PER_ACTIVE_SOURCE = 1
TOTAL_TOKEN_INSTANCES_PER_ACTIVE_SOURCE = 3
THREE_REELS_TO_THREE_LANES_FIXED_MAPPING = FORBIDDEN
IRREVERSIBLE_LANE_COMMITMENT = REQUIRED
DANGER_STAGE_TYPE = REMOVED
BOSS_STAGES = 5 / 10 / 15 / 20
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
PRESCRIPTIVE_NEXT_BUILD_COMMAND = FORBIDDEN
RUN_COMMAND_SCREEN = PREPARE -> COMMIT -> BATTLE -> REVIEW
```

Player-facing core:

```text
징조 관측
→ 건설 / 동원 인장 / 미래 병력 분포 설계
→ 3×3 징조륜 결과 / 제한된 행·열 조작
→ 병력 획득
→ 세 전선 중 하나에 비가역 커밋
→ 자동전투 + 제한된 수동 전술
→ 인과 복기
```

## 4. Durable world / visual boundary

```text
PLAYER_ROLE = Omen Warden / 징조수호관
ONE_MAPRUN = ONE_WARD_CITADEL + ONE_20_STAGE_OMEN_CYCLE
PRESSURE_LANGUAGE = MASS / ARMORED / FLYING / INFILTRATION / SIEGE
VEIL = 적 종족 하나가 아니라 현실과 겹쳐지는 적대적 경계 현상
RUN_HISTORY_RESET = FALSE

VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
WORLD_TONE = FANTASY_WARD_CITADEL + MAGIC_WARFARE
COMMANDER_ROLE_ANCHOR = LONG_COMMAND_FLAG
BATTLEFIELD_PRESENTATION = THREE_SIMULTANEOUS_FRONT_STATE_VIEWS
PER_FRONT_MINIMAP = REQUIRED
MINIMAP_IS_CONTEXT_NOT_SECOND_BATTLEFIELD = TRUE
NORMAL_COMBAT_UNIT_RULE = SILHOUETTE_FIRST
ROULETTE_EXPOSURE = 3×3
LOWER_CONTROL_DECK = FOCUS_ADAPTIVE_COMPACT
```

2026-08-25 이전의 `ANIME_PIXEL_ART + CLEAN_PIXEL_ART`, 긴 3전선 도로 전체표시, 미니맵 비요구 표현은 current Decision `OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01`이 해당 범위에서 supersede한다. 세 전선 **동시 가독성** 자체와 전장-primary / 하단-secondary, 병종 역할 실루엣 원칙은 유지한다.

Visual 작업은 current Decision index에서 active visual owner를 복원한다. 현재 battlefield/visual owner는 `docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md`다. 이미지 생성은 사용자가 명시적으로 요청한 경우에만 수행한다.

## 5. Runtime / evidence ceiling

현재 runtime·UI·human/player evidence 상태는 `docs/ACTIVE_CONTEXT.md`와 actual execution evidence에서 읽는다.

- 과거 exact evidence가 존재해도 current replan/runtime PASS로 자동 승격하지 않는다.
- file/Scene/resource 존재만으로 runtime 동작을 주장하지 않는다.
- runtime/human 검증을 실행하지 않았으면 `NOT_RUN / UNVERIFIED`를 유지한다.
- 최종 제품 수치는 simulation/runtime/human evidence 없이 확정하지 않는다.
- 전선별 미니맵 가독성과 SD 병종의 실제 전투 가독성은 runtime/human 검증 전 `NOT_RUN`이다.

## 6. GitHub work-item boundary

```text
CURRENT_OPEN_PRS_AND_ISSUES = FRESH_GITHUB_QUERY_REQUIRED
```

- open/draft PR은 Base 규칙대로 기본 read-only.
- closed-unmerged branch 내용을 current product truth로 사용하지 않는다.
- 과거 runtime execution Issue/PR은 future implementation 때 fresh main + current Decisions + actual runtime과 재대조한다.

## 7. Notion / repository authority

- Notion: 사람이 보는 전체 그림, Flow, 비교표, Visual/Story/Work Plan.
- Repository: Markdown/JSON/code/data/scene/resource/test/runtime evidence와 구조화 계약.
- 의미 변경 Decision은 양쪽에 같은 의미로 동기화하고 destination readback한다.
- Google Sheet는 migration/history compatibility input이며 current human authority가 아니다.

## 8. Platform / release / asset-rights durable routing

플랫폼·출시·자산 권리는 current visual/planning next gate와 별개의 durable product boundary다. 제출·등급·권리 PASS를 추정하지 않는다.

- `docs/APPROVED_PC_ANDROID_PLATFORM_RELEASE_AUTHORITY_2026-08-05.md`
- `docs/PLATFORM_RELEASE_AND_ASSET_RIGHTS_PROFILE.md`
- `docs/ASSET_RIGHTS_AND_PROVENANCE_RECORD.md`
- `docs/GAME_RELEASE_COMPLIANCE_EVIDENCE_PACK.md`

```text
PC / Steam = COMMITTED_PRIMARY
Android / Google Play = COMMITTED_RELEASE_TARGET_DEFERRED_RELEASE_NEAR
STOVE = SECONDARY_RELEASE_CANDIDATE
```

actual release/submission/compliance 상태는 위 owner와 current evidence에서 읽는다. 아트·오디오·폰트·외부 라이브러리·AI 산출물·외주물은 provenance/상업 이용/배포/원본 재배포/참조 독립성 기록을 확인한 뒤 제품 자산으로 승격한다.

## 9. Historical compatibility markers

과거 approval/runtime marker는 historical owner에 보존하고 이 영구 adapter에 live 상태로 복제하지 않는다.

retained repository change 뒤에는 Base current `POST_CHANGE_MONITOR_LOOP`와 최소 5회 full-scope adversarial review를 수행한다. `NOT_RUN`을 PASS로 승격하지 않는다.