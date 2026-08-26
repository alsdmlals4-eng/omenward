# OMENWARD · Image Production Master Checklist

```yaml
tracker_id: OMW-VIS-TRACKER-20260826-MASTER-01
status: CURRENT_PLANNING_CHECKLIST
created_at: 2026-08-26
scope: PLANNING_AND_IMAGE_PRODUCTION_TRACKING_ONLY
current_user_work_mode: PLANNING_PLUS_IMAGE_ONLY
product_code_mutation: NONE
godot_execution: NOT_IN_SCOPE
codex_execution: NOT_IN_SCOPE
image_generation: NOT_STARTED
current_visual_decision: OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01
current_reference_asset: OM-IMG-023
source_brief_package: OMW-VIS-BRIEF-20260826-CORE-PLAYER-FLOW-3PACK-01
```

## 1. 목적

이 문서는 OMENWARD에서 앞으로 제작해야 할 이미지의 **마스터 제작 관리표**다. 새 gameplay Decision을 만들지 않으며, 기존 Visual Requirement Inventory의 `OMW-VIS-001~012` 계보를 가능한 한 재사용한다.

2026-08-25 이후 새로 필수가 된 항목은 아직 영구 Asset ID를 임의 확정하지 않고 `TRACK-*` 제작 키로 관리한다. 실제 이미지가 승인될 때 필요한 경우 별도 Asset ID/Decision 승격을 검토한다.

Google Sheet는 현재 compatibility/history-only이며 이 체크리스트의 current authority가 아니다.

## 2. 공통 현재 Visual LOCK

모든 신규 이미지에서 다음을 우선한다.

```text
BATTLEFIELD_PRESENTATION = THREE_SIMULTANEOUS_FRONT_STATE_VIEWS
PER_FRONT_MINIMAP = REQUIRED
MINIMAP_IS_CONTEXT_NOT_SECOND_BATTLEFIELD = TRUE
VISUAL_STYLE = FANTASY_MAGIC_SD_TACTICAL_PIXEL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
BATTLEFIELD = PRIMARY
LOWER_CONTROL_DECK = SECONDARY
COMMANDER_ROLE = OMEN_WARDEN_COMMANDER_NOT_MELEE_HERO
CASINO_SLOT_MACHINE_LANGUAGE = FORBIDDEN
```

과거 `LONG_FULL_ROAD_PRESENTATION`, `NO_MINIMAP`, standalone `ANIME_PIXEL_ART`, standalone `CLEAN_PIXEL_ART`가 충돌하면 현재 Visual Decision이 우선한다.

## 3. 상태 정의

| 상태 | 의미 |
|---|---|
| `REFERENCE_APPROVED` | 이미 승인된 기준 이미지. 새 생성 대상 아님 |
| `BRIEF_READY` | 목적·구도·금지요소·검수표가 준비됨 |
| `NEEDS_BRIEF` | 제작 필요성이 확인됐지만 생성용 브리프 미완성 |
| `REBRIEF_REQUIRED` | 과거 브리프가 현행 Visual Decision과 충돌하여 다시 작성 필요 |
| `CANON_RECHECK` | 생성 전 최신 gameplay/수량/구조 정본 재확인 필요 |
| `BACKLOG` | 후속 제작 대상 |
| `GENERATING` | 이미지 1장 생성 중 |
| `USER_REVIEW` | 생성본 사용자 검수 중 |
| `APPROVED_CURRENT` | 사용자 승인 후 current visual lineage에 등록됨 |
| `REVISE` | 같은 브리프 기준 수정 필요 |
| `REJECTED_NOT_CANON` | 미승인. 구현/reference 승격 금지 |

## 4. 제작 완료 정의

이미지 한 건은 아래가 모두 끝나야 `APPROVED_CURRENT`다.

- [ ] current GitHub + Notion visual canon fresh-read
- [ ] 해당 이미지 브리프 준비
- [ ] 선행 이미지/컴포넌트가 필요한 경우 승인 상태 확인
- [ ] 정확히 1개 candidate 생성
- [ ] 이미지별 체크리스트 검수
- [ ] 사용자 `APPROVE / REVISE / REJECT` 판정
- [ ] 승인본만 Visual Bible / Asset Library / 관련 Flow에 등록
- [ ] destination readback
- [ ] runtime/human evidence와 이미지 승인 evidence를 혼동하지 않음

---

# 5. MASTER TABLE

## Reference · 이미 승인된 기준

| 순서 | Priority | ID | 이미지 | 목적 | 현재 상태 | 다음 Gate |
|---:|---|---|---|---|---|---|
| R0 | REF | `OM-IMG-023` | Front-State + Per-Front Minimap + SD Fantasy 승인 시안 | 모든 후속 이미지의 현재 방향 기준 | `REFERENCE_APPROVED` | 재생성하지 않고 reference로 사용 |

## P0 · Core Player Experience · 먼저 제작

