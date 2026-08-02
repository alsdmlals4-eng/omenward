# OMENWARD PR #121 승인 10건 적대적 병합 사전 검토

```yaml
review_id: OMW-OPS-20260802-PR121-TEN-DECISION-PREFLIGHT-V1
reviewed_at: 2026-08-02 19:26 KST
repository: alsdmlals4-eng/omenward
pull_request: 121
base_branch: main
base_head: 7c8be1ba47d4159ca3cead6343c20ef068907bcd
active_base: 9.4.2
candidate_evidence_head: be552b54b96a029dfa042675ae002ad21b96af65
feature_branch: gpt/omenward-gameplay-planning-20260802
approval_count: 10
review_status: CONTENT_PASS / FINAL_EXACT_HEAD_REVALIDATION_REQUIRED_BEFORE_MERGE
merge_eligibility: DOCS_ONLY_ELIGIBLE_AFTER_FINAL_REVALIDATION
merge_authorization: NOT_GRANTED
pr_state_required: DRAFT
product_code_authority: NONE
```

## 1. 결론

PR #121의 승인 10건은 GitHub 책임 원본과 연결 Google Sheet에 같은 Decision ID로 정리되어 있다. 권위 파일, Sheet bounded read-back, 최신 main ancestry, CI, 변경 경로, 댓글·리뷰·스레드를 적대적으로 검증했다.

```text
CONTENT_PREFLIGHT = PASS
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
PRODUCT_PATH_CHANGES = 0
MERGE_AUTHORIZATION = NOT_GRANTED
```

문서 묶음은 최종 exact HEAD 재검증이 통과하면 문서-only 병합 가능한 상태다. 그러나 사용자의 명시적 병합 승인은 없으므로 Draft를 유지하며 Ready 전환·병합·auto-merge를 수행하지 않는다.

## 2. 검토 대상 10건

1. `OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1`
2. `OMW-DEC-20260802-GAMEPLAY-HERO-UNLOCK-REGISTRATION-V1`
3. `OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1`
4. `OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1`
5. `OMW-DEC-20260802-GAMEPLAY-HERO-EXIT-AND-REPLACEMENT-V1`
6. `OMW-DEC-20260802-GAMEPLAY-MAPRUN-STAGE-WAVE-MAINTENANCE-V1`
7. `OMW-DEC-20260802-GAMEPLAY-HERO-STAGE-STATE-PERSISTENCE-V1`
8. `OMW-DEC-20260802-GAMEPLAY-HERO-REDEPLOYMENT-INITIAL-STATE-V1`
9. `OMW-DEC-20260802-GAMEPLAY-HERO-POWER-BUDGET-AND-SIDEGRADE-V1`
10. `OMW-DEC-20260802-GAMEPLAY-HERO-ABILITY-ACTIVATION-MODE-V1`

각 책임 원본을 직접 읽어 파일 존재, Decision ID, 사용자 승인 상태, `NOT_IMPLEMENTED`, `product_code_authority: NONE` 경계를 확인했다.

## 3. 최신 main·Base 동기화

preflight 동안 main이 두 번 이동했다.

### Base v9.4.1

```text
main = a521cf744533139063a72ab358b4381d2aae6f0b
initial feature state = behind 1
resolution = main→feature PR #124
```

- Base v9.4.1 adapter·workflow·test ancestry를 feature에 포함했다.
- PR #121을 main에 병합하지 않았다.

### Base v9.4.2 planning-first

```text
main = 7c8be1ba47d4159ca3cead6343c20ef068907bcd
feature state during finalization = behind 1
resolution = main→feature PR #125
sync merge commit = f9334f32bd5ac5142860c991a809b6bc911963c4
```

- Base v9.4.2 planning-first adapter·workflow·test ancestry를 feature에 포함했다.
- 별도 기록: `docs/operations/PR121_MAIN_SYNC_V942_NOTE_2026-08-02.md`.
- PR #125는 main을 feature로 동기화했을 뿐 PR #121의 main 병합 승인이 아니다.

