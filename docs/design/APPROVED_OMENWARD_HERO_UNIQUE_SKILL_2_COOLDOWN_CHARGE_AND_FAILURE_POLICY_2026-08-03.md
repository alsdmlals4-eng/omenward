# OMENWARD 해금 영웅 고유 2스킬 cooldown·charge·실패 정책 승인안

```yaml
decision_id: OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-COOLDOWN-CHARGE-AND-FAILURE-POLICY-V1
approved_at: 2026-08-03 07:47 KST
approval: USER_APPROVED_RECOMMENDATION
status: USER_APPROVED / ACTIVE_PLANNING_BRANCH / NOT_IMPLEMENTED
scope: UNIQUE_SKILL_2_COMMON_TIMER_CHARGE_AND_FAILURE_POLICY
parent_decision: OMW-DEC-20260803-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1
activation_lineage: OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1
benchmark_policy: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
product_code_authority: NONE
exact_seconds: PENDING
simulation: NOT_RUN
runtime_validation: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

초기 다섯 해금 영웅의 고유 2스킬은 다음 공통 구조를 사용한다.

```text
단일 cooldown
+ READY 1회 저장
+ charge 누적 없음
+ 새 전장 배치 뒤 INITIAL_WARMUP
+ 병종별 유효 조건
+ 결정론적 대상 선택
```

```text
INITIAL_WARMUP
→ READY_WAITING_FOR_VALID_CONDITION
→ CAST_PRECHECK
→ CAST_COMMIT
→ RESOLUTION_OR_ACTIVE_EFFECT
→ COOLDOWN
→ READY_WAITING_FOR_VALID_CONDITION
```

정확 warmup·cooldown 초, 스킬별 피해·지속시간·범위는 simulation 전까지 고정하지 않는다.

## 2. 공통 불변식

```text
MAX_STORED_READY_COUNT = 1
MAX_CHARGE_COUNT = 1
CHARGE_ACCUMULATION = FALSE
MANA_OR_ENERGY_RESOURCE = FALSE
STAGE_PER_USE_LIMIT = FALSE
MANUAL_CAST = FALSE
MANUAL_HOLD = FALSE
MANUAL_TARGET = FALSE
```

- cooldown이 끝나면 스킬은 `READY_WAITING_FOR_VALID_CONDITION`이 된다.
- 유효 조건이 없으면 READY 상태를 계속 보존한다.
- READY 상태에서 추가 시간이 지나도 두 번째 사용권을 비축하지 않는다.
- 영웅별 별도 마나·분노·에너지 자원을 만들지 않는다.
- 각 스킬은 같은 상태 머신을 쓰되 cooldown 값은 개별 데이터로 둔다.

## 3. INITIAL_WARMUP

새로운 영웅 인스턴스가 전장에 합법적으로 배치되면 첫 사용 전에 초기 준비시간을 거친다.

```text
새 전장 배치
→ INITIAL_WARMUP
→ READY
```

목적:

- 배치 즉시 자동 폭발로 전선 판단이 사라지는 것을 막는다.
- 영웅 투입과 고유 스킬 사건 사이에 읽을 수 있는 예고 시간을 만든다.
- 스킬 상태 UI와 전장 VFX가 준비될 시간을 준다.

경계:

- save/load·Retry로 warmup을 초기화하거나 단축할 수 없다.
- 동일 인스턴스의 저장 복원은 남은 warmup을 그대로 복원한다.
- 정확 warmup 비율·초는 후속 simulation 항목이다.
- Stage·정비시간 경계에서 timer를 pause·resume·carry하는 정확 규칙은 다음 Decision에서 확정한다.

## 4. READY와 유효 조건

```text
READY
+ valid trigger
+ valid target set
→ CAST_PRECHECK
```

- READY 상태 자체는 cooldown을 소비하지 않는다.
- 유효 조건·대상·priority·tie-break를 모두 만족해야 시도한다.
- 같은 저장 상태와 같은 입력 순서에서는 같은 대상과 시점을 선택한다.
- 조건이 한 프레임만 충족됐다가 사라지는 경우를 막기 위한 정확 안정화 창은 스킬별 trigger Decision에서 정한다.

## 5. CAST_PRECHECK 실패 정책

`CAST_COMMIT` 전 조건이나 대상이 무효화되면 사용권을 잃지 않는다.

```text
CAST_PRECHECK
+ trigger invalid OR target invalid
→ READY_WAITING_FOR_VALID_CONDITION
→ cooldown consumption = 0
```

- cooldown을 시작하지 않는다.
- 자동으로 다른 임의 대상에게 즉시 바꾸지 않는다.
- 다음 deterministic 평가 주기에 다시 검사한다.
- save/load·Retry로 다른 대상을 재굴림할 수 없다.

## 6. CAST_COMMIT 이후 정책

`CAST_COMMIT`은 되돌릴 수 없는 전투 사건 예약점이다.

### 6.1 단발 해결형

다음 능력은 commit된 뒤 시전자 상태가 바뀌어도 한 번 해결한다.

- `천공 소거`: commit된 표적 snapshot에 일제사격 판정을 해결한다.
- `메테오`: commit된 지점에 예고 후 메테오를 낙하시킨다.

```text
CAST_COMMIT
→ event payload persisted
→ resolve once
```

메테오의 적은 commit 뒤 이동해 피해 범위를 벗어날 수 있지만, 시전자 사망만으로 예약된 메테오가 취소되지는 않는다.

### 6.2 시전자 귀속 지속형

다음 능력은 시전자에게 귀속된 지속 효과다.

- `불퇴의 성벽`.
- `생명의 서약`.
- `그림자 분신`.

시전자가 사망·완전 제거되면 남은 효과를 종료한다.

```text
OWNER_REMOVED
→ owner-bound sustained effect ends
```

별도 독립 유닛·영구 오브젝트·사후 잔존 버프로 전환하지 않는다.

## 7. cooldown 시작점

cooldown은 cast 시작 시점이 아니라 능력의 전투 가치가 끝나는 시점부터 시작한다.

```text
불퇴의 성벽: 지속시간 또는 흡수 예산 종료 후
천공 소거: 일제사격 판정 완료 후
생명의 서약: 체력 하한 지속시간 종료 후
메테오: 낙하·폭발 판정 완료 후
그림자 분신: 분신 지속시간 또는 조기 종료 후
```

```text
COOLDOWN_DURING_ACTIVE_EFFECT = FALSE
```

긴 지속효과가 유지되는 동안 cooldown이 함께 흘러 사실상 상시 유지되는 문제를 차단한다.

## 8. 저장·결정론 계약

저장해야 하는 최소 상태:

- 상태 enum: `INITIAL_WARMUP | READY | CAST_PRECHECK | COMMITTED | ACTIVE | COOLDOWN`.
- warmup 남은 시간.
- cooldown 남은 시간.
- 선택한 전선·대상 stable ID 또는 target snapshot.
- commit된 메테오 위치·낙하 남은 시간.
- 방벽 남은 지속시간·흡수 예산.
- 생명의 서약 대상별 유효 체력 하한·남은 시간.
- 분신 owner link·남은 시간·복제 대상.
- 일제사격 commit snapshot.

```text
동일 저장 상태 + 동일 입력 순서 = 동일 결과
```

- Retry로 trigger·target·cooldown을 재굴림하지 않는다.
- save/load로 READY charge를 복제하지 않는다.
- commit payload 누락으로 스킬이 사라지거나 중복 해결되지 않게 한다.

## 9. UX 계약

플레이어가 확인할 수 있어야 하는 상태:

- `INITIAL_WARMUP`과 남은 준비시간.
- `READY` 여부.
- READY지만 유효 조건이 없어 대기 중인 이유.
- `CAST_COMMIT` 예고.
- 효과 남은 지속시간 또는 예산.
- cooldown 남은 시간.

READY와 charge를 혼동시키는 다중 점·스택 UI는 사용하지 않는다.

## 10. 벤치마크·현업 비교 결론

비교한 구조:

1. 마나·에너지형 자동 발동.
2. 고정 cooldown형.
3. 다중 charge형.
4. Stage당 1회형.

OMENWARD 권장안은 고정 cooldown형이다.

- 마나형은 공격속도·피격·아이템·역할 행동과 발동 빈도가 결합돼 밸런스 축이 늘어난다.
- 다중 charge형은 순간 연속 발동과 저장/UI/serialization 복잡도를 높인다.
- Stage당 1회형은 Stage 길이에 따라 가치 편차가 커진다.
- 단일 cooldown과 READY 1회는 자동전투에서 가장 설명 가능하고 공통 resolver·save/load·simulation 비용이 낮다.

공식 상용 사례는 구조의 가독성·발동 자원 복잡도 비교에만 사용하며 exact 초·수치 권위가 아니다.

## 11. 적대적 검토

| Audit ID | 공격 | 대응 |
|---|---|---|
| `OMW-AUD-173` | warmup이 너무 짧으면 배치 즉시 폭발, 너무 길면 해금 보상이 죽는다 | 정확 시간은 simulation과 human test 후 확정 |
| `OMW-AUD-174` | cast부터 cooldown이 흘러 지속형 능력이 사실상 상시 유지된다 | 효과 종료·해결 뒤 cooldown 시작 |
| `OMW-AUD-175` | 유효 조건이 없는데 cooldown을 소비한다 | READY 1회 보존 |
| `OMW-AUD-176` | charge 누적으로 영웅 한 명이 연속 발동해 전역 슬롯을 독점한다 | charge accumulation 금지 |
| `OMW-AUD-177` | save/load·Retry·Stage 전환으로 warmup/cooldown이 초기화된다 | timer와 commit payload 저장; 경계 규칙 후속 확정 |
| `OMW-AUD-178` | cast 직전 대상 소멸로 사용권을 잃는다 | precommit 실패는 READY 복귀·cooldown 0 |
| `OMW-AUD-179` | commit 뒤 시전자 사망 시 스킬 처리 기준이 모호하다 | 단발 해결형은 1회 해결, owner-bound 지속형은 종료 |
| `OMW-AUD-180` | READY와 cooldown 이유가 보이지 않아 자동전투가 불공정하게 느껴진다 | 상태·대기 이유·남은 시간 UX 필수 |
| `OMW-AUD-181` | Stage·정비시간 timer 진행이 미확정이다 | 다음 Decision에서 pause/resume/carry 규칙 확정 |

## 12. 금지

- mana·energy·rage 등 신규 영웅 전용 자원.
- 2회 이상 charge.
- READY 다중 비축.
- 유효 조건 없는 자동 소모.
- precommit 무효화 후 cooldown 소비.
- save/load·Retry 재굴림.
- active effect 중 cooldown 진행.
- 모든 스킬에 동일한 exact cooldown 강제.
- 스킬별 별도 상태 머신·별도 AI 아키텍처.

## 13. 구현·검증 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_APPROVED = DOCUMENTED_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
COMMON_STATE_MACHINE = APPROVED
SINGLE_READY_STORAGE = APPROVED
CHARGE_ACCUMULATION = FORBIDDEN
INITIAL_WARMUP = APPROVED
EXACT_WARMUP_SECONDS = PENDING
EXACT_PER_SKILL_COOLDOWN_SECONDS = PENDING
STAGE_AND_MAINTENANCE_TIMER_POLICY = PENDING
EXACT_TRIGGER_THRESHOLDS = PENDING
ASSETS = NOT_CREATED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 14. 다음 Gate

```text
OMW-DEC-20260803-GAMEPLAY-HERO-UNIQUE-SKILL-2-TIMER-PERSISTENCE-AND-STAGE-BOUNDARY-POLICY-V1
```

다음 질문은 warmup·READY·active effect·cooldown을 Stage 종료, 정비시간, Act 전환, save/load, 영웅 사망에서 어떻게 pause·resume·terminate할지 결정한다.