| 순서 | Priority | ID / Tracker Key | 이미지 | 핵심 검증 목적 | 선행조건 | Brief | 생성 | 사용자 승인 | 다음 Gate |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | P0 | `OMW-VIS-003` | Main Battle / BATTLE Focus | 세 Front-State 동시 비교, 미니맵 3개, 병종 실루엣, 전투 가독성 | `OM-IMG-023` | `BRIEF_READY` | ☐ | ☐ | **현재 첫 생성 대상** |
| 2 | P0 | `OMW-VIS-001` | PREPARE / Roulette STOPPED-MANIPULATE | 3×3 + 12 direct arrows + preview + 결과 확정, 전장 지속 맥락 | 1번 시각 언어 승인 권장 | `BRIEF_READY` | ☐ | ☐ | 1번 승인 후 생성 |
| 3 | P0 | `OMW-VIS-002` | COMMIT / Irreversible Front Assignment | 병력→세 전선 PENDING 계획→atomic confirm의 비가역 판단 | 1~2번 승인 권장 | `BRIEF_READY` | ☐ | ☐ | 2번 승인 후 생성 |
| 4 | P0 | `TRACK-P0-3X3-COMPONENT` | 3×3 Roulette Component Sheet | 3×3 token grammar, 정확히 12 arrows, judging line, preview/confirm 상태 고정 | `OMW-VIS-001` 승인 | `NEEDS_BRIEF` | ☐ | ☐ | PREPARE 화면에서 실제 문법 추출 |
| 5 | P0 | `TRACK-P0-MINIMAP-RULES` | Per-Front Minimap Rule Sheet | progress/stronghold/clash/route exception 문법과 금지 예시 고정 | `OMW-VIS-003` 승인 | `NEEDS_BRIEF` | ☐ | ☐ | Main Battle에서 미니맵 문법 추출 |
| 6 | P0 | `OMW-VIS-004` | REVIEW Focus Mode | Forecast→Prepare→Commit→Key Event→Result 인과 설명 | 1~3번 승인 | `NEEDS_BRIEF` | ☐ | ☐ | Core 3-Pack 완료 후 브리프 |
| 7 | P0 | `OMW-VIS-005` | Ward Citadel / Battlefield Clean Plate | UI 없이 세계/전장 구조와 공간 문법 확인 | 현재 Front-State Decision | `REBRIEF_REQUIRED` | ☐ | ☐ | 과거 long-road clean plate 의미를 현행 Front-State 기준으로 재정의 |

### P0 완료 Gate

- [ ] `OMW-VIS-003` 승인
- [ ] `OMW-VIS-001` 승인
- [ ] `OMW-VIS-002` 승인
- [ ] 3×3 component grammar 분리 확인
- [ ] per-front minimap grammar 분리 확인
- [ ] REVIEW 화면 브리프 준비
- [ ] clean plate가 과거 long-road 정본을 되살리지 않음

---

## P1 · Production Readability · 핵심 3장 이후

| 순서 | Priority | ID / Tracker Key | 이미지 | 목적 | 상태 | 생성 전 확인 |
|---:|---|---|---|---|---|---|
| 8 | P1 | `OMW-VIS-006` | Triple Omen Wheels / Command Device Close-up | 세 릴의 세계관 장치성, 3전선 1:1 비대응, 카지노 문법 회피 | `REBRIEF_REQUIRED` | 현행 3×3 player-facing 조작면과 물리 3-reel 세계관 관계 재확인 |
| 9 | P1 | `OMW-VIS-007` | Omen Signature Icon Sheet | MASS / ARMORED / FLYING / INFILTRATION / SIEGE 형태 구분 | `NEEDS_BRIEF` | 현행 Signature 명칭/개수 fresh-read |
| 10 | P1 | `OMW-VIS-008` | Mobilization Seal / TokenSource Feedback | 건물→동원 확률/인장 기여의 인과 시각화 | `NEEDS_BRIEF` | 현행 building→roulette 기여 계약 fresh-read |
| 11 | P1 | `OMW-VIS-009` | Building Family Silhouette Board | 건물 종류와 Tier 성장 식별 | `CANON_RECHECK` | **과거 Inventory의 `7 building family`와 후속 기획의 건물 수 표현 충돌 가능성부터 해소** |
| 12 | P1 | `OMW-VIS-010` | Troop Archetype Silhouette Lineup | 전략 줌에서 병종 역할을 실루엣으로 구분 | `NEEDS_BRIEF` | 현행 병종 목록/role count fresh-read 후 확정 |
| 13 | P1 | `OMW-VIS-011` | Ally vs Veil Faction Pair Board | 색만이 아니라 형태 언어로 진영 구분 | `NEEDS_BRIEF` | 현재 ally/Veil palette + shape language 적용 |
| 14 | P1 | `TRACK-P1-OMEN-WARDEN` | Omen Warden Commander Sheet | 긴 지휘 깃발, 갑주/외투, 지휘 포즈, melee hero 오독 방지 | `NEEDS_BRIEF` | `OMW-PLAN-20260825-FRONT-STATE-MINIMAP-SD-FANTASY-01` |
| 15 | P1 | `OMW-VIS-012` | Stage 1 FTUE Build-group Cue Sheet | 첫 세션의 build-group 단계적 강조 | `CANON_RECHECK` | 현행 FTUE/건물 수/Stage 1 flow fresh-read |

