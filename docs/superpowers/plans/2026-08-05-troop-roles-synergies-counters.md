# OMENWARD 병종 역할·시너지·카운터 실행 기록

```yaml
decision_id: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
branch: gpt/omenward-troop-roles-spec-20260805
pull_request: 139
status: BRANCH_WORK_COMPLETE / READY_FOR_FINAL_PREFLIGHT
planning_counter: 4_OF_10
product_code: UNCHANGED
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 목표

승인된 병종 설계를 현행 책임 원본으로 만들고, 문서 계약을 TDD로 검증하며, 중앙 권위와 Google Sheet를 같은 Decision ID로 동기화한다. 제품 코드·Scene·Resource·병종 `.tres`·정확 수치·아트 자산은 변경하지 않는다.

## 실행 결과

- [x] 승인 Spec 작성·사용자 검토·자체 모호성 검수.
- [x] `8~12종` 임의 제한 제거; `ROSTER_MIN_MAX: NOT_PRESET`으로 사용자 승인 범위 복원.
- [x] `tests/python/test_troop_role_canon.py` 작성 및 CI 등록.
- [x] RED run 922에서 정본·리뷰·4/10 라우팅·Legacy 데이터 격리 부재를 예상대로 검출.
- [x] 병종 정본과 적대적 검토 `OMW-AUD-420~443` 작성.
- [x] README·AGENTS·Project Core·GDD·Documentation Map·Lifecycle·Pending·Roadmap·Implementation Status·Handoff·Decision Ledger·Sheet 계약을 4/10으로 동기화.
- [x] `data/units/*.tres`를 파일 변경 없이 `[증거] LEGACY_PROTOTYPE_UNIT_DATA / IMPLEMENTATION_INPUT_FORBIDDEN`으로 격리.
- [x] Legacy C1/C2/C3 검증 증거를 최신 상태와 분리해 복원.
- [x] C3 정확 marker 중복 제거로 mutation test 검출력 복구.
- [x] Google Sheet에 Decision 4/10, 근거 `081~085`, 감사 `420~443`, 시스템·콘텐츠·변경 이력을 신규 행으로 기록.
- [x] Sheet bounded read-back에서 Decision ID·exact HEAD·4/10·10종 기준선·압력 경로·Legacy 경계·다음 Gate 일치 확인.
- [x] exact HEAD `bfaf34dbf7c8dd46a7aa833bb782cb3440db6cfd`에서 CI 네 종 Green 확인.

## TDD 증거

```text
RED
Validate Project Core Documentation run 922
result = FAILURE_AS_EXPECTED
cause = TROOP_CANON / REVIEW / 4_OF_10_ROUTING / LEGACY_UNIT_LIFECYCLE_MISSING

GREEN
Validate Project Core Documentation run 945
Validate Omenward GDD Sheet Adoption run 652
Validate Omenward Core run 121
Validate Base v9 adoption run 635
result = SUCCESS
```

## REFACTOR

- 긴 실행 체크리스트를 증거 중심 완료 기록으로 압축했다.
- 현재 4/10 상태와 과거 3/10·Legacy C1/C2/C3 증거를 분리했다.
- 존재하지 않는 계획 경로 대신 실제 현행 파일인 `HANDOFF_CONTEXT.md`, `PROJECT_CANON_DECISION_LEDGER.md`, `PROJECT_GOOGLE_SHEET_WORKBOOK.md`를 갱신했다.
- 정확 상태 marker는 mutation test가 제거를 탐지하도록 한 번만 유지했다.
- 구형 `.tres` 데이터의 내용은 수정하지 않았다.

## Sheet 기록 범위

```text
00_프로젝트_허브!E2:L2
01_작업순서!A55:L55
02_현재_확정결정!A62:M62
03_근거_라이브러리!A81:J85
04_누락_충돌_감사!A420:H443
05_GDD_요약!A12:J13
12_핵심루프!A35:J35
15_조작_게임규칙!A38:J38
40_핵심시스템_메인콘텐츠!A38:J38
50_메인콘텐츠!A45:J45
99_변경이력!A72:H72
```

## 최종 preflight 계약

병합 전 최종 HEAD에서 다음을 다시 확인한다.

```text
CI 4종 Green
behind main = 0
changed product paths = 0
reviews = 0 or addressed
unresolved threads = 0
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
unfinished TODO/TBD = 0
Sheet exact-head bounded read-back = PASS
```

최종 preflight가 HEAD를 변경하지 않으면 PR #139를 ready로 전환하고 exact HEAD 보호 조건으로 squash merge한다. 병합 후 Sheet의 현재 상태 범위만 merged main SHA로 갱신하고 bounded read-back을 다시 수행한다.

## 다음 Gate

```text
OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
5_OF_10
```

4/10 병합은 병종 데이터·AI·수치 구현 승인이 아니다.