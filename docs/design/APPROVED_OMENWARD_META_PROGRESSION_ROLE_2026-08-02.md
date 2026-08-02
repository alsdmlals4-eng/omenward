# 오멘워드 Profile 영구 성장 역할 승인 계약

```yaml
decision_id: OMW-DEC-20260802-META-PROGRESSION-ROLE-V1
approved_at: 2026-08-02 11:16 KST
approval: USER_APPROVED_RECOMMENDATION_PLUS_B
status: USER_APPROVED_PLAN / EXACT_VALUES_PENDING / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
product_code_authority: NONE
codex: BLOCKED
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

Profile 영구 성장은 **수평 해금과 제한된 편의 성장을 주축**으로 하고, B안의 장점인 성장 체감을 위해 **엄격히 상한이 있는 소규모 영구 전투력**을 보조축으로 포함한다.

```text
PRIMARY = HORIZONTAL_UNLOCKS_AND_LIMITED_CONVENIENCE
SECONDARY = CAPPED_SELECTABLE_READINESS_POWER
FORBIDDEN = UNBOUNDED_PASSIVE_STAT_GRIND
```

플레이어는 반복할수록 자동으로 모든 전투 수치가 누적되는 것이 아니라, 더 많은 전략 선택지를 이해하고 한 가지 제한된 준비 보정을 선택한다. 기본 Profile만으로도 전체 콘텐츠를 완료할 수 있어야 하며 영구 성장은 실패 분석과 런 내 판단을 대체하지 않는다.

## 2. 플레이어 경험 목표

- 실패와 완주 뒤 다음 런에서 시험할 새로운 전략이 생긴다.
- 성장 체감은 분명하지만 반복 노가다가 정답이 되지 않는다.
- 건물·TokenSource·세 물리 릴·세 전선 커밋이 승패의 중심으로 남는다.
- Profile 단계가 달라도 같은 런의 실패 원인을 설명할 수 있다.
- paid Retry와 장기 해금은 의미 있는 선택이지만 진행을 인질로 잡지 않는다.

## 3. 영구 성장 구성

### 3.1 수평 해금 — 주축

수평 해금은 새로운 선택지를 제공하되 기존 선택지의 단순 상위 호환이 되지 않는다.

허용 범위:

- 대체 시작 교리와 시작 구성안.
- 새로운 건물·TokenSource·미션의 sidegrade 분기.
- 새로운 전략용 해금과 도감·세계관 기록.
- 벨루의 추가 분석 기록과 복기 기능.
- 외형·문양·장식.
- 제한된 시작 보관 편의.

불변 조건:

- 해금 전 기본 구성으로 모든 Stage를 완료할 수 있어야 한다.
- 해금 선택지는 장점과 비용 또는 사용 조건을 함께 가진다.
- 특정 해금이 모든 공세·난이도·릴 구조에서 우월하면 sidegrade가 아니라 밸런스 결함으로 판정한다.
- 해금 수가 늘어도 한 런에서 동시에 활성화할 수 있는 시작 선택 수는 제한한다.

### 3.2 제한된 편의 성장

편의 성장은 판단 횟수와 정보 접근을 돕지만 전투 결과를 자동으로 만들지 않는다.

허용 후보:

- 시작 보관 용량의 작은 hard-cap 확장.
- 저장된 시작 구성안·필터·복기 기록.
- 비전투 UI 편의와 선택 이력.

금지:

- 런 안에서 무제한 보관 용량 확장.
- 실패 원인을 숨기는 자동 배치·자동 건설·자동 릴 편집.
- 편의 해금을 가장한 지속 전투 배율.

### 3.3 선택형 준비 보정 — B안 반영

소규모 영구 전투력은 `Readiness Perk` 형태로만 허용한다.

```yaml
ReadinessPerk:
  unlock_source: settled_profile_progress_milestone
  equipped_per_maprun: 1
  rank_model: finite_hard_cap
  stacking: forbidden
  duration: opening_or_act1_limited
  exact_values: pending_simulation
```

권장 후보군:

1. **재정 준비** — 시작 골드 또는 1회성 준비 자원 보정.
2. **군수 준비** — 시작 식량 한도 또는 배치 여유 보정.
3. **방어 준비** — 본진의 1회성 보호막·회복 여유 같은 초기 안전장치.

한 MapRun에서는 하나만 선택한다. 준비 보정은 선택의 성격을 가지며 모두 누적되지 않는다.

다음 형태는 금지한다.

- 유닛 공격력·공격속도·치명타·방어력의 영구 누적 배율.
- 건물·금고·농장 생산량의 전 구간 영구 배율.
- 릴 당첨 확률·TokenSource 후보를 조용히 유리하게 조작하는 보정.
- 무한 랭크, 반복 구매, prestige마다 재누적되는 성장.
- Stage 5·10·15·20의 고유 기믹을 무시하게 만드는 보정.

## 4. 획득·소비 구조

### 4.1 영구재화

정산 완료된 Profile 영구재화는 다음에 사용한다.

- 수평 해금.
- 제한된 편의 해금.
- 외형·기록.
- Stage 5 이후 제품 paid Retry.

현재 런에서 아직 정산되지 않은 예상 재화는 사용할 수 없다.

### 4.2 준비 보정 해금 방식

준비 보정은 Retry와 직접 같은 지갑에서 반복 구매하지 않는다. 권장 구조는 **정산된 누적 Profile 진행도 milestone**으로 유한 단계가 열리는 방식이다.

이유:

- Retry를 사용했다는 이유로 영구 전투력 성장이 뒤처지는 처벌을 막는다.
- 영구 전투력 구매를 위해 Retry를 포기하는 강제 최적화를 줄인다.
- 무한 재화 파밍을 전투력 누적과 분리한다.

정확 milestone 수·단계 수·효과량은 `RECOMMENDED_DEFAULT / TEST_VALUE`로 산출한 뒤 100K Profile trajectory와 사람 검증을 통과해야 한다.

## 5. 난이도·공정성 불변 조건

```text
BASE_PROFILE_CAN_COMPLETE_ALL_CONTENT
MAX_PROFILE_DOES_NOT_BYPASS_CORE_DECISIONS
ONE_READINESS_PERK_PER_MAPRUN
NO_INFINITE_RANKS
NO_GLOBAL_COMBAT_MULTIPLIER_STACK
NO_PREMIUM_POWER_PURCHASE
```

- 기본 난이도는 성장 Profile을 전제로 강제 상승시키지 않는다.
- 최고 Profile도 잘못된 릴 구조·건물 투자·전선 커밋을 자동으로 상쇄하지 못한다.
- 준비 보정의 주 영향은 런 시작과 Act 1에 집중하고 후반 복리로 확장하지 않는다.
- 비교·도전·리더보드 성격의 모드는 Profile 보정을 끄는 `STANDARDIZED_PROFILE`을 지원할 수 있다.

## 6. 권장 시험 가드레일

아래는 제품 확정 수치가 아니라 candidate 판정 기준이다.

```yaml
full_run_win_rate_delta_max_profile_vs_base:
  status: TEST_GUARDRAIL
  recommended_ceiling: 5_percentage_points
