# 오멘워드 현재 구현 상태

- 갱신일: 2026-08-04
- 전체 시스템 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 최신 아트 정본: `docs/design/APPROVED_OMENWARD_PIXEL_ILLUSTRATION_HYBRID_ART_DIRECTION_2026-08-04.md`
- 최신 HUD 보완: `docs/design/APPROVED_OMENWARD_HUD_ROULETTE_LAYOUT_AND_BATTLEFIELD_VIEW_AMENDMENT_2026-08-04.md`
- 작업 모드: `TOTAL_PLANNING / CORE_FUN_CONTENT_VISUAL_PROFILE`
- 최신 기획 상태: `USER_APPROVED_ACTIVE_BRANCH_NOT_IMPLEMENTED`
- 현재 Decision: `OMW-DEC-20260804-PLANNING-PIXEL-ILLUSTRATION-HYBRID-ART-DIRECTION-V1`
- 제품 코드 승인: `NOT_AUTHORIZED`
- 실제 아트 자산 제작: `NOT_AUTHORIZED`
- 이미지 생성: `STOPPED_BY_USER`
- 최신 버티컬 슬라이스 구현: `NOT_STARTED`

## 1. 정확한 상태 표기

```text
VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED
LATEST_AUTOMATED_CONTRACTS_NOT_RUN
HUMAN_QA_NOT_RUN
CORE_LOCK_NOT_ALLOWED
```

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED_PLANNING = PIXEL_ILLUSTRATION_HYBRID_ART_DIRECTION_DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

문서 계약과 CI 통과는 최신 Vertical Slice·HUD·룰렛·아트 방향이 제품에 구현됐다는 뜻이 아니다.

## 2. Legacy 검증 증거

```text
LEGACY_C1_C2_C3_PROVEN
LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
```

- C1 구현 검증 head: `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9`
- C1 최종 검증 run: `29926598807`

이 증거는 과거 Legacy C1 룰렛 계약의 원격 검증을 뜻한다. 최신 V2 전체 시스템, 20 Stage Vertical Slice, Planning Stack, 픽셀·일러스트 하이브리드 아트 구현을 증명하지 않으며 **V2 구현 완료를 뜻하지 않는다**.

## 3. 현행 작업 권한

```text
GPT / Work
= 핵심 재미·플레이 동기·콘텐츠 기획·플레이어 규칙·UX·이미지·아트 방향·검수 기준

Codex
= 자료구조·알고리즘·좌표·경로탐색·물리·성능·코드·테스트 구현
```

기존 1~6 Decision의 기술 세부는 `CODEX_REFERENCE_RECOMMENDATION / NOT_BINDING_IMPLEMENTATION`이다. 플레이어에게 보이는 규칙·밸런스 의도·가독성 목표는 승인 상태다.

## 4. 승인 Planning Stack

```text
P0 결과 재현·원인 복기 요구
P1 공통 전투 공정성·숨은 선공 금지
P2 Damage·Protection·Status 의미
P3 방어·Barrier·Status 기획 기본값
P4 전투 템포·Spawn 가독성 의도
P5 Modifier 폭증 방지·효과 가독성
P6 세 전선·Route·Targeting 경험
P7 전장 시각 계층·카메라·정보 밀도
P8 HUD·룰렛 정보·자원·상인·건물 역할
P9 픽셀·일러스트 하이브리드 아트 방향·자산 계보
```

## 5. 최신 플레이어 규칙

```text
BOTTOM_FUNCTIONS = ROULETTE / STORAGE / BUILD / TACTICAL_SKILL / BELU
MAIN_HUD_RESOURCES = GOLD / MANA_STONE / DEPLOYED_TROOP_CAPACITY
MOVE_TICKET = ROULETTE_PANEL_ONLY / STORED_CAP_3
MERCHANT = AFTER_STAGE_MAINTENANCE_ONLY
BUILDINGS = VAULT / FARM / BARRACKS / DEFENSE_TOWER / COMMAND_POST / MANA_TOWER
```

