---
name: omenward-technical-art-pipeline
description: Omenward의 테크니컬 아트·콘텐츠 파이프라인 책임 원본·구현·검증을 갱신할 때 자동 선택한다.
---

# 테크니컬 아트·콘텐츠 파이프라인

## Automatic routing

Trigger: `technical-art`, `import`, `animation`, `pipeline`, `asset-build`

**Use when:** 자산 import·애니메이션·스프라이트 규격·빌드 파이프라인·콘텐츠 생산 계약을 변경할 때.

**Do not use when:** 서사·수치만 변경되고 자산 파이프라인에 영향이 없을 때.

이 Skill은 프로젝트 주 책임 분야 Skill이며 동시에 최대 1개를 기본 선택한다. 필요한 Foundation/Specialist Skill만 별도로 조합한다.

## Canonical source

- Responsibility source: `[기획서]/05_테크니컬아트_콘텐츠_파이프라인/05_테크니컬아트_콘텐츠_파이프라인_본책.md`
- Registry: `[기획서]/00_프로젝트_허브/DESIGN_DOCUMENT_REGISTRY.json`
- Routing: `[기획서]/00_프로젝트_허브/SKILL_REGISTRY.json`
- Learning: `skills/LEARNING_LOG.md`

등록 부록은 승인 근거와 세부 계약을 보존하지만 본책·Registry·실제 구현과 충돌하면 자동으로 현행 정본이 되지 않는다. 충돌은 `[확인 필요]`로 남긴다.

## Work contract

Godot 생성 .import는 추적하지 않고 승인 원본·파생본·해시·재생성 경로를 구분한다.

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
