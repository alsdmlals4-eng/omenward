# OMENWARD 프로젝트 인수인계 컨텍스트

- 갱신일: `2026-08-01`
- 공식명: **오멘워드 / OMENWARD**
- 현재 Work Mode: `PLAN`
- 제품 상태: `LEGACY_PROTOTYPE`
- 최신 기획 상태: `APPROVED_VERTICAL_SLICE / NOT_IMPLEMENTED`
- PR: `#116 DRAFT / OPEN / NOT_MERGED`
- 제품 코드·Codex: `NOT_AUTHORIZED / BLOCKED`
- Runtime·사람 검증: `NOT_RUN / NOT_RUN`
- 활성 Base: `v9.1`
- 권장 다음 Base: `v9.3 / SEPARATE_ATOMIC_MIGRATION`
- 현재 감사: `OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1`

이 문서는 새 작업자가 과거 대화 없이 현재 정본, 실제 Legacy 구현, 열린 P1과 다음 작업을 복원하기 위한 압축 Handoff다. 상세 규칙은 책임 원본을 읽는다.

## 1. 가장 먼저 알아야 할 것

1. 오멘워드는 **세 물리 릴을 설계하고 결과를 세 전선 중 하나에 비가역 커밋하는 PC 실시간 전략 오토배틀**이다.
2. 현재 제품 코드는 최신 Vertical Slice가 아니라 Legacy 기술 프로토타입이다.
3. 최신 전장 불변식은 본진 6/진영, 중간 거점 6곳×3, 접전지 0, 총 30건설 노드다.
4. 최신 룰렛은 독립 9칸 가중 추첨이 아니라 세 원형 `TokenInstance` 배열·cursor·3×3 노출 보드다.
5. 최신 점령은 `capture_power` 합산이 아니라 병력 수·Tier·병종과 무관한 고정시간 규칙이다.
6. 최신 건물 가족은 금고·농장·타워·병영·지휘소 5종이다.
7. 패배 후 제품 재시도는 Stage 5 이후 MapRun당 최대 1회 영구재화 거래다. 현재 무료 restart는 개발 seam이다.
8. 안내자 정본명은 `벨루 / Belu`다. `율비`는 역사 별칭이다.
9. 최신 Red 테스트 명세는 작성됐지만 실제 test files와 expected-failure 증거는 없다.
10. PR #116은 Base adoption check만 통과하고 Project Core·GDD Sheet 검증은 실패했다. ready/merge 금지다.

## 2. 현재 플레이어 약속

> **공개된 공세를 읽고 건물과 TokenSource로 세 릴의 미래 구조를 만든 뒤, 잔여 RNG를 감수해 얻은 병력을 한 전선에 되돌릴 수 없이 배치하고 그 결과를 다음 설계에 반영한다.**

```text
공세 예고
→ 건설·릴 설계
→ 회전·이동
→ snapshot·확정
→ 보관/판매/배치
→ 세 라인 자동전투·점령
→ 정산·원인 복기
```

## 3. 현재 실제 구현

```text
Main Scene
├─ GameSession
├─ Battlefield
└─ UI
   ├─ StageHud
   └─ StageSelect

Legacy Roulette
├─ fixed spin cost 20
├─ X/GOLD/source weight
├─ independent 9-cell generation
├─ central-row judgement
└─ reward generation

Legacy Battle
├─ top/middle/bottom
├─ bases/gates/outposts/clash zones
├─ capture_power aggregation
└─ deterministic fixed-step seam

Legacy Buildings
├─ barracks
├─ tower
└─ farm
```

`StageHud`는 Label 중심 기술 HUD이고 제품 메인·준비·정산·패배 화면은 없다.

## 4. 현재 권위 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ docs/BASE_RULES_VERSION.md
→ docs/DOCUMENTATION_MAP.md
→ docs/PROJECT_CORE.md
→ docs/audits/OMENWARD_BASE_PROJECT_SHEET_REPOSITORY_WIDE_AUDIT_2026-08-01.md
→ docs/PROJECT_CANON_DECISION_LEDGER.md
→ docs/DECISIONS_PENDING.md
→ 분야 APPROVED 계약
→ docs/testing/LATEST_VERTICAL_SLICE_RED_TEST_SPEC_2026-08-01.md
→ docs/testing/LEGACY_TEST_PRESERVE_REPLACE_RETIRE_MATRIX_2026-08-01.md
→ docs/CURRENT_IMPLEMENTATION_STATUS.md
→ 실제 code/data/Scene/tests
→ 연결 Google Sheet
→ docs/ACTIVE_CONTEXT.md
```

과거 `CORE_POC`, 3스테이지 Slice, V6 intake, PR #92/#97 exact 수치는 최신 권위가 아니다. 삭제하지 않고 역사·Legacy 계보로만 사용한다.

## 5. 현재 열린 P1

- Project Core validator가 오래된 marker·routing에 고정돼 workflow 실패.
- GDD Sheet adoption test가 오래된 Base SHA·C1 증거 문자열에 고정돼 workflow 실패.
- Sheet 일부 분야 탭의 역사/current 상태 혼합.
- Base v9.3 Adapter·Snapshot·Router·validator 실제 마이그레이션 미실행.
- Screen Board V2 미작성.
- 경제·Retry 비용·save/checkpoint exact 계약 미확정.
- 최신 Red test files·expected failure 증거 미작성·미실행.

## 6. 다음 순서

```text
1. 현재 정본·Sheet 의미 drift 재조회 완료
2. Screen Board V2 화면별 독립 브리프·텍스트 명세
3. 경제·Retry 비용·save/checkpoint Approval Bundle·시뮬레이션 계약
4. 실제 최신 Red test Work Order·expected-failure package
5. 별도 Base v9.3 Adapter 원자 마이그레이션 package
6. 사용자 승인 Codex 제품 구현 Plan
7. Codex Build·자동/Runtime/사람 검증
```

현재 시각 작업의 다음 산출물은 생성 이미지가 아니라 화면 구조·상태·정보 위계가 있는 텍스트 명세다.

## 7. 금지된 완료 표현

다음 증거 전에는 사용하지 않는다.

```text
LATEST_VERTICAL_SLICE_IMPLEMENTED
LATEST_VERTICAL_SLICE_PROVEN
CORE_LOOP_PROVEN
MVP_COMPLETE
BASE_V9_3_ADOPTED
CI_PASS
RUNTIME_VALIDATED
HUMAN_VALIDATED
```

```text
NEXT_WORK_MODE: PLAN
PRODUCT_CODE: NOT_AUTHORIZED
CODEX: BLOCKED
PR_READY: NO
PR_MERGE: BLOCKED
```