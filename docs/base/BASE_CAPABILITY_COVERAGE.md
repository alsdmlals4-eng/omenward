# Base 25개 Skill → Omenward 기능 보존표

기계 정본은 `docs/base/BASE_CAPABILITY_COVERAGE.json`이다.

| Base 책임군 | Omenward 현행 책임 |
|---|---|
| 요청·운영체계·문서·상태·검증·Base 제안 | Foundation 동등 Skill |
| 프로젝트 코어 판정·확정 | `foundation.project-core`의 권한 분리 mode |
| 적대적 검토 | `foundation.adversarial-review` |
| 가지치기·간소화·리팩토링 | 각각 독립 Foundation |
| GitHub 동기화·외부 AI worktree | `foundation.project-operating-system` mode |
| 장기 작업 checkpoint | `foundation.context-handoff` mode |
| 게임 컨셉·DDD·PoC·Vertical Slice | `discipline.game-design` 중심 mode |
| Games User Research 11영역 | `discipline.analytics-research` |
| 아트 프롬프트·기법 카드 | `discipline.art`·`discipline.technical-art` |
| UI 아트 감사 | `discipline.ux-ui-accessibility` |
| 학습 노트·대시보드 | `foundation.design-documents` mode |
| 엔진 런타임 진단 | `discipline.engineering`·`discipline.qa` |

Validator는 Base 25개 ID의 정확한 집합, 현행 Skill·mode 존재, Alias, 패키지 1:1을 검사한다.
