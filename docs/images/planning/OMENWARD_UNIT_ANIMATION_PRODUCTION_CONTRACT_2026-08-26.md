# OMENWARD · Unit Animation Production Contract V1

```yaml
contract_id: OMW-PLAN-20260826-UNIT-ANIMATION-PRODUCTION-CONTRACT-01
status: USER_APPROVED_PRODUCTION_GATE
approved_at: 2026-08-26
approval_input: "승인"
issue_tracking: GitHub Issue #33
authority_domain: REPOSITORY_STRUCTURED_CANON
scope: SHIELD_GUARD_LUMERN_VEIL_PAIR_PILOT_ONLY
visual_generation: USER_REQUEST_ONLY
pixel_cleanup: NOT_RUN
pair_geometry_addendum: REQUIRED_BEFORE_ATLAS_PRODUCTION
godot_implementation: OUT_OF_SCOPE
runtime_validation: NOT_RUN
```

## 1. 목적과 범위

이 계약은 사용자 승인된 Shield Guard idle 원본 두 장을 이후의 픽셀 정리·animation atlas 제작·Godot 통합으로 넘길 때, 양 진영의 **전투 역할과 시간 계약이 갈라지지 않도록** 하는 생산 Gate다.

포함 범위는 `ASSET-UNIT-LUMERN-SHIELD-GUARD-IDLE-V1`과 `ASSET-UNIT-VEIL-SHIELD-GUARD-IDLE-V1`의 pair pilot뿐이다. 나머지 18개 병종, Token crop, VFX, Godot code/Scene/Resource 변경, runtime import는 포함하지 않는다.

## 2. 승인 원본과 보관 경계

| 진영 | 승인 원본 | 승인 기록 | 현재 상태 |
|---|---|---|---|
| Lumern | `ASSET-UNIT-LUMERN-SHIELD-GUARD-IDLE-V1` | `OMW-ASSET-APPROVAL-20260826-LUMERN-SHIELD-GUARD-IDLE-V1` | `USER_APPROVED_CURRENT_VISUAL_ASSET` |
| Veil | `ASSET-UNIT-VEIL-SHIELD-GUARD-IDLE-V1` | `OMW-ASSET-APPROVAL-20260826-VEIL-SHIELD-GUARD-IDLE-V1` | `USER_APPROVED_CURRENT_VISUAL_ASSET` |

- 승인 원본은 `.asset-vault/library/...`에 보존하며 덮어쓰지 않는다.
- 승인된 생성 이미지는 프로젝트 로컬 원본과 Notion 승인 자산 기록이 모두 readback된 경우에만 보관 완료다.
- cleanup 결과는 승인 원본의 역할·실루엣·진영 언어를 바꾸지 않는 fidelity 작업으로 한정한다. 이 범위를 넘는 형태·색·포즈 변경은 새 시각 승인으로 되돌린다.
- Google Drive 원본은 보조 보관처이며 프로젝트 로컬 원본 또는 Notion 기록을 대체하지 않는다.

## 3. 공통 gameplay / visual pair 불변식

같은 `shield_guard` archetype의 Lumern과 Veil은 서로 다른 이미지 세트이지만 다음을 공유한다.

```text
STATE_ORDER = deploy / idle / move / attack_basic / skill_1 / hit_light / death / victory
SOURCE_FACING = RIGHT
COMBAT_ROLE = frontline defender
PRIMARY_MASS = broad frontal shield or carapace defense mass
GROUND_CONTACT = same baseline logic
PIVOT = same ground-contact anchor logic
ATLAS_LAYOUT = same state order, cell envelope, frame count, and mirror convention
COMBAT_TIMING = visual_faction_id must not change gameplay timing
```

Lumern은 방패·아치·절제된 금속/천의 질서로, Veil은 전면 갑각·비대칭 균열·절제된 rift glow로 같은 방어 역할을 표현한다. Veil을 보스 체급으로 키우거나 Lumern을 영웅형 기사로 과장해 pair의 전술 규모를 깨면 실패다.

## 4. 상태별 제작 계약

| State | 역할 키포즈 | pair 상태 | atlas 제작 조건 |
|---|---|---|---|
| `idle` | 낮은 중심, 전면 방어 질량 고정, 미세 체중 이동 | 두 진영 원본 승인 완료 | pixel cleanup과 pair geometry addendum 뒤 |
| `move` | 방패 방향을 유지한 짧은 보폭 | 미제작 | pair geometry addendum 뒤 |
| `attack_basic` | 방어면 옆의 짧은 찌르기/베기 | 미제작 | actual attack event owner와 대조 뒤 |
| `skill_1` | 별도 핵심 능력의 명확한 준비·판정·회복 | 미제작 | 현재 gameplay choreography fresh-read 뒤에만 |
| `hit_light` | 1~2px 수준의 짧은 반동/플래시, 공격 흐름 과도 중단 금지 | 미제작 | pair geometry addendum 뒤 |
| `death` | 낮은 붕괴와 충돌 제거 인지 | 미제작 | collision/removal event와 대조 뒤 |
| `deploy` | 증원·배치 도착이 읽히는 짧은 진입 | 미제작 | deployment event와 대조 뒤 |
| `victory` | 방패를 세우고 짧게 무기를 정리 | 미제작 | stage-result presentation과 대조 뒤 |

