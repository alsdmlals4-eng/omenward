# Omenward Skill 시작점

```text
AGENTS.md
→ docs/BASE_RULES_VERSION.md
→ docs/base/SKILL_REGISTRY.json
→ skills/SHARED_EXECUTION_CONTRACT.md
→ tools/route_skills.py
→ 선택된 최소 Skill·mode
→ 프로젝트 책임 원본·실제 파일
→ tools/validate_skill_system.py
```

## 구조

- Foundation 12개
- Omenward Discipline 11개
- 별도 Specialist 0개
- Base 기능 coverage 25/25

전문 기능은 삭제되지 않았다. 게임 컨셉·Vertical Slice·연구 11영역·아트 프롬프트·UI 아트 감사·런타임 진단 등은 해당 Omenward 분야 Skill의 mode로 통합됐다.

## 구조 변경 순서

`가지치기 → Skill 본문 간소화 → 계약 보존 리팩토링 → 적대적 검토 → 실제 증거 검증 → 통합 PR 체크`

과거 ID는 `skills/LEGACY_SKILL_ALIASES.md`를 참고한다.
