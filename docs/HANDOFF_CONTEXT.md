# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: WORLD_CANON_FOUNDATION
recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1
baseline_main: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
working_branch: gpt/omenward-canon-recovery-20260802
recovery_pr: 119_DRAFT
superseded_pr: 116_CLOSED_NOT_MERGED
base: 9.4.0_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: APPROVED_NOT_IMPLEMENTED
product_code_authority: NONE
codex: BLOCKED
sheet_sync: WORLD_RUN_SYNC_IN_PROGRESS
```

## 1. 가장 먼저 알아야 할 것

1. 오멘워드는 건물과 TokenSource로 세 물리 릴의 미래 배열을 설계하고, 당첨 병력을 세 전선 중 하나에 비가역 배치하는 전략 오토배틀이다.
2. 현재 제품은 Legacy 프로토타입이고 최신 기획은 미구현이다.
3. PR #119가 현재 정본 복구·총기획 Draft PR이며 PR #116은 닫힌 역사 증거다.
4. Profile 영구 성장은 수평 해금 중심 + 한 런 1개의 상한형 준비 보정으로 승인됐다.
5. 하나의 MapRun은 징조로 감지된 별개의 실제 경계 공세를 막는 20 Stage·4막 방어 작전으로 승인됐다.
6. 징조는 시간 반복이나 시뮬레이션이 아니라 제한된 공세 예측 정보다.
7. Stage 20 승리는 한 균열·침공로를 실제로 봉쇄하고, 패배는 전진 방어선 붕괴와 실제 피해다.
8. paid Retry는 시간 되감기가 아니라 같은 공세의 비상 재투입이다.
9. 다음 세계관 결정은 베일의 본질이다.
10. 주요 Decision은 같은 ID로 GitHub·Sheet 동기화 후 다음 질문으로 진행한다.

## 2. 현재 세계관 정본

정본: `docs/design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md`

```text
징조 감지
→ 실제 경계 방어 작전
→ 4막·20 Stage 공세 고조
→ 균열 봉쇄 또는 방어선 붕괴
→ 기록·교리·정산 성과가 Profile로 귀환
```

- 동일한 멸망의 날을 반복하지 않는다.
- 모든 전투가 가상 훈련이었다는 반전을 사용하지 않는다.
- 징조는 결과를 확정하지 않는다.
- 벨루는 작전을 관측·기록하고 선택 인과를 설명한다.
- Profile은 조직적 학습과 준비 체계다.

기존 명칭 계보:

- 루메른 왕국, 루미엔 영토, 트리븐 전선, 실베른 성채.
- 베일런 황야, 베일의 법칙, 베일의 징조, 베일종.
- 벨루.

명칭은 보존하지만 최종 정의·정치·지리·어원은 아직 확정하지 않는다.

## 3. 보호할 프로젝트 코어

```text
공세 예고
→ 건설·TokenSource·세 물리 릴 설계
→ 회전·영구 이동·immutable snapshot·확정
→ 보관·판매·한 라인 비가역 배치
→ 세 라인 자동전투·고정시간 점령
→ 정산·인과 복기
```

- 20 Stage·4막·약 35분.
- 위험 Stage 5/10/15/20.
- 30개 건설 노드.
- 금고·농장·타워·병영·지휘소.
- paid Retry 원칙.
- 안내자 벨루.
- PC-primary.

## 4. Profile 영구 성장

정본: `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md`

```text
수평 해금·제한 편의 = 주축
선택형·상한형 준비 보정 = 보조축
무한 능력치 누적 = 금지
```

세계관상 이는 전술 교리·보급망·기록·준비 수준의 축적이다.

## 5. 금지된 해석

```text
APPROVED_PLAN != IMPLEMENTED
WORLD_PRINCIPLE_APPROVED != WORLD_DETAIL_APPROVED
SHEET_SYNCED != RUNTIME_VALIDATED
NO_TIME_LOOP_RESET
NO_ALL_SIMULATION_REVEAL
NO_PROPHECY_DETERMINISM
```

- 베일의 본질을 일반 판타지 관습으로 임의 보충하지 않는다.
- 기존 명칭을 승인 없이 교체하지 않는다.
- 징조를 완전 예언이나 운명 결정으로 만들지 않는다.
- Profile을 직접 공격력 무한 누적으로 확대하지 않는다.

## 6. 세계관 결정 큐

1. `OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1` — 베일의 본질과 세계 경계 상태.
2. 오멘워드·루메른 왕국·지휘관의 조직 및 정치적 위치.
3. 베일종·경계파쇄자의 발생·지성·목적.
4. 징조·세 물리 릴·TokenSource의 세계 내 원리.
5. 트리븐 전선·실베른 성채·베일런 황야의 지리와 역사.
6. 벨루의 종족·기원·관계.
7. 승패가 세계에 남기는 지속 결과.
8. 세계 코어 뒤 `VS-CONTENT-BREADTH` 결정.

## 7. 바로 다음 작업

```text
Grill Me: 베일은 무엇이며 세계와 어떤 관계인가?
```

세계·MapRun Decision의 exact PR HEAD·CI·Sheet 상태는 PR #119와 Sheet `00`, `02`, `11`, `99`에서 확인한다.
