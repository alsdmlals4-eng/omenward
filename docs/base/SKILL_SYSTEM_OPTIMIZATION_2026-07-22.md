# Base 전면 반영·Skill 구조 최적화

## 결과

- Base 기준: `41a20584dd2ee51d917e5c9d7cab6838e1ceba7e`
- Base 활성 책임: 25
- 최적화 전 Omenward 패키지: 24
- 최적화 후 Omenward 패키지: 23
- Omenward 분야: 11 유지
- 별도 Specialist: 6 → 0
- Base 기능 coverage: 25/25

## 최적화 기준

1. 독립 입력·산출물·권한·검증 경계가 있으면 별도 Skill.
2. 프로젝트 분야가 이미 같은 책임 원본을 소유하면 mode로 통합.
3. 통합 전 고유 기능을 coverage와 Alias에 먼저 기록.
4. 삭제 뒤 Router·Validator·회귀·PR diff를 재검토.
5. 파일 수 감소보다 기능 보존과 발견성을 우선.

## Base 자체에서 발견한 주의점

Base 최신 `skills/SKILL_REGISTRY.json`과 `START_HERE.md`는 25개 Skill을 기록하지만 `AGENTS.md`와 `docs/OPERATING_MODEL.md`의 기존 통합 Skill 표는 13개 중심 설명을 일부 유지한다. Omenward는 Registry와 capability coverage를 기계 정본으로 사용하고 숫자를 한곳에서만 검증해 같은 drift를 방지한다.
