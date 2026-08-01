# 오멘워드 최신 Vertical Slice Red 테스트 명세

- 결정 ID: `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1`
- 작성일: `2026-08-01`
- 상태: `DERIVED_FROM_CURRENT_CANON / CURRENT_IMPLEMENTATION_GATE / PLANNING_ONLY`
- 제품 코드 권한: `NONE`
- 테스트 코드 작성·실행: `NOT_RUN`
- Codex 실행: `BLOCKED_UNTIL_USER_APPROVED_IMPLEMENTATION_PLAN`

이 문서는 현재 승인된 오멘워드 계약을 실제 제품 구현으로 옮기기 전에 먼저 작성해야 할 **실패 계약(Red tests)**을 정의한다. 이 문서 자체는 구현 완료나 테스트 통과 증거가 아니다.

## 1. TDD 불변 조건

```text
최신 계약을 표현하는 테스트 작성
→ 현재 Legacy 구현에서 의도한 이유로 실패하는지 확인
→ 실패 증거 저장
→ 최소 제품 구현
→ 관련 테스트만 Green
→ 전체 회귀 테스트 Green
→ Runtime·사람 QA
```

다음은 금지한다.

- 제품 코드를 먼저 작성하고 테스트를 나중에 맞추기
- 현재 Legacy 동작을 통과시키기 위해 최신 계약 기대값을 낮추기
- 문구 존재만 검사하고 실제 상태 전이를 검사하지 않기
- 정확한 수치가 미확정인 항목에 임의 숫자를 고정하기
- Red 테스트가 실패하지 않았는데 구현 단계로 이동하기
- Legacy proof를 최신 Vertical Slice proof로 이름만 바꾸기

## 2. 테스트 계층

| 계층 | 목적 | 실행 형태 |
|---|---|---|
| `L0 Repository Contract` | 권위 문서·파일·금지 Legacy 활성화 검사 | Python unittest/validator |
| `L1 Domain Contract` | 단일 서비스·상태 객체의 실제 규칙 | Godot headless |
| `L2 Transaction Contract` | 건설·릴·점령·재시도 원자 거래 | Godot headless |
| `L3 Determinism/Simulation` | 동일 seed 재현·확률·경제 불변식 | Godot headless + Python simulation |
| `L4 Runtime/Human` | 제품 화면·조작성·이해 가능성 | Runtime smoke + 사람 QA |

`L0`는 `L1~L3`를 대체하지 않는다. 문자열 검사만 통과한 상태를 제품 구현 증거로 사용하지 않는다.

## 3. 제안 테스트 파일 구조

```text
tests/headless/latest/
  battlefield_topology_contract_test.gd
  construction_node_contract_test.gd
  physical_reel_contract_test.gd
  spin_snapshot_transaction_test.gd
  fixed_capture_contract_test.gd
  building_family_contract_test.gd
  pending_reward_deployment_contract_test.gd
  paid_retry_transaction_test.gd
  cross_system_vertical_slice_test.gd

tests/python/latest/
  test_latest_contract_repository_gate.py
  test_legacy_authority_boundary.py
  test_latest_ci_wiring.py

tools/
  validate_latest_vertical_slice_contracts.py
```

정확한 파일명은 구현 Plan에서 조정할 수 있지만, 테스트 책임을 한 대형 파일에 합치지 않는다.

---

# 4. 전장 토폴로지·건설 노드 Red 계약

권위 원본:

- `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_CONSTRUCTION_NODE_INVARIANTS_2026-08-01.md`
- `docs/PROJECT_CORE.md`

## 4.1 필수 Red 테스트

