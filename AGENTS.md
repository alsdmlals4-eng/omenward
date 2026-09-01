# OMENWARD 프로젝트 AI 작업 규칙

```yaml
updated_at: 2026-09-01
project_repository: alsdmlals4-eng/omenward
project_base_adapter: skills/PROJECT_BASE_ADAPTER.json
base_released_semantic_pin: v9.4.4
base_release_finalization: 5adc196c0185951f50e49ab5e51586eff8d60886
base_current_validator_reference: 19355b7ef065a21d0f2b685c7d9be64a4a3970f8
base_current_candidate_policy_adoption: NONE
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
planning_status: RESOLVE_FROM_CURRENT_DECISION_INDEX_AND_ACTIVE_CONTEXT
implementation_authorized: RESOLVE_FROM_CURRENT_DECISION_INDEX_AND_ACTIVE_CONTEXT
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_context: docs/ACTIVE_CONTEXT.md
current_gdd: docs/OMENWARD_GDD_CURRENT_CANON.md
repository_only_policy: docs/process/APPROVED_OMENWARD_REPOSITORY_ONLY_CANON_AND_NOTION_RETIREMENT_2026-08-28.md
visual_generation: USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
```

이 파일은 **얇은 진입 router와 보호 경계**만 소유한다. 현재 전선 구성, 화면 수, 자산 상태, PR 번호, runtime 결과처럼 변하는 제품 사실은 여기로 복제하지 않고 아래의 current owner에서 읽는다.

## 1. 권한 우선순위

1. 현재 대화의 최신 사용자 지시와 명시한 승인 범위
2. 이 `AGENTS.md`, `skills/PROJECT_BASE_ADAPTER.json`, current Decision/Context와 해당 owner
3. 실제 code, data, Scene, Resource, asset, test, runtime evidence
4. OMENWARD가 pin한 Base v9.4.4 released contract
5. fresh Base remote의 release/candidate drift 정보
6. 과거 chat, PDF, Notion, Google Sheet, historical handoff

PDF 예시는 reference일 뿐 current instruction이나 canon이 아니다. 이전 채팅, closed-unmerged branch, 오래된 SHA 역시 fresh repository truth보다 낮다.

## Current product routing receipt

다음은 current owner를 찾기 위한 안정적인 식별자이며, live evidence나 세부 기획을 이 파일이 소유한다는 뜻은 아니다.

```text
CURRENT_ROUTE = RESOLVE_FROM_CURRENT_DECISION_INDEX_AND_ACTIVE_CONTEXT
IMPLEMENTATION_START = RESOLVE_FROM_CURRENT_DECISION_INDEX_AND_ACTIVE_CONTEXT
CURRENT_APPROVED_REPLAN_DECISIONS = 30
CURRENT_VISUAL_DECISION = OMW-PLAN-20260830-BATTLE-PRIMARY-MARCH-MINIMAP-01
MAP_TOPOLOGY = ONE_WARD_CITADEL -> ONE_ACTIVE_MARCH_FRONT -> ONE_VEIL_CITADEL
FRONT_STRUCTURE = ONE_WARD_CITADEL -> ONE_ACTIVE_MARCH_FRONT -> ONE_VEIL_CITADEL
ROUTE_STATE_GRAMMAR = WARD_CITADEL_HOME_BASE -> WARD_FORWARD_BASE -> CONTESTED_CLASH_ZONE -> VEIL_FORWARD_BASE -> VEIL_CITADEL_HOME_BASE
PROJECT_CORE_SCENE_VISUAL_BOARD_SCOPE = STRATEGIC_MAP_ONLY__LOWER_UI_STORYBOARD_REMOVED
MARCH_MINIMAP = READ_ONLY_FIVE_SECTOR_CONTEXT
LEGACY_RUNTIME_BACKDROP = OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1
IMPLEMENTATION_AUTHORITY = SCOPED_APPROVED
FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL
DANGER_STAGE_TYPE = REMOVED
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
BOSS_STAGES = 5 / 10 / 15 / 20
IMAGE_GENERATION = USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
```

## 2. 매 작업 시작 read order

1. fresh `Base`의 `START_HERE.md`, `AGENTS.md`, 필요한 shared Skill과 v9.4.4 release lock을 읽는다.
2. project `main`, active worktree, 같은 목적의 open/draft PR·Issue, 현재 GitHub head를 fresh query한다.
3. `skills/PROJECT_BASE_ADAPTER.json`의 adapter test/operating-contract preflight를 실행한 뒤, 생성된 `skills/PROJECT_SKILL_SNAPSHOT.json`과 project router가 가리키는 **필요한 route만** 선택한다.
4. `docs/CURRENT_CONFIRMED_DECISIONS.md`, `docs/ACTIVE_CONTEXT.md`, `docs/OMENWARD_GDD_CURRENT_CANON.md`, `docs/PROJECT_CORE.md`와 현재 scope owner를 읽는다.
5. code, data, Scene, asset, provenance, test와 runtime evidence는 해당 scope가 실제로 열렸을 때만 current evidence로 판정한다.

`PROJECT_LOCAL_THEN_BASE_SHARED`가 기본 순서다. Base Skill 본문을 프로젝트에 복사하거나, Base current candidate를 release pin처럼 취급하지 않는다.

## 3. Base release와 validator를 분리한다

```text
SEMANTIC_OPERATING_CONTRACT = Base v9.4.4 released lock
CURRENT_VALIDATOR_REFERENCE = Base 19355b7... only for Git-canonical evidence handling
UNRELEASED_v9_5_POLICY_ADOPTION = NONE
```

