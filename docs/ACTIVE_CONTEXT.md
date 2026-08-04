# Active Context

```yaml
updated_at: 2026-08-04
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: PIXEL_ILLUSTRATION_HYBRID_ART_DIRECTION_APPROVED
current_planning_decision: OMW-DEC-20260804-PLANNING-PIXEL-ILLUSTRATION-HYBRID-ART-DIRECTION-V1
current_process_policy: OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1
current_branch: main
context_baseline_commit: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
working_branch: gpt/omenward-simulation-harness-planning-20260803
active_base_version: 9.4.3
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
codex_execution: BLOCKED_UNTIL_PLANNING_PREFLIGHT
current_grill_me_count: 10
future_merge_cadence: EVERY_10_APPROVED_GRILL_ME_DECISIONS
preflight: REQUIRED_NOW_AT_10_OF_10
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
→ 릴·행 이동과 회전 결과 확정
→ 보관·판매·한 전선 비가역 배치
→ 자동전투·점령·건물 운영
→ 결과 원인 복기
→ 다음 Stage 설계
```

전체 시스템 Vertical Slice 정본은 `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`다. 최신 HUD·자원·상인·건물 역할은 Decision 9가, 최신 시각 문법은 Decision 10이 우선한다.

## 2. GPT와 Codex 역할

```text
GPT / Work
= 핵심 재미·플레이 동기·콘텐츠 기획·플레이어 규칙·UX·이미지·아트 방향·검수 기준

Codex
= 자료구조·알고리즘·좌표·경로탐색·물리·성능·코드·테스트 구현
```

GPT 우선순위는 핵심 재미 → 콘텐츠 구조 → UX·이미지·아트 → 구현 결과 조건이다. Codex 구현이 플레이어 경험과 기획 역할을 바꾸면 다시 Grill Me 승인을 받는다.

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
10. Pixel·illustration hybrid art direction and asset lineage
```

Decision 10 책임 원본:

`design/APPROVED_OMENWARD_PIXEL_ILLUSTRATION_HYBRID_ART_DIRECTION_2026-08-04.md`

## 4. Decision 9 — HUD·룰렛·자원·상인·건물

```text
평상시 하단 = [룰렛] [보관함] [건설] [전술스킬] [벨루]
핵심 자원 = 골드 / 마석 / 배치 병력·병력 한도
이동권 = 룰렛 패널 내부 n/3 + 럭키 무료 이동
상인 = Stage 종료 정비시간
건물 = 금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
지휘소 = 현재 MapRun 전체 아군 병력 오라
```

룰렛 작업대는 낮고 가로로 길며 좌측 규칙, 중앙 3×3 보드와 이동 화살표, 우측 회전·결과·벨루로 구성한다.

## 5. Decision 10 — 최종 아트 방향

```text
STYLE = PIXEL_ILLUSTRATION_HYBRID
MOOD = FAIRYTALE_HOLY_FANTASY_VS_VEIL_GOTHIC
BATTLEFIELD = PIXEL_READABILITY + ILLUSTRATED_MATERIAL_AND_LIGHT
CLOSEUP_UI = ILLUSTRATION_FORWARD
```

- 전장에서는 먼 카메라 가독성과 역할 실루엣을 우선한다.
- 보상·도감·벨루에서는 일러스트의 재질·표정·동화 감성을 강화한다.
- 아군은 상아·청색·절제된 금색, Veil은 흑색·심자색·적자색을 사용한다.
- Veil은 아군 자산의 단순 재도색이 아니라 비대칭·가시·유기 고딕 형태를 사용한다.
- Tier 상승은 색 변경이나 몸집 확대가 아니라 장비·자세·실루엣·역할 판타지로 표현한다.

룰렛 자산:

```text
금화 토큰 = 인게임 금화 이미지
병종 토큰 = 인게임 T1·T2 병종 이미지
T3 병종 토큰 = 금지
결과 보상 = 실제 지급 병종 이미지
별도 금화·병종 토큰 아이콘 제작 = 금지
```

## 6. 이미지·제작 경계

```text
IMAGE_GENERATION = STOPPED_BY_USER
EXISTING_GENERATED_IMAGES = SELECTION_EVIDENCE_AND_LAYOUT_REFERENCE_ONLY / NOT_CANON_ASSETS
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
```

사용자가 별도로 제작 재개를 지시하기 전까지 추가 이미지·애니메이션·VFX 자산을 만들지 않는다.

## 7. 적대적 감사 계보

```text
OMW-AUD-208~289 = Decisions 1~6 and maintenance
OMW-AUD-290~299 = planning boundary and combat-space readability
OMW-AUD-300~313 = battlefield visual hierarchy·camera·core-fun priority
OMW-AUD-314~343 = HUD·roulette·resources·merchant·building and asset reuse
OMW-AUD-344~359 = pixel·illustration hybrid art direction integrity
```

## 8. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = PIXEL_ILLUSTRATION_HYBRID_ART_DIRECTION_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 9. 다음 Gate

```text
GRILL_ME_COUNT = 10/10
NEXT_ACTION = FRESH_PREFLIGHT_AND_ADVERSARIAL_REVIEW
NEXT_PLANNING = CORE_FUN_AND_CONTENT_DEEPENING_AFTER_CANON_SYNC
NEXT_IMPLEMENTATION = SEPARATELY_AUTHORIZED_CODEX_HANDOFF
```
