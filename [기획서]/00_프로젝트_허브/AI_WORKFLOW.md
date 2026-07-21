# Omenward AI·GitHub Workflow

## 1. Intent to evidence

```text
사용자 방향
→ managing-project-intake-and-work-contract
→ Definition of Ready
→ 필요 시 작업 분해·게임 컨셉 분석
→ 사용자 승인
→ BUILD
→ reviewing-and-validating-project-changes
→ 필요 시 canonical freshness·UI art·accessibility·performance
→ 책임 원본·발행·Active Context
→ PR checks·review
→ Learning Log·Base proposal
```

## 2. Request routing record

```yaml
request:
work_level: L0/L1/L2/L3/L4
work_mode: PLAN/BUILD/REVIEW
project_mode: existing/operational
primary_discipline:
affected_disciplines:
change_types:
required_design_document_ids:
foundation_skills:
specialist_skills:
discipline_skill:
deferred_skills:
asset_impact:
publication_impact:
routing_reason:
```

라우팅은 한 번 판정하고 실제 조건이 바뀔 때만 수정한다. 사용자가 Skill 이름을 고르도록 요구하지 않는다.

## 3. Plan contract

```yaml
problem:
user_or_player_value:
scope:
out_of_scope:
repository_findings:
protected_decisions_paths_assets:
files_to_change:
data_and_state_ownership:
asset_ui_audio_impact:
migration_and_compatibility:
canonical_sources_and_consumers:
known_renames_aliases_replacements:
external_evidence_questions:
playtest_and_telemetry:
execution_steps:
dependencies:
parallel_batches:
gates:
accessibility_scope:
performance_budget:
risks_and_fallbacks:
acceptance_criteria:
validation:
document_skill_publication_updates:
rollback:
```

각 단계는 `outcome / inputs / files / dependencies / output / acceptance / validation / rollback`을 가진다.

## 4. Execution gates

```text
Intake·Context
→ Definition of Ready
→ Planning·Approval·Sequencing
→ Implementation
→ Verification
→ Documentation·Publication
→ Integration·Completion
→ Context·Learning
```

### Definition of Ready

- 목적·가치·범위·제외·보호 대상
- 책임 분야·의존성·선행 조건
- 데이터·저장·자산·호환성 위험
- 관찰 가능한 완료 기준
- 자동·수동·사용자 검수
- 정본·Skill·발행 영향과 소비자

### Implementation

- 승인 Plan 범위만 변경
- 가장 작은 검증 가능한 단위
- 기능 추가와 대규모 리팩터링 분리
- 정상 사용자 변경·보류·승인 자산 보호
- 정본·경로·ID·Schema 변경 시 참조·소비자·파생본 동시 갱신

### Verification

```text
contract-check
→ external-source-review(적용 시)
→ reference-freshness
→ static-validation
→ runtime-validation
→ accessibility/performance(적용 시)
→ regression
→ publication/link/package integrity
→ evidence-report
```

## 5. PR checklist

- [ ] Base 고정 commit과 적용·비적용 표가 정확함
- [ ] Registry와 24개 Skill 경로가 1:1
- [ ] 자동 routing·Work Mode·실행 보고 계약이 테스트됨
- [ ] Legacy PR #18 정보가 현재 정본으로 노출되지 않음
- [ ] 게임 코드·Scene·데이터·자산이 범위 밖에서 바뀌지 않음
- [ ] Skill Map·본책 PDF·Manifest가 재생성 후 clean diff
- [ ] Python·링크·Schema·Godot·사람 QA 상태를 구분함
- [ ] Active Context·PR 설명·Learning Log가 실제 결과와 일치함
