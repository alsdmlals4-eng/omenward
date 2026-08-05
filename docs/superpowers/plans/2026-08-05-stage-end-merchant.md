# OMENWARD Stage 종료 상인 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 승인된 6/10 Stage 종료 상인 설계를 문서 정본·자동 검증·Google Sheet에 같은 Decision ID로 반영한다.

**Architecture:** 상인은 Stage 1~19 종료 정비시간에만 등장하는 4칸 유한 재고 서비스로 정의한다. 제품 코드와 수치는 건드리지 않고, 문서 계약 테스트가 책임 원본·중앙 라우팅·수명주기·제품 경계를 검증하게 한다.

**Tech Stack:** Markdown authority documents, Python 3.12 unittest contracts, GitHub Actions, Google Sheets bounded synchronization.

## Global Constraints

- Decision ID: `OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1`.
- Planning count: `6_OF_10`.
- Stage 1~19 종료 뒤 상인 방문, Stage 20 종료 뒤 상인 금지.
- 상시 HUD 상점·전투 중 재진입·무한 구매·무한 reroll 금지.
- 재고 4칸: 룰렛 제어·복구·성장 보조·가변 기회.
- A 슬롯은 이동권이 3 미만이면 이동권, 3/3이면 다음 룰렛 1회 할인.
- 병종·T3·Hero·Legendary·전술스킬·마력 직접 판매 금지.
- 구매 통화는 골드 하나.
- 정확 가격·재고 수·등장률·할인율은 `PENDING_SIMULATION`.
- 제품 코드·Scene·Resource·게임 데이터 변경 금지.

---

### Task 1: 문서 계약 RED

**Files:**
- Create: `tests/python/test_stage_end_merchant_canon.py`
- Modify: `.github/workflows/validate-project-core-docs.yml`

**Interfaces:**
- Consumes: 승인 Spec과 기존 중앙 권위 문서.
- Produces: 상인 정본·리뷰·6/10 라우팅 부재를 검출하는 실패 계약.

- [ ] 신규 테스트에서 책임 원본·적대적 검토·4칸 재고·Stage 20 예외·금지 상품·6/10 중앙 라우팅을 요구한다.
- [ ] 문서 검증 워크플로의 path filter·compile·unittest 목록에 테스트를 등록한다.
- [ ] PR exact HEAD의 Actions를 읽어 신규 테스트만 예상 실패하고 기존 계약은 유지되는지 확인한다.
- [ ] RED run 번호와 실패 원인을 기록한다.

### Task 2: 상인 책임 원본과 적대적 검토 GREEN

**Files:**
- Create: `docs/design/APPROVED_OMENWARD_STAGE_END_MERCHANT_2026-08-05.md`
- Create: `docs/reviews/ADVERSARIAL_STAGE_END_MERCHANT_ECONOMY_AND_INVENTORY_REVIEW_2026-08-05.md`

**Interfaces:**
- Consumes: 승인 Spec과 RED 계약.
- Produces: 상인 역할·재고·경제·거래·예외의 현행 책임 원본과 감사 `OMW-AUD-468~491`.

- [ ] Stage 1~19 방문과 Stage 20 최종 정산 예외를 명시한다.
- [ ] 4칸 슬롯과 상태 기반 대체 규칙을 명시한다.
- [ ] 허용·금지 상품, 유한 재고, 골드 기회비용, 할인 소멸을 명시한다.
- [ ] 적대적 검토에서 필수 구매·경제 스노우볼·죽은 슬롯·직접 해금·중복 구매·저장 복제·최종 Stage 상인 회귀를 공격한다.
- [ ] 정확 수치와 제품 구현은 승인하지 않는다.
- [ ] 테스트를 다시 실행해 책임 원본 단계의 GREEN 범위를 확인한다.

### Task 3: 중앙 권위와 수명주기 동기화

**Files:**
- Modify: `README.md`
- Modify: `AGENTS.md`
- Modify: `docs/PROJECT_CORE.md`
- Modify: `docs/ACTIVE_CONTEXT.md`
- Modify: `docs/DOCUMENTATION_MAP.md`
- Modify: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
- Modify: `docs/OMENWARD_GDD_CURRENT_CANON.md`
- Modify: `docs/DECISIONS_PENDING.md`
- Modify: `docs/OMENWARD_ROADMAP.md`
- Modify: `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- Modify: `docs/HANDOFF_CONTEXT.md`
- Modify: `docs/PROJECT_CANON_DECISION_LEDGER.md`
- Modify: `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`

**Interfaces:**
- Consumes: 상인 책임 원본과 리뷰.
- Produces: 현재 Decision 6/10과 다음 Decision 7/10을 가리키는 중앙 라우팅.

- [ ] 5/10 전술 결정은 완료 이력으로 보존한다.
- [ ] 현재 Decision·count·책임 원본·다음 Gate를 6/10으로 전환한다.
- [ ] 기존 Stage·건물·병종·전술·Legacy C1/C2/C3 계약을 삭제하지 않는다.
- [ ] 상시 상점·무한 재고·직접 병종/전술 판매를 폐기 또는 금지 상태로 기록한다.
- [ ] 전체 문서 계약을 실행해 Green을 확인한다.

### Task 4: Google Sheet 동기화

**Files:**
- Modify: linked Google Sheet only.

**Interfaces:**
- Consumes: exact PR HEAD, Decision ID, 책임 원본, 감사 범위, CI 증거.
- Produces: 6/10 운영 미러와 bounded read-back 증거.

- [ ] 다음 빈 행을 bounded read로 확인한다.
- [ ] 현재 상태·작업순서·확정결정·근거·감사·GDD·핵심루프·조작·핵심시스템·메인콘텐츠·변경이력에 같은 Decision ID를 기록한다.
- [ ] 과거 행을 덮어쓰지 않는다.
- [ ] exact HEAD·6/10·4칸 재고·Stage 20 예외·감사 `468~491`·다음 Gate를 bounded read-back으로 확인한다.

### Task 5: REFACTOR와 최종 preflight

**Files:**
- Modify: `docs/superpowers/plans/2026-08-05-stage-end-merchant.md`
- Modify: 필요한 중앙 상태 문서.

**Interfaces:**
- Consumes: RED/GREEN·Sheet·review 증거.
- Produces: 병합 가능한 증거 중심 실행 기록.

- [ ] 계획 체크리스트를 실제 run·HEAD·Sheet 범위 중심 완료 기록으로 압축한다.
- [ ] placeholder·중복 marker·구형 상시 상점 권위 누출을 제거한다.
- [ ] final exact HEAD에서 CI 4종 Green을 확인한다.
- [ ] behind main 0, 제품 경로 0, 리뷰·미해결 thread·Sheet blocker·미완성 placeholder 0을 확인한다.
- [ ] PR 본문을 최종 증거로 갱신하고 ready 전환한다.
- [ ] exact HEAD 보호 조건으로 squash merge한다.
- [ ] 병합 main SHA를 Sheet에 기록하고 post-merge bounded read-back을 수행한다.

## Next Gate

`OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1 / 7_OF_10`
