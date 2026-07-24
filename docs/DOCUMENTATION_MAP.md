# 오멘워드 Documentation Map

- 갱신일: 2026-07-24
- 현재 정본 세대: `V2_CANON_CANDIDATE`
- 현재 Issue: `#56`

이 문서는 작업별 책임 원본을 선택하는 라우터다. 모든 문서를 매번 읽지 않는다.

## 1. 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ PROJECT_CORE.md
→ design/APPROVED_CORE_V2_INTEGRATED_SPEC.md
→ CURRENT_IMPLEMENTATION_STATUS.md
→ HANDOFF_CONTEXT.md
→ 작업별 세부 APPROVED 책임 원본
→ OMENWARD_GAME_DESIGN.md
→ OMENWARD_ROADMAP.md
→ 현재 Issue·PR·제안서
→ 실제 파일과 테스트
→ ACTIVE_CONTEXT.md
```

## 2. 항상 확인할 책임 원본

| 문서 | 역할 |
|---|---|
| `PROJECT_CORE.md` | 제품 정체성, 프로젝트 코어, 불변 조건, V2 검증 게이트 |
| `design/APPROVED_CORE_V2_INTEGRATED_SPEC.md` | V2 시스템 관계와 승인 상태 통합 |
| `design/APPROVED_ROULETTE_CORE_RULES.md` | 물리 릴, 토큰, 이동, snapshot, 판정, 럭키, 전설 |
| `design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md` | MapRun, 시간, 웨이브, 보관·배치·식량, 접전지 |
| `CURRENT_IMPLEMENTATION_STATUS.md` | legacy 구현 증거와 V2 미구현 경계 |
| `HANDOFF_CONTEXT.md` | 새 작업자용 현재 방향과 다음 행동 |
| `OMENWARD_GAME_DESIGN.md` | 세계관·경험·시스템 전체 설명 |
| `OMENWARD_ROADMAP.md` | 단계별 구현·검증 순서 |
| `DECISIONS_PENDING.md` | 아직 수치·콘텐츠로 남은 결정 |
| `ACTIVE_CONTEXT.md` | 최신 작업 상태 캡슐 |

## 3. 조건부 라우팅

| 작업 | 추가 문서 |
|---|---|
| 물리 릴·토큰·럭키·전설·금화 | `design/APPROVED_ROULETTE_CORE_RULES.md` |
| 준비·위험·웨이브·보관·식량·접전지 | `design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md` |
| V2 구현 단계 | `superpowers/plans/2026-07-24-omenward-core-v2-implementation.md` |
| 공용 병종·진영 Visual | `design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md` |
| 전투 계산·상태·비행 | `design/APPROVED_COMMON_COMBAT_AND_RANK_BUDGET_POC_V1.md`, `design/APPROVED_COMBAT_KEYWORDS_STATUS_EFFECTS_AND_FLIGHT.md` |
| 아트·애니메이션 | 관련 `APPROVED_ART_*`, `APPROVED_UNIT_ANIMATION_*`, `images/VISUAL_REFERENCE_INDEX.md` |
| 기존 C1·C2·C3 증거 | `CURRENT_IMPLEMENTATION_STATUS.md`, C1/C2/C3 감사 보고서와 run |
| 문서 운영 | `DOCUMENT_LIFECYCLE.md` |
| Base·Skill | `BASE_RULES_VERSION.md`, `base/SKILL_REGISTRY.json` |

## 4. 구형 문서 해석

기존 60초 공세, T-30/T-15/T-5, 공개 12% 럭키, 이동 되돌리기, 스테이지 전설 1회, 점령력 합산을 설명하는 문서는 다음 중 하나로만 사용한다.

- 기존 구현 증거.
- 과거 의사결정 추적.
- 마이그레이션 회귀 대상.

V2 제품 구현 근거로 사용하지 않는다. 충돌 시 최신 사용자 승인과 위 V2 책임 원본이 우선한다.

## 5. 상태 판정 규칙

```text
V2_SPEC_APPROVED
≠ V2_IMPLEMENTED
≠ V2_PROVEN
≠ CORE_LOCK_V2
```

`CURRENT_IMPLEMENTATION_STATUS.md`의 실행 증거가 최종 구현 상태를 소유한다.
