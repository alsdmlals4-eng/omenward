# Stage 2 최초 T2 후보·골드 규칙 검증 기록

```yaml
decision_id: OMW-DEC-20260806-PLANNING-STAGE2-FIRST-T2-CANDIDATES-AND-GOLD-RULES-V1
verified_at: 2026-08-06 KST
scope: CHECKPOINT_7_DOCUMENT_CONTRACT
result: BOUNDED_MARKER_CONTRACT_PASS / FULL_HEAD_SUITE_PENDING
product_change: NONE
```

## 1. RED

```text
RED_COMMIT = 0b3d6a5c5ae8ce326ca3d9e08773168f1b8cad81
RED_TESTS = 8
RED_RESULT = 1_FAILURE / 7_ERRORS
RED_EXIT_STATUS = 1
```

신규 책임 원본·적대적 검토·설계 명세와 부모 온보딩 승격이 없는 상태에서 테스트를 실행했다. 권위 파일 부재와 기존 `PENDING_GRILLME` 상태 때문에 실패했으며, 실패 원인은 새 계약이 아직 존재하지 않는 것이었다.

## 2. 원격 GitHub read-back

```text
TEST_BLOB = cf49e64c65ca0e19231f475adc1722378a33365c
AUTHORITY_BLOB = c80219098d8b3b01db3550173f5ba377b9222a08
REVIEW_BLOB = ff2eaaa1e07a6133eaea9aae4d45ab2cbe377b27
SPEC_BLOB = 1b46ce06088c9fa0a2381ac228d5230d7cc1cbbb
ONBOARDING_BLOB = ff52c8ec8817583f0bd9c35cf4d302c6102b83fb
```

GitHub connector read-back에서 다음을 확인했다.

- 새 Decision ID와 부모 Decision ID.
- `PARTIAL_APPROVAL_7_OF_10`.
- 방패병·궁병 고정 후보.
- 같은 병영의 두 분기.
- 같은 비용 등급과 실제 골드 예약 규칙.
- 미선택 분기의 전역 잠금 금지.
- 혼합 소프트 카운터와 하드키 금지.
- 부모 온보딩 문서의 7/10 승격과 기존 pending 표식 제거.

## 3. GREEN

원격 read-back에서 확인한 체크포인트 7 계약 표식을 제한된 로컬 구조로 재구성해 전용 테스트를 실행했다.

```text
CHECKPOINT_7_TESTS = 8 PASS / 0 FAIL / 0 ERROR
PY_COMPILE = PASS
GREEN_EXIT_STATUS = 0
```

이 실행은 새 테스트가 요구하는 결정 표식과 금지 표식의 상호 일관성을 증명한다.

## 4. 검증 한계

```text
FULL_PRIVATE_REPOSITORY_CHECKOUT = UNAVAILABLE
EXACT_FULL_FILE_RECONSTRUCTION = NOT_RUN
FULL_PLANNING_CONTRACT_SUITE = NOT_RUN
FRESH_PHASE1_GODOT_TEST_ON_CURRENT_PR_HEAD = NOT_RUN
GITHUB_ACTIONS_GREEN = NOT_PROVEN
AUTOMATED_GREEN = NOT_PROVEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

따라서 `8 PASS`는 체크포인트 7 전용 표식 계약에만 적용한다. 저장소 전체 테스트 통과, 제품 구현 완료 또는 병합 준비 완료로 확대 해석하지 않는다.

## 5. 제품 경계

```text
PRODUCT_CODE = UNCHANGED
GAMEPLAY_SCENE_RESOURCE_DATA = UNCHANGED
ART_ASSETS = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
EXACT_NUMERICS = PENDING_SIMULATION
```

## 6. 후속 Gate

1. Google Sheet 동일 Decision ID 동기화와 bounded read-back.
2. 최신 main 대비 ahead/behind와 mergeability 재확인.
3. 특수병 병영 T1 무작위 선정·결과 공개 시점 GrillMe.
4. 전체 기획 계약 suite와 Phase 1 Godot 검증은 병합 전 별도 실행.
