# OMENWARD 프로젝트 AI 작업 규칙

```yaml
updated_at: 2026-08-06
common_work_authority: alsdmlals4-eng/Base/AGENTS.md
current_decision: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
current_count: 6_OF_10
next_decision: OMW-DEC-20260805-PLANNING-FIRST-10-15-MINUTES-FLOW-V1
work_mode: TOTAL_PLANNING
product_code_authority: NONE
image_generation: STOPPED_BY_USER
parallel_platform_architecture: OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1
parallel_platform_phase2: OMW-DEC-20260806-PC-ANDROID-PHASE2-GAME-SESSION-DECOUPLING-V1
platform_phase2_status: MAIN_CANONICAL
work_entry_gate: REQUIRED_FAIL_CLOSED
work_entry_gate_decision: OMW-DEC-20260806-TOOLS-HIGODOT-GUT-AUTHORITY-AND-WORK-ENTRY-GATE-V1
work_entry_gate_status: BLOCKED_CANON_VENDOR_AND_RUNTIME_RECONCILIATION
work_entry_command: python tools/validate_godot_authoring_test_authority.py --entry
```

공통 작업·검증·TDD·벤치마킹·PR·승인 배치·정본·Sheet 동기화 규칙은 Base 책임 원본만 따른다. 이 파일은 해당 규칙을 재서술하지 않고 OMENWARD 고유의 읽기 순서, 현재 결정, 제품 제약, 구현·검증 상태만 책임진다.

## 0. 필수 작업 진입 Gate

모든 일반 작업은 다음 명령을 먼저 통과해야 한다.

```text
python tools/validate_godot_authoring_test_authority.py --entry
```

현재 Decision Ledger·미확정 목록·Sheet·이미지 검수·GUT vendor/runtime 상태에 차단 요소가 있으므로 일반 제품 작업은 시작하지 않는다. Gate 자체 bootstrap과 명시된 정본·vendor 교정 경로만 exact changed-file allowlist로 허용한다.

권위 경계:

```text
HIGODOT_AUTHORING_AUTHORITY = Scene / Node / Resource / project settings mutation
GUT_TEST_AUTHORITY = discovery / assertion / double / execution / report
MUTATION_AUTHORITY_OVERLAP = FORBIDDEN
```

책임 원본:

- `docs/design/PROPOSED_OMENWARD_HIGODOT_GUT_AUTHORITY_AND_GUT_9_7_1_ADOPTION_2026-08-06.md`
- `docs/operations/OMENWARD_WORK_ENTRY_GATE_2026-08-06.md`
- `docs/operations/GUT_ADOPTION_RECORD.v1.json`
- `docs/operations/WORK_ENTRY_GATE_STATE.v1.json`

## 1. 작업 시작 순서

1. `docs/PROJECT_CORE.md`
2. `docs/ACTIVE_CONTEXT.md`
3. `docs/DOCUMENTATION_MAP.md`
4. `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
5. `docs/OMENWARD_GDD_CURRENT_CANON.md`
6. 현재 Decision 책임 원본과 적대적 검토
7. `docs/CURRENT_IMPLEMENTATION_STATUS.md`

대상 파일이 `[현행]`인지 확인하지 않고 구현 입력으로 사용하지 않는다.

## 2. 현재 6/10 계약

전술·마력 5/10 완료 계약:

```text
자원 = 골드 / 마력 / 배치 병력·병력 한도 / 이동권
마력탑 최대 활성 수 = 1
마력탑 = T1 → T2 → T3
마력탑 분기 = FORBIDDEN
연구 = 골드 + 시간
시전 = 마력
동시 연구 = 1
Stage 전 편성 = 없음
자동 시전 = 금지
새 MapRun = 마력탑 Tier·연구·해금·보유 마력 초기화
```

Stage 종료 상인 6/10 현행 계약:

```text
Stage 1~19 종료 정비시간 방문
Stage 20 상인 = FORBIDDEN
재고 = 룰렛 제어 / 복구 / 성장 보조 / 가변 기회
재고 = 방문별 유한
구매 통화 = 골드
상시 HUD 상점 = FORBIDDEN
무한 구매·무한 reroll = FORBIDDEN
```

- 이동권이 3 미만이면 이동권, 3/3이면 다음 룰렛 1회 할인을 제시한다.
- 병종·T3·Hero·Legendary·전술스킬·마력·건물 분기를 직접 판매하지 않는다.
- 상인은 기존 시스템을 보정하지만 우회하지 않는다.
- 정확 가격·재고·등장률·할인율은 `PENDING_SIMULATION`이다.

## 3. OMENWARD 고유 보호 경계

- 현재 기획 6/10은 문서 정본이며 제품 코드·Scene·Resource·게임 데이터·실제 아트 자산을 자동 승인하지 않는다.
- 사용자가 승인하지 않은 자동화·편성·하드카운터·직접 핵심 보상 판매를 추가하지 않는다.
- 이미지 생성은 사용자 지시에 따라 중단 상태다.
- 정확 수치는 시뮬레이션과 제품 구현 계약 전까지 `PENDING_SIMULATION`을 유지한다.
- 병렬 플랫폼 작업은 Planning Batch 카운터에 포함되지 않는 `NON_COUNTER`다.

## 4. 완료 이력

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10
LEGACY_C1_C2_C3_PROVEN
```

