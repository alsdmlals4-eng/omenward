# OMENWARD 프로젝트 AI 작업 규칙

```yaml
updated_at: 2026-08-20
common_work_authority: alsdmlals4-eng/Base/AGENTS.md
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
contract_adapter: THIN_ADAPTER_DO_NOT_DUPLICATE_BASE_CANON
planning_status: REOPENED_REVIEW_IN_PROGRESS
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
current_gdd: docs/OMENWARD_GDD_CURRENT_CANON.md
implementation_authorized: false
visual_generation: PAUSED_PENDING_USER_REFERENCE_FILES
current_chat_runtime: NOT_RUN
```

공통 TDD·벤치마킹·PR·적대적 검토·정본 freshness는 매 작업 시작 시 fresh `alsdmlals4-eng/Base` current authority를 따른다. 이 문서는 OMENWARD의 current routing과 보호 경계만 소유한다.

## 1. 매 작업 시작 read order

1. fresh Base `START_HERE.md` / `AGENTS.md` / relevant Skill / main.
2. fresh OMENWARD `main`, open/draft PR, target files.
3. `docs/CURRENT_CONFIRMED_DECISIONS.md`.
4. `docs/ACTIVE_CONTEXT.md`.
5. `docs/OMENWARD_GDD_CURRENT_CANON.md` + relevant detailed owner.
6. Project Notion Home + relevant human-facing page.
7. runtime/code/data/scene/test는 실제 구현/검증 scope가 열렸을 때만 current evidence로 판정한다.

과거 채팅·Handoff·오래된 SHA·closed-unmerged PR을 current product truth로 사용하지 않는다.

## 2. Current planning truth

2026-08-20 사용자가 프로젝트 기획을 다시 열었다. 현재 승인된 재기획 Decision 6개는 `docs/CURRENT_CONFIRMED_DECISIONS.md`가 복원 인덱스를 소유한다.

```text
OMW-PLAN-20260820-WORLD-ROLE-01
OMW-PLAN-20260820-MAPRUN-WORLD-01
OMW-PLAN-20260820-PRESSURE-LANGUAGE-01
OMW-PLAN-20260820-MOBILIZATION-REGISTRY-01
OMW-PLAN-20260820-FIRST5-FTUE-01
OMW-PLAN-20260820-RUN-COMMAND-SHELL-01
```

현재 이미지 workstream은 사용자가 보유한 시안/레퍼런스 파일을 받을 때까지 보류한다. 이미지 보류는 다른 기획 작업을 막지 않는다.

현재 비이미지 기획 순서:

```text
ADVERSARIAL_REVIEW_AND_CANON_RECONCILIATION
→ WORLD_CONFLICT_AND_CORE_STORY
→ 20_STAGE_CONTENT_AND_BOSS_STRUCTURE
→ BALANCE_BUDGET
→ TEXT_UX_AND_STATE_TRANSITION_SPEC
```

## 3. Protected product identity

```text
ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE
GAMBLING_FANTASY_POSITIONING = FORBIDDEN
PAID_SPIN = FORBIDDEN
RNG_CAN_REMOVE_ALL_VALID_RESPONSES = FORBIDDEN
FORECASTED_PRESSURE_MULTIPLE_RESPONSE_AXES_REQUIRED = TRUE
AUTO_PRODUCTION_AND_TOKEN_SOURCE = SEPARATE_ACQUISITION_PATHS
TOKEN_INSTANCES_PER_REEL_PER_ACTIVE_SOURCE = 1
TOTAL_TOKEN_INSTANCES_PER_ACTIVE_SOURCE = 3
THREE_REELS_TO_THREE_LANES_FIXED_MAPPING = FORBIDDEN
IRREVERSIBLE_LANE_COMMITMENT = REQUIRED
BOSS_STAGES = 5 / 10 / 15 / 20
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
PRESCRIPTIVE_NEXT_BUILD_COMMAND = FORBIDDEN
```

Player-facing core:

```text
징조 관측
→ 건설 / 동원 인장 / 미래 병력 분포 설계
→ 세 징조륜에서 병력 획득
→ 세 전선 중 하나에 비가역 커밋
→ 자동전투 + 제한된 수동 전술
→ 인과 복기
```

## 4. World / MapRun current truth

