# OMENWARD 플랫폼 출시·에셋 권리 Profile

> Base 정본: `alsdmlals4-eng/Base/docs/knowledge/game-development/PLATFORM_REVIEW_ASSET_RIGHTS_AND_REFERENCE_PRODUCTION_GUIDE.md`
> 기준 main: `6b23ca2bb627827651a42ba6db01829e44ee8a14`

현재 기획 정본에는 최종 출시 플랫폼이 확정되어 있지 않다. 저장소명·장르·도구만으로 플랫폼을 추론하지 않는다.

## 전략

```yaml
rating_strategy: LOWEST_VIABLE_RATING
adult_only_avoidance: AVOID_ADULTS_ONLY
content_rating_target: UNASSIGNED_PENDING_REPRESENTATIVE_BUILD
rating_candidate_range: ALL_OR_12_CANDIDATE
target_audience: UNDECIDED
platform_decision: PLATFORM_DECISION_REQUIRED
platforms:
  PC: UNDECIDED
  Steam: UNDECIDED_EVALUATION_ROW
  STOVE: UNDECIDED_EVALUATION_ROW
  Android: UNDECIDED
  Google_Play: UNDECIDED_EVALUATION_ROW
```

플랫폼 결정 전에는 특정 상점 출시 준비 완료를 주장하지 않는다. 청소년이용불가·18+는 기본적으로 피하되, 전투·암살자 침투·전장 압박·마법 연출의 실제 강도는 대표 빌드에서 정직하게 공개한다.

## 콘텐츠 위험 초안

| Risk | 현재 관찰 | 상태 |
|---|---|---|
| violence | 병력 전투·전술·방어선 붕괴 | 대표 빌드 미확인 |
| horror / sexual content / language / drugs / crime | 전수 근거 부족 | UNVERIFIED |
| gambling/simulated gambling | 룰렛 제어가 있으나 과금·사행성 관계 미확정 | UNVERIFIED |
| ads/IAP | 플랫폼·사업 모델 미확정 | UNDECIDED |
| UGC/online interaction | 확정 근거 없음 | UNDECIDED |
| AI-generated/live-generated content | 제작 자산별 증빙 필요 | UNVERIFIED |

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

## Gate

플랫폼 결정, 필요한 권리, 약관·계약 버전, OSS 의무, AI 입력 권리, build/store/questionnaire 일치 중 하나라도 미확인이면 `RELEASE_BLOCKED_UNVERIFIED`다.

```text
PLATFORM_DECISION_REQUIRED
RUNTIME_ASSET_USE_CHECKED: NOT_RUN
BUILD_STORE_CONSISTENCY_CHECKED: NOT_RUN
PLATFORM_SUBMISSION_NOT_RUN
FINAL_RATING: NOT_ASSIGNED
LEGAL_REVIEW_NOT_PERFORMED
```
