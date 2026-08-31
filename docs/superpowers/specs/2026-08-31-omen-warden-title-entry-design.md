# Omen Warden Title Entry Design

```yaml
decision_id: OMW-PLAN-20260831-OMEN-WARDEN-TITLE-ENTRY-01
approved_at: 2026-08-31 KST
approval_source: USER_CHAT__"승인,진행해"
status: USER_APPROVED__TITLE_ASSETS_CANON_REGISTERED__IMPLEMENTED__MACHINE_VERIFIED__RUNTIME_TECHNICAL_SMOKE_PASS__HUMAN_NOT_RUN
scope: TITLE_ENTRY / BOOT_TO_TUTORIAL_ROUTE / TITLE_RUNTIME_ASSET_CANDIDATES
authority_domain: REPOSITORY_STRUCTURED_CANON
publication_policy: source_only
runtime_evidence: LOCKED_ART_MACHINE_VERIFIED__RUNTIME_TECHNICAL_SMOKE_PASS__HUMAN_NOT_RUN
human_usability_evidence: NOT_RUN
```

## Goal

현재 부팅 직후 곧바로 튜토리얼을 시작하는 경로를, 세계관을 보여 준 뒤 플레이어가 명시적으로
`원정 시작`을 선택하는 진입 화면으로 교체한다. 이 화면은 저장·설정·메타 진행을 새로 만들지
않으며, 기존 튜토리얼 Stage와 단일 전선 Run Command 흐름을 그대로 시작한다.

## Player experience

```text
부팅
→ 수호 성채와 먼 베일 균열을 한 장면에서 읽는다
→ “징조를 읽고, 전선을 지휘하라”는 역할을 확인한다
→ 원정 시작
→ 기존 tutorial_stage의 내정 탭
→ 룰렛 → 단일 전선 커밋 → 전투
```

첫 화면은 전투 UI를 다시 설명하거나 가짜 메타 메뉴를 늘어놓지 않는다. 플레이어가 지금 할
수 있는 행동은 한 가지이며, 그 행동의 결과도 실제로 존재한다.

## Confirmed structure

| Element | Rule |
|---|---|
| Entry state | `GameSession`은 bootstrap 성공 뒤에도 자동으로 Stage를 시작하지 않는다. |
| Primary action | `원정 시작`은 bootstrap이 성공한 뒤에만 활성화되고 `tutorial_stage`를 시작한다. |
| Transition | 실제 Stage 시작 신호를 받은 뒤에만 TitleScreen을 숨기고 RunCommandScreen을 보인다. |
| Failure | bootstrap 실패 시 시작 버튼은 비활성 상태를 유지하고 실패 문구를 보여 준다. |
| Excluded UI | 저장 파일이 없으므로 Continue, Save, Settings, Shop, Record 메뉴를 만들지 않는다. |
| Existing game flow | 튜토리얼의 `내정 → 룰렛 → 전선`과 전투 데이터·경제·건물 로스터는 변경하지 않는다. |

## Visual and asset contract

```text
STYLE = STORYBOOK_WATERCOLOR_SD_TACTICAL_ILLUSTRATION
ALLY = NAVY + IVORY + COOL_GRAY_METAL + RESTRAINED_GOLD
VEIL = BLACK_PURPLE + DARK_RED + CARAPACE_GRAY + LIMITED_RIFT_GLOW
TITLE_COMPOSITION = WARD_WALL_DEFENSE_LEFT + ACTIVE_WARD_REAR_ROLES + VEIL_BATTLE_SURGE_RIGHT + SAFE_UPPER_CENTER_WORDMARK
BAKED_TEXT_IN_GENERATED_IMAGE = FORBIDDEN
BATTLEFIELD_BUILDINGS_OR_CONSTRUCTION_NODES = FORBIDDEN
```

승인된 자산은 서로 다른 레이어로 유지한다.

