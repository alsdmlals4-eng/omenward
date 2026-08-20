# [현행] OMENWARD 세 전선 · Omen Signature 압력 언어

```yaml
decision_id: OMW-PLAN-20260820-PRESSURE-LANGUAGE-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_APPROVED_RECOMMENDED_OPTION_A
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
parent_decisions:
  - OMW-PLAN-20260820-WORLD-ROLE-01
  - OMW-PLAN-20260820-MAPRUN-WORLD-01
scope: THREE_FRONTS_PRESSURE_MODEL_WORLD_MEANING_FORECAST_LANGUAGE
runtime_mutation: NONE
balance_mutation: NONE
visual_asset_approval: NONE
```

## 1. 결정

세 전선은 수호성의 물리적 방어 구역이다. `MASS / ARMORED / FLYING / INFILTRATION / SIEGE`는 적 종족·세력명이 아니라 징조수호관이 관측하는 다섯 개의 **Omen Signature** 즉, 다가올 공세의 문제 유형으로 정의한다.

한 적, 한 Wave, 한 전선은 복수 Signature를 가질 수 있다. 따라서 세력/적 외형과 전투 압력은 서로 독립된 레이어다.

```text
적 세력 / 종족 / 외형 / 문화
≠
전투에서 해결해야 하는 Pressure Signature
```

예시:

```text
중장 공성괴수 = ARMORED + SIEGE
다수의 소형 비행체 = MASS + FLYING
비행 공성병 = FLYING + SIEGE
```

## 2. 다섯 압력의 의미

| Signature | 플레이어가 읽는 문제 | 세계관적 의미 |
|---|---|---|
| MASS | 수적 밀도·전선 포화 | 병력 흐름이 한 지점에 비정상적으로 집중됨 |
| ARMORED | 높은 방어·내구 | 중장갑·보호된 병력이 공세의 중심임 |
| FLYING | 지상 전선 무시·공중 접근 | 상공 경로를 이용한 우회 압력이 증가함 |
| INFILTRATION | 우회로·후열 침투 | 정면선보다 약한 Route와 후방을 노림 |
| SIEGE | 구조물 파괴·전선 붕괴 | 병력 교환보다 성벽·거점 파괴가 공세 목표임 |

이 표는 세계관 설명이며 기존 전투 수치·타게팅 계약을 변경하지 않는다.

## 3. 세 전선과 Forecast

전선 A/B/C는 특정 Signature 전용 지역이 아니다. 어느 전선에도 모든 Signature가 올 수 있다.

권장 Forecast 정보 계약:

```text
전선별 주 압력
+ 부 압력
+ 강도
+ Route 징후
```

예:

```text
전선 A = MASS ★★★ + SIEGE ★
전선 B = ARMORED ★★
전선 C = INFILTRATION ★★ + FLYING ★
```

Forecast는 문제를 보여주되 정답을 지시하지 않는다.

기본 비공개/비권장 정보:

- 정확한 전체 병종 명단
- 정확한 출현 순서
- 특정 병종/건물을 직접 지시하는 정답 추천

예고 정보는 여러 대응축을 남겨야 하며, 하나의 하드카운터만 강제해서는 안 된다.

## 4. 기존 시스템 보호

### INVARIANT

- Pressure는 적 종족이나 세력과 동일시하지 않는다.
- 한 적/Wave/전선은 복수 Pressure를 가질 수 있다.
- 세 전선은 특정 Pressure 전용으로 고정하지 않는다.
- Forecast는 대응 가능한 정보를 주되 정답표가 되지 않는다.
- 기존 병종 역할·카운터·TokenSource·룰렛·비가역 전선 커밋을 유지한다.
- `FLYING`은 세계관 표현 때문에 새로운 보편 타게팅 금지 규칙으로 확대하지 않는다.

### CHANGEABLE

- `Omen Signature`의 최종 한국어 인게임 명칭
- 각 Signature의 아이콘/색/연출
- 전선 A/B/C의 지역명·지형·문화
- 적 세력별 Signature 사용 성향
- Forecast의 구체 UI 표현과 강도 표기 방식

## 5. 장기 확장 원칙

새 적·세력·지역을 추가할 때 기존 5압력을 다시 정의하지 않는다. 새 콘텐츠는 기존 Signature를 조합해 자기 전술 정체성을 만든다.

예:

```text
세력 X = MASS + SIEGE 성향
세력 Y = INFILTRATION + FLYING 성향
보스 Z = ARMORED + SIEGE + 국면 전환
```

따라서 플레이어는 적 콘텐츠가 늘어도 같은 5개의 문제 언어를 계속 사용할 수 있고, 세력은 세계관/외형/행동 성향으로 차별화한다.

## 6. 피해야 할 방향

- 5개 Pressure를 5개 적 종족으로 1:1 고정
- 전선마다 특정 Pressure만 등장하도록 고정
- 예고 정보가 특정 병종 하나를 강제하는 하드카운터 지시표가 됨
- Pressure 이름 때문에 기존 runtime targeting 의미를 새로 정의함
- 적 세력의 시각 차별화와 Pressure UI를 같은 축으로 혼합해 가독성을 떨어뜨림

## 7. 다음 기획 의존성

이 Decision을 전제로 다음을 설계한다.

1. 건물·TokenSource·세 징조륜의 세계관상 연결
2. 첫 5 Stage에서 Pressure 읽기 학습 순서
3. Forecast UI 정보 계층
4. Visual Bible의 Signature 아이콘/색/실루엣 규칙
5. 적 세력/생물군은 이후 Story/Content 단계에서 Signature 조합으로 설계

## 8. 검증 상태

```yaml
TECH_EVIDENCE: NOT_APPLICABLE_FOR_THIS_PLANNING_DECISION
UI_EVIDENCE: NOT_RUN
HUMAN_USABILITY_EVIDENCE: NOT_RUN
PLAYER_EXPERIENCE_EVIDENCE: NOT_RUN
world_system_fit: HYPOTHESIS_APPROVED_FOR_PLANNING
revisit_conditions:
  - 5개 Signature만으로 실제 적 패턴을 설명하기 어려움
  - 복합 Signature가 플레이어에게 지나치게 복잡하게 읽힘
  - Forecast가 사실상 정답표 또는 무의미한 장식으로 변함
  - release-near Vertical Slice에서 전선 간 우선순위 판단이 발생하지 않음
```

실제 UI 가독성·학습성·재미는 release-near Vertical Slice 사람 플레이 전까지 PASS로 확정하지 않는다.
