# Base 규칙·공용 지식 버전

```yaml
status: HISTORICAL_ADOPTION_RECORD
base: alsdmlals4-eng/Base
historical_base_version: 9.4.0
historical_base_payload_commit: a728712cb776ec98f4875914a580fcf7d0156593
historical_base_trusted_evidence_commit: ef1fba11167e4da0b298123b0c85ebd268191a42
historical_base_pin_finalization_commit: 87a0b54c2847ce4b685879209205957c170cc1cd
historical_base_registry_sha256: 693a0dff3f054ecdd653079909e044211473838e73dd9aff07734d1ce5694c59
current_authority_policy: ALWAYS_REFETCH_CURRENT_COMPLETED_MAIN
current_loading_policy: BASE_OWNER_PROGRESSIVE_LOAD
google_sheets_policy: COMPATIBILITY_ONLY
project: alsdmlals4-eng/omenward
adoption_scope: OPERATING_CONTRACT_HISTORY_ONLY
product_paths_changed: false
```

이 파일은 OMENWARD가 과거 어떤 Base release를 채택했는지 추적하는 **historical adoption evidence**다. 현재 작업의 Base router나 Skill inventory를 고정하지 않는다.

현재 작업은 항상 다음 순서로 Base를 resolve한다.

```text
alsdmlals4-eng/Base latest completed main
→ root AGENTS.md
→ current skills/SKILL_REGISTRY.json inventory
→ trigger가 맞는 owner만 progressive-load
```

프로젝트 승인 정본·실제 code/data/Scene/Resource/test/runtime가 Base 기본값보다 우선한다. Project Notion은 사람용 정본이고 GitHub repository와 actual runtime은 구조화/runtime 정본이다. Google Sheet는 `COMPATIBILITY_ONLY` migration/history input이며 신규 기본 작업면이 아니다.

## 보호 경계

- OMENWARD 코어·3전선·징조륜·비가역 배치·결정론 규칙은 Base 업데이트만으로 변경하지 않는다.
- `data/`, `scripts/`, `scenes/`, `resources/`, `assets/`, `addons/`, `project.godot`은 별도 제품 구현 승인 없이 운영계약 동기화가 수정하지 않는다.
- 과거 Base pin/registry hash는 provenance와 rollback evidence로만 보존한다.
- 새 Base main에서 route/schema/owner가 바뀌면 project adapter/router/validator 영향을 fresh audit한다.
- runtime·입력·사람 이해·player experience는 실제 실행 전 `NOT_RUN`이다.