판정: `RESOLVED / FINAL_COMPARE_REQUIRED`.

## 4. GitHub 권위·계보 검토

### PASS

- Decision Ledger가 10개 승인 Decision과 `10/10`을 소유한다.
- Documentation Map이 각 질문의 주 책임 원본을 라우팅한다.
- 영웅 능력 자동 발동 책임 원본이 정확한 Decision ID를 소유한다.
- 기존 전체 시스템 Vertical Slice 권위가 보존됐다.
- `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` 라우팅을 유지한다.
- `ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md` 라우팅을 유지한다.
- `OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md`는 `PILOT_RECOMMENDATION / NOT_CANON`이다.
- Legacy 제품과 최신 승인 기획의 미구현 경계가 분리돼 있다.
- 정확 능력·수치·simulation·runtime·human QA를 완료로 승격하지 않았다.

### CI 실패 발견·해결

Documentation Map 정리 과정에서 validator가 요구하는 Vertical Slice·적대적 검토·Evidence Pilot 계보가 누락되어 Project Core run 614가 실패했다. 네 경계를 복원한 뒤 run 615가 통과했다.

판정: `RESOLVED`.

## 5. Google Sheet 검토

Workbook:

- ID: `1VLwRtXGDtyj0JFt98wdIOtG6Zqc3wtdfCzSF9Fo6lpw`
- 제목: `오멘워드(OMENWARD)`
- 필수 탭: 25개
- locale: `ko_KR`
- timezone: `Asia/Seoul`

10번째 Decision 동기화 범위:

- `00_프로젝트_허브!E2:L2`
- `01_작업순서!A25:N26`
- `02_현재_확정결정!A34:M34`
- `04_누락_충돌_감사!A103:H111`
- `05_GDD_요약!D8:J8`
- `05_GDD_요약!B9:J9`
- `12_핵심루프!A11:J11`
- `15_조작_게임규칙!A14:J14`
- `40_핵심시스템_메인콘텐츠!A14:J14`
- `41_성장_경제!A24:I24`
- `50_메인콘텐츠!A21:J21`
- `60_UX_UI_접근성!A22:J22`
- `99_변경이력!A35:H36`

bounded read-back:

```text
SAME_DECISION_ID = PASS
APPROVAL_COUNT = 10_OF_10
MERGE_AUTHORIZATION = NOT_GRANTED
PRODUCT_STATUS = NOT_IMPLEMENTED
```

과거 PR #116 CI `OPEN_P1` 두 건은 현재 Green CI 증거로 역사적 해결 상태로 전환했다. 경제 parser·100K simulation·Save fault injection은 제품 구현 전 `TEST_REQUIRED`로 유지하되 제품 코드가 없는 문서-only PR의 병합 blocker와 분리했다.

최종 검색:

```text
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
```

## 6. CI 검토

후보 증거 HEAD `be552b54b96a029dfa042675ae002ad21b96af65`:

```text
Validate Project Core Documentation: PASS / run 615
Validate Omenward GDD Sheet Adoption: PASS / run 332
Validate Base v9 adoption: PASS / run 308
```

Base v9.4.1 main 증거:

```text
Validate Base Shared External AI Adapter: PASS / run 16
Validate Omenward Skill System: PASS / run 153
Validate Base v9 adoption: PASS / run 304
```

Base v9.4.2 current main `7c8be1ba47d4159ca3cead6343c20ef068907bcd`:

```text
Validate Base v9.4.2 Planning First Adoption: PASS / run 4
Validate Base Shared External AI Adapter: PASS / run 19
Validate Base v9 adoption: PASS / run 316
Validate Omenward Skill System: PASS / run 157
```

마감 문서와 latest-main sync로 HEAD가 이동했으므로 최종 exact HEAD에서 PR 필수 CI를 다시 확인한다.

## 7. PR 메타데이터·범위 검토

후보 증거 단계:

