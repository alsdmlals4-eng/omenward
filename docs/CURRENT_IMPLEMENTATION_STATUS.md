# [현행] 오멘워드 현재 구현 상태

```yaml
updated_at: 2026-08-06
current_planning_decision: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
current_planning_count: 6_OF_10
latest_planning_status: PR_CANON_TARGET / NOT_IMPLEMENTED
최신 버티컬 슬라이스 구현: `NOT_STARTED`
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: HUMAN_QA_NOT_RUN
parallel_platform_architecture: OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1
```

현재 시스템 연결 기준선은 `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`다.

## 최신 구현 경계

```text
VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED
LATEST_AUTOMATED_CONTRACTS_NOT_RUN
HUMAN_QA_NOT_RUN
CORE_LOCK_NOT_ALLOWED
```

6/10 Stage 종료 상인은 문서 정본이며 다음은 아직 구현되지 않았다.

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

이 C1·C2·C3 증거는 과거 룰렛·전투 목표·핵심 UX 계약 검증 사실만 보존하며 **V2 구현 완료를 뜻하지 않는다**. 최신 6/10 기획이 제품에 구현됐다는 의미도 아니다.

## 6/10 문서 TDD

```text
RED_RUN = 986
RED_RESULT = FAILURE_AS_EXPECTED
RED_EXISTING_CONTRACTS = 55 PASS
RED_NEW_CONTRACTS = 10 FAIL_OR_ERROR
RED_CAUSE = CANON / REVIEW / 6_OF_10_ROUTING / LIFECYCLE_MISSING

GREEN_CANDIDATE_HEAD = 83c1dc0e241c4fd8b04a0e9a5680562f9469bd01
PROJECT_CORE_RUN = 1002 / SUCCESS
GDD_SHEET_RUN = 707 / SUCCESS
OMENWARD_CORE_RUN = 174 / SUCCESS
BASE_V9_RUN = 690 / SUCCESS
SHEET_BOUNDED_READBACK = PASS
REFACTOR = COMPLETE
```

REFACTOR 뒤의 final exact-head 검증·병합 SHA는 PR #141과 Sheet 현재 상태 셀에서 기록한다. 문서 자체에 final SHA를 고정해 self-reference를 만들지 않는다.

## 구현 시작 전 필수 Gate

1. 7/10 첫 10~15분 흐름 재설계.
2. Hero·Legendary와 Meta·Hub 재조정.
3. 전체 Run 콘텐츠·UX·아트 종합 검토.
4. 경제·전술·병종·상인 수치 시뮬레이션.
5. 사용자 승인 Codex 구현 계획.
6. 제품 행동을 재현하는 RED 테스트.
7. 데이터 마이그레이션·롤백·수동 플레이 계획.

## 완료 이력

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10
```

현재 구현 판정은 `VERTICAL_SLICE_NOT_IMPLEMENTED`다.

## PC·Android 공용 코어·어댑터 구현 상태

```text
OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1
APPROVED_DESIGN_NOT_IMPLEMENTED
PRODUCT_CODE_AUTHORITY = NONE
PC_ANDROID_ADAPTER_IMPLEMENTATION = NOT_STARTED
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
EXPORT_PRESETS = ABSENT
REPRESENTATIVE_PC_BUILD = NOT_RUN
REPRESENTATIVE_ANDROID_BUILD = NOT_RUN
STORE_SDK_INTEGRATION = NOT_STARTED
```

현행 프로토타입에는 결정론적 전투·경제·룰렛 서비스가 있지만, 공용 코어와 Godot Scene 조립 경계가 완결되지 않았다. `GameSession`은 frame tick과 Scene/HUD binding을 함께 담당하며, 제품 저장 adapter·모바일 lifecycle adapter·플랫폼 store adapter·재현 가능한 export preset이 없다.

승인된 설계는 다음 구현 순서를 정할 뿐 제품 변경을 승인하지 않는다.

1. 기준선 characterization test와 금지 API 정적 검사.
2. command/event 및 platform contract.
3. `GameSession`의 `GameApplication`·`SessionDriver`·`SceneBinder`·`PlatformBootstrap` 분리.
4. 공유 versioned save schema와 원자 저장 adapter.
5. shared ViewModel, responsive UI, PC/Android 입력 adapter.
6. PC 대표 build와 독립 Gate 증거.
7. Android lifecycle·성능·대표 build와 독립 Gate 증거.
8. offline core 이후 Steam·Google Play adapter. STOVE는 별도 Gate.

책임 원본은 `docs/design/APPROVED_PC_ANDROID_CORE_ADAPTER_ARCHITECTURE_2026-08-06.md`다. 구현 시작 전 별도 제품 Decision, 제품 RED 테스트, 데이터 마이그레이션·롤백·수동 QA 승인이 필요하다.
