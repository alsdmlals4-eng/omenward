# 오멘워드 기획 정본 결정 원장

- 갱신일: `2026-08-01`
- 상태: `CURRENT_DECISION_LEDGER / PLANNING_ONLY / SYNC_VERIFIED`
- 동기화 프로토콜: `docs/operations/CANON_SYNC_PROTOCOL_2026-07-31.md`
- 누락 방지 게이트: `docs/operations/PROJECT_UNDERSTANDING_AND_OMISSION_PREVENTION_GATE_2026-08-01.md`
- 연결 Sheet ID: `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw`
- 제품 코드·Codex·병합: `NONE / BLOCKED / NOT_AUTHORIZED`

이 원장은 주요 승인 결정, 폐기·대체 상태, GitHub 권위 경로와 Google Sheet 위치를 같은 Decision ID로 연결한다. 현재 브랜치 head는 PR metadata가 소유하며 원장 안에 자기 자신의 최종 commit을 요구하지 않는다.

## 1. 현재 결정 요약

| Decision ID | 상태 | 요약 |
|---|---|---|
| `OMW-DEC-20260731-CONTENT-MANIFEST-V1` | `USER_APPROVED_PLAN` | 전장 1개·4막, Stage 20, 공세 8, 위험 4, 보스 3, 미션 12 |
| `OMW-DEC-20260731-CANON-SYNC-V1` | `CURRENT_PROJECT_WORK_RULE` | GitHub·Sheet 동일 Decision ID 동기화 |
| `OMW-DEC-20260731-DEFEAT-RETRY-V1` | `USER_APPROVED_DETAIL / EXACT_COSTS_PENDING` | Stage 5 이후 MapRun당 1회 유료 재시도 |
| `OMW-DEC-20260731-DANGER-BOSS-V1` | `USER_APPROVED_PLAN / EXACT_VALUES_PENDING` | Stage 5·10·15·20 위험 공세·보스 |
| `OMW-DEC-20260731-MID-IMAGE-REVIEW-V1` | `WORKFLOW_RETAINED / CURRENT_BATCH_REJECTED` | 화면별 이미지 검수 절차 유지 |
| `OMW-DEC-20260731-VISUAL-SCREEN-BOARD-V1` | `REJECTED_EVIDENCE / SUPERSEDED` | 잘못된 화면 보드 V1 재사용 금지 |
| `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1` | `CURRENT_PROJECT_WORK_RULE / CURRENT_USER_CONFIRMED_CANON` | 사실표·충돌 원장·전장 `6/3/0=30` |
| `OMW-DEC-20260801-BELU-IDENTITY-V1` | `CURRENT_USER_CONFIRMED_CANON` | 벨루·율비 동일 인물, 정본명 벨루 |

## 2. OMW-DEC-20260801-BELU-IDENTITY-V1

```yaml
decision_id: OMW-DEC-20260801-BELU-IDENTITY-V1
approved_at: 2026-08-01T05:15:00+09:00
status: CURRENT_USER_CONFIRMED_CANON
canonical_name_ko: 벨루
canonical_name_en: Belu
historical_alias_ko: 율비
identity_relation: SAME_CHARACTER
github_authority_paths:
  - docs/PROJECT_CORE.md
  - docs/DOCUMENTATION_MAP.md
  - docs/DECISIONS_PENDING.md
  - docs/design/APPROVED_BELU_GUIDE_IDENTITY_AND_NAMING_CONTRACT_2026-08-01.md
  - docs/images/VISUAL_REFERENCE_INDEX.md
  - docs/reviews/OMENWARD_COMPREHENSIVE_PROJECT_INTEGRITY_REVIEW_2026-08-01.md
github_authority_commit: 214cedf259ee9ad848117a33dd70d62c4293bf27
github_pr: 116
github_merge_state: NOT_MERGED
sheet_ranges:
  - 00_프로젝트_허브!G2:K2
  - 02_현재_확정결정!E2:E5
  - 02_현재_확정결정!L2:L5
  - 02_현재_확정결정!A13:L13
  - 04_누락_충돌_감사!D6:H13
  - 13_주요인물!A4:J4
  - 60_UX_UI_접근성!A9:J9
  - 70_아트_오디오_에셋!A5:J5
  - 99_변경이력!A13:H13
sheet_sync_status: SYNCED_TO_PR_HEAD
verified_at: 2026-08-01T05:15:00+09:00
verification_result: PASS
verification_evidence_commit: 5ba10618339f71336a63dee1435a53ead7014080
```

