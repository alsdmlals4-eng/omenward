# 오멘워드 Legacy 테스트 보존·교체·폐기 판정표

- 결정 ID: `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1`
- 작성일: `2026-08-01`
- 상태: `CURRENT_MIGRATION_TEST_AUTHORITY / PLANNING_ONLY`
- 제품 코드·테스트 코드 변경: `NONE`
- 실제 테스트 실행: `NOT_RUN`

이 문서는 기존 테스트를 통째로 신뢰하거나 통째로 폐기하는 오류를 방지한다. 판정 단위는 파일과 그 안의 행동 계약이다.

## 1. 판정 용어

| 판정 | 의미 |
|---|---|
| `PRESERVE` | 최신 구조에서도 동일한 행동 계약으로 유지 |
| `PRESERVE_SEAM` | 구현은 교체하지만 경계·resolver·결정성 계약은 유지 |
| `SPLIT_REPLACE` | 한 파일 안의 일부는 보존하고 일부는 최신 계약으로 교체 |
| `RETIRE_AS_CURRENT_GATE` | 역사 증거는 보존하지만 최신 제품 통과 게이트에서 제거 |
| `ARCHIVE_EVIDENCE` | 실행 대상이 아니라 과거 proof로만 유지 |
| `EXTEND` | 기존 게이트를 유지하고 최신 테스트를 추가 |

## 2. Godot headless 제품 테스트 판정

### `tests/headless/phase_0_contract_test.gd`

**판정: `PRESERVE`**

보존:

- 공용 병종 데이터와 진영 시각 데이터 분리
- enemy 전용 전투 프로필 금지
- bootstrap registry 검증
- 동일 seed의 manifest 결정성
- 신규 manifest의 빈 input log

보완:

- 최신 20 Stage manifest와 MapRun schema를 별도 테스트로 추가
- 정확히 10개 공용 archetype은 현재 Vertical Slice 범위에서 유지하되 Tier 1·Tier 2·Tier 3 데이터 검증은 신규 테스트가 소유

### `tests/headless/scene_contract_test.gd`

**판정: `SPLIT_REPLACE`**

보존:

- Scene load·instantiate 실패 방지
- 공유 Unit Scene 사용
- 적 전용 Unit Scene 금지
- runtime service binding 경계

교체:

- `main.tscn`이 Battlefield·StageHud·StageSelect를 직접 포함해야 한다는 Legacy 조립 계약
- 현재 무료 `retry_stage()`를 제품 재시도 증거로 보는 assertion
- 제품 메인·Stage 준비·전투·정산·패배 화면은 Screen Board V2와 구현 Plan 이후 별도 계약으로 작성

### `tests/headless/stage_data_contract_test.gd`

**판정: `SPLIT_REPLACE`**

보존:

- Resource load와 bootstrap validation
- 허용 faction/team/lane ID 검증
- manifest JSON 결정성·필수 필드
- spawn data가 공용 archetype을 참조하는 계약

교체:

- tutorial 4 waves + regular stage 내부 W1~W20 구조
- W15/W20을 단일 regular stage의 wave index로 해석하는 계약

최신 교체:

- MapRun에 Stage 1~20이 존재
- 위험 Stage 5·10·15·20
- Stage별 assault package·mission·checkpoint 필드
- 같은 seed에서 Stage manifest 재현

### `tests/headless/roulette_contract_test.gd`

**판정: `PRESERVE_SEAM + SPLIT_REPLACE`**

보존:

- 중앙 판정선 실패 시 다른 줄 무시
- X 무보상
- 1/2/3~7/8 완성선 등급 resolver
- 금화 75/200/500%와 floor
- 동일 snapshot 후보·seed의 source 선택 결정성

교체:

- 단순 9 symbol board가 권위 입력인 구조
- live 물리 릴 없이 resolver만으로 전체 회전을 증명하는 구조
- 전설 제한을 Stage 또는 Legacy 전역 상태로 처리하는 부분

신규 테스트:

- 세 물리 릴·TokenInstance·cursor·wrap
- source-bound token 추가·제거
- 영구 가로 이동
- immutable SpinSnapshot
- 5 Stage 위험 주기당 전설 1회
- 확정 idempotency

### `tests/headless/economy_roulette_test.gd`

**판정: `SPLIT_REPLACE`**

보존:

- 건설·회전·배치가 승인 입력 로그를 남김
- 동일 상태·seed 결과 결정성
- 배치 성공 시 food 예약
- 실패 배치는 추가 food를 소비하지 않음
- TokenSource가 아닌 건물은 병종 토큰을 공급하지 않음

