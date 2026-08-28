# Omenward Storybook SD · Three-Front Strategic Map Visual Direction

```yaml
decision_id: OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01
issue: 239
revision_issue: 241
board_revision_issue: 243
map_only_revision_issue: 245
battlefield_layout_amendment: OMW-PLAN-20260828-BASE-FORWARD-BATTLEFIELD-CONSTRUCTION-LAYOUT-01
status: USER_CONFIRMED_CURRENT__V6_OPEN_BATTLEFIELD_VISUAL_LOCKED
revision: 2026-08-29__V6_OPEN_BATTLEFIELD_VISUAL_LOCK
approval_source: "2026-08-28 user: 1번이미지 = 그림체, 2번이미지 = 전장 미니맵·UI; 세 전선이 다 보이게; Ward 본진에서 3갈래로 뻗어져 나감; 전진기지·접전지 배치; 하단 룰렛 이미지 제거; Veil도 Ward와 같은 단일 본진 구조; 본진 건물 제거; 본진 건설 노드 4·방어탑 2, 전진기지당 건설 노드 2·방어탑 1; 2026-08-29 user: v6 열린 전장 보드 확정"
scope: VISUAL_DIRECTION_LOCK_AND_PLANNING_BOARD_ONLY
runtime_implementation: NOT_AUTHORIZED_BY_THIS_DECISION
runtime_target_asset: NOT_CREATED
```

## 1. Decision

Run Command의 주 전장 표현은 가까운 전투 배경 일러스트가 아니라, 세 전선이 동시에 보이는 **전략 지도 UI**다. 지도에는 **단 하나의 Ward Citadel 본진**과 **단 하나의 Veil Citadel 본진**이 있고, 양쪽 본진이 각각 상·중·하 세 전선을 공유한다. 플레이어는 Ward 본진에서 시작한 세 갈래가 세 접전지를 거쳐 Veil 본진으로 되돌아드는 대칭 구조 안에서 위험·route·commit 결과를 읽는다.

전체 그림체는 밝은 아이보리·종이 질감 위의 동화풍 수채화 SD 전술 일러스트다. 부대는 2.5~3등신이며 얇은 청회색 선, 부드러운 수채화 명암, 읽기 쉬운 역할 실루엣을 사용한다.

## 2. Reference and rights boundary

| Reference | Role | Status |
|---|---|---|
| User-provided image 1 (`codex-clipboard-2a40138e-df7c-4fb8-ab74-25ae363bd13c.png`) | rendering, proportion, paper/ink/watercolor language | REFERENCE_ONLY__NOT_PROJECT_ASSET__RIGHTS_UNVERIFIED |
| User-provided image 2 (`codex-clipboard-11752bf6-5e9b-4c31-b863-923bad673089.png`) | simultaneous-three-front map hierarchy and route readability | REFERENCE_ONLY__NOT_PROJECT_ASSET__RIGHTS_UNVERIFIED |

References are not copied into the product, promoted to runtime assets, or used as proof of commercial-use rights. The project keeps only original direction documentation and generated planning work with provenance.

## 3. Visual Direction Lock Packet

### Global anchor

```text
VISUAL_STYLE = STORYBOOK_WATERCOLOR_SD_TACTICAL_ILLUSTRATION
RENDERING_LANGUAGE = IVORY_PAPER + DELICATE_BLUE_GRAY_INK + SOFT_WATERCOLOR + RESTRAINED_PIXEL_TACTILITY
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
CAMERA = WIDE_ORTHOGRAPHIC_STRATEGIC_MAP
PRIMARY_VISUAL_MASS = THREE_FRONT_STRATEGIC_MAP
SECONDARY_VISUAL_MASS = FOCUS_ADAPTIVE_LOWER_CONTROL_DECK
BATTLEFIELD_PRESENTATION = ONE_SIMULTANEOUS_THREE_FRONT_STRATEGIC_MAP
PER_FRONT_MINIMAP = ABSORBED_INTO_PRIMARY_STRATEGIC_MAP
MAP_TOPOLOGY = ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT
PARALLEL_THREE_LANE_COMPOSITION = FORBIDDEN
FRONT_STRUCTURE = ONE_WARD_CITADEL_ROOT -> THREE_SHARED_FRONTS -> ONE_VEIL_CITADEL_ROOT
ROUTE_STATE_GRAMMAR = WARD_CITADEL_HOME_BASE -> WARD_FORWARD_BASE -> CONTESTED_CLASH_ZONE -> VEIL_FORWARD_BASE -> VEIL_CITADEL_HOME_BASE
FORWARD_BASE = ROUTE_OUTPOST__NOT_ADDITIONAL_HOME_BASE
CLASH_ZONE = ACTIVE_WARD_VS_VEIL_CONTACT_NODE__NOT_GENERIC_ROUTE_DECORATION
HOME_BASE_PREBUILT_PRODUCTION_BUILDINGS = NONE
HOME_BASE_CONSTRUCTION_NODE_COUNT_PER_FACTION = 4
HOME_BASE_FIXED_AUTO_ATTACK_TOWER_COUNT_PER_FACTION = 2
FORWARD_BASE_CONSTRUCTION_NODE_COUNT_PER_BASE = 2
FORWARD_BASE_FIXED_AUTO_ATTACK_TOWER_COUNT_PER_BASE = 1
FORWARD_BASE_FIXED_DEFENSE_STACK = AUTO_ATTACK_TOWER_ONLY
FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL
FENCED_OR_ENCLOSED_BASE_BOUNDARY = FORBIDDEN
PROJECT_CORE_SCENE_VISUAL_BOARD_SCOPE = STRATEGIC_MAP_ONLY__LOWER_UI_STORYBOARD_REMOVED
ROULETTE_SYSTEM = RETAINED__NOT_VISUALIZED_IN_CURRENT_MAP_ONLY_BOARD
```

