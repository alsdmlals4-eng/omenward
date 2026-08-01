# Active Context

- 갱신일: `2026-08-01`
- 공식명: **오멘워드 / OMENWARD**
- 현재 Work Mode: `PLAN`
- 실행 프로필: `PLANNING_ONLY_PROFILE`
- 현재 제품: `LEGACY_PROTOTYPE`
- 최신 Vertical Slice: `APPROVED_CANON / NOT_IMPLEMENTED`
- 제품 코드·Codex: `NOT_AUTHORIZED / BLOCKED`
- PR: `#116 DRAFT / OPEN / NOT_MERGED`
- CI: `BASE_ADOPTION_PASS / PROJECT_CORE_FAIL / GDD_SHEET_FAIL`
- Runtime·사람 검증: `NOT_RUN / NOT_RUN`
- 활성 Base: `v9.1`
- 다음 권장 Base: `v9.3 / SEPARATE_ATOMIC_MIGRATION_REQUIRED`
- 현재 감사 Decision: `OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1`

## 1. 현재 기준선

```yaml
project: OMENWARD / 오멘워드
platform: PC_PRIMARY
engine: Godot 4.7 / GDScript / Compatibility
viewport: 960x540
window_override: 1920x1080
scaling: integer
work_mode: PLAN
product_state: LEGACY_PROTOTYPE
latest_vertical_slice: APPROVED_NOT_IMPLEMENTED
active_base_version: 9.1.0
active_base_release: 3c158f52cfdad889970aef4d6ce6650a6fea0645
active_base_evidence: dd20ad3852e264d7e337e34d2cb963f71053a6cb
recommended_base_version: 9.3.0
product_code_authority: NONE
codex_execution: BLOCKED
merge_authority: NOT_GRANTED
```

## 2. 프로젝트 약속

> **세 개의 물리 릴 구조를 건물과 TokenSource로 설계하고, 남은 무작위성을 감수해 얻은 병력을 세 전선 중 하나에 비가역적으로 커밋하며, 전투 결과의 원인을 다음 설계에 반영한다.**

```text
공세 예고
→ 건설·TokenSource·세 물리 릴 설계
→ 회전·세로 이동·영구 가로 이동
→ SpinSnapshot·확정
→ PendingReward 보관/판매/한 라인 배치
→ 세 라인 자동전투·고정시간 점령
→ 정산·원인 복기·다음 Stage
```

## 3. 현재 승인 불변 조건

- 표준 MapRun 약 35분, 20 Stage, 4막.
- 위험 Stage 5·10·15·20.
- 하나의 전장, `top/middle/bottom` 3라인.
- 건설 노드 종류 1개.
- 본진 6노드/진영.
- 중간 거점 `3라인 × 2진영 = 6곳`, 거점당 3노드.
- 중앙 접전지 3곳, 건설 노드 0개.
- 전체 건설 노드 `2×6 + 6×3 = 30`.
- 세 물리 릴과 3×3 노출 보드.
- 가로 이동은 TokenInstance 전체를 교환하며 영구 유지.
- 이동권 소비 뒤 undo/reset 없음.
- immutable `SpinSnapshot`.
- 배치 후 라인 변경·회수·판매 없음.
- 유닛 수·Tier·병종과 무관한 고정시간 점령.
- 금고·농장·타워·병영·지휘소 5건물.
- Stage 5 이후 MapRun당 최대 1회 제품 유료 재시도.
- 안내자 정본명 `벨루 / Belu`; `율비`는 역사 별칭.

## 4. 실제 구현 경계

현재 Godot 구현은 Legacy 기술 프로토타입이다.

```text
CURRENT_IMPLEMENTATION
- Main = Battlefield + Label HUD + StageSelect
- 독립 가중치 9칸 Roulette
- 중앙 판정·8개 완성선·금화·등급 resolver
- 병영·타워·농장 3건물
- outpost당 front_a/front_b/rear 3노드
- capture_power 합산 점령
- pending reward·한 라인 배치 seam
- 패배 후 무료 same-stage restart

NOT_IMPLEMENTED
- 본진 포함 30노드 topology
- 세 물리 릴·cursor·TokenInstance lifecycle
- 영구 가로 이동·immutable full SpinSnapshot transaction
- 고정시간 점령
- 5건물 최신 lifecycle·BLOCKED 거래
- 20 Stage MapRun·checkpoint·제품 유료 Retry
- 제품 화면·벨루 Runtime
```

```text
LEGACY_PROVEN != LATEST_IMPLEMENTED != LATEST_PROVEN
```

## 5. 테스트·검증 상태

- 최신 Red 테스트 명세: `WRITTEN`.
- Legacy 보존·교체·폐기 판정: `WRITTEN`.
- 실제 최신 test files: `NOT_CREATED`.
- expected Red 실행: `NOT_RUN`.
- 제품 Runtime·접근성·성능·사람 QA: `NOT_RUN`.
- PR #116 workflow:
  - Base v9 adoption: `PASS`.
  - Project Core Documentation: `FAIL`.
  - GDD Sheet Adoption: `FAIL`.

PR을 ready 또는 merge 상태로 승격하지 않는다.

## 6. 현재 P1

1. 프로젝트 정본 validator와 GDD Sheet test가 구형 문자열·Base SHA에 고정되어 현재 문서와 충돌.
2. Sheet 일부 분야 탭이 역사 PR #92/#97을 현재 exact 권위처럼 표시.
3. Base v9.3 Adapter 이관은 아직 실제 수행·검증되지 않음.
4. Screen Board V2·경제/Retry/save exact 계약·실제 Red package가 미작성 또는 미실행.

## 7. 우선 읽기

1. `AGENTS.md`
2. `docs/BASE_RULES_VERSION.md`
3. `docs/DOCUMENTATION_MAP.md`
4. `docs/PROJECT_CORE.md`
5. `docs/audits/OMENWARD_BASE_PROJECT_SHEET_REPOSITORY_WIDE_AUDIT_2026-08-01.md`
6. `docs/PROJECT_CANON_DECISION_LEDGER.md`
7. `docs/DECISIONS_PENDING.md`
8. `docs/testing/LATEST_VERTICAL_SLICE_RED_TEST_SPEC_2026-08-01.md`
9. `docs/testing/LEGACY_TEST_PRESERVE_REPLACE_RETIRE_MATRIX_2026-08-01.md`
10. `docs/CURRENT_IMPLEMENTATION_STATUS.md`
11. 실제 code/data/Scene/tests
12. 연결 Google Sheet

## 8. 다음 작업 순서

```text
현재 Context·Sheet 의미 drift 동기화 완료
→ Screen Board V2 화면별 독립 브리프·텍스트 명세
→ 경제·Retry 비용·save/checkpoint Approval Bundle·시뮬레이션 계약
→ 실제 최신 Red test Work Order·expected-failure package
→ 별도 Base v9.3 Adapter 원자 마이그레이션 package
→ 사용자 승인 Codex 제품 구현 Plan
```

현재 다음 단계는 **화면 이미지를 생성하는 작업이 아니라 Screen Board V2의 화면 구조·상태·정보 위계를 텍스트 명세로 확정하는 작업**이다.

```text
NEXT_WORK_MODE: PLAN
PRODUCT_CODE: NOT_AUTHORIZED
CODEX: BLOCKED
PR_READY: NO
PR_MERGE: BLOCKED
```