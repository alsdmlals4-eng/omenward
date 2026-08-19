# [현행] OMENWARD 징조주기 · MapRun 세계 의미

```yaml
decision_id: OMW-PLAN-20260820-MAPRUN-WORLD-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_APPROVED_RECOMMENDED_OPTION_A
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
parent_decision: OMW-PLAN-20260820-WORLD-ROLE-01
scope: MAPRUN_WORLD_MEANING_STAGE_CADENCE_LONG_TERM_EXPANSION
runtime_mutation: NONE
balance_mutation: NONE
visual_asset_approval: NONE
```

## 1. 결정

세계에는 여러 **수호성(Ward Citadel)** 이 존재한다. 한 MapRun은 하나의 수호성이 겪는 **20 Stage 징조주기(Omen Cycle)** 하나를 버티는 전역으로 정의한다.

수호성은 인류의 마지막 요새가 아니다. 여러 국가·세력·수호성이 존재할 수 있으며, 각 수호성은 징조가 집중되는 국경/전선 거점이다. 한 Run의 성공과 함락은 더 큰 전쟁의 기록으로 남는다.

```text
WORLD
→ 여러 수호성 / 지역 / 전역
→ 하나의 수호성 선택
→ 20 Stage Omen Cycle
→ 성공 / 함락 / 전쟁 기록
→ 다음 전역
```

## 2. 기존 시스템과의 연결

현재 20 Stage 구조와 Boss cadence를 보존한다.

```text
MAPRUN_STAGE_COUNT = 20
BOSS_STAGES = 5 / 10 / 15 / 20
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
```

세계관상 Stage 5/10/15/20은 징조가 크게 수렴하는 주요 결절로 해석한다. 세부 명칭은 이후 Story/Visual planning에서 조정할 수 있으나, Boss cadence와 전투 규칙 자체는 이 Decision으로 변경하지 않는다.

권장 서사 리듬:

```text
Stage 1~4   = 초기 징후와 첫 압력 학습
Stage 5     = 제1 수렴
Stage 6~9   = 복합 압력 확대
Stage 10    = 제2 수렴
Stage 11~14 = 누적된 설계의 대가와 적응
Stage 15    = 대수렴
Stage 16~19 = 최종 전역 압축
Stage 20    = 최종 징조 / 붕괴점
```

위 이름은 작업용 의미이며 최종 명칭은 CHANGEABLE이다.

## 3. 플레이어 감정 곡선

- 초반: "무슨 일이 올지 읽어야 한다."
- 중반: "내가 만든 군대 구조가 점점 굳어진다."
- 후반: "초반에 만든 확률과 건설 선택의 대가까지 안고 버텨야 한다."
- Stage 20: "20단계 동안 만든 전쟁 계획 전체가 시험받는다."

핵심은 Stage 수를 단순 난이도 번호로 소비하지 않고 **징조가 수렴하고, 플레이어의 설계가 점차 되돌리기 어려워지며, 마지막에 전체 계획이 검증되는 세션 곡선**으로 읽히게 하는 것이다.

## 4. 장기 확장 원칙

### INVARIANT

- 한 Run 안에서는 건물/TokenSource/룰렛 설계가 누적된다.
- 한 Run은 하나의 수호성에서 진행되는 하나의 Omen Cycle이다.
- 20 Stage와 5/10/15/20 Boss cadence는 현재 승인 규칙을 유지한다.
- Run 종료는 단순 메뉴 리셋이 아니라 그 전역의 성공/함락 기록으로 해석한다.

### CHANGEABLE

- 수호성·국가·지역 이름
- 각 수호성의 biome/지형/문화
- 징조주기의 최종 인게임 용어
- Stage 5/10/15/20 수렴점의 서사 명칭
- Run 사이 세계지도/전역 선택 표현

### AVOID

- 시간 루프를 기본 반복 원인으로 사용해 이전 전역의 의미를 지우는 것
- 매 Stage마다 완전히 다른 지역으로 이동해 누적 건물의 세계관 의미를 약화하는 것
- 모든 Run을 '인류 마지막 요새' 한 곳에 고정해 장기 콘텐츠 확장을 막는 것

## 5. 콘텐츠 확장 문법

정식판 이후 새 콘텐츠는 가능하면 새 핵심 시스템보다 다음 조합을 우선한다.

```text
새 수호성
+ 새 환경/전장 외피
+ 새 압력 조합과 Route 변형
+ 새 Elite/Boss
+ 새 세계 사건/세력 맥락
```

이는 룰렛 설계→병력 획득→전선 커밋이라는 제품 정체성을 유지하면서 replayability를 늘리는 장기 확장 문법이다.

## 6. 재검토 조건

다음 중 하나가 release-near Vertical Slice 또는 후속 플레이테스트에서 확인되면 이 Decision을 reopen한다.

- 고정 수호성 때문에 플레이 공간이 지나치게 정적으로 느껴진다.
- 여러 MapRun 사이 세계적 진행감과 목적감이 약하다.
- 20 Stage가 실제 플레이에서 세션 호흡과 맞지 않는다.
- 한 Run 안에서 다양한 지역/biome 이동이 핵심 재미에 더 중요하다는 강한 증거가 나온다.

## 7. 다음 기획 의존성

1. 세 전선의 세계관적 의미
2. MASS / ARMORED / FLYING / INFILTRATION / SIEGE를 세계 안에서 읽는 정보 언어
3. 건물·TokenSource·징조륜의 작동 의미
4. 첫 5 Stage 학습/감정 곡선
5. 주요 화면과 Visual Requirement Inventory

## 8. 검증 상태

```yaml
TECH_EVIDENCE: NOT_APPLICABLE_FOR_THIS_PLANNING_DECISION
UI_EVIDENCE: NOT_RUN
HUMAN_USABILITY_EVIDENCE: NOT_RUN
PLAYER_EXPERIENCE_EVIDENCE: NOT_RUN
world_system_fit: HYPOTHESIS_APPROVED_FOR_PLANNING
```

실제 재미·세션 호흡·세계적 진행감은 release-near Vertical Slice 사람 플레이 전까지 PASS로 확정하지 않는다.
