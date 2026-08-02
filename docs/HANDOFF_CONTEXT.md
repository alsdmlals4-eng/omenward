# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: META_PROGRESSION_SYNC_AND_NEXT_GRILL_ME
recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-META-PROGRESSION-ROLE-V1
baseline_main: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
working_branch: gpt/omenward-canon-recovery-20260802
recovery_pr: 119_DRAFT
superseded_pr: 116_CLOSED_NOT_MERGED
base: 9.4.0_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: APPROVED_NOT_IMPLEMENTED
product_code_authority: NONE
codex: BLOCKED
sheet_sync: PENDING_META_DECISION_SYNC
ci_validation: PREVIOUS_HEAD_3_GREEN / CURRENT_HEAD_PENDING
```

## 1. 가장 먼저 알아야 할 것

1. 오멘워드는 건물과 TokenSource로 세 물리 릴의 미래 배열을 설계하고, 당첨 병력을 세 전선 중 하나에 비가역 배치하는 전략 오토배틀이다.
2. 주 플랫폼은 PC다. 모바일은 후속 고려이며 현재 구현 범위가 아니다.
3. 현재 `main`은 Base v9.4 운영 계약을 채택했다.
4. PR #116은 역사적 승인 근거로만 보존되고 닫혔으며 병합되지 않았다.
5. PR #119가 현재 정본 복구·총기획 Draft PR이다.
6. 최신 기획은 제품에 구현되지 않았다. 실제 제품은 Legacy 9칸 룰렛·3건물·capture_power·무료 Stage retry다.
7. 첫 Grill Me에서 Profile 영구 성장 역할이 사용자 승인됐다.
8. 상세 수치는 `RECOMMENDED_DEFAULT/TEST_VALUE`로 제시하고 simulation·playtest·사용자 승인 뒤 제품값으로 승격한다.
9. 중요한 기획 충돌만 Grill Me로 한 번에 하나씩 결정한다.
10. 한 Decision이 승인되면 GitHub와 Sheet를 같은 ID·commit으로 동기화한 뒤 다음 질문으로 간다.

## 2. 보호할 프로젝트 코어

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

## 3. 승인된 Profile 영구 성장

정본: `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md`

```text
수평 해금·제한 편의 = 주축
선택형·상한형 준비 보정 = 보조축
무한 능력치 누적 = 금지
```

- 기본 Profile로 전체 콘텐츠 완료 가능.
- 수평 해금은 sidegrade.
- 제한된 시작 보관 편의 허용.
- 한 MapRun에 준비 보정 하나만 장착.
- 준비 보정은 유한 랭크·초반 한정.
- 유닛 전투 배율·전 구간 생산 배율·릴 확률 조작·무한 prestige 누적 금지.
- Retry는 spendable balance를 소비하고 준비 보정은 누적 정산 milestone으로 해금하는 구조를 권장.
- 정확 효과량·milestone·비용은 미확정.

권장 준비 보정 후보:

1. 재정 준비 — 시작 자원 또는 1회성 준비 자원.
2. 군수 준비 — 시작 식량 한도 또는 배치 여유.
3. 방어 준비 — 본진 1회성 보호막·회복 여유.

## 4. 권위 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ docs/BASE_RULES_VERSION.md
→ docs/DOCUMENTATION_MAP.md
→ docs/PROJECT_CORE.md
→ docs/PROJECT_CANON_DECISION_LEDGER.md
→ docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md
→ docs/CURRENT_IMPLEMENTATION_STATUS.md
→ docs/ACTIVE_CONTEXT.md
→ 관련 분야 정본·Sheet
→ 실제 code/data/Scene/tests
```

## 5. 적대적 검토 결과

### 해결됨

- 수평 성장의 약한 체감 → 제한된 준비 보정 추가.
- 영구 능력치 노가다 위험 → 한 런 1개·유한 랭크·초반 한정.
- Retry와 전투력 구매 충돌 → milestone 해금과 spendable balance 분리.
- 수평 해금의 숨은 상위 호환 → sidegrade 검증 의무.

### 테스트 필요

- P0 기본 / P1 수평 / P2 혼합 최고 Profile 100K 비교.
- full-run 승률·Act 1 clear rate·실패 seed·지배 전략.
- 성장 체감·노가다 강제감·실패 귀인 사람 검증.
- save/retry fault injection.

## 6. 사용자 결정 큐

1. `OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1` — 세계·세력·플레이어 동기와 20 Stage 반복의 연결.
2. `OMW-DEC-20260802-VS-CONTENT-BREADTH-V1` — 10병종·20전문화의 완성형 데모 대표 범위.

## 7. 조사·테스트 큐

- 룰렛 통제감 사람 검증.
- Profile 포함 100K 경제·Retry·save simulation.
- save/retry fault injection.
- 위험 Stage 인지 부하.
- 35분 런 피로도.
- 해상도·접근성 검증.

## 8. 금지된 해석

```text
APPROVED_PLAN != IMPLEMENTED
USER_APPROVED_ROLE != USER_APPROVED_EXACT_VALUES
RECOMMENDED_GUARDRAIL != PRODUCT_VALUE
SHEET_SYNCED != RUNTIME_VALIDATED
```

- 제품 코드·Scene·Resource·data·asset을 변경하지 않는다.
- Profile 영구 성장 승인을 직접 공격력 트리 승인으로 확대하지 않는다.
- 한 런 1개·유한 랭크·초반 한정 경계를 조용히 제거하지 않는다.
- 실행하지 않은 runtime·simulation·human 검증을 통과로 기록하지 않는다.

## 9. 바로 다음 작업

```text
Meta Decision GitHub·Sheet 동일 ID 동기화·재조회
→ Grill Me #2: 세계·플레이어 동기와 20 Stage 반복
```

동기화 완료 전 다음 Grill Me를 확정 Decision으로 진행하지 않는다.
