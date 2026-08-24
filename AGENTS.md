# OMENWARD 프로젝트 AI 작업 규칙

```yaml
updated_at: 2026-08-24
common_work_authority: alsdmlals4-eng/Base/AGENTS.md
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
contract_adapter: THIN_ADAPTER_DO_NOT_DUPLICATE_BASE_CANON
planning_status: NORTH_STAR_V2_1_AUDITED_CORRECTION_BRIEF_CURRENT
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
current_gdd: docs/OMENWARD_GDD_CURRENT_CANON.md
implementation_authorized: false
visual_generation: USER_REQUEST_ONLY
current_chat_runtime: NOT_RUN
```

공통 TDD·벤치마킹·PR·적대적 검토·정본 freshness는 매 작업 시작 시 fresh `alsdmlals4-eng/Base` current authority를 따른다. 이 문서는 OMENWARD의 **영구 routing과 보호 경계**만 소유하며, PR 번호·HEAD·Decision 개수처럼 자주 변하는 live 상태를 복제하지 않는다.

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

현재 승인 상태의 복원 owner는 `docs/CURRENT_CONFIRMED_DECISIONS.md`다.

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 19
NORTH_STAR_V2_1 = APPROVED_REFERENCE_WITH_BOUNDARY
CURRENT_NEXT = COMPONENT_BREAKDOWN_REUSE_IN_FINAL_PLANNING_REVIEW
CORRECTED_NORTH_STAR_IMAGE = USER_EXPLICIT_IMAGE_REQUEST_ONLY
VISUAL_GENERATION = USER_REQUEST_ONLY
IMPLEMENTATION_START = NOT_AUTHORIZED
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_HUMAN_PLAYER_EVIDENCE = NOT_RUN
```

현재 non-image 기획의 world/content/balance envelope/Text UX/Visual Component/Top-down Layout/Silhouette/North Star v2.1 audit 계약은 이미 승인 owner가 존재한다. 같은 질문을 다시 열지 않는다.

각 개별 Decision owner 안의 과거 `CURRENT_NEXT / THEN` 블록은 **그 Decision 승인 당시의 local sequence**로 읽고, 현재 프로젝트 routing은 `docs/CURRENT_CONFIRMED_DECISIONS.md`와 `docs/ACTIVE_CONTEXT.md`를 우선한다.

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

## 4. Current world / visual truth

```text
PLAYER_ROLE = Omen Warden / 징조수호관
ONE_MAPRUN = ONE_WARD_CITADEL + ONE_20_STAGE_OMEN_CYCLE
PRESSURE_LANGUAGE = MASS / ARMORED / FLYING / INFILTRATION / SIEGE
VEIL = 적 종족 하나가 아니라 현실과 겹쳐지는 적대적 경계 현상
RUN_HISTORY_RESET = FALSE
CHARACTER_AND_UNIT_STYLE = ANIME_PIXEL_ART
BATTLEFIELD_AND_BACKGROUND_STYLE = CLEAN_PIXEL_ART
DEFAULT_CAMERA = FULL_THREE_LANES_VISIBLE
NORMAL_COMBAT_UNIT_RULE = SILHOUETTE_FIRST
ROULETTE_EXPOSURE = 3×3
LOWER_CONTROL_DECK = FOCUS_ADAPTIVE_COMPACT
NORTH_STAR_V2_1 = APPROVED_REFERENCE_WITH_BOUNDARY
NORTH_STAR_BATTLEFIELD = APPROVED_DIRECTION
NORTH_STAR_ART_MOOD = APPROVED_DIRECTION
NORTH_STAR_LOWER_DECK = NEEDS_CORRECTION
NORTH_STAR_ROULETTE_INTERACTION = NEEDS_CORRECTION
NORTH_STAR_EXACT_TEXT_VALUES_MICROLAYOUT = NON_CANON_REFERENCE
```

Visual owner를 읽을 때 최소 다음을 함께 확인한다.
- visual style/component
- battlefield scale/readability
- 3×3 roulette component
- token component
- lower control deck
- roulette DDD
- top-down battlefield layout
- top-down unit silhouette
- `docs/design/APPROVED_OMENWARD_NORTH_STAR_V2_1_AUDIT_AND_CORRECTION_BRIEF_2026-08-24.md`

이미지 생성은 사용자가 명시적으로 요청한 경우에만 수행한다.

## 5. Runtime / evidence ceiling

현재 v4.8 재기획 의미에 대한 runtime/사람 검증은 실행하지 않았다.

```text
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_UI_EVIDENCE = NOT_RUN
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
LEGACY_C1_C2_C3_PROVEN
```

`LEGACY_C1_C2_C3_PROVEN`은 과거 exact evidence의 존재만 뜻한다. 정확한 head/run은 historical audit/archive owner에서 검증하고 Current 문서에 복제하지 않는다.

## 6. GitHub work-item boundary

```text
CURRENT_OPEN_PRS_AND_ISSUES = FRESH_GITHUB_QUERY_REQUIRED
PR175 = CLOSED_UNMERGED_HISTORICAL
PR177 = CLOSED_UNMERGED_REFERENCE_HISTORY
PR197 = CLOSED_UNMERGED_SUPERSEDED_BY_198
```

- open/draft PR은 Base 규칙대로 기본 read-only.
- closed-unmerged branch 내용을 current product truth로 사용하지 않는다.
- Issue176/과거 runtime package는 future implementation 때 fresh main + current Decisions + actual runtime과 재대조한다.

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
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
PLATFORM_SUBMISSION_NOT_RUN
LEGAL_REVIEW_NOT_PERFORMED
RELEASE_BLOCKED_UNVERIFIED
```

아트·오디오·폰트·외부 라이브러리·AI 산출물·외주물은 provenance/상업 이용/배포/원본 재배포/참조 독립성 기록을 확인한 뒤 제품 자산으로 승격한다.

## 9. Historical compatibility markers

```text
MAIN_CANONICAL_APPROVED_10_OF_10 = HISTORICAL_2026_08_11
PHASE_B_FINAL_PLANNING_REVIEW = HISTORICAL_PASS
PHASE_C_C0_OVERALL = HISTORICAL_PASS
LEGACY_C1_C2_C3_PROVEN
```

retained repository change 뒤에는 Base current `POST_CHANGE_MONITOR_LOOP`와 최소 5회 full-scope adversarial review를 수행한다. `NOT_RUN`을 PASS로 승격하지 않는다.
