# [현행] OMENWARD Roadmap

2026-09-12 방패병 베기 4자세 후보 runtime 연결 완료: 원화 성분 분리→공통 발 피벗→native/PNG 정합성→준비 후 단일 타격→저장 회귀→실제 GPU 3상태 캡처. 이 단계는 ASSET_READY/IMPLEMENTED/MACHINE_VERIFIED 및 해당 검토판 RUNTIME_VERIFIED이며 USER_APPROVED 아트·전체 모션은 아니다. 다음은 실제 크기에서 4자세 동작 품질 검토, 방패병 이동·피격·사망 및 베일/다른 병종 모션 확장이다. 베일 사제 종이색 잔여도 PARTIAL로 유지. 범위 밖 T3/영웅/등급/5맵 및 부모 PR·main 통합은 별도다.

2026-09-12 경계 후속: 베일 alpha 경계/발밑 제한 보정과 회귀 검증 진행. 완전한 종이 배경 제거가 아니며 품질 PARTIAL. 방패병 전체 4자세 시트는 새 출력도 RGB 체크무늬로 실패했으므로 다음 제작 단위를 개별 자세로 축소한다. 한 자세의 추출·외형·피벗을 먼저 통과시킨 뒤 나머지 자세, Aseprite 시간/태그, 실제 타격 시점으로 진행한다. 새 모션 runtime 연결은 아직 없다.

2026-09-12: 베일 10종 정적 투명 후보 연결과 Aseprite 왕복 검사를 진행했다. 우선 잔여 종이색 가장자리/밝은 외피 품질을 검토하고, 다음은 셀 침범 없는 베기·이동·피격 상태군과 피벗/시간/타격 동기화다. 정적 투명화를 모션 완료로 취급하지 않는다. 임시/불필요 파일 정리는 직접 삭제 대신 사용자 삭제 검토 폴더로 이동한다. 현재 사용 자산, 부모 기획 PR, 미확인 과거 원본은 유지한다.

2026-09-11 후속: 한정 BUILD 승인 검사와 CI 범위 분리, 탭/정지/배속/한국어 UI 상태, 방패병 대기 RGBA 연결을 진행했다. 다음은 **셀 간 침범 없는 실제 RGBA 베기 상태군 → Aseprite 피벗/시간 데이터 → 타격 시점 연동 → 베일 및 나머지 병종**이다. 최초 투명 후보의 베기 검이 이웃 셀로 넘어가므로 현재 연결은 대기 1셀뿐이다. 픽셀 이동을 베기 모션 완료로 취급하지 않는다. 원격 main 및 부모 기획 PR 통합은 별도다.

2026-09-11 현재: 인게임 전투·병영 건설·이미지 연결의 제한된 실행 검토판을 구현 중/검증한다. 실행 owner는 `docs/superpowers/plans/2026-09-11-visible-battle-slice.md`. 다음 필수 작업은 (1) 정적 카드 대신 투명 병종 스프라이트와 베기 상태군, (2) 겹침/공간 점유·전투 가독성, (3) 징조륜 행/열 조작과 보너스, (4) 남은 병종 능력/T3·등급·영웅, (5) 전체 맵/밸런스 및 오래된 CI 계약 정합성이다. 본문 과거 ‘최종 승인 전 runtime 금지’는 최신 단일 전선 BUILD 승인 범위에서 superseded. 검토판 작동과 제품 완성은 구분한다.

v3 현재: 일반/특수 분리·10병종·T3 심화 교정과 기획 데이터 자동검사 완료. 누락 2병종 도감 후보 추가. 다음은 특수병영 등 누락 건물 원화, 실제 투명 전투 상태군, 경제/전투 검증 및 정본 CI 드리프트 교정, 최종 승인이다. 문서 검사 PASS는 인게임 구현 준비 전체 PASS가 아니다.

61쪽 v2 보완: 병종 pair 도감/등급 스킬/건물 특화/영웅 후보까지 추가. 다음은 특화 비용·기본 방패 편성 생존 fixture, 그림 경계·영웅 SD·군수소 및 모션 상태군 보완, PDF 전체 검수와 보호된 원격 동기화다. 사용자 최종 승인 전 runtime 변경 금지.

