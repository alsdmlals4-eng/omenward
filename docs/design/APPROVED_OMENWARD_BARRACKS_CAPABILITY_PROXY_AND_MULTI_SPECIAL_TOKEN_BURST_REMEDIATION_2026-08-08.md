# [승인] OMENWARD 병영 Capability Proxy·복수 특수 TokenSource Burst Remediation

```yaml
updated_at: 2026-08-08
decision_id: OMW-DEC-20260808-PLANNING-BARRACKS-CAPABILITY-PROXY-AND-MULTI-SPECIAL-TOKEN-BURST-REMEDIATION-V1
parent_decision_id: OMW-DEC-20260806-PLANNING-BARRACKS-SMOKE-SWEEP-RESULTS-AND-IDENTIFIABILITY-GATE-V1
status: APPROVED_REMEDIATION_CONTRACT / SMOKE_RERUN_REQUIRED
approval: USER_APPROVED_RECOMMENDED_PATH
approval_count: 5_OF_10_REMEDIATION_CONTRACT
scope: ANALYSIS_AND_SIMULATION_CONTRACT_ONLY
product_code_authority: NONE
```

## 1. 결론

4/10 조건부 실패의 두 원인을 서로 다른 층으로 분리한다.

```text
MODEL_IDENTIFIABILITY_FAIL
= 제품 HP/DPS/방어탑 출력/지휘 오라 계수/전술 출력이 없는 상태에서
  LOW/MID/HIGH 비병영 전투 기여를 하나의 TU scalar로 주입해 승패를 판정한 모델 식별성 실패

SPECIAL_TOKEN_SHARE_BURST_MAX = 0.50 > 0.45
= 비용·생산간격·기능가치 벡터와 무관하게 두 특수 TokenSource가 동시에 활성화될 때 발생하는 물리 source-count 구조 실패
```

이 Decision은 임의의 전투 출력 숫자를 새로 만들지 않는다. 전투 승패형 proxy는 제품 전투 수치가 생길 때까지 balance pass/fail에서 제외하고, 현재 승인된 구조의 가용성만 별도 capability vector로 기록한다.

```text
PLAYER_CAPABILITY_PROXY = STRUCTURAL_CHANNEL_VECTOR
COMBAT_POWER_SCALAR = FORBIDDEN
SUPPORT_TU_NUMERIC_INJECTION = FORBIDDEN
GENERAL_PATH_VALIDITY_RATE = DIAGNOSTIC_NON_IDENTIFIABLE
EACH_SPECIAL_OUTCOME_PATH_VALIDITY_RATE = DIAGNOSTIC_NON_IDENTIFIABLE
```

## 2. 구조 Capability Vector

Stage 1~5에서 다음 네 채널의 **존재·해금 상태만** 기록한다.

```text
DEFENSE_TOWER
COMMAND_AURA
MANA_TACTIC
FRONTLINE_STATE
```

이 vector는 HP·DPS·승률·실제 처리량을 뜻하지 않는다.

| Stage | 방어탑 | 지휘 오라 | 마력·전술 | 기본 전선 상태 |
|---|---|---|---|---|
| 1 | PRESENT | PRESENT | LOCKED_BY_ONBOARDING | PRESENT |
| 2 | PRESENT | PRESENT | LOCKED_BY_ONBOARDING | PRESENT |
| 3 | PRESENT | PRESENT | AVAILABLE_AFTER_RESEARCH | PRESENT |
| 4 | PRESENT | PRESENT | AVAILABLE_AFTER_RESEARCH | PRESENT |
| 5 | PRESENT | PRESENT | AVAILABLE_AFTER_RESEARCH | PRESENT |

근거 경계:

- Stage 1 필수 기초 세트에 방어탑·지휘소·마력탑이 포함된다.
- 마력탑은 Stage 1에 설치하지만 연구 설명·첫 전술은 Stage 3에 노출한다.
- 병종·건물·전술은 각각 압력 대응 경로를 제공하지만 단일 하드 카운터는 금지된다.
- 실제 전투 출력 수치는 아직 `PENDING_SIMULATION` 또는 미승인이다.

따라서 `GENERAL_PATH_VALIDITY_RATE`와 특수병별 전투 유효율을 0.95/0.85 선으로 제품 밸런스 판정하는 것은 현재 단계에서 금지한다. 재실행 결과에는 역사 비교를 위해 raw diagnostic으로 남길 수 있으나 Gate 실패 사유로 사용하지 않는다.

## 3. 복수 특수 TokenSource 구조 수정

현행 V2 확률축은 fractional weight가 아니라 실제 릴의 `TokenInstance` 개수다. 이 원칙을 유지한다.

