# 오멘워드 Profile 영구 성장 역할 승인 계약

```yaml
decision_id: OMW-DEC-20260802-META-PROGRESSION-ROLE-V1
approved_at: 2026-08-02 11:16 KST
approval: USER_APPROVED_RECOMMENDATION_PLUS_B
status: USER_APPROVED_PLAN / EXACT_VALUES_PENDING / NOT_IMPLEMENTED
extension_decision: OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1
work_mode: TOTAL_PLANNING
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

Profile 영구 성장은 **수평 해금과 제한된 편의**를 주축으로 하고, 성장 체감을 위해 **엄격히 상한이 있는 선택형 초기 준비 보정**을 보조축으로 포함한다.

```text
PRIMARY = HORIZONTAL_UNLOCKS_AND_LIMITED_CONVENIENCE
SECONDARY = CAPPED_SELECTABLE_READINESS_POWER
AUXILIARY_HUB = TAVERN + BARRACKS + RESEARCH
FORBIDDEN = UNBOUNDED_PASSIVE_STAT_GRIND
```

기본 Profile만으로 전체 콘텐츠를 완료할 수 있어야 한다. 영구 성장은 실패 분석·건물 투자·릴 설계·전선 커밋을 대체하지 않는다.

## 2. 수평 해금

허용:

- 대체 시작 교리와 시작 구성안.
- 새로운 병종·전문화·건물·TokenSource·미션 sidegrade.
- 영웅 이상 전문 인재의 제한된 출전 선택.
- 도감·세계관·벨루 분석·복기 기록.
- 외형·문양·장식.
- 제한된 시작 보관 편의.

불변 조건:

- 해금 전 기본 구성으로 모든 Stage 완료 가능.
- 해금 선택지는 장점과 비용 또는 조건을 함께 가짐.
- 모든 공세에서 우월한 선택은 sidegrade가 아니라 밸런스 결함.
- 한 런에서 동시에 활성화할 시작 선택·영웅·준비 보정은 제한.

## 3. 제한된 편의

허용 후보:

- 시작 보관 용량의 작은 hard-cap 확장.
- 시작 구성안·필터·복기·선택 이력.
- 비전투 UI와 정보 접근 편의.

금지:

- 런 안의 무제한 보관 확장.
- 자동 건설·자동 배치·자동 릴 편집.
- 편의를 가장한 지속 전투 배율.

## 4. ReadinessPerk

```yaml
ReadinessPerk:
  unlock_source: settled_permanent_currency_total_milestone
  equipped_per_maprun: 1
  rank_model: finite_hard_cap
  stacking: forbidden
  duration: opening_or_act1_limited
  exact_values: pending_simulation
```

후보군:

1. 재정 준비 — 시작 골드 또는 1회성 준비 자원.
2. 군수 준비 — 시작 식량 한도 또는 배치 여유.
3. 방어 준비 — 본진 1회성 보호막·회복 여유.

금지:

- 유닛 공격력·공격속도·치명타·방어력의 영구 누적 배율.
- 건물·금고·농장 생산량의 전 구간 영구 배율.
- 릴 당첨 확률·TokenSource 후보의 숨은 유리 조작.
- 무한 랭크·prestige 재누적.
- Stage 5·10·15·20 고유 기믹 무시.

## 5. 메인 허브 소비 surface

상세 책임 원본: `APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md`.

### 주점

- 영웅 이상 전문 인재를 결정론적 공개 노드로 영구 영입.
- 랜덤 상자·유료 재굴림·중복 합성 금지.
- 영입은 영구, MapRun 출전은 제한. 정확 상한 pending.

### 허브 병영

- 병사 훈련·병종·전문화·교리 sidegrade.
- 전장 TokenSource 병영과 Profile 시설을 구분.
- 무한 훈련·전 구간 전투 배율 금지.

### 연구

- 대체 건물·TokenSource·미션·분석·편의 sidegrade.
- 숨은 릴 확률 조작·전 구간 생산 배율·자동 플레이 금지.

## 6. 획득·소비 구조

```text
settled_permanent_currency_balance
= 주점·병영·연구 노드 + paid Retry 소비