2026-09-11 우선 순서: 통합 Blueprint 검토 PDF → 부족한 alpha/병종 상태군/5맵/탑·분리 소품 제작 및 검수 → 명세·경제 fixture 교차 검증 → 최종 사용자 승인 → 승인 패킷 구현. 이미지 보류는 해제되었다. 현재 PDF는 39쪽 REVIEW_EDITION이며 전체 납품 자산 완료로 표시하지 않는다. 상세 owner: `docs/design/OMENWARD_HUMAN_BLUEPRINT_REVIEW_20260911.md`.

최우선 순서 변경: 맵/라운드/웨이브 상세 기획 검토 → 경제·점령·병력 계승/실패 사례 검토 → 화면 흐름 정합성 → 구현 패킷 판단. 이미지와 모션은 보류하며 아래 이전 아트 순서는 현재 실행 지시가 아니다. 진행 설계 owner는 Blueprint §1의 현행 상세 진행 설계다. 이번에는 권장안만 명세하고 제품 코드는 변경하지 않는다.

2026-09-10 우선 순서: 핵심 유지·연구 비교 → 화면/흐름 Blueprint → 방패병 V3·비인간 베일 pair → 내려베기 V2 5키포즈/Aseprite·브라우저 재생 검사 → 장비 continuity·투명 경계 교정 → Godot 검증 → 콘텐츠 확장. 회복 포즈를 추가했지만 아트 일관성은 PARTIAL이다. 현재 상세 owner는 `docs/design/OMENWARD_COMMAND_FLOW_AND_MOTION_BLUEPRINT_2026-09-10.md` §8이다.

> **2026-09-10 재기획 우선 적용:** 사용자는 기획부터 다시 시작하고 기존 이미지는 참고자료로만 사용하며 새 이미지와 모션을 함께 제작하도록 지시했다. 현재 접수·근거·작업 순서는 `docs/design/OMENWARD_REPLAN_AND_MOTION_INTAKE_2026-09-10.md`가 소유한다. 아래의 이전 제품 기획·시각 승인·phase·완료 상태는 새 기획의 실행 권한이 아닌 기존 빌드의 역사/비교 자료다. 보안·저장 보호·권리·Git 보호 경계는 유지한다. 읽기 순서는 프로젝트 최신 AGENTS → 최신 main → Decisions/Active Context → 실제 consumer와 열린 PR 중첩 → 적용 Base 지침이다. Base version lock은 변경하지 않는다.

```yaml
updated_at: 2026-08-29
status: FIRST5_FTUE_CORE_LOOP_RECONCILIATION__OPEN_BATTLEFIELD_V6_VISUAL_DIRECTION_LOCKED
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_next_gate: PHASE2_OPEN_BATTLEFIELD_READINESS_REVIEW__ISSUE_RED_TEST_PROVENANCE_TARGET_RESOLUTION_REQUIRED
repository_only_policy: docs/process/APPROVED_OMENWARD_REPOSITORY_ONLY_CANON_AND_NOTION_RETIREMENT_2026-08-28.md
visual_generation: USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
implementation_authorized: true
implementation_execution: IMPLEMENTED__HEADLESS_CONTRACTS_AND_THREE_RESOLUTION_TECHNICAL_QA_CAPTURED__HUMAN_NOT_RUN
```

## 1. Product north star

> 건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.

```text
징조 관측
→ 확률 설계
→ 3×3 징조륜 / 제한 조작
→ 병력 획득
→ PREPARE -> COMMIT -> BATTLE -> REVIEW
→ 비가역 전선 커밋
→ 자동전투 / 전술
→ 인과 Review
```

