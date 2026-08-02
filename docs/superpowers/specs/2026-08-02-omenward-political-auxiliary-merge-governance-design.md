# OMENWARD 정치·보조 허브·병합 운영 설계

```yaml
status: USER_APPROVED_DESIGN
approved_decisions:
  - OMW-DEC-20260802-WORLD-OMENWARD-POLITICAL-ROLE-V1
  - OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1
  - OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
product_code_authority: NONE
```

## 1. 목표

1. 오멘워드의 왕실 인가·현장 자율·사후 책임을 세계관 정본으로 고정한다.
2. 메인 화면에 주점·병영·연구 보조 시설과 영구재화 노드 진행을 연결한다.
3. 승인 Grill Me 10건마다 안전한 병합 사전 검증과 main 동기화를 수행한다.

## 2. 책임 분리

| 단위 | 책임 원본 | 핵심 책임 |
|---|---|---|
| 조직·정치 | `APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md` | 왕실 인가, 작전 권한, 금지 권한, 책임 감사 |
| 영구 보조 허브 | `APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md` | 주점·병영·연구, 영구 노드, 영웅 영입, 공정성 경계 |
| 화면 | `APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md` | 메인 허브 정보 위계와 8개 화면 계약 |
| 병합 운영 | `GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md` | 카운트, preflight, blocker, 병합 후 동기화 |
| 결정 라우팅 | `PROJECT_CANON_DECISION_LEDGER.md`, `DOCUMENTATION_MAP.md` | 현재 승인과 다음 Gate |
| 사용자 작업면 | Google Sheet | 결정·분야·감사·변경이력 read-back |

## 3. 데이터·상태 설계

```yaml
ProfileProgressionState:
  settled_permanent_currency_balance: integer_non_negative
  settled_permanent_currency_total: integer_non_decreasing
  unlocked_node_ids: unique_stable_ids
  tavern_recruit_ids: unique_stable_ids
  barracks_training_ids: unique_stable_ids
  research_unlock_ids: unique_stable_ids
  readiness_perk_unlocks: finite_set
  selected_run_loadout_ids: bounded_set
  transaction_receipts: idempotent_ids
```

- balance는 노드와 paid Retry 소비에 사용한다.
- total은 감소하지 않는 milestone 판정에 사용한다.
- 정확 schema·ID·비용은 구현 전 Parameter Registry와 Red test로 고정한다.

## 4. 주요 플레이 흐름

```text
실제 공세 정산
→ 영구재화·기록 귀환
→ 메인 작전 허브
→ 주점/병영/연구 노드 확인
→ 공개 비용과 기회비용 확인
→ 유한 노드 구매
→ 제한된 영웅·교리·연구 선택
→ 다음 MapRun
→ 결과 복기에 활성 Profile 기여 표시
```

## 5. 오류·복구 경계

- 잔액 부족: 구매 차단, 선행 조건과 필요한 차액 표시.
- 중복 receipt: 재차감 없이 기존 결과 반환.
- 저장 실패: 이전 정상 Profile과 journal 보존.
- 노드 정의 누락: 구매 차단, 손상된 ID를 자동 대체하지 않음.
- 영웅·교리 활성 상한 초과: 명시적 교체 선택 요구.
- exact value 없음: 제품 코드·이미지에서 임의 숫자 사용 금지.

## 6. 적대적 검토 결과

- 영웅이 일반 병사를 대체할 위험 → 영입 영구·출전 제한·고유 역할·기본 Profile 완주.
- 세 시설이 메뉴 게임이 될 위험 → MapRun 진입 1순위, 시설은 2차.
- 병영 훈련이 무한 전투력 트리가 될 위험 → 유한 sidegrade, 전 구간 배율 금지.
- 연구가 숨은 확률 조작이 될 위험 → 릴 확률·전 구간 생산 배율 금지.
- Retry와 노드 지갑 충돌 → 공개 기회비용, balance/total 분리, simulation 필수.
- 10건 주기가 안전하지 않은 병합을 강제할 위험 → 주기는 preflight trigger이며 blocker가 있으면 병합 금지.
- 역사 PR의 책임 원본이 current branch에 빠질 위험 → 현재 책임 경로 존재 검사를 병합 blocker로 지정.

## 7. 검증 계획

### 문서·정본

- Decision ID와 책임 경로 존재.
- 최신 사용자 승인과 Ledger·Map·Context 일치.
- 역사 PR 참조와 current authority 구분.
- 제품 코드 변경 0.

### Sheet

- 같은 Decision ID와 exact PR HEAD.
- 분야 행·감사 finding·변경이력 bounded read-back.
- main 병합 뒤 merged SHA 재기록.

### 후속 제품 검증

- P0/P1/P2 Profile trajectory.
- 시설별 채택률·지배 경로·재화 비축·Retry 기회비용.
- 영웅 미보유/보유 동일 seed 성능 차이.
- 저장 transaction fault injection.
- 메인 허브와 노드 그래프 사람 가독성.

## 8. 범위 밖

- 정확 영구재화 명칭·획득량·비용.
- 노드 개수·좌표·아트.
- 영웅 명단·등급명·능력·출전 상한 확정.
- 병영 훈련 목록·연구 목록.
- 제품 코드·Scene·Resource·데이터 구현.

## 9. 자체 검토

```text
PLACEHOLDER_SCAN: PASS — 미확정 항목은 명시적 PENDING이며 구현 요구가 아님
CONTRADICTION_SCAN: PASS — 기존 수평 해금·Readiness·Retry 지갑 계약 유지
SCOPE_SCAN: PASS — 정치·허브·운영을 책임 원본으로 분리
AMBIGUITY_SCAN: PASS — 영입과 출전, 허브 병영과 MapRun 병영을 분리
```
