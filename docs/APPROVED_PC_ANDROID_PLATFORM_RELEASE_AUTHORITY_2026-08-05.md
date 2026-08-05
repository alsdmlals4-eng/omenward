# OMENWARD PC·Android 플랫폼 출시 책임 원본

```yaml
document_status: CURRENT_APPROVED_PLATFORM_SCOPE
decision_id: OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1
approved_at: 2026-08-05
baseline_main: da382d52b4490acb8758a1683ea6c9e4f4bf388b
platform_decision: APPROVED_DUAL_PLATFORM
release_strategy: STAGED_CROSS_PLATFORM
simultaneous_release: SIMULTANEOUS_RELEASE_NOT_COMMITTED
product_code_authority: NONE
```

## 1. 승인 범위

```yaml
platforms:
  PC: COMMITTED
  Steam: COMMITTED_PRIMARY_STORE
  STOVE: SECONDARY_RELEASE_CANDIDATE
  Android: COMMITTED
  Google_Play: COMMITTED_PRIMARY_STORE
  iOS: NOT_CURRENT_SCOPE

stove_policy: STOVE_SECONDARY_RELEASE_CANDIDATE
```

- PC와 Android는 OMENWARD의 정식 지원 범위다.
- Steam은 PC 첫 출시 준비의 대표 상점이다.
- Google Play는 Android 첫 출시 준비의 대표 상점이다.
- STOVE는 PC 지원 범위 안의 2차 출시 후보이며 별도 상점 Gate 통과 전 출시 확정이 아니다.
- PC와 Android의 동시 출시는 확정하지 않는다. 구현·검증·사업 준비 결과에 따라 순차 출시할 수 있다.
- iOS는 현재 범위가 아니다. 별도 Decision 없이 암묵적으로 포함하지 않는다.

## 2. 공용 구조 원칙

PC판 완성 뒤 모바일로 억지 이식하지 않는다. 게임 규칙과 데이터는 공용 코어에 두고 다음 경계를 플랫폼 어댑터로 분리한다.

- 입력: 키보드·마우스·게임패드 / 터치
- 표현: 해상도·화면비·안전 영역·UI 밀도
- 저장·수명주기: 데스크톱 종료 / 모바일 일시정지·백그라운드·복귀
- 성능: PC 사양 / 모바일 메모리·발열·배터리
- 배포·SDK: Steam·STOVE / Android·Google Play

플랫폼 SDK가 전투 규칙·경제·저장 도메인 정본을 소유해서는 안 된다.

## 3. 독립 Gate

### COMMON_PLATFORM_GATE

- 게임 규칙·콘텐츠 데이터의 플랫폼 독립성
- 입력 추상화와 UI 어댑터 경계
- 저장 스키마와 결정론적 상태 호환성
- 해상도·화면비·안전 영역 정책
- 플랫폼 전용 SDK의 코어 침투 방지
- 에셋 권리·출처·OSS·AI·외주 증거

### PC_RELEASE_GATE

- 키보드·마우스·게임패드 조작 검증
- 창모드·전체화면·해상도·접근성 설정
- 최소·권장 사양과 성능 검증
- Steam build/store/questionnaire 일치
- STOVE는 별도 상점 요구사항과 배포 Gate

### MOBILE_RELEASE_GATE

- 터치 조작과 작은 화면 UX
- 다양한 화면비·노치·안전 영역
- 앱 일시정지·백그라운드·복귀와 저장 원자성
- 메모리·발열·배터리·저사양 성능
- Android 권한과 Google Play 대상 연령·Families·SDK·데이터·개인정보
- 광고·인앱결제가 도입될 경우 등급·상점 설명·실제 빌드 일치

```yaml
gate_transfer_policy: PASS_DOES_NOT_TRANSFER
COMMON_PLATFORM_GATE: NOT_RUN
PC_RELEASE_GATE: NOT_RUN
MOBILE_RELEASE_GATE: NOT_RUN
```

PC Gate PASS는 모바일 Gate PASS가 아니며, 반대도 동일하다.

## 4. 등급·권리·제출 경계

```yaml
rating_strategy: LOWEST_VIABLE_RATING
adult_only_avoidance: AVOID_ADULTS_ONLY
rating_candidate_range: ALL_OR_12_CANDIDATE
final_content_rating: NOT_ASSIGNED
asset_inventory_audit: NOT_RUN
runtime_asset_use_status: NOT_RUN
build_store_consistency_status: NOT_RUN
platform_submission_status: PLATFORM_SUBMISSION_NOT_RUN
legal_review_status: LEGAL_REVIEW_NOT_PERFORMED
release_decision: RELEASE_BLOCKED_UNVERIFIED
```

플랫폼 지원 범위 승인은 상점 제출 승인, 최종 등급, 법률 적합성, 자산 권리 완결, 제품 구현 완료를 의미하지 않는다. 대표 빌드와 증거가 없는 항목은 계속 실패 폐쇄한다.

## 5. 권위·동기화

- 운영 Profile: `docs/PLATFORM_RELEASE_AND_ASSET_RIGHTS_PROFILE.md`
- 에셋 권리 기록: `docs/ASSET_RIGHTS_AND_PROVENANCE_RECORD.md`
- 출시 증거 Pack: `docs/GAME_RELEASE_COMPLIANCE_EVIDENCE_PACK.md`
- 회귀 계약: `tests/python/test_platform_release_asset_rights_contract.py`
- Sheet 운영 미러: `02_현재_확정결정`, `90_본제작_출시_사업`, `99_변경이력`

진행 중 PR #142의 온보딩 정본·Grill Me 카운터와 이 플랫폼 운영 Decision은 독립이다.
