# OMENWARD Base v9.4.4 맞춤형 운영 어댑터 설계

```yaml
decision_id: OMW-OPS-20260901-BASE-V944-TAILORED-OPERATING-ADAPTER-01
status: USER_DIRECTED_UPDATE__IMPLEMENTATION_IN_PROGRESS
scope: PROJECT_OPERATING_SYSTEM / ROUTING / DOCUMENTATION / VALIDATION
product_code_authority: NONE
user_request: Base를 상세하게 fresh-read한 뒤, 프로젝트에 맞춘 작업순서·구조·계약으로 갱신
base_remote_observed: 19355b7ef065a21d0f2b685c7d9be64a4a3970f8
base_released_line_to_adopt: v9.4.4
base_unreleased_reference_line: v9.5 focused maintenance candidate
base_current_validator_role: GIT_CANONICAL_EVIDENCE_VALIDATOR_ONLY
adapter_schema_target: PROJECT_BASE_ADAPTER_V2
```

## 1. 현재 상태와 문제

OMENWARD의 실제 제품 정본은 이미 단일 행군 전선, `내정 / 룰렛 / 전선` 탭, repository-only human canon, close battle + march minimap으로 전환되었다. 반면 운영 계층에는 다음과 같은 과거 표현이 남아 있다.

- `skills/PROJECT_BASE_ADAPTER.json`은 Base v9.4.3을 고정하고 Google Sheet를 `CURRENT` human workspace로 표현한다.
- `AGENTS.md`와 `docs/BASE_SHARED_SKILL_INTEGRATION.md`는 현행 단일 전선과 repository-only 정책보다 오래된 3전선·Sheet 표현을 일부 유지한다.
- 생성 route view와 이전 호환 view는 adapter의 이전 hash와 Base release identity를 유지한다.

이 상태는 현재 제품 코드의 동작을 바꾸지 않지만, 새 작업자가 다른 authority와 오래된 운영 경로를 함께 읽을 위험을 만든다.

## 2. 조사·비교와 채택 결정

| 대안 | 판단 | 이유 |
| --- | --- | --- |
| Base `main` v9.5 후보를 즉시 통째로 채택 | REJECT | `main`의 v9.5는 released compatibility line이 아니다. project pin·검증기·human workflow 증거를 건너뛰면 채택 상태를 과장한다. |
| 기존 v9.4.3을 유지하고 문구만 보정 | REJECT | released v9.4.4의 `REUSE_FIRST_PREFLIGHT_REQUIRED`와 `REUSE_LEARNING_HANDOFF_REQUIRED`를 놓쳐 새 시스템·시각·workflow 작업의 소비처/재사용 근거가 약해진다. |
| **v9.4.4만 정확히 pin하고 OMENWARD adapter로 변형** | **ADOPT** | Base의 released reuse-first gate를 사용하면서, OMENWARD의 단일 전선·repository-only·승인 자산·Godot 검증 경계를 그대로 보존한다. Windows evidence 검증은 policy를 채택하지 않는 current validator reference로 보완한다. |

채택하는 Base release identity는 다음과 같다.

```yaml
version: 9.4.4
release_commit: 210ec78292fa12ed7563ba743b322dd36103ae4a
release_evidence_commit: bb61e68dc3028421b60c11b87ba2abd297ee6f78
finalization_commit: 5adc196c0185951f50e49ab5e51586eff8d60886
registry_sha256: 08f882d0c77339e8f7ff187c35b79501e0a2958ab1ff1c7aaa1c0ef8dbee45d6
```

`19355b7`은 최신 Base remote의 **validator program reference**다. Git canonical bytes로 generated artifact를 확인해 Windows EOL false mismatch를 막지만, OMENWARD가 v9.5 candidate policy를 채택했다는 의미가 아니다. release lock, registry, shared Skill contract는 여전히 exact v9.4.4 source에서 읽는다.

## 3. 맞춤형 권한 구조

```text
사용자 최신 지시
→ OMENWARD AGENTS + current decision/context + 명시 승인 범위
→ 실제 code / data / scene / asset / test / runtime evidence
→ OMENWARD가 pin한 Base v9.4.4 adapter
→ latest Base remote의 released/candidate drift 정보
→ 과거 chat / PDF / Notion / Google Sheet / legacy plan
```

세부 owner는 중복하지 않는다.

| 책임 | 단일 owner | 역할 |
| --- | --- | --- |
| 매 작업 시작 라우팅·보호 경계 | `AGENTS.md` | 얇은 entry router; 제품 세부 값을 복제하지 않는다. |
| Base 차용 범위·pin·route | `skills/PROJECT_BASE_ADAPTER.json` | 기계 판독 정본. |
| 효과 route | `skills/PROJECT_SKILL_SNAPSHOT.json` | adapter에서 생성되는 파생 view. |
| 사람이 읽는 Base 변형 설명 | `docs/BASE_SHARED_SKILL_INTEGRATION.md` | adoption 이유와 current/candidate 분리. |
| 현행 제품 의미·승인 | `docs/CURRENT_CONFIRMED_DECISIONS.md`, `docs/ACTIVE_CONTEXT.md`, GDD/Project Core | single-front product truth와 evidence ceiling. |
| historical Sheet / Notion | dated evidence·migration records | compatibility/reference only; 현재 정본·일상 read/write 경로가 아니다. |