교체:

- `front_a/front_b/rear`가 제품 노드 계약이라는 가정
- 병영·타워·농장 3종만 존재
- 가중치 entry가 물리 토큰을 대체
- `spin()`이 직접 9칸 결과를 생성하는 계약
- 현재 exact 시작 골드·food·수입을 최신 수치로 고정하는 assertion

신규 테스트:

- 30노드 topology
- 금고·농장·타워·병영·지휘소 5종
- 금고·병영의 세 릴 TokenSource
- 정확한 경제값은 시뮬레이션 승인 뒤 별도 데이터 테스트

### `tests/headless/stage_run_test.gd`

**판정: `SPLIT_REPLACE`**

보존:

- 핵심 Script load·instantiate false-pass 방지
- PendingReward가 있으면 새 spin을 비용 없이 차단
- 보상 배치 성공 시 저장 제거·food 예약
- 일반 유닛이 같은 라인에서 행동하는 seam
- assassin same-lane bypass의 독립 행동 계약은 해당 병종이 최신 콘텐츠에 유지되는 범위에서 보존

교체:

- tutorial 승리로 regular stage 하나를 unlock
- 한 Stage 안에서 W1~W20 진행
- W15 legendary/W20 mythic를 최신 20 Stage 구조로 오인하는 계약
- 현재 무료 retry seam을 제품 retry로 사용

신규 테스트:

- MapRun Stage 1~20
- Stage checkpoint persistence
- 보관·판매·비가역 배치
- paid retry와 development retry 분리

### `tests/headless/battle_simulation_test.gd`

**판정: `SPLIT_REPLACE`**

보존:

- 공용 전투 수치와 faction visual 분리
- 일반 병력 라인 격리
- gate 구조 피해와 collapse 시간
- 같은 seed·입력의 battle snapshot 결정성
- contested 시 점령 진행 정지
- 점령 부재 시 즉시 초기화하지 않는 hold/reversion 개념

교체·폐기:

- `capture_power`가 병종별 점령 속도를 결정
- 0.5/1.25/2.0 fractional capture scaling
- 유닛 수 합산으로 점령 시간 단축

최신 교체:

- 유닛 수·Tier·등급·병종과 무관한 고정시간 점령
- 중앙 접전지 기본 8초
- 데이터화된 hold/reversion
- 같은 tick 점령 완료→contested 원자 순서

### `tests/headless/c2_battle_objective_test.gd`

**판정: `SPLIT_REPLACE`**

보존:

- 하나의 전장과 3라인의 독립 진행
- 동일 라인 구조물 공격과 다른 라인 gate 비오염
- 자연 본진 파괴 승패
- contested freeze
- 거점 소유권 변화가 경제·건물 효과에 연결되는 개념

교체:

- giant 수와 `capture_power`로 접전지·거점을 빠르게 점령
- `front_a/front_b/rear` node ID를 제품 구조로 고정
- 점령 시 기존 건물을 일괄 `RUINED` 처리
- 현재 tutorial/regular Stage result wiring

최신 교체:

- 고정시간 점령
- 본진 6·거점당 3·접전지 0·전체 30
- 호환 이전/비호환 BLOCKED 원자 거래
- MapRun Stage result와 checkpoint

### `tests/headless/c3_core_ux_test.gd`

**판정: `PRESERVE_SEAM + SPLIT_REPLACE`**

보존:

- snapshot 조회가 read-only
- 동일 상태에서 snapshot 결정성
- UX service가 domain 계산을 소유하고 HUD가 계산하지 않음
- staged omen 정보 공개
- tactical counter/target/range surface
- 실제 사건 기반 wave/cause report
- script instantiation false-pass 방지

교체:

- `X_WEIGHT/GOLD_WEIGHT`와 source weight ledger가 최신 릴 권위 데이터라는 가정
- `lumern_middle:rear`와 home alias에 묶인 construction comparison
- Label node 존재만으로 제품 HUD를 증명하는 부분

최신 교체:

- 전체 physical reel order·cursor·visible 3×3·token source ledger
- 30노드 construction comparison
- 건물→token→snapshot→reward→배치→전투 인과 report
- 제품 화면 가독성은 Runtime·사람 QA로 분리

## 3. Python validator·contract 판정

### `tools/validate_c1_roulette.py` + `tests/python/test_c1_roulette_contract.py`

