# OMENWARD Game Release Compliance Evidence Pack

> PC·Android 지원 범위는 승인됐지만 현재 문서는 실제 제출·등급·법률 검토가 아니다. 모든 증거 Gate는 대표 빌드로 별도 판정한다.

```yaml
release_pack_id: OMW-REL-EVIDENCE-DRAFT-001
decision_id: OMW-DEC-20260805-PLATFORM-PC-ANDROID-V1
project: OMENWARD
repository: alsdmlals4-eng/omenward
baseline_commit: da382d52b4490acb8758a1683ea6c9e4f4bf388b
target_build: NOT_AVAILABLE
platform_decision: APPROVED_DUAL_PLATFORM
release_strategy: STAGED_CROSS_PLATFORM
simultaneous_release: SIMULTANEOUS_RELEASE_NOT_COMMITTED
status: RELEASE_BLOCKED_UNVERIFIED
rating_strategy: LOWEST_VIABLE_RATING
adult_only_avoidance: AVOID_ADULTS_ONLY
content_rating_target: UNASSIGNED_PENDING_REPRESENTATIVE_BUILD
target_audience: UNDECIDED_PENDING_REPRESENTATIVE_BUILD
```

## Platform evidence rows

```yaml
Steam:
  scope: COMMITTED_PRIMARY_STORE
  submission_status: PLATFORM_SUBMISSION_NOT_RUN
  questionnaire_version_or_checked_at:
  build_store_questionnaire_consistency: NOT_RUN
  ai_disclosure:
STOVE:
  scope: SECONDARY_RELEASE_CANDIDATE
  release_commitment: STORE_GATE_REQUIRED
  submission_status: PLATFORM_SUBMISSION_NOT_RUN
  questionnaire_version_or_checked_at:
  build_store_questionnaire_consistency: NOT_RUN
Google_Play:
  scope: COMMITTED_PRIMARY_STORE
  submission_status: PLATFORM_SUBMISSION_NOT_RUN
  questionnaire_version_or_checked_at:
  target_audience_declaration: NOT_RUN
  families_policy_status: NOT_RUN
  ads_sdk_data_privacy_status: NOT_RUN
  build_store_questionnaire_consistency: NOT_RUN
iOS:
  scope: NOT_CURRENT_SCOPE
```

지원 범위 승인을 `READY_FOR_SUBMISSION`이나 상점 승인으로 해석하지 않는다. STOVE는 별도 상점 Gate 전 초기 출시 약속이 아니다.

## Independent platform Gates

```yaml
COMMON_PLATFORM_GATE:
  status: NOT_RUN
  evidence:
PC_RELEASE_GATE:
  status: NOT_RUN
  evidence:
MOBILE_RELEASE_GATE:
  status: NOT_RUN
  evidence:
gate_transfer_policy: PASS_DOES_NOT_TRANSFER
```

각 Gate는 독립 판정한다. PC 결과를 Android에, Android 결과를 PC에 전이하지 않는다.

## Risk matrix

| Risk | Present | Context/evidence | Platform answer | Mitigation | Status |
|---|---|---|---|---|---|
| violence |  |  |  |  |  |
| sexual content |  |  |  |  |  |
| horror |  |  |  |  |  |
| language |  |  |  |  |  |
| drugs/alcohol/tobacco |  |  |  |  |  |
| crime |  |  |  |  |  |
| gambling/simulated gambling |  |  |  |  |  |
| ads/IAP |  |  |  |  |  |
| UGC/online interaction |  |  |  |  |  |
| AI-generated/live-generated content |  |  |  |  |  |

```yaml
build_store_questionnaire_consistency:
  target_build_matches_review_build:
  store_description_matches_features:
  screenshots_and_video_match_build:
  ads_and_offers_match_content_rating:
  online_ugc_features_disclosed:
  ai_content_disclosed:
  result: PASS | REVISION_REQUIRED | RELEASE_BLOCKED_UNVERIFIED

asset_rights_coverage:
  MUSIC_SFX:
  FONT:
  CHARACTER_ILLUSTRATION:
  MODEL_3D_ANIMATION:
  PLUGIN_ASSET:
  OPEN_SOURCE_LIBRARY:
  AI_OUTPUT_MODEL_TERMS:
  OUTSOURCING_CONTRACT:
  VOICE_COMPOSER_TRANSLATOR_CONTRACT:
```

권리 `UNKNOWN/PROHIBITED`, 조건 이행 누락, reference-only 원본 포함, OSS 고지 누락, AI 입력 권리·약관·공개 누락, 계약 범위 누락, build/store/questionnaire 불일치, 민감 원본 공개는 `RELEASE_BLOCKED_UNVERIFIED`다.

```yaml
release_decision: RELEASE_BLOCKED_UNVERIFIED
asset_inventory_audit: NOT_RUN
runtime_asset_use_status: NOT_RUN
build_store_consistency_status: NOT_RUN
platform_submission_status: PLATFORM_SUBMISSION_NOT_RUN
final_content_rating: NOT_ASSIGNED
legal_review_status: LEGAL_REVIEW_NOT_PERFORMED
```
