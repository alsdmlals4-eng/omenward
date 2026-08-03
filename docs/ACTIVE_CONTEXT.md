# Active Context

```yaml
updated_at: 2026-08-04
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_BUILDING_ROSTER_APPROVED
current_planning_decision: OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1
current_process_policy: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
current_branch: main
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-simulation-harness-planning-20260803
active_base_version: 9.4.3
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
product_code_authority: NONE
image_production_authority: PAUSED_BY_USER
codex_execution: BLOCKED_UNTIL_PLANNING_AND_VISUAL_PREFLIGHT
current_grill_me_count: 9
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
→ SpinSnapshot 이동·결과 확정
→ 보관·판매·한 전선 비가역 배치
→ 자동전투·점령·건물 운영
→ 결과 원인 복기
→ 다음 Stage 설계
```

전체 시스템 Vertical Slice 정본은 `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`다. Decision 9에서 변경한 HUD·자원·상인·건물 역할은 `design/APPROVED_OMENWARD_COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_AND_BUILDING_ROSTER_2026-08-04.md`가 최신 우선 정본이다.

## 2. GPT 역할과 작업 우선순위

```text
GPT / Work
= 핵심 재미·플레이 동기·콘텐츠 기획·플레이어 규칙·UX·이미지·아트 방향·검수 기준

Codex
= 자료구조·알고리즘·좌표·경로탐색·물리·성능·코드·테스트 구현
```

GPT 우선순위:

```text
1. 핵심 재미와 반복 플레이 동기
2. Stage·Wave·Boss·영웅·병종·건물 콘텐츠 구조
3. UX·이미지·아트 표현
4. 구현에 필요한 결과 조건과 검수 기준
```

기존 검증 문서의 플레이어 경험과 밸런스 의도는 유지한다. `30 TPS`, 정수 좌표·시간, R00~R130 명칭, Schema·정렬 키 같은 기술 세부는 `CODEX_REFERENCE_RECOMMENDATION / NOT_BINDING_IMPLEMENTATION`으로 재분류한다.

Codex 구현이 핵심 재미·콘텐츠 역할·플레이어가 보는 이동·Targeting·밸런스·UX를 바꾸면 다시 Grill Me 승인을 받는다.

## 3. 승인된 Planning Stack

```text
1. Deterministic outcome·provenance requirement
2. Common combat behavior and same-tick fairness intent
3. Damage·Protection·Status player-facing semantics
4. Mitigation·Barrier·Status design defaults
5. Combat tempo·spawn readability intent
6. Modifier readability·stacking guard intent
7. Combat space·route·targeting experience
8. Battlefield visual hierarchy·camera·information density
9. Combat HUD·roulette information·resources·merchant·building roster
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
design/APPROVED_OMENWARD_BATTLEFIELD_VISUAL_HIERARCHY_AND_CAMERA_2026-08-04.md
design/APPROVED_OMENWARD_COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_AND_BUILDING_ROSTER_2026-08-04.md
```

## 4. Decision 9 — HUD·룰렛·자원·상인·건물

평상시 하단 기능 순서:

```text
[룰렛] [보관함] [건설] [전술스킬] [벨루]
```

- 상시 상점 버튼은 제거한다.
- 벨루는 우측 하단 초상과 상황 대사로만 사용한다.
- 평상시 핵심 자원은 골드·마석·배치 병력/병력 한도다.
- 이동권은 룰렛 정보 패널 안에서 `보관 이동권 n/3`과 `럭키 무료 이동`으로 표시한다.
- 건물별 지속 유지비와 토큰 초당 공급 표시는 사용하지 않는다.
- 룰렛 조작은 릴/행 선택→이동 미리보기→실행 순서다.
- 보상 등급은 독립 희귀도 확률표가 아니라 동일 심벌 완성선 수로 결정한다.
- Stage 종료 정비시간에 유한 재고 상인이 방문한다.

기본 건물 6종:

```text
금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
```

- 농장은 병력 한도를 확장한다.
- 지휘소는 주변 반경이 아니라 현재 MapRun 전체 아군 배치 병력 오라다.
- 같은 지휘소 계열은 최고 Tier만 적용하고 돌격·수비 계열은 함께 활성화할 수 있다.
- 마력탑은 마석 수급 또는 최대 보유량을 강화한다.

## 5. 이미지·아트 경계

사용자 지시에 따라 현재 이미지 생성은 중단한다.

```text
IMAGE_GENERATION = PAUSED_BY_USER
EXISTING_GENERATED_IMAGES = CONCEPT_REFERENCE_ONLY / NOT_CANON
```

10/10에서는 추가 이미지를 생성하지 않고, 아트 방향·실루엣·색·재질·등급 성장 문법과 최종 Brief를 텍스트로 확정한 뒤 preflight를 수행한다.

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
OMW-AUD-290~299 Planning boundary and combat-space readability
OMW-AUD-300~313 Battlefield visual hierarchy·camera·core-fun priority
OMW-AUD-314~330 HUD·roulette·resource·merchant·building-role integrity
```

## 7. 구현·제작 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_BUILDING_ROSTER_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
IMAGE_PRODUCTION = PAUSED_BY_USER
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 8. 다음 Gate

```text
GRILL_ME_COUNT = 9/10
10/10 = ART_DIRECTION_AND_IMAGE_PROTOTYPE_BRIEF
NEXT_PREFLIGHT = AT_10_OF_10
```
