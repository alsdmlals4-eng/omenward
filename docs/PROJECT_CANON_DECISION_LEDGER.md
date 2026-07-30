# 오멘워드 기획 정본 결정 원장

- 갱신일: `2026-07-31`
- 상태: `CURRENT_DECISION_LEDGER / PLANNING_ONLY / SYNC_VERIFIED`
- 동기화 프로토콜: `docs/operations/CANON_SYNC_PROTOCOL_2026-07-31.md`
- 연결 Sheet ID: `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw`
- 제품 코드 권한: `NONE`

이 원장은 주요 승인 결정의 동일 ID, GitHub 권위 경로, authority commit과 Google Sheet 위치를 연결한다. Sheet는 자체 Git commit이 없으므로 GitHub authority commit과 `99_변경이력`을 상호 참조한다.

---

## 1. 현재 결정

### OMW-DEC-20260731-CONTENT-MANIFEST-V1

```yaml
decision_id: OMW-DEC-20260731-CONTENT-MANIFEST-V1
approved_at: 2026-07-31T08:02:00+09:00
status: USER_APPROVED_PLAN
github_authority_paths:
  - docs/PROJECT_CORE.md
  - docs/DOCUMENTATION_MAP.md
  - docs/DECISIONS_PENDING.md
  - docs/design/APPROVED_VERTICAL_SLICE_CONTENT_MANIFEST_AND_MISSION_CARD_POOL_2026-07-31.md
github_authority_commit: 292a00d4aad3c836d5f3907e38c6496cc03d6c73
github_pr: 116
github_merge_state: NOT_MERGED
sheet_ranges:
  - 02_현재_확정결정!A6:L6
  - 30_데모범위_품질기준_제작기반!A4:H4
  - 40_핵심시스템_메인콘텐츠!A6:K6
  - 50_메인콘텐츠!A6:J7
  - 99_변경이력!A5:H5
sheet_sync_status: SYNCED_TO_PR_HEAD
verified_at: 2026-07-31T08:02:00+09:00
verification_result: PASS
```

승인 요약:

- 시스템 조합형 Manifest.
- 전장 1개·4막 상태.
- StageManifest 20, 일반 공세 템플릿 8, 위험 패키지 4, 보스 패키지 3.
- Tier 1 1종, Tier 2 10종, Tier 3 20전문화.
- 미션 카드 12장: 전선 4 / 설계 4 / 제약 4.
- Stage 6·11·16에서 2장 중 1장 또는 거절.
- 보상 종류는 골드·식량·추가 무료 회전.
- 시간제 미션·숨은 보상·실패 직접 페널티·미션 전용 경제 제외.

### OMW-DEC-20260731-CANON-SYNC-V1

```yaml
decision_id: OMW-DEC-20260731-CANON-SYNC-V1
approved_at: 2026-07-31T08:02:00+09:00
status: USER_APPROVED_PROJECT_WORK_RULE
github_authority_paths:
  - docs/PROJECT_CORE.md
  - docs/DOCUMENTATION_MAP.md
  - docs/operations/CANON_SYNC_PROTOCOL_2026-07-31.md
  - docs/PROJECT_CANON_DECISION_LEDGER.md
github_authority_commit: 292a00d4aad3c836d5f3907e38c6496cc03d6c73
github_pr: 116
github_merge_state: NOT_MERGED
sheet_ranges:
  - 00_프로젝트_허브!E2:K2
  - 02_현재_확정결정!A7:L7
  - 99_변경이력!A6:H6
sheet_sync_status: SYNCED_TO_PR_HEAD
verified_at: 2026-07-31T08:02:00+09:00
verification_result: PASS
```

승인 요약:

- 주요 변경·승인 결정에 의미형 결정 ID 발급.
- GitHub 권위 문서와 연결 Sheet에 같은 ID로 즉시 반영.
- 변경 위치·authority commit·sync ledger commit·재검증 결과 기록.
- Draft PR head 동기화와 main 동기화를 구분.
- 정본 충돌 시 Codex·구현 인계 중단.

---

## 2. 검증 증적

### Google Sheet 재조회

다음 범위를 값·서식과 함께 재조회했다.

- `02_현재_확정결정!A6:L7`
- `30_데모범위_품질기준_제작기반!A4:H4`
- `40_핵심시스템_메인콘텐츠!A6:K6`
- `50_메인콘텐츠!A6:J7`
- `99_변경이력!A5:H6`
- `00_프로젝트_허브!E2:K2`

검증 결과:

- 두 결정 ID가 GitHub와 Sheet에서 동일하다.
- authority commit `292a00d4aad3c836d5f3907e38c6496cc03d6c73`이 결정 원장과 변경 이력에 기록됐다.
- Draft PR 상태는 `NOT_MERGED`, 동기화 상태는 `SYNCED_TO_PR_HEAD`로 구분됐다.
- 새 행은 기존 행의 줄바꿈·상단 정렬·글꼴 크기 서식을 유지한다.
- 승인되지 않은 Threat·보상량·경제 수치는 기록하지 않았다.

초기 일괄 쓰기 요청은 Google Sheets API에서 원자적으로 거부되어 부분 데이터가 생성되지 않았다. 이후 범위별 값 쓰기로 전환하고 전체 범위를 재조회해 최종 상태를 검증했다.

---

## 3. 현재 동기화 상태

```text
GITHUB_AUTHORITY: WRITTEN
GOOGLE_SHEET: WRITTEN
SYNC_VERIFICATION: PASS
SYNC_STATE: SYNCED_TO_PR_HEAD
PR_MERGE: NOT_AUTHORIZED
PRODUCT_CODE: NOT_AUTHORIZED
CODEX_EXECUTION: BLOCKED
```

PR #116이 사용자 최종 승인 뒤 병합되면 Sheet의 GitHub SHA와 상태를 main commit 기준 `SYNCED_TO_MAIN`으로 다시 동기화해야 한다.
