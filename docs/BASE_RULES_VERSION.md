# Base 규칙·공용 지식 버전

- 원본 저장소: `alsdmlals4-eng/Base`
- Base v9.1 release pin: `3c158f52cfdad889970aef4d6ce6650a6fea0645`
- Base v9.1 evidence pin: `dd20ad3852e264d7e337e34d2cb963f71053a6cb`
- 적용 방식: 프로젝트 정본 우선, Base 공용 원칙의 명시적 채택, 자동 덮어쓰기 금지
- 프로젝트 고유 Skill 정본: `skills/SKILL_REGISTRY.json`
- Base·프로젝트 route 계약: `skills/PROJECT_BASE_ADAPTER.json`
- 생성 route view: `skills/PROJECT_SKILL_SNAPSHOT.json`
- Router: `.agents/skills/omenward-workflow-router/SKILL.md`
- 공통 실행 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 채택한 Base 영역

- spec-first PLAN / BUILD / REVIEW 게이트
- 프로젝트 코어 식별·보호
- 적대적 검토와 검증 증거 분리
- Skill 본문 단순화와 책임 중복 제거
- 구형·비기능 자료의 명시적 정리
- 원문 보존과 현재 권한 격리를 분리하는 archive governance
- 계약 보존 리팩터링
- 프로젝트 컨텍스트와 인수인계 압축
- 정본 최신성·참조 무결성 검사

## 프로젝트 우선순위

```text
최신 사용자 지시
→ AGENTS.md
→ docs/BASE_RULES_VERSION.md
→ docs/DOCUMENTATION_MAP.md
→ 현재 Work Order
→ 프로젝트 승인 책임 문서
→ 현재 Issue·Goal
→ 실제 파일과 테스트
→ skills/PROJECT_BASE_ADAPTER.json과 PROJECT_SKILL_SNAPSHOT.json
→ 선택된 Base shared 또는 Omenward local Skill
→ 이 문서가 고정한 Base 커밋
→ Base 최신 공용 지식과 외부 참고
```

Base 원격 변경은 자동 적용하지 않는다. 새 Base 커밋을 채택할 때는 프로젝트 정본·Registry·Router·Validator·문서 참조를 같은 변경 묶음으로 검증한다.

## Legacy Skill System v4 (compatibility only)

- 로컬 활성 Foundation: 7
- 활성 Omenward Discipline: 4
- 활성 Specialist: 1
- 로컬 활성 합계: 12
- Base 공용 Skill: adapter-only route이며 로컬 활성 개수에 포함하지 않음
- 레거시 패키지: 16개를 `inactive`와 `replaced_by`로 등록
- 과거 Skill ID와 PR 표기는 `aliases`로 활성 Skill에 해석
- `always_on` Skill 없음
- REVIEW 단계에서만 `foundation.validation-review`와 `specialist.canonical-freshness`를 추가
- 주 Discipline 최대 1개, 지원 Discipline 최대 1개

구형 Skill 파일은 과거 기록 보존용으로만 존재하며 Router가 선택하지 않는다. 새 기획서·Issue·PR·Work Order는 활성 ID만 사용한다.

## Omenward 전용 활성 Discipline

- `discipline.omenward-core-design`: 핵심 루프·규칙·데이터 계약
- `discipline.omenward-godot`: Godot·GDScript·결정론·공유 데이터 검증
- `discipline.omenward-core-ux`: 10~15분 플레이테스트·HUD·해상도 가독성
- `discipline.omenward-art-assets`: 아트·애니메이션·판정 연출·에셋 파이프라인

## Archive governance 채택

- Base Skill: `governing-legacy-retention-and-archives`
- 프로젝트 어댑터: `docs/archive/ARCHIVE_RETENTION_ADAPTER.json`
- Manifest: `docs/archive/MANIFEST.json`
- 기존 구형 자료 일괄 이동·삭제·본문 비우기: `NOT_IN_THIS_ADOPTION`
- branch/tag 삭제: `NOT_RUN`

## Base 승격 후보

- Registry의 고정 Skill 개수 검사를 제거하고 활성·비활성 상태를 검증하는 방식
- 특정 Base 커밋 문자열을 Validator에 하드코딩하지 않는 방식
- 레거시 Skill ID 별칭과 대체 대상 검증
- `always_on` 대신 trigger·stage 기반 최소 라우팅
- Registry와 실제 패키지 간 orphan·missing·dependency cycle 검사

Omenward 고유 코어 규칙, Godot 경로, C1~C4 게이트, 세 레인·룰렛·건설 노드 계약은 Base로 승격하지 않는다.

## GDD Sheet 기준

- GDD Sheet 의미 구조 기준: `c987647d01ad2baa028a16e03d85ddfc1572a727`
- Workbook: `docs/PROJECT_GOOGLE_SHEET_WORKBOOK.md`
- UX/UI 전용 content commit은 `docs/UX_UI_SYSTEM.md`가 별도로 소유한다.
