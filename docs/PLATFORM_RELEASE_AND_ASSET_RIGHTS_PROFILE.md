# OMENWARD 플랫폼 출시·에셋 권리 Profile

> Base 정본: `alsdmlals4-eng/Base/docs/knowledge/game-development/PLATFORM_REVIEW_ASSET_RIGHTS_AND_REFERENCE_PRODUCTION_GUIDE.md`
> 플랫폼 책임 원본: `docs/APPROVED_PC_ANDROID_PLATFORM_RELEASE_AUTHORITY_2026-08-05.md`
> Decision ID: `OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1`
> 기준 main: `da382d52b4490acb8758a1683ea6c9e4f4bf388b`

PC와 Android를 정식 지원 범위로 승인한다. 이 승인은 동시 출시, 상점 제출 준비 완료, 최종 등급, 법률 검토, 제품 구현 완료를 의미하지 않는다.

## 전략

```yaml
decision_id: OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1
rating_strategy: LOWEST_VIABLE_RATING
adult_only_avoidance: AVOID_ADULTS_ONLY
content_rating_target: UNASSIGNED_PENDING_REPRESENTATIVE_BUILD
rating_candidate_range: ALL_OR_12_CANDIDATE
target_audience: UNDECIDED_PENDING_REPRESENTATIVE_BUILD
platform_decision: APPROVED_DUAL_PLATFORM
release_strategy: STAGED_CROSS_PLATFORM
simultaneous_release: SIMULTANEOUS_RELEASE_NOT_COMMITTED
platforms:
  PC: COMMITTED
  Steam: COMMITTED_PRIMARY_STORE
  STOVE: SECONDARY_RELEASE_CANDIDATE
  Android: COMMITTED
  Google_Play: COMMITTED_PRIMARY_STORE
  iOS: NOT_CURRENT_SCOPE
```

Steam은 PC 대표 상점이고 Google Play는 Android 대표 상점이다. STOVE는 별도 상점 Gate가 필요한 2차 출시 후보다. iOS와 동시 출시는 별도 Decision 없이 포함하지 않는다.

청소년이용불가·18+는 기본적으로 피하되, 전투·암살자 침투·전장 압박·마법 연출의 실제 강도는 대표 빌드에서 정직하게 공개한다.

## 콘텐츠 위험 초안

| Risk | 현재 관찰 | 상태 |
|---|---|---|
| violence | 병력 전투·전술·방어선 붕괴 | 대표 빌드 미확인 |
| horror / sexual content / language / drugs / crime | 전수 근거 부족 | UNVERIFIED |
| gambling/simulated gambling | 룰렛 제어가 있으나 과금·사행성 관계 미확정 | UNVERIFIED |
| ads/IAP | 사업 모델 미확정 | UNDECIDED |
| UGC/online interaction | 확정 근거 없음 | UNDECIDED |
| AI-generated/live-generated content | 제작 자산별 증빙 필요 | UNVERIFIED |

## 플랫폼 Gate

```yaml
COMMON_PLATFORM_GATE: NOT_RUN
PC_RELEASE_GATE: NOT_RUN
MOBILE_RELEASE_GATE: NOT_RUN
gate_transfer_policy: PASS_DOES_NOT_TRANSFER
```

- `COMMON_PLATFORM_GATE`: 공용 규칙·데이터, 입력 추상화, 저장 호환성, 화면비, SDK 격리, 권리 증거.
- `PC_RELEASE_GATE`: PC 입력·화면 설정·성능·Steam, 그리고 별도 STOVE 평가.
- `MOBILE_RELEASE_GATE`: 터치 UX·안전 영역·앱 수명주기·모바일 성능·Android·Google Play 정책.

한 플랫폼의 PASS를 다른 플랫폼에 전이하지 않는다.

## 자산·참조 기반 제작

음악·효과음, 폰트, 캐릭터·일러스트·UI, 3D·애니메이션, 플러그인·에셋, OSS, AI 출력·약관, 외주, 성우·작곡·번역 계약을 자산별로 기록한다.

```text
lawful reference source
→ 기능·구조·정보 흐름·일반 제작 원리
→ forbidden_expression
→ OMENWARD 고유 reference_brief
→ 독립 working files·final_asset_record
→ similarity and rights review
```

원본을 조금 바꾸거나 AI로 재생성했다는 이유만으로 독립 자산으로 판정하지 않는다.

## 실패 폐쇄 Gate

플랫폼별 구현·검증, 필요한 권리, 약관·계약 버전, OSS 의무, AI 입력 권리, build/store/questionnaire 일치 중 하나라도 미확인이면 `RELEASE_BLOCKED_UNVERIFIED`다.

```text
APPROVED_DUAL_PLATFORM / STAGED_CROSS_PLATFORM
COMMON_PLATFORM_GATE: NOT_RUN
PC_RELEASE_GATE: NOT_RUN
MOBILE_RELEASE_GATE: NOT_RUN
RUNTIME_ASSET_USE_CHECKED: NOT_RUN
BUILD_STORE_CONSISTENCY_CHECKED: NOT_RUN
PLATFORM_SUBMISSION_NOT_RUN
FINAL_RATING: NOT_ASSIGNED
LEGAL_REVIEW_NOT_PERFORMED
RELEASE_BLOCKED_UNVERIFIED
```
