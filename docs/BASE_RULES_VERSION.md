# Base 규칙·공용 지식 버전 — 프로젝트 채택 이력

```yaml
artifact_role: PROJECT_BASE_ADOPTION_HISTORY
base: alsdmlals4-eng/Base
historical_adopted_base_version: 9.4.0
historical_base_payload_commit: a728712cb776ec98f4875914a580fcf7d0156593
historical_base_trusted_evidence_commit: ef1fba11167e4da0b298123b0c85ebd268191a42
historical_base_pin_finalization_commit: 87a0b54c2847ce4b685879209205957c170cc1cd
historical_base_registry_sha256: 693a0dff3f054ecdd653079909e044211473838e73dd9aff07734d1ce5694c59
project: alsdmlals4-eng/omenward
adoption_scope: OPERATING_CONTRACT_ONLY
product_paths_changed: false
current_base_authority: FRESH_LATEST_COMPLETED_MAIN
current_release_integrity_owner: skills/PROJECT_BASE_ADAPTER.json
```

```text
CURRENT_BASE_AUTHORITY = FRESH_LATEST_COMPLETED_MAIN
GOOGLE_SHEETS = COMPATIBILITY_ONLY
```

이 파일은 OMENWARD가 과거 어떤 Base release를 채택했는지 추적하는 **역사/호환 증거**다. 현재 Base 행동 규칙·Skill·Work Mode·검증 절차의 정본이 아니다. 현재 작업은 항상 fresh Base latest completed `main`의 `AGENTS.md`, current Registry, trigger에 맞는 owner를 먼저 읽고, `skills/PROJECT_BASE_ADAPTER.json`의 exact release pin은 채택 패키지 무결성과 compatibility 검증에만 사용한다.

프로젝트 승인 정본·실제 코드·데이터·Scene·테스트가 Base 기본값보다 우선한다. 현재 사람용 프로젝트 정본은 Project Notion이고, 구조화·runtime truth는 repository와 실제 실행 증거가 소유한다. Google Sheets는 미이관 고유 자료가 필요한 경우의 migration/compatibility source일 뿐 신규 작업면이 아니다.

## 보호 경계

- OMENWARD 현재 코어·세 전선·징조륜·비가역 배치·TokenSource·결정론 규칙을 이 운영 교정에서 변경하지 않는다.
- `data/`, `scripts/`, `scenes/`, `resources/`, `assets/`, `addons/`, `project.godot`은 이 운영 교정에서 수정하지 않는다.
- release pin 변경은 별도 Base adoption/migration 검증 없이 자동 수행하지 않는다.
- Godot 런타임·입력·사람 이해·player experience는 실제 실행 전 `NOT_RUN`이다.

새 Base release·Registry·route·adapter Schema가 바뀌면 fresh Base owner와 프로젝트 Adapter/Router/Validator를 함께 재감사한다. 새 release가 존재한다는 사실만으로 프로젝트 release pin을 자동 승격하지 않는다.
