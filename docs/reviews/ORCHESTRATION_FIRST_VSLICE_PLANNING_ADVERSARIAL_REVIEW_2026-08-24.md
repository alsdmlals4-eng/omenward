# OMENWARD · Orchestration-first Vertical Slice Planning Review

```yaml
review_date: 2026-08-24
scope: APPROVED_IMPLEMENTATION_ARCHITECTURE_PLUS_TDD_PLAN
base_commit: fb11c50d594c03d49f4d675e01340148f889cdbc
product_code_mutation: NONE
scene_resource_mutation: NONE
runtime_execution: NOT_RUN
human_validation: NOT_RUN
minimum_full_loops: 5
status: CLEAN_REVIEW_EXIT
```

이 문서는 `OMW-PLAN-20260824-ORCHESTRATION-FIRST-VSLICE-01`과 `docs/superpowers/plans/2026-08-24-omenward-orchestration-first-vertical-slice.md`를 대상으로 하는 planning-only 적대 검토 기록이다. 실제 제품 구현 PASS를 주장하지 않는다.

## Loop 1 · Canon / phase semantics

공격 질문:

- `PREPARE → COMMIT → BATTLE → REVIEW`가 current Text UX/Run Command owner와 일치하는가?
- PREPARE/COMMIT/REVIEW에서 battle/wave/economy active time이 흐르지 않는가?
- 세 릴을 세 전선과 1:1로 연결하는 설계가 숨어 있지 않은가?
- Debug StageHud를 final player UI로 승격하거나 삭제하지 않는가?

판정:

```text
PASS
```

근거:

- phase owner를 별도 `RunCommandState`로 제한했다.
- BATTLE만 active time을 허용하는 gate를 TDD acceptance로 고정했다.
- reel↔lane 1:1 mapping은 Global Constraints에서 명시적으로 금지했다.
- 기존 StageHud는 technical/debug surface로 보존한다.

Blocking finding: 0.

## Loop 2 · Transaction integrity

공격 질문:

- Spin 비용이 begin/finalize 사이에서 두 번 차감될 수 있는가?
- preview가 move resource나 live reel을 변경할 수 있는가?
- COMMIT 실패가 food/storage/battle/log 일부만 변경할 수 있는가?
- legacy immediate deployment API가 새 player surface에 다시 연결될 수 있는가?

판정:

```text
PASS_WITH_EXPLICIT_TEST_GATES
```

보호:

- `try_open_paid_spin()`과 `finalize_physical_spin()` 책임을 분리하고 double-charge Red/Green을 요구한다.
- preview는 duplicate state만 사용하고 move resource를 소비하지 않는다.
- batch preflight failure에서 observable delta 0을 검증한다.
- 새 Run Command Screen은 staged orchestration API만 호출하며 legacy immediate deploy path는 player surface에서 금지한다.

Blocking finding: 0.

## Loop 3 · Physical roulette determinism / identity

공격 질문:

- 3×3만 조작하고 실제 reel state를 버리는 가짜 구현인가?
- horizontal move가 token ID/source/reward payload를 함께 이동시키는가?
- executed horizontal move가 다음 live state에 남는가?
- snapshot이 live building/reel 변화에 오염되는가?
- random stop이 shared mutable RNG 때문에 replay에서 흔들리는가?

판정:

```text
PASS
```

보호:

- TokenInstance → ReelState ×3 → RunState → immutable Snapshot → SpinSession 경계를 사용한다.
- horizontal move는 선택 행의 실제 세 reel slot을 원형 교환한다.
- confirm 시 working run을 live run에 반영하도록 plan에 고정했다.
- snapshot copy-out/deep-copy tests가 있다.
- reel별 fixed salt RNG stream을 사용한다.

Blocking finding: 0.

## Loop 4 · UI authority / information density

공격 질문:

- UI가 probability/combat/eligibility를 다시 계산하는가?
- 여러 work surface와 CTA가 동시에 열리는가?
- raw debug ID/weight가 player surface에 누출되는가?
- Lower Deck가 battlefield보다 주의를 더 차지하는가?

판정:

```text
PASS
```

보호:

- `RunCommandViewModel`은 projection만 담당하고 StageRun public orchestration surface를 소비한다.
- one active work surface와 one primary CTA를 GUT contract로 고정한다.
- raw source/unit/target IDs 및 token weights 금지를 snapshot test로 확인한다.
- 960×540/1280×720/1920×1080 runtime evidence와 full-three-lane visibility를 실행 Gate로 남겼다.

Blocking finding: 0.

## Loop 5 · Scope / rollback / evidence ceiling

공격 질문:

- first slice가 MapRun 전체 rewrite, final balance, full content migration으로 팽창하는가?
- 현재 Economy drift를 새 숫자 선택으로 조용히 덮는가?
- HiGodot single-authority를 GitHub direct code write로 우회할 수 있는가?
- runtime/human evidence 없이 구현 완료를 주장할 수 있는가?
- rollback 시 기존 prototype path를 잃는가?

판정:

```text
PASS
```

보호:

- MapRun rewrite/final numerics/전체 Tier/Merchant 상세/새 generic framework를 exclusion으로 고정했다.
- `ECONOMY_BASELINE_DRIFT = OPEN_RECONCILIATION`을 유지한다.
- persistent `.gd/.tscn` authoring은 HiGodot-only다.
- GUT non-zero, import, deterministic replay, Hera source-delta, actual runtime evidence를 completion gate로 요구한다.
- 기존 services와 StageHud를 삭제하지 않아 기능 단위 revert가 가능하다.

Blocking finding: 0.

## Final planning review result

```text
FULL_LOOP_COUNT = 5
NEW_BLOCKING_FINDINGS = 0
P0 = 0
P1 = 0
ARCHITECTURE_SPEC_COVERAGE = PASS
TDD_PLAN_COVERAGE = PASS
PLACEHOLDER_SCAN = PASS
TYPE_AND_INTERFACE_CONSISTENCY = PASS
PRODUCT_CODE_EXECUTION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_VALIDATION = NOT_RUN
PLANNING_REVIEW = CLEAN_REVIEW_EXIT
```

현재 clean exit는 **구현 계획의 품질 Gate**다. 제품 구현·runtime·player experience PASS가 아니다.
