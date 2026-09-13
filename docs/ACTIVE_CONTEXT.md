# [현행] OMENWARD Active Context

병종 표적 연결 후 모델224/0실패, UI/저장/기본 실행 PASS. 궁병은 사거리내 비행 우선, 비행병 지상 후열 우선, 암살자는 상세 progression 명세의4거리(모델12) 내 후열 우선/첫 후열타1.4/10초 재사용. ambush 저장·맵 초기화·양진영 역방향 접근·재정비 동결 검사. 이동 방향 변경은 새 두 역할만, 기존 병종 보존. GPU 기존 전투14피해/13유닛·혼합10유닛·방패3상태 재확인; 암살자 전용 모션/시각 검증 아님. 자동 원정 결과는 여전히2맵2라운드패배. 다음은 생존 등급/T3/영웅을 포함한 미연결 성장·경제 대조.

후속 v6 재도전 연결: 새 맵 진입 checkpoint를 준비 구매/추첨 전에 저장, 패배시에만 정확 복원하며 반복 재도전 보상 누적 없음. 구형v1–v5는 근거없는 checkpoint를 생성하지 않아 다음 맵까지 재도전 불가 사유 표시. 모델209/0실패 및 UI/저장/기본씬 PASS. JSON 숫자 배열 직접 동등성으로 유효 checkpoint가 거절되던 회귀를 scalar 검증으로 수정. 전체 연속원정3seed는 자원 주입 없이 1맵 점령→2맵 진입에 성공했으나2맵2라운드 모두 패배. 5맵 자연완주/Human은 미달. 다음은 누락 병종 대응/성장과 후반맵 압력·경제 연결 점검. 2c25285b 원격5검사 PASS 확인; v6 원격은 별도.

전체 게임 구현 위임을 최신 실행 목표로 적용. 순차 5맵 전환/v5 저장/거점·자원·부상병·시설 계승/맵별10·10·10·11·12라운드/최종맵 경계/9칸 이후 목록 페이지 연결. GPU front-campaign은 승리 상태를 설정한 전환 경계 fixture이며 자연 5맵 완주 아님. 배경은 공통 임시 자산. 재도전 진입 snapshot·전체 맵 밸런스·고유 아트는 다음 작업. 독립5관점 정적 검토 차단 결함 없음, 후반 라운드와 v5 오류 입력 보강. 앞선 cc6961c1 원격2검사 실패 원인은 Blueprint exact2경로 allowlist 누락이며 RED/GREEN으로 교정; 새 원격 검증은 별도.

최신 로컬 검증: 모델161검사/0실패, 화면·저장·기본씬 PASS. 아래109/154 등은 이전 검사 이력. 프로젝트 scoped validator PASS, Base raw protected-path FAIL은 승인된8경로 예외로 별도 유지한다. CI/main/Human 상태는 별도 readback 없이는 승격하지 않는다.

2026-09-13 병종 대응/첫 맵 조정: 방패 정면 궁수 피해25% 감소(접전 중), 기병 이동2 후 첫 병력 타격1.5배, 창병 접전 정지0.6초 후 돌격 피해50% 감소를 양 진영에 연결했다. 새 첫 맵 pressure0.4는 임시 플레이테스트 값, v4 저장에 압력을 보존하고 v1–v3는1.0 유지. 1.0의12자동 운영은 모두 패배,0.4 추가 동원 운영은3seed 모두2라운드 본진 점령; 다른6운영은3–4라운드 패배. 최적/장기/Human 밸런스 PASS 아님. GPU14피해/13생존 유닛, 방패3상태 확인. 독립5관점 정적 검토의 부분 돌격 누적 결함 수정, 저장 경계 검사 보강. 기존 PDF는 이번 변경 전 파생물이다. 다음은 전략 편향과 다른 병종의 누락 능력, 전체 아트/5맵 연결이다.

최종 후속 검사109개 PASS: midwave 전체 상태는 JSON 부동소수점1e-9 허용오차 내 일치, legacy profile v3 재저장/재복원까지 확인. 아래107개는 직전 검사 이력. 공세 5관점 독립 정적 검토 차단 결함 없음; 독립 reviewer runtime/Human은 NOT_RUN.

2026-09-13 공세 연결 후속: 새 원정은 공세 cycle의 연속3항목, 라운드3% 증가의 올림 수량,0.4초 순차 출현을 사용한다. 예보/스폰은 wave_composition을 공유한다. v3는 wave_rules를 저장하고 v1/v2 원정은 legacy 출현 유지.107모델/UI/저장/기본 실행 PASS; GPU20damage/15units/방패3상태. 4자동 운영 모두 round2패배; paid_mobilization만 첫 재정비 아군5/적11, 치료2G 사용. 초기 밸런스는 미완료다. 다음은 병종 고유 대응·생산/충원·첫 맵 경제의 누락 대조와 복수 난수 검증이며 단순 HP 증액으로 결과를 덮지 않는다.

2026-09-13 징조륜 연결: 관측→행/열 3회 이동→복수 완성선 보너스 선택→확정 지급을 구현했다. 대기열은 병종 용량 합이며 최대 지급 공간을 회전 전 확인한다. pending 상태의 건설/전문화/재회전/공세 시작을 차단하고 v2 저장에 이동 수/예약량을 보존한다. 정상 v1은 수용, 용량 초과 구형 저장은 손실 없이 거절한다. 99모델/UI/저장/기본 실행 PASS, GPU front-omen 확인. 독립 검토에서 발견한 불가능한 pending 병종 저장 수락을 RED→수정→GREEN으로 교정했다. 실제 자원 유료 동원 정책은 첫 재정비 아군5명으로 개선됐지만 2라운드 패배; 다른3정책도 패배. 최적 전략/밸런스/Human PASS 아님. 다음은 명세의 wave cycle/0.4초 순차출현과 현재 동시 출현 구현의 차이를 교정한다.

