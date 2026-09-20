# [현행] OMENWARD Active Context

2026-09-20 원격 마감: 구현 d0658c5b + 증빙 경로 교정5e2eb337에서 원격6개 PASS, 로컬/origin 차이0/0. 첫 원격 실패2건은 로그 경로 범위 문제였고 허용목록 확장 없이 외부 기존 증빙 owner로 이동해 해결했다. PR259/부모258 Draft 유지, main90493888 그대로. 아래 로컬 시험과 경로 교정 근거를 함께 읽는다.

2026-09-20 저장 교정 최종 로컬: 모델715/저장61/화면/기본씬 PASS, 정책 집중255 및12조합 저장 재개 일치. scope9/스킬4 PASS, Base raw FAIL/scoped PASS 분리. 독립 검토2/2와 P3 한정 교정 완료. 증거·정리/복구 위치는 기존 실행 계획 상단, GitHub exact-head 판정은 PR259 Checks로 확인한다. main 병합·새 GPU·사람 재미·최종아트/출시 완료 아님.

2026-09-20 연속 교정: 첫 맵4정책×3seed 비교에서 저장 숫자 정밀도 손실로5조합의 이후 전투 결과가 달라지는 결함을 재현했다. 검증 저장 writer에 full_precision만 적용해 규칙·스키마·구형 읽기를 보존한다. 실제 디스크 저장/재개의 최종 상태 비교와 위치/HP 정확 동등성 회귀를 추가했다. 현재 결과/최종 검증은 [기존 실행 계획 상단](superpowers/plans/2026-09-11-visible-battle-slice.md#2026-09-20-연속-작업--첫-맵-정책-비교저장-재개)을 따른다. 1948의 네 정책 패배는 조사 후보이지 임의 난이도 변경 근거가 아니다. 다음 P04 비재귀 사건·남은 등급 효과 순서 유지, 사람 재미 NOT_RUN. 이하 마감 수치는 앞선 묶음 이력이다.

2026-09-20 마감: 부모8810ae00 원격10 PASS/1조건부SKIP(동일 HEAD Godot native 종료 실패1회 후 재실행 PASS), BUILD e5a5bb92 원격6 PASS와 로컬=origin 확인. 검토 finding은 한정 재확인으로 해결. 실제 main90493888은 변경하지 않았다. 아래 검토 완료와 사람 재미/출시 완료를 혼동하지 않는다. 누적 일지 원본 및 복구 가능한 시험파일40개의 정리 위치는 기존 계획의 9/20 마감 절에 연결했다. PDF는 이번에 재발행하지 않았다.

2026-09-20 첫 맵 정보 검토: 다음 공세의 북부/중앙/남부 배정 수와 선택 전선 병종을 실제 출현 순환 규칙에서 읽기 전용으로 표시한다. 기존 구형 저장의 전체 예보는 유지한다. 첫 맵은 시작 자원 그대로 병영 건설→징조륜→전선 분산 배치→실제 미니맵 클릭/확대/복귀→재정비2회→3라운드 본진 점령 승리를 GPU로 확인했다(251G, 아군 본진1000). 고정 시계 가속 자동 정책이며 인간 재미·밸런스 통과 아님. 모델/저장59/화면/기본씬 gate PASS, 기획63+BUILD scope9 Python 검사 PASS. 원본 Base 보호경로 FAIL과 승인 PROJECT_SCOPED_BUILD PASS를 구별한다. 독립 검토의 준비 모드 우선순위 P2는 8810ae00에서 반례 회귀로 교정했다. 실제 계획/증거는 `docs/superpowers/plans/2026-09-11-visible-battle-slice.md` 9/20 절. PR258/259는 Draft, main 미병합. 다음: 3전선 선택 이유의 사람 관찰 + 첫 맵 반복/다른 정책 확인 후 P04 잔여 계약 순서; 신규 아트/규칙 조정은 이번 범위 밖이다.

> 2026-09-20 현재 승인 작업: [통합 준비·첫 맵 검토](design/OMENWARD_REPLAN_AND_MOTION_INTAKE_2026-09-10.md#2026-09-20-승인된-통합-준비와-첫-맵-검토). 이 planning 브랜치와 후속 BUILD PR259를 구분한다. 현행 제품 방향은 3전선 동시 진행 / 기본 전체 미니맵 / 선택 전선 확대이며 아래 단일전선·구현 보류 기록은 역사다. 실제 최신 구현·시험 근거는 PR259의 기존 visible-battle 계획에서 읽는다. 이번 준비가 전체 PR 병합·최종 자산 승인 권한을 추가하지 않는다.

> 2026-09-20 운영 개선: [Base 선택 채택·재미 검증 연결·작업 순서](BASE_RULES_VERSION.md). v9.4.3 lock과 기존 제품 승인/구현 상태는 유지한다. 최신 게임 작업 브랜치를 main 구현 완료로 간주하지 않는다. 운영 진척과 검증은 이 링크에 누적한다.

2026-09-16 마무리 readback: 구현33c61fb7 원격 CI5 SUCCESS, 작업 브랜치 local/origin 차이0/0 확인. 기존 미제출 월간PDF v0.2에 E11 당일 요약/실제 화면2쪽을 누적해14쪽으로 갱신(새 v0.3 생성 없음). 이전12쪽 추출 텍스트 보존, 추가2쪽 렌더 시각 검수. SHA bbe47fe27906d08d8b3400e3cd979227a2b7b50cd1714ccc823dbdcd58be684a. 사용완료 저장검사3폴더60파일214254bytes는 `Downloads/OMENWARD_DELETE_REVIEW_20260912/three-front-tests-20260916`로 해시검증 이동; 이전PDF 복구사본/렌더도 그곳에 보존, 직접삭제 없음. PR259는 부모 기획브랜치 대상 Draft 유지, main 미통합. 이번 사용자 요청은 기능 연결·당일 누적·작업브랜치 동기화로 마무리하며 최종 아트/전체게임 완료로 표시하지 않는다.

2026-09-16 최신 사용자 요청 구현: 신규 three_v1 원정은 3전선 동시 진행·기본 전황 미니맵·경로 클릭/버튼으로 선택 전선 확대·전체 복귀. 시계/경제/양측 본진은 공유하고 공격·치료·점령·탑은 전선별 분리한다. 각 중앙 거점/탑1개, 초기병력2/1/1, 기존 공세 총량 순환분배. 선택은 미래 출전 목적지만 변경한다. JSON front_layout을 모델이 소비한다. 구형 single 저장은 기존 규칙과 3거점 확대 화면을 유지하며 자동 분할하지 않는다.

최종 로컬 모델455/저장59/UI·기본실행 PASS, scope7/docs PASS. Base 원검사는 기존9보호경로 FAIL, 승인된 PROJECT_SCOPED_BUILD PASS로 분리한다. 독립5관점 검토의 직접치료 교차전선 및 legacy 기본화면 거점누락을 RED→GREEN으로 교정했다. GPU 실제 중앙 경로 좌표 클릭→확대→복귀 및 선택 외 전체 snapshot 불변 PASS; output/front-overview.png / front-inspection.png 직접 시각 검수. 도식 미니맵은 기능 UI이며 최종 지형아트/3전선 전체 밸런스/Human/출시 PASS가 아니다. P04 잔여등급→P05 영웅→P06~P09는 남는다. 현재 요청의 마무리는 기존 미제출 월간PDF에 날짜별 누적 및 현재 PR259 작업 브랜치 동기화이며 부모/main 통합은 별개다. 새 Base 승격은 없고 프로젝트 회귀검사에 교차전선·legacy 표기·실제 입력 경계를 보존했다.

2026-09-14 증빙집 추가 발행: 지정 9월 폴더에 v0.2 12쪽(후속 E06-E10 4쪽+원문v0.1 8쪽)을 발행하고 모든 페이지를 렌더 검수했다. 사후 기록·개별입력/계정/비용 미확인·미제출 유지. 기존v0.1 보존, 새v0.2 SHA e51f5e2dbef0c06f1129b3e9fa87b5036cc73423984afbe023d29994f936484b. 사용완료 저장검사9폴더161파일550500bytes는 삭제검토 폴더로 해시확인 이동만 했다. P04 교정5a9a3339의 exact-head CI5 PASS, main/부모 통합은 미실행. 게임 후속은 아래 P04→P05 순서 그대로다.

2026-09-14 P04 범위 타격 교정: 대검의 추가 타격은 전방만, 마법사/대검의 제한 대상은 주표적 거리→숫자 ID로 결정한다. 실제 units 배열은 재정렬하지 않는다. 독립5관점 검토의 구형 소수ID 절삭 결함을 RED→직접비교→GREEN으로 교정. 최종435모델/55저장/화면/기본실행 PASS; 이번 교정의 GPU/Human은 NOT_RUN. 직전 T3 커밋0369c217 exact-head CI5 PASS 재확인. 다음은 P04 남은 등급 proc와 비재귀 사건/저장 계약이며 전체 P04 완료 아님. E08/E09 사후 증빙 추가 기록을 지정 외부 원본근거 폴더에 작성했지만 PDFv0.1은 덮어쓰지 않았다.

2026-09-14 T3 연결: 신규 birth_v2에서 T2 동일병종 심화(첫맵6라운드/이후맵 유지, T2가격1.25배 올림)·신규 생산/징조·10병종 capstone·내정 구매/설명 연결. v1 원정의 T3는 자동 해금하지 않는다. 최종426모델/55저장/화면/기본실행 PASS, docs/scope7 PASS. 독립5관점 지적의 경직 중 비행 재접촉과 타워 원거리 방어 누락을 RED→GREEN; 효과상한·역할/구형주입·8초재준비/양진영 기본 검사 보강. GPU front-tier3는 명시적 후반 라운드 fixture에서 실제구매→생산→출전 T3 보존을 확인한 것이며 자연6라운드/최종Human 아님. 기존 GPU 전투12피해13병력/방패3자세/혼합10피해/상태효과 유지. 다음 P04 나머지 숙련·정예와 추가타 계약, P05 영웅/P06~P09 UI·아트·완주·출시 경계 남음. 새 아트 생성 없음.

2026-09-14 P03 출생정보 증분: 신규 birth_v1의 고유 시설/병력 ID, 출생tier/source 보존을 생산→징조확정→정확 출전→JSON/맵기록에 연결했다. 최저티어 토큰 보너스, 선입순 대기 카드와 확정 전 티어 표시. 최종391모델/55저장/화면/기본실행 PASS, scope7/docs PASS. 독립5관점 검토에서5개 저장경계 결함을 재현·교정 후 차단 결함 없음; 추가 checkpoint 미래카운터 RED→GREEN. GPU 기존 전투12피해13유닛/방패3자세/혼합10피해/상태효과 및 징조 티어 표시 확인. T3는 아직 잠겨 있고 실제 심화효과 미연결. 구형 저장은 기존 프로필 보존, 신규 아트 없음. 다음은 P03 T3 비용/gate/생산 뒤 P04 실제효과. 전체원정/Human/main 미완료, PDF0.1은 이전 발행본이다.

2026-09-14 P03 T2 gate 후속: 신규 slots_v1 원정은 첫 맵 1라운드 재정비부터 T2를 해금하며 다음 맵 1라운드에서 다시 잠기지 않는다. Blueprint facility_progression.specialization_round를 모델과 UI 공통 판정이 소비한다. 구형 원정의 기존 gate는 보존. 올바른 시설 id의 모델/실제 버튼 RED→GREEN, 최종 모델368/저장51/화면/기본실행 PASS 및 독립5관점 검토 차단 결함 없음. 이번 증분의 GPU 별도 재실행은 없으며 위 고정슬롯 GPU 증거와 구분한다. T3·출생정보 및 자연5맵완주/Human/main 통합은 미완료.

2026-09-14 P03 고정슬롯/철거 증분: 신규 slots_v1 원정에 무환급·확인창·첫해금빈칸 재건설·빈칸 저장을 연결. 잠긴7번시설을 앞칸 철거로 이동시키지 않으며 기존 병력/확정대기 보존. 모델366/저장51/화면/기본실행 PASS, 독립5관점+최종 재검토 차단 결함 없음. stale 확인창이 같은 값의 복원시설을 철거하던 UI 회귀를 RED→참조 동일성 검사→GREEN으로 보강했다. GPU 확인창 캡처/취소 무변경, 전투12피해13병력/방패3자세/혼합·상태 재확인. 기존 v7 logistics_v1/legacy 보존. T3·출생정보·최종UI/Human/main은 미완료. 원본근거에 이번 검사 로그를 추가하며 기존 월간PDF0.1은 과거 snapshot으로 보존한다.

2026-09-14 증빙 발행 마감: 지정9월 폴더에 `OMENWARD_2026-09_AI활용_작업일지_증빙집_v0.1.pdf`8쪽과 `OMENWARD_원본근거`를 작성했다. 확인된9월14일5패킷만 포함하며 사후 기록/정확한AI시각·계정·개별입력화면·비용연결 미확인/미제출을 명시했다. 전페이지 렌더 검수와 텍스트·페이지 검사 PASS. 원본협약 확인·제출·서명 없음. 코드8e159525는 로컬=작업원격 및 exact-head CI5 SUCCESS; main/부모통합은 아님. 아래 ‘발행 준비’는 이전 상태다. 신규 아트 제작은 없음. P03 다음 고정슬롯·철거·T3·출생정보부터 기존 순서를 유지한다. 사용완료 저장 fixture3폴더는 해시대조 후 P03-tests-20260914 사용자 삭제검토 폴더로만 이동했다.

2026-09-14 재개: P03 군수소 증분은 활성 시설당 수용량+6, 비생산/비룰렛 시설, 슬롯 잠김 시 효과 비활성 및 기존 병력 보존, legacy/미래 저장 보호를 구현했다. 모델349/저장51/화면/기본 실행 PASS, 독립5관점 재검토 차단 결함 없음. 화면 카드의18고정 결함은 실제18→20 출전 회귀로 교정했다. P03 전체(T3·출생정보·철거 등)는 미완료다. 최신 사용자 추가에 따라 앞으로 크로마키→배경제거→alpha QA를 적용하며 이번에는 신규 이미지를 생성하지 않는다. 별도 월간 AI 작업 증빙집을 지정 외부 폴더에 발행 준비 중이며 커밋/검사/기존 캡처를 원본 연결한 사후 정리로 구분한다. 청구·제출·협약/계정 원본 확인·Human·main 통합은 미실행이다. 이하 완료 수치/현재-next는 해당 시점 이력이다.

P02 최종 증분 검사: 모델339/저장47/화면/기본headless PASS, 최종 독립5회 정적 재검토 차단 결함 없음. 시간제 점령·본진 claim·기본보급 정산 및 타워 사망 우선·구형 저장 호환 연결 완료(국소 증분). 다음은 P03 시설/군수와 출생정보. 임시검사91파일은 사용자 삭제 검토 폴더로만 이동/해시검증했고 실제 저장은 보존했다. 전체게임·최종아트·Human·main 통합은 완료가 아니다.

2026-09-14 후속 P02: 신규 원정 시간제 점령/자동 확보대기/중앙탑 소유/본진 최종점령/잔여기본보급1회 정산과 UI 진행률 연결. 구형 rules marker는 보존하며 checkpoint/ledger 교차 검증을 보강 중이다. 실제 GPU 전투12피해/13유닛·방패3자세·혼합/상태 fixture 확인. 모델338/저장47까지 PASS 후 타워 사망→점령 순서 회귀를 추가해 전체 재검증 중. 전체 캠페인/최종UI·아트·Human/main은 아직 아니다. 남은 작업은 현재 실행 계획 P03 이후 및 명시 P01/P07 후속 consumer를 따른다.

2026-09-14 연속 구현 위임: 사용자가 P00–P09 명세 순서의 전체 구현·개선 루프를 다시 명시했다. 계획-only 상태는 이력이며 일상 기술 선택의 추가 승인을 요청하지 않는다. 현재 P01 새 원정 fixed30-v1 시계·정수 동작 duration 저장·1×/2× UI 연결을 검증 중이다. v1–v6는 기존 적분/공세를 다음 맵에서도 유지한다. P01 전체 사건 순서·catalog 식별·이후 점령/보상/영웅/전체UI/아트/완주까지 완료했다는 뜻은 아니다. 검증의 최신 결과는 실행 계획의 후속 증분 절에 기록한다.

2026-09-14 구현 재개: 사용자 승인에 따라 P00 owner routing 및 P01 첫 저장 증분 연결. 파일 교체 전 temp 재읽기/모델 검증/해시 대조, 이전 정상 backup, 손상 원본 보존 및 primary/backup 미래형식 차단 구현. 모델268/0실패, 저장43/0실패, 화면 복구·재저장 및 기본 headless 실행 PASS, scope7 PASS. 독립5회 정적 검토의 미래형식·미래backup·현재상태 지적 수정 후 재검토 완료. Base raw FAIL/scoped PASS 구분. 30Hz 정수 시계/v7 전환은 다음 P01 증분이며 기존 v1–v6 전투 규칙은 미변경. 아래 계획-only는 이전 턴 이력. 전체원정/Human/main 통합은 미완료. exact 원격 상태는 PR 최신head로 확인한다.

2026-09-14 최신 작업은 사용자의 ‘남은 작업과 구현·설계 명세 준비’ 요청에 따른 계획 전용이다. 현 코드496bc3b1/Blueprint/main·PR 중첩/Base를 대조하고 [기존 실행 계획의 2026-09-14 절](superpowers/plans/2026-09-11-visible-battle-slice.md)에 P00~P09 잔여 명세를 통합했다. 현재 우선순위는 정본 routing 정합성→고정 시계/저장→점령/정산→군수/T3→남은 효과/영웅→화면/아트/전체원정 검증이다. 즉시점령·HP0즉시승리·가변step·용량18고정과 명세의 차이를 확인했다. 게임 코드/JSON 수치/이미지는 이번에 변경하지 않으며 새 기본값은 권장안이지 사용자 최종확정이 아니다. 아래 과거 ‘다음’ 문장과 단계는 이력으로 읽는다. 신규 모듈은 착수 때 exact scope 추가가 필요하고 Base lock/main 통합/최종Human 경계는 유지한다.

2026-09-13 공통 효과 후속: 보호막 선흡수/비합산, 독립 만료 둔화의 최강값/이동50%하한, 경직 미발사 취소/종료후1초면역을 기존 전투시계에 연결. 숙련 방패4타/기병돌격 경직, 숙련 마법사15%둔화, 사제3회치료 단일최강둔화정화/정예 과잉치료보호막 소비처 구현. optional 저장 검증과 맵초기화, tooltip 실제효과 표시. 독립5관점 검토에서 정화 전체제거/부분돌격 경직유지 두 결함을 RED→수정했고 취소공격 저장 불변식도 보강. GPU 상태 편성 실제0.25초에서 보호막7/경직0.3/이동0.85 확인; 일반 성장·획득/밸런스 증거 아님. 나머지 병종 숙련/정예, 보호막 전용 아트·전체 모션/T3/영웅/자연5맵완주/Human 미완료. Base lock 유지, 프로젝트 한정 BUILD 경계 유지.

2026-09-13 투명화 후속: Ward 일반/특수 및 시설8종은 RGB 보존 RGBA 파생본으로 소비 경로 변경. 방패 기존4프레임/베일10종 유지. Python7검사, Godot242모델/화면/저장/기본실행 PASS 및 GPU 혼합10병력·10피해 확인. 첫 실행은 미등록 이미지 오류가 있었으므로 PASS로 인정하지 않았고 import 후 재실행; 검증기가 엔진 ERROR도 실패 처리하도록 보완. 시설 atlas y407 분할로 다른 행 십자가 침범 교정. 이번 파생본 Aseprite 미사용/새 모션 없음; 내부 종이색·좁은 셀·일반 UI 대체 아이콘 및 전체 모션은 잔여. 전체 게임/Human/main 통합 미완료.

성장 후속: 생존2/5회 숙련/정예 판정과 저장·맵 계승·재도전 rollback 연결. 기본HP/공격 일괄배수 없음. 숙련 궁병 동일대상 매3타1.25/숙련 대검 첫대상1.2를 첫 소비처로 연결했다. 모델242/0실패, 화면/저장/기본실행 PASS; 두 번째 사격 저장→복원→세 번째 보너스 검사 포함. GPU 기존 전투/혼합/캠페인 캡처 갱신, 실제 숙련 전용 장면 검증은 별도 미실행.5관점 정적 검토 차단 결함 없음. 다른8병종 숙련/전 병종 정예 특수효과는 미연결; 다음은 공통 보호막/둔화/경직 계약을 구현해 연결하며 T3/영웅에 재사용. 전체 게임·자연5맵완주·최종Human 미완료.

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

1. `AGENTS.md`의 current-authority read order;
2. fresh OMENWARD main/open PR/Issue inventory;
3. below owners, actual consumers, then selected Base contract/latest drift;
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
