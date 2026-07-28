# 오멘워드 Documentation Map

- 갱신일: 2026-07-29
- 현재 정본 세대: `V2_CANON_CURRENT_BY_PR_57_MERGE`
- 현재 구현 상태: `V2_IMPLEMENTATION_NOT_STARTED`
- 제품 단계: `PROTOTYPE_AND_VERTICAL_SLICE`
- 현재 Work Mode: `PLAN`
- 실행 프로필: `PLANNING_ONLY_PROFILE`
- 직전 REVIEW: `COMPLETE`
- 다음 작업: `V6_PLANNING_INTAKE`
- 현재 제품 Issue: `#69`
- 제품 코드 승인: `NO`

이 문서는 작업별 책임 원본을 선택하는 라우터다. 모든 문서를 무조건 읽지 않고 현재 요청과 연결된 책임 원본만 확장한다.

## 1. 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ 이 Documentation Map
→ PROJECT_CORE.md
→ 통합 결정 원장
→ 통합 명세
→ CURRENT_IMPLEMENTATION_STATUS.md
→ HANDOFF_CONTEXT.md
→ v6 검수 완료·기획 전환 보고
→ 작업별 세부 APPROVED 책임 원본
→ 현재 Issue·Goal·Plan
→ 실제 파일과 테스트
→ ACTIVE_CONTEXT.md
```

## 2. 항상 확인할 책임 원본

| 문서 | 역할 |
|---|---|
| `PROJECT_CORE.md` | 제품 정체성, 플레이어 약속, 코어, 불변 조건, 게이트 |
| `design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md` | GM-01~GM-106 통합 결정과 대체 순위 |
| `design/APPROVED_CORE_V2_INTEGRATED_SPEC.md` | V2 시스템 관계와 승인 상태 |
| `CURRENT_IMPLEMENTATION_STATUS.md` | Legacy 실행 증거와 V2 미구현 경계 |
| `reviews/2026-07-27-v6-review-complete-planning-transition.md` | REVIEW 완료, v6 PLAN 전환, Coverage 감사 |
| `HANDOFF_CONTEXT.md` | 새 작업자용 현재 방향과 다음 행동 |
| `ACTIVE_CONTEXT.md` | 현재 Context Pack |
| `OMENWARD_ROADMAP.md` | 구현·검증 순서 |
| `DECISIONS_PENDING.md` | 아직 수치·콘텐츠로 남은 결정 |

## 3. 현재 R1+R2·v6 기획 입력

| 입력 | 역할 | 권한 |
|---|---|---|
| Issue `#69` | R1+R2 목표·가치·범위·제안서 기준 | `CODEX_PLAN_MODE_INPUT / BUILD_NOT_AUTHORIZED` |
| `reviews/2026-07-26-v2-r1-r2-planning-review.md` | baseline·권한·고정 결정·벤치마크 보정 | `HISTORICAL_REVIEW_AUTHORITY` |
| `reviews/2026-07-27-v2-construction-repair-same-timestamp-order-review.md` | F-30 기술 검수 | `MERGED_REVIEW_EVIDENCE` |
| `design/APPROVED_V2_CONSTRUCTION_REPAIR_SAME_TIMESTAMP_ORDER_2026-07-27.md` | F-30 최신 승인 순서 | `CURRENT_CANON_FOR_F30` |
| `benchmarks/OMENWARD_V2_BENCHMARK_REFRESH_2026-07-26.md` | V2 UX 채택·후속·제외 판정 | `PLANNING_INPUT` |
| `benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` | 룰렛 구조 설계·잔여 RNG·전선 커밋 인과의 CORE_POC 위험 가설 | `PILOT_RECOMMENDATION / NOT_CANON` |
| `superpowers/plans/2026-07-26-omenward-v2-r1-r2-roulette-foundation.md` | 구현 계획 초안 | `IMPLEMENTATION_READY_DRAFT / BUILD_NOT_AUTHORIZED` |
| `superpowers/plans/2026-07-24-omenward-core-v2-implementation.md` | 구형 전체 계획 | `HISTORICAL / REVALIDATION_REQUIRED` |

## 4. 현재 상태 순서

```text
R1+R2 기획 완료
→ 적대적 REVIEW 완료
→ F-30 정본화
→ 사용자 최신 지시로 v6 PLAN 계속
→ CORE_POC·Vertical Slice 기획 갱신
→ 사용자 기획 승인
→ 필요 시 Codex 읽기 전용 Plan Mode 인계
→ Codex 제안서
→ GPT 검수
→ 사용자 명시적 Build 승인
```