| ID | 테스트 행동 | 현재 Legacy 예상 실패 이유 |
|---|---|---|
| `RED-TOPO-001` | 전장 수가 정확히 1개다 | 명시적 최신 BattlefieldTopology 모델 없음 |
| `RED-TOPO-002` | 라인이 `top/middle/bottom` 3개다 | 일부 seam은 존재하나 최신 토폴로지 객체 없음 |
| `RED-TOPO-003` | 건설 노드 종류가 `CONSTRUCTION_NODE` 1종뿐이다 | 노드 종류 계약을 소유하는 최신 데이터 없음 |
| `RED-TOPO-004` | 아군·적 본진이 각각 건설 노드 6개를 가진다 | 본진 건설 노드 모델 없음 |
| `RED-TOPO-005` | 중간 거점이 `3라인 × 2진영 = 6곳`이다 | Legacy outpost 구조는 있으나 최신 위치 데이터 계약 없음 |
| `RED-TOPO-006` | 각 중간 거점이 건설 노드 3개를 가진다 | `front_a/front_b/rear` 등록 seam만 존재 |
| `RED-TOPO-007` | 중앙 접전지 3곳의 건설 노드 수가 0이다 | 접전지·건설 명령 분리 자동 계약 없음 |
| `RED-TOPO-008` | 전체 건설 노드가 `2×6 + 6×3 = 30`이다 | 전체 30노드 데이터 모델 없음 |
| `RED-TOPO-009` | 중앙 접전지에 건설 요청하면 명시적 실패하며 자원을 소비하지 않는다 | 최신 construction target validator 없음 |
| `RED-TOPO-010` | 양 진영 구조가 대칭이며 라인별 객체가 서로 독립이다 | 최신 대칭 topology snapshot 없음 |

## 4.2 테스트가 특정하면 안 되는 것

- 노드의 최종 화면 좌표
- 정확한 node ID 문자열 형식
- 노드별 건물 비용
- 시각적 모양과 아이콘

이 항목은 후속 데이터·화면 계약이 소유한다.

---

# 5. 세 물리 릴·SpinSnapshot Red 계약

권위 원본:

- `docs/design/APPROVED_ROULETTE_CORE_RULES.md`

## 5.1 물리 릴

| ID | 테스트 행동 | 현재 Legacy 예상 실패 이유 |
|---|---|---|
| `RED-REEL-001` | 왼쪽·중앙·오른쪽 세 원형 `TokenInstance` 배열이 존재한다 | 독립 가중치 기반 3×3 결과 생성 |
| `RED-REEL-002` | 각 릴 길이는 항상 3 이상이다 | 물리 배열 없음 |
| `RED-REEL-003` | MapRun 시작 시 각 릴은 `[X,X,X]`다 | 초기 물리 릴 없음 |
| `RED-REEL-004` | 동일 live state와 RNG stream은 같은 cursor·보드를 만든다 | 물리 cursor 없음 |
| `RED-REEL-005` | 길이 3·4·N에서 3칸 wrap 노출이 정확하다 | 물리 배열 없음 |

## 5.2 TokenSource

| ID | 테스트 행동 | 현재 Legacy 예상 실패 이유 |
|---|---|---|
| `RED-REEL-006` | TokenSource 한 동이 동일 출처 토큰을 세 릴에 하나씩 공급한다 | source entry/weight만 존재 |
| `RED-REEL-007` | 각 릴에서 최저 안정 index의 X를 먼저 교체한다 | 실제 X 인스턴스 배열 없음 |
| `RED-REEL-008` | X가 없을 때만 append한다 | 실제 배열 없음 |
| `RED-REEL-009` | 모든 토큰이 고유 `token_instance_id`와 source ID를 가진다 | symbol 중심 resolver |
| `RED-REEL-010` | 파괴·BLOCKED source 토큰은 이동 위치와 무관하게 source ID로 제거된다 | source-bound instance 제거 없음 |
| `RED-REEL-011` | 제거 뒤 릴 길이 3 미만이면 X로 보충한다 | 물리 배열 없음 |

## 5.3 이동

