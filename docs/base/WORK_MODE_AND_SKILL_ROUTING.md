# Work Mode·Skill 라우팅

## 기본 흐름

```text
사용자 요청
→ project-intake
→ PLAN / BUILD / REVIEW 판정
→ 주 책임 Discipline 1개
→ 지원 Discipline 최대 2개
→ 명시적으로 필요한 Specialist
→ 실행
→ Adversarial Review
→ Red Teaming
→ Critique–Refine
→ 독립 검증
```

## REVIEW 강제 스택

REVIEW에서는 다음 두 Skill을 제거할 수 없다.

- `foundation.validation-review`
- `discipline.integration-review`

## 충돌 해결

- 게임 규칙: `discipline.game-design`
- 코드·상태 소유: `discipline.engineering`
- 정보 계층·조작: `discipline.ux-ui-accessibility`
- 시각 언어: `discipline.art`
- 테스트 판정: `discipline.qa`
- 최종 병합 판정: `discipline.integration-review`

지원 Skill은 주 책임자의 파일을 직접 소유하지 않는다. 충돌 시 책임 원본을 먼저 확인하고, 해결되지 않으면 `확인 필요`로 중단한다.