settled_permanent_currency_total
= 감소하지 않는 누적 진행도 + Readiness milestone 판정
```

- 현재 런의 미정산 예상 재화는 사용할 수 없다.
- balance 거래는 transaction journal과 idempotent receipt를 사용한다.
- Retry 소비가 total과 Readiness 진행도를 후퇴시키지 않는다.
- 노드 구매와 Retry의 지갑 경쟁은 공개된 기회비용으로 유지하되 과도한 비축·후회·파밍을 simulation과 사람 검증으로 검사한다.

## 7. 공정성 불변 조건

```text
BASE_PROFILE_CAN_COMPLETE_ALL_CONTENT
MAX_PROFILE_DOES_NOT_BYPASS_CORE_DECISIONS
ONE_READINESS_PERK_PER_MAPRUN
NO_INFINITE_RANKS
NO_GLOBAL_COMBAT_MULTIPLIER_STACK
NO_RANDOM_PAID_RECRUITMENT
NO_PREMIUM_POWER_PURCHASE
```

- 최고 Profile도 잘못된 릴 구조·건물 투자·전선 커밋을 자동 상쇄하지 못한다.
- 영웅·훈련·연구가 모든 공세에서 동일한 필수 정답으로 수렴하면 결함이다.
- 비교·도전 모드는 Profile 보정을 끄는 `STANDARDIZED_PROFILE`을 지원할 수 있다.

## 8. 시험 가드레일

아래는 제품 확정값이 아니다.

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
readiness_rank_count_per_perk:
  status: RECOMMENDED_DEFAULT
  candidate: 2
hero_active_cap:
  status: RECOMMENDED_DEFAULT
  candidate: 1_contract_per_maprun
```

가드레일을 넘으면 효과량 축소, 적용 구간 단축, 후보 제거 순으로 조정한다.

## 9. 저장 책임

```yaml
ProfileProgressionState:
  settled_permanent_currency_balance
  settled_permanent_currency_total
  horizontal_unlock_ids
  convenience_unlock_tiers
  readiness_perk_unlocks
  readiness_perk_ranks
  selected_readiness_perk_id
  auxiliary_unlocked_node_ids
  tavern_recruit_ids
  barracks_training_ids
  research_unlock_ids
  selected_run_loadout_ids
  cosmetics
  discoveries
  achievements
  transaction_receipts
```

schema·migration·rollback·journal replay·current/backup 복구는 fault injection Gate를 따른다.

## 10. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 영구 성장으로 노가다가 난이도를 무력화한다 | 유효 | 한 런 1개 Readiness·유한 랭크·초반 한정·전 구간 배율 금지 |
| 수평 해금도 숨은 상위 호환이 된다 | 유효 | 비용·조건·채택률·공세별 성능 검증 |
| 영웅이 일반 병사를 무가치하게 만든다 | 유효 | 고유 역할·출전 상한·기본 Profile 완주 |
| 주점이 가챠로 변질된다 | 유효 | 공개 결정론적 노드, 랜덤 유료 영입 금지 |
| Retry와 노드가 같은 지갑에서 충돌한다 | 유효 | balance/total 분리, 기회비용 공개, trajectory 검증 |
| 연구가 숨은 확률 버프가 된다 | 유효 | 릴 확률·전 구간 생산 배율 금지 |
| 시작 보정이 Act 1을 형식화한다 | 유효 | Act 1 delta 가드레일·후반 복리 금지 |

## 11. 검증 계획

동일 seed·policy로 비교:

- `P0_BASE_PROFILE`
- `P1_HORIZONTAL_ONLY`
- `P2_HYBRID_MAX_CANDIDATE`

추가 검사:

- 시설별 노드 채택률과 지배 순서.
- 영웅 없음/후보 영웅 활성의 Act·full-run 차이.
- Retry 사용률·노드 해금 지연·재화 비축.
- 실패 seed·후반 꼬리·실패 귀인.
- 구매 transaction fault injection.
- 메인 허브와 노드 그래프 사람 가독성.

## 12. 현재 상태

```text
DESIGN: USER_APPROVED
AUXILIARY_HUB: USER_APPROVED_STRUCTURE
EXACT_VALUES_AND_CONTENT: PENDING
PARAMETER_REGISTRY: UPDATE_REQUIRED_BEFORE_IMPLEMENTATION
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
NEXT_WORLD_GATE: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
```