v9.4.4의 release/evidence/finalization identity와 registry hash는 `skills/PROJECT_BASE_ADAPTER.json`이 기계 정본으로 소유한다. 최신 validator reference는 Windows EOL을 포함한 generated artifact의 Git-byte 검증을 안정화하기 위한 실행 참조일 뿐, v9.5 candidate의 workflow·product policy를 채택한 것이 아니다.

## 4. Reuse-first intake

새로 만들거나 의미 있게 바꾸는 system, game data, UI, visual, tool, workflow, test는 구현 전 다음 순서로 조사한다.

```text
current project owner / actual consumer
→ approved project asset and reference
→ Base PROJECT_WORK_REUSE_HANDOFF and OMENWARD profile
→ targeted repository evidence or benchmark
→ required external primary source
```

`REUSE_FIRST_PREFLIGHT_REQUIRED`와 `REUSE_LEARNING_HANDOFF_REQUIRED`를 적용한다. 단순 문서 정리·mechanical regeneration처럼 새 consumer나 제품 의미가 없는 작업은 근거와 함께 `NOT_APPLICABLE`로 기록한다. 후보 module·외부 asset·Base module은 actual consumer, provenance/rights, rollback과 project adapter route가 확인되기 전 설치하거나 runtime에 연결하지 않는다.

## 5. OMENWARD 제품·자산 경계

- 현재 제품 topology, combat/roulette rule, scene/UI priority는 current Decision, Active Context, GDD와 actual runtime owner가 단일 정본이다.
- Godot `assets/`, `scenes/`, `scripts/`, `data/`, `addons/`, `project.godot`은 보호 경로다. approved manifest가 있는 변경만 해당 baseline/approval contract로 검증한다.
- 이미지 상태는 `NEEDED → BRIEF_READY → GENERATED_CANDIDATE → REVIEWED → USER_APPROVED → CANON_REGISTERED → IMPLEMENTED → RUNTIME_VERIFIED`로 구분한다. 이미지는 image model로 생성하고, SVG/Canvas/primitive/vector 대체물로 제품 art를 만들지 않는다.
- actual consumer, repository path, SHA-256, prompt/source, rights/provenance, approval, implementation state가 함께 있을 때만 asset을 runtime candidate로 취급한다.
- runtime, human/device, accessibility, player UX, release/rights PASS는 서로 독립이다. 실행하지 않은 검증을 PASS로 쓰지 않는다.

## 6. Repository-only canon과 문서 구조

Repository Markdown/JSON/code/data/scene/resource/test/runtime evidence가 사람·기계 정본이다. Notion은 user-approved migration 완료 후 `RETIRED`이며 future read/write/delete는 금지한다. Google Sheet는 historical compatibility input으로만 보존하며 current authority나 routine synchronization target이 아니다.

문서 구조는 다음처럼 분리한다.

```text
current product meaning / approval  → Decision + GDD + Active Context owner
Base adoption / route              → PROJECT_BASE_ADAPTER + generated snapshot
human operating explanation        → docs/BASE_SHARED_SKILL_INTEGRATION.md
history / migration evidence       → dated archive or migration owner
```

동일 사실을 여러 current owner에 복제하지 않는다. current 상태를 고치면 해당 owner, linked test/validator, documentation map만 함께 갱신한다.

## Platform, release, and asset-rights routing

플랫폼/출시/권리의 실제 gate는 다음 owner에서만 판단한다. 이 파일은 NOT_RUN을 PASS로 올리지 않는다.

```text
docs/APPROVED_PC_ANDROID_PLATFORM_RELEASE_AUTHORITY_2026-08-05.md
docs/PLATFORM_RELEASE_AND_ASSET_RIGHTS_PROFILE.md
docs/ASSET_RIGHTS_AND_PROVENANCE_RECORD.md
docs/GAME_RELEASE_COMPLIANCE_EVIDENCE_PACK.md
PC / Steam = COMMITTED_PRIMARY
Android / Google Play = COMMITTED_RELEASE_TARGET_DEFERRED_RELEASE_NEAR
STOVE = SECONDARY_RELEASE_CANDIDATE
```

## 7. 구현·검증·GitHub 안전 규칙

- 의미 변경, public contract, dependency/cost/security, release scope, destructive deletion/migration, final human UX는 before/after, reason, expected effect, rollback을 제시한 별도 승인 뒤에만 바꾼다.
- 이미 승인된 동일 범위의 implementation continuation은 exact approval reference를 재사용한다. 제품 의미를 확장하지 않는다.
- test는 affected behavior를 먼저 RED로 고정하고 GREEN으로 만든다. static check, generated artifact check, canonical freshness, runtime(코드 변경 시), exact-head CI 순으로 검증한다.
- unrelated user changes, uncertain asset, legacy material, open/draft PR을 삭제·reset·force-push·rebase하지 않는다. direct `main` push와 ruleset bypass는 금지한다.
- completion route는 fetch/reconcile → validate → scoped commit → normal push → exact PR head CI → readback이다. merge는 사용자 명시 지시가 있을 때만 한다.

## 8. 완료 보고와 공용 환류

완료 보고는 `작업 전 문제 → 조사·비교 → 채택 구조와 이유 → 구현/준비 → 사용 예 → 기대효과 → 검증 증거 → 자동화·학습 반영 → 미검증·남은 위험` 순서를 따른다. 항상 현재 상태, 권장 조치, 요청 이유, 기대효과를 함께 밝힌다.

프로젝트 특수 교훈은 project owner에만 기록한다. 다른 프로젝트에도 검증된 개선은 Base promotion **candidate**로 제시하되, Base write·release pin 변경은 별도 review/approval 없이는 수행하지 않는다.