### Character / environment / UI / VFX anchors

- **Character:** shield, banner, weapon, silhouette, faction color를 장식보다 먼저 읽는다. 수호군은 navy/ivory/pale steel/restrained gold, Veil은 charcoal/plum-black/dark violet/limited rift glow다.
- **Environment:** 화면의 양 끝에는 Ward Citadel과 Veil Citadel이 각각 하나씩 있다. 본진은 거대 성·병영·농장 군집·울타리 없이 열린 지형의 지휘 표식, 고정탑 2개, 빈 건설 패드 4개로 읽힌다. 각 branch의 전진기지에는 고정탑 1개·빈 패드 2개만 있으며 바리케이드와 닫힌 경계는 없다. 양쪽 본진에서 갈라진 상·중·하 route는 바위 능선·얕은 물길·분화구·연기와 넓은 세 접전지에서 맞물린다. Ward는 navy/ivory, Veil은 charcoal/violet으로 구분하되 구조적 수량은 대칭이다.
- **Route state:** 각 branch는 `Ward 본진 → Ward 전진기지 → Ward/Veil 접전지 → Veil 전진기지 → Veil 본진` 순서로 읽힌다. 양쪽 전진기지는 home base가 아닌 route outpost다. 접전지는 양 진영 SD 병력·손상 지형·crossed-swords signifier로 보이는 contested contact node다.
- **UI:** 종이 패널, 정교한 얇은 테두리, 상징 기반 아이콘, 제한된 금색 강조를 사용한다. UI는 지도 위에 과적되지 않으며 3×3 roulette은 계속 노출된다.
- **VFX:** 아주 작은 별빛, 수호 문장 광택, 균열의 보랏빛 glow만 허용한다. full-screen flash, 과도한 흔들림, 시야를 가리는 보상 연출은 금지한다.

### Keep / Avoid / Do Not Drift

| Keep | Avoid | Do Not Drift |
|---|---|---|
| Ward/Veil 각각 단일 본진, 양측 각 branch의 전진기지, 세 접전지, 전선 동시 가독성, 전장-primary, silhouette-first | 카지노/도박 표현, 가짜 near miss, copied character/UI, 조밀한 개체 단위 미니맵, 장식이 정보보다 앞서는 화면, 세 개의 독립 본진, 병렬 3-lane road, 접전지 없는 장식 node, 지도 보드 안의 하단 roulette/storyboard | player-constructed probability engine, fixed reel-to-lane mapping 금지, 비가역 commit, Ward 대 Veil 양 진영, 아이보리/남색 대 어두운 보랏빛 명도 위계 |

### Allowed variation

상·중·하 branch는 지역·시간대·위협 상태에 따라 식생, 물길, 석재, 안개, Veil 균열 밀도를 다르게 가질 수 있다. 다만 **한 본진 → 세 갈래** topology, 종이/수채화/잉크 문법, faction color hierarchy, route node 의미는 유지한다.

## 4. Confirmed Flow / Screen anchors

