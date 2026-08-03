# Active Context

```yaml
updated_at: 2026-08-04
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: COMBAT_SPACE_ROUTE_AND_TARGETING_EXPERIENCE_APPROVED
current_planning_decision: OMW-DEC-20260804-PLANNING-COMBAT-SPACE-ROUTE-AND-TARGETING-EXPERIENCE-V1
current_process_policy: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
current_branch: main
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-simulation-harness-planning-20260803
active_base_version: 9.4.3
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
product_code_authority: NONE
image_production_authority: NONE
codex_execution: BLOCKED_UNTIL_PLANNING_AND_VISUAL_PREFLIGHT
current_grill_me_count: 7
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
preflight: NEXT_AT_10_OF_10
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

`current_main`과 `context_baseline_commit`은 실행 시점 저장소에서 해석한다.

## 1. 프로젝트 코어

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
예고된 세 전선 공세 읽기
→ 제한된 건물·TokenSource로 세 원형 릴 설계
→ SpinSnapshot 결과 보관·판매·획득
→ 한 전선에 비가역 배치
→ 자동전투·점령·건물 운영
→ 결과 원인 복기
→ 다음 Stage 설계
```

전체 시스템 Vertical Slice 정본은 `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`다.

## 2. 작업 권한 경계

```text
GPT / Work
= 게임 기획·플레이어 규칙·콘텐츠·UX·아트 방향·이미지 Brief·검수 기준

Codex
= 자료구조·알고리즘·좌표·경로탐색·물리·성능·코드·테스트 구현
```

기존 검증 문서의 플레이어 경험과 밸런스 의도는 유지한다. `30 TPS`, 정수 좌표·시간, R00~R130 명칭, Schema·정렬 키 같은 기술 세부는 `CODEX_REFERENCE_RECOMMENDATION / NOT_BINDING_IMPLEMENTATION`으로 재분류한다.

Codex 구현이 플레이어가 보는 이동·Targeting·밸런스·UX를 바꾸면 다시 Grill Me 승인을 받는다.

## 3. 승인된 Planning Stack

```text
1. Deterministic outcome·provenance requirement
2. Common combat behavior and same-tick fairness intent
3. Damage·Protection·Status player-facing semantics
4. Mitigation·Barrier·Status design defaults
5. Combat tempo·spawn readability intent
6. Modifier readability·stacking guard intent
7. Combat space·route·targeting experience
```

책임 원본:

```text
design/APPROVED_OMENWARD_DETERMINISTIC_SIMULATION_HARNESS_SCOPE_2026-08-03.md
design/APPROVED_OMENWARD_COMMON_COMBAT_SCHEMA_AND_RESOLUTION_ORDER_2026-08-03.md
design/APPROVED_OMENWARD_DAMAGE_PROTECTION_AND_STATUS_SEMANTICS_2026-08-03.md
design/APPROVED_OMENWARD_MITIGATION_FORMULA_AND_PROTECTION_NUMERIC_DEFAULTS_2026-08-03.md
design/APPROVED_OMENWARD_FIXED_TICK_TIME_AND_ACTIVATION_DEFAULTS_2026-08-03.md
design/APPROVED_OMENWARD_MODIFIER_STACKING_AND_EFFECT_PRECEDENCE_2026-08-03.md
design/APPROVED_OMENWARD_COMBAT_SPACE_ROUTE_AND_TARGETING_EXPERIENCE_2026-08-04.md
```

## 4. Decision 7 — 전투 공간·이동·Targeting

```text
THREE_FRONTS = TOP / MID / BOTTOM
MAIN_ROUTE = visible per front
BYPASS_AND_AIR_ROUTE = visible and telegraphed
DEFAULT_TARGET = nearest valid target on same front/route
CROSS_LANE = explicit ability/building only
HIDDEN_AUTO_LANE_CHANGE = FORBIDDEN
```

- Ground는 전열·후열과 혼잡을 화면에 형성한다.
- Flying은 Ground 혼잡을 넘지만 전선·Target 규칙을 무시하지 않는다.
- 침투 병력은 입구·이동·출구가 보이는 우회로를 사용한다.
- Target 변경은 사망·사거리·은신·도발·Route 변경 등 설명 가능한 이유가 있어야 한다.

## 5. 전장 이미지 요구

후속 이미지는 다음을 실제 규칙과 함께 보여야 한다.

```text
세 전선 전체 구도
주 경로·우회로·공중 경로 Overlay
전열·후열·Flying·Target 방향
Cross-lane 지원·공격 범위
```

분위기만 좋은 Concept Art가 아니라 GDD를 설명하는 이미지가 목표다.

## 6. 적대적 감사 계보

```text
OMW-AUD-208~220 Harness
OMW-AUD-221 Sheet HEAD correction / RESOLVED / NON_COUNTER
OMW-AUD-222~232 Common Combat
OMW-AUD-233~246 Damage Semantics
OMW-AUD-247~260 Numeric Defaults
OMW-AUD-261 CI compatibility restore / RESOLVED / NON_COUNTER
OMW-AUD-262~275 Time/Activation
OMW-AUD-276~289 Modifier/Precedence
OMW-AUD-290~299 Planning/Visual boundary and combat-space readability
```

## 7. 구현·제작 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = COMBAT_SPACE_ROUTE_TARGETING_EXPERIENCE_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
IMAGE_PRODUCTION = NOT_AUTHORIZED_UNTIL_10_OF_10_PREFLIGHT
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 다음 Gate

```text
GRILL_ME_COUNT = 7/10
8/10 = BATTLEFIELD_VISUAL_HIERARCHY_AND_CAMERA
9/10 = COMBAT_HUD_REEL_AND_BUILD_UX
10/10 = ART_DIRECTION_AND_IMAGE_PROTOTYPE_BRIEF
NEXT_PREFLIGHT = AT_10_OF_10
```
