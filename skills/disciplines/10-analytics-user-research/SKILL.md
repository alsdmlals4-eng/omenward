---
name: omenward-analytics-user-research
description: Omenward의 분석·유저리서치 책임 원본·구현·검증을 갱신할 때 자동 선택한다.
---

# 분석·유저리서치

## Automatic routing

Trigger: `research`, `benchmark`, `player-reaction`, `telemetry`, `funnel`, `experiment`

**Use when:** 벤치마킹·플레이어 반응·텔레메트리·퍼널·실험·사용자 연구를 설계하거나 해석할 때.

**Do not use when:** 출처 없이 기능을 복제하거나 이미 승인된 구현만 수행할 때.

이 Skill은 프로젝트 주 책임 분야 Skill이며 동시에 최대 1개를 기본 선택한다. 필요한 Foundation/Specialist Skill만 별도로 조합한다.

## Canonical source

- Responsibility source: `[기획서]/10_분석_유저리서치/10_분석_유저리서치_본책.md`
- Registry: `[기획서]/00_프로젝트_허브/DESIGN_DOCUMENT_REGISTRY.json`
- Routing: `[기획서]/00_프로젝트_허브/SKILL_REGISTRY.json`
- Learning: `skills/LEARNING_LOG.md`

등록 부록은 승인 근거와 세부 계약을 보존하지만 본책·Registry·실제 구현과 충돌하면 자동으로 현행 정본이 되지 않는다. 충돌은 `[확인 필요]`로 남긴다.

## Work contract

제품 사실·자기보고·행동 데이터·통제 실험·해석을 분리하고 ADOPT/ADAPT/AVOID/TEST/IGNORE로 판정한다.

1. 최신 사용자 지시와 승인 Issue/Plan을 확인한다.
2. 본책·관련 등록 부록·실제 파일·테스트를 대조한다.
3. 범위·보호 대상·수용 기준·검증·롤백을 명시한다.
4. 승인 범위만 BUILD하고 인접 분야 영향은 Registry로 라우팅한다.
5. 검증 결과와 미검증을 구분해 본책·Active Context·Learning Log를 갱신한다.

## Required review

- 정상 경로, 실패·경계·반례
- 기존 승인 결정·자산·저장·표시 계약 보존
- 정본·경로·ID·Schema·발행 전파
- 자동 테스트와 필요한 사람 검수의 분리
- 범위 밖 변경·추정 구현·보류 자료 활성화 여부

## Output

```md
## 분야와 자동 선택 이유
## 읽은 책임 원본·부록·실제 파일
## 변경·유지·확인 필요
## 검증 증거와 미검증
## 인접 분야·Context·Learning 갱신
```
