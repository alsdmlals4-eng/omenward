# Godot Live-Editor Pilot Adoption

## Status

```yaml
adoption_mode: TEMPORARY_COPY_ONLY
legacy_source_policy: LEGACY_GODOT_AI_SOURCE_PRESERVED
legacy_workspace_policy: LEGACY_DISABLED_IN_DISPOSABLE_COPY_ONLY
mutation_authority_policy: DUAL_MUTATION_AUTHORITY_FORBIDDEN
main_scene_policy: MAIN_SCENE_READ_ONLY
mutation_policy: SCRATCH_SCENE_MUTATION_ONLY
source_integrity: SOURCE_TREE_UNCHANGED
base_pilot_commit: 2b595570bd237174b2b962a1eb54588b5ecc508d
evidence_bundle: SELF_CONTAINED_EVIDENCE_BUNDLE
expected_platform: PC
PRODUCTION_ADAPTER_READY: NOT_READY
```

이 저장소는 Base C0.1 Pilot의 immutable commit `2b595570bd237174b2b962a1eb54588b5ecc508d`를 네 개 채택 파일로만 연결합니다.

## Legacy 공존 경계

`LEGACY_GODOT_AI_SOURCE_PRESERVED`는 원본 저장소의 `res://addons/godot_ai/plugin.cfg`, Godot AI Addon 바이트, `_mcp_game_helper`를 유지한다는 뜻입니다.

`LEGACY_DISABLED_IN_DISPOSABLE_COPY_ONLY`는 Base runner가 임시 작업공간을 만들고 선언된 Plugin·Autoload 항목만 복사본에서 비활성화한다는 뜻입니다. 원본 `project.godot`은 변경하지 않습니다.

`DUAL_MUTATION_AUTHORITY_FORBIDDEN`에 따라 Godot AI와 Base transaction adapter는 Pilot 작업공간에서 동시에 편집 권한을 갖지 않습니다.

## Pilot 실행

Godot 4.7.1로 임시 프로젝트를 Import·Parse한 뒤, 현재 저장소의 11개 `tests/headless/*.gd` 회귀를 같은 작업공간에서 실행합니다.

실제 메인 Scene `res://scenes/main/main.tscn`은 `MAIN_SCENE_READ_ONLY`로만 검사합니다. Rename·Editor Undo·Save·물리 SHA-256 검증은 runner 소유 `res://.godot-live-editor-pilot/scratch.tscn`에서만 수행합니다.

원본 Git tracked 바이트는 실행 전후 인벤토리를 비교하며, 변경이 있으면 `SOURCE_TREE_UNCHANGED` 위반으로 실패합니다.

## Evidence bundle

`SELF_CONTAINED_EVIDENCE_BUNDLE`은 다음 세 파일을 요구합니다.

```text
project-pilot-evidence.json
runtime-result.json
scratch.tscn
```

다운로드 후 `runtime-result.json`과 `scratch.tscn`을 독립 재해시해 Evidence JSON의 SHA-256과 대조해야 합니다.

## 플랫폼·제품 보호 경계

`expected_platform: PC`는 Ubuntu desktop headless Pilot의 실행 경계입니다. OMENWARD의 PC·Android 제품 계획 전체를 검증한다는 뜻이 아닙니다.

전투·룰렛·경제·스테이지·플랫폼 계약·저장·UI·데이터·에셋·기획 정본·Decision·Registry·Google Sheet·제품 Scene·Resource·GDScript는 이 채택으로 변경하지 않습니다.

Program B authenticated local STDIO MCP transport와 Program C opt-in runtime debugger는 구현하지 않습니다.

```yaml
actions_runner: BLOCKED_RUNNER_ID_0
exact_head_ci: BLOCKED_ENVIRONMENT
runtime_artifact: NOT_PRODUCED
android_device: NOT_RUN
android_export: NOT_RUN
physical_input: NOT_RUN
human_editor_usability: HUMAN_NOT_RUN
windows_production_operation: NOT_RUN
PRODUCTION_ADAPTER_READY: NOT_READY
```

환경 차단이 해소되어 exact-head Workflow와 자체 완결형 Artifact 검증이 모두 통과하기 전에는 이 Draft를 병합하지 않습니다.

## 제거

Rollback은 다음 네 파일의 단일 revert입니다.

```text
.godot-live-editor/project-pilot.json
docs/GODOT_LIVE_EDITOR_ADOPTION.md
tests/test_godot_live_editor_adoption.py
.github/workflows/validate-godot-live-editor-pilot.yml
```
