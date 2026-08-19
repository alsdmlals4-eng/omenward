# [현행] OMENWARD 세계 역할 · Omen Warden 정체성

```yaml
decision_id: OMW-PLAN-20260820-WORLD-ROLE-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_APPROVED_RECOMMENDED_OPTION_A
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
scope: WORLD_PREMISE_PLAYER_ROLE_SYSTEM_MEANING
runtime_mutation: NONE
balance_mutation: NONE
visual_asset_approval: NONE
```

## 1. 결정

플레이어 역할은 **징조수호관(Omen Warden)** 으로 확정한다.

플레이어는 세 전선을 지키는 요새의 징조수호관으로서 다가올 공세의 징조를 읽고, 요새의 건물과 TokenSource를 통해 세 개의 전쟁륜/징조륜이 어떤 병력을 더 자주 동원할지 조율한다.

룰렛은 카지노나 도박 장치가 아니다. 세계 안에서 **전쟁의 불확실성을 통제하기 위한 군사적 확률 장치**로 해석한다.

```text
OMEN = 다가올 위협을 읽는다
WARD = 읽은 위협에 대비해 지킨다
```

## 2. 기존 코어와의 연결

기존 승인 코어는 보존한다.

```text
예고된 압력
→ 건물 / TokenSource / 룰렛 확률 설계
→ 병력 획득
→ 비가역 전선 배치
→ 수동 전술 타이밍
→ 설명 가능한 결과 / 다음 설계
```

세계관 표현에서는 다음처럼 읽힌다.

```text
징조 관측
→ 요새 건설
→ 징조륜/전쟁륜 조율
→ 병력 동원
→ 세 전선 중 하나에 커밋
→ 자동전투와 전술 개입
→ 전쟁 기록과 다음 조율
```

이 Decision은 룰렛의 확률 규칙, TokenSource 물리 grammar, 건물 Tier, 병종 역할, 비가역 lane commitment를 변경하지 않는다. 기존 시스템에 세계관상 이유와 플레이어 판타지를 결합한다.

## 3. 플레이어 약속

플레이어가 느껴야 하는 핵심은 "운이 좋았다"가 아니라 다음 인과다.

1. 나는 앞으로 닥칠 압력을 읽었다.
2. 그 정보로 미래 병력 분포를 설계했다.
3. 완전히 통제할 수 없는 결과를 받아들였다.
4. 나온 병력을 어느 전선에 희생·집중할지 결정했다.
5. 결과를 보고 내 설계가 왜 성공/실패했는지 배웠다.

핵심 긴장은 **예측 가능하지만 완전히 확정할 수 없는 미래를 얼마나 잘 준비하고 받아들이는가**다.

## 4. 보호할 표현 원칙

### INVARIANT

- `ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE`
- `GAMBLING_FANTASY_POSITIONING = FORBIDDEN`
- `PAID_SPIN = FORBIDDEN`
- 예고 정보는 대응 가능성을 남겨야 한다.
- 건설은 단순 경제 버튼이 아니라 미래 병력 확률을 설계하는 행동이어야 한다.
- 병력의 비가역 전선 커밋은 의미 있는 희생/집중 결정으로 남긴다.
- 결과 화면은 성공/실패의 인과를 복기할 수 있어야 한다.

### CHANGEABLE

- `징조륜`, `전쟁륜` 등 인게임 최종 명칭
- 징조수호관의 조직명, 요새명, 국가/세력명
- 세계의 기술 수준과 마법/기계 비율
- 룰렛 장치의 구체적 외형과 애니메이션
- 개별 병종/건물의 최종 세계관 명칭

이 항목들은 상위 의미를 훼손하지 않는 범위에서 이후 Visual/Story planning에서 조정한다.

## 5. 피해야 할 방향

- 슬롯머신, 카지노 칩, 잭팟 등 도박 보상 문법을 핵심 Visual로 사용하는 것
- 룰렛 결과를 플레이어가 설계할 수 없는 순수 랜덤 보상으로 만드는 것
- 징조가 사실상 정답을 직접 알려주는 하드카운터 지시표가 되는 것
- 세계관 설명을 위해 기존 확률/전선 판단을 불필요하게 복잡하게 만드는 것
- 영웅 서사 때문에 플레이어의 지휘/설계 주도권을 NPC에게 넘기는 것

## 6. 다음 기획 의존성

이 Decision을 전제로 다음 순서로 상세화한다.

1. 세계 전제와 핵심 갈등
2. 20 Stage MapRun이 세계 안에서 무엇을 의미하는지
3. 세 전선과 다섯 압력의 세계관적 정체
4. 건물/TokenSource/징조륜의 작동 의미
5. 첫 5 Stage의 학습·감정 곡선
6. 주요 Decision Screen과 Flow
7. Visual Requirement Inventory
8. 병종·건물·보상 세부 표현
9. Balance Budget

## 7. 검증 상태

```yaml
TECH_EVIDENCE: NOT_APPLICABLE_FOR_THIS_PLANNING_DECISION
UI_EVIDENCE: NOT_RUN
HUMAN_USABILITY_EVIDENCE: NOT_RUN
PLAYER_EXPERIENCE_EVIDENCE: NOT_RUN
world_system_fit: HYPOTHESIS_APPROVED_FOR_PLANNING
revisit_conditions:
  - 플레이어가 룰렛을 여전히 순수 운/가챠로 인식함
  - 세계관 설명이 핵심 판단 이해를 방해함
  - 세 전선/건설/룰렛이 세계 안에서 서로 다른 장치처럼 분리되어 보임
  - release-near Vertical Slice에서 예측→설계→커밋→복기 감정이 발생하지 않음
```

이 문서는 현재 기획 정본의 새 world/player-role owner다. 실제 재미와 이해도는 release-near Vertical Slice 사람 플레이 전까지 PASS로 확정하지 않는다.
