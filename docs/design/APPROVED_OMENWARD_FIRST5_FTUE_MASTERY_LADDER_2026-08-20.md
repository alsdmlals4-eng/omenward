# [현행] OMENWARD 첫 5 Stage FTUE · 숙련 사다리

```yaml
decision_id: OMW-PLAN-20260820-FIRST5-FTUE-01
status: APPROVED_CURRENT
approved_at: 2026-08-20
approval: USER_APPROVED_RECOMMENDED_OPTION_A
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
parent_decisions:
  - OMW-PLAN-20260820-WORLD-ROLE-01
  - OMW-PLAN-20260820-MAPRUN-WORLD-01
  - OMW-PLAN-20260820-PRESSURE-LANGUAGE-01
  - OMW-PLAN-20260820-MOBILIZATION-REGISTRY-01
scope: FIRST_SESSION_STAGE_1_TO_5_LEARNING_AND_EMOTION
runtime_mutation: NONE
balance_mutation: NONE
visual_asset_approval: NONE
```

## 1. 결정

기존 Stage 1~5 기능 순서를 유지하되, 첫 세션을 다음 **5단계 숙련 사다리**로 읽히게 한다.

```text
Stage 1 = 인과 이해
Stage 2 = 미래 수정
Stage 3 = 순간 개입
Stage 4 = 응용 시험
Stage 5 = 첫 결산
```

새 시스템을 추가하는 결정이 아니라, 이미 승인된 기능을 플레이어가 한 번에 하나의 핵심 질문으로 학습하도록 **노출 순서와 피드백 목적을 명확히 하는 결정**이다.

## 2. Stage 1 · 인과 이해

기존 승인 규칙을 보존한다.

```text
STAGE_1_T1_BUILDINGS = ONE_EACH_ALL_SIX
STAGE_1_REQUIRED_T1 = VAULT / FARM / GENERAL_BARRACKS / DEFENSE_TOWER / COMMAND_POST / MANA_TOWER
SPECIAL_BARRACKS_STAGE1_REQUIRED = FALSE
FIRST_ROULETTE_UNLOCK = AFTER_ALL_SIX_T1_AND_SETUP_CONFIRMATION
FIRST_MEANINGFUL_COMBAT_CHOICE = STAGE_1_IRREVERSIBLE_DEPLOYMENT
```

단, 6개 건물을 한 화면에서 동일 밀도로 설명하지 않는다. 사람용 노출은 세 목적 묶음으로 순차 진행한다.

```text
1. 생존 기반
   VAULT + FARM
   → 전쟁을 지속할 기반

2. 군사 기반
   GENERAL_BARRACKS + DEFENSE_TOWER
   → 지금 병력이 생기는 경로와 전선을 버티는 수단
   → 병영 건설 시 AUTO_PRODUCTION과 TokenSource/동원 인장 기여를 별도 피드백

3. 지휘 기반
   COMMAND_POST + MANA_TOWER
   → 이후 지휘·전술 확장의 기반
   → Mana Tower의 세부 연구 학습은 Stage 3까지 미룬다
```

Stage 1의 교육 목표는 건물명 6개 암기가 아니다.

```text
징조를 읽었다
→ 건물을 세웠다
→ 미래 병력 분포가 바뀌었다
→ 징조륜에서 병력을 얻었다
→ 내가 한 전선을 골라 비가역 배치했다
→ 전투 결과가 나왔다
```

플레이어가 이 인과를 한 문장으로 설명할 수 있는 것이 Stage 1의 핵심 이해 목표다.

## 3. Stage 2 · 미래 수정

기존 첫 T2 선택을 첫 번째 진짜 건설 결정으로 유지한다.

```text
FIRST_MEANINGFUL_BUILD_CHOICE = STAGE_2_T2_UPGRADE
STAGE_2_T2_CANDIDATES = TWO_RELEVANT_VALID_OPTIONS
STAGE_2_T2_UPGRADE_BUDGET = GUARANTEED_SUFFICIENT_FOR_ONE_CANDIDATE
T2_UPGRADE_PREVIEW = REQUIRED
```

T2 선택 화면은 가능하면 다음 인과를 비교해서 보여준다.

```text
현재 동원 구성
→ 후보 업그레이드
→ 어떤 병종/역할의 직접 생산과 동원 인장 기여가 어떻게 바뀌는지
→ 변경 후 예상 방향
```

최종 절대 확률·비용·생산간격은 evidence 전 확정하지 않는다. 초기 UI는 **방향 변화와 상대적 영향**을 우선 전달한다.

