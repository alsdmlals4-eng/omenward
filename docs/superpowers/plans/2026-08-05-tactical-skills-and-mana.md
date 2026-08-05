# OMENWARD 전술스킬·마력 실행 기록

```yaml
decision_id: OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
branch: gpt/omenward-tactical-skills-mana-spec-20260805
pull_request: 140
status: BRANCH_WORK_COMPLETE / READY_FOR_FINAL_PREFLIGHT
planning_counter: 5_OF_10
product_code: UNCHANGED
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 목표

승인된 5/10 설계를 현행 정본으로 만들고, 전술 자원·마력탑 성장·연구·해금·수동 시전·MapRun 초기화 계약을 GitHub와 Google Sheet에 같은 Decision ID로 동기화한다.

## 확정된 계약

```text
마력탑 최대 활성 수 = 1
마력탑 T1 → T2 → T3
분기 = FORBIDDEN
동시 연구 = 1
연구 비용 = 골드 + 연구 시간
시전 비용 = 마력
Stage 전 편성 = 없음
자동 시전 = 금지
Reset = NEW_MAPRUN
```

```text
T1 4종 = 속박진 / 수호장 / 집중 명령 / 충격파
T2 3종 = 폭풍 억제 / 파쇄 명령 / 봉쇄 결계
T3 3종 = 결전의 깃발 / 성역 / 시간 왜곡
```

## 실행 결과

- [x] 승인 Spec 작성 및 사용자 검토 완료.
- [x] `tests/python/test_tactical_skill_mana_canon.py` 작성 및 CI 등록.
- [x] RED run 954에서 새 정본·검토·5/10 라우팅·용어·수명주기 부재만 예상대로 검출.
- [x] 기존 문서·CI 계약 45개가 RED 단계에서도 통과함을 확인.
- [x] 전술스킬·마력 책임 원본과 적대적 검토 `OMW-AUD-444~467` 작성.
- [x] 중앙 13개 권위 문서를 5/10으로 라우팅.
- [x] Project Core의 현행 자원 계약을 마력으로 전환하고 구형 용어 재유입 mutation test 추가.
- [x] 과거 마력탑 분기는 결정 계보로 보존하되 `[대체됨] / IMPLEMENTATION_INPUT_FORBIDDEN`으로 격리.
- [x] Legacy C1·C2·C3와 3/10·4/10 완료 이력 보존.
- [x] Google Sheet에 Decision 5/10, 근거 `089~093`, 감사 `444~467`, 시스템·콘텐츠·변경 이력을 신규 행으로 기록.
- [x] Sheet bounded read-back에서 Decision ID·exact HEAD·5/10·4·3·3·MapRun reset·감사 범위·다음 Gate 일치 확인.
- [x] candidate HEAD `917445ba9b09260da1f2b7bafb0bbf2f809a834b`에서 CI 네 종 Green 확인.

## TDD 증거

```text
RED
Validate Project Core Documentation run 954
result = FAILURE_AS_EXPECTED
existing_contract_tests = 45 PASS
cause = TACTICAL_CANON / REVIEW / 5_OF_10_ROUTING / TERMINOLOGY / LIFECYCLE_MISSING

GREEN CANDIDATE
Validate Project Core Documentation run 976
Validate Omenward GDD Sheet Adoption run 682
Validate Omenward Core run 150
Validate Base v9 adoption run 665
result = SUCCESS
```

## REFACTOR

- 긴 실행 체크리스트를 실제 증거 중심 기록으로 압축했다.
- 5/10 현행 상태와 3/10·4/10 완료 이력 및 Legacy C1·C2·C3 증거를 분리했다.
- 구형 건물 문서 전체를 파괴적으로 교체하지 않고 수명주기 우선순위로 마력탑 부분만 대체했다.
- 검증기의 전술 자원 계약을 마력으로 이동하고 구형 용어 회귀를 자동 차단했다.
- Sheet 과거 행을 보존하고 신규 5/10 행만 추가했다.
- 제품 코드·Scene·Resource·게임 데이터·실제 아트 자산은 변경하지 않았다.

## Sheet 기록 범위

```text
00_프로젝트_허브!E2:L2
01_작업순서!A56:L56
02_현재_확정결정!A63:M63
03_근거_라이브러리!A89:J93
04_누락_충돌_감사!A444:H467
05_GDD_요약!A14:J15
12_핵심루프!A36:J36
15_조작_게임규칙!A39:J39
40_핵심시스템_메인콘텐츠!A39:J39
50_메인콘텐츠!A46:J46
99_변경이력!A73:H73
```

## 최종 검증 계약

REFACTOR로 HEAD가 변경됐으므로 다음을 새 exact HEAD에서 다시 확인한다.

```text
CI 4종 Green
behind main = 0
product paths changed = 0
reviews addressed
unresolved threads = 0
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
unfinished placeholders = 0
Sheet exact-head bounded read-back = PASS
```

검증이 통과하면 PR #140을 ready로 전환하고 exact HEAD 보호 조건으로 squash merge한다. 병합 뒤 현재 5/10 Sheet 상태만 merged main SHA로 갱신한다.

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
OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
6_OF_10
```
