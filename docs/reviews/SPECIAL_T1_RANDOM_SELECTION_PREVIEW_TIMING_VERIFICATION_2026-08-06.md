# 특수병 병영 T1 무작위 선정·공개 시점 검증 기록

```yaml
decision_id: OMW-DEC-20260806-PLANNING-SPECIAL-T1-RANDOM-SELECTION-AND-PREVIEW-TIMING-V1
verified_at: 2026-08-06 KST
scope: CHECKPOINT_8_DOCUMENT_CONTRACT_ONLY
result: BOUNDED_MARKER_PASS / FULL_HEAD_GREEN_NOT_PROVEN
```

## 1. RED 증거

```text
RED_COMMIT = 42255ccc1601aeb7bc63f74b06373d8b14b5298f
RED_TEST = tests/python/test_special_t1_random_selection_preview_timing_canon.py
RED_RESULT = 1_FAILURE / 8_ERRORS
RED_INTERPRETATION = EXPECTED_MISSING_AUTHORITY_REVIEW_SPEC_AND_PARENT_MARKERS
```

테스트를 먼저 추가한 뒤 새 책임 원본이 없는 재구성 환경에서 실행했다. 파일 존재 검사는 실패했고 나머지 검사는 책임 원본 부재로 오류가 발생해 RED를 확인했다.

## 2. 원격 read-back

```text
AUTHORITY_BLOB = 356686b8f729570d712af5258f32968e7242dd8c
REVIEW_BLOB = 836011e1ac106c44601cfb39a548b16ea6b88759
SPEC_BLOB = 940309eb359888abe0857e5e099f02f7453e484a
TEST_BLOB = 4e56a005d76fe7c2964ac4bcd3632abfb1b0ad14
PARENT_ONBOARDING_BLOB = da2171231cec6d80ba54c28438bd0c6090330636
GITHUB_AUTHORITY_READBACK = PASS
```

원격 connector read-back에서 다음 계약 표식을 확인했다.

- 건설 성공 커밋 뒤 병영별 1회 독립 추첨.
- 결과 즉시 공개 뒤 첫 생산 타이머 시작.
- T1 동안 선정 병종 반복 생산과 TokenSource 없음.
- 저장·불러오기·무료 취소 재추첨 금지.
- T2 플레이어 선택 전문화와 TokenSource 해금.
- 부모 온보딩 `PARTIAL_APPROVAL_8_OF_10` 승격과 구형 pending 표식 제거.

## 3. bounded GREEN

```text
CHECKPOINT_8_BOUNDED_CONTRACT = 9_PASS / 0_FAIL / 0_ERROR
PY_COMPILE = PASS
```

원격 read-back으로 확인한 계약 표식을 테스트 경로 구조에 재구성해 전용 unittest 9개를 실행했다. Python 실행 환경은 시작 시 artifact_tool spreadsheet warmup 경고를 stderr에 출력했으나 unittest와 py_compile의 반환 코드는 각각 0이었다.

## 4. 검증 한계

```text
FULL_PRIVATE_REPOSITORY_CHECKOUT = UNAVAILABLE
FULL_PLANNING_CONTRACT_SUITE = NOT_RUN
EXACT_HEAD_FULL_TEST_EXECUTION = NOT_RUN
FRESH_PHASE1_GODOT_TEST_ON_CURRENT_HEAD = NOT_RUN
GITHUB_ACTIONS_GREEN = NOT_PROVEN
AUTOMATED_GREEN = NOT_PROVEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

9 PASS는 체크포인트 8 문서 marker 계약에만 적용한다. 저장소 전체 무결성, 제품 난수·저장·건설 거래, Scene 조립, 실제 생산 타이머나 UX 동작을 증명하지 않는다.

## 5. 제품 경계

```text
PRODUCT_CODE = UNCHANGED
GAMEPLAY_SCENE_RESOURCE_DATA = UNCHANGED
ART_ASSETS = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
```