## 4. 새 작업 순서

1. **Fresh state** — Base remote와 project `main`, active worktree, same-goal PR/Issue를 fresh query한다. Base `main`의 관찰값과 project pin을 혼동하지 않는다.
2. **Contract preflight** — dependency-ready interpreter로 project operating contract를 검사하고, project router가 읽는 canonical adapter/snapshot으로 필요한 route만 고른다.
3. **Current authority** — `CURRENT_CONFIRMED_DECISIONS`, `ACTIVE_CONTEXT`, handoff, relevant product owner와 실제 consumer/evidence를 읽는다.
4. **Reuse-first intake** — 신규 또는 의미 있게 개정하는 system/data/UI/visual/tool/workflow/test에는 current project implementation·approved reference→Base reuse handoff/profile→targeted evidence→necessary external benchmark 순서를 사용한다. 순수 기계 정리만 reasoned `NOT_APPLICABLE`로 기록한다.
5. **Decision and build gate** — product meaning, public contract, new dependency, irreversible deletion, cost/security/release scope는 before/after/risk/rollback을 제시한 승인 뒤에만 바꾼다. 이미 승인된 동일 범위의 implementation continuation은 approval reference를 재사용한다.
6. **Implementation** — project-local skill은 Omenward 고유 전투/룰렛/asset consumer에만 사용한다. Base skill body, candidate module, external asset은 필요한 consumer와 project adapter 없이 복사·설치하지 않는다.
7. **Verification and freshness** — affected contract test를 먼저 RED→GREEN으로 만들고, static validation, required runtime when code changes, canonical freshness, exact-head CI를 수행한다. `NOT_RUN` human/device/release evidence는 승격하지 않는다.
8. **Sync and closeout** — fetch/reconcile/push PR, exact-head checks, five adversarial review passes, relevant owner/readback, reuse-learning handoff를 실행한다. human review가 필요한 것은 next gate로 남긴다.

## 5. OMENWARD 변형과 보호 경계

- `REPOSITORY_PRIMARY_CANON`을 유지한다. Notion은 2026-08-28 user-approved migration 후 `RETIRED`; Google Sheet는 historical compatibility input이다.
- Base의 generic example directory layout을 강제하지 않는다. 기존 Godot `assets/`, `scenes/`, `scripts/`, `data/`, `tests/`, `docs/`를 유지한다.
- Product identity는 current decision owner가 소유한다. 운영 adapter는 single march front, 5-sector minimap, 3×3 roulette, `PREPARE → COMMIT → BATTLE → REVIEW`를 다시 정의하지 않고 해당 owner로 연결한다.
- 이미지·자산은 actual consumer, repository path, SHA-256, provenance, approval and implementation state가 함께 있을 때만 runtime candidate가 된다.
- Base reusable module은 existing project consumer가 명확할 때만 `REUSE / ADAPT / EXTRACT_PROJECT_ONLY_MODULE / NO_REUSE`로 선택한다. 이 변경은 새 runtime module을 설치하지 않는다.

## 6. 변경 범위와 검증

### 변경 대상

- `AGENTS.md`
- `skills/PROJECT_BASE_ADAPTER.json` 및 생성 adapter/snapshot views
- `docs/BASE_SHARED_SKILL_INTEGRATION.md`, `skills/README.md`
- current documentation map/lifecycle and active context pointers
- Base v9.4.x adapter regression tests and targeted workflows
- this design, implementation plan, and adversarial review receipt

### 보호 대상

- Godot code, scenes, resources, game data, save keys, approved runtime assets
- current product decisions and their owner documents
- legacy Notion/Sheet source evidence and compatibility views
- unrelated files and other open PRs

### Required evidence

```text
RED targeted adapter contract test
→ generated-artifact check using current validator program + Base v9.4.4 exact source
→ project adapter and core-doc validators
→ Python regression suite
→ canonical freshness audit
→ exact PR-head GitHub checks
→ five-pass adversarial review
```

Runtime/UX/player/release evidence is `NOT_APPLICABLE` for the contract-only diff unless a validator reveals an actual runtime consumer change. Existing product human usability remains `NOT_RUN`.

## 7. Rollback

One revert of the adapter-update commit restores the v9.4.3 adapter and generated views. The v2 identity transition and validator/reference split revert together. Base release history, historical Sheet/Notion evidence, current product assets, scenes, data, and unrelated PRs are never rewritten or deleted by this work.
