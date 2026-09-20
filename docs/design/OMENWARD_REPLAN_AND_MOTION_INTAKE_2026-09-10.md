# OMENWARD 재기획 · 신규 이미지 · 모션 제작 접수

## 2026-09-20 승인된 통합 준비와 첫 맵 검토

사용자는 제안된 첫 작업 묶음(통합 검사 정리 + 3전선 첫 맵 조작/재미 검토)을 승인했다. 기존 기획 PR258의 정확한 파일은 tools/validate_canon_freshness_v45_scope.py의 REPLAN_PREPARATION_ALLOWED_FILES로 등록한다. 디렉터리 전체/제품 코드/플러그인/미등록 후보는 허용하지 않는다. 후보를 저장소 검토 대상으로 인정하는 것과 최종 아트·수치·제품 승인은 별개다. 기존 사용자 미커밋 Blueprint/후보는 수정·스테이징하지 않는다.

| 분류 | 기존 파일과 책임 | 이번 처리 |
|---|---|---|
| 현재 승인/진행 원본 | AGENTS, Decisions, Active Context, Core/GDD/Roadmap, 본 접수 | 최신 전선 결정과 실행 범위를 연결; 아래 9/10 단일전선은 역사 |
| 권장 상세 설계 | benchmarks 재설계 검토, 9/10 command Blueprint, 9/11 human Blueprint 및 JSON | 수치/영웅/전체 기능을 자동 확정하지 않음 |
| 후보 시각 자료 | blueprint-20260911의 roster/building/hero/background/icon PNG 및 provenance | 실제 후속 consumer와 연결하되 최종 승인 상태는 유지 |
| 역사·비교 자료 | replan-20260910의 attack/slash pilot·field study·quality 후보, HTML/JSON/Aseprite | 폐기/삭제하거나 새 모션 완료로 표시하지 않음 |
| 파생 보고/검사 | v3 PDF/receipt, publisher, Blueprint tests | PDF는 바이너리 분류, 내용·원본 hash 불변; 문서 검사는 게임 검증 아님 |

작업 순서: 검사 실패 재현 → exact 범위/바이너리 분류 교정 → PR259에 부모 교정 연결 → 첫 맵의 정보·입력·결과 검증 → 기존 기록/원격 검사 갱신. 게임/저장/자산 수치 변경, 전체 게임 완료, 최종 아트 승인은 포함하지 않는다. 기존 승인이 있는 독립 구현을 막지는 않지만, 두 Draft PR의 전체 main 병합은 이번 '통합 준비'만으로 자동 실행하지 않는다.

Ruling: 기존 접수와 구현 계획을 실행 기록으로 재사용한다. 별도 ledger/PDF를 만드는 일반 스킬 관례보다 사용자 요청의 기존 정본 누적을 우선한다. 이번 계약의 검토는 전체 최대2회에서 공유하고 이전 운영 계약의 완료 검토를 재실행하지 않는다.

검증: 기존 실패를 재현한 뒤 준비 범위·PDF 분류 집중/회귀 62개 PASS, Git diff whitespace PASS. 독립 검토 1/2에서 작은 기존 운영 변경이 새 모드에 먼저 포착되는 P2를 발견했다. 기존 허용 모드 우선순위를 보존하고 동일 반례 RED→GREEN, 63개 회귀 PASS로 교정한다. PDF 데이터는 변경하지 않는다. 후속 첫 맵 검토의 코드·화면·결과는 BUILD 브랜치의 기존 visible-battle 계획에 기록한다. 루트의 사용자 미커밋 command Blueprint와 후보/미등록 PDF는 스테이징하지 않는다.

