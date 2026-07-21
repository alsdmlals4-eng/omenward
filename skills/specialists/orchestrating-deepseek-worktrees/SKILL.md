---
name: orchestrating-deepseek-worktrees
description: Omenward에서 대량 초안·분류 작업을 격리된 외부 AI 작업 공간에 위임하고 결과를 회수한다.
---

# orchestrating-deepseek-worktrees

## Base source

- Source repository: `alsdmlals4-eng/Base`
- Pinned Base main: `ee265576da7f67d3278f8099dd97d4e714ef0651`
- Source skill: `Base:skills/orchestrating-deepseek-worktrees/SKILL.md`
- Installation: Base 공용 Skill을 그대로 복제한 파일이 아니라 Omenward의 경로·게이트·검증 계약에 맞춘 로컬 진입 어댑터다.

## Automatic routing

Trigger: `external-ai`, `large-draft`, `isolated-worktree`

**Use when:** 대량 초안·분류 작업을 격리된 외부 AI 작업 공간에 위임하고 결과를 회수한다.

**Do not use when:** 작은 작업, 외부 AI가 필요 없는 작업, 정본 브랜치에 직접 쓰게 하는 작업.

사용자가 Skill 이름을 선언하지 않아도 `SKILL_REGISTRY.json`의 trigger와 현재 단계에 따라 자동 선택한다. 전체 Skill을 한꺼번에 읽지 않으며 Foundation은 최대 3개, 주 책임 분야 Skill은 최대 1개를 기본으로 한다.

## Work Mode

- `PLAN`: 조사·분해·제안·승인 조건을 만든다. 승인되지 않은 구조·게임 경험·아트 방향 변경은 여기서 멈춘다.
- `BUILD`: 승인된 계약 범위만 수정하고 단계별 검증을 수행한다.
- `REVIEW`: diff·정본·참조·실행 증거·회귀·미검증을 대조한다.

Work Mode와 아래 Skill Mode를 혼용하지 않는다.

## Skill Modes

- `prepare-worktree`
- `delegate`
- `collect`
- `validate`
- `integrate`

## Omenward read order

1. `AGENTS.md`
2. `[기획서]/00_프로젝트_허브/START_HERE.md`
3. `ACTIVE_CONTEXT.md`, `DOCUMENTATION_MAP.md`, `DEVELOPMENT_GATES.md`
4. `DESIGN_DOCUMENT_REGISTRY.json`, `SKILL_REGISTRY.json`
5. 영향 분야 본책·등록 부록·실제 코드·데이터·자산·테스트
6. 현재 Issue·Plan·PR와 실행 증거

`[백업]`, `[보류]`, 제거 후보는 이력·복구·정리 작업이 아니면 기본 읽기에서 제외한다.

## Project contract

외부 결과는 Omenward 정본이 아니다. 별도 worktree/브랜치, 명시적 입력·출력·금지 경로를 사용하고 reviewing-and-validating-project-changes로 검증 후 통합한다.

- 기존 승인 결정·수치·자산·저장 형식과 정상 사용자 변경을 보존한다.
- 저장소에서 확인할 수 있는 사실을 사용자에게 되묻지 않는다.
- 실행하지 않은 검증은 `NOT_RUN` 또는 `[미검증]`으로 기록한다.
- 정본·경로·ID·Schema·생성기를 바꾸면 소비자·참조·테스트·파생본까지 추적한다.
- 결과·증거·남은 위험·롤백과 이 Skill을 선택한 이유를 보고한다.

## Output and evidence

```md
## Work Mode / Skill Mode
## 자동 선택 이유
## 확인한 정본과 보호 대상
## 변경 또는 제안
## 검증 증거
## 미검증·위험·롤백
## 갱신한 Context·Registry·Learning
```

## Learning and review

Learning Log: `skills/LEARNING_LOG.md`

다음이 발생했을 때만 본문 또는 Registry를 갱신한다.

- 반복 실패나 새 예외
- 책임·경로·검증·trigger 변경
- 오래된 ID·정본·파생본이 다시 선택됨
- 공용화 가능한 검증된 교훈
