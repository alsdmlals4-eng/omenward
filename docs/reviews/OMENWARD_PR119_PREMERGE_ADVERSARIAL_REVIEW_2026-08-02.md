# OMENWARD PR #119 병합 직전 적대적 검토

```yaml
review_date: 2026-08-02
review_type: ADVERSARIAL_PREMERGE_REVIEW
pr: 119
base: main
base_sha: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
evidence_head_before_review_commit: bde257d99af57c94fe79156d94ae2a39cb2474d0
merge_authorization: USER_APPROVED
proposed_merge_method: squash
product_code_authority: NONE
final_head_revalidation: REQUIRED_AFTER_THIS_REVIEW_COMMIT
```

## 1. 검토 범위

현재 승인 묶음:

- `OMW-DEC-20260802-CANON-RECOVERY-V1`
- `OMW-DEC-20260802-META-PROGRESSION-ROLE-V1`
- `OMW-DEC-20260802-WORLD-RUN-MOTIVATION-V1`
- `OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1`
- `OMW-DEC-20260802-WORLD-OMENWARD-POLITICAL-ROLE-V1`
- `OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1`
- `OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1`
- `OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2` current local restore.

현재 묶음의 Grill Me 카운트는 4건이다. 사용자가 조기 병합을 명시했으므로 10건 전이라도 preflight와 병합을 수행한다.

## 2. GitHub 상태 증거

`main...gpt/omenward-canon-recovery-20260802` 비교:

```text
status: ahead
base: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
ahead_by: 69
behind_by: 0
changed_files: 16
product_paths_changed: 0
```

변경 경로는 모두 `docs/` 아래다.

- Context·Documentation Map·Decision Ledger·Workbook.
- recovery audit.
- world/meta/political/auxiliary/Screen Board 승인 문서.
- merge cadence 운영 문서.
- Superpowers spec·plans.

다음 경로는 변경되지 않았다.

```text
scripts/
scenes/
data/
resources/
assets/
addons/
tests/
tools/
project.godot
```

PR 상태:

```text
state: open
draft: true
mergeable: true
merged: false
base: main
comments: 0
review_submissions: 0
unresolved_review_threads: 0
```

Draft는 preflight 완료 후 Ready로 전환한다.

## 3. current authority 경로 감사

직접 존재를 확인한 신규 current authority:

- `docs/design/APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md`
- `docs/operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md`