2026-09-13 최신 루프 교정: 유사 장르 조사→기획 구체화→시스템 연결→구현→실제 실행→보완을 반복하며 UI 수정만으로 축소하지 않는다. 기존 Blueprint 개별 유료 치료를 준비/재정비 창·골드·HP·저장에 연결했다. 모델81검사 및 UI/저장/기본 실행 PASS. 치료 GPU 캡처는 명시적 혼합 부상병 경계 fixture이며 자연 생존 증거가 아니다. 시작 자원/seed1947/0.1초 간격의 병영 증설·궁병 전문화·일반/특수 혼합 운영은 모두 첫 재정비 아군0/적12~13, 2라운드 패배, 치료 지출0이었다. 최적 운영 불가능이나 전체 밸런스 FAIL 확정은 아니다. 다음은 초반 생산·공세·충원과 징조륜 선택 연결이며 아래 아트-only 우선순위를 대체한다. 전체 게임/Human/main 통합 미완료.

혼합 병종 후속: 실제 병력 상태의 진영/이름/체력을 읽는 근접 hover 정보 추가(최대6행+초과 안내). 5병종×양측10유닛 검증 편성, 실제0.6초 전투10피해 처리 후720/1080 캡처. 720에서 마우스 입력→native 팝업 표시 확인. 일반 획득/밸런스 증거 아님. 혼합 검사에서 아군 방패병 외 도감의 불투명 흰 사각형이 확인되어 다음은 해당 소비 자산 투명화 계획이 우선. 모델68/UI·저장/기본실행 PASS; Human/전체 아트 미완료.

2026-09-13 계획 승인 후 표시 개선: 고정 4단 깊이/최대24px 후방 표시 보정, 복사 배열 깊이 정렬, 체력바 후순위 표시. 전투 모델/저장 규칙은 변경하지 않았다. 68모델·화면/저장/기본실행 PASS, 표시 계산 포함230단계와 대조 모델 상태 일치. 720p/1080p GPU 화면 및 방패3상태 확인. 중첩은 감소했으나 동일 배치 반복/체력바 중첩은 PARTIAL. 전체 혼합 병종 시각 스트레스·Human은 남아 있다.

2026-09-12 지속 개선 1회차: 최신 Base remote d830c0f6를 비교했으며 채택 v9.4.3은 유지한다. 현재 공세 스폰 데이터에서 다음 병종/수량/시간을 읽는 공통 2줄 예보와 선택 병영 생산 진행·중단 사유를 연결했다. Into the Breach/Thronefall/Commander Quest/Slotbound 공식 자료의 ADOPT/ADAPT/REJECT는 기존 실행 계획이 소유한다. 모델68검사·화면/저장/기본 실행 PASS; 정지·종료·잠긴 건물 전문화 회귀 포함. Human/전체 제품 완료는 아니다. 후속 순서는 Roadmap 최신 블록을 따른다.

2026-09-12 베기 연결: 기존 RGBA 원화의 네 병사 성분은 서로 겹치지 않아 개별 분리 후 768×768, 발 피벗(384,700)으로 평행이동했다. RGB/가시 픽셀 보존, native Aseprite 4프레임 및 PNG 정확 일치. 방패병 대기→준비180ms→베기100ms→복귀150ms를 실제 전투에 연결했고 준비 종료 때 살아 있는 동일 대상/사거리를 재검증해 1회 타격한다. 첫 타격에 준비 지연이 생기며 기존 피해량/공격 주기 수치는 유지한다. 모델55검사, 화면·저장·기본실행 PASS, 원화/출력2검사 PASS, GPU 자연 전투19damage/16units 및 준비·베기·복귀3상태 캡처 확인. 5회 전체 범위 독립 검토에서 차단 결함 없음. 아래 idle-only/모션 미연결은 이 방패병 범위에서 역사. 4자세 후보이며 이동·피격·사망/다른 병종 공격·최종 Human은 미완료. Aseprite 프레임 복제에 따른 겹침 실패본은 직접 삭제하지 않고 사용자 검토 폴더에 모은다. Base 원검사 FAIL / 한정 BUILD PASS와 부모 PR·main 통합 경계는 유지한다.

2026-09-12 경계 후속: alpha 안쪽 0.5px 보정과 사제 발밑의 제한 영역 제거를 적용했다. 원본 RGB는 전부 유지, 제거된 1860픽셀은 검토한 발밑 영역 안이며 몸체/좌측 마법광 회귀를 추가했다. cutout 5개, scope 5개, Godot39/UI·저장 PASS, GPU19damage/16units 재검증. PNG/native Aseprite 왕복 동일. 여전히 사제 종이색 띠·내부 잔여·수평 절단 인상은 PARTIAL. 새 방패병 4자세 생성본은 RGB 체크무늬여서 runtime 미적용. 다음은 자세별 개별 제작→추출 검수→동일 피벗/시간→시트 조립→타격 연결이며 전체 시트 투명화 반복 요청은 중단한다. 삭제 검토 목록은 현재92개/139319809바이트, 직접 삭제 없음. 최신 자산 해시는 ROSTER_PROVENANCE가 소유한다.

