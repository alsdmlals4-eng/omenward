# [현행] OMENWARD · North Star v2.1 Audit & Correction Brief

```yaml
decision_id: OMW-PLAN-20260824-NORTH-STAR-V2-1-AUDIT-01
status: APPROVED_CURRENT
approved_at: 2026-08-24
approval: USER_APPROVED_AREA_BY_AREA_ACCEPTANCE_AND_CORRECTION_ROUTE
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
source_visual: NORTH_STAR_V2_1_USER_PROVIDED_IMAGE
notion_surface: 13 · 비주얼 컴포넌트 · 전장/룰렛/UI
runtime_mutation: NONE
scene_mutation: NONE
product_data_mutation: NONE
human_runtime_validation: NOT_RUN
```

## 1. 목적

사용자가 제공한 `OMENWARD NORTH STAR v2.1` 시안을 전체 UI final canon으로 일괄 승인하지 않고, **재사용 가능한 방향과 교정이 필요한 영역을 분리**한다.

이 문서는 기존 Visual / 3×3 Roulette / Lower Control Deck owner를 대체하지 않는다. 이미지에서 무엇을 **ADOPT / ADAPT / REJECT**할지 연결하는 현재 감사·교정 owner다.

## 2. 권위와 연결 owner

이 감사는 다음 current owner를 보존한다.

- `docs/design/APPROVED_OMENWARD_VISUAL_STYLE_AND_COMPONENT_CONTRACT_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_BATTLEFIELD_SCALE_AND_COMBAT_READABILITY_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_TOPDOWN_BATTLEFIELD_LAYOUT_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_TOPDOWN_UNIT_SILHOUETTE_RULES_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_3X3_ROULETTE_COMPONENT_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_TOKEN_COMPONENT_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_LOWER_CONTROL_DECK_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_ROULETTE_DDD_FEEDBACK_SPEC_2026-08-20.md`

Notion은 승인 visual과 사람이 읽는 판정·설명을 소유하고, repository는 이 구조화된 상태·규칙·implementation boundary를 소유한다.

## 3. 영역별 판정

| 영역 | 판정 | 처리 |
|---|---|---|
| Battlefield composition | `APPROVED_DIRECTION` | 3전선 전체 표시, 아군 좌측 ↔ Veil 우측, 넓은 combat road, 큰 clash node 방향 재사용 |
| Art / mood / faction contrast | `APPROVED_DIRECTION` | Anime Pixel 유닛 + Clean Pixel 전장 + 절제된 아군/Veil 대비 재사용 |
| Overall North Star | `APPROVED_REFERENCE_WITH_BOUNDARY` | 전장·분위기·정보 위계 reference로 사용하되 전체 UI final canon으로 사용하지 않음 |
| Lower Control Deck | `NEEDS_CORRECTION` | persistent dashboard 밀도를 줄이고 Focus-adaptive single active work surface로 교정 |
| Roulette interaction | `NEEDS_CORRECTION` | 3×3 보드 주변 12개 direct arrow의 대상·방향 affordance를 더 명확하게 교정 |
| Exact text / values / micro-layout | `NON_CANON_REFERENCE` | 이미지 속 문구·수치·패널 폭·픽셀 위치를 제품 수치/최종 UI로 승격하지 않음 |

## 4. ADOPT / ADAPT / REJECT

### ADOPT

- `PRIMARY_VISUAL_MASS = BATTLEFIELD`.
- 상·중·하 세 전선을 한 화면에서 유지한다.
- 아군 본진은 좌측, Veil 측은 우측이라는 큰 방향성을 유지한다.
- 전투로와 접전 노드를 장식보다 먼저 읽히게 한다.
- 상단 HUD와 하단 Control Deck의 역할을 시각적으로 분리한다.
- Anime Pixel unit + Clean Pixel battlefield 조합을 유지한다.

### ADAPT

- 하단 전체 분위기와 프레임 언어는 유지할 수 있으나 내부 정보 구조는 Focus Mode별로 다시 나눈다.
- COMMIT 전선 비교는 유지하되 Roulette Focus와 동시에 큰 패널로 상시 펼치지 않는다.
- 전장 요약은 유용하지만 BATTLE/REVIEW surface에 맞춰 노출한다.
- 3×3 보드의 직접 조작 느낌은 유지하되 row/column arrow를 current component contract 수준으로 강화한다.

### REJECT

- Roulette / Storage / Commit / battlefield summary를 하나의 persistent dashboard처럼 동시에 큰 비중으로 노출하는 구성.
- 이미지의 세부 숫자를 product baseline으로 사용하는 것.
- 이미지의 local copy를 Text UX canon으로 사용하는 것.
- 이미지 한 장을 runtime implementation 완료 또는 usability PASS 증거로 사용하는 것.

## 5. 보호할 North Star 특성

```text
BATTLEFIELD_PRIMARY = TRUE
FULL_THREE_LANES_VISIBLE = TRUE
ALLY_LEFT_VEIL_RIGHT = TRUE
WIDE_COMBAT_ROADS = TRUE
LARGE_READABLE_CLASH_NODES = TRUE
ANIME_PIXEL_UNITS = TRUE
CLEAN_PIXEL_BATTLEFIELD = TRUE
LOWER_DECK_SECONDARY = TRUE
```

이 특성은 후속 correction에서 퇴행시키지 않는다.

## 6. Lower Deck Correction Brief

### 6.1 공통 Shell

```text
ONE_ACTIVE_WORK_SURFACE_AT_A_TIME = TRUE
DUPLICATE_TOP_RESOURCE_TOTALS = FORBIDDEN
PRIMARY_CTA_COUNT = ONE_PER_CURRENT_QUESTION
BATTLEFIELD_VISIBILITY = PRESERVE_FULL_THREE_LANES
```

