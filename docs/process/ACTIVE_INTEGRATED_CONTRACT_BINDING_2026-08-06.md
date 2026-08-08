# [현행] OMENWARD 통합 작업지시문 v4.4 활성 바인딩

```yaml
decision_id: OMW-DEC-20260808-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-4-AND-RECONCILE-ENTRY-STATE-V1
last_gate_update_decision: OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1
contract_name: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION
contract_version: "4.4"
contract_status: ACTIVE_INTEGRATED_AUDIT_IMPLEMENTATION_DELIVERY_CONTRACT
binding_status: ACTIVE
counter: NON_COUNTER
activation_authority: USER_DIRECT_APPROVAL_IN_CURRENT_CONVERSATION
source_repository_main: 7b41923628b68c7c1477b286584973d8516eab6d
base_main: fa69a77a14f923a756064f6ae151d34cadb374f7
reconciliation_branch: process/v4-4-entry-reconciliation-20260808
entry_gate: BLOCK
```

## 1. 활성 계약

사용자가 제공한 `PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.4.md`를 현재 OMENWARD 운영 계약으로 바인딩한다. 프로젝트 입력은 현재 대화에서 사용자가 지정한 OMENWARD 저장소와 `C:/Users/user/Documents/GitHub/Ninza/omenward` 경로로 해석한다.

- v4.4: `ACTIVE`
- v4.3 / v4.2: `HISTORICAL_COMPARISON_ONLY`
- 계약 활성화는 제품 구현 진입 허가와 다르다.

## 2. 현재 재조정 사실

- Base `main`: `fa69a77a14f923a756064f6ae151d34cadb374f7`
- 온보딩 기획: `APPROVED_10_OF_10_WITH_TOKEN_SOURCE_AMENDMENT`
- 이미지 Sheet: `READY=0`, `AWAITING=0`, `IN_REVIEW_NOT_GENERATED=1`, mismatch reject 6
- PR #154: Draft / 2,000-seed smoke conditional fail 계열
- PR #155: Draft / GUT 9.7.1 adoption spec not merged
- PR #159: `MERGED` / Base recovery `COMPLETE` / merge `c6f8babe1dbb31f436eac45fa2056242baa445b1`
- PR159 exact Base recovery: tracked-file `ZERO_UNCLASSIFIED`, project-relevant full-text recovery `CLOSED`
- local Windows checkout / local Godot / shared audio vault: 현재 agent 환경에서 접근 불가

PR159 완료는 Base recovery blocker만 제거한다. 복원 과정에서 확인된 `PROJECT_BASE_ADAPTER_FRESHNESS_FIX_REQUIRED`는 별도 fail-closed finding으로 유지한다.

## 3. 직접 main 변경의 provenance

과거 Sheet 기준 이후 다음 direct-main 변경이 확인됐다.

1. `37f13c2ba4b76d59a300ce08d15c2dd4ab784ce6`: Hera Agent Godot 파일 유입.
2. `7b41923628b68c7c1477b286584973d8516eab6d`: `.asset-vault/`를 `.gitignore`에 추가.

이 재조정은 두 변경을 소급 승인하지 않는다. Hera 파일은 현재 저장소에 존재하지만 `project.godot`의 editor plugin에는 활성화되어 있지 않으므로 `NOT_VERIFIED_INSTALLED_UNUSED`로 판정한다. Existing Solution First 절차로 provenance, exact version, license, 소비 경로, HiGodot/GUT과의 비중첩을 별도 검증해야 한다.

## 4. 역할 경계

```text
HiGodot = SOLE_PERSISTENT_GODOT_AUTHORING_AUTHORITY
GUT 9.7.1 = DETERMINISTIC_GDSCRIPT_TEST_AUTHORITY_WHEN_ADOPTED
Hera = LIVE_QA_AND_OBSERVABILITY_ONLY
Hera persistent source mutation = FORBIDDEN
role overlap = FORBIDDEN
```

현재 HiGodot exact source/version은 미검증이다. GUT adoption spec PR #155는 미병합이고 formal GUT 실행은 차단한다. Hera는 저장소 존재만 확인됐으며 adoption은 검증되지 않았다.

## 5. Entry Gate

PR159 Base recovery completion을 반영해도 다음 독립 차단 조건 때문에 Entry Gate는 `BLOCK`을 유지한다.

- `PROJECT_BASE_ADAPTER_FRESHNESS_FIX_REQUIRED`
- PR #154 conditional fail / unmerged
- GUT adoption spec PR #155 not merged
- HiGodot exact source/version unverified
- Hera direct-main import disposition not closed
- local Godot / shared audio vault unavailable
- historical secret scan unproven accepted risk

따라서 제품 구현, Godot 저작 mutation, formal GUT, Hera live-QA 완료 주장, 이미지 생성, audio import, local-main/Godot runtime 완료 주장은 금지한다.

## 6. 다음 허용 작업

1. `PROJECT_BASE_ADAPTER_FRESHNESS_RECONCILIATION`
2. PR #154 conditional-fail remediation
3. PR #155 GUT adoption-spec review
4. Hera Existing Solution First disposition

Base recovery 완료 자체를 다시 수행하거나 PR159을 pending으로 취급하지 않는다.

## 7. Sheet 동기화

v4.4 활성 계약 Decision은 다음 ID를 유지한다.

```text
OMW-DEC-20260808-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-4-AND-RECONCILE-ENTRY-STATE-V1
```

후속 Gate 변경은 해당 승인 Decision ID를 별도로 기록한다. PR159 Base recovery 완료 전파는 다음 ID를 사용한다.

```text
OMW-DEC-20260807-PROCESS-BASE-REPOSITORY-SKILL-MAP-AND-LOCAL-VERIFICATION-PACK-V1
```

PR exact-head와 병합 결과는 Sheet의 PR/변경이력 surface에서 추적하며, 이 활성 바인딩 정본에는 병합 직후 stale해지는 임시 HEAD 상태를 현재값처럼 고정하지 않는다.

## 8. v4.3 역사

`OMW-DEC-20260806-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-3-V1`은 당시 계약 활성화와 fail-closed Gate를 증명하는 역사 자료로 보존한다. v4.4가 그 이후의 현재 운영 바인딩을 승계한다.