2026-09-12: 사용자는 로컬 배경 제거/마스크 도구와 삭제 대신 별도 폴더 보관을 승인했다. 베일 10종은 기존 원화 RGB를 보존한 RGBA 정적 후보로 검토판에 연결했다. 사제형 밝은 외피 유실을 검수에서 발견해 해당 셀만 보수 처리했으며 특수 비행병은 y=610 빈 간격에서 잘라 날개를 보존했다. 잔여 종이색 가장자리 품질은 PARTIAL, 새 공격 프레임은 미제작이다. Aseprite 정적 native 저장/PNG 왕복 RGBA 일치, cutout 3검사, Godot 모델 39검사/화면·저장 PASS. 전체 모션/Human 승인 아님. 삭제 검토 위치는 `C:/Users/user/Downloads/OMENWARD_DELETE_REVIEW_20260912`; 최종 목록 `ALL_FILES.csv`와 `README.md`를 따른다. 직접 삭제하지 않는다. 세부 출처·상태는 ROSTER_PROVENANCE, 승인 범위는 기존 UI/motion owner를 따른다.

2026-09-11 후속 UI/투명 이미지: 사용자가 기획 전용 계약의 한정 BUILD 전환을 승인했다. owner: `docs/process/APPROVED_REPLAN_UI_MOTION_BUILD_SCOPE_20260911.md`. Base v9.4.3 원검사의 protected-path FAIL과 프로젝트 한정 승인 PASS를 분리한다. 버전/기준점/보호 목록은 유지한다. 탭 선택, 일시정지/재개, 현재 배속, 한국어 phase를 연결했다. 아군 방패병 대기 1셀만 실제 RGBA 후보로 연결했다. 베기 시트는 셀 침범 때문에 모션 미연결; 간격 교정본은 RGB 체크무늬로 실패했다. Aseprite 이번 후보 미사용. 전투 규칙 39검사, 화면/저장/알파 검사, 실제 GPU 전투·건설 캡처 PASS. 전체 모션·나머지 병종 투명화·Human/제품 완료는 아님. 새 원격 CI 상태는 exact HEAD로 별도 확인한다.

2026-09-11 현재 BUILD: 사용자 승인에 따라 `scenes/replan/front_slice.tscn`에 별도 단일 전선 검토판을 구현했다. 이 작업 공간의 기본 실행은 검토판이며 기존 장면은 ‘기존 빌드’ 버튼으로 보존한다. 새 앱 이름으로 저장 공간을 분리했다. 실제 규칙 모델 `scripts/replan/front_run.gd`, UI `front_screen.gd`, 아틀라스 소비 `front_art.gd`. 상세 범위·검사·잔여 작업은 `docs/superpowers/plans/2026-09-11-visible-battle-slice.md`. 아래 구현 보류와 제품 코드 미변경 기록은 이 범위에서 역사다. 원격 main 통합 완료를 뜻하지 않는다.

현행 v3: 일반병/특수병 분리 사용자 교정을 반영했다. 일반 5+특수 5=10병종, 별도 T1 뿌리와 T2 전문화, T3 동일 병종 심화로 데이터/본문을 교정했다. 이전 8병종·단일 병영 트리는 superseded. 특수 T1 추첨/토큰, 등급 체계와 영웅은 권장안이다. 68쪽 v3 검토 PDF, 기획 데이터 검사 12개 PASS. 암살자/비행병 아군·베일 정적 도감 후보 추가(Aseprite 미사용). 전체 구현 착수 준비는 PARTIAL; 제품 코드는 변경하지 않았다.

최신 보완: 사용자 요청으로 아군/베일 병종 이미지, 티어·등급 스킬, 영웅, 건물 이미지를 추가한 61쪽 v2 검토판을 제작했다. T1 병영=방패병, 업그레이드 후 전문 병종 공급이 사용자 확정이며 이전 자유 공급변경/전문시설 직접건설 권장안을 교정했다. 세부 분기·숙련/정예·영웅 3명은 RECOMMENDED. 도감 이미지 4시트는 RGB 카드 후보이며 전투 sprite/모션 아님. 관련 owner는 아래 동일 문서/JSON, 자산 검토는 `docs/images/candidates/blueprint-20260911/ROSTER_PROVENANCE.md`. 제품 구현·전체 자산 준비·Git 원격 반영 완료는 주장하지 않는다.

2026-09-11 최신 우선 지시: 다른 프로젝트 PDF의 편집 구조만 참고하여 사람용 통합 블루프린트를 제작한다. 필요한 인게임용 이미지 후보 제작은 다시 허용되었으며 아래 이미지 보류 기록을 supersede한다. 제품 구현은 사용자 최종 승인 전 보류한다. 현행 검토 owner는 `docs/design/OMENWARD_HUMAN_BLUEPRINT_REVIEW_20260911.md`, 숫자 입력은 `docs/design/OMENWARD_BLUEPRINT_BUILD_INPUT_20260911.json`. 39쪽 검토 PDF를 생성했으나 전체 자산/모션이 준비되지 않아 FINAL_IMPLEMENTATION_READY가 아니다. 실제 Godot/밸런스/Human은 NOT_RUN.

후속 기획 검토: Blueprint §1 H~L에 재미 축·누적 12게임 비교 연결·방어/진격/경제 운영·10라운드 학습 흐름·고의 지연 보상 위험·선택 치료 후보를 추가했다. main 기반 단일 대상 공격 경로에서는 사제 치료/마법사 범위공격 태그의 실제 효과를 확인하지 못해 기획과 구현을 분리했다. 부분 코드 감사이며 재미/밸런스 시험은 NOT_RUN. 다음 안전 작업은 병종 역할과 공급/회복 비용의 검증용 명세이며 이미지/구현 보류는 유지한다.