## 5. 플랫폼 출시·에셋 증거

출시 플랫폼과 프로젝트별 자산 증거는 다음 파일을 읽는다.

- `docs/APPROVED_PC_ANDROID_PLATFORM_RELEASE_AUTHORITY_2026-08-05.md`
- `docs/PLATFORM_RELEASE_AND_ASSET_RIGHTS_PROFILE.md`
- `docs/ASSET_RIGHTS_AND_PROVENANCE_RECORD.md`
- `docs/GAME_RELEASE_COMPLIANCE_EVIDENCE_PACK.md`

플랫폼 운영 Decision은 `OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1`이다.

```text
platform_decision = APPROVED_DUAL_PLATFORM
release_strategy = STAGED_CROSS_PLATFORM
PC = COMMITTED
Steam = COMMITTED_PRIMARY_STORE
STOVE = SECONDARY_RELEASE_CANDIDATE
Android = COMMITTED
Google Play = COMMITTED_PRIMARY_STORE
iOS = NOT_CURRENT_SCOPE
simultaneous release = NOT_COMMITTED
COMMON_PLATFORM_GATE = NOT_RUN
PC_RELEASE_GATE = NOT_RUN
MOBILE_RELEASE_GATE = NOT_RUN
RELEASE_BLOCKED_UNVERIFIED
```

자산 감사, 런타임 검증, 상점 제출, 최종 등급, 법률 검토는 현재 `NOT_RUN / NOT_ASSIGNED`다.

## 6. PC·Android 공용 코어·어댑터 상태

```text
ARCHITECTURE_DECISION = OMW-DEC-20260806-PC-ANDROID-CORE-ADAPTER-ARCHITECTURE-V1
PHASE0_DECISION = OMW-DEC-20260806-PC-ANDROID-PHASE0-FREE-LOCAL-V1
PHASE1_DECISION = OMW-DEC-20260806-PC-ANDROID-PHASE1-CONTRACTS-V1
PHASE2_DECISION = OMW-DEC-20260806-PC-ANDROID-PHASE2-GAME-SESSION-DECOUPLING-V1
PHASE2_MAIN = 04e53660387a3bb6d51edd746950cbb6cad8b745
ARCHITECTURE_STATUS = MAIN_CANONICAL
PHASE0_STATUS = MAIN_CANONICAL_LOCAL_PASS
PHASE1_STATUS = MAIN_CANONICAL_LOCAL_PASS
PHASE2_STATUS = MAIN_CANONICAL_LOCAL_PASS
PHASE0_LEGACY_ALLOWLIST = 0
SHARED_SAVE_SCHEMA = NOT_STARTED
PC_ADAPTER_IMPLEMENTATION = NOT_STARTED
ANDROID_ADAPTER_IMPLEMENTATION = NOT_STARTED
STORE_SDK_INTEGRATION = NOT_STARTED
```

제품 구조 책임 원본:

- `docs/design/APPROVED_PC_ANDROID_CORE_ADAPTER_ARCHITECTURE_2026-08-06.md`
- `docs/APPROVED_PC_ANDROID_PHASE0_FREE_LOCAL_BASELINE_2026-08-06.md`
- `docs/APPROVED_PC_ANDROID_PHASE1_CONTRACTS_2026-08-06.md`
- `docs/APPROVED_PC_ANDROID_PHASE2_GAME_SESSION_DECOUPLING_2026-08-06.md`
- `docs/CURRENT_IMPLEMENTATION_STATUS.md`

공용 domain/core의 실제 검사 대상과 실행 명령은 `scripts/platform/README.md`에 기록한다. 전체 프로젝트 runtime·대표 PC/Android build·export는 아직 실행하지 않았다.