# Omenward Skill System 시작점

1. `AGENTS.md`와 현재 책임 문서를 읽는다.
2. 요청을 Router에 넣는다.

```bash
python tools/route_skills.py --request "<사용자 요청>"
```

3. 출력된 Work Mode와 Skill 경로를 읽는다.
4. `skills/SHARED_EXECUTION_CONTRACT.md`를 따른다.
5. REVIEW에서는 Adversarial Review → Red Teaming → Critique–Refine → 독립 검증을 수행한다.
6. 작업 후 `python tools/validate_skill_system.py`와 관련 테스트를 실행한다.

기계 판독 정본은 `docs/base/SKILL_REGISTRY.json`이다.
