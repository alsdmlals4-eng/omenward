# OMENWARD Stage 종료 상인 실행 기록

```yaml
decision_id: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
branch: gpt/omenward-stage-end-merchant-spec-20260805
pull_request: 141
status: BRANCH_WORK_COMPLETE / READY_FOR_FINAL_PREFLIGHT
planning_counter: 6_OF_10
product_code: UNCHANGED
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 목표

승인된 Stage 종료 상인 설계를 현행 책임 원본으로 만들고, 문서 계약을 TDD로 검증하며, 중앙 권위와 Google Sheet를 같은 Decision ID로 동기화한다. 제품 코드·Scene·Resource·게임 데이터·정확 가격·재고·등장률·아트 자산은 변경하지 않는다.

## 확정된 계약

```text
MERCHANT_VISIT_STAGES = 1_TO_19
STAGE_20_MERCHANT = FORBIDDEN
STAGE_20_NEXT = MAPRUN_FINAL_SETTLEMENT
TOTAL_MERCHANT_SLOTS = 4
VISIT_STOCK = FINITE
PURCHASE_CURRENCY = GOLD_ONLY
```

```text
A = 룰렛 제어
B = 복구 서비스
C = 성장 보조
D = 가변 기회
```

```text
이동권 < 3 → 보관형 이동권
이동권 = 3 → 다음 룰렛 1회 골드 할인
```

## 실행 결과

- [x] 권장 4칸 상인 Spec 작성·사용자 검토·최종 승인.
- [x] 이동권 3/3에서 보장 슬롯이 죽는 문제를 발견해 룰렛 1회 할인 대체 규칙 추가.
- [x] `tests/python/test_stage_end_merchant_canon.py` 작성 및 문서 CI 등록.
- [x] RED run 986에서 상인 정본·리뷰·6/10 라우팅·Legacy 상점 격리 부재를 예상대로 검출.
- [x] RED 단계에서 기존 문서·CI·건물·병종·전술 계약 55개 통과 확인.
- [x] Stage 종료 상인 책임 원본과 적대적 검토 `OMW-AUD-468~491` 작성.
- [x] README·AGENTS·Project Core·GDD·Documentation Map·Lifecycle·Pending·Roadmap·Implementation Status·Handoff·Decision Ledger·Sheet 계약을 6/10으로 동기화.
- [x] 상시 HUD 상점·무한 재고·직접 핵심 보상 판매를 `[대체됨] / IMPLEMENTATION_INPUT_FORBIDDEN`으로 격리.
- [x] 3/10·4/10·5/10 및 Legacy C1/C2/C3 완료 증거 보존.
- [x] Google Sheet에 Decision 6/10, 근거 `094~098`, 감사 `468~491`, 시스템·콘텐츠·변경 이력을 신규 행으로 기록.
- [x] 감사 탭 행 수를 520으로 확장하고 과거 행을 덮어쓰지 않음.
- [x] Sheet bounded read-back에서 Decision ID·exact HEAD·6/10·4칸 재고·Stage 20 예외·감사 범위·다음 Gate 일치 확인.
- [x] candidate HEAD `83c1dc0e241c4fd8b04a0e9a5680562f9469bd01`에서 CI 네 종 Green 확인.

## TDD 증거

```text
RED
Validate Project Core Documentation run 986
result = FAILURE_AS_EXPECTED
existing_contracts = 55 PASS
cause = MERCHANT_CANON / REVIEW / 6_OF_10_ROUTING / LEGACY_SHOP_LIFECYCLE_MISSING

GREEN CANDIDATE
Validate Project Core Documentation run 1002
Validate Omenward GDD Sheet Adoption run 707
Validate Omenward Core run 174
Validate Base v9 adoption run 690
result = SUCCESS
```

## REFACTOR

- 긴 실행 체크리스트를 실제 RED·GREEN·Sheet 증거 중심 기록으로 압축했다.
- 이동권 보장 상품을 고정 아이템이 아닌 상태 기반 룰렛 제어 슬롯으로 정리했다.
- 현행 6/10 상태와 3/10·4/10·5/10·Legacy 증거를 분리했다.
- 과거 HUD·상인 개요 전체를 파괴적으로 교체하지 않고 lifecycle precedence로 상인 부분만 대체했다.
- Sheet 과거 행을 보존하고 신규 6/10 행만 추가했다.
- 제품 코드·Scene·Resource·게임 데이터·실제 아트 자산은 변경하지 않았다.

## Sheet 기록 범위

```text
00_프로젝트_허브!E2:L2
01_작업순서!A57:L57
02_현재_확정결정!A64:M64
03_근거_라이브러리!A94:J98
04_누락_충돌_감사!A468:H491
05_GDD_요약!A16:J17
12_핵심루프!A37:J37
15_조작_게임규칙!A40:J40
40_핵심시스템_메인콘텐츠!A40:J40
50_메인콘텐츠!A47:J47
99_변경이력!A74:H74
```

## 최종 preflight 계약

REFACTOR와 증거 갱신으로 HEAD가 변경됐으므로 다음을 새 exact HEAD에서 다시 확인한다.

```text
CI 4종 Green
behind main = 0
changed product paths = 0
reviews addressed
unresolved threads = 0
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
unfinished TODO/TBD = 0
Sheet exact-head bounded read-back = PASS
```

검증이 통과하면 PR #141을 ready로 전환하고 exact HEAD 보호 조건으로 squash merge한다. 병합 뒤 현재 6/10 Sheet 상태만 merged main SHA로 갱신한다.

## 제품 경계

```text
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 다음 Gate

```text
OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
7_OF_10
```