1. `TITLE-BG-06`: 16:9 수채화 전쟁 배경. 성벽의 수호군은 모두 후면 실루엣으로 보이며 방패·창,
   궁수의 실제 사격, 마법사·천사·사제의 서로 다른 주문 준비가 함께 읽힌다. 베일 군단은 우측에서
   불규칙한 혼성 돌격으로 다가오며, 좌측에는 하나의 고정 방어탑과 별도 기수의 긴 지휘 깃발만 둔다.
   이는 세계관 배경일 뿐 건설 노드·다중 전선·게임플레이 미니맵을 뜻하지 않는다. 사용자가 마지막
   첨부 이미지를 명시 승인했고, byte-exact copy는
   `assets/art/ui/title/omenward_title_wall_battle_surge_v1.png`이다.
2. `TITLE-WORDMARK-01`: 투명 알파의 `OMENWARD` 게임 제목. 사용자가 워드마크를 명시 승인했고,
   byte-exact copy는 `assets/art/ui/title/omenward_title_omenward_wordmark_v1.png`이다.

승인된 두 PNG의 SHA-256, source, consumer, provenance와 rights ceiling은
`docs/images/approved/OMENWARD_TITLE_ENTRY_ASSETS_V1.md`가 소유한다. 승인되지 않은 배경,
seal, preview screenshot과 candidate preview scene은 사용자 요청에 따라 제거했고, 식별 정보와
prompt archive만 `docs/images/candidates/OMENWARD_TITLE_ENTRY_CANDIDATES_2026-08-31.md`에 남긴다.

## Runtime composition

```text
Main
├── GameSession
└── UI
    ├── TitleScreen                 visible at boot
    │   ├── approved battle-surge backdrop TextureRect
    │   ├── approved transparent OMENWARD wordmark TextureRect + native role line
    │   ├── 원정 시작                only functional primary action
    │   └── bootstrap status label
    ├── RunCommandScreen            hidden at boot; visible after stage_started
    ├── StageHud                    retained hidden
    └── StageSelect                 retained hidden developer surface
```

한국어 역할 문구와 버튼은 native Godot `Label` / `Button`이 계속 소유한다. `OMENWARD` 워드마크는
승인된 투명 이미지지만 배경에 구워 넣지 않고 독립 `TextureRect`로 둔다. 따라서 이미지 교체와
로컬라이제이션 책임을 혼동하지 않으며, 타이틀 화면은 전장 삽화의 가시성을 유지한다.

## Acceptance criteria

- [x] Main boot does not schedule or begin `tutorial_stage` until the player presses `원정 시작`.
- [x] The title action is disabled while bootstrap is pending or failed.
- [x] A successful title action starts exactly `tutorial_stage` and reveals the existing Run Command screen.
- [x] The title scene contains no non-functional Continue, Save, Settings, Shop, or Record action.
- [x] Only the user-approved `TITLE-BG-06` and `TITLE-WORDMARK-01` are byte-exact runtime assets; the remaining candidates are deleted after provenance readback.
- [x] Locked art has a canonical record with SHA-256, prompt provenance, exact consumer, approval, and evidence ceiling.
- [x] Headless editor import, then the locked-art focused contract, full Godot/Python suites, and live technical capture were rerun on the locked working-tree state; the exact outputs are in `docs/qa/OMENWARD_TITLE_ENTRY_RUNTIME_SMOKE_2026-08-31.md`.
- [x] Focused headless title-route test, full headless suite, Python suite, Godot import, and a live technical capture pass before any machine-PASS statement. See `docs/qa/OMENWARD_TITLE_ENTRY_RUNTIME_SMOKE_2026-08-31.md`.

## Boundaries and rollback

- No save schema, unlock state, balance parameter, building rule, roulette rule, or single-front rule changes.
- No external addon, plugin, paid service, or new networking path.
- Rollback is limited to restoring automatic tutorial start and hiding/removing TitleScreen; no run save migration is required because none exists.
- Machine verification and technical runtime capture do not establish human readability, player UX, release rights, or release readiness.