```text
TOKEN_SOURCE_PROBABILITY_AXIS = PHYSICAL_TOKEN_INSTANCES_PER_REEL
TOKENS_PER_ACTIVE_SOURCE_PER_REEL = 1
FRACTIONAL_TOKEN_WEIGHT_WORKAROUND = FORBIDDEN
```

첫 번째 특수병 병영의 TokenSource는 기존 amendment대로 건설 확정 후 선택된 특수병으로 활성화한다.

두 번째 특수병 병영은 자동생산 기능을 잃지 않지만, **릴 TokenSource는 비특수 active source가 3개 이상일 때만 활성화**한다.

```text
FIRST_SPECIAL_TOKEN_SOURCE = ACTIVE_ON_BUILD_COMMIT
SECOND_SPECIAL_TOKEN_SOURCE = DEFERRED_WHILE_GUARD_FALSE
SECOND_SPECIAL_MIN_NON_SPECIAL_ACTIVE_SOURCES = 3
SECOND_SPECIAL_AUTO_PRODUCTION_WHILE_DEFERRED = ALLOWED_UNCHANGED
TOKEN_GUARD_EVALUATION = CONTINUOUS_AT_TOKEN_STATE_READ
```

두 특수 TokenSource가 실제로 동시에 활성화되는 최소 상태는 다음과 같다.

```text
NON_SPECIAL = 3
SPECIAL = 2
TOTAL = 5
SPECIAL_SHARE = 2 / 5 = 0.40
APPROVED_BURST_MAX = 0.45
```

따라서 물리 토큰 문법을 유지하면서 `0.50` burst를 구조적으로 제거한다. 비특수 source가 줄어 guard가 깨지면 두 번째 특수 TokenSource는 다시 deferred 상태가 되며, 해당 병영의 자동생산은 계속된다.

## 4. 변경하지 않는 것

```text
SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_TOKEN_SOURCE_NONE = SUPERSEDED
AUTO_PRODUCTION_IS_SEPARATE_ACQUISITION_PATH = REQUIRED
GENERAL_AND_SPECIAL_COST_VECTOR = UNCHANGED_FOR_RERUN
PRODUCTION_INTERVAL_VECTOR = UNCHANGED_FOR_RERUN
SPECIAL_FUNCTIONAL_VALUE_VECTOR = UNCHANGED_FOR_RERUN
PHYSICAL_REEL_TOKEN_INSTANCE_GRAMMAR = UNCHANGED
```

구형 `SPECIAL_T1_TOKEN_SOURCE = NONE`으로 되돌리거나 fractional weight를 도입하여 burst를 숨기지 않는다.

## 5. 2,000-seed 재실행 Gate

동일한 9개 상대 파라미터 벡터와 공통 random-number seed 구조를 재사용한다. 재실행에서 전투 성공률형 지표는 diagnostic으로만 보존하고, 물리 릴·경제·상대 비교 지표와 새 TokenSource guard를 검증한다.

```text
SMOKE_RERUN_SEEDS = 2000
COMMON_RANDOM_NUMBERS = TRUE
PARAMETER_VECTORS = 9
BARRACKS_2000_SEED_SMOKE_RERUN = REQUIRED
DECISION_SWEEP_10000 = BLOCKED_UNTIL_RERUN_PASS
CONFIRMATION_SWEEP_50000 = BLOCKED
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED
GODOT_AUTHORING = NOT_AUTHORIZED
```

재실행이 Green이어도 10,000-seed decision sweep를 자동 실행하지 않는다. 결과를 정본·Sheet에 동기화하고 별도 Gate 판정을 거친다.

## 6. 이전 4/10 증거 복구

현재 main Decision Ledger·Sheet는 4/10 conditional fail을 현행 상태로 기록하지만, 책임 원본과 재현 분석 파일이 역사 PR154에만 남아 있었다. 이 Decision의 branch는 **4/10 승인 결과와 재현에 필요한 최소 분석 파일만** current-main lineage로 복구한다.

PR154의 38개 전체 변경이나 과거 라우터 상태를 병합하지 않는다.

## 7. 제품 경계

```text
PRODUCT_CODE = UNCHANGED
SCENE_RESOURCE_DATA = UNCHANGED
GAMEPLAY_DATA = UNCHANGED
LOCAL_GODOT_PROJECT = UNCHANGED
PRODUCT_IMPLEMENTATION = NOT_AUTHORIZED
FORMAL_GUT_EXECUTION = NOT_AUTHORIZED_BY_THIS_DECISION
HERA_LIVE_QA = NOT_AUTHORIZED_BY_THIS_DECISION
```

이 Decision은 분석·시뮬레이션 Gate만 다룬다.
