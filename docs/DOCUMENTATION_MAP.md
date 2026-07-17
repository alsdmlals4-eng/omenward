# 오멘워드 Documentation Map

- 갱신일: 2026-07-17
- 상태: **활성 문서 라우터**

이 문서는 새 작업자와 AI가 필요한 책임 원본만 읽도록 안내한다. 본문을 복제하지 않고 책임과 읽기 순서만 고정한다.

## 1. 최초 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ DOCUMENTATION_MAP.md
→ 작업 영향 분야의 5개 본책
→ 관련 APPROVED 상세 부록
→ 현재 Issue·Goal·Work Order
→ 실제 파일과 테스트
→ HANDOFF_CONTEXT·ACTIVE_CONTEXT
```

새 작업자는 다음 다섯 본책만으로 10분 안에 핵심 경험, 현재 구현 상태, 최신 시각 방향, 다음 단계, 금지 범위와 검증 방법을 설명할 수 있어야 한다.

## 2. 다섯 활성 본책

| 분야 | 활성 책임 원본 | 책임 범위 |
|---|---|---|
| 게임 기획 | [`planning/01_GAME_DESIGN.md`](planning/01_GAME_DESIGN.md) | 게임 약속, 규칙, 시나리오, UI/UX 행동, 밸런스 원칙 |
| 프로그래밍 | [`planning/02_PROGRAMMING_MVP_ROADMAP.md`](planning/02_PROGRAMMING_MVP_ROADMAP.md) | Godot 구조, Scene·데이터 책임, AI·전투·결정론·성능, MVP 로드맵 |
| 아트 | [`planning/03_ART_DIRECTION.md`](planning/03_ART_DIRECTION.md) | 캐릭터·전장·건물·UI 시각 언어, 애니메이션·VFX, 제작 규격, 최신 이미지 |
| 사운드 | [`planning/04_SOUND_DIRECTION.md`](planning/04_SOUND_DIRECTION.md) | BGM·SFX·벨루 음성, 이벤트 연결, 믹싱·접근성·제작 상태 |
| QA·PM | [`planning/05_QA_PM_PLAN.md`](planning/05_QA_PM_PLAN.md) | 자동·수동·시각·오디오·성능 QA, 버그, 일정·위험·예산, 릴리스 게이트 |

`HANDOFF_CONTEXT.md`와 `ACTIVE_CONTEXT.md`는 본책 내용을 복제하지 않고 현재 작업과 읽기 순서만 연결한다. `design/APPROVED_*.md`는 구체 수치와 데이터 계약을 보존하는 상세 부록이다.

## 3. 현재 작업·검증 라우팅

| 목적 | 문서 |
|---|---|
| 현재 main 감사·다음 개선 | `work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md` |
| 현재 시각자료와 승인 상태 | [`images/VISUAL_REFERENCE_INDEX.md`](images/VISUAL_REFERENCE_INDEX.md) |
| 미확정·PoC 조정 항목 | `DECISIONS_PENDING.md` |
| 실제 Godot 구조 | `GODOT_PROJECT_STRUCTURE.md`, 프로그래밍 본책 |
| 수직 슬라이스 검증 | `VERTICAL_SLICE_VALIDATION.md`, QA·PM 본책 |
| 테스트 실행 | `../tests/README.md`, `tools/validate_documentation.ps1` |
| 문서 생명주기 | `DOCUMENT_LIFECYCLE.md` |
| 제안·승인 형식 | `PROPOSAL_WORKFLOW.md` |
| GitHub Issue 미러 | `issues/README.md` — 동기화 도구 외 직접 편집 금지 |

## 4. 조건부 상세 부록

| 작업 조건 | 추가로 읽을 문서 |
|---|---|
| 전장·성문·거점·접전지·우회로 | `design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md` |
| 공용 병종·진영 Visual Set | `design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`, `design/APPROVED_UNIT_VISUAL_FORMAT_AND_REFERENCE_USE_V1.md` |
| W1~20·보스·공세 시간 | `design/APPROVED_SHARED_ARCHETYPE_WAVE_1_20_POC_V1.md`, `design/APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md` |
| 이동·공격·피격·사망·연출 | `design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md` |
| 벨루·튜토리얼·대사 | `design/APPROVED_BELLU_MASCOT_AND_GUIDE_CONTRACT.md`, `design/APPROVED_BELLU_SINGLE_GUIDE_AND_FIRST_10_MINUTE_FLOW.md` |
| 룰렛·등급·토큰 | `design/APPROVED_ROULETTE_CORE_RULES.md`, `design/APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md`, `design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md` |
| 병종 계보·건물 | `design/APPROVED_PLAYER_TEN_UNIT_LINEAGES_POC_V1.md`, `design/APPROVED_BARRACKS_AND_SPECIAL_CORPS_UNIT_TREE_V5.md`, `design/APPROVED_BUILDINGS_TACTICAL_MERCENARY_POC_V1.md` |
| 전투 계산·상태·비행 | `design/APPROVED_COMMON_COMBAT_AND_RANK_BUDGET_POC_V1.md`, `design/APPROVED_COMBAT_KEYWORDS_STATUS_EFFECTS_AND_FLIGHT.md` |
| 경제·비용 | `design/APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md` |
| 튜토리얼·캠페인 | `design/APPROVED_TUTORIAL_CAMPAIGN_PROCEDURAL_POC_V1.md`, `design/APPROVED_TUTORIAL_FIRST_FOUR_WAVES_BALANCE_V1.md` |
| 성능·데이터·테스트 | `design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md` |
| 이미지 유입·교체 | `images/README.md`, `images/VISUAL_REFERENCE_INDEX.md`, 아트·QA 본책 |

## 5. 승인 문서 책임 분류

모든 활성 `APPROVED_*.md`는 주 책임 분야를 정확히 하나만 가진다. 영향 분야는 협업·검토 대상을 뜻한다.

| 승인 부록 | 주 책임 | 영향 분야 |
|---|---|---|
| `APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md` | 게임 | 프로그래밍, 사운드, QA·PM |
| `APPROVED_BARRACKS_AND_SPECIAL_CORPS_UNIT_TREE_V5.md` | 게임 | 프로그래밍, 아트, QA·PM |
| `APPROVED_BARRACKS_TIER2_TIER3_INTEGRATED_TREE_V2.md` | 게임 | 프로그래밍, 아트, QA·PM |
| `APPROVED_BARRACKS_TIER3_EVOLUTION_AND_GRADE_SKILLS.md` | 게임 | 프로그래밍, 아트, QA·PM |
| `APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md` | 게임 | 프로그래밍, 아트, QA·PM |
| `APPROVED_BELLU_MASCOT_AND_GUIDE_CONTRACT.md` | 게임 | 아트, 사운드, 프로그래밍, QA·PM |
| `APPROVED_BELLU_SINGLE_GUIDE_AND_FIRST_10_MINUTE_FLOW.md` | 게임 | 프로그래밍, 아트, 사운드, QA·PM |
| `APPROVED_BENCHMARK_DECISIONS.md` | 게임 | QA·PM |
| `APPROVED_BUILDINGS_TACTICAL_MERCENARY_POC_V1.md` | 게임 | 프로그래밍, 아트, QA·PM |
| `APPROVED_BUILDING_SPECIALIZATION_AND_TACTICAL_COMMANDS.md` | 게임 | 프로그래밍, 아트, QA·PM |
| `APPROVED_COMBAT_KEYWORDS_STATUS_EFFECTS_AND_FLIGHT.md` | 게임 | 프로그래밍, 아트, QA·PM |
| `APPROVED_COMMON_COMBAT_AND_RANK_BUDGET_POC_V1.md` | 게임 | 프로그래밍, QA·PM |
| `APPROVED_DOPAMINE_DRIVEN_DESIGN_AND_FIRST_10_MINUTES.md` | 게임 | 프로그래밍, 아트, 사운드, QA·PM |
| `APPROVED_ENEMY_WARRIOR_LINEAGE_MILESTONES_V1.md` | 게임 | 프로그래밍, 아트, QA·PM |
| `APPROVED_OMENWARD_WORLD_AND_NAMING.md` | 게임 | 아트, 사운드, QA·PM |
| `APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md` | 프로그래밍 | QA·PM |
| `APPROVED_PLAYER_TEN_UNIT_LINEAGES_POC_V1.md` | 게임 | 프로그래밍, 아트, QA·PM |
| `APPROVED_PREPRODUCTION_POC_BASELINE_V1.md` | QA·PM | 게임, 프로그래밍, 아트, 사운드 |
| `APPROVED_PRIEST_HEAL_AND_COMMAND_SUPPORT_CLASS_V1.md` | 게임 | 프로그래밍, 아트, 사운드, QA·PM |
| `APPROVED_ROULETTE_CORE_RULES.md` | 게임 | 프로그래밍, 아트, 사운드, QA·PM |
| `APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md` | 게임 | 프로그래밍, QA·PM |
| `APPROVED_SHARED_ARCHETYPE_WAVE_1_20_POC_V1.md` | 게임 | 프로그래밍, 아트, 사운드, QA·PM |
| `APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md` | 프로그래밍 | 게임, 아트, QA·PM |
| `APPROVED_SPECIAL_CORPS_BUILDING_AND_GIANT_CLASS_V3.md` | 게임 | 프로그래밍, 아트, 사운드, QA·PM |
| `APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md` | 게임 | 프로그래밍, QA·PM |
| `APPROVED_TUTORIAL_CAMPAIGN_PROCEDURAL_POC_V1.md` | 게임 | 프로그래밍, 아트, 사운드, QA·PM |
| `APPROVED_TUTORIAL_FIRST_FOUR_WAVES_BALANCE_V1.md` | 게임 | 프로그래밍, QA·PM |
| `APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md` | 아트 | 게임, 프로그래밍, 사운드, QA·PM |
| `APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md` | 게임 | 프로그래밍, 아트, QA·PM |
| `APPROVED_UNIT_VISUAL_FORMAT_AND_REFERENCE_USE_V1.md` | 아트 | 게임, 프로그래밍, QA·PM |
| `APPROVED_WARRIOR_FAMILY_TIER2_ABILITIES.md` | 게임 | 프로그래밍, 아트, QA·PM |

`APPROVED_UI_ART_AUDIO_POC_BIBLE_V1.md`의 고유 내용은 게임·아트·사운드·QA 본책으로 분리됐다. 해당 경로에는 활성 본문이 아니라 대체 경로 안내만 남긴다.

## 6. 공식명·금지 범위

- 공식명은 **오멘워드/OMENWARD**, 안내 정령은 **벨루/Bellu**다.
- `율비/Yulbi`는 캐릭터 외형 참고 이미지 안의 폐기 표기다.
- 미니맵, 일반 유닛 라인 횡단, 적군 전용 전투 데이터 복제는 금지한다.
- 이미지 안 임시 문구·수치·맵 연결은 시스템 계약이 아니다.

## 7. Base 공용 지식

프로젝트는 `BASE_RULES_VERSION.md`가 고정한 Base 커밋을 따른다. Base는 작업 방법을 제공하며 오멘워드의 최신 승인 사양을 덮어쓰지 않는다.

| 작업 | Base 참고 |
|---|---|
| 인수인계 | `Base/docs/knowledge/methods/PROJECT_HANDOFF_CONTEXT_METHOD.md` |
| Plan Mode 작업 패키지 | `Base/docs/knowledge/methods/CODEX_PLAN_MODE_WORK_PACKAGE_METHOD.md` |
| 시각자료 유입·교체 | `Base/docs/knowledge/methods/VISUAL_REFERENCE_INTAKE_AND_SUPERSESSION_METHOD.md` |
| 아트·연출 | `Base/docs/knowledge/methods/ART_DIRECTION_METHOD.md`, `ANIMATION_AND_PRESENTATION_METHOD.md` |

다른 문서가 같은 내용을 반복하면 이 라우터와 해당 본책을 링크하고 작업별 차이만 기록한다. 이전 버전은 Git 이력에서 확인한다.
