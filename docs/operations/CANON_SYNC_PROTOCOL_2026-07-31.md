# 오멘워드 즉시 기획 정본 동기화 프로토콜

- 결정 ID: `OMW-DEC-20260731-CANON-SYNC-V1`
- 승인일: `2026-07-31`
- 상태: `USER_APPROVED_PROJECT_WORK_RULE`
- 적용 범위: 주요 변경사항, 사용자 승인 결정, GitHub 권위 문서, 계획 데이터, 연결 Google Sheet
- 제품 코드 권한: `NONE`
- PR 병합 권한: `NONE`

이 문서는 주요 변경사항과 승인된 내용을 GitHub 기획 정본과 연결된 Google Sheet에 같은 결정 ID로 즉시 동기화하는 운영 규칙을 소유한다.

---

## 1. 적용 트리거

다음이 발생하면 별도 요청을 기다리지 않고 정본 동기화를 수행한다.

1. 사용자가 주요 기획안을 확정·승인.
2. 새 시스템·핵심 규칙·콘텐츠 구조·UX 흐름이 승인.
3. 기존 핵심 계약을 대체하거나 우선순위를 바꾸는 결정.
4. 플레이 세션, 성장, 난이도, 저장, 경제, 콘텐츠 생산 구조의 중대한 변경.
5. 독립·적대적 검토로 승인 정본의 수정이 확정.

다음은 원칙적으로 즉시 동기화 대상이 아니다.

- 승인되지 않은 제안과 브레인스토밍 후보.
- 정확한 수치가 미확정인 가설.
- 문장 교정, 오탈자, 링크와 표 정리만 수행한 경우.
- 연구·벤치마킹 결과 자체. 단, 그 결과로 설계가 승인되면 승인 결정은 동기화한다.

---

## 2. 결정 ID 규칙

주요 결정은 하나의 원자적 의미 단위마다 ID 하나를 부여한다.

```text
OMW-DEC-YYYYMMDD-<SEMANTIC-SLUG>-V<REVISION>
```

예:

- `OMW-DEC-20260731-CONTENT-MANIFEST-V1`
- `OMW-DEC-20260731-CANON-SYNC-V1`

규칙:

- GitHub와 Google Sheet에서 문자열을 변경하지 않는다.
- 서로 다른 결정을 한 ID로 합치지 않는다.
- 승인 내용이 의미적으로 대체되면 기존 행을 삭제하지 않고 `V2` 또는 새 의미 ID를 만든다.
- 대체 관계는 GitHub 결정 원장과 Sheet `대체 Decision` 열에 기록한다.
- 단순 문구 보정은 새 ID를 만들지 않고 기존 결정의 sync ledger에 남길 수 있다.

---

## 3. 권위 계층

동기화 시 다음 계층을 함께 확인한다.

```text
최신 사용자 승인
→ PROJECT_CORE.md
→ DOCUMENTATION_MAP.md
→ 분야별 APPROVED 계약
→ PROJECT_CANON_DECISION_LEDGER.md
→ DECISIONS_PENDING.md
→ Google Sheet 결정 원장·분야 탭·변경 이력
→ 구현 상태와 실제 코드·테스트
```

분야별 계약이 세부 규칙을 소유하고, `PROJECT_CORE.md`는 제품 불변 조건과 현재 범위를 요약한다. `DOCUMENTATION_MAP.md`는 어느 문서가 책임 원본인지 라우팅한다.

---

## 4. 즉시 동기화 절차

```text
1. 승인 문장과 범위 고정
2. 결정 ID 발급
3. 영향받는 GitHub 권위 문서 탐색
4. 연결된 Sheet 탭·헤더·기존 행 탐색
5. 분야별 APPROVED 계약 기록
6. Project Core·Documentation Map·Pending 갱신
7. GitHub authority commit 생성
8. 같은 결정 ID로 Sheet 결정 원장·분야 데이터 기록
9. Sheet 변경 이력에 범위와 authority commit 기록
10. GitHub sync ledger에 Sheet 범위와 검증 결과 기록
11. GitHub·Sheet 재조회
12. 사용자에게 문서 경로·Sheet 범위·commit 보고
```

동기화는 같은 응답의 작업 흐름에서 수행한다. 비동기 작업이나 추후 반영을 약속하지 않는다.

