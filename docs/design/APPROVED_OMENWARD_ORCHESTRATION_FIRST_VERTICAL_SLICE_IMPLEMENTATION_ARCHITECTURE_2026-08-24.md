# [현행] OMENWARD · Orchestration-first Vertical Slice 구현 아키텍처

```yaml
decision_id: OMW-PLAN-20260824-ORCHESTRATION-FIRST-VSLICE-01
status: APPROVED_CURRENT
approved_at: 2026-08-24
approval: USER_APPROVED_RECOMMENDED_OPTION_B
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
scope: IMPLEMENTATION_ARCHITECTURE_AND_EXECUTION_BOUNDARY
product_code_authorized: false
persistent_godot_authority: HIGODOT_ONLY
gut_role: DETERMINISTIC_GDSCRIPT_TEST_AUTHORITY
hera_role: LIVE_QA_AND_OBSERVABILITY_ONLY
current_runtime_evidence: NOT_RUN
current_human_evidence: NOT_RUN
```

## 1. 결정

OMENWARD의 첫 current-v4.8 구현은 **Orchestration-first Vertical Slice**로 진행한다.

새 전체 프레임워크를 재작성하지 않고 현재 `StageRun`·`RouletteService`·`DeploymentService`·`BattleSimulator`·`StageEconomy`를 보존하면서, 승인된 `PREPARE → COMMIT → BATTLE → REVIEW` 상태와 transaction boundary를 그 위에 추가한다.

```text
GameApplication
→ StageRun
   → RunCommandState
      ├─ PREPARE
      ├─ COMMIT
      ├─ BATTLE
      └─ REVIEW
   → RouletteSpinSession
   → PendingDeploymentPlan
   → existing Economy / Buildings / Deployment / Battle
→ RunCommandViewModel
→ player-facing Run Command Screen
```

UI는 상태를 계산하거나 규칙을 소유하지 않는다. Domain/orchestration이 현재 phase, 가능한 행동, block reason, staged plan, 결과를 소유하고 presentation은 읽기와 명령 전달만 담당한다.

## 2. Fresh repository reality

현재 `main`의 실제 구조는 다음과 같다.

### StageRun

`StageRun.start()`는 `clock.is_planning = false`로 시작하고 `advance()`는 phase 구분 없이 WaveDirector, BattleSimulator, Building sync, Economy를 계속 진행한다.

현재 API:

```text
spin_roulette(seed_input)
store_roulette_result(result)
construct_home(building_id)
deploy_next_roulette_reward(lane_id)
deploy_card(card, lane_id)
advance(delta)
```

### RouletteService

현재 룰렛은 다음 경로다.

```text
spend 20 gold
→ weighted 9-cell board 생성
→ 중앙 가로줄 판단
→ 동일 judging symbol의 8-line count
→ reward/gold 즉시 확정
```

현재 `scripts/roulette/`에는 `roulette_service.gd`만 존재한다. 현재 current canon이 요구하는 physical triple-reel state, stopped immutable snapshot, row/column manipulation session은 아직 runtime owner가 없다.

### DeploymentService

현재 `deploy()`는 호출 즉시 food를 예약하고 deployed card를 기록한다. `StageRun.deploy_next_roulette_reward()`는 pending reward 하나를 즉시 실제 전선에 투입한다.

즉 현재 구현은 승인된 다음 계약과 다르다.

```text
보관 병력 선택
→ 전선 선택
→ PENDING 배치안
→ COMMIT 안에서 수정 가능
→ 전체 preflight
→ 원자적 확정
→ 비가역 actual deployment
```

### StageHud

현재 `stage_hud.gd/.tscn`은 Token Ledger, Build comparison, Tactical Overlay, Wave Report, Spin, Build, 즉시 Deploy를 동시에 보이는 technical/debug surface다. 이는 current player-facing North Star가 아니다.

## 3. 3안 비교 결과

| 대안 | 방식 | 장점 | 주요 위험 | 판정 |
|---|---|---|---|---|
| A · UI-first replacement | StageHud를 먼저 North Star 형태로 교체하고 기존 API에 직접 연결 | 보이는 결과가 빠름 | phase/transaction이 없는 상태에서 UI가 규칙을 떠안고 즉시 배치가 유지됨 | REJECT |
| B · Orchestration-first Vertical Slice | domain state와 transaction seam을 먼저 만들고 player UI를 연결 | 기존 검증 기반 최대 재사용, TDD/rollback 용이, UI 규칙 누출 방지 | 화면 변경 전에 domain work 필요 | **ADOPT** |
| C · MapRun full rewrite | StageRun부터 전면 교체 | 장기 구조를 새로 맞출 수 있음 | 현재 구현·historical evidence를 버리고 회귀 범위가 과도함 | REJECT |

권장 B안은 `BEST_LONG_TERM_EFFICIENT_METHOD` 기준에서 변경 면적, 되돌리기 난이도, current evidence 보존, 모듈성, player-facing contract 적합성이 가장 좋다.

## 4. RunCommandState 소유권

새 `RunCommandState`는 **phase transition만** 소유한다.

