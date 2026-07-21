# Base 규칙·공용 지식 버전

- 원본 저장소: `alsdmlals4-eng/Base`
- 기준 커밋: `ee265576da7f67d3278f8099dd97d4e714ef0651`
- 동기화 기준일: `2026-07-21`
- 적용 방식: 프로젝트 정본을 우선하고, Base 공용 원칙은 `docs/base/SKILL_REGISTRY.json`과 로컬 Skill 어댑터로 명시적으로 채택
- Skill 시작점: `docs/base/START_HERE_SKILLS.md`
- 공통 실행 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 채택한 Base 영역

- spec-first 작업과 PLAN / BUILD / REVIEW 게이트.
- 최소 변경·실제 파일 우선·검증 중심 보고.
- 프로젝트 인수인계·컨텍스트 설계 방법.
- 새 Codex 채팅용 Work Order와 제안서·구현 결과의 분리.
- 아트 디렉션과 실제 화면 검수 방법.
- 애니메이션·전투 연출·판정 동기화 방법.
- 조사·벤치마킹·근거 관리 방법.
- Foundation 7개·Specialist 6개의 공용 책임 구조.
- 자동 Work Mode·Skill 라우팅과 패키지 무결성 검사.
- Adversarial Review·Red Teaming·Critique–Refine 검증 루프.

## 프로젝트 우선순위

일상 작업은 다음 순서를 사용한다.

```text
오멘워드 최신 사용자 지시
→ AGENTS.md
→ HANDOFF_CONTEXT.md
→ DOCUMENTATION_MAP.md
→ 현재 Work Order
→ 프로젝트 승인 책임 문서
→ 현재 Issue·Goal
→ 실제 파일과 테스트
→ docs/base/SKILL_REGISTRY.json과 선택된 로컬 Skill
→ 이 문서가 고정한 Base 커밋
→ Base 최신 공용 지식과 외부 참고
```

Base 원격 변경을 자동 적용하지 않는다. 동기화가 필요할 때 최신 Base `main`과 프로젝트 책임 문서를 비교하고 별도 PR로 갱신한다.

## 로컬 Skill 구성

- Foundation: 7
- Omenward Discipline: 11
- Specialist: 6
- 총 패키지: 24
- 기계 판독 정본: `docs/base/SKILL_REGISTRY.json`
- 실행 Router: `tools/route_skills.py`
- 무결성 검사: `tools/validate_skill_system.py`
- CI: `.github/workflows/validate-skill-system.yml`

공통 규칙은 `skills/SHARED_EXECUTION_CONTRACT.md` 한 곳에만 두고, 개별 Skill에는 고유 책임만 둔다. REVIEW는 `foundation.validation-review`와 `discipline.integration-review`를 강제로 포함한다.

## 주요 공용 지식 경로

- Base `docs/knowledge/README.md`
- Base `docs/knowledge/methods/`
- Base `docs/knowledge/research/`
- Base `docs/knowledge/skills/`
- Base `docs/knowledge/cases/`
- Base `templates/`

Base의 프로젝트 사례는 문제 해결 원리를 참고하기 위한 것이며 오멘워드의 최신 사양을 대체하지 않는다.
