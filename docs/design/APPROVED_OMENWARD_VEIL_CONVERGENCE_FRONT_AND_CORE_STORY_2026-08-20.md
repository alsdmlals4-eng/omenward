# [현행] OMENWARD · 베일 수렴전선과 핵심 스토리

```yaml
decision_id: OMW-PLAN-20260820-WORLD-CONFLICT-STORY-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_APPROVED_RECOMMENDED_OPTION_A
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
parent_decisions:
  - OMW-PLAN-20260820-WORLD-ROLE-01
  - OMW-PLAN-20260820-MAPRUN-WORLD-01
  - OMW-PLAN-20260820-PRESSURE-LANGUAGE-01
  - OMW-PLAN-20260820-MOBILIZATION-REGISTRY-01
runtime_mutation: NONE
balance_mutation: NONE
visual_asset_approval: NONE
```

## 1. 결정

OMENWARD의 상위 세계 갈등은 **베일 수렴전선(Veil Convergence Front)** 으로 정의한다.

```text
VEIL = 적 종족 하나가 아니라 현실과 겹쳐지는 적대적 경계 현상
OMEN = 실제 공세가 도착하기 전에 나타나는 전조 / Pre-Echo
OMEN_WARDEN = 전조를 읽고 군사적 대응을 설계하는 수호성 지휘자
OMEN_CYCLE = 한 수호성 주변에서 Veil 겹침이 20 Stage에 걸쳐 심화되는 한 번의 수렴기
STAGE_20 = 해당 Cycle을 현실에 고정시키는 수렴핵/정박체를 파괴하는 결산
RUN_VICTORY = 세계 리셋이 아니라 해당 수호성의 이번 수렴을 진압한 실제 전쟁 기록
```

`수렴핵`, `정박체`, `Pre-Echo`는 작업용 명칭이며 최종 세계관 명칭은 후속 네이밍에서 변경 가능하다.

## 2. Veil의 역할

Veil은 `MASS`, `ARMORED`, `FLYING`, `INFILTRATION`, `SIEGE` 중 하나와 동일하지 않다.

Veil은 현실과 다른 층이 겹치며 병력·괴이·변질된 전쟁 형태가 침투하거나 증폭될 수 있게 만드는 **세계 현상 / 전선 레이어**다.

따라서 다음을 허용한다.

- Veil에서 태어난 존재.
- Veil에 변질된 병단.
- Veil을 이용하는 인간·국가·교단·세력.
- Veil과 독립된 적 세력이나 괴물이 수렴기에 편승하는 구조.

금지:

- `Veil = 적 종족 하나`로 고정.
- `Pressure = 적 종족/세력`으로 고정.
- `MASS 세력`, `SIEGE 세력`처럼 Omen Signature와 세계 세력을 1:1 연결.

## 3. Omen과 Forecast의 세계관 의미

Veil을 통해 현실에 도착할 공세는 완전히 현현하기 전에 **전조(Pre-Echo)** 를 남긴다.

징조수호관은 그 전조를 분석해 전술적으로 읽을 수 있는 Omen Signature로 분류한다.

```text
Veil 전조
→ 공세의 성질이 먼저 비침
→ Omen Warden 관측/분석
→ MASS / ARMORED / FLYING / INFILTRATION / SIEGE 분류
→ 주 압력 + 부 압력 + 강도 + Route 징후 Forecast
→ 건설/동원/전선 대응
→ 실제 공세 현현
```

Forecast는 미래의 정확한 전체 병종·순서·정답 카운터를 공개하는 예언이 아니다. **다가오는 문제의 구조를 미리 읽는 군사 정보**다.

## 4. 20 Stage Omen Cycle의 세계 의미

Veil 겹침은 한 번에 최대가 되지 않고 단계적으로 수렴한다.

```text
미세한 전조
→ 작은 균열
→ 반복 공세
→ 복합 Omen Signature 중첩
→ 수렴체 출현
→ 대수렴
→ 수렴핵/정박체 현현
```

한 수호성에서 이 전 과정이 완성되는 한 번의 수렴기가 `20 Stage Omen Cycle`이다.

기존 cadence는 보호한다.

```text
Stage 5  = 제1 수렴 결절
Stage 10 = 제2 수렴 결절
Stage 15 = 대수렴
Stage 20 = 최종 수렴 / Cycle 정박 결산
BOSS_STAGES = 5 / 10 / 15 / 20
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
```

위 서사 명칭은 CHANGEABLE이고 Stage 수·Boss cadence는 이번 Decision으로 바꾸지 않는다.

## 5. Stage 20의 결산

Stage 20의 목표는 세계 전체의 Veil을 영구 제거하는 것이 아니다.

플레이어는 이번 수호성에 형성된 **수렴핵/정박체**와 그 최종 공세를 파괴해 현재 Omen Cycle을 끝낸다.

