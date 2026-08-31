# Omen Warden Title Entry Design

```yaml
decision_id: OMW-PLAN-20260831-OMEN-WARDEN-TITLE-ENTRY-01
approved_at: 2026-08-31 KST
approval_source: USER_CHAT__"승인,진행해"
status: IMPLEMENTED__MACHINE_VERIFIED__HERA_TECHNICAL_SMOKE_PASS__TITLE_ASSET_LOCK_PENDING
scope: TITLE_ENTRY / BOOT_TO_TUTORIAL_ROUTE / TITLE_RUNTIME_ASSET_CANDIDATES
authority_domain: REPOSITORY_STRUCTURED_CANON
publication_policy: source_only
runtime_evidence: HERA_TECHNICAL_SMOKE_PASS
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
TITLE_COMPOSITION = WARD_CITADEL_LEFT + QUIET_CENTER_TEXT_SAFE_AREA + DISTANT_VEIL_RIGHT
BAKED_TEXT_IN_GENERATED_IMAGE = FORBIDDEN
BATTLEFIELD_BUILDINGS_OR_CONSTRUCTION_NODES = FORBIDDEN
```

두 후보를 만든다.

1. `TITLE-BG-01`: 16:9 수채화 메인 배경. 수호 성채·깃발·먼 장막 균열은 보이되, 중앙은
   실제 UI 텍스트와 버튼을 위한 깨끗한 여백으로 남긴다.
2. `TITLE-SEAL-01`: 글자 없는 정사각 수호 문장. 타이틀 옆 장식으로만 쓰며, 능력·재화·점령
   오브젝트로 읽히게 만들지 않는다.

두 파일은 생성 직후 `GENERATED_CANDIDATE`다. 사용자가 화면에서 본 후보를 `LOCK`할 때만
repository의 `assets/art/ui/title/` runtime path, SHA-256, consumer, provenance record에
올리고 TitleScreen에 연결한다. 후보 거절 시 해당 후보만 제거하고 기존 전장 자산은 보존한다.

## Runtime composition

```text
Main
├── GameSession
└── UI
    ├── TitleScreen                 visible at boot
    │   ├── candidate/approved backdrop area
    │   ├── Omenward title + role line (Godot Label)
    │   ├── 원정 시작                only functional primary action
    │   └── bootstrap status label
    ├── RunCommandScreen            hidden at boot; visible after stage_started
    ├── StageHud                    retained hidden
    └── StageSelect                 retained hidden developer surface
```

The English wordmark and Korean copy remain native Godot `Label` text, not
pixels inside generated art. This preserves readable scaling and later localization.

## Acceptance criteria

- [x] Main boot does not schedule or begin `tutorial_stage` until the player presses `원정 시작`.
- [x] The title action is disabled while bootstrap is pending or failed.
- [x] A successful title action starts exactly `tutorial_stage` and reveals the existing Run Command screen.
- [x] The title scene contains no non-functional Continue, Save, Settings, Shop, or Record action.
- [x] The candidate background and seal remain non-runtime candidates until the user visually locks them.
- [ ] Locked art, once promoted, has a manifest record with SHA-256, prompt provenance, exact consumer, and state.
- [x] Focused headless title-route test, full headless suite, Python suite, Godot import, and a live technical capture pass before any machine-PASS statement. See `docs/qa/OMENWARD_TITLE_ENTRY_RUNTIME_SMOKE_2026-08-31.md`.

## Boundaries and rollback

- No save schema, unlock state, balance parameter, building rule, roulette rule, or single-front rule changes.
- No external addon, plugin, paid service, or new networking path.
- Rollback is limited to restoring automatic tutorial start and hiding/removing TitleScreen; no run save migration is required because none exists.
- Machine verification and technical runtime capture do not establish human readability, player UX, release rights, or release readiness.
