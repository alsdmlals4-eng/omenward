---
name: omenward-workflow-router
description: Use when selecting OMENWARD project skills or validating its adopted Base operating contract.
---

# OMENWARD workflow router

AGENTS.md의 current-authority read order를 따른다. docs/BASE_RULES_VERSION.md가 release lock, 선택 채택 및 검사 도구를 연결한다.

1. 프로젝트 루트에서 `python -X utf8 tools/validate_skill_system.py`를 실행한다.
2. `python -X utf8 tools/project_operating.py --base-tools <채택 Base tools 경로> --base-repository <Base checkout> --check`로 release/protected/generated 계약을 검사한다. 실패 원인·범위를 분류한다. 승인된 운영 교정은 가능하나 보호 baseline 이동이나 실패 은폐는 금지한다. 제품 의존 실행은 해당 범위 검사 전 보류한다.
3. `python -X utf8 tools/route_skills.py --request "<현재 요청>"`로 후보를 확인하고 필요한 패키지만 읽는다. 명시 선택은 --skill, 사용법은 --help.
4. 로컬 경로는 현재 checkout 기준, Base는 출력 commit의 원문이다. selected_source는 선택 채택이고 나머지는 기존 release다. 최신 Base main도 조회해 drift를 구분한다.

선택은 실행 승인이 아니다. adapter/effective snapshot과 current registry만 사용하며 과거 docs/base registry는 명시 호환 검사 전용이다. Base 원문을 복사하지 않는다.
이 파일은 adapter.shared_overrides의 router_body에서 tools/project_operating.py가 생성한다. 직접 편집하지 않는다.

기계 정본: skills/PROJECT_BASE_ADAPTER.json, skills/PROJECT_SKILL_SNAPSHOT.json, skills/SKILL_REGISTRY.json.