Stage 2의 목표 감정:

> 룰렛은 운을 기다리는 장치가 아니라 내가 미래 분포를 설계하는 장치다.

## 4. Stage 3 · 순간 개입

Stage 3에서 Mana Tower의 연구와 수동 전술 사용을 처음 완전하게 학습한다.

교육 목표는 10개 전술을 암기시키는 것이 아니라 다음 인과다.

```text
병력/건물/확률 설계로 대부분을 준비한다
→ 자동전투가 진행된다
→ 중요한 순간에 마력 전술로 보완한다
```

전술은 구조적 준비를 대체하는 자동 승리 버튼이 아니다.

Stage 3의 목표 감정:

> 자동전투지만 결정적인 순간의 판단은 여전히 내 몫이다.

## 5. Stage 4 · 응용 시험

Stage 4에는 의도적으로 새 핵심 시스템을 가르치지 않는다.

플레이어는 이미 배운 다음 요소를 스스로 결합한다.

```text
Forecast / Omen Signature
+ 건설·동원 인장·징조륜 설계
+ 비가역 전선 배치
+ 수동 전술
→ final-wave Elite 대응
```

Stage 4는 정보 추가가 아니라 **인지적 휴식 + 독립 응용 확인**을 담당한다.

## 6. Stage 5 · 첫 결산

기존 Boss cadence를 유지한다.

```text
STAGE_5 = FIRST_BOSS_PLUS_FINAL_WAVE_ELITE_MASTERY_CHECK
BOSS_STAGE_FINAL_WAVE_ELITE_REQUIRED = TRUE
```

Boss의 핵심 위협은 사전 Omen Signature로 읽을 수 있어야 한다. Boss전은 새 튜토리얼이 아니라 Stage 1~4에서 만든 첫 빌드 전체의 결산이다.

Stage 종료 복기는 다음 인과를 보여준다.

```text
처음 본 징조
→ 내가 만든 동원 구조
→ 주요 전선 배치
→ 결정적 사건
→ 플레이어 대응
→ 결과
```

`다음에는 X를 지으세요` 같은 처방형 정답 추천은 금지한다.

## 7. 보호 경계

### INVARIANT

- 첫 세션은 실제 MapRun이다.
- 별도 튜토리얼은 만들지 않는다.
- Stage 1 필수 T1 6종 자체는 이번 Decision으로 삭제하지 않는다.
- 첫 룰렛은 기존대로 6종 T1과 setup confirmation 이후 열린다.
- Stage 1 첫 의미 있는 전투 선택은 비가역 전선 배치다.
- Stage 2 첫 T2 선택, Stage 3 전술, Stage 4 응용, Stage 5 Boss 순서를 보존한다.
- Stage 4에는 새 핵심 시스템 교육을 추가하지 않는다.
- scripted victory, prescriptive next-build command, NPC 대리 결정을 금지한다.

### CHANGEABLE

- 각 설명 팝업의 정확한 문구·길이
- 6건물 묶음의 시각 배치·강조 방식
- 상대적 확률 변화 표현 방식
- Stage 1~5의 정확한 분 단위 시간
- Stage 1/2의 세부 enemy composition

## 8. 대안과 재검토

### 대안 B · Stage 1 필수 건물 수 축소

초기 학습 과부하를 줄일 가능성이 있지만 기존 경제·첫 T2·테스트·밸런스 계약을 넓게 다시 열어야 하므로 현 시점에는 채택하지 않는다.

다음 조건이면 B를 최우선으로 재검토한다.

- release-near Vertical Slice 사람 플레이에서 6건물 설치 전 핵심 인과 이해가 무너짐
- 첫 룰렛 도달 전 이탈/혼란이 반복됨
- 플레이어가 건물 역할은 기억하지만 `건설 → 미래 분포 → 전선` 인과를 설명하지 못함

### 대안 C · Stage 1 전체 시스템 일괄 설명

정보 밀도가 지나치게 높고 현재 `FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN`과 충돌하므로 제외한다.

## 9. 검증 상태

```yaml
TECH_EVIDENCE: NOT_APPLICABLE_FOR_THIS_PLANNING_DECISION
UI_EVIDENCE: NOT_RUN
HUMAN_USABILITY_EVIDENCE: NOT_RUN
PLAYER_EXPERIENCE_EVIDENCE: NOT_RUN
FTUE_CLARITY: HYPOTHESIS_APPROVED_FOR_PLANNING
```

실제 이해도·첫인상·감정 곡선은 release-near Vertical Slice 사람 플레이 전까지 PASS로 올리지 않는다.