```text
PREPARE
→ COMMIT
→ BATTLE
→ REVIEW_RESULT
→ REVIEW_MAINTENANCE
→ PREPARE
```

Stage 20은 `REVIEW_FINAL` 이후 MapRun final settlement로 향하며 첫 Vertical Slice에서는 별도 제품 확장을 당겨오지 않는다.

필수 invariants:

```text
PREPARE:
  battle advance = false
  wave advance = false
  economy active-time income = false
  build = allowed by existing rules
  spin/manipulate = allowed by session rules

COMMIT:
  battle advance = false
  wave advance = false
  economy active-time income = false
  pending deployment editing = allowed
  actual deployment = forbidden before final confirm

BATTLE:
  battle/wave/economy active-time = true
  build/spin/commit mutation = closed

REVIEW:
  battle/wave/economy active-time = false
  result readback = allowed
```

`CombatClock`의 기존 planning/combat 분리를 재사용하고 두 번째 시간 authority를 만들지 않는다.

## 5. Roulette physical-state boundary

첫 current implementation은 visible 3×3 배열만 회전시키는 가짜 board-only 구현으로 만들지 않는다.

현재 world/canon을 보존하는 최소 domain:

```text
RouletteTokenInstance
→ RouletteReelState × 3
→ RouletteRunState
→ RouletteSpinSnapshot
→ RouletteSpinSession
```

### RouletteTokenInstance

한 token instance는 최소 다음을 가진다.

```text
instance_id
symbol_id
reward_archetype_id
source_building_id
source_tier_id
kind = NORMAL_X | GOLD | SOURCE_BOUND
```

활성 TokenSource 하나는 세 릴 각각에 source-bound token instance 하나씩 총 3개를 제공한다.

### RouletteReelState

- 원형 token sequence와 cursor를 소유한다.
- cursor normalize/wrap을 순수 domain으로 제공한다.
- 세로 이동은 해당 reel cursor만 변경한다.

### RouletteRunState

- 정확히 3개 reel을 소유한다.
- 세 릴은 세 전선과 1:1 대응하지 않는다.
- source snapshot으로부터 deterministic reel state를 만든다.

### RouletteSpinSnapshot

- 정지 순간의 3×3 row-major projection과 reel cursor를 깊은 복사로 보관한다.
- confirm 전 preview의 기준이 된다.
- live reel state mutation과 섞이지 않는다.

### RouletteSpinSession

```text
READY
→ SPINNING
→ STOPPED_MANIPULATE
→ CONFIRMED
```

- READY에서만 Spin 가능.
- STOPPED에서만 row/column manipulation 가능.
- preview는 비용을 소비하지 않는다.
- 실행된 move는 즉시 확정되며 undo/reset을 제공하지 않는다.
- confirm은 기존 중앙 가로줄/8-line resolver 결과와 reward 생성 규칙을 재사용한다.
- 동일 상태+seed+입력 명령은 동일 결과를 만든다.

기존 `RouletteService.resolve_board_snapshot()`의 중앙 판정·line count·rank/gold/reward semantics는 보존 seam으로 재사용한다. 첫 slice에서 이 resolver를 새 확률 시스템으로 재작성하지 않는다.

## 6. PendingDeploymentPlan과 atomic commit

`PendingDeploymentPlan`은 실제 deployed truth가 아닌 **COMMIT 내부 편집 상태**다.

최소 데이터:

```text
assignment_id
reward_index or stable reward identity
lane_id
```

필수 동작:

```text
assign reward → lane
reassign before confirm
remove assignment before confirm
validate all assignments
commit all or commit none
```

Atomic preflight는 actual mutation 전에 다음을 전부 확인한다.

```text
모든 reward가 아직 storage에 존재
모든 lane_id가 유효
각 reward가 중복 assignment되지 않음
전체 food cost가 현재 남은 capacity 이내
StageRun phase가 COMMIT
```

하나라도 실패하면:

```text
food_used delta = 0
battle spawned unit delta = 0
pending reward delta = 0
manifest deployment log delta = 0
```

성공하면 전체 assignment를 deterministic order로 적용하고, 성공한 reward만 storage에서 제거한 뒤 BATTLE로 전환한다.

기존 `DeploymentService.deploy()`의 단일 실제 배치 동작은 최종 apply primitive로 재사용하되, transaction preflight 없이 반복 호출해 partial commit을 만들지 않는다.

## 7. StageRun orchestration adapter

`StageRun`은 새 domain을 조합하는 orchestration owner가 된다.

추가 surface 예시:

```gdscript
func command_phase() -> StringName
func request_commit_phase() -> bool
func begin_roulette_spin(seed_input: Dictionary) -> Dictionary
func preview_roulette_move(axis: StringName, index: int, direction: int) -> Dictionary
func execute_roulette_move(axis: StringName, index: int, direction: int) -> bool
func confirm_roulette_result() -> RouletteSpinResult
func assign_pending_reward(reward_index: int, lane_id: StringName) -> bool
func clear_pending_assignment(reward_index: int) -> bool
func confirm_deployment_and_start_battle() -> bool
func review_snapshot() -> Dictionary
```

