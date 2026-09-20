# OMENWARD 프로젝트 작업 규칙

한국어를 쓰는 1인 개발자와 협업한다. 결과부터 설명하고 중요한 변경은 이유·작동 방식·직접 시험하는 방법을 알려준다.

채택 planning 계약: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8.
이미지 제작 권한 표식: USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES. 실제 범위와 최종 승인은 현재 Decision에서 확인한다.

## Current-authority read order

1. 이 저장소의 최신 AGENTS와 작업 폴더 변경사항을 확인한다.
2. 최신 원격 main, [현재 결정](docs/CURRENT_CONFIRMED_DECISIONS.md), [Active Context](docs/ACTIVE_CONTEXT.md)를 읽는다. 작업 브랜치의 승인·구현 상태와 main 상태를 구분한다.
3. 해당 결정의 기획 owner, 실제 코드·씬·데이터·자산 consumer, 관련 열린 PR과 중첩을 확인한다. [문서 지도](docs/DOCUMENTATION_MAP.md)에서 필요한 owner만 찾는다.
4. [채택 기록](docs/BASE_RULES_VERSION.md)과 [Base 계약](skills/PROJECT_BASE_ADAPTER.json)을 확인한 뒤 Base 최신 main과 적용되는 규칙·스킬·참조만 비교한다. 채택 lock 전체를 임의 교체하지 않는다.

과거 대화·메모리·PDF·고정 SHA·phase·닫힌 미병합 PR은 현재 실행 권한이 아니다. 충돌은 최신 사용자 지시와 현재 승인 owner, 실제 파일·검증 증거로 판정한다. 실행 사실이 승인되지 않은 제품 변경의 권한을 만들지는 않는다.

## 승인과 실행

- 새 변경은 의도·현재 상태·변경/보호 범위·방법·완료/검증 기준을 설명하고 승인받는다. 같은 승인 범위에서는 재질문·재계획을 반복하지 않는다.
- 승인 범위 안에서 구현·필수 자산 연결·검증·교정·정본 갱신·허용된 정상 PR 병합·main 재확인까지 이어간다. 새 방향·범위·비용·보안·파괴적 작업은 별도로 확인한다.
- 승인된 현재 게임 규칙·엔진·저장 호환성·자산은 보호한다. 제품 수치·전선 수·화면·아트 방향은 이 문서에 복제하지 않고 해당 결정 owner에서 읽는다.
- 기존 구현·승인 자산·Base 재사용 사례를 먼저 본다. 새로운 판단에 필요한 공식 자료·벤치마크만 추가 조사한다. 조사·스킬·문서의 양을 완료 기준으로 삼지 않는다.
- [공통 실행 계약](skills/SHARED_EXECUTION_CONTRACT.md)이 작업별 검토 예산과 증거 경계를 소유한다. 같은 승인 계보에서 전체 검토를 단계마다 초기화하지 않는다.

## 스킬과 검증

[프로젝트 라우터](.agents/skills/omenward-workflow-router/SKILL.md)를 통해 필요한 스킬만 선택한다. 새 스킬·서버·대시보드는 기존 책임으로 해결되지 않는 독립 필요가 있을 때만 제안한다.

계약 검사는 `tools/project_operating.py`의 프로젝트 router 생성을 사용한다. 원본 Base 판정과 별도 승인된 BUILD 범위 판정은 섞지 않는다.

- 기능·자동 검사, 실제 Godot 실행/화면, 기기·접근성, 사람 검수, 최종 자산 승인, 병합과 출시를 구분한다. 미실행은 NOT_RUN이다.
- Godot 작업은 project.godot와 현재 편집기/실행 대상이 같은 프로젝트인지 확인하고 테스트 저장은 실사용 저장과 격리한다.
- 플레이어 경험 변경은 [재미 검증 연결](docs/BASE_RULES_VERSION.md#재미-검증의-프로젝트-연결)을 따른다. 자동 검사·AI 판단으로 재미 통과를 선언하지 않는다. 사람 검수가 없어도 승인된 구현은 계속할 수 있다.
- 이미지 제작은 현재 시각 owner·실제 consumer·규격부터 확인한다. 필요한 실제 이미지 도구로 제작하며 후보·승인·등록·런타임 연결·화면 검증을 구분한다. 투명 오브젝트는 크로마키 제작 후 배경 제거와 alpha 검수를 연결하고, Aseprite 사용 여부는 실제 작업대로 기록한다.

## 보호와 기록

- 사용자 변경·다른 작업 폴더·열린 PR은 보호한다. 다른 PR의 수정·병합은 해당 범위의 명시적 권한이 있을 때만 한다. 강제 push나 보호 규칙 우회는 하지 않는다.
- 오래된 이름만으로 삭제하지 않는다. 사용처·폐기 근거를 확인한 정리 대상은 복구 정보와 함께 삭제 검토 폴더로 모아 링크를 준다. 사용자가 직접 삭제한다.
- 설치 플러그인·전역 설정·외부 서비스를 임의 변경하지 않는다.
- [저장소 정본 정책](docs/process/APPROVED_OMENWARD_REPOSITORY_ONLY_CANON_AND_NOTION_RETIREMENT_2026-08-28.md)을 유지한다. Notion은 RETIRED로 미래 read/write를 하지 않으며 Sheet는 역사 호환 자료이지 현재 기획 owner가 아니다.
- 플랫폼·출시·권리는 [플랫폼 승인](docs/APPROVED_PC_ANDROID_PLATFORM_RELEASE_AUTHORITY_2026-08-05.md), [기존 프로필](docs/PLATFORM_RELEASE_AND_ASSET_RIGHTS_PROFILE.md), [자산 권리 기록](docs/ASSET_RIGHTS_AND_PROVENANCE_RECORD.md), [출시 근거](docs/GAME_RELEASE_COMPLIANCE_EVIDENCE_PACK.md)를 따른다.
- 진행·다음 작업·근거는 기존 Active Context/책임 원본에 짧게 누적한다. 작업일지는 날짜별로 기존 월간 문서에 추가하며 매 작업마다 별도 PDF를 만들지 않는다.
- 완료보고는 달라진 점·이유·검증 결과·시험 방법·남은 위험 중심으로 작성한다. 문서만 바꾼 경우 게임 실행 완료로 보고하지 않는다.