`skill_1`의 choreography와 모든 state의 정확 frame count/FPS는 현재 `NOT_LOCKED`다. 과거 guide의 frame range는 탐색 예산일 뿐 이 계약에서 runtime 수치로 승격하지 않는다.

## 5. Geometry / timing addendum Gate

대량 atlas 제작 전에, cleaned Shield Guard pair를 기준으로 아래 값을 **하나의 pair geometry addendum**에 기록해야 한다.

```text
MASTER_CANVAS_WIDTH / HEIGHT
CELL_WIDTH / HEIGHT
GROUND_BASELINE_Y
PIVOT_X / Y
SOURCE_SCALE_AND_NEAREST_NEIGHBOR_RULE
STATE_FRAME_COUNTS
STATE_FPS_OR_DURATION
LOOP_FLAGS
ATTACK_IMPACT_FRAME
PROJECTILE_SPAWN_FRAME = NOT_APPLICABLE_OR_EXACT_FRAME
MIRROR_CONVENTION
```

이 값은 Lumern/Veil 사이에서 달라질 수 없다. `visual_faction_id`는 palette·sprite source만 선택하며 공격속도, damage, cooldown, impact timing을 변경하지 않는다.

이 addendum이 없으면 `MASS_UNIT_ATLAS_PRODUCTION = BLOCKED`다. 단, 승인된 idle 원본의 비파괴적 cleanup 준비와 문서 검수는 허용된다.

## 6. Cleanup / export readiness

`IMPLEMENTATION_READY`는 아래를 모두 만족할 때만 검토할 수 있다.

- [ ] 양쪽 원본의 project-local/Notion 보관과 checksum이 다시 확인됨.
- [ ] 투명 배경, UI·문구·바닥 그림자 없는 cleaned master가 비파괴적으로 생성됨.
- [ ] hard pixel edge, 일관된 pixel density, fuzzy alpha edge 없음.
- [ ] Shield Guard primary silhouette와 진영별 모양 언어가 승인 원본과 동일하게 유지됨.
- [ ] pair geometry addendum이 양쪽에 공통 적용됨.
- [ ] export filename·dimensions·SHA-256·Notion approval record가 남음.
- [ ] Godot import 전 asset reviewer가 visual regression 없음을 판정함.

이 목록을 통과해도 runtime import/readability와 release-rights review는 별도 Gate다.

## 7. 현재 코드와 통합 경계

현재 `scripts/units/unit_view.gd`는 procedural graybox이고 `scripts/data/animation_contract.gd`는 state ID만 소유한다. 이 계약은 두 파일, `scenes/units/unit.tscn`, `data/bootstrap_catalog.tres` 또는 faction visual profile을 변경하도록 승인하지 않는다.

후속 Codex scope는 B안의 P0 및 current-consumer P1 자산 전체가 사용자 승인·cleanup·export·`IMPLEMENTATION_READY`를 충족한 뒤에만 별도 Issue/Goal로 열 수 있다.

## 8. 검증과 다음 Gate

| 검증 | 현재 상태 |
|---|---|
| 계약과 기존 state ID 일치 | `DOCUMENT_REVIEW_REQUIRED` |
| Lumern/Veil idle 원본 보관·hash | `PROVEN` |
| pixel cleanup / master export | `NOT_RUN` |
| geometry / timing addendum | `NOT_RUN` |
| Godot import / runtime readability | `NOT_RUN` |
| human player test | `NOT_RUN` |

```text
CURRENT_GATE = PAIR_PIXEL_CLEANUP_AND_MASTER_EXPORT_PREPARATION
NEXT_IMAGE_OR_EDIT_ACTION = REQUIRES_ITS_OWN_EXPLICIT_USER_APPROVAL
NEXT_DECISION_AFTER_CLEANUP = PAIR_GEOMETRY_AND_TIMING_ADDENDUM
CODEX_GODOT = BLOCKED
```

## 9. Adversarial review

- **Hidden recolor risk:** same frame layout must not turn Veil into a purple human knight. Preserve faction-specific silhouette while holding the shared pivot/timing contract.
- **Premature numeric lock risk:** no atlas cell size, FPS, or impact frame is invented from an approved concept image. Those values require the cleaned pair and an addendum.
- **Implementation leak risk:** this document does not authorize `UnitView` replacement, resource schema expansion, or runtime claims.
- **Asset-loss risk:** cleanup never overwrites approved originals; dual storage and checksum remain mandatory.
- **Scope-creep risk:** this pilot does not authorize the remaining unit roster, tokens, VFX, or new generated imagery.
