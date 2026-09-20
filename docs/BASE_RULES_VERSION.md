# Base 채택 기록과 운영 변경

## 현재 기준

- 프로젝트 실행 권위: AGENTS.md → 최신 main·현재 Decisions/Active Context → 관련 owner·실제 consumer·열린 PR → 적용 Base.
- released 계약: **v9.4.3 유지**. payload/evidence/finalization/registry hash의 기계 정본은 skills/PROJECT_BASE_ADAPTER.json의 base_release·skill_registry다. 이 문서가 별도 pin owner를 만들지 않는다.
- 2026-09-20 선택 채택 기준: Base main `23ecad5a3084f97c4e5d1e39a9a6d70d1eeb37ef`. 이는 이번 검토 revision이지 영구 최신 기준이 아니다. 다음 작업에서도 원격 main drift를 확인한다.
- [PR #883](https://github.com/alsdmlals4-eng/Base/pull/883)의 경량화는 main에 포함됨을 ancestry로 확인했다. [PR #885](https://github.com/alsdmlals4-eng/Base/pull/885)의 재미 검증도 사용자의 추가 지시로 이번 선택 채택 범위에 포함했다.
- 공용 원문: [작업 정책](https://github.com/alsdmlals4-eng/Base/blob/23ecad5a3084f97c4e5d1e39a9a6d70d1eeb37ef/docs/GPT_CODEX_WORKFLOW_POLICY.md), [운영 구조 스킬](https://github.com/alsdmlals4-eng/Base/blob/23ecad5a3084f97c4e5d1e39a9a6d70d1eeb37ef/skills/managing-game-project-operating-system/SKILL.md), [접수 스킬](https://github.com/alsdmlals4-eng/Base/blob/23ecad5a3084f97c4e5d1e39a9a6d70d1eeb37ef/skills/managing-project-intake-and-work-contract/SKILL.md).
- 선택 source는 adapter.shared_overrides에 기록하며 CLI가 해당 commit/path를 출력한다. 나머지 shared route는 released 계약을 유지한다. 이전 first_prompt/planning_first 필드는 released 호환 근거이며 같은 승인 재질문이나 Sheet 동기화의 현행 실행 명령이 아니다.

## 적용·보호·비적용

| 구분 | 결정과 이유 |
|---|---|
| 유지 | repository-only, 보호 경로/저장/권리, 승인 상태·runtime·human 증거 분리 |
| 선택 적용 | 프로젝트 우선 fresh-read, 승인 재사용, 필요한 스킬만 로드, 계약 전체 2회 full-scope 검토, 이후 영향 범위 교정 |
| 연결 교정 | 기본 CLI/검사 → current registry; 역사 registry는 명시 호환 전용. AGENTS에서 제품값 중복 제거, 4개 전문 스킬은 현재 owner 참조 |
| Sheet | legacy schema의 role은 호환 필드. effective_authority=COMPATIBILITY_ONLY, 과거 동기화 주장을 STALE로 교정; 미래 read/write 없음 |
| 비적용 | 전체 Base release/엔진 업그레이드, 게임 규칙 변경, 승인 자산 교체, 플러그인/전역 설정 변경, 새 감독 스킬/분석 서버 |
| 정리 | 파일 물리 삭제 없음. 폐기 대상은 사용자 검토/삭제 방식 유지 |

## 재미 검증의 프로젝트 연결

방법만 채택하며 이번 작업은 게임 재미 검증 PASS가 아니다.
[재미 검증 생명주기](https://github.com/alsdmlals4-eng/Base/blob/23ecad5a3084f97c4e5d1e39a9a6d70d1eeb37ef/skills/analyzing-and-refining-game-concepts/references/concept-evidence-and-gates.md#fun-verification-lifecycle),
[경험→효과·비주얼·UI 가이드](https://github.com/alsdmlals4-eng/Base/blob/23ecad5a3084f97c4e5d1e39a9a6d70d1eeb37ef/docs/knowledge/game-development/EXPERIENCE_TO_PRESENTATION_GUIDE.md),
[프로젝트별 연결/재구체화](https://github.com/alsdmlals4-eng/Base/blob/23ecad5a3084f97c4e5d1e39a9a6d70d1eeb37ef/skills/auditing-and-refining-ui-art/references/project-adapter-contract.md#10-효과비주얼ui의-프로젝트별-연결)를 필요한 기능 작업에서 선택해 읽는다.

- 경험 원본은 현재 Decisions가 선택한 GDD/Core의 source_id + path + section이다. 핵심/보조 경험·대상 플레이 맥락·금지 방향·대표 구간이 미정이면 HYPOTHESIS로 표시한다. 과거 브랜치의 기획을 main 승인으로 옮기지 않는다.
- 같은 기능 ID에 경험 가설/반증 → 입력·상태·규칙·정보·선택·표현/결과 → 실제 consumer → 검사·관찰을 연결한다. 검증/화면에서 역으로 같은 승인 원본까지 확인한다.
- 규칙 효과의 값·지속·중첩·실패는 domain owner, 표현은 실제 상태/이벤트를 소비한다. UI/VFX가 피해·보상·저장을 다시 계산하지 않는다.
- 표현·UI는 필요한 상태, 정보 우선순위, 실제 발생 시점, 입력·취소·중단·복귀, 자산 상태군, 해상도/설정별 확인 방법을 기록한다. 모든 상태·효과를 무조건 추가하지 않는다.
- L1은 기존 작업 기록에 **목적 → 상태/표현 → consumer → 확인 방법**으로 짧게 연결한다. 주요 기능은 기존 상세 Spec을 사용한다. L0 문구·순수 운영 도구는 이유 있는 NOT_APPLICABLE이며 별도 재미 보고서를 만들지 않는다.
- 관찰 행동·자기보고·필요 로그·반증을 대조한다. 이해 실패 / 선택·규칙 문제 / 피드백·감각 부족 / 반복 피로 / 기술 결함을 구분해 KEEP·CHANGE·DEFER·RETEST를 기존 Decision에 연결한다. 화려함·보상 빈도·재도전율을 보편 합격선으로 쓰지 않는다.
- 기술 Spike는 기술 질문에만 사용한다. 사람 경험은 실제 UI·대표 아트/모션/피드백이 연결된 짧은 대표 구간으로 확인하며 전체 게임 완성을 기다리는 게이트로 만들지 않는다.
- 동일 승인·가설·consumer·환경의 유효한 근거만 REUSED_EVIDENCE. DOC/MACHINE/RUNTIME/HUMAN/USER_APPROVAL/RELEASE를 분리하고 HUMAN NOT_RUN이어도 승인된 구현은 계속한다.

### 이번 main에서 확인한 연결과 적용 한계

아래는 기존 consumer 경로 확인이며 동작·재미 재검증 결과가 아니다. 기획 내용은 변경하지 않는다. 작업 브랜치 재개 시 해당 브랜치의 현재 owner·consumer로 다시 대조한다.

| 책임 | 기존 위치 | 이 방법의 적용 |
|---|---|---|
| 경험/인과 | docs/PROJECT_CORE.md §1·§2; docs/CURRENT_CONFIRMED_DECISIONS.md; docs/OMENWARD_GDD_CURRENT_CANON.md | 해당 기능이 어떤 선택/이해를 돕는지와 반증을 기존 owner에 기록 |
| 화면/입력 | scripts/ui/run_command_screen.gd; scripts/ui/stage_hud.gd | 승인된 입력의 접수와 확정 결과 구분, 취소/복귀·정보 가림 관찰 |
| 규칙/결과 | scripts/roulette/roulette_service.gd; scripts/units/deployment_service.gd; scripts/waves/wave_director.gd | UI가 확정 결과를 소비하는지 검증; 기능의 구체 값은 기존 데이터 owner |
| 시각 consumer | scripts/units/unit_view.gd; scripts/presentation/scene_binder.gd | 실제 소비 크기·상태군·pivot·alpha·모션 타이밍 대조 |
| 검증 기록 | tests/python/; tests/headless/; docs/ACTIVE_CONTEXT.md | exact revision/환경·기계/실행/사람 근거 분리 |

이 연결은 운영 방법 채택이다. 각 실제 기능의 값·상태·실패 복구·관찰 기준 구체화는 해당 승인 기능 작업에서 한다. 링크만으로 SPECIFIED나 FUN_PASS를 선언하지 않는다. 이번 governance의 플레이어 경험 영향은 NOT_APPLICABLE(제품 파일 변경 없음); 새 Godot 실행·사람 재미 검증은 NOT_RUN.

## 승인 작업 순서와 재개 기록

승인: 현재 대화의 “승인할게” 및 #885 재미 검증 추가 지시. 범위: 운영 지침·스킬 연결·관련 검사·정상 PR 병합/main 확인. PR258/259는 이번 운영 변경만 동기화하고 게임/기획 변경의 병합 승인은 확대하지 않는다.

1. 최신 main에서 별도 작업 폴더, dirty 사용자 파일/타 PR 보호 — 확인.
2. 기존 router의 legacy 기본 로드와 과도한 REVIEW stack을 테스트로 재현 — RED 확인.
3. AGENTS/공통 계약/4개 스킬/adapter/CLI/검사를 함께 교정하고 생성 view 갱신 — 완료.
4. full-scope 독립 검토 2/2 완료. 1차: 생성기/CI 불일치(P1), 선택 source 검증·영어 trigger 오분류(P2) 교정. 2차: 07c30fa4 기준 P0/P1/P2 지적 0건. 이후에는 해당 finding/CI 경로의 교정·회귀만 수행하며 전체 예산을 재시작하지 않는다.
5. PR #260을 정상 병합했다(main `7168c36706fcc1e5fbd1d1ca78b785a571b660ad`). PR 검사는 14 PASS/1 조건부 SKIP, 병합 후 로컬 569+22 검사 PASS. main의 Linux 3종/Godot는 PASS였으나 Windows 3종은 새 테스트의 인코딩 누락 1건씩 실패했다. 아래 한정 교정과 exact-head 재검증을 완료 기준으로 삼는다. 승인된 PR258/259에는 운영 변경만 동기화하며 두 제품 PR은 Draft/미병합으로 유지한다.

2026-09-20 병합 후 교정: cp1252로 한글 adapter를 읽을 때 같은 UnicodeDecodeError를 재현했다. 테스트의 파일 읽기/쓰기에 UTF-8을 명시하고, 기존 router projection을 BUILD 소비자가 재사용할 수 있는 함수로 추출했다. 전역 인코딩/엔진/플러그인 변경은 없다. 전체 검토 2/2 근거는 재사용하며 이 교정의 집중 검사·전체 회귀·원격 Windows 결과를 별도로 확인한다. 이 절의 오류 이력은 후속 PASS로 지우지 않는다.

Ruling: 승인된 적용안을 이 기존 채택 기록에 계획/진행으로 누적한다. 별도 Plan/ledger/PDF를 늘리는 일반 스킬 관례보다 사용자의 기존 정본 누적 요청을 따른다. 보호된 게임·자산 경로는 변경하지 않는다.

검증 기록(2026-09-20): Python 전체 569개, 실패/오류/skip 0; released 채택 검사 11개 통과; 현재 router 반례 10개 통과; Project Core 문서 및 프로젝트 특화 Base 계약 검사 통과. 첫 실행의 UTF-8 출력 오류는 이번 프로세스의 -X utf8로 분리했다. Registry의 raw hash는 약화하지 않고 해당 파일에만 LF checkout을 명시했다. 독립 baseline/forward-test는 옛 read order·리뷰 중복·고정 건설 노드·alpha/저장 보호 누락을 확인했으며, 교정 후 남은 UX 고정 질문을 현재 가설 기반으로 바꿨다.

기존 CI backend bfdc9e44의 Windows raw-byte health 검사에서는 CRLF checkout 때문에 Sheet 역사 증거 hash가 불일치했다. 최신 프로젝트 검증 backend 19355b7e는 Git canonical bytes를 사용해 통과한다. Linux CI backend의 실제 결과는 PR에서 별도 확인한다. 역사 증거를 현재 Sheet 권한으로 승격하거나 hash를 덮어쓰지 않는다.

PR #260 첫 원격 검사에서 단독 test module 실행 시 Python sibling import 실패를 확인했다. 전체 discovery가 먼저 sys.path를 추가해 가리던 결함이며 단독 실행 RED→package/CLI 양쪽 import 교정→19개 통과로 확인했다. 별도 tests/ 루트 검사 22개도 실행해 v9.4.0을 요구하던 낡은 released 기대값을 현재 v9.4.3으로 교정했다. router 원본 경로 표시는 생성 source에서 보충했다. 게임·기기·사람 평가 및 과거 기록 정리의 제외 판단은 유지하며 기존 문제를 새 게임 결함으로 꾸미지 않는다.

## 검사와 복구

프로젝트 루트에서:
- `python -X utf8 tools/validate_skill_system.py`
- `python -X utf8 tools/route_skills.py --request "AGENTS 작업구조 검토" --mode REVIEW`
- `python -X utf8 -m unittest discover -s tests/python`
- `python -X utf8 tools/validate_project_core_docs.py`
- `python -X utf8 tools/project_operating.py --base-tools <채택 Base tools 경로> --base-repository <Base checkout> --check`; 이 환경의 검증 도구 checkout은 원 프로젝트의 .worktrees/_base-validator-19355-blueprint. CI는 .base-contract/tools를 사용한다.
- 생성 view는 위 프로젝트 명령의 `--write`로 갱신한다. 원본은 adapter/registry다. released Base 생성기의 router template만 adapter.router_body로 특화하며 release/schema/hash/protected 검사들은 그대로 호출한다. 원본 Base 생성기를 직접 실행하면 옛 router가 재생성되므로 이 프로젝트에서는 wrapper를 사용한다. 원본 `--check`의 router 차이를 프로젝트 전체 PASS로 오인하지 않는다.

보호 경로 diff가 있으면 이번 운영 승인으로 통과시키지 않는다. 복구는 이번 운영 commit만 정상 revert PR로 되돌리며 제품·실사용 저장을 복원 대상으로 삼지 않는다. 과거 기록과 다른 작업 폴더는 삭제하지 않는다.
