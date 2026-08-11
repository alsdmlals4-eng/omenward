# [승인] OMENWARD Benchmark & Industry Research First

```yaml
updated_at: 2026-08-11
decision_id: OMW-DEC-20260811-OPS-BENCHMARK-INDUSTRY-RESEARCH-FIRST-V1
status: APPROVED_CURRENT_PROCESS_AUTHORITY
approval_source: USER_EXPLICIT_STANDING_PROJECT_INSTRUCTION
scope: OMENWARD_NON_TRIVIAL_WORK
```

사용자 지시에 따라 앞으로 OMENWARD의 모든 비사소 작업은 **실제 설계·정본 변경·구현 전에 벤치마킹과 현업조사를 먼저 수행**한다.

```text
BENCHMARK_AND_INDUSTRY_RESEARCH_REQUIRED_BEFORE_WORK = TRUE
BENCHMARK_DISPOSITION = ADOPT / ADAPT / AVOID / TEST / IGNORE
COMPETITOR_BEHAVIOR_AUTOMATIC_AUTHORITY = FORBIDDEN
```

## 1. 필수 선행 순서

```text
FRESH_BASE_PROJECT_SHEET_READ
→ TARGETED_BENCHMARK_AND_INDUSTRY_RESEARCH
→ SOURCE_DATE_AND_RELEVANCE_RECORD
→ ADOPT_ADAPT_AVOID_TEST_IGNORE
→ PROJECT_CANON_CONFLICT_CHECK
→ DESIGN_CANON_IMPLEMENTATION_WORK
```

1. Base current main/구조/적용 skill과 OMENWARD main/open PR/current owner, 연결 Sheet를 fresh-read한다.
2. 해당 작업 결정을 실제로 바꿀 수 있는 비교작·현업 관행·공식 문서·플레이어 evidence를 최신 상태로 조사한다.
3. 출처, 조사 날짜, 비교 이유, 프로젝트와의 구조 차이를 기록한다.
4. 각 finding을 `ADOPT / ADAPT / AVOID / TEST / IGNORE` 중 하나로 분류한다.
5. 외부 사례와 OMENWARD 정본이 충돌하면 외부 사례를 자동 채택하지 않고 충돌을 보고한다.
6. 그 뒤에만 설계·정본·Sheet·코드 작업을 시작한다.

## 2. 조사 품질

- 가능하면 공식 제품 페이지, 공식 문서, 개발자 발표, 플랫폼 문서, 원 연구 등 1차 자료를 우선한다.
- 장르/시장/UX/밸런스처럼 현행 상태가 중요한 항목은 최신 사례를 우선한다.
- 단순 인기 순위가 아니라 **현재 작업 질문과 같은 의사결정 구조**를 가진 비교작을 고른다.
- 벤치마킹은 복사가 아니라 프로젝트의 차별화·인과·리스크를 검증하기 위한 stress test다.
- 조사 결과가 기존 승인안을 바꾸지 않는 경우에도 `NO_CHANGE_AFTER_BENCHMARK` 근거를 남긴다.

## 3. 처분 정의

```text
ADOPT = 구조 원칙을 거의 그대로 채택할 가치가 있음
ADAPT = 원리는 유효하지만 OMENWARD 핵심루프에 맞게 변형해야 함
AVOID = OMENWARD 정체성·인과·가드레일과 충돌하므로 피함
TEST = 정본 확정 전 PoC/측정/플레이테스트가 필요함
IGNORE = 현재 결정에 영향이 없으므로 제외
```

## 4. 예외

동일 work item 안의 단순 bounded reread, merge-state propagation, SHA/status 동기화는 그 work item에서 이미 수행한 benchmark packet을 재사용할 수 있다.

긴급 correctness/security remediation은 먼저 최소한의 관련 primary-source/current-practice 검증을 수행한 뒤 수정할 수 있다. 이 예외도 fresh Base/project/Sheet authority read를 면제하지 않으며, 관련 benchmark evidence를 사후가 아니라 같은 work item 안에 기록한다.

```text
TRIVIAL_SAME_WORK_ITEM_READBACK_RESEARCH_REUSE = ALLOWED
EMERGENCY_MINIMAL_TARGETED_RESEARCH_FIRST = ALLOWED
SKIP_ALL_RESEARCH_FOR_NON_TRIVIAL_WORK = FORBIDDEN
```

## 5. OMENWARD 장르 benchmark 기본 세트

제품 방향이나 시스템 설계와 관련된 작업에서는 필요에 따라 다음 비교 축을 다시 fresh-check한다.

- 전략 auto-battler의 formation/counter/readability
- roguelite auto-battler의 run identity와 build causality
- roulette/slot/deckbuilder 계열의 확률 구성 agency
- engine/inventory builder의 pre-combat construction agency
- roguelite meta progression의 horizontal vs vertical power

기본 비교작 목록은 고정 권위가 아니다. 작업 시점의 시장/제품 상태를 다시 조사하며, 더 적합한 비교작이 있으면 교체한다.

## 6. Base 관계

Base current skill과 운영 정본이 공통 방법론 authority다. 이 문서는 프로젝트별 강화 규칙이며 Base를 복제하거나 Base active canon을 직접 수정하지 않는다.

```text
BASE_CURRENT_AUTHORITY = REQUIRED
PROJECT_BENCHMARK_FIRST_ADAPTER = THIS_DECISION
BASE_ACTIVE_CANON_MUTATION = NOT_AUTHORIZED_BY_THIS_DECISION
```
