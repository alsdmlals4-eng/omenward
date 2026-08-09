# [승인] OMENWARD 병영 Role-Output Runtime 구현 패키지

```yaml
updated_at: 2026-08-09
decision_id: OMW-DEC-20260809-PLANNING-BARRACKS-ROLE-OUTPUT-RUNTIME-IMPLEMENTATION-PACKAGE-V1
parent_decision_id: OMW-DEC-20260809-PLANNING-BARRACKS-FUNCTIONAL-VALUE-MEASUREMENT-SCENARIOS-DEFINITION-V1
baseline_main: b77fb4dcf0bead75ab796cb287fa510dd7ec751e
status: PACKAGE_SPEC_APPROVED / EXECUTION_DEFERRED_EXTERNAL_EXECUTOR
scope: PLANNING_AND_IMPLEMENTATION_CONTRACT_ONLY
product_mutation_in_this_gate: NONE
```

## 1. 결론

```text
PACKAGE_MODE = SPEC_ONLY_NO_PRODUCT_MUTATION
GENERIC_ABILITY_SYSTEM = DEFERRED_NOT_REQUIRED
TARGET_PRIORITY_SOURCE = EXISTING_TARGET_PRIORITY_TAGS
ROLE_EVENT_SURFACE = EXTEND_EXISTING_RECORD_EVENT_DRAIN_EVENTS
POC_NUMERICS = PROVISIONAL_POC_INPUT_NOT_FINAL_PRODUCT_AUTHORITY
HIGODOT_AUTHORING = REQUIRED_FOR_PERSISTENT_GODOT_MUTATION
GUT_TEST_AUTHORITY = REQUIRED_FOR_DETERMINISTIC_ACCEPTANCE
HERA_ACCEPTANCE = LIVE_QA_SOURCE_DELTA_NONE
FINAL_FUNCTIONAL_VALUE_INDEX = NOT_SELECTED
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
```

현재 hosted ChatGPT 세션에는 HiGodot persistent authoring executor가 노출되어 있지 않다. 따라서 이 Decision은 실행 명세를 닫지만 `scripts/`, `data/`, `project.godot`을 GitHub API로 우회 수정하지 않는다. 실제 구현은 `DEFERRED_EXTERNAL_EXECUTOR`다.

## 2. Fresh current-runtime evidence

현재 main `b77fb4dc...`에서 확인한 사실:

- `UnitArchetypeProfile`에는 `magic_resistance`, `target_priority_tags`, `attack_profile_id`가 이미 있다.
- `UnitInstance.receive_damage(raw_damage)`는 armor만 적용하며 magic resistance를 소비하지 않는다.
- `LaneState.find_target(attacker)`는 기존 `target_priority_tags`를 소비하지 않는다.
- `BattleSimulator` 일반 교전은 `lane.find_target(unit)` 뒤 단일 대상 damage만 전달한다.
- `BattleSimulator`에는 이미 `_record_event()`와 `drain_events()`가 있으므로 별도 telemetry subsystem을 만들 필요가 없다.
- 현재 Priest/Mage/Flier/Giant resource의 `attack_profile_id`는 각각 archetype ID와 일치한다. 과거/다른 branch에서 관찰된 `special_ranged`/`special_melee` 값을 현행 정본으로 사용하지 않는다.

## 3. 최소 runtime architecture

새 범용 ability framework를 만들지 않는다. vertical-slice 역할 출력에 필요한 최소 변화만 허용한다.

### 3.1 Data contract

기존 필드를 우선 재사용한다.

```text
REUSE role
REUSE magic_resistance
REUSE target_priority_tags
REUSE attack_profile_id
REUSE structure_damage_tags
NEW GENERAL PASSIVE_IDS = NOT_REQUIRED
NEW GENERAL SKILL_IDS = NOT_REQUIRED
NEW TARGETING_PROFILE_ID = NOT_REQUIRED
NEW THREAT_COST = NOT_REQUIRED
```

필요한 새 선언은 구현 RED가 기존 데이터로 표현 불가능함을 증명한 경우에만 추가한다. Flier의 air semantics도 먼저 `role = air`와 현행 archetype identity로 처리하고, 별도 `movement_layer`는 GUT RED가 요구할 때만 추가한다.

