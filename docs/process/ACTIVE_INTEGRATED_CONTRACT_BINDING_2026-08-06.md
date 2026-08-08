# [현행] OMENWARD 통합 작업지시문 v4.4 활성 바인딩

```yaml
decision_id: OMW-DEC-20260808-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-4-AND-RECONCILE-ENTRY-STATE-V1
last_gate_update_decision: OMW-DEC-20260808-PLANNING-BARRACKS-CAPABILITY-PROXY-AND-MULTI-SPECIAL-TOKEN-BURST-REMEDIATION-V1
contract_name: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION
contract_version: "4.4"
contract_status: ACTIVE_INTEGRATED_AUDIT_IMPLEMENTATION_DELIVERY_CONTRACT
binding_status: ACTIVE
counter: NON_COUNTER
activation_authority: USER_DIRECT_APPROVAL_IN_CURRENT_CONVERSATION
source_repository_main: b28533cba722e293fdbfc1d1b43478dd8ded380d
base_main: fa69a77a14f923a756064f6ae151d34cadb374f7
reconciliation_branch: planning/pr154-conditional-fail-remediation-20260808
entry_gate: BLOCK
```

## 1. 활성 계약

사용자가 제공한 `PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.4.md`를 현재 OMENWARD 운영 계약으로 바인딩한다. 프로젝트 입력은 현재 대화에서 사용자가 지정한 OMENWARD 저장소와 `C:/Users/user/Documents/GitHub/Ninza/omenward` 경로로 해석한다.

- v4.4: `ACTIVE`
- v4.3 / v4.2: `HISTORICAL_COMPARISON_ONLY`
- 계약 활성화는 제품 구현 진입 허가와 다르다.

## 2. 현재 재조정 사실

- Base `main`: `fa69a77a14f923a756064f6ae151d34cadb374f7`
- OMENWARD gate baseline main: `b28533cba722e293fdbfc1d1b43478dd8ded380d`
- 온보딩 기획: `APPROVED_10_OF_10_WITH_TOKEN_SOURCE_AMENDMENT`
- 병영 수치·시뮬레이션 배치: `APPROVED_5_OF_10_REMEDIATION_SMOKE_PASS / 10000_REVIEW_REQUIRED`
- PR #155: Draft / GUT 9.7.1 adoption spec not merged
- PR #159: `MERGED` / Base recovery `COMPLETE`
- PR #163: `MERGED` / Project Base Adapter freshness `RECONCILED`
- local Windows checkout / local Godot / shared audio vault: 현재 agent 환경에서 접근 불가

### Project Base Adapter freshness

```text
Base release pin = 9.4.3 / PRESERVED
Base main automatic migration = FORBIDDEN
GDD Sheet = CURRENT / SHEET_GITHUB_SYNCED
protected baseline = 1f23981fdfc3e965ff46c8866e978c4701eb3d4e
protected policy source = CANONICAL_ADAPTER_SOURCE
protected policy hash = 1c36c4180b85d6bd97f4e7cdba908cc73298f529d368aa07e0dffde6e1e8ec52
generated views = BASE_GENERATOR_VALIDATED
PROJECT_BASE_ADAPTER_FRESHNESS_FIX_REQUIRED = CLEARED
```

### Barracks 5/10 remediation

`OMW-DEC-20260808-PLANNING-BARRACKS-CAPABILITY-PROXY-AND-MULTI-SPECIAL-TOKEN-BURST-REMEDIATION-V1`로 4/10의 두 핵심 차단을 다음과 같이 처리한다.

```text
MODEL_IDENTIFIABILITY_FAIL
-> unsupported combat-support scalar 제거
-> STRUCTURAL_CHANNEL_VECTOR 사용
-> combat validity / role-blind regret = DIAGNOSTIC_NON_IDENTIFIABLE

SPECIAL_TOKEN_SHARE_BURST_MAX = 0.50 > 0.45
-> second special TokenSource deferred until 3 non-special active sources
-> auto-production remains allowed
-> physical TokenInstance grammar preserved
-> exact 2,000-seed observed burst = 0.333333 <= 0.45
```

Exact smoke evidence:

```text
run = 31254624591
job = 93096088531
SMOKE_RERUN = PASS
failed_decision_gates = []
JSON_SHA256 = a02c4e0bad6a7113937fbd23f4521c364d109944c7f05c94eb5839b9119d00e2
CSV_SHA256 = 3b6a164a4ca847d29b82d73b3841100f246cdc36b9b86f30198bfcfe586f6560
```

이 PASS는 10,000-seed 실행이나 제품 수치 확정을 자동 승인하지 않는다.

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

Base recovery, adapter freshness, 2,000-seed remediation smoke를 닫아도 다음 독립 차단 조건 때문에 Entry Gate는 `BLOCK`을 유지한다.

- `BARRACKS_10000_SEED_DECISION_SWEEP_REVIEW_REQUIRED`
- GUT adoption spec PR #155 not merged
- HiGodot exact source/version unverified
- Hera direct-main import disposition not closed
- local Godot / shared audio vault unavailable
- historical secret scan unproven accepted risk

따라서 제품 구현, Godot 저작 mutation, formal GUT, Hera live-QA 완료 주장, 이미지 생성, audio import, local-main/Godot runtime 완료 주장은 금지한다.

## 6. 다음 허용 작업

1. `BARRACKS_10000_SEED_DECISION_SWEEP_REVIEW`
2. PR #155 GUT adoption-spec review
3. Hera Existing Solution First disposition

10,000-seed decision sweep는 사용자 리뷰·별도 승인 전 실행하지 않는다. 50,000 confirmation sweep, 최종 파라미터 선택, 제품 구현도 계속 차단한다.

## 7. Sheet 동기화

v4.4 활성 계약 Decision은 다음 ID를 유지한다.

```text
OMW-DEC-20260808-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-4-AND-RECONCILE-ENTRY-STATE-V1
```

현재 Gate 변경은 다음 Decision ID로 GitHub와 Sheet에 함께 기록한다.

```text
OMW-DEC-20260808-PLANNING-BARRACKS-CAPABILITY-PROXY-AND-MULTI-SPECIAL-TOKEN-BURST-REMEDIATION-V1
```

PR exact-head와 병합 결과는 Sheet의 PR/변경이력 surface에서 추적하며, 이 활성 바인딩 정본에는 병합 직후 stale해지는 임시 HEAD 상태를 현재값처럼 고정하지 않는다.

## 8. v4.3 역사

`OMW-DEC-20260806-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-3-V1`은 당시 계약 활성화와 fail-closed Gate를 증명하는 역사 자료로 보존한다. v4.4가 그 이후의 현재 운영 바인딩을 승계한다.