기존 current authority:

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/HANDOFF_CONTEXT.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`

PR #116은 `CLOSED_NOT_MERGED / HISTORICAL_APPROVAL_EVIDENCE`로 유지한다. PR #116 경로를 current local authority로 사용하지 않는다.

### 발견·수정

- `Screen Board V2`가 Ledger와 Sheet에서 current처럼 참조됐지만 current branch에 없었다.
- 최신 Base v9.4·정치 역할·보조 허브 금지선에 맞춰 current local authority로 선별 복구했다.
- GDD 요약이 Base v9.1·v9.3 미채택·CI 실패 상태를 유지하고 있었다.
- Base v9.4·현재 세계·Meta·preflight 상태로 갱신했다.

판정: `RESOLVED_BEFORE_MERGE`.

## 4. Google Sheet 감사

Workbook:

```text
spreadsheet_id: 1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw
role: USER_FACING_GDD_WORKSPACE
canonical_authority: GITHUB
required_tabs: 25
```

갱신·재조회 범위:

- `00_프로젝트_허브!E2:L2`
- `01_작업순서!A13:N15`
- `02_현재_확정결정!A22:M24`
- `04_누락_충돌_감사!A43:H53`
- `05_GDD_요약!A4:J9`
- `11_세계관!A16:H18`
- `13_주요인물!A2:J2`
- `14_조연_세력_관계!A5:J8`
- `41_성장_경제!A14:I18`
- `60_UX_UI_접근성!A11:J12`
- `99_변경이력!A22:H24`

확인:

- 세 신규 Decision ID가 GitHub와 일치.
- 정치 권한의 범위·금지 권한이 일치.
- 주점·병영·연구·Hero+ 노드와 공정성 금지선이 일치.
- Grill Me 4건·조기 병합·향후 10건 cadence가 일치.
- exact values·simulation·runtime·human validation은 pending으로 유지.
- Sheet-only 정본 승격 없음.

판정: `CONTENT_READBACK_PASS / FINAL_HEAD_UPDATE_REQUIRED`.

## 5. CI 감사

증거 head `bde257d99af57c94fe79156d94ae2a39cb2474d0`:

```text
Validate Project Core Documentation: PASS / run 514
Validate Omenward GDD Sheet Adoption: PASS / run 225
Validate Base v9 adoption: PASS / run 200
```

Validator·tests는 변경하지 않았다. 이 review 문서 commit으로 HEAD가 이동하므로 최종 exact HEAD에서 동일 workflow 3개를 다시 확인해야 한다.

## 6. 적대적 검토 finding

| ID | 공격 | 판정 | 조치·잔여 검증 |
|---|---|---|---|
| `PRE-01` | 왕실 인가가 플레이어 주체성을 약화 | `RESOLVED` | 활성 작전 자율권과 사후 책임을 함께 정의 |
| `PRE-02` | 자율권이 무제한 국가 권력이 됨 | `RESOLVED` | 구역·기간·배속 전력 제한, 통치·사법·무제한 징발 금지 |
| `PRE-03` | Hero+가 일반 병사·기본 Profile을 무가치하게 함 | `TEST_REQUIRED` | 고유 역할·출전 상한·기본 Profile 완주; same-seed 검증 필요 |
| `PRE-04` | 주점이 가챠로 변질 | `RESOLVED` | 결정론적 공개 노드, 유료 재굴림·중복 합성 금지 |
| `PRE-05` | 병영이 무한 능력치 트리 | `RESOLVED` | 유한 sidegrade, 전 구간 전투 배율 금지 |
| `PRE-06` | 연구가 숨은 odds·생산량 버프 | `RESOLVED` | 확률 조작·전 구간 생산 배율·자동 플레이 금지 |
| `PRE-07` | 노드와 Retry 공유 지갑이 비축·후회·파밍 유발 | `TEST_REQUIRED` | balance/total 분리, 비용 공개, 100K trajectory·사람 검증 |
| `PRE-08` | 보조 시설이 MapRun보다 중요한 메뉴 게임이 됨 | `RESOLVED` | 런 진입 1순위·Profile 2순위·시설 3순위 |
| `PRE-09` | 10건 규칙이 불완전 PR을 강제 병합 | `RESOLVED` | cadence는 preflight trigger; blocker가 있으면 병합 금지 |
| `PRE-10` | history PR의 누락 파일을 current로 가리킴 | `RESOLVED` | current local authority 존재 검사와 Screen Board 복구 |
| `PRE-11` | exact value 후보가 승인 제품값으로 승격 | `RESOLVED` | 비용·노드·영웅 수·등급·능력·출전 상한 pending 유지 |
| `PRE-12` | 승인 문서를 구현 완료로 오인 | `RESOLVED` | Legacy 제품·latest not implemented 경계 반복 표기 |
| `PRE-13` | main 병합 뒤 PR head 상태가 Sheet에 남음 | `MERGE_STEP_REQUIRED` | merge commit 확인 뒤 `SYNCED_TO_MAIN / MERGE_VERIFIED`로 교체 |
| `PRE-14` | 세계·Meta 범위가 너무 넓어 한 PR이 됨 | `ACCEPTED_RISK` | 문서-only recovery bundle이며 squash merge; 이후 새 branch로 분리 |

## 7. P0/P1 판정

```text
OPEN_P0: 0
OPEN_P1_MERGE_BLOCKER: 0
TEST_REQUIRED_NON_BLOCKING: Hero power delta, shared wallet economy, usability, save fault injection
USER_DECISION_REQUIRED_NON_BLOCKING: exact values, hero content, royal details, Veil-species purpose
```

미구현·미검증 항목은 제품 구현 승인에 대한 blocker지만, 현재 문서 정본 병합에는 blocker가 아니다. 완료로 허위 표기하지 않는 것이 조건이다.

## 8. 병합 승인 조건

이 review commit 이후 다음을 모두 새로 통과하면 PR #119 squash 병합 가능:

1. final exact HEAD 확인.
2. Sheet의 exact HEAD 갱신과 bounded read-back.
3. required CI 3개 모두 Green.
4. compare 결과 product path 0.
5. mergeable true, behind 0.
6. comments/reviews/unresolved threads 0.
7. PR body를 최신 Decision·Sheet 범위·finding·exact HEAD로 갱신.
8. Draft를 Ready로 전환.
9. verified exact HEAD를 expected head로 squash merge.
10. merged main SHA·파일·Sheet를 재검증.

## 9. 결론

```text
PREMERGE_CONTENT_REVIEW: PASS
CURRENT_BLOCKERS: 0
FINAL_HEAD_REVALIDATION: REQUIRED
MERGE_METHOD: SQUASH_RECOMMENDED
PRODUCT_CODE: UNCHANGED
```
