# 오멘워드 Documentation Map

이 문서는 Codex와 공동 작업자가 현재 작업에 필요한 문서만 읽도록 안내하는 라우터다. 모든 문서를 매번 읽지 않는다.

## 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ DOCUMENTATION_MAP.md
→ PROPOSAL_WORKFLOW.md
→ OMENWARD_GAME_DESIGN.md
→ 관련 APPROVED 문서
→ 현재 Issue/Goal
→ 대상 파일
→ ACTIVE_CONTEXT.md
```

승인된 `docs/design/APPROVED_*.md`가 메인 기획서와 충돌하면 더 최근 승인 문서를 우선한다.

## 항상 확인할 공식 문서

- 게임 전체: `OMENWARD_GAME_DESIGN.md`
- 현재 상태: `ACTIVE_CONTEXT.md`
- 개발 순서: `OMENWARD_ROADMAP.md`
- 미확정 항목: `DECISIONS_PENDING.md`
- 공식 명칭·세계관: `design/APPROVED_OMENWARD_WORLD_AND_NAMING.md`

## 조건부 라우팅

| 작업 조건 | 추가로 읽을 문서 |
|---|---|
| Codex Plan Mode 또는 구현 전 제안 | `PROPOSAL_WORKFLOW.md`, 현재 Issue/Goal |
| 프리프로덕션 기획 프리즈 | `design/DESIGN_FREEZE_CHECKLIST.md`, `DECISIONS_PENDING.md` |
| 벨루·튜토리얼·HUD·대사 | `design/APPROVED_BELLU_MASCOT_AND_GUIDE_CONTRACT.md`, `design/APPROVED_BELLU_SINGLE_GUIDE_AND_FIRST_10_MINUTE_FLOW.md` |
| Dopamine Driven Design·첫 10분 | `design/APPROVED_DOPAMINE_DRIVEN_DESIGN_AND_FIRST_10_MINUTES.md` |
| 룰렛·등급·토큰 | `design/APPROVED_ROULETTE_CORE_RULES.md`, `design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md` |
| 병영 Tier·세부 병종·공유 토큰 | `design/APPROVED_BARRACKS_TIER3_EVOLUTION_AND_GRADE_SKILLS.md` |
| 전사 Tier 2 능력 | `design/APPROVED_WARRIOR_FAMILY_TIER2_ABILITIES.md` |
| 전투 키워드·상태이상·비행 | `design/APPROVED_COMBAT_KEYWORDS_STATUS_EFFECTS_AND_FLIGHT.md` |
| 건설·전문화·전술 명령·보스 | `design/APPROVED_BUILDING_SPECIALIZATION_AND_TACTICAL_COMMANDS.md`, 관련 proposals 0005~0007 |
| Godot 프로젝트·Scene·데이터 | `GODOT_PROJECT_STRUCTURE.md` |
| 외부 저장소 참고 | `REFERENCE_REPOSITORIES.md` |
| 외부 게임·시장·UX 벤치마킹 | `benchmarks/README.md`, 관련 제안서와 출처 스냅샷 |
| 작업 종료·인수인계 | `ACTIVE_CONTEXT.md`, Issue/PR 완료 형식 |

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

레거시 명칭 `Roulettebound`, `율비`, `경계의 율`, `은종성채`, `무명야`는 과거 링크 호환과 변경 이력 외에는 사용하지 않는다.

## 책임 원본

- 작업 규칙·Plan Mode·완료 보고: `AGENTS.md`
- 제안 형식과 승인 기준: `PROPOSAL_WORKFLOW.md`
- 전체 기획: `OMENWARD_GAME_DESIGN.md`
- 명칭·세계관: `design/APPROVED_OMENWARD_WORLD_AND_NAMING.md`
- 벨루 제작·안내: `design/APPROVED_BELLU_MASCOT_AND_GUIDE_CONTRACT.md`
- 첫 10분: `design/APPROVED_BELLU_SINGLE_GUIDE_AND_FIRST_10_MINUTE_FLOW.md`
- 개발 순서: `OMENWARD_ROADMAP.md`
- 미확정: `DECISIONS_PENDING.md`
- 현재 상태: `ACTIVE_CONTEXT.md`
- 구현 범위와 완료 기준: 최신 Issue/Goal과 승인 제안서

다른 문서가 같은 내용을 반복하면 위 책임 원본을 링크하고 작업별 차이만 기록한다.
