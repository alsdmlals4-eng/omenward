# [현행] OMENWARD 동원 인장망 · 세 징조륜 세계 작동 의미

```yaml
decision_id: OMW-PLAN-20260820-MOBILIZATION-REGISTRY-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_APPROVED_RECOMMENDED_OPTION_A
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
parent_decisions:
  - OMW-PLAN-20260820-WORLD-ROLE-01
  - OMW-PLAN-20260820-MAPRUN-WORLD-01
  - OMW-PLAN-20260820-PRESSURE-LANGUAGE-01
scope: BUILDING_TOKENSOURCE_ROULETTE_WORLD_MEANING
runtime_mutation: NONE
balance_mutation: NONE
scene_resource_mutation: NONE
visual_asset_approval: NONE
```

## 1. 결정

건물은 직접 생산 기능과 중앙 **동원 인장망(Mobilization Registry)** 등록 기능을 가질 수 있다.

병영의 자동생산은 해당 시설에서 직접 훈련·편성되는 정규 병력이며, TokenSource는 같은 병종의 **동원 인장**을 수호성의 세 징조륜 각각에 등록하는 별도 획득 경로다.

```text
BUILDING
├─ AUTO_PRODUCTION = 해당 건물의 직접 훈련/편성
└─ TOKEN_SOURCE = 해당 병종의 중앙 동원 인장 등록
```

자동생산과 TokenSource는 같은 병종을 사용할 수 있지만 동일 이벤트로 합치지 않는다.

## 2. 세 징조륜

세 원형 릴은 세 전선과 1:1로 대응하지 않는다. 중앙 지휘소의 **하나의 삼중 동원 확률 장치**다.

활성 TokenSource 하나는 기존 물리 grammar를 그대로 따른다.

```text
TOKEN_INSTANCES_PER_REEL_PER_ACTIVE_SOURCE = 1
TOTAL_TOKEN_INSTANCES_PER_ACTIVE_SOURCE = 3
FRACTIONAL_TOKEN_WEIGHT = FORBIDDEN
```

세계관상 한 TokenSource는 같은 병종의 동원 인장을 세 징조륜 각각에 하나씩 등록한다.

```text
TokenSource: SHIELD
├─ Omen Wheel I   + Shield Seal 1
├─ Omen Wheel II  + Shield Seal 1
└─ Omen Wheel III + Shield Seal 1
```

징조륜 결과로 병력이 확보된 뒤에도 실제 전선 선택은 플레이어가 한다.

```text
징조륜 결과
→ 병력 획득
→ 보관 / 판매
→ 세 전선 중 하나 선택
→ 비가역 배치
```

따라서 `WHEEL_1 = LANE_1` 같은 고정 대응은 금지한다.

## 3. 일반병 병영

```text
GENERAL_T1_AUTO_PRODUCTION = BASIC_INFANTRY
GENERAL_T1_TOKEN_SOURCE = BASIC_INFANTRY
GENERAL_T2_AUTO_PRODUCTION = SELECTED_GENERAL_UNIT
GENERAL_T2_TOKEN_SOURCE = SELECTED_GENERAL_UNIT
```

플레이어가 일반병 병영을 건설/전문화하면 두 인과를 동시에 만든다.

1. 해당 병종이 일정 주기로 직접 생산된다.
2. 해당 병종의 동원 인장이 세 징조륜에 등록되어 미래 추가 동원 확률 분포가 바뀐다.

플레이어가 이해해야 하는 한 문장은 다음과 같다.

> 이 건물을 지었기 때문에 지금 병력이 생기고, 앞으로 어떤 병력이 더 자주 동원될지도 바뀐다.

## 4. 특수병 병영

기존 계약을 보존한다.

