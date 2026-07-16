# 오멘워드 Documentation Map

이 문서는 새 작업자와 AI가 필요한 책임 원본만 읽도록 안내하는 라우터다. 모든 문서를 매번 읽지 않는다.

## 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ HANDOFF_CONTEXT.md
→ DOCUMENTATION_MAP.md
→ 현재 Codex 작업이면 work_orders 문서
→ OMENWARD_GAME_DESIGN.md
→ 관련 APPROVED 책임 문서
→ 시각 작업이면 docs/images/VISUAL_REFERENCE_INDEX.md
→ OMENWARD_ROADMAP.md
→ 현재 Issue / Goal / 승인 제안서
→ 실제 파일과 테스트
→ ACTIVE_CONTEXT.md
```

- `HANDOFF_CONTEXT.md`는 현재 방향과 다음 행동을 압축한 최초 인수인계 문서다.
- `docs/work_orders/`는 새 Codex 채팅에 전달하는 작업 요청·컨텍스트 패키지다.
- `docs/design/proposals/`는 기획 측 사전 기술 추천안이며 Codex가 실제 저장소를 조사해 제출하는 Plan Mode 결과와 구분한다.
- `APPROVED_*.md`는 세부 승인 규칙의 책임 원본이다.
- `docs/images/VISUAL_REFERENCE_INDEX.md`는 이미지의 승인·부분 참고·폐기 상태와 올바른 해석을 관리한다.
- 프로젝트 문서와 Base 공용 자료가 충돌하면 최신 사용자 지시와 프로젝트 책임 문서가 우선한다.
- 승인 구조, PoC 가설, 작업 요청, Plan Mode 제안서, 실제 구현, 검증 완료를 구분한다.

## 현재 Codex 시작 문서

| 작업 | 시작 문서 | 상태 |
|---|---|---|
| Issue #1 Phase 0 Bootstrap | `goals/0001-engine-selection-and-bootstrap.md` | 구현·검증 완료 |
| Issue #32 Vertical Slice Plan Mode | Issue #32, `goals/0002-core-vertical-slice.md` | 다음 Plan Mode 작업 |

현재 `design/proposals/0001-phase-0-godot-bootstrap.md`는 사전 기술 추천안이다. Codex는 이를 참고하되 실제 저장소와 공식 근거를 확인해 별도의 Plan Mode 제안서를 제출해야 한다.

## 항상 확인할 공식 문서

| 문서 | 역할 |
|---|---|
| `HANDOFF_CONTEXT.md` | 현재 방향, 불변 조건, 데이터 소유, 다음 실행 순서 |
| `OMENWARD_GAME_DESIGN.md` | 전체 게임 경험과 시스템 관계 |
| `ACTIVE_CONTEXT.md` | 최신 작업 상태 캡슐 |
| `OMENWARD_ROADMAP.md` | 단계별 개발 순서와 완료 기준 |
| `DECISIONS_PENDING.md` | 미확정·PoC 조정 항목 |
| `design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md` | 승인된 프리프로덕션 통합 인덱스 |
| `images/VISUAL_REFERENCE_INDEX.md` | 이미지 상태·우선순위·누락 감사 |
| `work_orders/0001-phase-0-codex-plan-mode.md` | 새 Codex 채팅 작업 요청·복사 프롬프트 |
| `design/proposals/0001-phase-0-godot-bootstrap.md` | Phase 0 사전 기술 추천안·검증 대상 |

## 조건부 라우팅

| 작업 조건 | 추가로 읽을 문서 |
|---|---|
| 새 Codex 채팅·Plan Mode 작업 요청 | 현재 `work_orders/*.md`, `PROPOSAL_WORKFLOW.md`, 현재 Issue/Goal |
| Codex가 작성한 구현 전 제안 검토 | Codex 제출 제안서, 관련 작업 요청서, 현재 Issue/Goal |
| Phase 0 Godot 부트스트랩 검토 | `work_orders/0001-phase-0-codex-plan-mode.md`, `design/proposals/0001-phase-0-godot-bootstrap.md`, Issue #1, Goal 0001 |
| 문서 추가·교체·정리·인수인계 | `DOCUMENT_LIFECYCLE.md`, `HANDOFF_CONTEXT.md`, `archive/README.md` |
| GitHub Issue·로컬 미러 동기화 | `issues/README.md`, `DOCUMENT_LIFECYCLE.md`, `tools/sync_repo.ps1` |
| 전장·성문·중간거점·접전지·암살자 우회로·카메라 | `design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`, `design/APPROVED_UI_ART_AUDIO_POC_BIBLE_V1.md`, `images/VISUAL_REFERENCE_INDEX.md` |
| 공용 병종 데이터·아군/적군 이미지 분리·UnitProfile | `design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md`, `design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md` |
| 적 웨이브·Threat·W1~20·보스 | `design/APPROVED_SHARED_ARCHETYPE_WAVE_1_20_POC_V1.md`, `design/APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md` |
| 병종 이동·공격·피격·사망·승리·전투 연출 | `design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md`, `design/APPROVED_ART_DIRECTION_AND_PRODUCTION_GUIDE_V1.md`, `design/APPROVED_UNIT_VISUAL_FORMAT_AND_REFERENCE_USE_V1.md` |
| 병종 월드 스프라이트 형식·등급별 외형 | `design/APPROVED_UNIT_VISUAL_FORMAT_AND_REFERENCE_USE_V1.md`, `images/VISUAL_REFERENCE_INDEX.md` |
| 아트 스타일·실루엣·팔레트·자산 제작 | `design/APPROVED_ART_DIRECTION_AND_PRODUCTION_GUIDE_V1.md`, `design/APPROVED_UNIT_VISUAL_FORMAT_AND_REFERENCE_USE_V1.md`, `design/APPROVED_UI_ART_AUDIO_POC_BIBLE_V1.md`, `images/VISUAL_REFERENCE_INDEX.md` |
| 새 이미지·도표·UI 시안 유입 | `images/README.md`, `images/VISUAL_REFERENCE_INDEX.md`, 관련 APPROVED 기획서 |
| 벨루·튜토리얼·HUD·대사 | `design/APPROVED_BELLU_MASCOT_AND_GUIDE_CONTRACT.md`, `design/APPROVED_BELLU_SINGLE_GUIDE_AND_FIRST_10_MINUTE_FLOW.md` |
| Dopamine Driven Design·첫 10분 | `design/APPROVED_DOPAMINE_DRIVEN_DESIGN_AND_FIRST_10_MINUTES.md` |
| 룰렛·등급·토큰 | `design/APPROVED_ROULETTE_CORE_RULES.md`, `design/APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md`, `design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md` |
| 기본 병영·특수병단·Tier 3 | `design/APPROVED_PLAYER_TEN_UNIT_LINEAGES_POC_V1.md`, `design/APPROVED_BARRACKS_AND_SPECIAL_CORPS_UNIT_TREE_V5.md`, `design/APPROVED_BARRACKS_TIER2_TIER3_INTEGRATED_TREE_V2.md` |
| 전투 계산·키워드·상태이상·비행 | `design/APPROVED_COMMON_COMBAT_AND_RANK_BUDGET_POC_V1.md`, `design/APPROVED_COMBAT_KEYWORDS_STATUS_EFFECTS_AND_FLIGHT.md` |
| 건설·경제·전문화·전술·용병 | `design/APPROVED_BUILDINGS_TACTICAL_MERCENARY_POC_V1.md`, `design/APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md` |
| 튜토리얼·캠페인·절차 생성 | `design/APPROVED_TUTORIAL_CAMPAIGN_PROCEDURAL_POC_V1.md`, `design/APPROVED_TUTORIAL_FIRST_FOUR_WAVES_BALANCE_V1.md` |
| Godot 프로젝트·Scene·Resource·상태 소유 | `GODOT_PROJECT_STRUCTURE.md`, `design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md` |
| 외부 저장소·Base 공용 지식 | `REFERENCE_REPOSITORIES.md`, `BASE_RULES_VERSION.md` |
| 외부 게임·시장·UX 벤치마킹 | `benchmarks/README.md`, 관련 제안서와 출처 스냅샷 |
| 작업 종료·인수인계 | `HANDOFF_CONTEXT.md`, `ACTIVE_CONTEXT.md`, Issue/PR 완료 형식 |

## 공식명 사용 규칙

신규 기획·UI·대사·데이터에는 다음 명칭만 사용한다.

```text
오멘워드 / OMENWARD
루메른 왕국
루미엔 영토
트리븐 전선
실베른 성채
베일런 황야
베일의 법칙
베일의 징조
벨루
베일종
```

레거시 명칭 `Roulettebound`, `율비`, `경계의 율`, `은종성채`, `무명야`는 과거 변경 이력 외에는 사용하지 않는다.

## 핵심 책임 원본

| 주제 | 책임 원본 |
|---|---|
| 작업 규칙·Plan Mode·완료 보고 | `AGENTS.md` |
| 프로젝트 인수인계 | `HANDOFF_CONTEXT.md` |
| 현재 Codex 작업 요청 | 현재 `work_orders/*.md` |
| 문서 생명주기 | `DOCUMENT_LIFECYCLE.md` |
| GitHub Issue 미러 | `issues/README.md` |
| 제안 형식·승인 기준 | `PROPOSAL_WORKFLOW.md` |
| Phase 0 사전 기술 추천 | `design/proposals/0001-phase-0-godot-bootstrap.md` |
| 전체 기획 | `OMENWARD_GAME_DESIGN.md` |
| 전장·성문·거점·우회로 | `design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md` |
| 공용 10병종 데이터·진영 이미지 | `design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md` |
| 병종 월드 스프라이트 형식 | `design/APPROVED_UNIT_VISUAL_FORMAT_AND_REFERENCE_USE_V1.md` |
| 시각자료 상태·해석 | `images/VISUAL_REFERENCE_INDEX.md` |
| W1~20 적 웨이브·보스 | `design/APPROVED_SHARED_ARCHETYPE_WAVE_1_20_POC_V1.md` |
| 병종 애니메이션·전투 연출 | `design/APPROVED_UNIT_ANIMATION_AND_BATTLE_PRESENTATION_GUIDE_V1.md` |
| 아트 방향·제작 규격 | `design/APPROVED_ART_DIRECTION_AND_PRODUCTION_GUIDE_V1.md` |
| 명칭·세계관 | `design/APPROVED_OMENWARD_WORLD_AND_NAMING.md` |
| 벨루 제작·안내 | `design/APPROVED_BELLU_MASCOT_AND_GUIDE_CONTRACT.md` |
| 첫 10분 | `design/APPROVED_BELLU_SINGLE_GUIDE_AND_FIRST_10_MINUTE_FLOW.md` |
| 개발 순서 | `OMENWARD_ROADMAP.md` |
| 미확정 | `DECISIONS_PENDING.md` |
| 기술·데이터·테스트 | `GODOT_PROJECT_STRUCTURE.md`, `design/APPROVED_PERFORMANCE_DATA_TEST_READINESS_POC_V1.md` |
| 현재 상태 | `ACTIVE_CONTEXT.md` |
| 구현 범위 | 최신 Issue/Goal, 작업 요청서와 사용자 승인된 Codex Plan Mode 제안서 |

## Base 공용 지식 라우팅

Base는 프로젝트 특화 사양이 아니라 작업 방법과 사례를 제공한다.

| 작업 | Base 참고 |
|---|---|
| 인수인계 컨텍스트 | `Base/docs/knowledge/methods/PROJECT_HANDOFF_CONTEXT_METHOD.md` |
| Codex Plan Mode 작업 패키지 | `Base/docs/knowledge/methods/CODEX_PLAN_MODE_WORK_PACKAGE_METHOD.md` |
| 아트 디렉션 | `Base/docs/knowledge/methods/ART_DIRECTION_METHOD.md` |
| 애니메이션·전투 연출 | `Base/docs/knowledge/methods/ANIMATION_AND_PRESENTATION_METHOD.md` |
| 조사·벤치마킹 | `Base/docs/knowledge/research/DESIGN_RESEARCH_AND_EVIDENCE_METHOD.md` |
| 실무 검수 | `Base/docs/knowledge/skills/` |
| 유사 결정 사례 | `Base/docs/knowledge/cases/` |

Base 방법은 오멘워드의 최신 승인 문서를 덮어쓸 수 없다.

다른 문서가 같은 내용을 반복하면 위 책임 원본을 링크하고 작업별 차이만 기록한다. 일반적인 이전 버전은 별도 활성 파일로 남기지 않고 Git 이력에서 확인한다.