| ID | 테스트 행동 | 현재 Legacy 예상 실패 이유 |
|---|---|---|
| `RED-MOVE-001` | 세로 이동은 선택 릴 cursor만 ±1 wrap 변경한다 | cursor 이동 미구현 |
| `RED-MOVE-002` | 세로 이동은 배열 순서·다른 릴·릴 소속을 바꾸지 않는다 | 물리 배열 미구현 |
| `RED-MOVE-003` | 가로 이동은 선택 노출 행의 TokenInstance 3개를 순환 교환한다 | 영구 가로 이동 미구현 |
| `RED-MOVE-004` | 가로 이동 뒤 릴 길이와 cursor가 유지된다 | 영구 가로 이동 미구현 |
| `RED-MOVE-005` | 토큰 ID·심벌·source·reward payload가 함께 이동한다 | token instance 모델 없음 |
| `RED-MOVE-006` | 가로 이동 결과가 다음 회전에도 유지된다 | live 릴 영구 편집 없음 |
| `RED-MOVE-007` | preview는 복제 상태만 변경하고 live 상태를 변경하지 않는다 | SpinSession preview 없음 |
| `RED-MOVE-008` | 이동 실행 즉시 이동권을 소비하며 undo/reset은 없다 | 최신 이동 거래 없음 |

## 5.4 Snapshot·확정

| ID | 테스트 행동 | 현재 Legacy 예상 실패 이유 |
|---|---|---|
| `RED-SNAP-001` | 정지 시 전체 릴·cursor·보드·비용·source 후보를 깊은 복사한다 | 완전한 immutable snapshot 없음 |
| `RED-SNAP-002` | snapshot 뒤 건물 파괴가 snapshot 보상을 바꾸지 않는다 | live source 재조회 위험 |
| `RED-SNAP-003` | 확정은 snapshot과 최종 SpinSession 보드만 사용한다 | 최신 확정 거래 없음 |
| `RED-SNAP-004` | 같은 SpinSession 두 번째 확정은 무보상이다 | idempotent confirm 계약 없음 |
| `RED-SNAP-005` | 미확정 session·PendingReward·공간 부족은 새 회전을 비용 없이 차단한다 | 일부 pending seam만 존재 |

## 5.5 보존해야 하는 Legacy resolver 회귀

다음 행동은 최신 물리 릴 위에서도 유지한다.

- 중앙줄이 실패하면 다른 7줄 무시
- X는 보상 없음
- 동일 판정 심벌의 1/2/3~7/8 완성선 등급
- 금화 75%/200%/500%와 floor
- 동일 snapshot·seed의 source 선택 결정성

다만 `스테이지당 전설 1회` 또는 기존 all-nine 처리 방식은 최신 `5 Stage 위험 주기당 1회` 계약으로 교체한다.

---

# 6. 고정시간 점령 Red 계약

권위 원본:

- `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`

| ID | 테스트 행동 | 현재 Legacy 예상 실패 이유 |
|---|---|---|
| `RED-CAP-001` | 동일 조건에서 유닛 1기와 다수가 같은 고정시간으로 점령한다 | `capture_power` 합산 |
| `RED-CAP-002` | Tier·등급·병종이 점령속도를 바꾸지 않는다 | unit profile의 capture_power 사용 |
| `RED-CAP-003` | 중앙 접전지 기본 점령시간은 현재 계약값 8초다 | Legacy power 기반 phase 시간 |
| `RED-CAP-004` | 적이 구역에 들어오면 진행이 즉시 일시정지한다 | contested seam은 있으나 최신 거래 순서 미보장 |
| `RED-CAP-005` | 점령 부대 부재 시 데이터화된 유예 뒤 합법 소유 상태로 회복한다 | Legacy 수치·상태 모델과 다름 |
| `RED-CAP-006` | 점령 완료와 적 진입이 같은 tick이면 소유권 거래 후 contested가 된다 | 원자 순서 자동 계약 없음 |
| `RED-CAP-007` | 소유권은 주둔 병력 없이 Stage 사이에 유지된다 | MapRun 지속 모델 미구현 |
| `RED-CAP-008` | 중앙 접전지 미점령 상태에서 적 중간 거점 진격이 차단된다 | 최신 objective gate 미구현 |
| `RED-CAP-009` | 적 중간 거점 미점령 상태에서 적 본진 진격이 차단된다 | 최신 objective gate 미구현 |

