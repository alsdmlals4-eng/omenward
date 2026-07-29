# 오멘워드 Documentation Map

- 갱신일: 2026-07-29
- 현재 제품 단계: `PROTOTYPE_AND_VERTICAL_SLICE`
- 현재 Work Mode: `PLAN`
- 실행 프로필: `PLANNING_ONLY_PROFILE`
- 최신 설계 권한: `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 최신 구현 상태: `CURRENT_IMPLEMENTATION_STATUS.md`
- 제품 코드 승인: `NO`
- 최신 Vertical Slice 구현: `NOT_STARTED`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- 합성 위험 검토: `SYNTHETIC_RISK_REVIEW / T6_AI_INFERENCE`
- 별도 Core PoC: `SKIPPED_BY_USER_DECISION`

이 문서는 질문별 책임 원본을 선택하는 라우터다. 최신 사용자 지시와 현재 책임 원본을 우선하며, 모든 과거 V2 문서를 한꺼번에 활성 정본으로 취급하지 않는다.

## 1. 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ 이 Documentation Map
→ PROJECT_CORE.md
→ design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md
→ CURRENT_IMPLEMENTATION_STATUS.md
→ ACTIVE_CONTEXT.md
→ HANDOFF_CONTEXT.md
→ 현재 작업과 연결된 세부 승인 문서·Evidence Pilot·검증 Artifact
→ 실제 코드·데이터·테스트
```

## 2. 현재 활성 책임 원본

| 질문 | 책임 원본 | 권한 |
|---|---|---|
| 제품 정체성·플레이어 약속·불변 조건 | `PROJECT_CORE.md` | `CURRENT_CORE_AUTHORITY` |
| 전체 시스템 Vertical Slice 범위·관계 | `design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` | `CURRENT_USER_APPROVED_PLAN` |
| 최신 적대적 검토 | `reviews/ADVERSARIAL_VERTICAL_SLICE_REVIEW_2026-07-27.md` | `CURRENT_REVIEW_EVIDENCE` |
| 구현·Legacy·미검증 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 현재 작업 Context | `ACTIVE_CONTEXT.md` | `CURRENT_CONTEXT_PACK` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF` |
| 통합 게임 설명 | `OMENWARD_GAME_DESIGN.md` | `CURRENT_DESIGN_SUMMARY` |
| 후속 수치·콘텐츠 결정 | `DECISIONS_PENDING.md` | `PENDING_ONLY` |
| 구현·검증 순서 | `OMENWARD_ROADMAP.md` | `PLANNING_SEQUENCE` |
| 룰렛 통제감·인과 Pilot | `benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` | `PILOT_RECOMMENDATION / NOT_CANON` |
| 룰렛 통제감 사람 검증 Artifact | `superpowers/plans/2026-07-29-roulette-agency-validation-artifact.md` | `HUMAN_VALIDATION_INPUT / NOT_CANON` |
| 합성 테스터 적용 Skill·작업 구조 | `research/OMENWARD_SYNTHETIC_TESTER_STRUCTURE_ANALYSIS_2026-07-29.md` | `T6_AI_INFERENCE / NOT_CANON` |
| 룰렛 통제감 합성 위험 판정 | `research/OMENWARD_ROULETTE_AGENCY_SYNTHETIC_TESTER_REPORT_2026-07-29.md` | `SYNTHETIC_RISK_REVIEW / HUMAN_NOT_RUN` |

## 3. 룰렛 Evidence·사람·합성 경계

Evidence Pack은 구조 설계와 잔여 무작위성의 검증 가설을 소유한다. 사람 검증 Artifact는 실제 세션 카드·진행자 스크립트·관찰 기록을 소유한다. 합성 분석서는 현행 Skill·정본·보호 경로를 소유하고 합성 보고서는 T6 위험 가정·반례·수정 후보만 소유한다.

다음은 어느 Pilot 문서도 소유하지 않는다.

- 별도 CORE_POC.
- 제품 코드·Godot Scene·Resource·GDScript.
- 밸런스 수치·정확 확률·최종 병종.
- Vertical Slice 구현 완료 또는 사람 검증 통과.
- `CORE_LOCK`, `VERTICAL_SLICE_PROVEN`, `MVP_COMPLETE`, `LOOP_PROVEN` 판정.

## 4. 세부 규칙과 역사 계보

현재 Vertical Slice 계약이 전체 관계를 소유한다. 아래 문서는 충돌하지 않는 범위에서 세부 규칙·결정 계보·Legacy 회귀 근거로 읽는다.

| 영역 | 세부 원본·계보 |
|---|---|
| V2 통합 결정 계보 | `design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md` |
| 과거 V2 통합 명세 | `design/APPROVED_CORE_V2_INTEGRATED_SPEC.md` |
| 룰렛·이동·snapshot | `design/APPROVED_ROULETTE_CORE_RULES.md` |
| MapRun·Stage·Wave·거점 | `design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md` |
| 전설 배치 제한 | `design/APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md` |
| 전술계획 건물 작업 | `design/APPROVED_V2_TACTICAL_PLANNING_BUILDING_WORK_CONSOLIDATED_2026-07-26.md` |
| F-30 동일시각 처리 | `design/APPROVED_V2_CONSTRUCTION_REPAIR_SAME_TIMESTAMP_ORDER_2026-07-27.md` |
| Legacy C1·C2·C3 증거 | `CURRENT_IMPLEMENTATION_STATUS.md`와 실제 run·test 증거 |

충돌 우선순위:

```text
최신 사용자 지시
→ PROJECT_CORE.md
→ APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md
→ 세부 승인 문서
→ 과거 V2 계획·검토
→ Legacy 구현 증거
```

## 5. 상태 판정 규칙

```text
USER_APPROVED_PLAN
!= PRODUCT_CODE_AUTHORIZED
!= VERTICAL_SLICE_IMPLEMENTED
!= VERTICAL_SLICE_PROVEN
!= CORE_LOCK

