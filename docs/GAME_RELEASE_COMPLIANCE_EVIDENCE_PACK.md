# OMENWARD Game Release Compliance Evidence Pack

> 플랫폼 결정과 대표 빌드가 생긴 뒤 채운다. 현재 문서는 실제 제출·등급·법률 검토가 아니다.

```yaml
release_pack_id:
project: OMENWARD
repository: alsdmlals4-eng/omenward
baseline_commit:
target_build:
platform_decision: PLATFORM_DECISION_REQUIRED
status: DRAFT | IN_PROGRESS | READY_FOR_SUBMISSION | SUBMITTED | APPROVED | RETURNED | RELEASE_BLOCKED_UNVERIFIED
rating_strategy: LOWEST_VIABLE_RATING
adult_only_avoidance: AVOID_ADULTS_ONLY
content_rating_target: UNASSIGNED_PENDING_REPRESENTATIVE_BUILD
target_audience: UNDECIDED
```

## Platform evaluation rows

```yaml
Steam:
  status: UNDECIDED
  questionnaire_version_or_checked_at:
  build_store_questionnaire_consistency:
  ai_disclosure:
STOVE:
  status: UNDECIDED
  questionnaire_version_or_checked_at:
  build_store_questionnaire_consistency:
Google_Play:
  status: UNDECIDED
  questionnaire_version_or_checked_at:
  target_audience_declaration:
  families_policy_status:
  ads_sdk_data_privacy_status:
  build_store_questionnaire_consistency:
```

플랫폼이 확정되지 않았으므로 어느 행도 출시 약속이나 `READY_FOR_SUBMISSION`으로 해석하지 않는다.

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

플랫폼 미결정, 권리 `UNKNOWN/PROHIBITED`, 조건 이행 누락, reference-only 원본 포함, OSS 고지 누락, AI 입력 권리·약관·공개 누락, 계약 범위 누락, build/store/questionnaire 불일치, 민감 원본 공개는 `RELEASE_BLOCKED_UNVERIFIED`다.

```yaml
release_decision: RELEASE_BLOCKED_UNVERIFIED
runtime_asset_use_status: NOT_RUN
build_store_consistency_status: NOT_RUN
platform_submission_status: PLATFORM_SUBMISSION_NOT_RUN
legal_review_status: LEGAL_REVIEW_NOT_PERFORMED
```