최우선 작업 변경: 이미지/모션 제작과 구현 보류. 사용자 확정은 맵→10+α 시간제 라운드→복수 웨이브, 라운드 후 재정비, 전체 라운드 생존 또는 적 본진 점령 승리다. 상세 조사·권장 설계는 `docs/design/OMENWARD_COMMAND_FLOW_AND_MOTION_BLUEPRINT_2026-09-10.md` §1의 현행 상세 진행 설계가 소유한다. 아래 아트 작업은 보존된 이전 작업이며 다음 실행 순서가 아니다. 권장 수치/동결 계승/재시도는 SPECIFIED_RECOMMENDATION, runtime/Human NOT_RUN.

현재 작업(2026-09-10): 베기 V2에서 후속 자세의 긴 검을 보정하고 별도 회복 포즈를 추가해 5프레임 후보를 구성했다. Aseprite 입력 픽셀·시간·기하 및 실제 로컬 브라우저의 단계/재생/정지/모바일 배치를 검사했다. 회복 프레임의 검/갑옷 차이가 남아 아트는 PARTIAL; 투명화·피벗·Godot는 미완료다. `docs/design/OMENWARD_COMMAND_FLOW_AND_MOTION_BLUEPRINT_2026-09-10.md` §8의 V2가 owner다. PR 정본/계약 범위 불일치도 병합 전 해결 대상이다.

> **2026-09-10 재기획 우선 적용:** 사용자는 기획부터 다시 시작하고 기존 이미지는 참고자료로만 사용하며 새 이미지와 모션을 함께 제작하도록 지시했다. 현재 접수·근거·작업 순서는 `docs/design/OMENWARD_REPLAN_AND_MOTION_INTAKE_2026-09-10.md`가 소유한다. 아래의 이전 제품 기획·시각 승인·phase·완료 상태는 새 기획의 실행 권한이 아닌 기존 빌드의 역사/비교 자료다. 보안·저장 보호·권리·Git 보호 경계는 유지한다. 읽기 순서는 프로젝트 최신 AGENTS → 최신 main → Decisions/Active Context → 실제 consumer와 열린 PR 중첩 → 적용 Base 지침이다. Base version lock은 변경하지 않는다.

```yaml
updated_at: 2026-08-29
status: FIRST5_FTUE_CORE_LOOP_RECONCILIATION__OPEN_BATTLEFIELD_V6_VISUAL_DIRECTION_LOCKED
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
current_decision_index: docs/CURRENT_CONFIRMED_DECISIONS.md
current_gdd: docs/OMENWARD_GDD_CURRENT_CANON.md
current_project_core: docs/PROJECT_CORE.md
current_handoff: docs/handoffs/2026-08-29-open-battlefield-v6-visual-lock-handoff.md
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_open_work_items: FRESH_GITHUB_QUERY_REQUIRED
current_activity: FIRST5_FTUE_CORE_LOOP_RECONCILIATION__OPEN_BATTLEFIELD_V6_VISUAL_DIRECTION_LOCKED
current_forward_defense_spec: docs/design/APPROVED_OMENWARD_FORWARD_DEFENSE_AND_OCCUPATION_NODE_CONTRACT_2026-08-28.md
current_open_battlefield_layout_spec: docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_TOWER_ONLY_FORWARD_LAYOUT_2026-08-28.md
current_visual_direction_lock: docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_V6_VISUAL_DIRECTION_LOCK_2026-08-29.md
current_visual_spec: docs/superpowers/specs/2026-08-28-storybook-sd-three-front-strategic-map-design.md
current_visual_decision: OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01
current_visual_topology: ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT
current_visual_board_file: docs/images/planning/generated/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28_v6_OPEN_BATTLEFIELD_NO_BARRICADE.png
current_visual_route_state_grammar: WARD_CITADEL_HOME_BASE__WARD_FORWARD_BASE__CLASH_ZONE__VEIL_FORWARD_BASE__VEIL_CITADEL_HOME_BASE
current_visual_asset: NONE__NEW_DIRECTION_PLANNING_ONLY
legacy_runtime_visual_asset: OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1
current_build_runtime_unit_asset_set: LEGACY_STYLE_FIT_REVIEW_REQUIRED
current_unit_animation_production_contract: docs/images/planning/OMENWARD_UNIT_ANIMATION_PRODUCTION_CONTRACT_2026-08-26.md
current_screen_surface_visual_coverage_audit: docs/design/OMENWARD_GAME_SCREEN_AND_IMAGE_COVERAGE_2026-08-28.md
implementation_authorized: true
implementation_scope: RUN_COMMAND_ORCHESTRATION_FIRST_VERTICAL_SLICE
implementation_execution: IMPLEMENTED__HEADLESS_CONTRACTS_AND_THREE_RESOLUTION_TECHNICAL_QA_CAPTURED__HUMAN_NOT_RUN
implementation_packet: docs/implementation/OMENWARD_RUN_COMMAND_VERTICAL_SLICE_WORK_PRODUCTION_INPUT_PACKET_2026-08-27.md
implementation_plan: docs/superpowers/plans/2026-08-24-run-command-vertical-slice.md
visual_generation_policy: USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
visual_generation: USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
visual_confirmation: GENERATE_THEN_USER_CONFIRM_LOCK
current_human_facing_canon: REPOSITORY_ONLY
notion_current_authority: RETIRED__NO_FUTURE_READ_OR_WRITE
repository_only_policy: docs/process/APPROVED_OMENWARD_REPOSITORY_ONLY_CANON_AND_NOTION_RETIREMENT_2026-08-28.md
notion_migration_report: docs/migrations/OMENWARD_NOTION_CURRENT_CONTENT_TO_REPOSITORY_MIGRATION_2026-08-28.md
current_chat_runtime_status: PARTIAL__RUN_COMMAND_PREPARE_TO_BATTLE_LIVE_CAPTURED__HEADLESS_NATURAL_TUTORIAL_TO_REVIEW_PASS__HUMAN_NOT_RUN
human_player_evidence: NOT_RUN
```

