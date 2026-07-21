# Omenward Skill System

이 디렉터리는 Base의 공용 작업 방법을 Omenward 책임 구조에 맞게 적용한 실행 패키지다.

## 시작

```bash
python tools/route_skills.py --request "PR의 누락과 중복을 적대적으로 검토해줘"
python -m unittest discover -s tests/python -v
```

## 구조

- `SHARED_EXECUTION_CONTRACT.md`: 모든 Skill이 공유하는 우선순위·Work Mode·검증 계약
- `foundation/`: 모든 분야에 공통인 운영·문서·검증 능력 7개
- `disciplines/`: Omenward의 실제 책임 분야 11개
- `specialists/`: 특정 문제에만 켜지는 전문 Skill 6개
- `docs/base/SKILL_REGISTRY.json`: 유일한 기계 판독 라우팅 정본

## 최적화 원칙

- 공통 규칙은 한 번만 정의한다.
- 개별 Skill은 고유 책임·입력·절차·출력만 가진다.
- 한 작업의 주 책임 Discipline은 하나다.
- REVIEW는 항상 Adversarial Review, Red Teaming, Critique–Refine을 수행한다.
- Registry에 없는 Skill, 중복 ID, 고아 패키지, 과도한 자동 선택은 CI에서 실패한다.