```text
SPECIAL_T1_SELECTION_TRIGGER = SUCCESSFUL_CONSTRUCTION_COMMIT
SPECIAL_T1_SELECTED_UNIT_PERSISTENCE = FIXED_WHILE_BUILDING_REMAINS_T1
SPECIAL_T1_AUTO_PRODUCTION = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_TOKEN_SOURCE = SELECTED_RANDOM_SPECIAL_UNIT
SPECIAL_T1_SAVE_RELOAD_RESELECT = FORBIDDEN
SPECIAL_T1_FREE_REROLL = FORBIDDEN
SPECIAL_T2_AUTO_PRODUCTION = SELECTED_SPECIAL_UNIT
SPECIAL_T2_TOKEN_SOURCE = SELECTED_SPECIAL_UNIT
```

세계관상 T1 특수병 병영 완성 시 어떤 전문 병단/교단이 해당 시설에 배속·계약되었는지가 확정된 것으로 해석한다. T1 동안 그 계약은 고정되고, 같은 병종의 직접 생산과 동원 인장 등록이 각각 작동한다.

T2에서 플레이어가 전문화를 선택하는 것은 우연히 시작된 T1 배속을 **의도적인 군제 개편**으로 확정하는 의미를 가진다.

구체적인 조직명·교단명은 CHANGEABLE이며 후속 Story/Visual planning에서 정한다.

## 5. 시스템 추가 금지 경계

동원망/중앙 예비대/병단 등록은 현재 시스템을 설명하는 세계관 레이어다. 다음 신규 관리 시스템을 이 Decision으로 만들지 않는다.

- 인구 자원
- 별도 예비군 수치
- 수송 시간/보급 마차
- 병영 인력 배치
- 동원권 화폐
- 신규 운송·물류 시뮬레이션

세계관은 기존 `건설 → 확률 설계 → 병력 획득 → 전선 커밋` 인과를 이해시키기 위한 것이며 새 관리 노동을 추가하기 위한 근거가 아니다.

## 6. Visual / UI 후속 원칙

아직 Visual asset은 승인하지 않는다. 후속 Visualization planning에서는 최소한 다음 차이가 한눈에 읽혀야 한다.

- 건물의 직접 자동생산 출력
- TokenSource의 세 징조륜 확률풀 기여
- 건물/전문화 변경으로 미래 분포가 어떻게 바뀌었는지
- 세 징조륜과 세 전선이 별개라는 정보 구조

카지노·슬롯머신·잭팟 시각 문법은 계속 금지한다.

## 7. 보호 경계

### INVARIANT

- 자동생산과 TokenSource는 별도 획득 경로다.
- 같은 병종을 두 경로가 사용할 수 있다.
- 활성 Source 하나는 각 릴에 TokenInstance 하나씩 총 3개를 공급한다.
- 세 릴은 세 전선과 1:1로 대응하지 않는다.
- 룰렛/징조륜 이후 실제 전선 배치는 플레이어가 결정한다.
- 세계관 설명을 이유로 신규 인구/물류 자원을 추가하지 않는다.

### CHANGEABLE

- `동원 인장망`, `동원 인장`, `징조륜`의 최종 인게임 명칭
- 중앙 지휘소의 장치 외형
- 특수병 병단/교단/조직 이름
- 마법/기계/의식 장치의 비율

## 8. 검증 상태와 재검토 조건

```yaml
TECH_EVIDENCE: NOT_APPLICABLE_FOR_WORLD_MEANING_DECISION
RUNTIME_EVIDENCE: NOT_RUN_FOR_THIS_DECISION
UI_EVIDENCE: NOT_RUN
HUMAN_USABILITY_EVIDENCE: NOT_RUN
PLAYER_EXPERIENCE_EVIDENCE: NOT_RUN
revisit_conditions:
  - 플레이어가 자동생산과 TokenSource를 같은 보상 이벤트로 오해함
  - 세 징조륜을 세 전선 전용 릴로 오해함
  - 룰렛이 소환/가챠 장치처럼 인식됨
  - 세계관 설명이 신규 자원 관리 요구로 팽창함
  - release-near Vertical Slice에서 건물 선택이 미래 병력 분포를 바꾼다는 인과가 읽히지 않음
```

실제 이해도와 재미는 release-near Vertical Slice 사람 플레이 전까지 PASS로 확정하지 않는다.