유예시간·회복속도의 정확한 값은 현재 pending data이므로 테스트는 설정값 준수와 결정성을 검사하고 임의 수치를 고정하지 않는다.

---

# 7. 5개 건물 가족·점령 거래 Red 계약

| ID | 테스트 행동 | 현재 Legacy 예상 실패 이유 |
|---|---|---|
| `RED-BLD-001` | 기본 건물 가족이 금고·농장·타워·병영·지휘소 5종이다 | 병영·타워·농장 3종 |
| `RED-BLD-002` | 금고와 병영만 TokenSource다 | 금고·물리 source 미구현 |
| `RED-BLD-003` | 농장 food cap 감소는 기존 병력을 제거·약화하지 않고 신규 배치만 차단한다 | 일부 seam만 존재 |
| `RED-BLD-004` | 타워는 완공 전 공격하지 않는다 | 최신 건설 project 모델 미구현 |
| `RED-BLD-005` | 지휘소 효과는 실제 범위 기반이며 기본 전역 버프가 아니다 | 지휘소 미구현 |
| `RED-BLD-006` | 중간 거점 점령 완료는 소유권·건설권·건물 호환성·TokenSource를 원자 처리한다 | Legacy ruin 중심 처리 |
| `RED-BLD-007` | 호환 건물은 HP·Tier를 보존해 이전한다 | 최신 호환성 모델 미구현 |
| `RED-BLD-008` | 비호환·병영은 `BLOCKED`, 노드 점유 유지, 효과 중지다 | Legacy RUINED 처리 |
| `RED-BLD-009` | BLOCKED 병영 토큰은 live 릴에서 source-bound X 상태로 비활성화된다 | 물리 릴 미구현 |
| `RED-BLD-010` | 거래 중 실패 시 전체 상태가 롤백된다 | transaction journal 없음 |

정확한 비용·공사시간·Tier 수치는 별도 수치 계약 전 테스트에 고정하지 않는다.

---

# 8. PendingReward·보관·판매·비가역 배치 Red 계약

| ID | 테스트 행동 | 상태 |
|---|---|---|
| `RED-RWD-001` | 확정된 유닛 결과가 `PendingReward`로 한 번만 생성된다 | Legacy seam 부분 보존 |
| `RED-RWD-002` | 플레이어는 보관·판매·한 라인 배치 중 하나를 선택한다 | 판매·최신 저장 구조 미완성 |
| `RED-RWD-003` | 보관 병력은 식량을 사용하지 않는다 | 최신 저장 계약 필요 |
| `RED-RWD-004` | 배치 성공 시 식량을 예약한다 | Legacy seam 보존 후보 |
| `RED-RWD-005` | 배치 뒤 라인 변경·회수·판매가 불가능하다 | 최신 비가역 API 계약 필요 |
| `RED-RWD-006` | 식량 한도 감소는 배치 병력을 제거하지 않는다 | 최신 통합 회귀 필요 |
| `RED-RWD-007` | 생존 병력의 HP·라인이 다음 Stage checkpoint로 유지된다 | MapRun persistence 미구현 |
| `RED-RWD-008` | 같은 reward transaction 재실행은 중복 생성·지급하지 않는다 | idempotency key 미구현 |

---

# 9. 제품 유료 재시도·checkpoint Red 계약

권위 원본:

- `docs/design/APPROVED_VERTICAL_SLICE_DEFEAT_AND_PAID_RETRY_PRINCIPLE_2026-07-31.md`