Notion의 current structure/work read-only migration은 완료했다. 이관 내용과 stale/superseded 분류는 `docs/migrations/OMENWARD_NOTION_CURRENT_CONTENT_TO_REPOSITORY_MIGRATION_2026-08-28.md`가 소유하며, 이후 Notion read/write는 재활성화 전 금지다.

## Current planning state

```text
CURRENT_APPROVED_REPLAN_DECISIONS = 27
WORLD_ROLE = CONFIRMED
MAPRUN_WORLD_MEANING = CONFIRMED
PRESSURE_LANGUAGE = CONFIRMED
MOBILIZATION_REGISTRY = CONFIRMED
FIRST5_FTUE = CONFIRMED__STAGE1_COMMAND_ROOT_FORWARD_DEFENSE_AND_LOCKED_NODE_LEARNING_AMENDED
STAGE_1_DIRECT_CONSTRUCTION = FORBIDDEN
HOME_BASE_PREBUILT_PRODUCTION_BUILDINGS = NONE
HOME_BASE_CONSTRUCTION_NODE_COUNT_PER_FACTION = 4
HOME_BASE_FIXED_AUTO_ATTACK_TOWER_COUNT_PER_FACTION = 2
FORWARD_BASE_CONSTRUCTION_NODE_COUNT_PER_BASE = 2
FORWARD_BASE_FIXED_AUTO_ATTACK_TOWER_COUNT_PER_BASE = 1
STAGE_1_NODE_INTERACTION_STATE = VISIBLE_LOCKED__FIRST_MEANINGFUL_BUILD_STAGE_2
FIRST_MEANINGFUL_BUILD_OR_UPGRADE = STAGE_2_T2_UPGRADE
FORWARD_BASE_FIXED_DEFENSE_STACK = AUTO_ATTACK_TOWER_ONLY
FORWARD_BARRICADE = REMOVED__NOT_A_FIXED_DEFENSE_OR_MAP_VISUAL
FENCED_OR_ENCLOSED_BASE_BOUNDARY = FORBIDDEN
OCCUPATION_NODE_ACTIVATION = STABLE_PLAYER_OWNED_OUTPOST_ONLY
FORWARD_DEFENSE_OCCUPATION_NODE_STATUS = CONFIRMED__PLANNING_ONLY__NOT_IMPLEMENTED
FORWARD_DEFENSE_OCCUPATION_NODE_DECISION = OMW-PLAN-20260828-FORWARD-DEFENSE-OCCUPATION-NODES-01
OPEN_BATTLEFIELD_TOWER_ONLY_LAYOUT = CONFIRMED__PLANNING_ONLY__NOT_IMPLEMENTED
OPEN_BATTLEFIELD_TOWER_ONLY_LAYOUT_DECISION = OMW-PLAN-20260828-OPEN-BATTLEFIELD-TOWER-ONLY-01
RUN_COMMAND_SCREEN = CONFIRMED
WORLD_CONFLICT_AND_STORY = CONFIRMED
CONTENT_BOSS_ARC = CONFIRMED
NORMALIZED_BALANCE_BUDGET = CONFIRMED
TEXT_UX_STATE = CONFIRMED
VISUAL_STYLE_COMPONENTS_20260820 = PARTIALLY_SUPERSEDED
BATTLEFIELD_SCALE_AND_COMBAT_READABILITY = RETAINED_WITH_LAYOUT_OVERRIDE
ROULETTE_3X3_COMPONENT = CONFIRMED
TOKEN_COMPONENT = CONFIRMED
LOWER_CONTROL_DECK = CONFIRMED
ROULETTE_DDD_FEEDBACK = CONFIRMED
TOPDOWN_BATTLEFIELD_LAYOUT_20260820 = PARTIALLY_SUPERSEDED
TOPDOWN_UNIT_SILHOUETTE = CONFIRMED
NORTH_STAR_V2_1 = HISTORICAL_REFERENCE_ONLY
FRONT_STATE_MINIMAP_SD_FANTASY = PARTIALLY_SUPERSEDED__THREE_FRONT_RESPONSIBILITY_RETAINED
APPROVED_VISUAL_OM_IMG_023 = HISTORICAL_REFERENCE_ONLY
APPROVED_VISUAL_BATTLEFIELD_BACKDROP_V1 = LEGACY_RUNTIME_ASSET__CURRENT_BUILD_ONLY
STORYBOOK_SD_THREE_FRONT_STRATEGIC_MAP = USER_CONFIRMED_CURRENT
MAP_TOPOLOGY = ONE_WARD_CITADEL_ROOT__THREE_SHARED_FRONTS__ONE_VEIL_CITADEL_ROOT
FRONT_STRUCTURE = ONE_WARD_CITADEL_ROOT -> THREE_SHARED_FRONTS -> ONE_VEIL_CITADEL_ROOT
ROUTE_STATE_GRAMMAR = WARD_CITADEL_HOME_BASE -> WARD_FORWARD_BASE -> CONTESTED_CLASH_ZONE -> VEIL_FORWARD_BASE -> VEIL_CITADEL_HOME_BASE
PROJECT_CORE_SCENE_VISUAL_BOARD_SCOPE = STRATEGIC_MAP_ONLY__LOWER_UI_STORYBOARD_REMOVED
PROJECT_CORE_SCENE_VISUAL_BOARD = USER_CONFIRMED_PLANNING_LOCK__V6_OPEN_BATTLEFIELD_NO_BARRICADE__NOT_RUNTIME_ASSET
NOTION_CURRENT_VISUAL_IMAGE = HISTORICAL_SERVER_READBACK_ONLY__NO_FUTURE_WRITES
FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5
GITHUB_NOTION_DRIFT_CHECK = PASS
FINAL_PLANNING_REVIEW_SCOPE = RETAINED_PRE_20260825_VISUAL_OVERRIDE_EVIDENCE
IMPLEMENTATION_AUTHORITY = SCOPED_APPROVED
RUN_COMMAND_IMPLEMENTATION_EXECUTION = IMPLEMENTED__MACHINE_QA_AND_HUMAN_PLAYTEST_REMAIN
HISTORICAL_PRE_APPROVAL_GATE = IMPLEMENTATION_AUTHORITY_REQUIRED
PROJECT_ACTIVITY = FIRST5_FTUE_CORE_LOOP_RECONCILIATION__VISUAL_EXECUTION_PAUSED
UNIT_ANIMATION_PRODUCTION_CONTRACT = RETAINED_GEOMETRY_ONLY__STYLE_FIT_REVIEW_REQUIRED
SHIELD_GUARD_CLEANUP_MASTER_PAIR = LEGACY_STYLE_FIT_REVIEW_REQUIRED
CURRENT_NEXT = PHASE2_OPEN_BATTLEFIELD_READINESS_REVIEW__ISSUE_RED_TEST_PROVENANCE_TARGET_RESOLUTION_REQUIRED
VISUAL_GENERATION_POLICY = USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
IMAGE_GENERATION = USER_AUTHORIZED_AUTONOMOUS_REQUIRED_IMAGES
GODOT_CODEX = RUN_COMMAND_VERTICAL_SLICE_IMPLEMENTED__MACHINE_QA_ACTIVE
```