| Screen | Player need | Required information | Feedback |
|---|---|---|---|
| PREPARE | 어느 전선의 미래 압력이 가장 위험한지 본다 | 세 route, threat class, advance direction, stronghold state | forecast emphasis only; 정답 빌드 지시 금지 |
| 3×3 ROULETTE | 결과를 읽고 행/열 조작을 검토한다 | 3×3, 선택 항목, move budget, preview | 선택/조작이 결과 의미를 즉시 갱신 |
| COMMIT | 얻은 병력을 한 전선에 쓸지 결정한다 | 세 전선의 현재 압력·route·commit target | atomic irreversible confirmation |
| BATTLE | 세 전선의 결과 변화를 한눈에 읽는다 | friendly/Veil advance, clash, priority threat | 지도 상태 강조; UI는 두 번째 전장을 만들지 않음 |
| REVIEW | 선택의 인과를 복기한다 | forecast → design → commit → outcome | 인과 연결, 처방식 next build 금지 |

## 5. Supersession and legacy boundary

- `OMW-VISUAL-20260828-BATTLEFIELD-MAP-ROULETTE-PICKER-01`의 **가까운 확대 전장 backdrop 표현**은 이 Decision이 supersede한다. 해당 Decision의 3×3 tile/list inspection behavior는 retained다.
- `OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01`의 세 전선 동시 책임, 전장-primary, compact lower deck, silhouette-first rule은 retained다. 세부 rendering language와 close-battlefield framing은 이 Decision이 supersede한다.
- `OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1`는 현 빌드가 실제로 소비하는 **LEGACY_RUNTIME_ASSET**이다. 삭제·교체·runtime PASS 취소를 뜻하지 않는다. 새 target asset은 별도 Phase 2 implementation packet과 provenance review 뒤에만 생성·적용한다.
- 기존 P0 unit idle master와 Shield Guard animation production contract는 현 빌드의 geometry/consumer evidence로만 retained한다. 새 Storybook rendering language에 대한 **style-fit review가 끝나기 전에는 current visual asset으로 승격하지 않는다**.
- `OM-IMG-023`은 historical visual reference로 보존하되 current direction 또는 product asset으로 사용하지 않는다.

## 6. Planning board

`docs/images/planning/generated/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v6_OPEN_BATTLEFIELD_NO_BARRICADE.png`은 이 방향의 AI 이해·기획 검토 보드이며, 2026-08-29 사용자가 planning direction으로 확정했다. v1은 세 개의 Ward 본진과 병렬 행을 보여 `SUPERSEDED__PARALLEL_COMPOSITION_REJECTED`, v2는 전진기지·접전지 state anchor가 부족해 `SUPERSEDED__OPERATIONAL_MARKERS_INCOMPLETE`, v3는 Ward 본진만 root로 그리고 하단 storyboard를 넣어 `SUPERSEDED__VEIL_ROOT_AND_MAP_ONLY_SCOPE_CORRECTED`, v4는 본진·전진기지의 정확한 패드/탑 수와 전장 밀도가 부족해 `SUPERSEDED__BASE_FORWARD_NODE_COUNTS_AND_BATTLEFIELD_LAYOUT_REQUIRED`, v5는 울타리/고정 바리케이드가 열린 전장 의도를 가려 `SUPERSEDED__OPEN_TERRAIN_NO_FENCE_NO_BARRICADE_REQUIRED`다. v6 lock의 상세 owner는 `docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_V6_VISUAL_DIRECTION_LOCK_2026-08-29.md`다.

```text
PROJECT_CORE_SCENE_VISUAL_BOARD = GENERATED_EXPLORATION
!= PROJECT_ASSET_APPROVED
!= RUNTIME_ASSET
!= GODOT_APPLIED
!= HUMAN_USABILITY_OR_PLAYER_EXPERIENCE_PASS
```

## 7. Phase 2 entry criteria

1. 사용자 review는 2026-08-29에 완료됐으며 v6 planning lock이 current다.
2. Phase 2 readiness review에서 target resolution의 **Ward/Veil 각각의 공유 본진·세 branch·양측 전진기지·세 접전지** 정보 우선순위를 별도 UI spec으로 고정한다. 3×3 roulette과 compact lower deck의 UI spec은 이 map-only board와 별도로 유지한다.
3. Phase 2에서 원본 runtime asset의 provenance/rights 기록을 만든다.
4. 새 Godot Scene/Resource/code 변경은 별도 Issue, RED test, implementation packet, provenance review 뒤에만 시작한다.

## 8. Incident / solution / lesson

**Incident:** 첫 planning board가 세 개의 Ward 본진과 병렬 행을 그려, 사용자가 요구한 "하나의 본진에서 세 갈래로 뻗는 전선"을 전진기지 세 개처럼 오해했다.