**판정: `RETIRE_AS_CURRENT_GATE / ARCHIVE_EVIDENCE`**

보존할 논리:

- active 문서의 폐기 Work Order 참조 검사
- 중앙 판정·등급·금화 resolver 회귀 문구
- false-pass 방지

교체 이유:

- 특정 과거 commit/run 문구를 현재 통과 조건으로 강제
- `resolve_board_snapshot` Legacy 구조를 전체 C1 완료로 간주
- 물리 릴·이동·snapshot 거래를 검사하지 않음

조치:

- 최신 validator에서 repository boundary와 preserve seam만 재작성
- 과거 proof SHA/run은 감사 문서에 남기고 제품 gate에서 제거

### `tools/validate_c2_battle_objective.py` + `tests/python/test_c2_battle_objective_contract.py`

**판정: `RETIRE_AS_CURRENT_GATE / SPLIT_REPLACE`**

보존할 논리:

- 자연 승패·라인 격리·CI 통합·broken link 검사
- 임시 finalizer/workflow 잔존 금지

교체 이유:

- `capture_power`, fractional capture, Legacy outpost API를 승인 계약으로 강제
- 특정 proof phrase·run 번호를 현재 제품 gate로 사용

### `tools/validate_c3_core_ux.py` + `tests/python/test_c3_core_ux_contract.py`

**판정: `SPLIT_REPLACE`**

보존할 논리:

- read-only snapshot API
- HUD의 domain 계산 금지
- 타입 명시와 script instantiation
- timeout·통합 workflow·임시 산출물 금지
- Legacy proof와 최신 제품 상태 경계

교체 이유:

- Legacy token weight API·home alias·Label HUD surface를 현재 계약으로 고정
- 문서의 특정 버전·proof string 의존도가 높음

### 운영·스킬·Base 계약 테스트

다음 계열은 제품 규칙과 분리해 `PRESERVE`한다.

- `tests/python/test_project_core_docs.py`
- `tests/python/test_ci_usage_contract.py`
- `tests/python/test_adversarial_review_contract.py`
- `tests/python/test_skill_*.py`
- `tests/test_base_v9_adoption.py`
- `tests/test_base_v91_operating_contract.py`
- `tests/test_base_shared_skill_adapter.py`

단, Base v9.3 최종 채택 시 v9.1 고정 assertion은 별도 Base migration gate에서 판정한다.

## 4. CI workflow 판정

### `.github/workflows/validate-omenward-core.yml`

**판정: `PRESERVE + EXTEND`**

보존:

- 통합 workflow 1개
- Python compile·unit tests
- Godot import
- 모든 headless test 순회
- Runtime smoke
- timeout 상한
- PR fast path와 main multi-platform path

확장:

- `tests/headless/latest/**`
- `tests/python/latest/**`
- `validate_latest_vertical_slice_contracts.py`
- Red 단계에서는 expected-failure job을 별도 명시
- 구현 시작 뒤 expected-failure 표식을 제거하고 Green 필수화

금지:

- C1/C2/C3별 임시 workflow 재생성
- 테스트 실패를 `continue-on-error`로 영구 무시
- compile/import 오류를 expected Red로 인정

## 5. 마이그레이션 순서

```text
1. 최신 Red 테스트 파일 작성
2. 현재 Legacy에서 계약 미구현 이유로 실패 확인
3. 기존 테스트를 PRESERVE/SPLIT 파일로 분리
4. capture_power scaling 등 정면 충돌 assertion 제거
5. 최신 구현을 최소 단위로 진행
6. 관련 테스트 Green
7. 전체 Legacy preserve regression Green
8. Runtime·사람 QA
9. 과거 validator를 ARCHIVE_EVIDENCE로 강등
```

## 6. 현재 판정 요약

```text
HEADLESS_PRESERVE: phase_0, shared combat, lane isolation, determinism, read-only UX
HEADLESS_SPLIT_REPLACE: scene, stage data, roulette, economy, stage run, battle objective, C3 UX
DIRECT_RETIRE_BEHAVIOR: capture_power scaling, independent weighted spin, legacy home node aliases as product canon
PYTHON_LEGACY_VALIDATORS: RETIRE_AS_CURRENT_GATE / REWRITE
CORE_CI_WORKFLOW: PRESERVE_AND_EXTEND
LATEST_RED_TEST_FILES: NOT_CREATED
PRODUCT_CODE: UNCHANGED
TEST_EXECUTION: NOT_RUN
```