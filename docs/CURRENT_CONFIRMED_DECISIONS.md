# OMENWARD · Current Confirmed Decisions

```yaml
updated_at: 2026-08-20
status: CURRENT_DECISION_RECOVERY_INDEX
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.7
planning_reopened_at: 2026-08-20
current_planning_track: WORLD_CORE_FTUE_UI_VISUAL_REPLAN
runtime_evidence_ceiling: NOT_CHANGED_BY_THIS_INDEX
human_play_evidence: NOT_RUN
```

이 문서는 현재 승인 Decision을 새 채팅에서 빠르게 복원하기 위한 인덱스다. 상세 규칙은 각 Decision owner가 책임지며, Notion은 사람이 읽는 전체 그림·Flow·비교표를 책임진다. 구현·runtime truth는 repository code/data/scene/test/evidence가 책임진다.

## 2026-08-20 재기획 현재 Decision

| Decision ID | 승인 핵심 | Repository structured owner | Notion human-facing owner | 대표 반영 commit | 상태 |
|---|---|---|---|---|---|
| `OMW-PLAN-20260820-WORLD-ROLE-01` | 플레이어는 세 전선을 지키는 `징조수호관(Omen Warden)`이며 룰렛은 도박이 아니라 군사적 확률/동원 장치다. | `docs/design/APPROVED_OMENWARD_WORLD_ROLE_AND_OMEN_WARD_IDENTITY_2026-08-20.md` | Project Home · 세계관/플레이어 역할 | `8d3c1699ff2aaec999c85f140270780f586309df` | CONFIRMED |
| `OMW-PLAN-20260820-MAPRUN-WORLD-01` | 한 MapRun은 하나의 수호성이 버티는 20 Stage `Omen Cycle`; 세계에는 여러 수호성이 존재한다. | `docs/design/APPROVED_OMENWARD_OMEN_CYCLE_MAPRUN_WORLD_2026-08-20.md` | Project Home + `08 · 핵심 시스템 · 상세` | `cbe1b3d7de2dcc1aa41b9f60def500d4faf58bc5` | CONFIRMED |
| `OMW-PLAN-20260820-PRESSURE-LANGUAGE-01` | 5 Pressure는 적 종족이 아니라 복합 가능한 `Omen Signature`; 세 전선도 특정 Pressure 전용이 아니다. | `docs/design/APPROVED_OMENWARD_PRESSURE_LANGUAGE_AND_OMEN_SIGNATURES_2026-08-20.md` | Project Home + `다섯 압력 모델` + `08` | `982bdee79cdbc780201ac9791bb01b3f95c308ba` | CONFIRMED |
| `OMW-PLAN-20260820-MOBILIZATION-REGISTRY-01` | 자동생산은 직접 훈련, TokenSource는 동원 인장 등록. 세 징조륜은 세 전선과 1:1 대응하지 않는다. | `docs/design/APPROVED_OMENWARD_MOBILIZATION_REGISTRY_AND_TRIPLE_OMEN_WHEELS_2026-08-20.md` | Project Home + `자동생산 ≠ TokenSource` + `세 원형 릴` + `08` | `41d9927af7f6a5c28e14beab513635328f923486` | CONFIRMED |
| `OMW-PLAN-20260820-FIRST5-FTUE-01` | Stage 1~5를 `인과 이해 → 미래 수정 → 순간 개입 → 응용 시험 → 첫 결산`의 숙련 사다리로 운영한다. | `docs/design/APPROVED_OMENWARD_FIRST5_FTUE_MASTERY_LADDER_2026-08-20.md` + `docs/ONBOARDING_PLANNING_CURRENT_AUTHORITY.md` | Project Home + `03 · UI · 게임플레이 Flow Map` + `08` | `d0708598170045eb24819d25b4e26d137a0689a8` | CONFIRMED |
| `OMW-PLAN-20260820-RUN-COMMAND-SHELL-01` | 하나의 Run Command Screen에서 `PREPARE → COMMIT → BATTLE → REVIEW` Focus Mode를 사용하고 debug/raw 정보는 player HUD에서 분리한다. | `docs/design/APPROVED_OMENWARD_RUN_COMMAND_SCREEN_FOCUS_MODES_2026-08-20.md` | Project Home + `03 · UI · 게임플레이 Flow Map` + `08` | `8a553ac47d64b91545f50301a881e2e220a36828` | CONFIRMED |

## 보호되는 상위 정체성

```text
건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.

징조 관측
→ 건설 / 동원 인장 / 확률 설계
→ 병력 획득
→ 세 전선 중 하나에 비가역 커밋
→ 자동전투 + 제한된 수동 전술
→ 인과 복기
→ 다음 설계
```

다음은 현재 재기획에서도 보호한다.

- `ROULETTE_IDENTITY = PLAYER_CONSTRUCTED_PROBABILITY_ENGINE`
- `GAMBLING_FANTASY_POSITIONING = FORBIDDEN`
- 세 전선 비가역 커밋
- Forecast는 대응 가능한 정보를 주되 정답 카운터를 직접 지시하지 않음
- 자동생산과 TokenSource는 별도 획득 경로
- Stage 5/10/15/20 Boss cadence
- Stage 1 필수 T1 6종은 현재 유지; 실제 FTUE 과부하가 관측되면 축소안을 재검토
- player-experience PASS는 release-near Vertical Slice 사람 플레이 전까지 금지

## 현재 다음 Gate

```text
CURRENT_NEXT = VISUAL_REQUIREMENT_INVENTORY
NEXT_DECISION_CLASS = VISUAL_NORTH_STAR_PRIORITY
IMPLEMENTATION_START = NOT_AUTHORIZED_BY_THIS_INDEX
CURRENT_GODOT_RUNTIME = NOT_RUN_IN_2026-08-20_REPLAN_CHAT
OPEN_DRAFT_PR_197 = READ_ONLY_OTHER_WORKSTREAM
```

Visual Requirement Inventory에서 필요한 대표 화면·전장·건물/병종·Omen Wheel·Forecast·Review 시각 자료를 우선순위화하고, 첫 생성 자산은 사용자 생성 승인을 받은 뒤 한 장씩 제작·승인·Notion readback한다.

## 재개 규칙

1. 이 인덱스와 최신 `main`을 먼저 읽는다.
2. 기존 Decision이 유효하면 같은 질문을 다시 묻지 않는다.
3. Notion 사람용 표현과 repository owner가 다르면 `CANON_CONFLICT` 또는 `NOTION_OUTDATED / REPOSITORY_OUTDATED`로 먼저 복구한다.
4. 진행 중 open/draft PR은 별도 workstream으로 읽기 전용 처리하고 현재 기획 sync 때문에 수정하지 않는다.
5. 실제 runtime/사람 검증을 수행하지 않은 항목은 `NOT_RUN / UNVERIFIED`를 유지한다.
