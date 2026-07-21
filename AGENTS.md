# Omenward 프로젝트 AI 작업 규칙

이 파일은 Omenward의 최상위 작업 계약이다. Base의 공용 원칙을 Omenward의 Godot 구조, 세계관, 승인 수치·자산, 검증 순서에 맞게 분화한다.

## Continuity

새 채팅·새 AI·새 작업자는 과거 대화 없이 저장소만으로 프로젝트 방향, 현재 상태, 다음 작업, 보호 범위, 책임 원본, Skill과 검증 방법을 찾을 수 있어야 한다.

- Active Context가 현재 상태의 기본 원본이다.
- Handoff는 경계 시점 스냅샷이며 두 번째 활성 상태 원본이 아니다.
- 같은 정보의 활성 복제본을 만들지 않는다.
- `[백업]`·`[보류]`는 이력·복구·재개 자료이며 기본 구현 기준이 아니다.

## Project

- Name: `OMENWARD / 오멘워드`
- Engine: Godot 4.7
- Genre: 싱글플레이 PvE 전략 오토배틀
- Core promise: 건물 구성·룰렛 확률 변화·공용 10병종 획득·독립 3라인 배치·거점/성문 공방의 결합
- Current stage: 플레이 가능한 수직 슬라이스의 운영체계·문서·검증 정합성 갱신
- DDD: `Digital Dopamine Design`

## Base

- Repository: `alsdmlals4-eng/Base`
- Pinned current main: `ee265576da7f67d3278f8099dd97d4e714ef0651`
- Version record: `[기획서]/00_프로젝트_허브/BASE_RULES_VERSION.md`
- Local adaptation:
  - `docs/base/OPERATING_MODEL.md`
  - `docs/base/WORK_MODE_AND_SKILL_ROUTING.md`
  - `docs/base/BASE_SYNC_AUDIT_2026-07-21.md`
  - `[기획서]/00_프로젝트_허브/AI_WORKFLOW.md`
  - `skills/foundation/`, `skills/specialists/`, `skills/disciplines/`

Base PR #18의 `d2457e75a856260d309203e20262f2a2142d2dd6` Productivity Manifest는 현재 Base main에 존재하지 않는다. Omenward에서는 삭제하지 않고 Registry의 `legacy_extensions`에 비정본 호환 기록으로만 보존한다.

## Priority

1. 최신 사용자 지시
2. 이 `AGENTS.md`
3. 보안·엔진·데이터·저장·승인 자산 규칙
4. Active Context와 승인된 Issue/직접 요청 계약
5. 등록된 책임 원본과 실제 파일·테스트
6. 로컬 Base 분화 문서와 Skill Registry
7. 고정 Base main
8. 과거 대화·백업·추정

## Default reading order

```text
AGENTS.md
→ BASE_RULES_VERSION.md
→ START_HERE.md·ACTIVE_CONTEXT.md·DOCUMENTATION_MAP.md
→ DEVELOPMENT_GATES.md·Roadmap
→ DESIGN_DOCUMENT_REGISTRY.json·현재 책임 원본
→ SKILL_REGISTRY.json·자동 선택된 최소 Skill/Skill Mode
→ 현재 Issue·Plan·PR
→ 실제 수정 대상·참조·테스트
```

`모두 확인`은 무차별 전체 로드를 뜻하지 않는다. Registry·정본·참조 지도를 사용하고, 백업·보류·제거 후보와 비선택 Skill은 필요할 때만 읽는다.

## Work Mode and automatic routing

- `PLAN`: 조사·분해·제안·승인 조건. 승인 전 구조·게임 경험·아트 방향·워크플로 변경 금지.
- `BUILD`: 승인 계약 범위의 최소 검증 가능한 변경.
- `REVIEW`: 계약·diff·정본·참조·실행·회귀·미검증 대조.

사용자가 Skill 이름을 선언하지 않아도 Registry trigger와 현재 단계로 자동 선택한다.

- 전체 Skill 자동 로드 금지
- 주 책임 분야 Skill 최대 1개
- Foundation Skill 최대 3개
- Specialist는 실제 trigger가 있을 때만 추가
- 사용한 Skill과 이유·결과·미검증을 보고
- Work Mode와 Skill 내부 mode를 혼용하지 않음

## Protected project contracts

- 공식 세계관·명칭, 전장 3라인 구조, 공용 10병종 데이터 계약
- 승인 전장 시안과 Asset Registry SHA-256
- `project.godot`의 960×540 논리 해상도, 1920×1080 기준, `viewport`, `keep`, integer scaling, nearest filter
- 게임 코드·Scene·Resource·데이터·저장 형식은 승인 계약 없이 변경 금지
- 정상 사용자 변경과 이력·보류·복구 경로 보존
- 범위 밖 리팩터링 금지

## Request-to-work

기능·경험·아트 방향·구조·워크플로 변경은 `managing-project-intake-and-work-contract`를 자동 선택한다.

```text
route
→ 저장소 사실 조사
→ 필요한 경우 clarify
→ 사용자 마지막 재진술 확인
→ contract
→ 필요 시 decompose-and-sequence
```

오탈자·명확한 단일 파일 기계 수정·같은 입력 검사 재실행은 예외다.

## Documents and publication

- 한 질문에는 Registry에 등록된 현행 Markdown 또는 JSON 책임 원본 하나만 둔다.
- 서술은 Markdown, 구조·상태·ID·경로·게임 데이터는 JSON.
- 본책은 원본·PDF·Publication Manifest를 같은 작업에서 갱신.
- PDF·DOCX·이미지·다이어그램은 독립 원본으로 수동 수정하지 않는다.
- 정본·경로·ID·Schema·생성기 변경은 `auditing-canonical-reference-freshness`를 포함한다.

## Validation

일반 변경은 `reviewing-and-validating-project-changes`를 사용한다.

```text
contract-check
→ 필요한 경우 external-source-review
→ reference-freshness
→ static-validation
→ Godot editor import
→ headless 6종
→ runtime smoke
→ 적용 시 accessibility/performance
→ regression
→ document publication·link·Registry
→ evidence-report
```

1920×1080·1280×720 사람 플레이/시각 QA를 실행하지 않았으면 `[미검증]`이다. 미실행 검사를 PASS로 기록하지 않는다.

## End of work

1. 책임 원본·코드·테스트·Roadmap을 동기화한다.
2. Active Context를 갱신하고 경계 시 Handoff를 만든다.
3. Skill·Documentation Map·Issue·Plan 연결을 확인한다.
4. 실패·중요 결정·재사용 교훈·검증 결과만 Learning Log에 남긴다.
5. 공용화 가치가 있으면 Base 제안과 구현 PR을 분리한다.
6. 새 작업자가 콜드 스타트 질문에 답할 수 있는지 검수한다.

## Required report

```md
## Work Mode / Skill Mode와 자동 선택 이유
## 변경 파일과 이유
## 유지한 기존 동작·결정·자산
## 구현·문서·발행 변경
## 검증 판정과 증거
## 미검증·위험·롤백
## Active Context·Roadmap·Skill 최신화
## Base 동기화·Legacy 상태
```