결정 내용:

- 기존 문서의 벨루와 사용자 첨부 `요정 율비 시안.png`의 캐릭터는 동일 인물이다.
- 제품 정본명은 `벨루 / Belu`다.
- `율비 / Yulbi`는 과거 시안 파일명·변경 이력의 역사 별칭으로만 보존한다.
- 신규 UI·대사·에셋·데이터·파일명은 `벨루 / Belu / belu`를 사용한다.
- 벨루는 설명·경고·결과 반응을 제공하되 건설·릴 조작·배치·전술 결정을 대신하지 않는다.
- 최종 픽셀 크기·애니메이션·음성·표정 조건·화면 배치는 후속 화면·에셋 명세 항목이다.

## 3. 프로젝트 무결성 정정 상태

```text
OPEN_P0: 0
BELU_IDENTITY_CONFLICT: VERIFIED_FIXED
PROJECT_CORE_REFRESH: VERIFIED
HISTORICAL_CURRENT_SHEET_CLASSIFICATION: VERIFIED
VISUAL_SCREEN_BOARD_V1: REJECTED_EVIDENCE
GENERATED_IMAGES: REJECTED_EVIDENCE
VISUAL_BINARY_MIGRATION: PENDING
LATEST_CONTRACT_RED_TEST_SPEC: NOT_WRITTEN
PRODUCT_CODE: NOT_AUTHORIZED
CODEX_EXECUTION: BLOCKED
RUNTIME_AND_HUMAN_QA: NOT_RUN
```

과거 Sheet 행 `PR97-VS`, `PR92-BUILDING`, `F-30`, `OMENWARD-EVP-001`은 삭제하지 않고 각각 `HISTORICAL_APPROVED_SOURCE`, `LEGACY_PROVEN`, `HISTORICAL_EVIDENCE`로 분류했다. 현재 정본 권한으로 사용하지 않는다.

## 4. 비주얼 결정 상태

```text
MID_IMAGE_REVIEW: WORKFLOW_RETAINED / CURRENT_BATCH_REJECTED
VISUAL_SCREEN_BOARD_V1: REJECTED_EVIDENCE / DO_NOT_REUSE
OM-IMG-005_TO_010: REJECTED / RESET_REQUIRED
NEW_IMAGE_GENERATION: BLOCKED_PENDING_SCREEN_BRIEF_APPROVAL
```

## 5. Sheet 재검증 결과

```text
DECISION_ID_MATCH: PASS
CANONICAL_NAME_BELU: PASS
HISTORICAL_ALIAS_YULBI: PASS
AUDIT_FINDING_CLOSED: PASS
HISTORICAL_CURRENT_CLASSIFICATION: PASS
AUTHORITY_COMMIT_MATCH: PASS
EXISTING_FORMATS_PRESERVED: PASS
SYNC_STATE: SYNCED_TO_PR_HEAD
```

## 6. 다음 작업 게이트

```text
최신 계약 Red 테스트 명세
→ Legacy 테스트 보존·교체·폐기 판정
→ 화면 명세 보드 V2
→ 대표 화면 중간 검수
→ 경제·Retry 비용·save schema
→ 독립 적대적 검토
→ 사용자 승인 구현 Plan
```

최신 계약 Red 테스트 명세 없이 Codex 제품 구현을 시작하지 않는다.