`REVIEW_COMPLETE`는 `FINAL_CODEX_HANDOFF_AUTHORIZED`나 `PRODUCT_CODE_AUTHORIZED`를 의미하지 않는다.

## 5. 현재 고정된 R1+R2 해석

- transient V2 runtime state는 `RefCounted`.
- token instance ID는 caller 주입.
- R1+R2에서 global ID generator 미도입.
- Legacy live spin 유지.
- V2 domain은 StageRun과 비연결.
- snapshot은 copy-out deep immutable.
- session은 이동·확정 없는 stopped-only seam.
- Codex 기준선은 실행 시점 최신 `origin/main`.
- 계획의 과거 SHA는 조사 이력으로만 사용.
- 설계 청사진·전선 브리핑·전투 인과 사슬은 후속 UX 패키지.
- F-30은 construction progress 후 repair settlement.

## 6. 다음 v6 기획 라우팅

| 작업 | 우선 책임 원본·모듈 |
|---|---|
| CORE_POC 위험 가설 | `PROJECT_CORE.md`, 통합 명세, 룰렛 통제감 Evidence Pilot, `analyzing-and-refining-game-concepts`, `identifying-project-core` |
| Vertical Slice 계약 | v6 `VERTICAL_SLICE_MODULE`, `designing-vertical-slices` |
| 플레이어 연구·벤치마크 | V2 benchmark refresh, 룰렛 통제감 Evidence Pilot, `governing-game-user-research-coverage` |
| UX 청사진·브리핑·인과 | `discipline.omenward-core-ux`, 실제 화면 역할 정의 |
| 마스코트·상징 동반자 | v6 `ASSET_AND_MASCOT_MODULE`, 세계관·UI·세일즈 역할 |
| 에셋·플러그인 | `evaluating-godot-assets-and-plugins-before-creation`, 라이선스 원장 |
| Codex Goal·인계 | 기획 승인 후 `CODEX_HANDOFF_MODULE`, Superpowers `writing-plans` |
| REVIEW | 영향 범위 지도 → 공격 → Finding 라우팅 → 회귀 |

## 7. 조건부 기술 라우팅

| 작업 | 추가 정본 |
|---|---|
| 룰렛·이동·snapshot·럭키·전설 | `design/APPROVED_ROULETTE_CORE_RULES.md`와 통합 원장 |
| MapRun·Stage·Wave·보관·식량·접전지 | `design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md` |
| 전술계획 건물 작업 | `design/APPROVED_V2_TACTICAL_PLANNING_BUILDING_WORK_CONSOLIDATED_2026-07-26.md`와 F-30 최신 정본 |
| 공용 병종·진영 Visual | `design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md` |
| 전투 계산·상태·비행 | 관련 `APPROVED_COMMON_COMBAT_*` 정본 |
| 아트·애니메이션 | 관련 `APPROVED_ART_*`, `APPROVED_UNIT_ANIMATION_*`, `images/VISUAL_REFERENCE_INDEX.md` |
| 기존 C1·C2·C3 증거 | `CURRENT_IMPLEMENTATION_STATUS.md`와 해당 run 증거 |
| Base 공용 Skill | `skills/BASE_SHARED_SKILL_ROUTES.json` → `skills/PROJECT_BASE_SKILL_ADAPTER.json` |
| 레거시·아카이브 | archive adapter·manifest |

## 8. 대체된 문서 해석

다음은 현재 제품 구현 근거가 아니라 Legacy 회귀·의사결정 이력으로만 사용한다.

- 독립 9칸과 Pre-V2 룰렛 확률.
- T-30/T-15/T-5 공세 구조.
- 공개 12% 럭키.
- 이동 되돌리기·확정 시 소비.
- 스테이지 전설 1회.
- 점령력 합산.
- 아군 주기적 3기 배치.
- 계열 고정 상위 등급 템플릿.
- 적 존재 시 성문 재건 정지.
- 재건 완료 HP 50%.

## 9. 상태 판정 규칙

```text
V2_SPEC_APPROVED
!= V2_IMPLEMENTED
!= V2_PROVEN
!= CORE_LOCK_V2

REVIEW_PHASE_COMPLETE
!= FINAL_CODEX_HANDOFF_AUTHORIZED
!= PRODUCT_CODE_AUTHORIZED

PLANNING_ONLY_PROFILE
!= CODEX_BUILD
```

최종 구현 상태는 `CURRENT_IMPLEMENTATION_STATUS.md`의 실제 실행 증거가 소유한다.