### P1 완료 Gate

- [ ] Omen Wheel이 slot machine으로 읽히지 않음
- [ ] Signature 5종이 색 없이도 구분됨
- [ ] 건물→동원 확률 기여가 설명 가능함
- [ ] 현행 건물 목록 확정 뒤 building board 승인
- [ ] 현행 병종 목록 확정 뒤 troop lineup 승인
- [ ] Ally / Veil shape language 승인
- [ ] Omen Warden silhouette 승인
- [ ] FTUE cue가 current first-session flow와 일치

---

## P2 · Content Expansion · 후속 제작

아래는 과거 Visual Requirement Inventory에서 명시된 후속 이미지다. 영구 Asset ID는 아직 부여하지 않는다.

| 순서 | Priority | Tracker Key | 이미지 | 목적 | 상태 | 선행조건 |
|---:|---|---|---|---|---|---|
| 16 | P2 | `TRACK-P2-HIGH-GRADE-HIERARCHY` | Elite / Hero / Legendary / Mythic Boss Hierarchy Board | 등급·체급·연출 위계 | `BACKLOG` | 현행 고등급/보스 visual budget 확정 |
| 17 | P2 | `TRACK-P2-MERCHANT-REWARD` | Merchant / Reward / Growth Surface | Stage 종료 보상·상인·성장 화면 | `BACKLOG` | REVIEW/maintenance flow 승인 |
| 18 | P2 | `TRACK-P2-SPECIAL-BARRACKS` | Special Barracks T1 Reveal + T2 Specialization | 특수 병영 선택 구조 설명 | `CANON_RECHECK` | 현행 barracks role/output 기획 재확인 |
| 19 | P2 | `TRACK-P2-ASSASSIN-WARNING` | Assassin Bypass / Omen-Fog Warning | 침투 위협의 사전 경고 표현 | `BACKLOG` | infiltration Signature/route cue 확정 |
| 20 | P2 | `TRACK-P2-GATE-SIEGE-VFX` | Gate Damage / Siege Warning / Capture State VFX Sheet | 거점 피해·공성·위기 상태를 전장에서 읽기 | `BACKLOG` | per-front minimap + battle VFX 문법 승인 |
| 21 | P2 | `TRACK-P2-BIOME-WARD-KIT` | Biome / Ward Citadel Expansion Kit | 맵/환경 확장 시 동일 세계관 유지 | `BACKLOG` | clean plate + faction/environment language 승인 |

---

# 6. 현재 실제 작업 Queue

```text
NOW
1. OMW-VIS-003 · Main Battle

THEN
2. OMW-VIS-001 · PREPARE Roulette
3. OMW-VIS-002 · COMMIT

AFTER_CORE_3PACK
4. TRACK-P0-3X3-COMPONENT
5. TRACK-P0-MINIMAP-RULES
6. OMW-VIS-004 · REVIEW
7. OMW-VIS-005 · Current Front-State Clean Plate

THEN_PRODUCTION_READABILITY
P1 sequence

LATER
P2 content expansion
```

## 7. 한 장씩 생성하는 운영 규칙

```text
ONE CURRENT ITEM
→ fresh-read its brief/canon
→ generate ONE candidate
→ checklist review
→ USER APPROVE / REVISE / REJECT
→ only approved candidate is registered
→ advance tracker
```

금지:

- 여러 이미지를 한꺼번에 생성해서 서로 다른 시각 문법을 확산시키기
- 사용자 승인 전 `APPROVED_CURRENT` 처리
- 이미지가 예쁘다는 이유만으로 gameplay/UX drift 허용
- runtime/human usability를 이미지 승인만으로 PASS 처리
- 오래된 Visual Inventory의 `NO_MINIMAP`, long-road, 과거 art-style 표현을 current로 부활시키기

## 8. 현재 체크 상태

```text
REFERENCE_OM_IMG_023 = APPROVED
MASTER_CHECKLIST = READY
OMW_VIS_003_BRIEF = READY
OMW_VIS_003_GENERATION = NOT_STARTED
OMW_VIS_001_BRIEF = READY
OMW_VIS_001_GENERATION = NOT_STARTED
OMW_VIS_002_BRIEF = READY
OMW_VIS_002_GENERATION = NOT_STARTED
OTHER_IMAGE_BRIEFS = PARTIAL_OR_NOT_STARTED
GODOT_CODEX = OUT_OF_CURRENT_SCOPE
```

## 9. Source lineage

- `docs/images/planning/OMENWARD_CORE_PLAYER_FLOW_IMAGE_BRIEFS_2026-08-26.md`
- `docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md`
- `docs/design/OMENWARD_VISUAL_REQUIREMENT_INVENTORY_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_3X3_ROULETTE_COMPONENT_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_RUN_COMMAND_SCREEN_FOCUS_MODES_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_LOWER_CONTROL_DECK_SPEC_2026-08-20.md`
- `docs/design/APPROVED_OMENWARD_TEXT_UX_AND_STATE_TRANSITION_2026-08-20.md`
