# Omenward Skill System

이 디렉터리는 Base의 공용 작업 방법을 Omenward 책임 구조에 맞게 적용한 실행 패키지다.

## 시작

```bash
python tools/route_skills.py --request "PR의 누락과 중복을 적대적으로 검토해줘"
python -m unittest discover -s tests/python -v
```

## 활성 구조

- `SHARED_EXECUTION_CONTRACT.md`: 모든 Skill이 공유하는 우선순위·Work Mode·검증 계약
- `foundation/`: 활성 Foundation 7개
- `disciplines/`: 활성 Omenward 전용 Discipline 4개
- `specialists/`: 활성 canonical-freshness Specialist 1개
- `docs/base/SKILL_REGISTRY.json`: 유일한 기계 판독 라우팅 정본

활성 Discipline:

- `discipline.omenward-core-design`
- `discipline.omenward-godot`
- `discipline.omenward-core-ux`
- `discipline.omenward-art-assets`

과거 11개 Discipline과 5개 Specialist 패키지는 `inactive` 역사 자료로 유지한다. Router는 이 패키지를 직접 선택하지 않으며, 레거시 ID는 Registry의 `aliases`와 `replaced_by`로 활성 Skill에 해석한다.

## 최적화 원칙

- 공통 규칙은 한 번만 정의한다.
- 개별 Skill은 고유 책임·입력·절차·출력만 가진다.
- `routing.always_on`은 비워 두고 trigger와 stage로만 선택한다.
- 한 작업의 주 책임 Discipline은 하나이며 지원 Discipline은 최대 하나다.
- REVIEW는 `foundation.validation-review`와 `specialist.canonical-freshness`를 추가한다.
- 비활성 Skill, 중복 ID, 고아 패키지, 잘못된 alias·dependency와 과도한 자동 선택은 CI에서 실패한다.
