# [적대적 검토] OMENWARD 통합 계약 v4.3 활성화

```yaml
decision_id: OMW-DEC-20260806-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-3-V1
review_model: GPT_ROLE_SEPARATED_PLUS_USER_DECISION_AUTHORITY
status: REVIEWED_WITH_BLOCKERS
```

## 공격 관점

계약 버전 문자열만 바꾸고 기존 진행 상태를 그대로 신뢰하면, v4.3의 작업 진입 Gate와 GUT 선행 명세 순서가 무효화될 수 있다. 따라서 다음을 분리해 판정한다.

```text
CONTRACT_ACTIVE != ENTRY_READY
DRAFT_EVIDENCE != MERGE_READY
BOOTSTRAP_PYTHON_TEST != FORMAL_GUT_TEST
PUBLIC_COMPATIBILITY_CLAIM != PROJECT_RUNTIME_COMPATIBILITY
```

## Finding

### P1 — 중앙 진입 정본 불일치

`PROJECT_CANON_DECISION_LEDGER.md`는 PR #142/7-of-10 계열 상태를 유지하고, `DECISIONS_PENDING.md`는 10-of-10 이후 상태를 기록하며, Sheet의 최신 counted planning Decision은 PR #154 4-of-10 conditional fail이다. 이 상태에서 제품 작업을 READY로 열면 v4.3 위반이다.

판정: `BLOCKED_BY_CANON_DIVERGENCE`.

### P1 — PR #155 범위 정렬 필요

PR #155는 GUT 채택 의도와 HiGodot/GUT 비중첩을 다루지만, 작업 진입 Gate·AGENTS·검증 workflow를 함께 포함한다. v4.3의 “설계 명세 전용 Draft PR” 원칙에 맞는지 필수 항목별 검토와 필요 시 분리가 선행돼야 한다.

판정: `DRAFT_SCOPE_ALIGNMENT_REQUIRED_UNDER_V4_3`.

### P1 — PR #156 순서 차단

PR #156은 vendor 파일을 수정하지 않는 provenance evidence이므로 Draft 조사로는 유지 가능하다. 그러나 adoption spec merged-main readback 전에는 formal install·GUT execution·Ready·merge 근거로 사용할 수 없다.

판정: `DRAFT_EVIDENCE_ONLY_SEQUENCE_BLOCKED`.

### P1 — exact Godot·HiGodot 미검증

Godot exact 4.7.x executable과 HiGodot pinned commit/version이 검증되지 않았다. Scene·Resource·project settings 작업 진입은 금지한다.

판정: `BLOCKED_BY_HIGODOT_AUTHORITY`.

### P1 — 이미지·오디오 선행 상태 미폐쇄

이미지 검수 Sheet는 READY 0, AWAITING 0, 미생성 IN_REVIEW 1, 프로젝트 불일치 반려 6이다. 공유 사운드 Vault는 현재 환경에서 접근할 수 없고 권리·hash도 확인되지 않았다.

판정: `BLOCKED_BY_VISUAL_AUDIO_REVIEW`.

### P2 — Base 전체 복원 미완료

Base main과 recursive tree는 조회했지만 모든 tracked file의 역할 분류, Skill 호출 그래프, dead route·중복·누락 테스트 지도는 아직 완료되지 않았다. 전체 복원을 완료했다고 주장할 수 없다.

판정: `BASE_WHOLE_REPOSITORY_AND_SKILL_RECOVERY_NOT_COMPLETED`.

### P2 — CI 사전 시작 차단

최근 workflow는 runner step 0에서 billing/spending limit로 시작되지 않았다. 코드 실패로 오인해서는 안 되지만 Green으로도 간주할 수 없다.

판정: `GITHUB_ACTIONS_BILLING_PRE_START / NOT_GREEN`.

## 오탐 검증

- v4.3 활성화가 기존 모든 Decision을 폐기한다: 거짓. 최신 사용자 승인과 프로젝트 정본의 내용은 유지하며 운영 계약만 v4.3으로 전환한다.
- PR #156을 즉시 닫아야 한다: 근거 부족. mutation 없는 Draft provenance evidence로는 유지 가능하나 merge·formal execution은 차단한다.
- Python contract test를 사용하면 v4.3 GUT 권위를 위반한다: 거짓. GUT 명세 병합 전 운영 바인딩 검증이며 `BOOTSTRAP_CONTRACT_TEST_ONLY_NOT_FORMAL_GUT`로 명시한다.
- 계약 활성화만으로 자동 병합 권한이 발생한다: 거짓. exact-head, checks, blockers, review thread, scope 조건이 모두 닫혀야 한다.

## 최종 판정

```text
APPLICATION_BINDING = PASS
ACTIVE_CONTRACT = V4_3
ENTRY_STATE_RECONCILIATION = BLOCK
PRODUCT_IMPLEMENTATION = BLOCKED
HIGODOT_AUTHORING = BLOCKED
FORMAL_GUT_EXECUTION = BLOCKED
PR155_MERGE = BLOCKED
PR156_MERGE = BLOCKED
LOCAL_SYNC = BLOCKED_NO_LOCAL_ACCESS
GODOT_RUN = BLOCKED_NO_LOCAL_ACCESS
MERGE_READY = FALSE
```
