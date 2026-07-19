# Omenward 작업 규칙

작업 전에는 다음 순서로 읽습니다.

1. [`[기획서]/00_프로젝트_허브/START_HERE.md`]([기획서]/00_프로젝트_허브/START_HERE.md)
2. [`ACTIVE_CONTEXT.md`]([기획서]/00_프로젝트_허브/ACTIVE_CONTEXT.md)
3. [`DOCUMENTATION_MAP.md`]([기획서]/00_프로젝트_허브/DOCUMENTATION_MAP.md)
4. 영향 분야의 본책과 `skills/disciplines/`의 1:1 스킬
5. 실제 코드·Scene·데이터·테스트

Base 기준은 [`BASE_RULES_VERSION.md`]([기획서]/00_프로젝트_허브/BASE_RULES_VERSION.md)에 고정한다. 서술형 본책은 Markdown 책임 원본이고, Registry·Manifest·상태·ID·경로·게임 데이터는 JSON으로 관리한다. 각 본책의 PDF와 Publication Manifest는 항상 함께 갱신한다.

게임 코드, Scene, 데이터, 저장 형식은 별도 승인 없이 바꾸지 않는다. Issue #41에서 승인된 `project.godot`의 Godot 4.7 feature 메타데이터 변경만 예외이며, viewport·stretch·filter 계약은 회귀 테스트로 보호한다. Omenward 검증 순서는 Godot editor import → 기존 headless 6종 → runtime smoke → 문서 발행 검증이다. 사람 플레이 QA가 실행되지 않았다면 `[미검증]`으로 남긴다.

`[보류]`와 `[백업]`은 역사·재개 자료이며 기본 읽기와 구현 기준에서 제외한다. 새 작업자는 10분 안에 프로젝트 목적, 현재 단계, 다음 작업, 금지 범위, 11개 본책·스킬, 검증 경로를 찾아야 한다.