### 3.2 Target selection

`LaneState.find_target()`를 파괴하지 않고 deterministic priority consumption을 추가한다.

- `nearest`: 기존 동작 보존.
- `flying`: air 역할 대상 우선.
- `backline`: 같은 lane의 상대 후열을 결정론적으로 우선.
- `cluster`: 주변 적 밀도가 가장 높은 합법 대상을 우선하되 동률은 기존 lane order/unit id로 결정.
- `structure`: unit-target selector의 가짜 unit을 만들지 않는다. 구조물은 기존 objective path가 책임진다.
- `lowest_health_ally`: enemy selector에 섞지 않고 Priest support-target helper에서 처리한다.

`target_priority_tags`가 비어 있거나 매칭이 없으면 기존 nearest 결과로 fallback한다.

### 3.3 Damage channel / resistance

Mage/Priest PoC가 magic damage를 선언하지만 현 runtime damage API에는 channel이 없다. 구현 package는 먼저 GUT RED로 physical/magic mitigation 분리를 요구한다.

권장 최소 계약:

```text
DAMAGE_CHANNEL = PHYSICAL | MAGIC
PHYSICAL -> armor
MAGIC -> magic_resistance
UNKNOWN -> fail closed in test / no silent weighted conversion
```

정확한 수식은 기존 armor mitigation 형태를 동일 resistance scale에 적용하는 `PROVISIONAL_RECOMMENDED_VALUE`로 시작할 수 있으나, 이는 final combat numeric authority가 아니다.

## 4. 역할별 최소 행동 + 출력

PoC 수치는 행동을 재현하기 위한 provisional input이며 functional scalar 선택 근거로 직접 사용하지 않는다.

### Priest — FV-PRIEST-01

행동 형태:
- 같은 lane `lowest_health_ally`를 deterministic 선택.
- 유효한 치유 대상이 있으면 healing action.
- 없으면 같은 lane ally encouragement/buff action.

PoC provisional input:
- heal: max HP 10% + 40
- shared cooldown: 8s
- encouragement: 5s attack-speed +8%

필수 event/output:
- `role_heal`: source, target, raw_heal, effective_heal, overheal
- `role_buff_start`, `role_buff_end`: source, target, buff_id, duration
- collector: `EFFECTIVE_HEALING_HP`, `OVERHEAL_WASTE`, `SUPPORTED_TARGET_SECONDS`, `BUFF_UPTIME`

### Mage — FV-MAGE-01

행동 형태:
- existing `cluster` target priority를 deterministic 소비.
- primary target + bounded same-lane collateral AoE.
- magic channel을 사용.

PoC provisional input:
- explosive orb: center 60, collateral 45, max 5, cooldown 7s

필수 event/output:
- `role_aoe_hit`: source, primary_target, affected_unit_ids, primary_damage, collateral_damage
- collector: `PRIMARY_TARGET_DAMAGE`, `COLLATERAL_AOE_DAMAGE`, `TARGETS_HIT_PER_CAST`
- `CONTROL_TARGET_SECONDS`는 실제 control behavior가 구현되기 전까지 `BLOCKED_RUNTIME_OUTPUT`; fake zero 금지.

### Flier — FV-FLIER-01

행동 형태:
- ground-frontline ordering을 그대로 통과하는 ordinary nearest path가 아니라 same-lane backline pressure path.
- existing air role + `backline` priority를 재사용.
- Assassin bypass state를 복사해 쓰지 않고, Flier own deterministic route로 분리한다.

PoC provisional input:
- dive distance 100, damage 70, cooldown 8s

필수 event/output:
- `role_backline_contact`
- `role_dive`
- collector: `TIME_TO_BACKLINE_CONTACT`, `FRONTLINE_BYPASS_DISTANCE_OR_TIME`, `DIVE_DAMAGE`, `BACKLINE_PRESSURE_SECONDS`
- `AIR_TARGETABILITY_EXPOSURE`는 anti-air targeting contract가 실제 구현될 때만 측정; 그 전에는 `BLOCKED_RUNTIME_OUTPUT`.