| ID | 테스트 행동 | 현재 Legacy 예상 실패 이유 |
|---|---|---|
| `RED-RETRY-001` | Stage 1~4 제품 유료 재시도가 비활성이다 | 무료 Stage restart seam |
| `RED-RETRY-002` | Stage 5 이후 MapRun당 최대 1회다 | 제품 retry state 없음 |
| `RED-RETRY-003` | 비용은 프로필 정산 영구재화만 사용한다 | meta wallet 없음 |
| `RED-RETRY-004` | 현재 런 미정산 재화·골드·식량·무료 회전은 사용할 수 없다 | 거래 경계 없음 |
| `RED-RETRY-005` | 실패 Stage 준비 checkpoint로 복원한다 | 최신 checkpoint schema 없음 |
| `RED-RETRY-006` | seed·공세·미션·룰렛 RNG 계보가 동일하다 | lineage 복원 없음 |
| `RED-RETRY-007` | 실패 전투 중 피해·사망·소비·점령·미정산 보상은 폐기된다 | checkpoint 복원 없음 |
| `RED-RETRY-008` | 복원 실패 시 영구재화를 차감하지 않는다 | 원자 거래 없음 |
| `RED-RETRY-009` | 중복 transaction은 이중 차감·무료 복원을 만들지 않는다 | idempotency journal 없음 |
| `RED-RETRY-010` | 개발 무료 retry는 메타 보상·업적·공식 기록이 0이다 | 제품/개발 분리 없음 |
| `RED-RETRY-011` | 비용 tier가 `T1 < T2 < T3`다 | 실제 값 pending; 순서만 검사 |

영구재화 명칭과 실제 비용값은 확정 전 assertion에 넣지 않는다.

---

# 10. 교차 시스템 Vertical Slice Red 계약

최소 한 개의 통합 테스트가 다음 인과를 실제 상태로 검증해야 한다.

```text
소유 건설 노드 선택
→ TokenSource 건물 완공
→ 세 릴의 source-bound TokenInstance 변화
→ 물리 회전·SpinSnapshot
→ 이동·예측·확정
→ PendingReward
→ 한 라인 비가역 배치
→ 자동전투·점령·건물 상태 변화
→ Stage 정산·checkpoint
→ 동일 seed 재현
```

필수 assertion:

- 중간 UI snapshot 조회는 상태를 변경하지 않는다.
- 동일 초기 상태·입력 로그·seed는 동일 결과를 만든다.
- 다른 라인의 일반 병력·구조물 상태는 직접 명령 없이 오염되지 않는다.
- 원인 보고는 실제 건물 source ID, token instance, 릴 결과, 배치 라인과 전투 사건을 연결한다.
- Legacy alias `construct_home()` 또는 `front_a/front_b/rear`만으로 최신 토폴로지 통과를 주장하지 않는다.

---

# 11. CI Red 단계

최신 계약 테스트를 처음 추가하는 PR은 다음 상태가 정상이다.

```text
Repository contract: PASS
Legacy preserved tests: PASS
Latest domain/transaction tests: EXPECTED_FAIL
Failure reason: MISSING_LATEST_IMPLEMENTATION
Compile/import error: NOT_ALLOWED
Timeout/hang: NOT_ALLOWED
```

Red 증거에는 다음을 남긴다.

- commit SHA
- 실행 명령
- 실패 테스트 ID
- 기대한 실패 메시지
- 단순 문법·로드·환경 오류가 아니라 계약 미구현 때문임을 확인한 기록

제품 구현 PR에서는 `EXPECTED_FAIL` 표식을 제거하고 실제 Green을 요구한다.

# 12. Codex 인계 차단 조건

다음이 모두 충족되기 전에는 Codex 구현 Plan을 승인하지 않는다.

```text
LATEST_RED_TEST_SPEC: USER_REVIEWED
LEGACY_TEST_MATRIX: COMPLETE
EXACT_PENDING_VALUES: NOT_HARDCODED
TEST_FILE_OWNERSHIP: ASSIGNED
EXPECTED_RED_REASONS: DOCUMENTED
PRODUCT_CODE_SCOPE: USER_APPROVED
ROLLBACK_BOUNDARY: DEFINED
```

현재 판정:

```text
LATEST_RED_TEST_SPEC: WRITTEN_NOT_EXECUTED
LATEST_TEST_FILES: NOT_CREATED
RED_FAILURE_EVIDENCE: NONE
PRODUCT_CODE: UNCHANGED
CODEX_EXECUTION: BLOCKED
```