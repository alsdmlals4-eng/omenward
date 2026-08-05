# [현행] OMENWARD 전술스킬·마력·연구 적대적 검토

```yaml
review_id: OMW-REV-20260805-TACTICAL-SKILLS-MANA-RESEARCH-V1
decision_id: OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
status: PASS / REQUIRED_CANON_FIXES_APPLIED
review_scope: RESOURCE / RESEARCH / TOWER / TACTICAL_ROSTER / PRESSURE / UX / LIFECYCLE
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결론

```text
CORE_FIT = STRONG
TACTICAL_ROLE = MOMENTARY_AMPLIFICATION_NOT_REPLACEMENT
RESEARCH_LOOP = COHERENT
PRESSURE_COVERAGE = STRUCTURALLY_VIABLE
DOCUMENT_PR_MERGE_READINESS = PASS
PRODUCT_CODE = UNCHANGED
EXACT_NUMERICS = PENDING_SIMULATION
IMPLEMENTATION_READINESS = BLOCKED_BY_NUMERIC_AND_RUNTIME_PLAN
```

강점:

- 마력탑 연구와 전투 중 수동 시전을 분리해 비용 목적이 명확하다.
- 마력탑 단일 선형 성장으로 중복 연구·중복 수급 상태를 줄인다.
- 4·3·3 구조가 범용 보정·압력 전문·결정 전술의 읽기 쉬운 위계를 만든다.
- Stage 전 편성을 제거해 연구 자체가 해금 선택이 된다.
- 전술이 병종·건물의 지속 역할을 대체하지 않도록 한계를 명시한다.

잔여 한계:

- 정확 수급량·비용·쿨다운·연구시간은 시뮬레이션 전 판정 불가.
- 첫 5 Stage에서 연구 투자와 건설·룰렛 비용의 경쟁이 과도한지 사람 플레이가 필요하다.
- 열 개 해금 후 패널 가독성과 입력 속도는 UX 프로토타입 검증이 필요하다.

## 2. P0 핵심 재미·공정성 공격

### OMW-AUD-444 — RESOURCE_HOARDING_DOMINANCE

- 위험: 플레이어가 모든 마력을 Boss까지 저장해 일반 Stage 전술 사용이 오답이 된다.
- 조치: T1은 저비용·빈번 대응 역할을 가지며 일반 Stage에도 사용 가치가 있어야 한다. 정확 수급·비용 곡선은 사용률과 잔여 마력 분포로 검증한다.

### OMW-AUD-445 — RESEARCH_SNOWBALL

- 위험: 초반 연구가 경제와 전투를 동시에 강화해 선행 플레이어만 계속 앞선다.
- 조치: 연구는 전술 선택지를 해금할 뿐 초당 마력 수급을 직접 높이지 않는다. 수급 증가는 마력탑 Tier가 소유한다.

### OMW-AUD-446 — SINGLE_TOWER_LOCKOUT

- 위험: 유일한 마력탑이 파괴되면 이후 전술 시스템 전체가 영구 봉쇄된다.
- 조치: 파괴 중에는 신규 연구·수급만 중단하고 완료 연구는 유지한다. 재건을 허용하되 비용·시간은 시뮬레이션 대상이다.

### OMW-AUD-447 — REBUILD_DUPLICATION_EXPLOIT

- 위험: 철거·재건으로 연구 완료 보상·초기 마력·진행도를 반복 복제할 수 있다.
- 조치: 연구·해금·보유 마력은 MapRun 상태이며 건물 인스턴스 생성 보상이 아니다. 재건은 복제·초기화 트리거가 아니다.

### OMW-AUD-448 — AUTO_CAST_REGRESSION

- 위험: 편의 기능 명목으로 자동 시전·자동 대상 선택이 재도입돼 플레이어 판단이 사라진다.
- 조치: `AUTO_CAST = FORBIDDEN`; 추천·미리보기는 가능하지만 확정은 플레이어 입력만 허용한다.

### OMW-AUD-449 — T3_PANIC_BUTTON_DOMINANCE

- 위험: T3가 무너진 전선을 완전 복구해 건물·병종·배치 실수를 무효화한다.
- 조치: 결전의 깃발·성역·시간 왜곡은 짧은 기회·생존·지연만 제공하며 부활·완전 회복·전면 정지·전선 이동을 금지한다.

### OMW-AUD-450 — HARD_COUNTER_UNLOCK_DEPENDENCY

- 위험: 특정 전술 미연구 시 FLYING·INFILTRATION Stage가 자동 패배한다.
- 조치: 모든 압력은 병종·건물·전술 중 최소 두 계층 대응을 유지하며 전술은 보조 경로다.

## 3. P1 자원·연구 경제 공격

### OMW-AUD-451 — RESEARCH_CANCEL_REFUND_EXPLOIT

- 위험: 연구 취소를 반복해 골드·시간·상인 타이밍을 악용한다.
- 조치: 환불률·진행 보존은 수치 Gate에 남기되 완전 반복 환불·시간 복제를 금지한다.

### OMW-AUD-452 — MANA_OVERFLOW_INFINITE_STORAGE

- 위험: 상한 초과분·비활성 시간·Stage 전환에서 숨은 마력이 누적된다.
- 조치: 명시적 보유 상한을 사용하고 초과분 저장을 금지한다. Stage 전환은 보유량을 유지하되 새 MapRun에서 초기화한다.

### OMW-AUD-453 — PASSIVE_INCOME_AFKSOLUTION

- 위험: 초당 수급 때문에 안전 구간에서 무한 대기하는 것이 최적해가 된다.
- 조치: Stage 흐름은 무한 대기를 허용하지 않으며 정비시간·전투시간 계약 안에서만 수급한다. 정확 수급 가능 구간은 구현 계획에서 고정한다.

### OMW-AUD-454 — RESEARCH_QUEUE_OVERLOAD

- 위험: 여러 연구를 병렬 진행해 마력탑 하나라는 제한이 무의미해진다.
- 조치: `ONE_CONCURRENT_RESEARCH`; 예약 큐를 도입하더라도 동시 진행은 하나다.

### OMW-AUD-455 — TOWER_UPGRADE_RESEARCH_RACE

- 위험: 업그레이드와 연구가 동시에 완료돼 Tier 권한·비용 판정이 모호해진다.
- 조치: 업그레이드와 연구는 동시 진행하지 않으며 상태 전환 순서를 구현 계약에서 단일화한다.

### OMW-AUD-456 — RESEARCH_CHAIN_FALSE_CHOICE

- 위험: 하위 연구 강제 사슬 때문에 4·3·3 선택이 사실상 고정 순서가 된다.
- 조치: 같은 Tier 연구는 독립적이며 상위 Tier 접근 조건은 마력탑 Tier만 사용한다.

## 4. 압력·전술 역할 공격

### OMW-AUD-457 — FLYING_COVERAGE_GAP

- 위험: 폭풍 억제가 직접 대공 처치를 보장하지 않아 FLYING 대응이 부족할 수 있다.
- 조치: 궁수·비행병·요격 포대가 지속 대응을 소유하고 집중 명령·폭풍 억제는 보조한다.

### OMW-AUD-458 — SIEGE_PERMANENT_CANCEL

- 위험: 파쇄 명령·시간 왜곡으로 공성 행동을 영구 반복 취소한다.
- 조치: 1회 방해·짧은 지연만 허용하고 연속 봉쇄 방지 규칙과 쿨다운·비용을 시뮬레이션한다.

### OMW-AUD-459 — ROUTE_INFORMATION_CHEATING

- 위험: 봉쇄 결계가 숨은 Route를 탐지하거나 비공개 침투를 자동 차단한다.
- 조치: Stage 시작 전에 공개된 Route 구간에만 사용 가능하며 비공개 Route에는 시전할 수 없다.

### OMW-AUD-460 — LAYER_BYPASS_BY_MARK

- 위험: 집중 명령이 도달 불가능한 공중·지상 Layer 공격 권한을 부여한다.
- 조치: 우선 표적만 변경하며 기존 공격 가능 Layer·Route·사거리 권한은 바꾸지 않는다.

### OMW-AUD-461 — CROWD_CONTROL_CHAIN_LOCK

- 위험: 속박진·충격파·폭풍 억제·시간 왜곡을 순환해 적이 행동하지 못한다.
- 조치: 대상 면역·효과 감소·쿨다운·마력 비용 중 적절한 조합을 수치 시뮬레이션에서 검증하고 영구 제어를 Stop-ship으로 둔다.

## 5. UX·상태 공격

### OMW-AUD-462 — TEN_SKILL_PANEL_OVERLOAD

- 위험: 10종 해금 뒤 전술 패널이 과밀해 대상 선택이 늦어진다.
- 조치: T1·T2·T3 분류, 비용·대상·압력 아이콘, 사용 가능 우선 정렬을 제공하되 Stage 전 편성 슬롯은 만들지 않는다.

### OMW-AUD-463 — INVALID_CAST_RESOURCE_LOSS

- 위험: 대상 소멸·Layer 불일치·입력 취소에도 마력이 소비된다.
- 조치: `INVALID_CAST_SPENDS_MANA = FALSE`; 유효 시전 확정 시점에만 비용을 지불한다.

### OMW-AUD-464 — TOWER_DESTRUCTION_STATE_DESYNC

- 위험: 파괴 직전 연구 완료가 클라이언트·로그·실제 해금에서 다르게 판정된다.
- 조치: 완료와 파괴 이벤트의 단일 순서를 구현 계약에 고정하고 해금은 멱등 처리한다.

### OMW-AUD-465 — MAPRUN_RESET_LEAK

- 위험: 새 MapRun에 이전 연구·마력·Tier가 일부 남는다.
- 조치: 새 MapRun 생성 시 마력탑 Tier·진행 연구·완료 연구·해금 목록·보유 마력을 하나의 reset scope로 초기화한다.

## 6. 권위·구형 문서 공격

### OMW-AUD-466 — LEGACY_MASOK_TERM_LEAK

- 위험: 현행 문서와 UI에서 `마석`이 계속 사용돼 자원명이 분열된다.
- 조치: 현행 권위는 `마력`으로 통일하고 `LEGACY_TERM_MASOK / IMPLEMENTATION_INPUT_FORBIDDEN`으로 수명주기에 기록한다.

### OMW-AUD-467 — LEGACY_MANA_TOWER_BRANCH_AUTHORITY_LEAK

- 위험: 3/10의 유량·저장 분기가 새 단일 선형 마력탑과 동시에 구현 입력으로 사용된다.
- 조치: 두 분기를 `[대체됨] LEGACY_MANA_TOWER_BRANCHES`로 표시하고 5/10 정본을 우선한다.

## 7. 병합·구현 판정

```text
DOCUMENT_PR_MERGE_READINESS = PASS
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

문서 PR은 중앙 라우팅·용어 전환·수명주기·Sheet 동기화와 fresh preflight가 통과하면 병합 가능하다. 제품 구현은 수치 시뮬레이션·Codex 구현 계획·제품 RED 테스트 뒤에만 시작한다.
