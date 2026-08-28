# 본진·전진기지 전장 건설 배치 · 5회 적대적 검토

```yaml
review_id: OMW-REV-20260828-BASE-FORWARD-BATTLEFIELD-LAYOUT-01
reviewed_at: 2026-08-28 KST
decision: OMW-PLAN-20260828-BASE-FORWARD-BATTLEFIELD-CONSTRUCTION-LAYOUT-01
scope: THREE_FRONT_STRATEGIC_MAP / BASE_FORWARD_CONSTRUCTION_CAPACITY / STAGE1_FTUE / VISUAL_BOARD / IMPLEMENTATION_FEASIBILITY
result: PASS_5_OF_5__PLANNING_SCOPE_ONLY
product_code_authority: NONE
runtime: NOT_RUN
human_usability: NOT_RUN
player_experience: NOT_RUN
visual_lock: USER_CONFIRM_PENDING
```

## 검토 기준과 증거

- 현행 정본: `docs/design/APPROVED_OMENWARD_BASE_FORWARD_BATTLEFIELD_CONSTRUCTION_LAYOUT_2026-08-28.md`.
- 실제 구현 대조: `scripts/buildings/building_service.gd`, `scripts/battle/outpost_state.gd`, `scripts/battle/base_state.gd`, `scripts/battle/battle_simulator.gd`, `tests/headless/economy_roulette_test.gd`, `tests/headless/c2_battle_objective_test.gd`.
- 생성 보드: `docs/images/planning/generated/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v5_BASE_FORWARD_NODE_LAYOUT.png` (SHA-256 `FAC354B73A7D287327566FD0DCB115C26CE634CCBB6ECBA22820FB847BF1E8A1`).
- 외부 구조 대조: [Commander Quest](https://commanderquest.itch.io/commanderquest), [Thronefall](https://store.steampowered.com/app/2239150/Thronefall/), [Cataclismo](https://store.steampowered.com/app/1422440/Cataclismo/), [Godot Custom GUI Controls](https://docs.godotengine.org/en/stable/tutorials/ui/custom_gui_controls.html), [Godot Control](https://docs.godotengine.org/en/stable/classes/class_control.html) (2026-08-28 KST fresh-read).

## 5회 루프 결과

| Loop | 실패 가정 | 발견한 문제 | 교정 / 판정 |
|---|---|---|---|
| 1 | 고정 방어가 병력 커밋·징조륜 설계를 대신해 핵심 재미가 ‘시설 구경’으로 바뀐다. | 탑/바리케이드의 점령 기여와 단독 처리 금지가 없으면 전진기지 확보가 자동화될 수 있었다. | `FIXED_DEFENSE_CAPTURE_CONTRIBUTION = 0`, `FIXED_DEFENSE_SOLO_CLEAR = FORBIDDEN`을 계약에 명시했다. 방어물은 시간·보조 화력만 주고, 비가역 전선 커밋의 원인을 대체하지 않는다. **PASS (계획 규칙)**. |
| 2 | 지도에 세 개의 병렬 길 또는 본진 세 개처럼 보이는 구조가 다시 들어가며, 요청한 정확한 수량도 이미지에서 틀린다. | 초기 생성 탐색안은 본진에서의 실제 분기와 노드 수를 충분히 증명하지 못했다. | 초기 탐색안은 정본·runtime asset에서 제외했다. v5는 양 진영의 한 root에서 상·중·하 세 branch가 갈라지고, root당 패드 4/탑 2, 전진기지당 패드 2/바리케이드 1/탑 1만 보이도록 재생성·hash readback 했다. target-resolution 가독성은 **NOT_RUN**이다. |
| 3 | ‘본진 건물 제거’를 기존 시작 자원·병력 한도·룰렛 접근까지 삭제하는 것으로 오해하여 Stage 1이 붕괴한다. | 과거 Stage 1은 병영·농장 외형 설명을 전제했다. | 지도 표면의 사전 구축 생산 건물만 supersede하고, MapRun 시작 baseline은 유지한다고 분리했다. Stage 1은 잠긴 패드와 고정 방어를 설명한 뒤 첫 룰렛/커밋으로 진입하며, 최초 의미 있는 건설은 Stage 2다. **PASS (정본 충돌 교정)**. |
| 4 | 계획 문서가 실제로 없는 State·consumer를 이미 구현된 것으로 올려 부정확한 완료 주장을 한다. | forward node 배열 등록은 존재하지만 home node·고정탑·고정바리케이드·전략 지도 consumer는 현재 code에 없다. | 이 배치를 `CONFIRMED__PLANNING_ONLY__NOT_IMPLEMENTED`로 유지했다. Phase 2는 별도 Issue, RED 테스트, State/Resource 계약, target-resolution GUI 검증 전에는 열리지 않는다. **PASS (구현 경계 명시)**. |
| 5 | 과거 candidate/Notion/handoff를 현행 정본으로 혼동하거나, 생성 보드를 runtime asset·사람 검증 PASS로 착각한다. | v4 candidate와 퇴역한 Notion 흐름이 current owner처럼 남을 위험이 있었다. | v4는 `SUPERSEDED`, 새 restart handoff가 현행 owner를 가리키며 Notion은 historical/discovery-only로 표기했다. 보드는 `GENERATED_EXPLORATION__USER_CONFIRM_PENDING`, 권리는 planning reference only, runtime/human/player evidence는 모두 **NOT_RUN**이다. **PASS (정본·증거 경계)**. |

## 사용자 실패 가정 대조

| 실패 가정 | 결과 |
|---|---|
| 기능 목록만 나열하고 Player Promise → 행동 → 선택 → 결과가 끊긴다 | 고정 방어는 시간만 만들고, 관측·룰렛·비가역 커밋·점령 unlock의 인과를 계약 본문에 기록했다. |
| 승인된 Decision 대신 새 시스템을 발명한다 | 노드, 고정 방어, 세 전선 topology만 사용자 승인 범위에서 정리했다. 자유형 성벽·추가 건물·추가 카드 시스템은 만들지 않았다. |
| 비교안이 허수이거나 카메라/정보량이 달라 공정 비교가 안 된다 | 이번에는 후보 간 비교가 아니라 확정된 구조를 정확히 보이는 단일 planning board만 생성했다. 이전 탐색안은 후보도 asset도 아니다. |
| 이미지가 기획에 없는 버튼·UI·상태를 발명한다 | 하단 룰렛/UI/의사 텍스트를 제거하고 지도만 남겼다. 정확한 상태는 구조화된 Markdown 계약이 소유한다. |
| 모든 지역을 동일하게 만들어 전장성이 사라진다 | 공통 topology는 고정하되, 각 접전지의 엄폐물·지형·Veil 밀도만 제한적으로 변주한다. |
| target resolution/UI 합성 없이 승인한다 | 보드는 목표 해상도 GUI 검증이 아니다. 이 항목은 Phase 2 human/usability gate로 남겼다. |
| reference 또는 생성물을 제품 자산으로 오인한다 | 외부 사례는 구조 benchmark이고, ImageGen 산출물은 planning reference다. runtime export/provenance/release rights 승격은 수행하지 않았다. |

## 잔여 위험과 다음 검증

```text
RISK_01 = ROOT_FOUR_PAD_READABILITY_AT_TARGET_RESOLUTION
NEXT_VALIDATION = TARGET_RESOLUTION_STRATEGIC_MAP_GUI_TEST

RISK_02 = FIXED_DEFENSE_OVERPOWERS_COMMITMENT
NEXT_VALIDATION = DETERMINISTIC_SIMULATION_WITH_CAPTURE_POWER_AND_SOLO_CLEAR_ASSERTIONS

RISK_03 = STAGE1_LOCKED_NODES_READ_AS_IMMEDIATE_TASKS
NEXT_VALIDATION = HUMAN_FIRST_SESSION_OBSERVATION

RISK_04 = HOME_AND_FORWARD_NODE_STATE_DRIFT
NEXT_VALIDATION = PHASE2_RED_TESTS_BEFORE_GODOT_IMPLEMENTATION
```

## 결론

현행 계획 범위에서는 5개 공격 모두 교정되었거나 명시적인 후속 검증 gate로 격리되었다. 이는 **전장 배치 정본의 PASS**일 뿐 Godot Scene/UI/Resource 구현, 수치 밸런스, target-resolution 가독성, Human usability, Player Experience의 PASS가 아니다.

```text
NO_BASE_PROMOTION = PROJECT_SPECIFIC_THREE_FRONT_ROOT_AND_OCCUPATION_CAPACITY_LAYOUT
NEXT_GATE = USER_CONFIRM_V5_PROJECT_CORE_SCENE_VISUAL_BOARD
```