PILOT_RECOMMENDATION
!= HUMAN_VALIDATION_INPUT
!= SYNTHETIC_RISK_REVIEW
!= 사람 검증 완료
!= NOT_CANON 해제
!= CODEX_BUILD 승인

SYNTHETIC_RISK_REVIEW
= T6_AI_INFERENCE
!= LOOP_PROVEN
!= 실제 RNG 체감
!= 실제 플레이어 이해
```

## 6. 다음 작업 라우팅

| 작업 | 먼저 읽을 책임 원본 |
|---|---|
| 룰렛 통제감·실패 귀인·전투 인과 | Evidence Pilot, 사람 검증 Artifact, 합성 보고서, 현재 Vertical Slice 계약 |
| 합성 위험 재검토 | 구조 분석서, 합성 보고서, `discipline.analytics-research`, 적대적 검토 |
| 저충실도 사람 세션 준비·관찰·판정 | 사람 검증 Artifact, Evidence Pilot, 현재 Vertical Slice 계약 |
| 전체 Vertical Slice 범위·시스템 연결 | 현재 Vertical Slice 계약, Project Core, Current Implementation Status |
| 밸런스·100,000 seed 시뮬레이션 | 세부 룰렛·경제 정본, 결정론 계약, 별도 검증 계획 |
| UI·접근성·정보 위계 | Evidence Pilot, 사람 검증 Artifact, 합성 보고서, `discipline.omenward-core-ux` |
| Codex 구현 인계 | 사용자 별도 Build 승인 후 최신 Plan과 실제 main 기준선 |
| REVIEW | 영향 범위 지도 → 공격 → Finding 판정 → 수정 → 회귀 재검사 |

최종 구현 상태와 검증 상태는 항상 `CURRENT_IMPLEMENTATION_STATUS.md`와 실제 실행 증거가 소유한다.
