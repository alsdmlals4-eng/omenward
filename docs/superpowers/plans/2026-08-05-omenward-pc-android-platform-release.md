# OMENWARD PC·Android 플랫폼 정본화 구현 계획

> Decision: `OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1`

**목표:** PC(Steam)와 Android(Google Play)를 승인된 지원 범위로 고정하되 플랫폼별 출시 PASS, 동시 출시, STOVE 초기 출시, iOS, 최종 등급·법률·제출 완료를 허위 확정하지 않는다.

**구조:** 플랫폼 책임 원본을 신설하고 Profile·Evidence Pack·AGENTS를 그 원본으로 라우팅한다. 계약 테스트는 승인된 플랫폼, 단계적 출시, 세 Gate 분리, 실패 폐쇄 증거를 검증한다. Google Sheet에는 같은 Decision ID를 결정 원장·출시 로드맵·변경이력에 기록한다.

## Task 1 — RED 계약

**파일**
- 수정: `tests/python/test_platform_release_asset_rights_contract.py`

1. 플랫폼 책임 원본 파일 존재를 요구한다.
2. `APPROVED_DUAL_PLATFORM`, `STAGED_CROSS_PLATFORM`, PC·Steam·Android·Google Play 승인, STOVE 2차 후보, iOS 범위 제외를 요구한다.
3. `COMMON_PLATFORM_GATE`, `PC_RELEASE_GATE`, `MOBILE_RELEASE_GATE`를 요구한다.
4. 기존 main 문서에서 테스트가 실패하는지 전용 GitHub Actions로 확인한다.

## Task 2 — GREEN 정본

**파일**
- 신설: `docs/APPROVED_PC_ANDROID_PLATFORM_RELEASE_AUTHORITY_2026-08-05.md`
- 수정: `docs/PLATFORM_RELEASE_AND_ASSET_RIGHTS_PROFILE.md`
- 수정: `docs/GAME_RELEASE_COMPLIANCE_EVIDENCE_PACK.md`
- 수정: `AGENTS.md`
- 수정: `.github/workflows/platform-release-asset-rights.yml`

1. 동일 Decision ID와 승인 범위를 모든 책임 문서에 기록한다.
2. Steam은 PC 대표 상점, STOVE는 별도 Gate가 필요한 2차 후보로 구분한다.
3. Android·Google Play는 지원 범위로 승인하되 제출 준비 완료로 표시하지 않는다.
4. iOS와 동시 출시는 현 범위에서 제외한다.
5. 실제 자산 감사·런타임 검증·상점 제출·최종 등급·법률 검토는 NOT_RUN/NOT_ASSIGNED로 유지한다.
6. CI path filter에 새 책임 원본을 추가한다.

## Task 3 — Sheet 동기화

**대상**
- `02_현재_확정결정!A66:M66`
- `90_본제작_출시_사업!A9:H9`
- `99_변경이력!A77:H77`

1. GitHub 최종 PR head와 PR 번호가 확정된 뒤 기록한다.
2. 세 범위에 `OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1`를 사용한다.
3. 기존 B0004·PR #142·Grill Me 카운터 셀은 수정하지 않는다.
4. 쓰기 후 세 범위를 다시 읽어 Decision ID·head·상태를 검증한다.

## Task 4 — 검증과 PR

1. 전용 계약 workflow PASS.
2. 저장소 필수 CI PASS.
3. `git diff --check` PASS.
4. PR 변경 파일에 제품 코드·Scene·Resource·게임 데이터가 없는지 확인한다.
5. 리뷰·댓글·충돌·차단 표식을 확인한다.
6. Ready for review로 전환하되 사용자 병합 승인 전 병합하지 않는다.
