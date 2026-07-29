# Base UX/UI 채택 기록

- Base repository: `alsdmlals4-eng/Base`
- Base main commit: `0fd95f4513343e77fd664af2763a01b02f52545b`
- Shared Skill: `auditing-and-refining-ui-art`
- Project source of truth: `docs/UX_UI_SYSTEM.md`
- Project Skill: `skills/disciplines/03-ux-ui-accessibility/SKILL.md`
- Adopted at: `2026-07-29`

## 적용 범위

- 위협→릴 설계→배치→전투→복기 UX
- 3라인 위험 우선순위·포커스·예상 결과·오류 복구
- 전투 결과 인과와 다음 설계 연결
- Godot UI와 위협·릴·배치·전투 상태 소유권 분리

## 검증 상태

- 문서·Skill·PR 검증: 실행
- 제품 코드·Scene·data·asset 변경: 없음
- Godot runtime/input: `NOT_RUN`
- Human understanding: `HUMAN_NOT_RUN`

공용 원리는 Base에 유지하고 실제 위협·릴·배치·전투 규칙과 런타임 결과는 Omenward에 유지한다.