```text
PLAYER_ROLE = Omen Warden / 징조수호관
WORLD_HAS_MULTIPLE_WARD_CITADELS = TRUE
ONE_MAPRUN = ONE_WARD_CITADEL + ONE_20_STAGE_OMEN_CYCLE
PRESSURE_LANGUAGE = MASS / ARMORED / FLYING / INFILTRATION / SIEGE
PRESSURE_IS_ENEMY_RACE_OR_FACTION = FALSE
MULTI_SIGNATURE_ENEMY_OR_WAVE = ALLOWED
```

세계 갈등의 원인, 적 세력의 상위 정체, Stage 20의 서사적 결산은 아직 새 재기획에서 확정되지 않았으며 다음 주요 Decision 대상이다.

## 5. First-session / UI current truth

```text
FIRST_SESSION = REAL_MAPRUN
STAGE_1_REQUIRED_T1 = VAULT / FARM / GENERAL_BARRACKS / DEFENSE_TOWER / COMMAND_POST / MANA_TOWER
SPECIAL_BARRACKS_STAGE1_REQUIRED = FALSE
FIRST_ROULETTE_UNLOCK = AFTER_ALL_SIX_T1_AND_SETUP_CONFIRMATION
STAGE_1 = CAUSAL_UNDERSTANDING
STAGE_2 = FUTURE_DISTRIBUTION_MODIFICATION
STAGE_3 = TACTICAL_INTERVENTION
STAGE_4 = APPLICATION_WITH_NO_NEW_CORE_SYSTEM
STAGE_5 = FIRST_BOSS_AND_BUILD_REVIEW
RUN_COMMAND_SCREEN = PREPARE -> COMMIT -> BATTLE -> REVIEW
```

Stage 1의 6개 필수 T1은 현재 유지하되 `생존 기반 / 군사 기반 / 지휘 기반` 세 묶음으로 순차 노출한다. 사람 플레이에서 과부하가 실제 관측되면 축소안을 재검토한다.

## 6. Current GitHub work-item boundary

Fresh current truth를 매번 다시 읽는다. 2026-08-20 기준 routing:

```text
PR175 = CLOSED_UNMERGED_HISTORICAL
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
ISSUE176 = OPEN_HISTORICAL_FOLLOWUP_REQUIRES_RECONCILIATION
PR197 = OPEN_DRAFT_OTHER_WORKSTREAM_READ_ONLY
```

- PR175/177의 unmerged 변경을 current main product truth로 사용하지 않는다.
- Issue176을 미래 구현 packet으로 쓰기 전 current main + current planning Decisions와 재대조한다.
- PR197은 현재 채팅에서 수정·retarget·merge 금지.
- 사용자가 진행 중 PR을 별도 workstream으로 선언한 경우 현재 작업에서 건드리지 않는다.

## 7. Runtime / evidence ceiling

2026-08-20 재기획 채팅은 current Godot runtime을 실행하지 않았다.

```text
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_UI_EVIDENCE = NOT_RUN
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

2026-08-11~12 signal11 / HiGodot / GUT / Hera 기록은 historical evidence다. 현재 crash가 재현된다고 주장하지 않는다.

실제 구현/런타임 작업이 다시 열리면 fresh current-main 실행과 current tool/session identity로 새 truth를 만든다.

## 8. Notion / GitHub authority

- Notion: 사람용 전체 그림, Flow, 비교표, Visual/Story/Work Plan.
- GitHub: Markdown/JSON/code/data/scene/resource/test/runtime evidence와 구조화 계약.
- 의미 변경 Decision은 두 surface가 같은 Decision ID와 의미를 갖도록 동기화한다.
- Google Sheets는 current human authority가 아니며 migration/history 용도로만 취급한다.

## 9. Historical compatibility markers

아래는 과거 validator/문서 lineage를 위한 `ALLOWED_LEGACY` 문자열이다. current routing으로 해석하지 않는다.

```text
MAIN_CANONICAL_APPROVED_10_OF_10 = HISTORICAL_2026_08_11
PHASE_B_FINAL_PLANNING_REVIEW = HISTORICAL_PASS
PHASE_C_C0_OVERALL = HISTORICAL_PASS
PR175 = OPEN_DRAFT = HISTORICAL_LABEL_ONLY
PR175_CURRENT_MAIN_REVALIDATION_NEXT = HISTORICAL_LABEL_ONLY
PR177 = REFERENCE_ONLY_DO_NOT_MERGE = HISTORICAL_LABEL_ONLY
```

retained repository change 뒤에는 Base current `POST_CHANGE_MONITOR_LOOP`를 수행하고, 최소 5회의 full-scope adversarial review가 요구되는 범위에서는 `CLEAN_REVIEW_EXIT` 조건을 만족하기 전 완료 선언하지 않는다.
