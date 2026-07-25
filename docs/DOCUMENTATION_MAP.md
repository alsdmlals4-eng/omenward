# 오멘워드 Documentation Map

- 갱신일: 2026-07-26
- 현재 정본 세대: `V2_CANON_CANDIDATE`
- 현재 Issue: `#56`

이 문서는 작업별 책임 원본을 선택하는 라우터다. 모든 문서를 매번 읽지 않는다.

## 1. 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ PROJECT_CORE.md
→ design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md
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
| `design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md` | 2026-07-25까지 사용자가 확정한 GM-01~GM-106 통합 결정, 충돌 문서 대체 순위 |
| `design/APPROVED_CORE_V2_INTEGRATED_SPEC.md` | V2 시스템 관계와 승인 상태 통합 |
| `design/APPROVED_ROULETTE_CORE_RULES.md` | 물리 릴, 토큰, 이동, snapshot, 판정, 럭키, 전설. 통합 결정 원장이 대체한 조항 제외 |
| `design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md` | MapRun, 시간, 웨이브, 보관·배치·식량, 접전지. 통합 결정 원장이 대체한 조항 제외 |
| `CURRENT_IMPLEMENTATION_STATUS.md` | legacy 구현 증거와 V2 미구현 경계 |
| `HANDOFF_CONTEXT.md` | 새 작업자용 현재 방향과 다음 행동 |
| `OMENWARD_GAME_DESIGN.md` | 세계관·경험·시스템 전체 설명 |
| `OMENWARD_ROADMAP.md` | 단계별 구현·검증 순서 |
| `DECISIONS_PENDING.md` | 아직 수치·콘텐츠로 남은 결정 |
| `ACTIVE_CONTEXT.md` | 최신 작업 상태 캡슐 |
| `BASE_SHARED_SKILL_INTEGRATION.md` | Base 공용 Skill route·어댑터와 공용/전용 Skill 경계 |

## 3. 조건부 라우팅

| 작업 | 추가 문서·Skill |
|---|---|
| 최신 통합 계약·충돌 해소 | `design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md` |
| 물리 릴·토큰·럭키·전설·금화 | `design/APPROVED_ROULETTE_CORE_RULES.md`와 최신 통합 결정 원장 |
| 준비·위험·웨이브·보관·식량·접전지·건설·수리·재건 | `design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`와 최신 통합 결정 원장 |
| 병종 출처·Tier 패시브·등급 액티브·AI 우선순위 | 최신 통합 결정 원장 |
| V2 구현 단계 | `superpowers/plans/2026-07-24-omenward-core-v2-implementation.md` |
| 공용 병종·진영 Visual | `design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md` |
| 전투 계산·상태·비행 | `design/APPROVED_COMMON_COMBAT_AND_RANK_BUDGET_POC_V1.md`, `design/APPROVED_COMBAT_KEYWORDS_STATUS_EFFECTS_AND_FLIGHT.md` |
| 아트·애니메이션 | 관련 `APPROVED_ART_*`, `APPROVED_UNIT_ANIMATION_*`, `images/VISUAL_REFERENCE_INDEX.md` |
| 기존 C1·C2·C3 증거 | `CURRENT_IMPLEMENTATION_STATUS.md`, C1/C2/C3 감사 보고서와 run |
| 문서 운영 | `DOCUMENT_LIFECYCLE.md` |
| Base 전체 운영 기준 | `BASE_RULES_VERSION.md`, `base/SKILL_REGISTRY.json` |
| Base 공용 Skill 자동 라우팅 | `../skills/BASE_SHARED_SKILL_ROUTES.json` → `../skills/PROJECT_BASE_SKILL_ADAPTER.json` |
| 레거시·아카이브·삭제 후보 | `governing-legacy-retention-and-archives` → `archive/ARCHIVE_RETENTION_ADAPTER.json`, `archive/MANIFEST.json` |
| Godot 기능·에셋·플러그인 직접 생성 전 조사 | `evaluating-godot-assets-and-plugins-before-creation` → `technical/ADOPTED_ASSETS.md`, `technical/THIRD_PARTY_LICENSES.md` |

## 4. Base 공용 Skill과 프로젝트 Skill 경계

```text
작업 요청
→ ../skills/BASE_SHARED_SKILL_ROUTES.json
→ Base 메인 SKILL_REGISTRY 자동 trigger 선택
→ ../skills/PROJECT_BASE_SKILL_ADAPTER.json으로 오멘워드 경로·정본·검증기 주입
→ 오멘워드 고유 전투·룰렛·성장 판단이 필요할 때만 프로젝트 Skill 선택
```

- Base 공용 Skill 본문을 프로젝트에 복사하지 않는다.
- 프로젝트 전용 Skill은 오멘워드의 전투 판정, 결정론적 결과, 룰렛, 성장과 데이터 계약처럼 다른 프로젝트에 직접 적용할 수 없는 책임만 소유한다.
- 제3자 자산 채택·라이선스는 `technical/ADOPTED_ASSETS.md`, `technical/THIRD_PARTY_LICENSES.md`에 기록한다.
- 아카이브는 `archive/README.md`, `archive/MANIFEST.json`이 비정본·복구 경계를 소유한다.

## 5. 대체된 문서 해석

다음 규칙을 설명하는 과거 문서는 기존 구현 증거, 과거 의사결정 추적 또는 마이그레이션 회귀 대상으로만 사용한다.

- 60초 공세와 T-30/T-15/T-5.
- 공개 12% 럭키.
- 이동 되돌리기와 확정 시 소비.
- 스테이지 전설 1회.
- 점령력 합산.
- 아군 주기적 3기 배치 묶음.
- 엘리트·영웅·전설의 계열 고정 템플릿.
- 적 존재 시 성문 재건 정지.
- 재건 완료 HP 50% 설정.

V2 제품 구현 근거로 사용하지 않는다. 충돌 시 최신 사용자 승인과 통합 결정 원장이 우선한다.

## 6. 상태 판정 규칙

```text
V2_SPEC_APPROVED
≠ V2_IMPLEMENTED
≠ V2_PROVEN
≠ CORE_LOCK_V2
```

`CURRENT_IMPLEMENTATION_STATUS.md`의 실행 증거가 최종 구현 상태를 소유한다.
