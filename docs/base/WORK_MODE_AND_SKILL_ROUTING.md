# Work Mode and Skill Routing

## Automatic selection

`SKILL_REGISTRY.json`이 유일한 routing 원본이다.

```text
요청 의도·현재 단계
→ Work Mode
→ trigger match
→ Foundation 최소 세트
→ 주 책임 분야 1개
→ 필요 시 Specialist
→ 실행 보고
```

사용자 Skill 선언은 필요하지 않다.

## Selection constraints

- `load_all_skills=false`
- `default_selection=automatic-trigger-match`
- `automatic_selection=true`
- `require_trigger_match=true`
- `require_execution_report=true`
- `max_primary_discipline_skills=1`
- `max_foundation_skills=3`
- HOLD/BACKUP/REMOVAL_CANDIDATE 제외

## Typical routes

| 요청 | Work Mode | Skill |
|---|---|---|
| 새 기능·다분야 변경 | PLAN | intake → 분야 Skill → validation |
| Base/문서 구조 갱신 | PLAN/BUILD/REVIEW | operating-system → freshness → integration |
| 게임 컨셉·PoC | PLAN | concept analysis → game design/analytics |
| 수직 슬라이스 품질 | PLAN/BUILD/REVIEW | vertical slice → 관련 분야 → validation |
| UI 결과 개선 | REVIEW→BUILD | UI art audit → UX/Art → validation |
| PR 최종 검수 | REVIEW | validation → freshness → integration |
| Handoff | REVIEW | context-and-handoff |

## Execution report

모든 L1 이상 작업은 선택 이유, 수행 내용, 결과·증거, 미검증, Context·Learning 갱신을 기록한다. 템플릿은 프로젝트 허브의 `SKILL_EXECUTION_REPORT.md`다.