`GITHUB_NOTION_DRIFT_CHECK = PASS`와 `FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5`는 2026-08-24 final-planning 시점의 보존 증거다. 2026-08-25 승인 이미지의 runtime/human 검증 PASS를 뜻하지 않는다.

`HISTORICAL_PRE_APPROVAL_GATE`는 2026-08-24 implementation 승인 이전의 과거 gate를 보존하는 호환 marker이며 현재 다음 작업이 아니다. 현재 gate는 열린 전장·탑 전용 배치가 반영된 v6 planning board를 사용자가 확정할지 검토하는 것이다.

`OMW-VISUAL-20260828-STORYBOOK-SD-THREE-FRONT-STRATEGIC-MAP-01` is the current presentation owner. It fixes the primary battlefield as one simultaneous strategic map with **one Ward Citadel root branching into three visible fronts**, using storybook watercolor SD visual language. Parallel rows or three independent Ward bases are rejected. The 2026-08-25 Decision retains only the protected three-front responsibility, battlefield-primary hierarchy, compact lower deck, and silhouette-first rule; the 2026-08-28 close-backdrop presentation is superseded while its roulette inspection behavior remains retained.

Current visual/handoff owners:
- `docs/superpowers/specs/2026-08-28-storybook-sd-three-front-strategic-map-design.md`
- `docs/design/APPROVED_OMENWARD_OPEN_BATTLEFIELD_TOWER_ONLY_FORWARD_LAYOUT_2026-08-28.md`
- `docs/images/planning/OMENWARD_PROJECT_CORE_SCENE_VISUAL_BOARD_2026-08-28.md`
- `docs/images/approved/OMENWARD_BATTLEFIELD_BACKDROP_V1.md` — legacy current-build consumer only
- `docs/superpowers/specs/2026-08-25-front-state-minimap-sd-fantasy-design.md`
- `docs/images/planning/canonical/OMENWARD_APPROVED_FRONT_STATE_VISUAL_2026-08-25.md`
- `docs/images/planning/OMENWARD_UNIT_ANIMATION_PRODUCTION_CONTRACT_2026-08-26.md`
- `docs/handoffs/2026-08-29-open-battlefield-v6-visual-lock-handoff.md`

Retained visual lineage/audit owner:
- `docs/design/APPROVED_OMENWARD_NORTH_STAR_V2_1_AUDIT_AND_CORRECTION_BRIEF_2026-08-24.md` (`OMW-PLAN-20260824-NORTH-STAR-V2-1-AUDIT-01`) — historical/partial reference where the 2026-08-25 Decision supersedes layout/style.

Retained final planning review owner:
- `docs/reviews/FINAL_PLANNING_ADVERSARIAL_REVIEW_AND_DRIFT_CHECK_2026-08-24.md` — `FINAL_PLANNING_ADVERSARIAL_REVIEW = PASS_5_OF_5` is retained planning evidence, not runtime or post-2026-08-25 visual validation.

