# [제안] OMENWARD HiGodot·GUT 권위 분리와 GUT 9.7.1 채택

```yaml
decision_id: OMW-DEC-20260806-TOOLS-HIGODOT-GUT-AUTHORITY-AND-WORK-ENTRY-GATE-V1
status: USER_DIRECTED_DESIGN / DRAFT_PR_REQUIRED / ACTIVATION_BLOCKED
counter: NON_COUNTER
product_code_authority: NONE
```

## 결론

```text
HIGODOT_AUTHORING_AUTHORITY
GUT_TEST_AUTHORITY
MUTATION_AUTHORITY_OVERLAP = FORBIDDEN
WORK_ENTRY_GATE = FAIL_CLOSED
BOOTSTRAP_EXCEPTION = PR155_ONLY
BROAD_REMEDIATION_PREFIX = FORBIDDEN
```

HiGodot은 Scene·Node·Resource·`project.godot`·InputMap·autoload 등 Godot 저작·편집의 단일 mutation 권위다. GUT는 test discovery, assertion, double, execution, JUnit report를 소유하는 테스트 권위다. GUT 테스트가 제품 Scene·Resource·프로젝트 설정을 영구 수정하거나 HiGodot이 테스트 결과를 임의로 통과 처리하는 역할 침범을 금지한다.

## GUT 9.7.1 출처·호환성

- upstream: `bitwes/Gut`
- branch: `godot_4_7`
- reviewed commit: `aeb5d4f3f7f0a6c9b5e178876d6c99b791fda605`
- plugin version: `9.7.1`
- declared Godot compatibility: `4.7.x`
- project Godot feature: `4.7`
- GUT license: MIT
- bundled font license: SIL OFL 1.1

문서 호환성은 PASS지만 OMENWARD 실제 import·CLI·Windows·Android 검증은 `NOT_RUN`이다.

## Vendor 판정

```text
UPSTREAM_ADDONS_TREE = 5d6893836af4917ee62b1a395125a7530b1f239d
PROJECT_ADDONS_TREE = 09d040309bbed0e07420ad72c4aa69cbd0e58190
VENDOR_TREE_MISMATCH
MANIFEST_RECONCILIATION_REQUIRED
ACTIVATION_READY = FALSE
```

`plugin.cfg` blob은 upstream과 일치하지만 전체 subtree는 일치하지 않는다. 전체 manifest를 비교해 의도된 Godot import 산출물인지, 누락·추가 파일인지 판정하기 전에는 활성화를 승인하지 않는다.

## 소비 경로

```text
TEST_ROOT = res://tests/gut
CLI_ENTRY = res://addons/gut/gut_cmdln.gd
REPORT = artifacts/gut/junit.xml
PROJECT_SCENE_RESOURCE_MUTATION_BY_GUT = FORBIDDEN
```

실행 후보는 exact Godot executable의 `--help` 확인 뒤 확정한다. `<EXACT_GODOT_BIN>`은 실행 전 환경에서 해소해야 하는 명시적 입력 토큰이며, 검증 없이 실제 명령으로 보고하지 않는다.

## CI Gate

CI는 다음을 실패 폐쇄한다.

1. HiGodot과 GUT의 owned surface 중복.
2. GUT의 제품 파일 mutation 허용.
3. vendor tree mismatch 상태에서 `ACTIVATION_READY` 주장.
4. import·GUT CLI·project regression 미실행 상태에서 채택 완료 주장.
5. Decision Ledger·미확정 목록·Sheet·이미지 검수 상태 충돌 상태에서 일반 제품 작업 진입.

현재 차단 상태의 bootstrap 예외는 PR #155·고정 브랜치·고정 base SHA·10개 exact path에만 적용한다. `addons/gut/**` 같은 포괄 prefix remediation은 금지한다. 후속 정본/vendor 교정은 별도 Decision·PR·base SHA·exact changed-file 목록을 먼저 승인한 경우에만 허용한다.

Godot authoring surface와 GUT test surface가 한 변경 묶음에 함께 나타나면 CI가 실패한다. Scene·Resource·`project.godot` 변경은 `HIGODOT_AUTHORING_AUTHORITY` manifest가 실제 authoring 파일 목록과 정확히 일치해야 한다.

## REMOVAL_AND_ROLLBACK_PROCEDURE

1. GUT 활성화가 존재한다면 HiGodot만 `project.godot`의 활성 상태를 되돌린다.
2. GUT 전용 테스트·CI·report wiring을 제거한다.
3. 전체 참조 검색이 0일 때만 `addons/gut`를 제거한다.
4. clean import, 기존 Python 계약, Godot regression을 재실행한다.
5. Scene·Resource·게임 데이터·무관한 프로젝트 설정 변경이 없는지 diff로 증명한다.

## 현재 판정

```text
DESIGN = READY_FOR_DRAFT_REVIEW
GUT_FORMAL_ADOPTION_INTENT = APPROVED
GUT_ACTIVATION = BLOCKED
GUT_RUNTIME = NOT_RUN
PROJECT_CODE = UNCHANGED
LOCAL_GODOT = BLOCKED_NO_LOCAL_ACCESS
```
