# OMENWARD 합성 테스터 적용 구조 분석

```yaml
analysis_id: OMENWARD-SYNTH-STRUCTURE-001
repository: alsdmlals4-eng/omenward
baseline_branch: main
baseline_commit: 5404fdc61c973696b6334d9726602e646f8749ac
work_mode: PLAN
execution_profile: PLANNING_ONLY_PROFILE
product_stage: PROTOTYPE_AND_VERTICAL_SLICE
validation_method: SYNTHETIC_TESTER_SIMULATION
evidence_tier: T6_AI_INFERENCE
base_governance_commit: 9c4071c5ecefe28769b512d426442338ceb7acdd
human_validation: NOT_RUN
vertical_slice_implementation: NOT_STARTED
implementation_authority: NONE
```

## 1. 분석 목적

룰렛 구조 설계→정지 결과→전선 커밋→자동전투 인과를 합성 페르소나로 공격하기 전에 OMENWARD의 분야별 Skill·문서 권한·Vertical Slice 게이트를 복원한다. 실제 사람 이해를 소유하는 Skill의 PASS 상태를 AI 추론으로 채우지 않는다.

## 2. 콜드 스타트 구조

```text
AGENTS.md
→ docs/DOCUMENTATION_MAP.md
→ 최신 Active/Current 상태 문서
→ APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT
→ Skill Registry
→ analytics-research
→ omenward-core-ux session contract
→ Evidence Pack·사람 검증 Artifact
→ 통합검수·적대적 검토
```

현재 권한은 전체 Vertical Slice의 기획·검증 준비이며 별도 Core PoC나 제품 Godot 구현을 승인하지 않는다.

## 3. Skill 책임

### selected_project_skills

| Skill | Mode | 책임·제한 |
|---|---|---|
| `discipline.analytics-research` | hypothesis / measurement / interpretation | 구조·RNG·커밋 인과의 가설과 편향을 분석. 실제 재미 판정 불가 |
| `discipline.omenward-core-ux` | session-contract input only | 실제 사람 관찰 질문·용어를 제공하지만 합성 결과로 `LOOP_PROVEN` 판정 금지 |
| `discipline.integration-validation` | contract / evidence review | Vertical Slice 정본·V2 상세 규칙·문서 상태 대조 |

### selected_base_skills

| Skill | Mode | 책임 |
|---|---|---|
| `governing-game-user-research-coverage` | `plan-evidence` | 사람·합성·runtime 증거 상태 분리 |
| `running-adversarial-review-and-refinement` | `attack` | 통제감 사후 합리화·fixed outcome 편향·영구 커밋 과부하 공격 |
| `reviewing-and-validating-project-changes` | `contract-check` / `evidence-report` | 제품 경로 비침범·정본·미검증 보고 |

## 4. canonical_sources

| 책임 | 경로 |
|---|---|
| 저장소 규칙 | `AGENTS.md` |
| 문서 지도 | `docs/DOCUMENTATION_MAP.md` |
| 최신 Vertical Slice | `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md` |
| 상세 V2 규칙 계보 | 관련 V2 결정·상세 문서 |
| 룰렛 Evidence Pack | `docs/benchmarks/OMENWARD_ROULETTE_AGENCY_EVIDENCE_PACK_2026-07-29.md` |
| 사람 검증 패킷 | `docs/superpowers/plans/2026-07-29-roulette-agency-validation-artifact.md` |
| 분석 Skill | `skills/disciplines/10-analytics-user-research/SKILL.md` |
| 실제 사람 UX Skill | `skills/disciplines/evaluating-omenward-core-ux-and-playtests/SKILL.md` |

## 5. protected_paths

```yaml
protected_paths:
  - Godot project files
  - scenes/**
  - scripts/**
  - resources/**
  - game data
  - docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md
  - detailed V2 rule authority
```

## 6. validation_routes

| 증거 | 상태 |
|---|---|
| 프로젝트 코어 문서 CI | 사용 가능 |
| 전체 Vertical Slice runtime | `NOT_STARTED` |
| 실제 RNG 분포 | `NOT_RUN` |
| 실제 사람 통제감·이해 | `NOT_RUN` |
| 합성 위험 검토 | `SYNTHETIC_RISK_REVIEW / T6_AI_INFERENCE` |

합성 결과에 `LOOP_PROVEN`, `PLAYTEST_PASSED`, `VERTICAL_SLICE_VALIDATED`를 사용하지 않는다.

## 7. 분석 대상

- 공세 브리핑.
- TokenSource와 3개 릴 구조.
- 비가역 가로 이동.
- fixed favorable / unfavorable-or-mixed 정지 결과.
- 출처 추적.
- 비가역 전선 커밋과 포기 비용.
- scripted 전투 인과와 다음 구조 수정.

## 8. 페르소나 렌즈

| ID | 공격 목적 |
|---|---|
| `ROGUELIKE_NOVICE` | TokenSource·릴·전선 용어 관계 오해 |
| `BUILDCRAFT_EXPERT` | 구조 최적화 깊이·정보 충분성 |
| `RESULTS_BIASED` | 좋은 결과는 실력, 나쁜 결과는 운으로 귀인 |
| `RNG_SKEPTIC` | 모든 결과를 운으로 축소 |
| `COMMIT_AVERSE` | 비가역 이동·배치의 후회 부담 |
| `OPTIMIZER` | 한 전선 몰빵·범용 구조 지배 전략 |
| `LOW_WORKING_MEMORY` | 3릴·출처·3전선·포기 비용 동시 부담 |

## 9. 산출물

```yaml
structure_analysis: COMPLETED
simulation_report: docs/research/OMENWARD_ROULETTE_AGENCY_SYNTHETIC_TESTER_REPORT_2026-07-29.md
result_state: SYNTHETIC_RISK_REVIEW
human_session_packet_changed: false
product_code_changed: false
canon_changed: false
human_validation: NOT_RUN
implementation_authority: NONE
```