### Giant — FV-GIANT-01

행동 형태:
- 기존 siege objective path와 `structure_damage_tags`를 보존.
- unit combat에서 bounded same-lane slam AoE를 추가.
- air target은 slam 대상에서 제외.

PoC provisional input:
- slam max 6
- center 100%, outer 75%
- structure ×1.35, barricade ×1.50은 현행 product data와 충돌 여부를 HiGodot 실행 전에 재대조하며 자동 덮어쓰지 않는다.

필수 event/output:
- `role_slam`: source, affected_unit_ids, damage_by_target
- existing `gate_damage` / `base_damage`를 공성 출력에 재사용
- collector: `SLAM_TARGETS_HIT`, `SLAM_TOTAL_DAMAGE`, `FRONTLINE_SURVIVAL_TIME`, `STRUCTURE_DAMAGE`

## 5. Functional-value collector

새 weighted score를 만들지 않는다. deterministic scenario runner/collector는 existing event queue를 소비해 role vector만 만든다.

```text
FV-COMMON-01
FV-PRIEST-01
FV-MAGE-01
FV-FLIER-01
FV-GIANT-01
```

필수 원칙:
- same input / same geometry / same opponent
- blocked output is `BLOCKED_RUNTIME_OUTPUT`, never numeric zero
- raw event evidence preserved
- no Monte Carlo role-value selection
- no post-hoc weights

## 6. HiGodot Authoring Manifest

실제 실행 시 persistent mutation 허용 후보:

```text
scripts/data/unit_archetype_profile.gd     # only if RED proves a new field is unavoidable
scripts/battle/unit_instance.gd
scripts/battle/lane_state.gd
scripts/battle/battle_simulator.gd
data/units/priest.tres                     # only provisional role-action values actually required
data/units/mage.tres
data/units/flier.tres
data/units/giant.tres
new deterministic role-output collector/harness under scripts/battle/ or tests support
new GUT tests under the adopted test root
```

Default `project.godot` mutation = NONE because Godot AI/GUT/Hera are already enabled on merged main.

## 7. GUT Red -> Green acceptance

RED must exist before HiGodot authoring. Minimum cases:

1. Priest lowest-health ally target is deterministic; effective heal/overheal are distinct.
2. Priest buff is emitted only when no valid heal target and uptime is measurable.
3. Mage cluster selection is deterministic; primary/collateral output separated.
4. physical vs magic channel exercises armor vs magic resistance.
5. Flier reaches backline through its own allowed path and emits first-contact timing.
6. Archer anti-air priority can select Flier when applicable.
7. Giant slam is bounded, deterministic, excludes air, and preserves siege objective output.
8. `BLOCKED_RUNTIME_OUTPUT` is not serialized as numeric zero.
9. event ordering is deterministic for identical seed/input.
10. zero-test discovery is failure, never PASS.

Existing headless regressions also remain green.

## 8. Hera live QA acceptance

After GUT Green + Godot import/parse:

- run each FV scenario through actual project/runtime path available to the QA harness;
- inspect source/target/state/events;
- assert role behavior and observable presence;
- capture diagnostics/screenshot only where they add evidence;
- snapshot tracked source before Hera;
- perform no Hera persistent write;
- snapshot tracked source after Hera;
- require `tracked source delta NONE`.

## 9. Execution boundary

```text
SPEC_STATUS = APPROVED
EXECUTION_STATUS = DEFERRED_EXTERNAL_EXECUTOR
CURRENT_CHATGPT_HIGODOT_EXECUTOR = NOT_AVAILABLE
GITHUB_TEXT_EDIT_AS_AUTHORING_BYPASS = FORBIDDEN
GLOBAL_ENTRY_GATE = BLOCK
BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED = REMAINS_UNTIL_RUNTIME_GREEN
```

다음 실제 실행자는 동일 Decision/패키지를 다시 읽고 current main을 fresh-verify한 뒤 GUT RED → HiGodot authoring → Godot parse/import → GUT Green/regression → Hera live QA/source-delta-none 순서를 수행해야 한다.