---

## 5. Google Sheet 쓰기 권한

사용자는 승인된 주요 결정의 기획 정본 동기화를 위해 연결 Google Sheet 쓰기를 승인했다.

허용:

- `02_현재_확정결정` 결정 원장 추가·대체 상태 갱신.
- 승인 결정과 직접 연결된 분야 탭 갱신.
- `99_변경이력`에 변경 위치·GitHub commit·재검증 결과 기록.
- 프로젝트 허브의 현재 Stage·다음 게이트·동기화 상태 갱신.

금지:

- 승인되지 않은 후보를 `CURRENT`로 기록.
- 후속 시뮬레이션이 필요한 수치를 임의 확정.
- 제품 코드 구현 상태를 `BUILT`, `PROVEN`, `LOCKED`로 과장.
- 기존 행을 근거 없이 삭제하거나 이력을 덮어쓰기.
- 사용자 승인 없이 Sheet 구조를 대규모 재편.

---

## 6. 동기화 상태

| 상태 | 의미 |
|---|---|
| `SYNCED_TO_PR_HEAD` | GitHub 기획 브랜치와 Sheet가 같은 결정 ID·내용을 보유 |
| `SYNCED_TO_MAIN` | 승인 PR 병합 후 main commit까지 Sheet에 재기록 |
| `GITHUB_SYNC_PENDING` | Sheet 기록은 있으나 GitHub 권위 commit 미완료 |
| `SHEET_SYNC_PENDING` | GitHub 권위 commit은 있으나 Sheet 기록 미완료 |
| `SYNC_CONFLICT` | 같은 ID의 의미·상태·경로가 서로 불일치 |
| `SUPERSEDED` | 새 결정 ID가 이전 결정을 명시적으로 대체 |

Draft PR 단계의 commit을 Sheet에 기록할 때는 `PR #번호 / head SHA / NOT_MERGED`를 함께 표시한다. 병합 뒤에는 main SHA로 재동기화한다.

---

## 7. 충돌 처리

GitHub와 Sheet가 충돌하면 구현·Codex 인계를 중단한다.

1. 동일 결정 ID가 다른 의미를 가진 경우 `SYNC_CONFLICT`.
2. 최신 사용자 승인 원문과 분야별 APPROVED 계약을 기준으로 판정.
3. 어느 한쪽을 조용히 덮어쓰지 않는다.
4. 정정 위치와 이유를 sync ledger와 Sheet 변경 이력에 남긴다.
5. 재조회 후에만 `SYNCED_TO_PR_HEAD` 또는 `SYNCED_TO_MAIN`으로 복구한다.

---

## 8. 커밋·범위 증적

각 동기화는 다음을 남긴다.

```yaml
decision_id: string
github_authority_paths: []
github_authority_commit: sha
github_pr: number | null
sheet_id: string
sheet_ranges: []
sync_status: enum
verified_at: ISO-8601
verification_result: PASS | PARTIAL | FAIL
```

GitHub commit은 권위 문서 변경을 증명한다. Sheet는 자체 commit이 없으므로 `99_변경이력`과 GitHub sync ledger가 변경 범위·시각·GitHub commit을 상호 참조한다.

---

## 9. 벤치마킹 원칙과의 연결

새 시스템·핵심 규칙·콘텐츠 구조·UX 흐름은 먼저 `docs/operations/BENCHMARK_FIRST_PLANNING_RULE_2026-07-31.md`를 따른다.

```text
벤치마킹
→ 설계
→ 사용자 승인
→ 즉시 정본 동기화
```

벤치마킹 결과는 승인 전까지 정본이 아니다. 승인 이후에는 본 프로토콜에 따라 GitHub와 Sheet에 같은 결정 ID로 기록한다.

---

## 10. 실행 경계

```text
CANON_SYNC_AUTHORIZED
!= PRODUCT_CODE_AUTHORIZED
!= CODEX_EXECUTION_AUTHORIZED
!= PR_MERGE_AUTHORIZED
!= HUMAN_QA_COMPLETE
```

기획 정본 동기화는 문서와 계획 데이터의 일치를 위한 작업이다. Godot 코드, Scene, Resource, 제품 데이터 구현과 PR 병합은 별도 게이트를 유지한다.
