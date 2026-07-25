# Base 규칙·공용 지식 버전

- 원본 저장소: `alsdmlals4-eng/Base`
- 기준 커밋: `c7c1103e4a69f8fdc9ee27aa382a21288605a7fb`
- 동기화 기준일: `2026-07-25`
- 적용 방식: 프로젝트 정본 우선, Base 공용 Skill은 route·adapter 연결, 자동 덮어쓰기 금지
- 기존 로컬 Skill 정본: `docs/base/SKILL_REGISTRY.json`
- 신규 Base 공용 route: `docs/base/BASE_SHARED_SKILL_ROUTES.json`
- 프로젝트 경로 어댑터: `docs/base/BASE_SHARED_SKILL_ADAPTER.json`
- 제3자 자산·플러그인 기록: `docs/base/THIRD_PARTY_ASSET_AND_PLUGIN_INVENTORY.json`
- 공통 실행 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 채택한 Base 영역

- spec-first PLAN / BUILD / REVIEW 게이트
- 프로젝트 코어 식별·보호
- 적대적 검토와 검증 증거 분리
- Skill 본문 단순화와 책임 중복 제거
- 구형·비기능 자료의 명시적 정리
- 계약 보존 리팩터링
- 프로젝트 컨텍스트와 인수인계 압축
- 정본 최신성·참조 무결성 검사
- 레거시 보존·아카이브 공용 Skill route
- Godot 에셋·상용 플러그인 선행 검색·평가 Skill route

## 공용 Skill·프로젝트 Skill 정책

```text
Base 공용 Skill
→ docs/base/BASE_SHARED_SKILL_ROUTES.json
→ docs/base/BASE_SHARED_SKILL_ADAPTER.json
→ 프로젝트 경로·정본·검증기 연결

Omenward 고유 Skill
→ 프로젝트 로컬에서 생성·유지
```

- 앞으로 Base 공용 Skill의 `SKILL.md` 복사본을 새로 만들지 않는다.
- 프로젝트 로컬 Skill은 Omenward 코어·Godot 구현·UX·아트처럼 프로젝트 고유 책임에만 만든다.
- 기존 `docs/base/SKILL_REGISTRY.json`의 로컬 공용 패키지는 즉시 삭제하지 않고 호환 입력으로 유지한다.
- 기존 복사본 정리는 별도 승인 아래 `governing-legacy-retention-and-archives`로 고유 정보·참조·복구 경로를 감사한 뒤 수행한다.
- Godot 기능·에셋·플러그인은 직접 제작 전에 공식 Store·기존 Asset Library·GitHub·itch.io·제작자 공식 판매처를 조사한다.
- 구매·계정 연결·프로젝트 설치는 별도 사용자 승인 범위에서만 수행한다.

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
→ docs/base/BASE_SHARED_SKILL_ROUTES.json과 프로젝트 어댑터
→ docs/base/SKILL_REGISTRY.json의 프로젝트 전용·호환 입력
→ 이 문서가 고정한 Base 커밋
→ Base 최신 공용 지식과 외부 참고
```

Base 원격 변경은 자동 적용하지 않는다. 새 Base 커밋을 채택할 때는 프로젝트 정본·Registry·Route·Adapter·Validator·문서 참조를 같은 변경 묶음으로 검증한다.

## Skill System v4 호환 상태

- 활성 Foundation: 7
- 활성 Omenward Discipline: 4
- 활성 Specialist: 1
- 활성 합계: 12
- 레거시 패키지: 16개를 `inactive`와 `replaced_by`로 등록
- 과거 Skill ID와 PR 표기는 `aliases`로 활성 Skill에 해석
- `always_on` Skill 없음
- REVIEW 단계에서만 `foundation.validation-review`와 `specialist.canonical-freshness`를 추가
- 주 Discipline 최대 1개, 지원 Discipline 최대 1개

구형 Skill 파일은 과거 기록과 호환성 보존용이며 새 Base 공용 Skill route보다 우선하지 않는다. 새 기획서·Issue·PR·Work Order는 프로젝트 전용 활성 ID 또는 Base 공용 route ID만 사용한다.

## Omenward 전용 활성 Discipline

- `discipline.omenward-core-design`: 핵심 루프·규칙·데이터 계약
- `discipline.omenward-godot`: Godot·GDScript·결정론·공유 데이터 검증
- `discipline.omenward-core-ux`: 10~15분 플레이테스트·HUD·해상도 가독성
- `discipline.omenward-art-assets`: 아트·애니메이션·판정 연출·에셋 파이프라인

## Base 공용 route

- `governing-legacy-retention-and-archives`: 레거시 인벤토리·통합·호환 stub·아카이브·승인 삭제·복구 검증
- `evaluating-godot-assets-and-plugins-before-creation`: 직접 제작 전 Godot 기본 기능·무료·오픈소스·상용 후보 검색과 도입 판정

## Base 승격 후보

- Registry의 고정 Skill 개수 검사를 제거하고 활성·비활성 상태를 검증하는 방식
- 특정 Base 커밋 문자열을 Validator에 하드코딩하지 않는 방식
- 레거시 Skill ID 별칭과 대체 대상 검증
- `always_on` 대신 trigger·stage 기반 최소 라우팅
- Registry와 실제 패키지 간 orphan·missing·dependency cycle 검사

Omenward 고유 코어 규칙, Godot 경로, C1~C4 게이트, 세 레인·룰렛·건설 노드 계약은 Base로 승격하지 않는다.
