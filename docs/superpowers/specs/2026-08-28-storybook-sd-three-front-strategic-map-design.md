# Omenward Storybook SD · Three-Front Strategic Map Visual Direction

```yaml
decision_id: OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01
issue: 239
status: USER_CONFIRMED_CURRENT
approval_source: "2026-08-28 user: 1번이미지 = 그림체, 2번이미지 = 전장 미니맵·UI; 세 전선이 다 보이게"
scope: VISUAL_DIRECTION_LOCK_AND_PLANNING_BOARD_ONLY
runtime_implementation: NOT_AUTHORIZED_BY_THIS_DECISION
runtime_target_asset: NOT_CREATED
```

## 1. Decision

Run Command의 주 전장 표현은 가까운 전투 배경 일러스트가 아니라, 세 전선이 동시에 보이는 **전략 지도 UI**다. 왼쪽 Ward 수호권 → 중앙 경합 거점 → 오른쪽 Veil 압력권의 공간 인과를 한 화면에서 읽는다.

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
```

### Character / environment / UI / VFX anchors

- **Character:** shield, banner, weapon, silhouette, faction color를 장식보다 먼저 읽는다. 수호군은 navy/ivory/pale steel/restrained gold, Veil은 charcoal/plum-black/dark violet/limited rift glow다.
- **Environment:** 각 전선은 Ward stronghold, 2~3개 원형 route node, 중앙 clash zone, Veil approach 또는 fortress를 가진다. 같은 카메라·축척을 유지하되 지형과 위협 상태만 제한적으로 변주한다.
- **UI:** 종이 패널, 정교한 얇은 테두리, 상징 기반 아이콘, 제한된 금색 강조를 사용한다. UI는 지도 위에 과적되지 않으며 3×3 roulette은 계속 노출된다.
- **VFX:** 아주 작은 별빛, 수호 문장 광택, 균열의 보랏빛 glow만 허용한다. full-screen flash, 과도한 흔들림, 시야를 가리는 보상 연출은 금지한다.

### Keep / Avoid / Do Not Drift

| Keep | Avoid | Do Not Drift |
|---|---|---|
| 세 전선 동시 가독성, 전장-primary, compact lower deck, silhouette-first, 3×3 roulette | 카지노/도박 표현, 가짜 near miss, copied character/UI, 조밀한 개체 단위 미니맵, 장식이 정보보다 앞서는 화면 | player-constructed probability engine, fixed reel-to-lane mapping 금지, 비가역 commit, Ward 대 Veil 양 진영, 아이보리/남색 대 어두운 보랏빛 명도 위계 |

### Allowed variation

지역·시간대·위협 상태에 따라 식생, 물길, 석재, 안개, Veil 균열 밀도는 달라질 수 있다. 다만 세 전선의 좌→우 인과, 종이/수채화/잉크 문법, faction color hierarchy, route node 의미는 유지한다.

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

`docs/images/planning/generated/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v1.png`은 이 방향의 AI 이해·기획 검토 보드다.

```text
PROJECT_CORE_SCENE_VISUAL_BOARD = GENERATED_EXPLORATION
!= PROJECT_ASSET_APPROVED
!= RUNTIME_ASSET
!= GODOT_APPLIED
!= HUMAN_USABILITY_OR_PLAYER_EXPERIENCE_PASS
```

## 7. Phase 2 entry criteria

1. 사용자가 이 Lock Packet과 planning board를 검토한다.
2. target resolution에서 route node·전선 상태·3×3 roulette·commit target의 정보 우선순위를 별도 UI spec으로 확정한다.
3. 원본 runtime asset의 provenance/rights 기록을 만든다.
4. 새 Godot Scene/Resource/code 변경은 별도 Issue, RED test, implementation packet이 승인된 뒤에만 시작한다.

## 8. Incident / solution / lesson

**Incident:** 기존 close-battlefield backdrop와 P0 unit master가 current visual asset처럼 남아 있으면, 사용자가 새로 확정한 동화풍 전략 지도 UI가 이미 구현·승인된 것처럼 오해될 수 있었다.

**Solution:** 새 Direction을 단일 current owner로 기록하고, 기존 backdrop은 current-build-only legacy asset, 기존 unit masters는 geometry/consumer evidence retained + style-fit review required로 재분류했다. planning board는 별도 `GENERATED_EXPLORATION`으로만 보관했다.

**Lesson:** 전역 visual direction 변경 시에는 rendering/style, battlefield framing, asset consumer, runtime evidence, planning visualization을 독립 상태로 기록해야 한다.

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