## 2. Current closure state

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 27
FORWARD_DEFENSE_OCCUPATION_NODES = CONFIRMED__PLANNING_ONLY__NOT_IMPLEMENTED
OPEN_BATTLEFIELD_TOWER_ONLY_LAYOUT = CONFIRMED__PLANNING_ONLY__NOT_IMPLEMENTED
FORWARD_BASE_DEFENSE_STACK = AUTO_ATTACK_TOWER_ONLY
FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL
OCCUPATION_NODE_ACTIVATION = STABLE_PLAYER_OWNED_OUTPOST_ONLY
CURRENT_FORWARD_DEFENSE_SPEC = docs/design/APPROVED_OMENWARD_FORWARD_DEFENSE_AND_OCCUPATION_NODE_CONTRACT_2026-08-28.md
CURRENT_BASE_FORWARD_LAYOUT_SPEC = docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_TOWER_ONLY_FORWARD_LAYOUT_2026-08-28.md
CURRENT_VISUAL_DECISION = OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01
CURRENT_TARGET_RUNTIME_ASSET = NOT_CREATED
LEGACY_RUNTIME_BACKDROP = OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1
PROJECT_CORE_SCENE_VISUAL_BOARD = USER_CONFIRMED_PLANNING_LOCK__V6_OPEN_BATTLEFIELD_NO_BARRICADE__NOT_RUNTIME_ASSET
CURRENT_BUILD_RUNTIME_UNIT_ASSET_SET = LEGACY_STYLE_FIT_REVIEW_REQUIRED
UNIT_ANIMATION_PRODUCTION_CONTRACT = RETAINED_GEOMETRY_ONLY__STYLE_FIT_REVIEW_REQUIRED
TOPDOWN_BATTLEFIELD_LAYOUT = RETAINED_WITH_LAYOUT_OVERRIDE
TOPDOWN_UNIT_SILHOUETTE = CONFIRMED
NORTH_STAR_V2_1 = HISTORICAL_REFERENCE_ONLY
BATTLEFIELD_PRESENTATION = ONE_SIMULTANEOUS_THREE_FRONT_STRATEGIC_MAP
MAP_TOPOLOGY = ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT
PER_FRONT_MINIMAP = ABSORBED_INTO_PRIMARY_STRATEGIC_MAP
VISUAL_STYLE = STORYBOOK_WATERCOLOR_SD_TACTICAL_ILLUSTRATION
IMPLEMENTATION_AUTHORITY = SCOPED_APPROVED_RETAINED
PROJECT_ACTIVITY = FIRST5_FTUE_CORE_LOOP_RECONCILIATION__VISUAL_EXECUTION_PAUSED
CURRENT_NEXT = PHASE2_OPEN_BATTLEFIELD_READINESS_REVIEW__ISSUE_RED_TEST_PROVENANCE_TARGET_RESOLUTION_REQUIRED
IMAGE_GENERATION = USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5
GITHUB_NOTION_DRIFT_CHECK = PASS
```

The 2026-08-24 planning review remains retained evidence. Its then-current route is history, not the current gate:

```text
HISTORICAL_20260824_CURRENT_APPROVED_REPLAN_DECISIONS = 19
HISTORICAL_20260824_NORTH_STAR_V2_1 = APPROVED_REFERENCE_WITH_BOUNDARY
HISTORICAL_20260824_CURRENT_NEXT = IMPLEMENTATION_AUTHORITY_REQUIRED
HISTORICAL_20260824_CURRENT_IMPLEMENTATION_AUTHORITY = NONE
```

Final planning review owner:
- `docs/reviews/FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK_2026-08-24.md`

Current visual owners:
- `docs/superpowers/specs/2026-08-28-storybook-sd-three-front-strategic-map-design.md`
- `docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_TOWER_ONLY_FORWARD_LAYOUT_2026-08-28.md`
- `docs/images/planning/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28.md` — generated planning exploration only.
- `docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md`
- `docs/images/planning/canonical/OMENWARD_APPROVED_FRONT_STATE_VISUAL_2026-08-25.md`
- `docs/images/planning/OMENWARD_UNIT_ANIMATION_PRODUCTION_CONTRACT_2026-08-26.md`
- `docs/handoffs/2026-08-29-open-battlefield-v6-visual-lock-handoff.md`

Historical visual audit owner:
- `docs/design/APPROVED_OMENWARD_NORTH_STAR_V2_1_AUDIT_AND_CORRECTION_BRIEF_2026-08-24.md`

## 3. Current visual route

```text
BATTLEFIELD_PRESENTATION = ONE_SIMULTANEOUS_THREE_FRONT_STRATEGIC_MAP
MAP_TOPOLOGY = ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT
PER_FRONT_MINIMAP = ABSORBED_INTO_PRIMARY_STRATEGIC_MAP
MINIMAP_IS_CONTEXT_NOT_SECOND_BATTLEFIELD = TRUE
VISUAL_STYLE = STORYBOOK_WATERCOLOR_SD_TACTICAL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
COMMANDER_SILHOUETTE = LONG_COMMAND_FLAG
TOPDOWN_BATTLEFIELD_LAYOUT = RETAINED_WITH_LAYOUT_OVERRIDE
TOPDOWN_UNIT_SILHOUETTE = CONFIRMED
NORTH_STAR_V2_1 = HISTORICAL_REFERENCE_ONLY
```

## 4. Evidence boundary

```text
LEGACY_C1_C2_C3_PROVEN
CURRENT_GODOT_RUNTIME = PARTIAL__RUN_COMMAND_UI_TECHNICAL_SMOKE_AND_THREE_RESOLUTION_CAPTURED
CURRENT_WINDOWS_RUNTIME = PARTIAL__STANDALONE_TECHNICAL_CAPTURED_960_1280_1920
CURRENT_MINIMAP_READABILITY = PARTIAL__THREE_RESOLUTION_TECHNICAL_CAPTURED__HUMAN_NOT_RUN
CURRENT_SD_UNIT_RUNTIME_READABILITY = PARTIAL__ALL18_UNIT_GALLERY_NO_CLIPPING_SIGNAL
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
```

CI regression execution does not promote the approved visual into human/minimap/player evidence.

## 5. Economy reconciliation

```text
ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