```yaml
decision_id: OMW-PLAN-20260910-RESTART-01
status: CORE_RETAINED__SYSTEM_SCREEN_ART_REDESIGN_RESEARCH_ACTIVE
authority: latest-user-request-2026-09-10
planning: REOPENED_FROM_FOUNDATION
existing_images_for_new_design: REFERENCE_ONLY
new_art: REQUIRED_AFTER_CONSUMER_AND_STYLE_BRIEF
motion: PLANNED_WITH_ART_FROM_START
runtime_replacement: NOT_STARTED
core_direction: ROULETTE_ARMY_BUILDING_AND_SINGLE_FRONT_AUTOBATTLE_RETAINED
research_owner: docs/benchmarks/OMENWARD_SYSTEM_SCREEN_ART_REDESIGN_REVIEW_2026-09-10.md
blueprint_owner: docs/design/OMENWARD_COMMAND_FLOW_AND_MOTION_BLUEPRINT_2026-09-10.md
recommended_direction_approval: USER_APPROVED_2026_09_10_CONTINUE
```

이 문서는 2026-09-10 사용자의 재기획 요청과 이번 조사 결과를 소유한다. 기존 게임의 완성 선언이나 새로운 장르 확정서가 아니다. 이전 이미지의 승인 이력은 역사로 보존하되 새 기획의 시각 정본으로 자동 계승하지 않는다. 기존 빌드의 이미지 참조는 새 자산 전환 때 교체한다. 원본 삭제나 저장 데이터 초기화는 이번 작업에 포함하지 않는다.

## 현재 근거와 책임 판정

| 대상 | 2026-09-10 직접 확인 | 판정 |
|---|---|---|
| 프로젝트 main | `9ea3245b5e4372222faa24e6acf84da7de8161d9` | 기존 병합 구현의 기준. 3전선과 건설 노드 표현이 남음 |
| 열린 PR 257 | `96198a22aa68e2153eb1a861b79e10b603612350` | 5개 순차 전선 구현과 9.4.4 adapter 존재. 미병합 비교 자료이며 새 작업에 흡수하지 않음 |
| 기타 열린 PR | 212, 209, 205 | 정본/오케스트레이션 문서 범위 중첩. 읽기 전용 |
| main Base adapter | `skills/PROJECT_BASE_ADAPTER.json`: 9.4.3 | 이번 분기에서 보존. 9.4.4는 열린 PR 쪽 상태 |
| 최신 Base remote | `2f93e872d9ed4fa18018ac759b01acd7d34e9b58` | 관련 Aseprite 지침만 사용자 요청에 따라 적용; release lock 업그레이드는 아님 |
| main 실제 이미지 consumer | `scripts/units/unit_view.gd`, `scripts/data/faction_visual_profile.gd`, `scenes/units/unit.tscn` | idle_texture와 IdleSprite 중심. 8개 상태명이 있어도 8개 동작 제작 완료가 아님 |
| PR 실제 consumer | `scripts/ui/battle_focus_view.gd` | 전장 배경·소품·병종 idle PNG를 직접 preload. 신규 프레임 재생·이벤트 계약 필요 |
| 이전 애니메이션 문서 | `docs/images/planning/OMENWARD_UNIT_ANIMATION_PRODUCTION_CONTRACT_2026-08-26.md` | 방패병 pair 한정·timing 미정·Notion 표현이 남은 역사 자료. 새 전 병종 계약으로 사용하지 않음 |

우선순위는 사용자 최신 지시 → 프로젝트 최신 AGENTS/main/Decisions/Active Context/실제 consumer/작업 중첩 → 적용되는 Base 공용 지침이다. 이름의 CURRENT/APPROVED, 과거 PASS 또는 문서에 고정된 SHA만으로 새 실행 권한을 복원하지 않는다. 기존 문서의 하위 블록은 새 기획 확정 전 역사/비교 자료다.

## Aseprite 자동 선택과 실호출 증거

사용 지침: Base `docs/knowledge/game-development/ART_DIRECTION_AND_ASSET_PLANNING_GUIDE.md` §11, 로컬 `C:/Users/user/.local/share/aseprite-local/LOCAL_USAGE.md`.

