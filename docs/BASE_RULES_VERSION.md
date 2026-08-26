# Base 규칙·공용 지식 버전

```yaml
base: alsdmlals4-eng/Base
base_version: 9.4.0
base_payload_commit: a728712cb776ec98f4875914a580fcf7d0156593
base_trusted_evidence_commit: ef1fba11167e4da0b298123b0c85ebd268191a42
base_pin_finalization_commit: 87a0b54c2847ce4b685879209205957c170cc1cd
base_registry_sha256: 693a0dff3f054ecdd653079909e044211473838e73dd9aff07734d1ce5694c59
release_state: BASE_RELEASED
project: alsdmlals4-eng/omenward
adoption_scope: OPERATING_CONTRACT_ONLY
product_paths_changed: false
```

프로젝트 승인 정본·실제 코드·데이터·Scene·테스트가 Base 기본값보다 우선한다. Base v9.4는 모델·추론·Prompt caching·비용 측정, 지시 권위, Interface-first Prompt, Context 큐레이션, Artifact 주장 상한, Godot UI 모션 계약을 제공한다.

## 보호 경계

- OMENWARD V2 코어·3라인·위협·릴·배치·TokenSource·룰렛·결정론 규칙을 변경하지 않는다.
- `data/`, `scripts/`, `scenes/`, `resources/`, `assets/`, `addons/`, `project.godot`은 이 적용에서 수정하지 않는다.
- Sheet는 `SHEET_GITHUB_CONFLICT / NO_AUTOMATIC_OVERWRITE`를 유지한다.
- Godot 런타임·입력·사람 이해·provider 비용은 `NOT_RUN` 또는 `HUMAN_NOT_RUN`이다.

새 Base release·Registry·route·adapter Schema가 바뀔 때 프로젝트 정본·Router·Validator와 함께 재감사한다.