```text
STATE = OPEN
DRAFT = TRUE
MERGEABLE = TRUE
MERGED = FALSE
PRODUCT_PATHS = 0
COMMENTS = 0
REVIEWS = 0
UNRESOLVED_THREADS = 0
```

Base adapter·workflow·test 파일은 current main ancestry로 포함되며 PR #121의 최종 feature diff에서 제외돼야 한다. 최종 compare에서 `behind 0`, 문서-only changed paths, 제품 경로 0을 다시 확인한다.

PR 설명은 최종 exact HEAD·CI·Sheet·preflight·병합 미승인 상태로 갱신한다.

## 8. 적대적 finding

| ID | 공격 | 판정 | 처리 |
|---|---|---|---|
| PF-01 | 영웅 자동 발동 규칙이 숨겨진다 | `RESOLVED` | trigger·ability/target priority·tie-break 공개 |
| PF-02 | 동률 선택이 비결정적이다 | `TEST_REQUIRED` | 고정 tie-break·save/reload runtime test |
| PF-03 | 수동 궁극기 예외로 APM 게임이 된다 | `RESOLVED` | 모든 영웅 능력 자동·수동 버튼 금지 |
| PF-04 | 저장·Retry로 타깃을 재굴림한다 | `TEST_REQUIRED` | 동일 상태·입력 순서 결정론·fault test |
| PF-05 | 자동 조건이 상시 충족되어 상위호환이 된다 | `SIMULATION_REQUIRED` | condition on/off encounter·선택률 검증 |
| PF-06 | 사망 전 토큰으로 즉시 영웅을 교대한다 | `RESOLVED` | post-death token provenance gate |
| PF-07 | 영웅 사망 보상 파밍이 생긴다 | `RESOLVED` | token·재화·회수권·pity 없음 |
| PF-08 | Base v9.4.1 latest main을 누락한다 | `RESOLVED` | PR #124 main→feature sync |
| PF-09 | Base v9.4.2 latest main을 누락한다 | `RESOLVED` | PR #125 main→feature sync |
| PF-10 | 10건을 자동 병합 승인으로 해석한다 | `RESOLVED` | preflight와 merge authorization 분리 |
| PF-11 | 승인 문서를 구현 완료로 오인한다 | `RESOLVED` | Legacy·NOT_IMPLEMENTED·NOT_RUN 경계 |
| PF-12 | 과거 OPEN_P1이 현행 blocker처럼 남는다 | `RESOLVED` | 역사 CI·제품 구현 테스트로 재분류 |
| PF-13 | 마감 커밋이 검증된 HEAD를 움직인다 | `FINAL_REVALIDATION_REQUIRED` | exact HEAD CI·compare·PR·Sheet 재검증 |

## 9. 남은 비병합 차단 검증

다음은 제품 구현·수치 승인·Release를 막지만 문서-only 기획 병합 자체를 막지는 않는다.

- HeroAbilitySpec의 정확 능력·trigger·priority·invalid-target 정책.
- 영웅 power-budget 가중치·허용 편차·encounter simulation.
- 영웅 token provenance·save/retry fault injection.
- 일반 MaintenancePhase 경제·건설·수리 clock matrix.
- runtime 결정론·UI usability·접근성·human QA.
- 제품 구현 전체.

## 10. 병합 판정

```text
CONTENT_PREFLIGHT = PASS
CURRENT_BLOCKERS = 0
FINAL_HEAD_REVALIDATION = REQUIRED
MERGE_ELIGIBILITY_AFTER_REVALIDATION = DOCS_ONLY_ELIGIBLE
MERGE_AUTHORIZATION = NOT_GRANTED
DRAFT_MUST_REMAIN = TRUE
AUTO_MERGE = FORBIDDEN
```

최종 exact HEAD 재검증이 통과해도 이 문서는 병합 명령이 아니다. 사용자의 별도 명시적 승인 전에는 PR #121을 Ready로 전환하거나 병합하지 않는다.
