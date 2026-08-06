# [현행 제안] OMENWARD 통합 작업지시문 v4.3 활성 바인딩

```yaml
decision_id: OMW-DEC-20260806-PROCESS-ACTIVATE-INTEGRATED-CONTRACT-V4-3-V1
contract_name: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION
contract_version: "4.3"
contract_status: ACTIVE_INTEGRATED_AUDIT_IMPLEMENTATION_DELIVERY_CONTRACT
binding_status: ACTIVE
counter: NON_COUNTER
activation_authority: USER_DIRECT_APPROVAL_IN_CURRENT_CONVERSATION
repository_main: 7588317f294d602cfad5f7f15bfebcf849b8a77b
base_main: 4f98f968a377f7b6a11aafa4fc94d11bddbebedc
entry_gate: BLOCK
```

## 1. 활성 계약

사용자가 제공하고 현재 대화에서 활성 계약으로 지정한 `PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.3.md`를 OMENWARD의 현재 작업 운영 계약으로 바인딩한다.

- v4.3: `ACTIVE`
- v4.2: `HISTORICAL_COMPARISON_ONLY`
- 과거 대화의 `[이미지 완료]`: v4.3의 `[이미지·오디오 완료]` 호환 표기로만 해석

계약 활성화는 작업 진입 허가와 다르다.

```text
APPLICATION_BINDING = ACTIVE
ENTRY_STATE_RECONCILIATION = BLOCKED
PRODUCT_IMPLEMENTATION = FORBIDDEN
GODOT_AUTHORING = FORBIDDEN
FORMAL_GUT_EXECUTION = FORBIDDEN
MERGE_PR155_OR_PR156 = FORBIDDEN
```

## 2. v4.3 권위와 역할

```text
GPT 기획 역할
→ GPT 검토 역할
→ 사용자 결정권
→ Codex script/data/test/CI 구현
→ HiGodot 단일 Godot 저작
→ GUT 9.7.1 테스트 실행·assert
→ CI exact-HEAD 객관 검증
```

- 검토 모델은 `GPT_ROLE_SEPARATED_PLUS_USER_DECISION_AUTHORITY`다.
- 1인 개발 환경에서 별도 외부 독립 리뷰어가 존재한다고 가장하지 않는다.
- HiGodot만 Scene·Node·Resource·Theme·Animation·signal·project settings를 저작한다.
- GUT은 production Scene·Resource·`project.godot`을 수정하지 않는다.
- 현재 Python 검증은 GUT 명세 병합 전 운영 계약을 지키기 위한 `BOOTSTRAP_CONTRACT_TEST_ONLY_NOT_FORMAL_GUT`이다.

## 3. 작업 진입 재판정

실제 readback:

```text
Decision Ledger = STALE_CANON_CONFLICT
DECISIONS_PENDING = STALE_RELATIVE_TO_PR154_4_OF_10
image READY = 0
image AWAITING = 0
image IN_REVIEW_NOT_GENERATED = 1
image REJECTED_PROJECT_MISMATCH = 6
PR154 = CONDITIONAL_FAIL / UNMERGED
```

따라서 v4.3의 `ENTRY_STATE_RECONCILIATION_BLOCKING_GATE`는 `BLOCK`이다.

## 4. PR #155·#156 전환

### PR #155

- GUT 9.7.1 채택 의도와 HiGodot/GUT 비중첩 계약은 v4.3 방향과 일치한다.
- 다만 작업 진입 Gate와 GUT 채택 명세가 한 PR에 결합돼 있어 v4.3의 설계 명세 전용 Draft PR 원칙에 대한 범위 재검토가 필요하다.
- 병합 전 `docs/testing/GUT_9_7_1_ADOPTION_SPEC.md` 수준의 필수 항목 충족 여부를 다시 검사한다.
- `DRAFT_SCOPE_ALIGNMENT_REQUIRED_UNDER_V4_3 / MERGE_BLOCKED`로 유지한다.

### PR #156

- `addons/gut/**`와 Godot 저작 파일을 변경하지 않는 provenance evidence Draft라는 점은 안전하다.
- 그러나 GUT 채택 명세가 merged main에 존재하기 전에는 정식 설치·실행·활성화·병합 순서로 승격할 수 없다.
- `DRAFT_EVIDENCE_ONLY_SEQUENCE_BLOCKED / MERGE_BLOCKED`로 유지한다.

## 5. 공유 사운드 Vault

원문 경로를 수정하지 않는다.

```text
C:/Users/user/Documents/GitHub/shered audio vault
```

현재 에이전트 환경에서는 해당 Windows 경로를 읽을 수 없다.

```text
AUDIO_VAULT_PATH_UNVERIFIED
AUDIO_RIGHTS_UNVERIFIED
AUDIO_IMPORT_NOT_AUTHORIZED
ABSOLUTE_RUNTIME_REFERENCE_FORBIDDEN
```

접근이 증명된 뒤에도 원본 Vault는 읽기 전용이며, 승인된 파일만 권리·hash·출처를 기록해 `res://` 아래로 복사하고 HiGodot으로 연결한다.

## 6. 허용되는 다음 작업

1. 이 계약 바인딩의 exact-head 검증과 Sheet 동기화.
2. Base 전체 tracked-file·Skill·Workflow 지도 복원.
3. PR #155의 v4.3 설계 명세 전용 범위 재검토와 필요 시 분리.
4. PR #156의 Draft provenance 증거 검토. `addons/gut` 또는 Godot 파일 mutation은 금지.
5. 별도 Decision·정확한 경로 목록을 사용한 중앙 정본의 비파괴 정합성 교정.

## 7. 완료 오해 방지

이 Decision은 다음을 증명하지 않는다.

```text
BASE_WHOLE_REPOSITORY_AND_SKILL_RECOVERY_COMPLETE
ENTRY_GATE_PASS
GUT_ADOPTION_SPEC_MERGED_MAIN_VERIFIED
HIGODOT_SOURCE_OR_VERSION_VERIFIED
EXACT_GODOT_4_7_X_VERIFIED
GUT_TEST_DISCOVERY_OR_JUNIT_VERIFIED
AUDIO_VAULT_INVENTORIED
WINDOWS_OR_ANDROID_VALIDATED
LOCAL_MAIN_SYNCED
GODOT_RUN_VALIDATED
```
