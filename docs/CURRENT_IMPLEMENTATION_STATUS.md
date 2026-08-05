# [현행] 오멘워드 현재 구현 상태

```yaml
updated_at: 2026-08-05
current_planning_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
current_planning_count: 7_OF_10_IN_PROGRESS
latest_planning_status: PARTIAL_APPROVAL_1_OF_10 / DRAFT_PR / NOT_IMPLEMENTED
최신 버티컬 슬라이스 구현: `NOT_STARTED`
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: HUMAN_QA_NOT_RUN
```

현재 시스템 연결 기준선은 `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`다.

## 최신 구현 경계

```text
VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED
LATEST_AUTOMATED_CONTRACTS_NOT_RUN
HUMAN_QA_NOT_RUN
CORE_LOCK_NOT_ALLOWED
```

## 7/10 부분 승인 — 아직 미구현

```text
OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
7_OF_10_IN_PROGRESS
PARTIAL_APPROVAL_1_OF_10
ONBOARDING_FORMAT = IN_RUN_PROGRESSIVE_DISCLOSURE
FIRST_SESSION = REAL_MAPRUN
SEPARATE_TUTORIAL = FORBIDDEN
FULL_SYSTEM_DUMP_AT_STAGE_1 = FORBIDDEN
RULE_PARITY_WITH_MAIN_RUN = REQUIRED
SCRIPTED_VICTORY = FORBIDDEN
BELU_REPLACES_PLAYER_CHOICE = FORBIDDEN
```

현재 제품에는 다음이 구현되지 않았다.

- 실제 MapRun 단계 노출형 온보딩 상태머신.
- 목표별 패널 강조·비모달 벨루 안내·재확인 툴팁.
- 온보딩 진행·저장·복구·스킵·재학습.
- 실패 원인 설명과 다음 선택 연결.
- Danger·Boss·상인의 첫 노출.
- 사람 플레이 검증 로그와 Stop-ship 계측.

시스템 노출 순서·최소 유효 경로·Danger/Boss/상인 노출·실패 규칙·정확 시간은 `PENDING_GRILLME`이므로 구현 입력으로 사용할 수 없다.

## 완료된 6/10 상인 — 아직 미구현

- Stage 1~19 종료 상인 방문·Stage 20 최종 정산 예외.
- 4칸 재고 생성과 상태 유효성 필터.
- 이동권 3/3 시 룰렛 할인 대체.
- 수리 대상 선택과 연구 가속 대상 선택.
- 골드 차감·상품 적용·재고 소모의 멱등 거래.
- 할인 소멸·중첩 방지·checkpoint 복구.
- 상품 가격·재고 수·등장률·Act별 후보 가중.
- 상인 화면·구매 확인·사용 불가 이유·다음 Stage 요약 UX.

5/10 전술·마력 역시 제품에는 구현되지 않았다.

```text
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = NOT_AUTHORIZED
ANIMATION_HX = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
```

## 과거 자동 검증 증거

```text
LEGACY_C1_C2_C3_PROVEN
LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
LEGACY_C2_BATTLE_OBJECTIVE_REMOTE_PROVEN
LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN
```

C1 구현 검증 head: `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9`

C1 최종 검증 run: `29926598807`

C2 최종 검증 run: `29938742864`

이 C1·C2·C3 증거는 과거 룰렛·전투 목표·핵심 UX 계약 검증 사실만 보존하며 **V2 구현 완료를 뜻하지 않는다**. 최신 7/10 기획이 제품에 구현됐다는 의미도 아니다.

## 6/10 문서 TDD·병합 증거

```text
RED_RUN = 986
RED_RESULT = FAILURE_AS_EXPECTED
RED_EXISTING_CONTRACTS = 55 PASS
PR = 141
MERGED_MAIN = 6b23ca2bb627827651a42ba6db01829e44ee8a14
SHEET_POST_MERGE_BOUNDED_READBACK = PASS
```

## 7/10 문서 TDD

```text
RED_TEST_COMMIT = 4c90e02b8ef1fbfae04bd6ea59fc50dffc108664
RED_CI_WIRING_COMMIT = 704da9d09427baa8bdc2e11298867611c050b9ba
RED_RESULT = PENDING_FRESH_RUN_CONFIRMATION
GREEN = NOT_YET_PROVEN
REFACTOR = NOT_YET_PROVEN
```

문서 자체에 final SHA를 고정해 self-reference를 만들지 않는다. exact-head 검증과 최종 병합 SHA는 PR과 Sheet 상태 셀이 소유한다.

## 구현 시작 전 필수 Gate

1. 7/10 첫 10~15분 흐름의 남은 GrillMe 승인.
2. 7/10 적대적 검토와 사람 QA 계획 완료.
3. Hero·Legendary와 Meta·Hub 재조정.
4. 전체 Run 콘텐츠·UX·아트 종합 검토.
5. 검토 완료 뒤 필요한 이미지·애니메이션·HX 승인.
6. 경제·전술·병종·상인 수치 시뮬레이션.
7. 사용자 승인 Codex 구현 계획.
8. 제품 행동을 재현하는 RED 테스트.
9. 데이터 마이그레이션·롤백·수동 플레이 계획.

현재 구현 판정은 `VERTICAL_SLICE_NOT_IMPLEMENTED`다.