하단 shell은 유지하되 현재 Mode/Tab의 질문 하나를 중심으로 내부 panel을 교체한다.

### 6.2 Roulette Focus

우선순위:

```text
LEFT_COMPACT = move resources / contextual help
CENTER_DOMINANT = 3×3 board + 12 direct arrows
RIGHT_ACTION = Spin OR Result Confirm + compact result preview
```

필수 교정:

- 각 열의 `↑ / ↓`와 각 행의 `← / →`가 설명 없이 대상과 방향을 읽을 수 있어야 한다.
- arrow hover/focus가 affected row/column preview와 동일하게 연결되어야 한다.
- 토큰 장식과 Tier 표식이 direct-arrow affordance를 압도하지 않는다.
- Storage / COMMIT / battle summary는 Roulette manipulation 동안 큰 고정 패널로 동시에 펼치지 않는다.

### 6.3 COMMIT Focus

```text
stored / newly acquired units
→ pending lane assignment
→ three-lane comparison cue
→ irreversible warning
→ PRIMARY CTA = 배치 확정 · 전투 시작
```

- 3×3 Roulette board는 기본적으로 닫는다.
- pending assignment는 confirm 전 editable plan이다.
- 확정 후 recall / sell / cross-lane 이동 금지 계약을 명확하게 읽힌다.

### 6.4 Build Focus

- building choice / current→after / local cost / construction or upgrade CTA만 우선한다.
- Gold/Mana/Troop total을 하단에서 다시 복제하지 않는다.
- TokenSource/roulette 영향이 있는 건물은 한 줄 preview로 연결한다.

### 6.5 Battle / Review Focus

- BATTLE은 tactical quick access와 target/cooldown/local Mana cost만 필요 시 전개한다.
- REVIEW는 Forecast → Prepare → Commit → Key Event → Result 인과를 요약한다.
- raw battle log와 전체 dashboard는 기본 surface에서 숨긴다.

## 7. Component Breakdown

North Star v2.1을 다음 재사용 가능한 컴포넌트 단위로 분리해 후속 시각/구현 handoff의 입력으로 사용한다.

### Battlefield

- `BattlefieldViewport`
- `AllyCitadelAnchor`
- `VeilCitadelAnchor`
- `LaneBand × 3`
- `WideCombatRoad`
- `ClashNode`
- `StrongholdNode`
- `BuildNode`
- `LaneLabel`
- `ForecastLegend / RouteCue`

### Top HUD

- `GoldCounter`
- `SecondaryResourceCounter`
- `TroopLimitCounter`
- `StageWaveIndicator`
- `PauseSpeedSettings`

### Lower Shell

- `FocusModeNav`
- `ActiveWorkSurface`
- `PrimaryCTA`
- `ContextHelp`

### Roulette Surface

- `Roulette3x3Board`
- `ColumnUpControl × 3`
- `ColumnDownControl × 3`
- `RowLeftControl × 3`
- `RowRightControl × 3`
- `MoveResourcePanel`
- `SpinControl`
- `ResultConfirmControl`
- `CompactResultPreview`

### Commit Surface

- `StoredUnitList`
- `PendingLaneAssignment`
- `LaneComparisonCue`
- `IrreversibleCommitWarning`
- `CommitPrimaryCTA`

### Build / Battle / Review

- `BuildChoiceStrip`
- `BuildEffectPreview`
- `TacticalQuickAccess`
- `BattlefieldRealtimeSummary`
- `CausalReviewTimeline`

## 8. 이미지와 구현 경계

```text
VISUAL_REFERENCE = APPROVED_WITH_BOUNDARY
FINAL_UI_GEOMETRY = NOT_APPROVED
FINAL_COPY = NOT_APPROVED_FROM_IMAGE
FINAL_PRODUCT_NUMERICS = NOT_APPROVED_FROM_IMAGE
GODOT_RUNTIME = NOT_RUN
UI_RUNTIME = NOT_RUN
HUMAN_USABILITY = NOT_RUN
PLAYER_EXPERIENCE = NOT_RUN
IMPLEMENTATION_AUTHORIZED = FALSE
```

이미지가 존재하고 Notion에 붙었다는 사실을 runtime 또는 player evidence로 승격하지 않는다.

## 9. 다음 순서

```text
COMPLETE = NORTH_STAR_V2_1_AREA_AUDIT
CURRENT = LOWER_DECK_AND_ROULETTE_CORRECTION_BRIEF_COMPLETE
NEXT = COMPONENT_BREAKDOWN_REUSE_IN_FINAL_PLANNING_REVIEW
THEN = FINAL_PLANNING_ADVERSARIAL_REVIEW
CORRECTED_NORTH_STAR_IMAGE = USER_EXPLICIT_IMAGE_REQUEST_ONLY
IMPLEMENTATION_HANDOFF = EXPLICIT_USER_AUTHORITY_REQUIRED
```

새 이미지를 자동 생성하지 않는다. 현재 승인 범위의 비이미지 planning/review는 계속 진행할 수 있다.

## 10. 재검토 조건

다음 중 하나가 생기면 이 판정을 다시 연다.

- 사용자가 v2.1의 Lower Deck / Roulette 부분까지 명시적으로 제품 방향으로 바꾸길 원함.
- runtime blockout에서 full-three-lane 가독성과 compact deck이 동시에 성립하지 않음.
- 960×540 / 1280×720 / 1920×1080에서 동일 정보 위계가 유지되지 않음.
- keyboard/controller focus route가 direct-arrow 구조에서 과도하게 복잡해짐.
- human usability test에서 현재 질문·Primary CTA·비가역 COMMIT 의미를 반복적으로 오해함.
