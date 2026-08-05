# OMENWARD PC·Android 플랫폼 출시 정본 설계

- 작성일: 2026-08-05
- Decision ID: `OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1`
- 기준 main: `da382d52b4490acb8758a1683ea6c9e4f4bf388b`
- 범위: 플랫폼·출시 운영 정본, 증거 Gate, Google Sheet 동기화
- 제외: 제품 코드, Scene, Resource, 게임 데이터, 콘텐츠 수치, 실제 제출·등급·법률 판정

## 문제

PR #143은 플랫폼 검토·에셋 권리·증거 구조를 설치했지만 OMENWARD의 플랫폼 행은 모두 `UNDECIDED`로 남아 있다. 이 상태에서는 공용 코어, 입력·화면·저장·SDK 경계와 플랫폼별 출시 검증의 책임을 계획할 수 없다.

## 승인된 방향

```yaml
decision_id: OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1
platform_decision: APPROVED_DUAL_PLATFORM
release_strategy: STAGED_CROSS_PLATFORM
simultaneous_release: NOT_COMMITTED
pc:
  status: COMMITTED
  primary_store: STEAM
  secondary_store: STOVE_SECONDARY_RELEASE_CANDIDATE
mobile:
  status: COMMITTED
  primary_os: ANDROID
  primary_store: GOOGLE_PLAY
ios:
  status: NOT_CURRENT_SCOPE
```

PC와 Android 지원 범위는 승인하지만 동시 출시, STOVE 초기 출시, iOS 지원, 최종 등급, 사업 모델은 자동 승인하지 않는다. Steam은 PC 첫 출시 준비의 대표 상점이고 STOVE는 별도 상점 Gate 통과 뒤 가능한 2차 후보이다.

## Gate 구조

- `COMMON_PLATFORM_GATE`: 게임 규칙·데이터의 플랫폼 독립성, 입력 추상화, 저장 호환성, 화면비·해상도, 플랫폼 SDK 격리, 자산 권리.
- `PC_RELEASE_GATE`: 키보드·마우스·게임패드, 창/전체화면, 성능·사양, Steam build/store/questionnaire, STOVE 별도 평가.
- `MOBILE_RELEASE_GATE`: 터치 UX, 작은 화면·안전 영역, 백그라운드 복귀, 메모리·발열·배터리, Android 권한, Google Play 대상 연령·SDK·데이터·개인정보.

한 플랫폼의 PASS는 다른 플랫폼의 PASS를 의미하지 않는다. 어느 Gate라도 미확인이면 `RELEASE_BLOCKED_UNVERIFIED`를 유지한다.

## 권위와 동기화

- GitHub 책임 원본: `docs/APPROVED_PC_ANDROID_PLATFORM_RELEASE_AUTHORITY_2026-08-05.md`
- 운영 Profile: `docs/PLATFORM_RELEASE_AND_ASSET_RIGHTS_PROFILE.md`
- 제출 증거 Pack: `docs/GAME_RELEASE_COMPLIANCE_EVIDENCE_PACK.md`
- 라우팅: `AGENTS.md`
- 회귀 계약: `tests/python/test_platform_release_asset_rights_contract.py`
- Sheet 미러: `02_현재_확정결정`, `90_본제작_출시_사업`, `99_변경이력`

Google Sheet는 GitHub 정본의 운영 미러이며 독립 권위가 아니다. 진행 중 PR #142의 온보딩 결정과 Grill Me 카운터를 변경하지 않는다.

## 실패 폐쇄 상태

다음은 계속 미완료로 유지한다.

```yaml
asset_inventory_audit: NOT_RUN
runtime_asset_use_status: NOT_RUN
build_store_consistency_status: NOT_RUN
platform_submission_status: PLATFORM_SUBMISSION_NOT_RUN
final_content_rating: NOT_ASSIGNED
legal_review_status: LEGAL_REVIEW_NOT_PERFORMED
```