- 건물별 지속 유지비는 없다.
- 토큰은 초당 공급되지 않는다.
- 보상 등급은 완성선 수로 결정한다.
- 지휘소는 현재 MapRun 전체 아군 병력 오라다.
- 벨루는 우측 하단에서 상황과 선택 근거만 제공한다.

## 6. 최신 시각 규칙

```text
STYLE = PIXEL_ILLUSTRATION_HYBRID
BATTLEFIELD = PIXEL_READABILITY + ILLUSTRATED_MATERIAL_AND_LIGHT
CLOSEUP_UI = ILLUSTRATION_FORWARD
ALLY = IVORY / BLUE / RESTRAINED_GOLD
VEIL = CHARCOAL / DEEP_PURPLE / CRIMSON / ASYMMETRIC_GOTHIC
```

룰렛 자산:

```text
GOLD_TOKEN_ART = IN_GAME_GOLD_IMAGE
TROOP_TOKEN_ART = IN_GAME_T1_T2_TROOP_IMAGE
T3_TROOP_TOKEN = FORBIDDEN
RESULT_REWARD_ART = ACTUAL_REWARDED_TROOP_IMAGE
SEPARATE_GOLD_OR_TROOP_TOKEN_ICON_PRODUCTION = FORBIDDEN
```

## 7. 구현 상태 행렬

| 영역 | 기획 상태 | 제품 구현 | 자동 검증 | 사람 검증 |
|---|---|---|---|---|
| 20 Stage 전체 시스템 Vertical Slice | 승인 정본 존재 | `NOT_STARTED` | `NOT_RUN_LATEST` | `NOT_RUN` |
| 전투 의미·공정성·기본값 | 승인 정본 존재 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 전투 공간·Route·Targeting | 플레이 경험 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 전장 시각 계층·카메라 | 플레이 경험 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| HUD·룰렛·자원·상인·건물 6종 | 사용자 승인 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 픽셀·일러스트 하이브리드 아트 | 사용자 승인 10/10 | `NOT_STARTED` | `NOT_RUN` | `NOT_RUN` |
| 실제 이미지·Animation·VFX | 사용자 중단 | `NOT_AUTHORIZED` | `N/A` | `NOT_RUN` |
| Codex 구현 계약 | Preflight 이후 별도 승인 | `BLOCKED` | `NOT_RUN` | `NOT_RUN` |

## 8. Decision 10 구현 검수 목표

- 먼 카메라에서 병종·전선·노드가 읽힌다.
- 근접 카드와 벨루에서는 동화풍 일러스트 매력이 유지된다.
- 아군과 Veil이 색뿐 아니라 실루엣·재질·형태로 구분된다.
- Tier 상승이 단순 색 변경·몸집 확대가 아니다.
- 건물 6종이 텍스트 없이도 역할별 실루엣으로 구분된다.
- UI·VFX·벨루가 전장 정보를 가리지 않는다.
- 룰렛 금화·병종 토큰을 위해 별도 자산을 만들지 않는다.
- T3 병종은 룰렛 병종 토큰에 나오지 않는다.
- 토큰·결과·보관함·배치·전장의 병종 디자인 계보가 일치한다.

## 9. CI 호환 marker

```text
CURRENT_VERTICAL_SLICE_AUTHORITY = design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md
CURRENT_ADVERSARIAL_REVIEW_LINEAGE = reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md
ROULETTE_AGENCY_EVIDENCE = benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md
PILOT_RECOMMENDATION / NOT_CANON
```

## 10. 남은 차단 요인

```text
FRESH_PREFLIGHT = REQUIRED_AT_10_OF_10
ART_ASSET_PRODUCTION_PLAN = REQUIRES_SEPARATE_USER_DIRECTION
CORE_FUN_AND_CONTENT_DEEPENING = NEXT_GPT_WORK
CODEX_IMPLEMENTATION_PLAN = BLOCKED_UNTIL_SEPARATE_HANDOFF
PRODUCT_CODE_AUTHORITY = NONE
```
