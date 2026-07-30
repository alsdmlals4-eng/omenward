# Omenward Skill System 시작점

1. `AGENTS.md`와 현재 책임 문서를 읽는다.
2. Base v9.1 계약 검증기를 통과시킨다. 실패하면 route를 추측하지 않는다.
3. `.agents/skills/omenward-workflow-router/SKILL.md`에서 `skills/PROJECT_BASE_ADAPTER.json`과 `skills/PROJECT_SKILL_SNAPSHOT.json`만 읽어 route를 고른다.

```bash
python <Base checkout>/tools/check_project_operating_contract.py --project-root . --base-repository <Base checkout> --check
```

4. 선택된 Base 또는 Omenward 고유 Skill 경로를 읽는다.
5. REVIEW에서는 Adversarial Review → Red Teaming → Critique–Refine → 독립 검증을 수행한다.
6. 작업 후 계약 검증기와 관련 테스트를 실행한다.

`docs/base/SKILL_REGISTRY.json`은 v4 호환·이력 자료로만 보존하며 자동 라우팅 정본이 아니다.