- 연결된 `aseprite-candidates` 도구를 현재 세션에서 발견하고 실제 호출했다.
- transport: native MCP, 제한된 후보 파일 batch 처리. 열린 편집기 실시간 제어가 아니다.
- 실행 파일 버전: Aseprite 1.3.18.5-dev.
- 새 그림과 창작 포즈: 이미지 모델. Aseprite: 복사본의 레이어/프레임/시간/PNG+JSON 정리.
- 후보 작업 경로: `C:/Users/user/.local/share/aseprite-local/candidates/omenward-replan-20260910/`.
- 참고용 기존 궁병 PNG 복사본 → `reference_probe.aseprite` → `reference_probe_sheet.png` + JSON 실제 내보내기 성공.
- readback: RGBA 512×512, 1 layer, 1 frame, 100ms, crop/rotation 없음. 이미지 미리보기 확인. 이 수치는 도구 확인 fixture이며 신규 제작 규격이 아니다.
- 원본 SHA-256: `B074BABB6B4088CA40C868230C0E79AC15E5857876F87E71BA4C9E8F00730B44`.
- PNG RGBA 디코드 비교: 원본/출력 전체 픽셀 동일, alpha 범위 0–255. JSON의 1 frame/100ms와 일치했다.
- 상태: `CLIENT_DISCOVERED`, `CALL_VERIFIED`; 신규 동작 제작/신규 자산 runtime은 `NOT_RUN`.
- 1프레임 파일 내보내기를 애니메이션 완성으로 간주하지 않는다. 기존 그림은 이 호출에서도 참고·호환성 확인 입력으로만 사용했다.

| 대안 | 적합성 | 선택 |
|---|---|---|
| 연결된 후보 MCP | 제한된 경로에서 필요한 복사·프레임·레이어·export 제공, 실호출 확인 | ADOPT: 현재 패키징 경로 |
| 공식 batch CLI | 반복 export에 적합하나 현재 MCP로 필요한 작업 가능 | DEFER: 지원 부족이 확인될 때 허용 범위 재평가 |
| 편집기 수동 타임라인 작업 | 섬세한 수작업 수정에 유효, 자동 완료 근거는 아님 | REFERENCE: 지원하지 않는 수작업의 대안 |