act1_clear_rate_delta:
  status: TEST_RANGE
  recommended_range: 3_to_8_percentage_points
readiness_perk_count:
  status: RECOMMENDED_DEFAULT
  candidate: 3
readiness_equipped_per_run:
  status: USER_APPROVED_CONSTRAINT
  value: 1
readiness_rank_count_per_perk:
  status: RECOMMENDED_DEFAULT
  candidate: 2
```

가드레일을 넘으면 효과량 축소, 적용 구간 단축, 후보 제거 순으로 조정한다. 평균만 보지 않고 실패 seed·후반 꼬리 분포·Profile별 지배 전략을 함께 검사한다.

## 7. 적대적 검토

| 공격 | 검증된 위험 | 보완 |
|---|---|---|
| B안이 반복 노가다로 난이도를 무력화한다 | 유효 | 한 런 1개·유한 랭크·초반 한정·전 구간 배율 금지 |
| A안의 수평 해금도 선택 폭을 통해 숨은 상위 호환이 된다 | 유효 | sidegrade 비용·사용 조건·채택률·공세별 성능 검증 |
| Retry와 영구 전투력 구매가 같은 재화를 두고 경쟁한다 | 유효 | 준비 보정은 누적 milestone 해금, Retry는 spendable balance 소비 |
| 시작 보정이 Act 1을 형식적인 구간으로 만든다 | 유효 | Act 1 clear delta 가드레일·후반 복리 금지 |
| Profile별 난이도 차이로 실패 원인이 불명확해진다 | 유효 | 결과 복기에 활성 Profile 보정과 기여도를 명시 |
| B를 반영했으므로 직접 공격력 트리가 필요하다 | 기각 | 성장 체감은 선택형 초기 준비 보정으로도 제공 가능하며 코어 전술을 덜 훼손함 |

## 8. 저장·데이터 책임

ProfileSave는 최소 다음을 구분한다.

```yaml
ProfileProgressionState:
  settled_permanent_currency_balance
  settled_permanent_currency_total
  horizontal_unlock_ids
  convenience_unlock_tiers
  readiness_perk_unlocks
  readiness_perk_ranks
  selected_readiness_perk_id
  cosmetics
  discoveries
  achievements
```

- `settled_permanent_currency_total`은 milestone 판정에 사용하고 Retry 소비로 감소하지 않는다.
- `settled_permanent_currency_balance`는 해금·Retry 소비에 사용한다.
- 해금·선택·Retry 거래는 transaction journal과 멱등 receipt를 사용한다.
- schema·migration·rollback은 경제·Retry·save 정본과 fault injection Gate를 따른다.

## 9. 검증 계획

### 자동·시뮬레이션

같은 seed와 policy set으로 최소 다음 Profile을 비교한다.

- `P0_BASE_PROFILE` — 영구 성장 없음.
- `P1_HORIZONTAL_ONLY` — 수평·편의 해금만.
- `P2_HYBRID_MAX_CANDIDATE` — 수평·편의 + 최고 후보 준비 보정.

검사 항목:

- Act별 clear rate·전선 붕괴·경제 softlock.
- full-run win rate 차이.
- Retry 사용률·해금 지연·재화 고갈.
- 준비 보정별 선택률과 지배 전략.
- Profile별 실패 귀인과 후반 꼬리 seed.

### 사람 검증

- 성장 체감은 있으나 노가다가 필수라고 느끼지 않는가.
- 새 해금이 다른 전략을 시험하게 하는가.
- 준비 보정이 실패 원인을 숨기지 않는가.
- 기본 Profile도 공정하고 완전한 게임으로 느껴지는가.

## 10. 현재 상태와 후속 Gate

```text
DESIGN: USER_APPROVED
EXACT_VALUES: PENDING
PARAMETER_REGISTRY: UPDATE_REQUIRED_BEFORE_IMPLEMENTATION
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
```

다음 핵심 Grill Me Decision은 `OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1`이다. 이 문서의 정확 수치·재화명·해금 비용·milestone 값은 후속 수치 작업에서 권장 후보로 작성하며 제품값으로 자동 승격하지 않는다.