**Historical solution (superseded):** 당시에는 topology를 `ONE_WARD_CITADEL_ROOT__THREE_DIVERGING_FRONT_ROUTES`로 명시하고 v2 branching board로 보정했다. 이는 Ward 쪽 기점을 하나로 바로잡은 중간 교정이다. 이후 Veil도 단일 본진·map-only board를 확정했고, 본진 생산 건물을 제거하며 양측 본진의 패드 4개·고정탑 2개와 전진기지의 패드 2개·고정탑 1개를 유지했다. 이후 울타리/닫힌 거점과 고정 전진 바리케이드는 제거되어 current owner는 `ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT`, 열린 지형 grammar, v6 board다. 기존 backdrop은 current-build-only legacy asset, 기존 unit masters는 geometry/consumer evidence retained + style-fit review required로 유지한다. planning board는 계속 별도 `GENERATED_EXPLORATION`으로만 보관한다.

**Lesson:** 전역 visual direction 변경 시에는 rendering/style뿐 아니라 **지도 topology(공통 기점·분기·종점)**를 문장과 보드에서 모두 독립적으로 검증해야 한다.

**Follow-up correction:** topology가 맞아도 route node가 전술적 의미를 보장하지는 않는다. 사용자가 확인한 전진기지와 접전지를 각 branch의 별도 visual state anchor로 배치하고, 이 보드를 runtime asset으로 오인하지 않는 경계를 유지한다.

**Map-only correction:** 보드 하단의 roulette/storyboard는 현재 UI 의미를 정확히 설명하지 못해 제거했다. 이는 roulette system이나 lower control deck의 제거가 아니라, 전략 지도를 독립적으로 검증하기 위한 board scope 축소다. Veil 측도 Ward와 같은 단일 본진·세 branch 구조로 보정했다.

**Base promotion:** `NO_BASE_PROMOTION` — 현재 finding은 Omenward의 세 전선·룰렛·P0 asset lineage에 특화되어 있으며, 두 번째 프로젝트의 재사용 evidence가 없다.

## 9. Adversarial verification

| Failure assumption | Result | Evidence / correction |
|---|---|---|
| AI가 핵심 재미를 기능 목록으로만 이해 | PASS | Board와 screen anchors가 forecast → design → result → irreversible commit → review 인과를 보인다. |
| Player Promise 연결이 끊김 | PASS | Flow anchors에 player need·required information·feedback을 기록했다. |
| 기존 승인 Decision을 무시 | PASS | 2026-08-25의 three-front / deck / silhouette 책임과 2026-08-28 roulette inspection을 retained로 명시했다. |
| 후보/보드를 runtime asset으로 오인 | PASS | spec·board·validator가 `!= RUNTIME_ASSET`을 강제한다. |
| 이미지가 미승인 시스템을 발명 | PASS | Board는 existing 3×3·commit·review·three-front language만 상징적으로 사용한다. |
| style drift 또는 타 프로젝트 혼입 | PASS | ivory/ink/watercolor, navy/gold Ward, restrained violet Veil, wide orthographic map을 layer anchor로 고정했다. |
| reference 권리 또는 직접 복제 | PASS | 두 user reference는 `REFERENCE_ONLY__RIGHTS_UNVERIFIED`; project asset promotion 금지다. |
| target resolution / human usability를 원화만으로 승인 | NOT_RUN | target-resolution UI readability와 human/player evidence는 Phase 2 이후 별도 검증한다. |
| 기존 asset이 새 그림체에 맞는다고 오인 | CORRECTED | backdrop은 legacy, P0 unit master는 style-fit review required로 변경했다. |
| 세 전선을 병렬 전진기지 세 개로 오해 | CORRECTED | v1 병렬 보드를 supersede하고 단일 Ward 본진에서 세 route가 갈라지는 v2를 current planning board로 기록했다. |
| 전진기지·접전지가 일반 route node처럼 보임 | CORRECTED | v3는 branch마다 Ward outpost와 contested contact node를 구별해 배치했다. |
| Veil 측이 세 독립 endpoint처럼 보이거나 하단 UI가 잘못된 시스템을 암시 | CORRECTED | v4는 단일 Veil Citadel root와 map-only composition을 고정하고, roulette은 retained-but-not-visualized로 분리했다. |
| 본진에 생산 건물이 남거나 패드/탑 수가 불명확 | CORRECTED_AS_PLANNING_BOARD | v6는 양 본진 4 empty pads·2 fixed towers, 각 전진기지 2 empty pads·1 tower를 열린 지형에 배치하며, fence와 fixed barricade를 제거했다. target resolution/human readability는 여전히 NOT_RUN이다. |