Retained Run Command implementation authority remains separate from this completed visual receiver pilot:
- `docs/implementation/OMENWARD_RUN_COMMAND_VERTICAL_SLICE_EXECUTION_PACKET_2026-08-24.md`
- `docs/superpowers/plans/2026-08-24-run-command-vertical-slice.md`

## Current product core

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
징조 관측
→ 건설 / 동원 인장 / 확률 설계
→ 3×3 징조륜 결과 / 제한된 행·열 조작
→ 병력 획득
→ 세 전선 중 하나에 비가역 커밋
→ 자동전투 + 제한된 수동 전술
→ 인과 복기
```

## Current world / commander

```text
PLAYER_ROLE = Omen Warden / 징조수호관
PLAYER_FANTASY = 전조를 읽고 수호성을 준비하며 병력을 세 전선에 보내는 지휘관
COMMANDER_ROLE_ANCHOR = LONG_COMMAND_FLAG
DIRECT_HERO_MELEE_FANTASY = FORBIDDEN_AS_PRIMARY
VEIL = 적 종족 하나가 아니라 현실과 겹쳐지는 적대적 경계 현상
OMEN = 실제 공세 전에 나타나는 전조 / Pre-Echo
ONE_MAPRUN = ONE_WARD_CITADEL + ONE_20_STAGE_OMEN_CYCLE
BOSS_STAGES = 5 / 10 / 15 / 20
ELITE_ESCALATION = EVERY_STAGE_FINAL_WAVE
```

## Current UI / visual

```text
RUN_COMMAND_SCREEN = PREPARE -> COMMIT -> BATTLE -> REVIEW
VISUAL_STYLE = STORYBOOK_WATERCOLOR_SD_TACTICAL_ILLUSTRATION
UNIT_PROPORTION = 2.5_TO_3_HEAD_SD_TACTICAL_MINIATURE
MATERIAL_FINISH = IVORY_PAPER + DELICATE_INK + SOFT_WATERCOLOR + RESTRAINED_PIXEL_TACTILITY
WORLD_TONE = FANTASY_WARD_CITADEL + MAGIC_WARFARE

BATTLEFIELD_PRESENTATION = ONE_SIMULTANEOUS_THREE_FRONT_STRATEGIC_MAP
THREE_FRONT_VISIBILITY = REQUIRED
PER_FRONT_MINIMAP = ABSORBED_INTO_PRIMARY_STRATEGIC_MAP
MINIMAP_IS_CONTEXT_NOT_SECOND_BATTLEFIELD = TRUE
UNIT_BY_UNIT_MINIMAP_REPLICATION = FORBIDDEN
LONG_FULL_ROAD_PRESENTATION = SUPERSEDED_AS_DEFAULT