```text
Stage 20 승리
→ 해당 Ward Citadel의 현재 Omen Cycle 진압
→ 지역 Veil 압력 완화
→ 수호성 생존 / 전쟁 기록 갱신
→ 더 큰 전쟁은 계속됨
```

이 구조는 확장 시 새 Ward Citadel, biome, 적 세력, Boss, 사건을 추가해도 핵심 시스템을 재작성하지 않도록 한다.

## 6. Run 간 세계 진행

시간 루프를 기본 설정으로 사용하지 않는다.

```text
RUN_HISTORY_RESET = FALSE
FAILED_OR_WON_RUNS_CAN_EXIST_AS_WORLD_HISTORY = TRUE
META_PROGRESS_IS_NOT_TIME_REWIND = TRUE
```

승전은 실제 역사로 남는다. 향후 메타/캠페인에서는 수호성별 방어 기록, 해금된 전선, 발견된 세력/적 유형, 세계 사건 등으로 연결할 수 있다.

단, 이 Decision은 새로운 영구 전투 스탯 누적이나 필수 grind currency를 승인하지 않는다.

## 7. 적군 공용 10병종 계약과의 연결

현재 첫 PoC 적군은 아군과 같은 10개 전투 아키타입을 공유하고 진영별 Visual Set으로 변환된다.

따라서 초기 Veil 적군은 다음 원리로 읽는다.

```text
공용 전투 역할은 익숙하게 읽힘
+
Veil을 거치며 외형/표시명이 왜곡된 전쟁 형태로 보임
```

예:

- shield_guard 역할 → 베일 갑각수 Visual Set.
- greatsword_warrior 역할 → 균열도살자 Visual Set.
- mage 역할 → 공허주술사 Visual Set.

세계관은 공용 아키타입 계약을 파괴하기 위해 새로운 적군 스탯/스킬 데이터 복제를 요구하지 않는다.

## 8. 의도적으로 미확정으로 남기는 것

다음은 현재 고정하지 않는다.

```text
VEIL_HAS_SENTIENT_WILL = UNRESOLVED
VEIL_ORIGIN = UNRESOLVED
WHO_FIRST_DISCOVERED_OR_CREATED_OMEN_WHEELS = UNRESOLVED
HUMAN_FACTION_EXPLOITING_VEIL = FUTURE_CONTENT_OPTION
FINAL_WORLD_ENDING = UNRESOLVED
```

초기에는 Veil이 자연현상인지, 의지가 있는지, 누군가 이용하는지 확정하지 않아 향후 세력·Boss·스토리 확장 공간을 남긴다.

## 9. 벤치마크 disposition

- `Against the Storm — ADAPT`: 반복되는 세계 현상, 명확한 플레이어 역할, 개별 run을 더 큰 cycle에 연결하는 구조 원리만 차용.
- `The Last Spell — ADAPT / AVOID`: 거점 방어 목적의 명료성은 차용하되 마지막 인류 요새/보라 안개/세계 재앙 영구종결 표면 설정은 회피.
- `Into the Breach — REFERENCE_ONLY / AVOID TIME LOOP`: 반복을 세계관으로 설명하는 원리는 참고하되 OMENWARD는 실제 전쟁 기록을 우선.
- `They Are Billions — ADAPT`: 고정 거점에 압도적 외부 압력이 다가오고 준비가 생존과 연결되는 명료성만 차용.

외부 작품의 고유 명칭, lore, 캐릭터, 미션 구조, 아트는 복제하지 않는다.

## 10. 보호 경계

INVARIANT:

- 여러 Ward Citadel이 존재한다.
- 한 MapRun = 한 수호성의 20 Stage Omen Cycle.
- Veil은 적 종족/Pressure 하나와 동일하지 않다.
- Omen Signature는 전술적 문제 언어다.
- 세 전선/룰렛/동원 인장/비가역 커밋 코어를 유지한다.
- Stage 5/10/15/20 Boss cadence 유지.
- 시간 루프는 기본 메타 설명으로 사용하지 않는다.
- 세계관 설명 때문에 새로운 강제 관리 자원 시스템을 만들지 않는다.

CHANGEABLE:

- Veil/Pre-Echo/수렴핵의 최종 로컬라이징 명칭.
- 첫 수호성·국가·조직의 고유명.
- Veil의 기원과 의지 여부.
- 향후 적 세력/교단/국가의 정치 관계.
- Stage 5/10/15/20 Boss의 정확한 개체명·외형·서사.

## 11. 다음 Gate

```text
NEXT_PRODUCT_DECISION = 20_STAGE_CONTENT_AND_BOSS_STRUCTURE
IMAGE_GENERATION = PAUSED_PENDING_USER_REFERENCE_FILES
IMPLEMENTATION_START = NOT_AUTHORIZED
CURRENT_RUNTIME = NOT_RUN
HUMAN_PLAYER_EVIDENCE = NOT_RUN
```