구현 재개 시 fresh main/runtime 기준으로 economy baseline을 다시 대조한다.

## 6. Retained implementation packet

```text
IMPLEMENTATION_AUTHORITY = SCOPED_APPROVED_RETAINED
IMPLEMENTATION_SCOPE = RUN_COMMAND_ORCHESTRATION_FIRST_VERTICAL_SLICE_ONLY
IMPLEMENTATION_EXECUTION = IMPLEMENTED__HEADLESS_CONTRACTS_AND_THREE_RESOLUTION_TECHNICAL_QA_CAPTURED__HUMAN_NOT_RUN
CURRENT_NEXT = PHASE2_OPEN_BATTLEFIELD_READINESS_REVIEW__ISSUE_RED_TEST_PROVENANCE_TARGET_RESOLUTION_REQUIRED
```

승인된 구현 구조는 보존하지만 이번 visual closeout이 제품 code/data/scene/runtime 작업을 재개하지 않는다.

## 7. Future implementation sequence after explicit reactivation

```text
PREPARE
→ COMMIT
→ BATTLE
→ REVIEW
```

기존 StageRun/Battle/Roulette foundation을 전면 rewrite하지 않고 orchestration/state layer를 추가하는 것이 retained default다.

## 8. Runtime / human vertical slice evidence

```text
GODOT_IMPORT
HEADLESS_CONTRACTS
RUNTIME_SMOKE
HUMAN_USABILITY
PLAYER_EXPERIENCE
```

앞 단계 PASS를 다음 단계로 자동 전이하지 않는다.

## 9. Platform / release

PC/Steam을 먼저 검증한다. Android/Google Play 실기기·모바일 UI·lifecycle은 PC 제품 구현 완료 후 출시 준비 단계에서 별도 검증한다.

## 10. Historical product-planning lineage

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10 = HISTORICAL_LINEAGE_ONLY
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10 = HISTORICAL_LINEAGE_ONLY
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10 = HISTORICAL_LINEAGE_ONLY
OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
6_OF_10 = HISTORICAL_LINEAGE_ONLY
```

## 11. GitHub live-state rule

```text
CURRENT_OPEN_PRS_AND_ISSUES = FRESH_GITHUB_QUERY_REQUIRED
```

## 12. Current handoff action

```text
CURRENT_NEXT = PHASE2_OPEN_BATTLEFIELD_READINESS_REVIEW__ISSUE_RED_TEST_PROVENANCE_TARGET_RESOLUTION_REQUIRED
IMAGE_GENERATION = USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
IMPLEMENTATION_AUTHORITY = SCOPED_APPROVED_RETAINED
IMPLEMENTATION_EXECUTION = IMPLEMENTED__HEADLESS_CONTRACTS_AND_THREE_RESOLUTION_TECHNICAL_QA_CAPTURED__HUMAN_NOT_RUN
```

For this handoff workstream, the operational action is exact-head PR verification → safe merge → post-merge main readback → stop.