정확한 signature는 구현 계획의 TDD task에서 고정한다. 이름만 다르게 만드는 중복 command API는 만들지 않는다.

`advance(delta)`는 phase에 따라 gated 된다.

```text
PREPARE / COMMIT / REVIEW
→ CombatClock planning time만 진행
→ WaveDirector/Battle/Economy active time은 진행하지 않음

BATTLE
→ CombatClock active combat time
→ 기존 WaveDirector/Battle/Economy path 재사용
```

## 8. Presentation boundary

기존 `StageHud`는 debug/evidence 용도로 삭제하지 않는다.

player-facing 신규 surface는 `RunCommandScreen` 또는 같은 책임의 단일 scene으로 둔다.

```text
TOP HUD
= Stage/Wave + core resources + compact Forecast

BATTLEFIELD
= primary visual mass, full three lanes

LOWER CONTROL DECK
= one active work surface
```

Focus별 surface:

```text
PREPARE / Roulette
  left = move resource
  center = 3×3 + 12 direct arrows
  right = Spin OR Result Confirm

PREPARE / Build
  selected build + current→after + local cost + one CTA

COMMIT
  storage/newly acquired + pending lane plan + irreversible warning + one CTA

BATTLE
  tactical access only; build/spin/commit mutation hidden/disabled

REVIEW
  Forecast → Prepare → Commit → Key Event → Result
```

Player UI에서 raw token weight, source IDs, target IDs, raw cause codes를 상시 노출하지 않는다.

## 9. 첫 Vertical Slice acceptance

첫 slice의 완료는 다음 한 경로가 실제로 연결되는 것으로 제한한다.

```text
PREPARE
→ Spin
→ STOPPED 3×3
→ row/column move 최소 1회
→ Result Confirm
→ reward storage
→ COMMIT pending lane assignment
→ atomic confirm
→ BATTLE
→ 실제 battle result
→ REVIEW snapshot
```

필수 자동 증거:

```text
GUT RED: >0 tests discovered and intended failure
HiGodot persistent authoring only
Godot 4.7.1 import/parse PASS
GUT GREEN: >0 tests discovered
existing headless regression PASS or isolated pre-existing blocker evidence
same seed/input deterministic replay PASS
partial deployment commit = impossible
PREPARE/COMMIT/REVIEW active-time leakage = 0
BATTLE active-time progression = expected
Hera read-only live QA after GREEN
Hera tracked source delta = NONE
```

필수 UI/runtime evidence:

```text
960×540 runtime capture
1280×720 runtime capture
1920×1080 runtime capture
mouse path
keyboard/controller focus path when input fixture is available
three lanes visible with lower deck open
one primary CTA per focus
```

실행하지 못한 device/human/accessibility evidence는 `NOT_RUN`으로 남긴다.

## 10. Economy drift boundary

현재 `ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION`은 별도 planning/balance finding이다.

이번 architecture는:

- 현재 runtime의 금화/식량/Spin cost 숫자를 final product balance로 승격하지 않는다.
- phase gating 때문에 planning time에 income/wave/battle이 흐르지 않는 구조만 구현한다.
- final numeric tuning, expected value, source weight rebalance를 이 first slice에 섞지 않는다.

새 숫자 결정이 필요해지면 implementation scope를 넓히지 말고 별도 Decision gate로 중단한다.

## 11. 제외 범위

첫 slice에서 하지 않는다.

- MapRun 전체 재작성
- Stage 1~20 전체 content conversion
- final economy parameter vector 선택
- final unit functional-value scalar/vector 선택
- 상위 Tier 전체 구현
- Merchant/maintenance 상세 경제
- 새로운 generic ability framework
- Debug StageHud 삭제
- 새 이미지 생성
- 최종 아트/애니메이션 자산 생산
- Android device PASS 주장
- human/player experience PASS 주장

## 12. Rollback

구현은 latest completed `main`에서 독립 branch/worktree로 시작한다.

Rollback 단위:

```text
1. player-facing RunCommand scene 연결 제거
2. StageRun orchestration adapter 제거
3. PendingDeploymentPlan 제거
4. RouletteSpinSession/physical-state domain 제거
5. 기존 StageHud + 기존 immediate prototype path 복구
```

기존 prototype을 첫 커밋부터 삭제하지 않으므로 rollback은 기능 단위 revert로 가능해야 한다.

## 13. 현재 Gate

```text
IMPLEMENTATION_ARCHITECTURE = APPROVED
IMPLEMENTATION_PLAN = REQUIRED_BEFORE_CODE
PRODUCT_CODE_AUTHORIZED = NO
PERSISTENT_GODOT_MUTATION = NOT_STARTED
CURRENT_RUNTIME = NOT_RUN
CURRENT_HUMAN_VALIDATION = NOT_RUN
NEXT = WRITE_TDD_IMPLEMENTATION_PLAN_AND_CREATE_ISOLATED_EXECUTION_WORK_ITEM
```

이 Decision은 구현 방향을 승인한다. 실제 제품 코드/Scene/Resource persistent mutation은 implementation plan handoff와 실행 경로 확정 뒤 시작한다.