공식 근거: [Aseprite PNG+JSON export](https://www.aseprite.org/docs/cli/), [Godot 2D sprite animation](https://docs.godotengine.org/en/stable/tutorials/2d/2d_sprite_animation.html). 현재 후보 MCP에는 tag 생성 도구가 노출되지 않는다. 지원을 추정하지 않고 초기에는 상태별 파일과 명시적인 상태 metadata로 패키징한다.

## 재기획 작업 순서

| 순서 | 검토 가능한 결과 | 선행 조건 | 완료 증거 |
|---|---|---|---|
| 1 | 핵심 유지 확인 완료; 시스템·화면·아트 대안 비교 | 2026-09-10 사용자 답변 수신 | research_owner의 11개 비교·SWOT·요소 판정 |
| 2 | 첫 플레이 루프·자원·병력·전선 진행·실패/재시도 | concept 방향 | 상태 흐름과 정상/실패 사례 |
| 3 | 화면별 와이어프레임과 기능 관계도 | 플레이 루프 | 각 조작의 입력/결과/다음 화면 설명 |
| 4 | 신규 아트 방향과 실제 화면 크기의 병종 시안 | 화면·역할·camera | 대표 배경+아군+적군을 함께 배치한 비교 |
| 5 | 대표 병종 하나의 이동·공격 모션 pilot | 역할·아트 후보 | 준비/타격/회복의 구별, 발 고정, 무기 continuity |
| 6 | Aseprite 상태별 source/PNG+JSON 납품 | 생성 프레임 | frame count/duration/alpha/offset/hash readback |
| 7 | Godot 표시와 전투 이벤트 연결 | 검증된 파일 계약 | 이동/공격/피격/사망 전환과 중단/재개 실제 실행 |
| 8 | 확인된 방식으로 병종·전장·UI 확장 | pilot 검증 | 상태 누락 없는 자산 목록과 전투 화면 검수 |

기획 초기에 모든 병종 이미지를 대량 생성하지 않는다. 첫 pilot이 제작 방식·실제 크기·동작 일관성을 증명한 뒤 확장한다. 사용자가 핵심 유지와 시스템·화면·아트 재설계를 명시했다. 룰렛 병력 구성·단일 전선 자동전투는 유지하며 나머지 요소는 조사 owner에서 유지/보완/변경/추가/폐기 후보로 평가한다. 이전 5맵·건물 슬롯 등의 구체 승인 규칙을 실제 변경하려면 변경점과 근거를 명시한다.

## 새 모션 명세의 필수 연결 (제안, 수치 미확정)

| 항목 | 명세 내용 | 검증 |
|---|---|---|
| 상태 | idle, move, attack, hit, death 및 역할에 실제 필요한 상태 | 존재하지 않는 skill/victory를 관성적으로 양산하지 않음 |
| 동작 | anticipation → contact/release → follow-through → recovery | 같은 그림의 이동/복제로 실제 공격을 대체하지 않음 |
| 기하 | cell size, ground baseline, pivot, facing, weapon envelope, trim offset | 발 미끄러짐·크기 떨림·무기 잘림 확인 |
| 시간 | frame duration, loop, interrupt/priority, hit/projectile event | 판정 owner와 동기화; 진영 그림 변경으로 공격속도가 바뀌지 않음 |
| 엔진 | state → animation resource → renderer, presentation event | 게임 판정의 중복 실행/사망 뒤 타격/빠른 배속 시 이벤트 누락 방지 |
| 납품 | 새 source, state PNG/atlas, JSON, provenance/hash, preview | asset consumer 경로와 상태별 coverage |

구현 수단은 frame animation, 부분 리깅, 혼합 방식을 실제 새 아트에 대조한 뒤 선택한다. Aseprite를 쓴다는 이유로 픽셀아트나 고정 FPS를 먼저 확정하지 않는다. 현행 Sprite2D 소비처에서 AnimatedSprite2D/SpriteFrames 또는 AnimationPlayer로 바꾸는 방식은 pilot 후 결정한다.

## 남은 결정·검증과 롤백

- 사용자 답변 수신: 시스템·화면·아트를 새로 설계하고 기존 요소를 인터넷·벤치마크·실무·SWOT·독창성·창의성 관점에서 검토한다. 핵심 유지 여부 질문은 해결됐으며 반복하지 않는다.
- 초기 도구 확인은 새 게임 완성이 아니다. 후속 신규 아트 생성·품질 교정 후보는 blueprint_owner §6에 기록했다. 모션, 엔진 통합, Human은 NOT_RUN.
- 기존 코드를 삭제하거나 기존 이미지 원본을 덮어쓰지 않았다. 새 문서 분기는 main에서 만들었고 기존 열린 PR은 수정하지 않았다.
- project lesson: 상태 이름 목록과 실제 프레임/타격 이벤트 소비처를 반드시 대조한다.
- Base 승격: NO_NEW_REUSE_LEARNING; 이번에는 기존 조건부 도구 지침을 적용했다.

접수 변경 검증: `python tools/validate_project_core_docs.py` PASS, `git diff --check` PASS. scripts/scenes/data/assets/skills 변경 0. 검토는 (1) 사용자 재기획 지시 우선, (2) main과 미병합 PR 구분, (3) Base lock 불변, (4) 참고 이미지와 신규 창작 구분, (5) 모션 미제작 및 engine 미검증 상태를 각각 대조했다. 새 제품의 디자인/런타임 수용 검토는 아직 실행하지 않았다.