NORMAL_COMBAT_UNIT_RULE = SILHOUETTE_FIRST
PRIMARY_VISUAL_MASS = BATTLEFIELD
SECONDARY_VISUAL_MASS = LOWER_CONTROL_DECK
ROULETTE_EXPOSURE = 3×3
ROW_COLUMN_ARROWS = PROMINENT
NORTH_STAR_V2_1 = HISTORICAL_REFERENCE_ONLY
CURRENT_TARGET_RUNTIME_ASSET = NOT_CREATED
LEGACY_RUNTIME_BACKDROP = OMW-IMG-20260828-BATTLEFIELD-BACKDROP-V1
PROJECT_CORE_SCENE_VISUAL_BOARD = USER_CONFIRMED_PLANNING_LOCK__V6_OPEN_BATTLEFIELD_NO_BARRICADE__NOT_RUNTIME_ASSET
```

Faction language retained:

```text
ALLY = NAVY + IVORY + COOL_GRAY_METAL + RESTRAINED_GOLD
ALLY_SHAPES = ARCH + SHIELD + BANNER + RELIC + VERTICAL_LINES
VEIL = BLACK_PURPLE + DARK_RED + CARAPACE_GRAY + LIMITED_RIFT_GLOW
VEIL_SHAPES = ASYMMETRIC_RIFT + CARAPACE + SPIKE + VOID_APERTURE
```

Front-State information split:

```text
FRONT_STATE_VIEW = CURRENT_UNITS + CURRENT_THREAT + CURRENT_CLASH + COMMIT_OUTCOME
PER_FRONT_MINIMAP = FRONT_PROGRESS + STRONGHOLD + ROUTE + INFILTRATION/AIR + BOSS/SIEGE_CONTEXT
```

## Approved visual asset

```text
IMAGE_ID = OM-IMG-023
IMAGE_STATUS = USER_APPROVED_HISTORICAL_REFERENCE_ONLY
FULL_RESOLUTION = 1536x1024 PNG
DRIVE_FILE_ID = 1-JRf4q95wZm51DsEYPH_-hnH_GLEIAQ5
SOURCE_SHA256 = 0326b012d1fbefba85b545086b84992051591edff6f3b7e159cf3e083f204224
NOTION_HOME_INLINE_PREVIEW = PASS_SERVER_READBACK
NOTION_VISUAL_BIBLE_INLINE_PREVIEW = PASS_SERVER_READBACK
```

Human surfaces:
- Project Home: https://app.notion.com/p/3c41b237eb1c816fbbc8e2dddc18b6eb
- Visual Bible: https://app.notion.com/p/3c01b237eb1c81c38be5e3ee9f64b59d
- Visual Components: https://app.notion.com/p/3c21b237eb1c81e29be2d6ce397c9c85

Notion server readback proves a historical image block/attachment existed; it is not current authority or a browser/device usability PASS.

## Runtime / evidence boundary

```text
CURRENT_GODOT_RUNTIME = PARTIAL__RUN_COMMAND_UI_TECHNICAL_SMOKE_AND_THREE_RESOLUTION_CAPTURED
CURRENT_WINDOWS_RUNTIME = PARTIAL__STANDALONE_TECHNICAL_CAPTURED_960_1280_1920
CURRENT_UI_EVIDENCE = PARTIAL__RUN_COMMAND_PREPARE_TO_BATTLE_LIVE_CAPTURED
CURRENT_MINIMAP_READABILITY = PARTIAL__THREE_RESOLUTION_TECHNICAL_CAPTURED__HUMAN_NOT_RUN
CURRENT_SD_UNIT_RUNTIME_READABILITY = PARTIAL__ALL18_UNIT_GALLERY_NO_CLIPPING_SIGNAL
CURRENT_GUT_RED = NOT_RUN
CURRENT_GUT_GREEN = NOT_RUN
CURRENT_HERA_LIVE_QA = PARTIAL__RUN_COMMAND_PREPARE_TO_BATTLE_MOUSE_AND_UI_ACCEPT_KEYBOARD__DIAGNOSTICS_CLEAN
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
```

## Current screen-surface coverage owner

`docs/design/OMENWARD_GAME_SCREEN_AND_IMAGE_COVERAGE_2026-08-28.md` is the current screen-first companion audit for the scoped Run Command vertical slice. It maps the actual default route and all relevant/not-applicable player-facing families to runtime consumers, approved local assets, Godot UI/procedural rendering, and evidence. It does not replace the visual Decision, asset manifests, or runtime evidence owners.

```text
SCREEN_INVENTORY_HANDOFF_READY = TRUE
IMAGE_GENERATION_FROM_AUDIT_GAPS = FORBIDDEN
NATURAL_TUTORIAL_BATTLE_TO_REVIEW_HEADLESS = PASS
LIVE_HERA_REVIEW_CAPTURE = NOT_RUN
HUMAN_PLAYER_EVIDENCE = NOT_RUN
```

Visual approval is not runtime proof. The visual closeout does not authorize final economy/balance values or claim implementation completion.

Machine-QA evidence owner: `docs/qa/OMENWARD_RUN_COMMAND_MACHINE_QA_2026-08-27.md`. It records technical layout and interaction capture only; human/player evidence remains `NOT_RUN`.

## GitHub routing

```text
CURRENT_OPEN_PRS_AND_ISSUES = FRESH_GITHUB_QUERY_REQUIRED
```

Unrelated open/draft work remains read-only. Fresh GitHub state overrides handoff PR numbers if they later change.

## Current work order

```text
1. COMPLETE — existing world/story/content/balance envelope/Text UX
2. COMPLETE — retained 3×3/token/lower deck/roulette DDD contracts
3. SUPERSEDED_IN_PART — old Anime Pixel/Clean Pixel + long-road battlefield default
4. COMPLETE — Front-State + per-front minimap + Fantasy/Magic/SD Decision
5. COMPLETE — written spec + alternatives + planning adversarial review 5/5
6. COMPLETE — OM-IMG-023 historical visual approval retained as reference only
7. HISTORICAL — Notion Home/Visual Bible image placement + server readback; future Notion writes retired
8. COMPLETE — durable GitHub visual asset record + new-chat handoff
9. COMPLETE — Shield Guard shared UnitView idle texture consumer import contract
10. COMPLETE — reconcile remaining approved P0 asset geometry and extend shared runtime consumers
11. PARTIAL — live tutorial plus all-18 gallery captures show the shared renderer without an automated clipping signal; broad interactive readability and human evidence remain `NOT_RUN`
12. COMPLETE — derive and bind General Barracks, Defense Tower, and Farm compact thumbnails to the three existing Stage HUD build-action buttons
13. COMPLETE — P1 structure-consumer discovery found no current scene/data receiver for the four source-only building masters; no inferred placement or rule was added
14. COMPLETE — bind approved Gold and Troop Capacity derivatives to the current Stage HUD resource indicator
15. COMPLETE — screen-first visual coverage audit; no asset-generation work inferred from its gaps
16. COMPLETE — user locks storybook watercolor SD and one simultaneous three-front strategic-map UI; planning board generated
17. NEXT — user confirms the v6 open-battlefield planning board before a Visual Direction Lock Packet and Phase 2 UI/implementation readiness review
```

## Resume order

1. fresh Base current authority and open PRs;
2. fresh OMENWARD main/open PR/Issue inventory;
3. `AGENTS.md`;
4. `docs/CURRENT_CONFIRMED_DECISIONS.md`;
5. this file;
6. `docs/handoffs/2026-08-29-open-battlefield-v6-visual-lock-handoff.md`;
7. `docs/images/planning/OMENWARD_UNIT_ANIMATION_PRODUCTION_CONTRACT_2026-08-26.md`;
8. current visual spec + approved asset record;
9. repository의 current visual spec / planning board / asset provenance owner;
9. current GDD/Project Core and relevant owner, treating older conflicting visual wording as superseded by the 2026-08-25 Decision;
10. Google Sheet as compatibility/history only;
11. Shield Guard, the remaining P0 unit imports, and the three current HUD building-button imports are verified. Live tutorial, all-18 gallery, and button captures are partial; broad runtime readability and human evidence remain `NOT_RUN`.

The user currently authorizes autonomous required-image production and scoped Codex/Godot continuation. Any runtime readability or human-play PASS still requires actual recorded evidence.
