# Omenward Work Mode·Skill·mode 라우팅

## 단계

- `PLAN`: 사실·정본·범위·코어·순서
- `BUILD`: 승인된 반영·이주·가지치기·리팩토링
- `REVIEW`: 적대적 공격·비판 검증·정적·런타임·회귀·PR 판정

`tools/route_skills.py`는 요청을 단일 고정 mode가 아니라 필요한 단계 순서로 라우팅한다.

## 최소 선택

- 첫 단계: `foundation.project-intake`
- 주 분야: 최대 1개
- 지원 분야: 최대 2개
- Foundation: 단계별 trigger 일치 항목만 선택
- REVIEW 강제:
  - `foundation.adversarial-review`
  - `foundation.validation-review`
  - `discipline.integration-review`

## 통합 원칙

별도 Specialist를 기본 구조로 유지하지 않는다. 전문 기능은 독립 입력·산출물·권한·검증이 보존되는 범위에서 분야 Skill의 mode로 통합한다.

예:

```text
게임 컨셉·DDD·PoC → discipline.game-design
11영역 연구 → discipline.analytics-research
아트 프롬프트 → discipline.art + discipline.technical-art
UI 아트 감사 → discipline.ux-ui-accessibility
Vertical Slice → game-design + production-pm + engineering
런타임 오류 → engineering + qa
정본 최신성 → foundation.validation-review: reference-freshness
DeepSeek worktree → foundation.project-operating-system: external-ai-worktree
```

## 수동 지정

현행 ID 또는 `skills/LEGACY_SKILL_ALIASES.json`의 과거 ID만 허용한다. Alias는 현행 ID와 mode로 변환되며 고아 패키지를 다시 활성화하지 않는다.
