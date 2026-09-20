# Visible battle and construction implementation plan

## 2026-09-20 P04 연속 실행 — 관통·저지·반격

기존 P04/Blueprint unit_progression의 궁병 정예5타 뒤1체50%, 창병 숙련 돌격 저지 둔화30%/1초·정예 즉시1타/6초를 연결한다. 기존 front_run/front_save/front_screen, Blueprint JSON, 세 replan test와 기존 상태 기록만 수정한다. 수치 owner는 JSON `grade_proc_rules`로 구조화하며 이미 명세된 값을 새 밸런스 확정으로 표시하지 않는다.

순서/합격: (1) 실제 전투 회귀 RED (2) 새 원정 proc_v1 표식과 동기 BASIC/SECONDARY/COUNTER 처리 (3) 궁병 거리→ID 후방 선택·창병 저지 소비 (4) 저장/미래 표식/맵 진입 교차 검사와 tooltip 연결 (5) 전체 gate·현재 PR exact scope·원격 확인. 양진영, 전선 격리, 죽음/아군/경직/잘못된 ID, 중복1000회, 관통 직전/반격 재사용 중 저장을 시험한다.

Ruling: 기존 즉시 처리에 범용 이벤트 버스·새 모듈을 만들지 않는다. BASIC은 기존 공격 consumer에 연결하고 SECONDARY/COUNTER는 피해만 처리해 기본 적중 카운터·추가 발동을 재실행하지 않는다. 단조 증가 event_id를 저장하고 완료한 ID 재입력은 거절한다. 자식은 현재 동기 기본 공격 안에서만 허용; 비동기 투사체/순서 재배열 queue는 아직 소비처가 없어 후속 P07로 남긴다. 저장은 이벤트 전체 처리 사이에서만 가능하다. 틀린 가정이 확인되면 비동기 consumer와 함께 queue/ledger를 확장해야 한다.

호환: 새 3전선 원정 생성 시 proc_v1, 기존 marker 없는 원정은 legacy 유지. 미래 표식은 primary/backup/map-entry에서 fail-closed. 새 카운터·시간은 저장하고 맵 전환 때 일시 효과/횟수 초기화, 사건 순번은 원정 안에서 유지한다. 이미 시작한 구형 원정에 능력을 몰래 추가하지 않는다. 방어 성공 시 생존한 창병의 반격은 해당 기본 공격의 후속 경직 적용 전 해결하며 사망/기존 경직/반격 대기 중에는 발동하지 않는다.

경험 가설: 살아남은 정예 궁병이 밀집 후열을 관통하고 준비한 창병이 돌격을 억제해 병종/전선 선택 이유를 만든다. 반례는 다른 전선의 피해·추가타의 무한 발동·불러오기 후 재충전·툴팁과 효과 불일치. 모델→HP/flash/action·대기 tooltip가 현재 표현 consumer이며 새 최종 VFX/아트·사람 재미는 NOT_RUN이다. 공식 Godot JSON 숫자 타입/정밀도와 Array의 참조/정렬 제약을 적용한다(위 P04 공식 출처 및 https://docs.godotengine.org/en/stable/classes/class_json.html). 기존 장르 조사/역할 명세를 재사용하고 장르·핵심 규칙을 재설계하지 않는다.

프로세스: 현재 AGENTS·Base23ecad5a 선택 채택/v9.4.3 lock 확인, BUILD scope PASS/Base raw 보호경로 FAIL 분리. 전체 검토 예산2/2는 계승하며 초기화하지 않는다. 이번 증분은 작성자 경계 검토·새 실패 회귀·원격 검사로 확인하고 과거 독립 검토를 새 코드의 검토로 주장하지 않는다. 기존 작업계획/월간 원본에 누적하고 신규 작업일지/스킬/전역 설정은 만들지 않는다. 현재 Hera는 urban-legend이므로 명시 OMENWARD CLI만 실행한다.

### P04 이번 증분 검증 결과

RED→GREEN: typed resolver 미구현, 사거리 밖 BASIC 수락, 새 효과 tooltip 누락을 각각 검사로 확인한 뒤 교정했다. 최종 효과 집중64 실패0, 전체 모델779/저장66 실패0·화면/기본씬 PASS. 첫 전체773 이후 맵 전환/재도전/저장 후 중복 입력6개를 추가하고 전체779를 다시 실행했다. Python 문서/범위97 PASS, 스킬4개 PASS. 첫 Python 호출은 존재하지 않는 모듈명을 지정해89중1 import 오류였고 실제 tests.test_replan_scope로 교정한97개 실행과 구별한다. 원본 Base 보호9 FAIL / 승인 PROJECT_SCOPED_BUILD PASS 유지, 커밋 후 정확한 PR 경로 검사를 별도 수행한다.

실제 Godot4.7.1 GPU tests/replan_capture.gd -- --procs-only: 새 원정에 의도적으로 정예/충전 상태를 준비하고 실제 advance_ticks(1)을 소비했다. 관통 표적172.741935483871, 돌격자151.440677966102, 창병 반격재사용6.0 확인. 실제 마우스 hover의 반격 tooltip 포함 output/front-status.png를 시각 검수했다(SHA256 a933d5d6d555887251d5323f76bb3ee45f98f5c209b317b855c18c21a907b6ab). 이는 자연 성장 획득·전체 밸런스·최종 모션/Human 검증이 아니다. 기존 투명 아트 재사용, 새 래스터/Aseprite 없음.

전체 자동 로그는 기존 월간 원본 C:/Users/user/Documents/증빙서류/9월 증빙서류/OMENWARD_원본근거/20260920_grade_procs_validation.log에 두 실행을 누적했다(SHA256 783ff2b8743f6738fa11d01fe6f31025581d085648bef015c7a97d0680a84309). 신규 PDF/지원기관 제출 없음. 다음 P04는 방패 인접보호→마법사/대검→기병/거인/암살자/비행 및 T3 교차검증이다. 아래 P04 표의 궁병·창병 행은 이 증분으로 구현됐고 나머지 행은 미완료다. Draft PR259 동기화만 이번 범위이며 부모258/main 병합 권한으로 확대하지 않는다.

## 2026-09-20 연속 작업 — 첫 맵 정책 비교·저장 재개

최신 진행 승인으로 직전 묶음의 다음 순서를 실행한다. 분산/북부집중/궁병특화/일반특수혼합 × seed1947~1949를 정상 초기 자원·실제 시설/징조/배치/공세 명령으로 비교한다. 정상 연속 실행과 첫 라운드22초의 JSON 저장 복원을 대조해 모든 최종 상태가 같은지 검사한다. 승률 자체에 합격선을 붙이지 않으며 결과를 보고 수치를 임의 변경하지 않는다. P04 잔여 효과는 기존 아래 명세/순서를 유지하며 이번 비교 결과를 먼저 읽는다.

경험 F1/F2 반증의 기술 관찰만 확장한다. 인간의 전략 선택/자기보고/반복 피로는 NOT_RUN. 완료 기준: 모든 표본이 제한된 첫맵 시간 안에 종료, 저장 재개 일치, 규칙/실사용 저장/다른 프로젝트 보존, 기존 gate와 원격 정확한 HEAD 확인. Ruling: 작업별 문서/스킬/서버를 새로 만들지 않고 이 계획·기존 모델 테스트를 누적한다. 기존 전체 검토1/2를 계승하여 마지막 검토로 이 연속 증분을 확인한다. 다른 프로젝트 Hera 세션에는 연결하지 않고 명시 project path의 Godot CLI만 실행한다.

### 정책 비교에서 발견한 저장 결함과 교정

실제 비교에서 기본 JSON 정밀도로 저장한 12조합 중5조합은 연속 실행과 최종 HP/공격횟수/적 잔존 상태가 달랐다. production `front_save.write_verified/read_verified`에 위치12.123456789012345와 HP179.12345678901235를 통과시킨 회귀도61검사 중1실패(RED)했다. 원인은 기본 `JSON.stringify`의 float 출력 자리수 손실이었다. **ADOPT** [Godot 공식 full_precision 계약](https://docs.godotengine.org/en/stable/classes/class_json.html#class-json-method-stringify): writer에 `full_precision=true`만 지정한다. **REJECT** 전투 좌표/피해 반올림, 스키마 변경, RNG 재추첨, 임의 밸런스 조정. 기존 파일은 계속 읽되 이미 반올림된 옛 값의 원래 정밀도를 복구했다고 주장하지 않는다.

정책 회귀는 임시 serializer가 아니라 실제 검증 저장 경로를 사용한다. 최종 snapshot 숫자 비교 허용오차는1e-9이며 별도 저장 회귀는 위치/HP의 정확한 동등성을 검사한다. 시간/난수/공세·큐·점령·시설·병력 상태도 비교하고 종료 때 특화/혼합 시설의 실제 존재를 확인한다. 자원이나 생존 HP를 주입하지 않는다.

| 정책 | seed1947 | seed1948 | seed1949 |
|---|---|---|---|
| 적은 병력 전선에 분산 | 승리 R3 /1000HP /251G | 패배 R3 /-16HP /141G | 승리 R3 /1000HP /251G |
| 북부 집중 증원 | 승리 R2 /856HP /236G | 패배 R2 /-12HP /112G | 승리 R2 /856HP /236G |
| 궁병 특화 후 분산 | 승리 R3 /1000HP /200G | 패배 R3 /-6HP /91G | 승리 R3 /1000HP /199G |
| 일반·특수 병영 후 분산 | 패배 R4 /-2HP /73G | 패배 R4 /-13HP /85G | 승리 R3 /1000HP /174G |

음수 HP는 모델 종결 snapshot 값이며 UI 표시 제안이 아니다. 1948 네 정책 패배와 혼합 두 표본 패배는 **초기 징조/초기 지출 의존성 조사 후보**다. 3seed·단순 자동 정책 표본만으로 승률·최적 전략·재미를 판정하지 않는다. F1/F2 정보 이해 및 수동 선택 반례는 HUMAN_NOT_RUN. 이 결함을 먼저 닫고 P04 비재귀 사건/저장 계약으로 이어간다.

검토2/2: 독립 read-only 검토 P0/P1/P2 없음, P3 정책 구매 실재 확인을 보완했다. 같은 계보 전체 검토를 초기화하지 않는다. 최종 로컬/원격 결과·정리 위치는 아래 마감 기록에 누적한다. 새로운 GPU/아트/사람/후속 맵/출시 승인 근거는 이번 증분에 없다.

최종 로컬(2026-09-20): 모델715/저장61 실패0, 화면/기본씬 PASS; 정책 집중255 실패0 및12조합 모두 실제 디스크 재개와 연속 실행 동일. 전체 원문은 기존 월간 증빙 원본 `C:/Users/user/Documents/증빙서류/9월 증빙서류/OMENWARD_원본근거/20260920_save_precision_validation.log`(SHA256 b5b4f159c8994657c7f7f97e3dc1ac950e7b1157d75dbe3239a176d41b6ace27). 프로젝트 스킬4개 검사 및 scope9 Python PASS, 원본 Base 보호경로9 FAIL / PROJECT_SCOPED_BUILD PASS 구별 유지. 검토 P3는 한정 재확인으로 해결. 실행은 명시 OMENWARD path의 Godot4.7.1 headless이며, 다른 프로젝트 Hera 편집기/실사용 저장은 조작하지 않았다.

사용완료 격리 시험폴더8개/132파일과 이전 로그1개(총637687bytes)를 SHA256 대조 후 `C:/Users/user/Downloads/OMENWARD_DELETE_REVIEW_20260912/save-precision-20260920`로 이동했다. 두 manifest에 원위치/복구 위치/해시가 있고 직접 삭제는 하지 않았다. 최신 gate 로그는 위 월간 증빙 원본에 보존한다. 기존 월간 원본 README에9/20을 누적하며 PDF 새 발행/제출은 하지 않는다. 부모 PR258/main/사용자 기획 미커밋 파일과27개 addon import dirt는 보존한다. 이번 GitHub 검증은 PR259의 새 정확한 HEAD를 기준으로 확인하며 Draft 전체 병합 권한으로 확대하지 않는다.

원격 교정: d0658c5b의 첫 원격 검사4 PASS/2 FAIL은 신규 output 로그 경로가 exact BUILD 허용목록에 없었기 때문이다. 앞선 로컬 `--base-repository` 판정은 전체 PR 경로 allowlist의 대체가 아니었다. 원본 로그를 기존 외부 증빙 폴더로 해시검증 이동하고 저장소 참조를 교정했다. 허용목록·CI·제품 코드는 넓히거나 우회하지 않았다. 이후에는 커밋한 정확한 HEAD에서 `--base origin/codex/replan-authority-20260910` 검사도 수행한다.

## 2026-09-16 current request readback

The latest three-front request below supersedes earlier single-front sequencing. Implemented shared-clock/economy/base overview → per-front inspection, isolated combat/healing/capture/towers, conservative legacy profile and fail-closed transport. Model455/save59/UI/default local gate PASS; docs/scope7 PASS with Base raw protected-path failure kept separate. Five-perspective independent review found direct cross-front healing and hidden legacy points; both received regression fixes. GPU uses actual viewport mouse input on center route, verifies only selected_front changes and returns to overview. Current mini-map is schematic UI, not final terrain art. No new raster/Aseprite work. Append September16 into existing unsubmitted monthly PDF; sync current-task PR259 branch only. Remaining product work stays P04→P05→P06–P09, not whole-game completion.

## 2026-09-14 T3 connected readback

Implemented new birth_v2 (v1 preserved) T3 same-role upgrade, round6/later-map gate, ceil1.25 price, same interval/reset production, nonretroactive tier3 entries/tokens and all ten capstone consumers. Numeric rules reside in Blueprint JSON. UI purchase and descriptions consume the same model/catalog; old runs explain T3 requires a new run. Tower damage is ranged in centralized damage input; melee remains untyped/nonranged.

Final local gate426 model/55save/UI/default PASS, docs/scope7 PASS. Ten effects and added timer/invalid profile/partial-state guards covered. Independent five-perspective review found stunned flying contact failed to reset rearm and tower bypassed ranged mitigation; reproduced then corrected. Additional no-melee-mitigation, full8seconds disengagement, Veil opening, guard integer ticks/maxima, armor-duration coupling and old-profile injection checks passed. GPU `output/front-tier3.png` is explicit round5-refit setup→purchase→begin round6→production→exact deployment fixture, not natural progression. Existing combat12damage13units/shield3poses/mixed10damage/status remain verified. No new raster art; P04 remaining grade triggers/event work and P05–P09 are not done.

## 2026-09-14 P03 birth records implementation

Next T3 execution: new birth_v2 marks support for tier3, v1 remains readable without silently gaining T3. Existing v7 envelope stays, transport rejects unknown marker at main/checkpoint. Add facility tier3 only on T2 branch, no role branching; cost ceil(T2price*1.25), first map next-round6 gate, later maps retained, same production interval and reset progress. Source/entry invariants stay. Wire all ten existing capstone meanings with numeric JSON input and saved temporary mitigation/reengagement fields in P04 tests, rather than granting an inactive T3 purchase. No new stat-wide multiplier or new art needed for this scope. Test first: upgrade gates/nonretroactivity, born3 through omen/deploy/save, each effect, interruption, timers and legacy preservation.

ADOPT source-frozen JSON dictionaries and deep snapshots, following [Godot Dictionary reference/copy semantics](https://docs.godotengine.org/en/stable/classes/class_dictionary.html) and [saving games](https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html). ADAPT existing flat v7 with fail-closed `birth_rules=birth_v1` marker; REJECT parallel role/metadata arrays and deferred source lookup from current slot (drift after demolition/upgrades). This is implementation research, not a new player benchmark.

Actual compatibility adapter: retain existing facility id/unit/clock fields plus positive monotonic instance_id; array index remains slot identity and empty sentinel stays unchanged. Save next_facility_id and next_entry_id. Upgrade retains instance; rebuilding a hole gets a new instance. New reserve entries contain entry_id/role_id/birth_tier/source_facility_id/survived=0. Source0 means base/legacy and requires tier1. Production and omen confirmation freeze source/tier; spawn/deploy preserves fields. New snapshots deep-copy both reserve and board. Legacy strings remain tier1/source0 inputs; older rulesets keep old acquisition behavior and never infer T2/T3. T3 is still excluded from this increment.

Omen cell dictionaries keep role/tier/source through shifts. Match by role only; each row-major group of3 produces its lowest tier. A selected bonus across multiple same-role completed lines uses the lowest tier across those completed lines, deterministic tie by first occurrence. Tier is shown before confirmation and in projected rewards. Role-grouped reserve cards bind the exact first entry ID and show next tier/source; arbitrary within-role tier selection is not implemented. No new art generation.

RED→GREEN coverage includes birth through production/upgrade/deploy/demolition/save, independent entry identities, lowest-tier group/bonus, stale card, pending cell tier, deep-copy isolation, partial-field rejection, positive unique facilities, base-source cap, marker contradiction, future checkpoint transport protection and checkpoint counters not ahead of live counters. Review found five save-boundary defects and all were reproduced/corrected. Initial full gate390/55 passed; final gate includes one added checkpoint regression. Existing GPU capture checks12damage/13units, shield3poses, mixed10damage and status fixture; no natural5map/Human approval. Latest counts are recorded in Active Context after final command completion.

## 2026-09-14 P03 specialization gate readback

New slots_v1 runs retain T2 access in later-map round1. First-map timing is owned by Blueprint `facility_progression.specialization_round=2`, with REFIT counting the upcoming round. Model and actual upgrade buttons consume `specialization_unlocked`; phase, pending omen, active slot, branch and cost guards remain. Older profiles keep their former gate. T3 and birth metadata are not implemented by this increment.

RED: corrected fixture facility id from nonexistent archery to range before establishing the meaningful old-gate failure; actual next-map range button also failed. GREEN: model368/save51/screen/default gate PASS; docs and scope7 PASS. Independent five-perspective static review found no blocker. No separate GPU capture for this increment. Validation receipt: external OMENWARD_원본근거/20260914_specialization_gate_validation.txt. Existing PDF v0.1 predates this increment and is not silently replaced.

> **For agentic workers:** Use `superpowers:executing-plans` for sequential implementation and review checkpoints. Do not start code merely because this plan exists. Fresh-read current authority and exact task scope first.

**Goal:** 단일 전선 원정을 마지막 맵까지 실제로 플레이할 수 있게 남은 기획·구현·자산·검증 작업을 연결한다.

**Architecture:** `front_run.gd`가 판정과 저장 가능한 전투 상태를 소유하고 `front_screen.gd`는 명령·표시만 담당한다. 기존 모델을 일괄 재작성하지 않으며, 저장 입출력·이벤트·화면의 명확한 책임만 단계적으로 분리한다. 실제 규칙 수치는 Blueprint JSON을 소비하고 화면에 독립 상수를 복제하지 않는다.

**Tech Stack:** Godot 4 / GDScript / JSON / 기존 SceneTree 테스트 / PowerShell 검증기 / Python 자산 검사 / 이미지 모델 원화 / Aseprite 조립·타이밍·메타데이터.

**Spec:** [사람용 규칙](../../design/OMENWARD_HUMAN_BLUEPRINT_REVIEW_20260911.md), [수치·로스터 입력](../../design/OMENWARD_BLUEPRINT_BUILD_INPUT_20260911.json), [현행 결정](../../CURRENT_CONFIRMED_DECISIONS.md). 아래는 그 원본을 대체하는 새 GDD가 아니라 **미구현 차이와 실행 계약**이다.

## 2026-09-14 남은 작업 설계·구현 명세 — 현재 실행 순서

**2026-09-14 재개 / P03 군수소 증분:** 신규 `facility_rules=logistics_v1`은 군수소35G·활성 슬롯당 용량+6을 JSON에서 소비한다. 군수소는 병력/징조 토큰을 생산하지 않고 UI에서 수용량 전용임을 명시한다. 슬롯 잠김은 효과만 제거하며 기존 병력은 삭제하지 않는다. 헤더/대기열/카드/실제 deploy는 하나의 `capacity_limit()`을 사용한다. 이전 v7 marker 없음은 legacy이며 미래 marker는 정상 backup이 있어도 덮어쓰기·자동복구를 거절한다. checkpoint와 규칙 일치도 검사한다. 모델349/저장51/화면/기본실행 PASS, 독립5관점 정적 재검토 차단 결함 없음. 고정18 UI 회귀 및 미래형식 보호 회귀를 RED→GREEN으로 교정했다. P03 T3·출생정보·철거 등은 남는다. 일반 시설 문양은 명시된 임시 표시이며 새 전용 아트/최종Human은 미완료다.

**월간 증빙 발행 사용자 추가:** 블루프린트를 복제하지 않고 기존 Git 변경/검사 결과/전투 PNG/사용자 요청 발췌로 별도 외부 파생 PDF를 만든다. 지정 9월 폴더의 `OMENWARD_원본근거`에 보고서 생성기·검사 원문·원본별 해시/소스 정보를 보존한다. 기존 작업은 커밋 기록 기반 사후 정리이며 시각 인증이나 개별 AI 사용 시각 인증이 아니다. 이번 발행은 확인한9월14일 패킷만 포함하는 초판이며 9월 전체 이용/정산내역이 아니다. 실제 메일/HWP·계정 식별·청구 연결·입력 화면 캡처는 미확인으로 남긴다. 이후 작업 종료 때 동일 근거 구조를 추가하고 월별/정정 버전으로 출력하며 다른 프로젝트 자료는 변경하지 않는다. 앞으로의 분리 아트는 크로마키→배경제거→알파/가장자리/상태군/runtime QA; 이번 증빙 작업에서 새 아트를 생성하지 않는다.

### 후속 승인 및 첫 구현 증분

P02 증분 결과: 모델339/0실패·저장47/0실패·화면/기본headless PASS. 타워 마지막 타격, 불완전 capture, checkpoint rule/work, 선정산 ledger, 살아있는 본진의 claim priming, 보급 단위/상한, 미래capture 저장 덮어쓰기 RED→수정→GREEN. 최종 독립5회 전체범위 정적 재검토에서 추가 차단 결함 없음. 자연5맵완주/최종Human/투사체·탑아트는 NOT_RUN/잔여. 사용완료한7개 검사 폴더91파일236683bytes는 해시 검증 후 `C:/Users/user/Downloads/OMENWARD_DELETE_REVIEW_20260912/P01-P02-tests-20260914`로 이동했다. README/복원경로/SHA-256 manifest 포함, 직접 삭제0. 실제 사용자 저장과 다른 작업 산출물은 이동하지 않았다.

**P02 실행 중:** P01의 실제 시계/저장 consumer 위에 점령과 정산을 연결했다. 사건 ID/지연 projectile은 P04/P07의 실제 consumer에서 확장하며 빈 queue를 선제 구축하지 않는 것으로 실행 의존을 구체화했다. 신규 원정만 `capture_rules=timed_v1`; marker 없는 기존 v7 및 v1–v6는 이전 즉시 점령/본진HP 규칙으로 유지한다. 반경3/1명8초/2명이상4초/혼재 동결/이탈초당10%/중립화→점령을 JSON owner에서 읽고, 정수 work로 저장한다. 실제 자동행군은 빈 거점 확보까지 대기하고 적이 들어오면 전투 접근을 재개한다. 암살자는 유효 후열 추격 우선이며 비행병은 점령에 기여하지 않는다.

비교 근거: [Company of Heroes 공식 배포 매뉴얼](https://steamcdn-a.akamaihd.net/steam/apps/20540/manuals/CoH_ToV_G4W_MNL.pdf)의 거점→자원/인구와 지도 표시 연결을 ADAPT, 보급선 단절과 다중 자원은 REJECT했다. [Age of Empires IV 공식 시작 안내](https://www.ageofempires.com/news/quickstart-guide-age-of-empires-iv/)의 특정 지점 확보·유지라는 별도 승리 목표를 ADAPT하되 전체 성지 동시 보유 규칙을 복제하지 않았다. 8초/반경3 등 숫자는 위 게임에서 추출한 값이 아니라 OMENWARD 권장값이다. 내부 엔진 역공학 또는 비교 게임 직접 플레이 검증으로 표현하지 않는다.

본진 방어HP0→지상 점령, 아군HP0패배 우선, 조기승리 잔여 기본보급(전체 맵 예산−이미 지급한 기본보급)1회 지급을 연결했다. ledger는 외부 공통 ledger가 아니라 각 run snapshot 내부의 연속 map index 목록이므로 불필요한 전역run_id는 아직 만들지 않는다. map checkpoint는 이전 맵 ledger만 보존하며 현재 점령 work/기본보급0을 검증한다. 살아 있는 본진의 사전 claim, BATTLE의 선정산, 비연속 이력,5G단위가 아닌 보급, 누락/미래점령규칙을 거절한다. 타워 피해·사망을 점령보다 먼저 처리하여 마지막 점령자가 해당 tick에 사망하면 중립화를 완료하지 못한다. 타워 투사체/전용 아트는 여전히 P07 잔여다.

이번 GPU 실행: 자연 동원→진군→전투12피해/13유닛, 방패3상태/3, 혼합 fixture10유닛/10피해, 효과 fixture barrier7/stun0.3/move0.85 확인. live Hera에 대상 프로젝트 editor는 없었고 다른 세 프로젝트에는 연결/변경하지 않았다. 로컬 Godot renderer로 기존 캡처 검증기를 실행했다. 축소 병력의 가독성/겹침·탑 marker는 최종아트 승인 대상이 아니며 P06/P07 개선 대상이다. 점령 UI 생성 중 null parent 오류는 실패 실행으로 분리했고 self 부모로 교정 후 screen PASS; 오류로 계속 돌던 정확한 두 테스트 프로세스만 종료했다.

고정 시계 증분 검증 결과: 모델312/0실패, 저장43/0실패, 실제 화면 노드의 속도 버튼/저장/복구 검사 PASS, 기본 headless 씬 PASS, scope7/문서88 PASS. 고정 API 누락 RED→구현,2× UI RED→수정, 정수 duration 저장 RED→구현, 재정비 debt 동결 RED→수정. JSON float version membership 거절을 수치 검증으로 교정했다. 독립5회 정적 검토와 재검토에서 battle-exit debt/유한 큰 delta/legacy fixture 문제를 처리했다. v1–v6에 비영 cooldown 초 단위 fixture를 추가했고 버전1로 표시만 했던 검사를 실제 version1로 수정했다. GPU 캡처·Human·전체원정 PASS는 이번 증거가 아니다. 실제 사용완료 임시 검사 산출물은 사용자 삭제 검토 대상으로만 보존한다.

**현재 연속 구현 — 고정 시계 증분:** 최신 사용자가 전체 구현 루프를 명시하여 아래 계획 준비 전용 문장을 이력으로 한정한다. P01을 실행 중이다. [Fix Your Timestep 원저자 실무 설명](https://gafferongames.com/post/fix_your_timestep/)의 고정 간격 누산 방식을 ADAPT하고, [Godot 공식 고정 physics/render 분리](https://docs.godotengine.org/en/stable/tutorials/physics/interpolation/physics_interpolation_introduction.html)를 참고했다. 가변 조각(REJECT: FPS에 따라 판정 변화), engine 전역 속도 변경(REJECT: UI까지 영향), 모델 소유30Hz+프레임당120tick상한+잔여 보존(ADAPT)을 비교했다. 예제의 시간 clamp는 채택하지 않는다. 과도 입력은 상태 변경 전 거절하고 실제 performance 최적값은 측정 전 확정하지 않는다.

현재 flat v7은 기존 model snapshot의 연속이며 별도 envelope를 만들지 않는다. `ruleset_id=fixed30-v1`, 누적 `tick`, 분수/지연 `tick_debt`, `timer_units=ticks`를 추가하고 단위/상태효과 countdown을 정수 tick으로 직렬화한다. 화면/모델 API는 초 단위를 유지한다. catalog_hash/run_id/사건 ID/보상 ledger/점령/투사체는 실제 후속 consumer와 함께 추가할 대상으로 남기며 빈 framework로 완료 표시하지 않는다. 따라서 P01 전체 완료가 아니다. v1–v6는 원래 가변 적분과 wave_rules를 다음 맵에서도 유지한다. UI는1×/2×로 연결했다. 테스트/독립 검토 진행 중이며 최종 결과는 아래 추가한다.

사용자 후속 승인 ‘좋아 권장안대로 작업진행해’로 아래 계획 준비 전용 상태를 해당 턴의 이력으로 전환한다. P00의 네 안정 진입점에 현재 owner와 역사 경계를 연결했고 scope는 exact8경로만 추가했다. 해시 고정 Skill/adapter는 유지하고 obsolete 제품 의미는 Registry의 override 경계로 명시했다.

P01은 저장 transport부터 진행했다. Ruling: 고정 시계·v7 전환과 파일 I/O 변경을 한 번에 섞지 않는다 — 구형 저장의 실제 복구 경로를 먼저 확보하고 이후 시뮬레이션 차이의 원인을 분리하기 위함 — P01 전체 완료는 아직 아니다. `front_save.gd`는 Model.restore를 검증기로 재사용하며 새 저장 모델을 만들지 않는다. 기존 파일 방식과 비교한 대안: 직접 덮어쓰기(REJECT, 실패 시 정상본 유실), temp+rename만 유지(REJECT, 검증/backup 없음), temp 재읽기+검증된 이전 정상본+교체(ADAPT). Godot 공식 FileAccess/DirAccess 문서를 확인했고 파일 크기4MiB 한도·flush/close·모델 검증·해시 대조를 결합했다. OS 전원손실까지 완전한 원자성/내구성을 보장한다는 주장은 하지 않는다.

실제 consumer는 `front_screen._save/_load_save`. 정상 primary를 검증한 backup으로 보존하고, 손상 primary를 읽을 때 backup에서 복구하되 원본을 변경하지 않는다. 복구 후 저장 시 손상본은 고유 rejected 이름으로 보존한다. 미래 `version`뿐 아니라 `schema_version/ruleset_id` 표지가 있는 primary/backup 모두 구형 writer에서 차단한다. v1–v6 gameplay와 저장 schema는 그대로 유지했다.

검증: 기존 모델268/0실패; 새 저장43/0실패; 화면 저장→손상→이전 정상본 복구→재저장 PASS; 기본씬 headless PASS; scope7 PASS. 새 파일 미존재 RED, 미래 envelope4실패 RED→수정, 미래 backup4실패 RED→수정→43 GREEN. 중간 테스트 변수 타입 파서 오류는 별도 교정했으며 기능 RED/PASS로 계산하지 않는다. 독립 검수자는5회 전체 범위 정적 검토 및 두 차례 수정 재검토를 수행했고 미래형식/백업 보호·최상단 현재상태 문제를 해결 확인했다. 독립 검수자 runtime/Human은 NOT_RUN. Base raw protected-path FAIL/scoped PASS 유지. 30Hz·정수 duration·v7·사건 순서는 다음 P01 증분으로 남는다.

참조 전파: Registry/Documentation Map/GDD locator/Project Core는 must-update, Decisions/Active/Roadmap은 current-mutable, 과거2026-08문서/PDF는 history, adapter/생성snapshot/기존모델은 compatibility-preserved. 새로운 runtime asset 없음. 이번 사용완료 검사 fixture56개(129741bytes)는 사용자 삭제 검토 폴더 `C:/Users/user/Downloads/OMENWARD_DELETE_REVIEW_20260912/P01-save-20260914`에 해시 대조 후 이동했고 직접 삭제하지 않았다. 장기 lesson: 미래 format의 primary뿐 아니라 backup도 downgrade 보호해야 한다. 공용 Base 승격은 아직 후보이며 외부 저장소 변경 없음.

문서 상태: `SPECIFIED_RECOMMENDATION / IMPLEMENTATION_NOT_RUN_THIS_TURN`. 이번 사용자 요청은 남은 작업과 명세 준비다. 게임 코드·자산·수치 입력은 이번에 변경하지 않는다. 이 절 이전의 실행 결과는 이력이고 아래쪽 과거 `next` 문장은 현재 작업 순서가 아니다.

검토 기준: 작업 브랜치 `codex/visible-battle-20260911`의 `496bc3b1573f0d6f6554c220baac8f83d58b2a8c`, fetch한 main `9ea3245b`, 작업 PR #259 → 부모 #258 → main. #257/#212/#209/#205의 열린 작업은 읽기 전용 중첩 조사 대상이며 흡수하지 않았다. main은 현 검토판과 동일 제품 상태가 아니다. Base remote `d830c0f6`와 채택 v9.4.3을 비교했고 lock은 유지했다. 재개할 때 SHA와 PR 상태를 다시 확인한다.

발행: 기존 실행 계획의 repository-native 운영 문서 갱신. 새 본책·PDF·독립 수치표를 만들지 않는다. 이전 사람용 PDF는 최신 구현 증거가 아니며 P09 milestone에서 원본 갱신 후 재발행한다.

### Global Constraints

- 사용자 확정: 전선 1개, 순차 맵 5개, 맵 → 시간제 10+α 라운드 → 복수 웨이브 → 재정비, 전체 라운드 생존 또는 적 본진 점령 승리.
- 사용자 확정: 상단 한 줄 미니맵, 룰렛/내정/전선 탭, 건물은 목록에만, 방어탑은 현재 전선에 한 개, 이동 영역 밖 분리 소품.
- 사용자 확정: 슬롯은 상단부터 `6 + 보유 점령지 수`; 잠긴 건물은 보존하되 비활성. 일반/특수 병종 계열은 별도, 일반 병영 T1은 방패병부터 전문화.
- 세 전선·강으로 끊긴 경로·건설 노드·기존 이미지의 자동 최종승인 복원 금지. 수치/영웅/등급 세부는 권장 초깃값과 사용자 확정을 구분한다.
- 전투용 유닛·건물 카드의 분리 오브젝트·소품·VFX는 실제 알파 채널을 검사한다. 불투명 배경화와 투명 오브젝트를 혼동하지 않는다.
- 생성 후보 → 검수 → 사용자 최종 아트 승인 → 정본 등록 → 소비처 적용 → 실제 화면 검증은 별개다. Aseprite 저장만으로 모션 완료를 주장하지 않는다.
- 기존 저장·승인 원화·다른 작업 변경을 보존한다. 삭제 후보는 출처/해시/복구 안내와 함께 사용자 삭제 검토 폴더로만 이동한다.
- 아래 `Create` 경로/API는 **제안이며 아직 존재하지 않는다**. 현 exact-path BUILD allowlist는 신규 모듈을 자동 허용하지 않는다. 각 패킷 착수 때 scope owner와 해당 경로만 검토·추가하고 Base 보호 계약을 우회하지 않는다.

### 1. 지금 무엇이 남았는가

| 영역 | 실제 상태와 차이 | 작업 / 완료 증거 |
|---|---|---|
| 원정 진행 | 5맵 전환·53라운드 설정·재도전 checkpoint 존재. 자연 5맵 완주는 미확인 | P01/P02/P08: 시간·점령·보상 정합성, 실제 자원 완주 로그 |
| 시간 | 프레임 delta를 최대 1초로 잘라 최대 0.05초 가변 조각 처리. 30Hz 정수 tick 명세와 다름 | P01: FPS/배속/저장 재개 동일 사건 결과 |
| 점령 | 반경 5 내 한쪽 병력이면 즉시 소유권 변경, 공중도 기여. 본진 HP 0이면 즉시 승리 | P02: 반경 3 지상 점령·중립화·본진 최종 점령·시각 진행률 |
| 경제 | 기본 20초/5G·거점 15초/1G 존재. 조기 점령 잔여 기본 보급 정산 없음 | P02: 한 번만 정산, retry/로드 보상 중복 0 |
| 건물/군수 | T1/T2 일부 연결, T3·군수소·철거 없음. 대기열은 병종 문자열이라 출생 티어가 없음 | P03: 고정 슬롯 ID·출생 정보·한도·기존 병력 비소급 |
| 병종 | 10역할 기본 전투, 일부 숙련/정예·공통 상태효과 연결. 전 효과 완성 아님 | P04: 남은 스킬·비재귀 추가타·양 진영 경계 테스트 |
| 영웅 | 도감/설계 3명, 실제 출정 선택·전투 소비처 없음 | P05: 선택/수동 능력/사망/복귀/저장 |
| 화면 | 검토판 3탭, 예보·치료·저장 있음. 완성형 메인/맵 선택/결과/설정 없음 | P06: 시작부터 결과까지 실제 입력으로 왕복 |
| 아트/모션 | Ward/Veil 정적 투명 파생본, 시설8종, 방패4자세만 일부 연결 | P07: 20병종 외형+3영웅 필수 상태군, 시설/탑/5맵 소비처 |
| 공세/밸런스 | 6템플릿에 창병·암살자·비행병이 빠짐. 자동 정책 3seed 모두 2맵2라운드 패배 | P08: 53라운드 전체 콘텐츠/다중 전략/회복 가능성 비교 |
| 최종 전달 | Draft 스택, 구형 문서와 최신 검토판 불일치, 출시/기기/Human 미완료 | P09: 보호된 main 통합·패키지·권리·사람 검증 분리 |

### 2. 조사·비교 및 채택 판단

기존 수치 입력의 `sources`에 있는 12게임 벤치마크를 유지한다. 이번에 모든 게임을 새로 플레이하거나 역공학한 것은 아니다. 새 확인은 준비/전투 구조와 Godot 저장·애니메이션 계약에 한정한다. 게임 소개 자료로 내부 알고리즘을 알아냈다고 주장하지 않는다.

| 근거 | 판단 | 프로젝트 적용 / 배제 |
|---|---|---|
| [Thronefall 공식 판매 페이지](https://store.steampowered.com/app/2239150/) | ADAPT | 준비 선택과 공세 결과를 분리해서 학습시키기. 전장 건설 위치/전멸제 종료를 복제하지 않음 |
| 기존 Into the Breach 비교 | ADAPT | 동일 공세 데이터로 예보와 실제 출현 생성. 비공개 편성 맞춤 하드카운터 배제 |
| 기존 Commander Quest/Monster Train 비교 | ADAPT | 병종 상호작용·배치/성장의 인과 표현. 다층/3전선 지형 배제 |
| 기존 Slotbound/Luck be a Landlord 비교 | ADAPT | 건물이 미래 동원 분포를 바꾸는 엔진. 조작된 아깝게 실패 연출·잭팟 필수 구원 배제 |
| [Godot Saving games](https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html) | ADAPT | 저장 가능한 상태를 명시적으로 직렬화. JSON 타입 한계 검사, 설정은 별도 저장. 문서 예제만으로 원자 교체/백업까지 보장된다고 해석하지 않음 |
| [Godot SpriteFrames](https://docs.godotengine.org/en/stable/classes/class_spriteframes.html) | ADOPT/ADAPT | 상태별 프레임·재생속도·반복 여부의 표현, 실제 타격은 모델 사건이 소유. 애니메이션 종료 콜백으로 중복 피해를 만들지 않음 |

**독창성을 강화할 축:** 확률 엔진을 만드는 내정, 생존과 진격의 이중 목적, 살아남은 개체의 성장, 점령으로 열리는 군수 슬롯이 서로 연결되어야 한다. 새 메타 성장·장비 랜덤 옵션·멀티플레이를 더하지 않고 이 네 가지의 선택 결과를 먼저 완성한다.

| 현재 약점/위험 | 강화·개선 | 기대효과와 실패 판정 |
|---|---|---|
| S: 두 승리조건이 있으나 현재 즉시 본진 파괴로 진격만 유리해질 수 있음 | 점령 마무리와 남은 기본 보급을 명확히 표시 | 방어/진격 선택이 성립; 한 정책이 모든 seed/맵에서 지배하면 재조정 |
| W: 숫자·모션·저장 시계가 어긋날 가능성 | 공통 tick·사건 ID·출생 데이터·손상 없는 저장부터 | 재개 시 피해/보상 복제 0; 실패하면 새 스킬 추가보다 기반 수정 |
| O: 생존 병사의 성장과 시설 전문화 조합 | 티어와 등급을 별도 표기, 결과에서 성장 원인 설명 | 병사를 지키는 가치가 보임; 죽은 병사/신규 병사에 성장 전이되면 실패 |
| T: 점령의 골드+슬롯+탑 눈덩이 | 기본6칸으로 대응 가능한 공세, 상실 후 재점령 시나리오 | 병력 강제 삭제 없이 회복 가능; 보유 슬롯 규칙 자체를 몰래 약화하지 않음 |
| T: 지연 파밍/유료 동원 단일 정답 | 즉시 점령/장기 생존의 순자산·시간·손실 비교 | 기본 보급 정산만으로 해결 선언 금지; 미래 거점 수입과 생산 차이도 측정 |

### 3. 의존 순서와 공통 실행 절차

```text
P00 현재 정본/범위 정합성
 → P01 고정 시계·저장 기반
 → P02 점령·본진·보상
 → P03 슬롯·군수·T3 출생 정보
 → P04 남은 병종 효과
 → P05 영웅
 → P06 전체 화면 흐름
 → P07 아트·모션 완성
 → P08 전체 공세·밸런스
 → P09 통합·사용자 전달·출시 준비
```

P07의 소비처별 원화 준비는 P03~P06의 규격이 고정된 부분부터 가능하다. 그러나 검증 전 이미지를 대량 제작하지 않는다. P08의 측정기는 P01부터 쓰되 최종 밸런스 판정은 P03~P07 연결 이후다.

각 패킷은 독립적으로 거절/롤백 가능한 단위다. 구현자는 다음 순서로 진행한다.

- [ ] 패킷이 참조하는 현재 파일과 범위 allowlist를 다시 읽고 변경 경로를 한정한다.
- [ ] 아래 명시된 반례를 `tests/replan_slice_test.gd` 또는 `tests/replan_screen_test.gd`에 추가한다. 없는 API는 `has_method`로 검사 후 조기 반환하여 RED 이유를 식별한다.
- [ ] 기존 검증기를 실행해 기대한 미구현/행동 불일치로 RED인지 확인한다. 파서 오류나 환경 실패는 기능 RED와 구분한다.
- [ ] 한 규칙과 해당 저장/표시 소비처만 최소 구현한다. 수치 변경은 JSON owner에 먼저 반영한다.
- [ ] 같은 반례 GREEN → 전체 인접 회귀 → 실제 화면/입력/저장 검사 → 5회 전체 범위 적대적 검토를 수행한다.
- [ ] Active Context의 현재 상태와 이 계획의 패킷 증거를 갱신하고 허용 파일만 commit/push한다. exact-head CI를 확인하며 main 통합을 추정하지 않는다.

공통 기존 실행 명령(구현 때 사용; 이번 문서 작업에서 게임 검증을 다시 실행했다는 뜻 아님):

```powershell
$godotExe = 'C:/Users/user/Downloads/Godot_v4.7.1-stable_win64.exe/Godot_v4.7.1-stable_win64_console.exe'
& $godotExe --headless --path . --script tests/replan_slice_test.gd
./tools/validate_replan_slice.ps1 -Godot $godotExe
python -m unittest discover -s tests -p 'test_replan_scope.py'
python tools/replan_scope.py --base-repository ../_base-validator-19355-blueprint
```

### P00 — 정본 차이와 실행 범위 교정

**상태:** REQUIRED_BEFORE_NEW_MODULES. **문제:** 오래된 lifecycle registry/GDD/skill 본문이 여전히 3전선 또는 구현 전 상태를 current로 표시한다. 최신 AGENTS 상단 재기획 예외가 우선하지만 cold-read 혼선을 남긴다.

**Modify(착수 시 범위 확인):** `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`, `docs/DOCUMENTATION_MAP.md`, `docs/OMENWARD_GDD_CURRENT_CANON.md`, `docs/PROJECT_CORE.md`, `docs/process/APPROVED_REPLAN_UI_MOTION_BUILD_SCOPE_20260911.md`, `tools/replan_scope.py`. 현재 lock/생성 snapshot은 교체하지 않는다.

**작업:** 현재 질문별 owner를 최신 결정→Blueprint→실제 consumer에 연결하고 이전 3전선 본문은 삭제 없이 history로 분류한다. 공유 Skill의 낡은 게임 규칙은 로컬 override의 정확한 대체 범위를 기록한다. 생성 snapshot을 수동 편집하지 않는다. 새 JSON 필드/모듈 경로만 exact allowlist amendment로 추가한다.

**합격:** 같은 사실의 active owner 한 개, 폐기된 3전선이 신규 실행 경로로 복원되지 않음, 부모/다른 PR 내용 미흡수. Base raw FAIL과 scoped PASS를 계속 별도로 보고한다. 문서 정합성이 보호된 main 통합 완료를 뜻하지 않는다.

### P01 — 고정 시계·저장·사건 기반

**Modify:** `scripts/replan/front_run.gd`의 `advance/_tick/snapshot/restore`, `scripts/replan/front_screen.gd`의 `_process/_save/_load_save`; 기존 모델/화면 테스트. **Create 제안:** `scripts/replan/front_save.gd`(파일 입출력만), `tests/replan_save_test.gd`(실파일 실패 경계), 검증기의 해당 테스트 호출.

**인터페이스 제안:** `advance(delta: float) -> void` 유지; `advance_ticks(count: int) -> void`, `simulation_tick() -> int`; `FrontSave.write_verified(path: String, state: Dictionary) -> Dictionary`, `FrontSave.read_verified(path: String) -> Dictionary` → `{ok: bool, reason: String, state: Dictionary}`. 실패는 live run을 수정하지 않는다.

**설계:** 신규 ruleset은 30Hz 고정, `ceil(seconds * 30)` duration tick. 프레임 누산기는 잔여 시간을 보존하고 한 프레임 실행량이 제한되어도 빚을 버리지 않는다. 일시정지/재정비에는 모델 tick 증가 없음. UI 배속은 명세의 1×/2×, 모델 공격 속도 상수를 곱하지 않는다. 큰 delta를 현재처럼 1초로 자르지 않는다. 렌더 보간은 상태에 역기록하지 않는다.

**동일 tick 순서:** 명령 검증 → 만료 처리 → 예정 공세/생산/수입 → 표적·이동 → 준비완료/발사 → 적중·효과 → 사망 정리 → 점령 → 본진/라운드 종료 → 종료 보상·성장 1회. 동일 종류는 생성 ID 오름차순. 종료 tick과 같은 신규 공세는 생성하지 않는다. 사망 전 발사된 사건은 유효하지만 미발사 공격은 취소한다.

**저장 v7 제안:** `schema_version`, `ruleset_id`, `catalog_hash`, `run_id`, `tick`, `next_event_id`, `rng_state`, `map_entry`, `reward_ledger`, `units`, `buildings`, `reserve`, `capture`, `pending_events`. 모든 숫자는 유한/범위/정수 조건 검증. ID 중복·알 수 없는 필수 ruleset·미래 버전은 원본 보존 후 거절. UI 선택/음량은 별도 설정이며 RNG에 섞지 않는다.

**호환:** v1~v6 진행 중 원정에 새 점령/경제 규칙을 무음 적용하지 않는다. 구형을 기존 경로로 계속 실행하고 새 원정부터 v7을 사용한다. 파일을 읽었다는 이유만으로 덮어쓰지 않는다. 다음 맵에서 자동 전환도 하지 않는다. 장기적으로 구형 adapter는 해당 fixture와 실제 사용자 호환 범위가 끝났다고 확인된 뒤 정리한다.

**입출력:** temp 쓰기→닫기→다시 읽고 모델 검증→기존 유효 파일을 backup으로 보존→교체. 실패 단계별 이전 정상본 유지/복구, backup도 검증 후만 사용. 원자 교체 성공을 OS별 실행 없이 주장하지 않는다. snapshot hash는 손상 탐지용이지 부정행위 방지 서명이 아니다.

**RED 예시(새 API 제안, 테스트 함수에 삽입):**

```gdscript
var a = model.new()
var b = model.new()
check(a.has_method("advance_ticks"), "P01 requires fixed ticks")
if not a.has_method("advance_ticks"):
    return
check(b.restore(a.snapshot()), "Share identical seed, run ID and entry state")
a.begin_round()
b.begin_round()
a.advance_ticks(30)
for i in range(30):
    b.advance_ticks(1)
check(a.snapshot() == b.snapshot(), "Tick batching must not alter state")
```

**추가 합격:** 동일 seed/input으로 30/60/144FPS·1×/2× 결과 사건 순서 일치, 중간 저장→재개 일치, 2.5초 delta 시간 유실 없음, 손상 temp/rename 실패/잘린 JSON 때 이전 정상본 보존, legacy fixture unchanged. 부동소수 위치까지 cross-platform bit-identical이라는 목표는 세우지 않으며 동일 실행 환경의 허용 오차를 따로 명시한다.

### P02 — 점령·탑·승리·정산

**Modify:** `front_run.gd`, `front_screen.gd`, Blueprint JSON의 점령/정산 명시 키, 모델/화면 테스트. **Consumes:** P01 tick/사건/저장. **Produces 제안:** `capture_state(point_id: String) -> Dictionary`, `settle_map(reason: String) -> bool`.

**좌표 계약:** 지도 좌표 0~100의 점령 반경은 3 그대로다. 병종 사거리의 전투 거리→지도 좌표 변환(현재 ×3)과 섞지 않는다. 점령 위치 25/50/75, 탑은 50의 한 개. 지상 생존 병력만 기여하며 진영별 인원 기여는 최대 2. 영웅의 점령 기여는 P05의 기본값에 명시한다.

**점령 상태 제안:** `{point_id, owner: -1|0|1, capturing_side: -1|0|1, progress: 0..1, leg: NEUTRALIZE|CLAIM}`. 여기 side 코드 역시 현재 점령 owner 관례(0중립/1Ward/-1Veil)를 사용하며 unit.side(0Ward/1Veil)와 변환 함수를 둔다. 혼재하면 정지, 공격측이 없으면 progress가 초당0.1 감소. 한 병력은8초/두 병력은4초. 빈 중립 거점은 CLAIM 한 단계. 적 소유 거점은 NEUTRALIZE 후 CLAIM 각8초라는 **모호성 해소 권장값**; 총16초(2인8초)를 툴팁에 표시한다. 단계를 넘은 잔여 tick을 다음 단계에 전달한다.

적 본진 HP0 이후 `BREACHED` 상태, 수리/자동 HP 복원 없음, 지상 병력의 CLAIM 완료 때 승리. 아군 HP0은 즉시 패배. 아군 함락→적 점령→최종 라운드 생존 순서 유지. 거점 반복 점령의 일회성 골드 없음. 적/아군이 빈 거점을 떠나면 기존 소유권은 유지한다.

**탑:** 소유권은 중앙 거점 owner에서 파생. 중립은 공격하지 않으며 다음 발사부터 새 진영. 예정 투사체는 `source_side_at_launch`를 보존. 시각만 늦게 날아가는데 피해는 먼저 들어가는 상태를 완성판으로 두지 않는다(P07 연결). 다른 두 거점에 탑을 추가하지 않는다.

**정산 기본값:** 맵의 기본 보급 예산 `rounds * base_gold_per_round`에서 이미 지급한 기본 보급만 뺀 값을 CAPTURE 승리 때 한 번 지급한다. 거점 수입·미생산 병력은 제외. `reward_ledger[run_id/map_id]`로 중복 방지하며 맵 진입 재도전은 실패 원정 ledger까지 되돌린다. 이 전체 맵 예산 해석은 권장안이며 밸런스 검증 전 확정 수익률로 표현하지 않는다.

**RED/합격:** 지상1명239tick 미점령/240tick(8초) 점령; 비행10명 기여0; 양측 혼재 진행0; 떠남/복귀 decay; 중립화 완료 때 탑 중지(완료 전 기존 소유 유지); 본진 HP0이지만 점령 미완료면 계속 전투; 동시 함락 패배; 같은 settle/로드/버튼 두 번 보상1회. 10라운드 맵에서 기본5G 수령 후 조기 승리 정산145G, 거점 수입은 차감 대상 아님. 재정비 점령/투사체 동결·반경 양진영 대칭 검사.

### P03 — 건물·군수·T3와 출생 정보

고정슬롯 증분 검증 결과: 기존349모델/51저장 baseline PASS → missing demolish RED → 모델/저장 구현 → missing confirmation UI RED → UI연결 →365모델/51저장 PASS. 독립5관점 검토 후 실제 비어있지 않은 확정대기 보존 검사를 보강하고 동일값복원 후 오래된 확인창 RED를 재현했다. 값동등성을 [Godot is_same 참조 동일성](https://docs.godotengine.org/en/stable/classes/class_@globalscope.html#class-globalscope-method-is-same)으로 교정해 최종366모델/51저장/화면/기본실행 PASS. GPU 철거 확인창/취소상태보존·전투12피해13유닛·방패3자세/혼합10피해·상태효과 확인. 전페이지 게임/Human 검증은 아님. 최신 Hera에는 다른4프로젝트만 있어 접속/변경하지 않고 프로젝트 standalone renderer를 사용했다. Base remote d830c0f6와 프로젝트 잠금v9.4.3 유지, 원검사보호9경로FAIL/scopedPASS. 독립 최종 재검토의 차단 결함 없음. 프로젝트 교훈: 되돌릴 수 없는 명령 확인은 값이 같은 새 데이터가 아니라 확인 당시의 실제 객체를 대조해야 한다. Base 승격은 후보이며 공용 파일 수정 없음.

2026-09-14 후속 실행 계약(고정 슬롯·철거): 기존 건물 배열의 위치를 유지하는 빈 슬롯 marker를 채택한다. 배열 압축은 잠긴 시설이 앞으로 당겨지는 규칙 우회를 만들므로 REJECT, slot-key Dictionary 전환은 모든 기존 consumer/저장을 재작성해야 하므로 이번 증분에서는 REJECT, 기존 배열+검증된 빈칸은 ADAPT. [Godot Array 공식 문서](https://docs.godotengine.org/en/stable/classes/class_array.html)의 인덱스/참조 동작과 [ConfirmationDialog](https://docs.godotengine.org/en/stable/classes/class_confirmationdialog.html)의 confirmed/cancelled 흐름을 확인했다. 기존 CoH 거점·경제 연결 비교는 REUSED_EVIDENCE이며 새 직접 플레이 조사로 표현하지 않는다. 신규 원정만 facility_rules=slots_v1을 사용하고 이전 logistics_v1/legacy는 원래 규칙을 보존한다. 빈칸은 id/unit 빈 문자열·clock0만 허용, 첫 해금 빈칸에 재건설, 철거는 준비/재정비·pending없음·활성시설에서만 무환급으로 실행한다. UI는 확인 전 모델 변경0, 취소0, 확정 후 해당 칸만 비우기·확정대기/생존병력 보존·군수 효과즉시감소를 검증한다. 재로드/미래규칙 차단/잠긴시설 이동 방지까지 기존 테스트로 확인한다. T3·출생정보는 뒤따르는 별도 증분이며 이번 marker만으로 완료하지 않는다.

**Modify:** `front_run.gd`의 건설/전문화/생산/징조륜/출전/저장, `front_screen.gd`의 내정·대기열·용량 표시, JSON 시설 입력, 기존 테스트. **API 제안:** `capacity_limit() -> int`, `upgrade_tier(slot: int) -> bool`, `demolish(slot: int) -> bool`, `deploy_entry(entry_id: int) -> bool`.

**상태:** 건물 `{instance_id, slot_index, facility_id, tier, fixed_special_role, production_ticks}`. 철거는 해당 슬롯만 빈칸으로 만들고 뒤 건물을 당기지 않는다. 새 건설은 첫 해금 빈칸. 건설/전문화/철거는 PREPARE/REFIT이면서 omen_pending=false일 때만. 철거 UI는 무환급·토큰/생산 중단·용량 감소를 확인하며 기존 병력과 이미 확정된 대기는 남긴다.

**군수:** `capacity_limit = 18 + 6 * active_logistics_count`; 잠긴 군수소 효과0. 사용량이 한도를 초과해도 생존 병력을 삭제하지 않고 추가 출전만 차단한다. 대기 한도24는 별개다. 모든 표시와 버튼은 API 값을 사용하고 `/18` 하드코딩을 제거한다.

**티어:** T2는 첫 맵2라운드 준비부터, T3는 첫 맵6라운드 준비부터라는 catalog 권장 gate. 다음 맵1라운드에서 다시 잠기지 않도록 `(map_index > 0 or round >= threshold)`로 판정한다. T3 비용/간격은 원본 `capstones`와 시설 가격을 참조한다. 일반↔특수 계열 이동 없음. T2→T3는 같은 역할 하나이며 T3 추가 분기 없음.

**출생 계약:** 대기열 문자열을 `{entry_id, role_id, birth_tier, source_facility_id, survived: 0}`로 변경. unit에 동일 출생 정보를 보존. 생산 완료/징조륜 확정 시점에 출생을 고정한다. 징조륜 token에는 role뿐 아니라 source/tier를 보존하고 같은 역할 매칭은 `role_id`로 판정한다. 선택 보너스의 추가 병력은 완성선의 가장 낮은 tier를 사용한다는 권장값으로 고급 한 토큰의 무한 복제를 방지한다. 구형 string 대기는 tier1로만 호환하고 임의 T3 승급하지 않는다.

**RED 예시:**

```gdscript
var run = model.new()
check(run.has_method("capacity_limit"), "P03 requires shared capacity")
if not run.has_method("capacity_limit"):
    return
check(run.capacity_limit() == 18, "Base capacity")
check(run.construct("logistics"), "Build affordable logistics")
check(run.capacity_limit() == 24, "Active logistics adds six")
```

**추가 합격:** 점령지 상실로 잠긴 군수소/생산/다음 토큰 모두 비활성, 회복 시 원래 슬롯/생산 잔여 복원; 철거로 슬롯 압축 불가; 업그레이드 전 대기/출전은 기존tier, 이후 생산만tier3; 저장후 source/tier/특수 추첨 불변; pending 중 변조/이중 비용 차감 불가. 예외적으로 공개 기본 토큰에는 출처 `base`/tier1 사용.

### P04 — 남은 숙련·정예·T3 전투 효과

**2026-09-14 execution order refinement:** First correct the existing area-hit consumer: preserve the primary target, select additional living enemies by distance from the primary then unique unit ID, and exclude enemies behind the greatsword attacker. Do not sort the live units array or change caps/radius/grade ownership in this correction. RED fixtures cover insertion-order independence, equal-distance ID ties, mirrored sides, dead/allied candidates, primary once, and no extra basic-hit increments. ADOPT Godot `Array.sort_custom`; ADAPT with explicit ID tie-break because the engine sort is not stable; REJECT sorting global units or a new event bus for this existing synchronous selection. Source: https://docs.godotengine.org/en/stable/classes/class_array.html#class-array-method-sort-custom . Subsequent grade proc additions still require the P04 event/save contract; this correction does not claim those effects complete.

**Modify:** `front_run.gd`의 `_hit/take_damage/heal_target/choose_target`와 저장; JSON progression/capstones의 구조 키; tooltip; 모델 테스트. **Create 제안:** `scripts/replan/front_combat_events.gd`는 아래 사건 처리 추출이 실제 중복을 줄일 때만 도입, 범용 ECS/이벤트 버스 재설계 금지.

**인터페이스 제안:** `resolve_hit(event: Dictionary) -> void`; event 필수값 `{event_id, parent_event_id, attack_id, source_id, target_id, side_at_launch, kind: BASIC|SECONDARY|COUNTER, damage_type, is_ranged, base_damage}`. 기본 적중만 기본타 카운터를 증가. secondary/counter는 추가타를 다시 발동하지 않는다. 동일 event_id 재처리는 피해0. 범위 대상은 거리→ID로 정렬, 대검은 공격 방향 앞쪽만. 점령 반경과 전투 사거리 변환은 P02 계약을 따른다.

기존 연결을 다시 구현하지 않는다: 숙련 방패/궁병/대검/기병/마법사, 숙련·정예 사제, 공통 보호막/둔화/경직. 아래 수치의 책임 원본은 JSON `unit_progression`/`capstones`; 여기서는 빠진 트리거/경계만 특정한다.

| 역할 | 아직 연결할 등급 효과 | 경계 및 합격 반례 |
|---|---|---|
| 방패 | 정예 인접 아군 보호 | 8초, 자기 제외, 인접은 전투거리1.5 권장, 거리→ID 1명. 대상 없으면 재사용 소비 안 함 |
| 궁병 | 정예 5타 관통 | 주표적 뒤쪽 전투거리1 내 적 1명 권장. 원 피해의50%, 추가타 카운터/집중사격 재발동 없음 |
| 마법사 | 정예 4타 반경 증가 | 네 번째 기본 발사에만 반경0.8; target cap은 T3와 독립. 한 번의 범위 적중은 공격1회 |
| 창병 | 숙련 돌격자 둔화·정예 반격 | 실제 brace 저지 성공 때만, counter 6초. 양 창병 상호 반격 무한루프0 |
| 대검 | 정예 4타 방어 감소 | 물리 방어-10/2초, 같은 원천 갱신·동일 효과 max. T3와 합산0, 방어 하한0 |
| 기병 | 정예 재돌격 | 3초간 근접 표적 없음 및 피해받음 없음이라는 이탈 기본값. 단순 공격 cooldown 대기만으로 충전하지 않음 |
| 거인 | 숙련 구조물 누적·정예 충격파 | 구조물 연속 적중 후 다음 공격 +10%씩 최대30%, 비구조물 적중 뒤 stack0 권장. 3번째 기본타 주변2체40%, 본체 중복 제외 |
| 암살자 | 숙련 지원 급소·정예 교란 | support=사제. 유효 ambush 첫타에1.4×1.1, 준비 지연0.3은 경직 아닌 준비/다음 공격 시각 연장, 대상 면역6초 |
| 비행 | 숙련 활공·정예 급강하 | 실제 이동 중 ranged 피해-10%; 첫 교전 경직과8초 재사용. 정지 중 감소0, 저장 재개로 재충전 불가 |

**T3:** 열 병종의 capstone 전부 별도 테스트. 등급과 티어는 독립: T3 명사수의 집중 사격은 숙련 조건이 충족될 때25→35% 강화, T3 대검과 정예 대검의 같은 방어 감소는 한 효과. T3 방패 경직 감소는 방어 자세일 때만, 무한 면역 아님. 기병/암살자 피해감소는 자기 상태로 시간 저장. 비행 재교전8초와 정예 급강하8초는 각각의 능력 준비 여부를 보존한다.

**피해 순서 권장:** 기본 공격/공성/집중 보너스 → 물리/마법 방어 → 조건부 받는 피해 배율(서로 다른 효과 곱, 동일 효과 max) → 보호막 → HP. 소수 피해는 모델 float 유지, 화면 반올림만. 추가 피해 기준은 이차 피해의 방어 적용 전 값을 정의해 방어 이중 적용하지 않는다.

**합격:** 전 역할 양진영 대칭(성장 획득은 Ward만), 2/5생존 임계/재정비/맵 이동/재도전, T3×grade 교차 조합, 취소/빗나감/죽은 표적은 적중횟수 증가0, 1000사건 스트레스 재귀/중복0. 상대 정예는 authored wave 데이터로만 부여하며 플레이어 성장에서 자동 추론하지 않는다.

### P05 — 영웅 3명과 수동 전술

**Modify:** 모델·화면·저장·JSON heroes; 모델/화면 테스트. **API 제안:** `select_hero(hero_id: String) -> bool`, `hero_skill_targets() -> Array`, `cast_hero_skill(target: Dictionary) -> bool`.

새 원정 첫 준비 전에3명 중1명 선택. 영웅은 별도1슬롯, 출전18용량/징조륜/병사 생존등급과 분리. 원정 도중 교체 없음, 재도전은 진입 snapshot의 같은 영웅. 영웅 지상 개체는 점령력1이라는 권장값. HP/공격/사거리/능력 수치는 JSON heroes를 소비한다.

| 영웅 | 실제 소비처 | 구현 상세 권장값 |
|---|---|---|
| 아우렐 | 전열 인접 방어·군기 보호막 | 인접 반경1.5, 자기 제외, 받는 피해8% 감소. 지정영역 반경4 내 가까운6체에40/5초, CD30초 |
| 리라 | 대공/지원 우선·표식 | 사거리 내 공중→사제→거리/ID. 단일적 표식 ranged 받는 피해20%/5초, CD25초 |
| 세렌 | 최저 체력비율 치료·범위 회복 | 기본3초/15HP, 자기 제외·사거리 내 비율→거리→ID. 지정영역 반경4 가까운5체30HP+둔화 정화, CD35초 |

수동 능력: 전투 중 선택→유효 대상 미리보기→확정, ESC/빈 공간 취소. 범위 선택은 지도좌표로 변환; 대상0/사망영웅/정지 상태/재사용 중이면 비용·CD 소비0. pause 중 미리보기는 가능하되 확정은 재개 후 다시 검증. 맵 전환은 HP계승/CD초기화, 재정비는 CD동결. 전투 중 사망하면 해당 라운드 불참, 정상 재정비 진입에만50%HP 1회 복귀 권장; 패배에서 부활로 결과를 뒤집지 않는다.

**합격:** 무효 표적/중복클릭/로드 직후 무료 시전0, 양진영 죽은 대상 제외, 보호막 비합산, 세렌 치료로 공격 트리거 발동0, 사망→재정비 부활 중복0. 이름·서사·최종 외형은 후보/권장 상태를 유지하고 전투 기능 PASS와 최종 캐릭터 승인을 분리한다.

### P06 — 전체 UI/UX와 결과의 인과 설명

**Modify:** `front_screen.gd`, `scenes/replan/front_slice.tscn`, `project.godot`, 화면 테스트. **Create 제안:** `scripts/replan/front_menu.gd`/`scenes/replan/front_menu.tscn`(메인·설정), `scripts/replan/front_results.gd`(결과 표시), `scripts/replan/front_settings.gd`(ConfigFile 설정). 기능 단위로만 분리하고 런타임 모델 복제 금지.

```text
메인 [새 원정 / 이어하기(불가 사유) / 설정]
 → 영웅 선택 → 원정 지도(현재 도전 가능 맵만 진입)
 → 준비 [상단5맵 한줄 + 공통자원 + 룰렛/내정/전선]
 → 전투 [근접 전투 화면 + 공세예보 + 영웅 + pause/1×/2×]
 → 재정비 [부상/성장/손실 → 치료/시설/동원 → 다음 라운드]
 → 맵 결과 [생존/점령, 기본/거점/정산 분리 → 다음 맵]
 → 최종 원정 결과 → 메인
패배 → 맵 진입 재도전 / 메인 (저장 없는 구형은 불가 사유)
```

맵 선택이라는 이름으로 이전 맵 자유 재방문·자원 파밍을 추가하지 않는다. 완료 맵은 요약 열람, 현재 맵은 이어하기, 미래 맵은 잠김. 결과에는 실제 ledger의 수입/지출, 손실·생존·등급 변화, 탑/점령 획득과 승리 이유만 표시한다. 고정 문구로 ‘좋은 전략’ 판정을 날조하지 않는다.

**와이어 배치(1280×720 기준 권장):** 상단0~56 공통자원·5맵 리본,56~104 공세 예보; 중앙104~480 전투; 하단480~720 선택 탭/카드. 전투 화면을 지도 전체 도로로 되돌리지 않는다. 좁은 화면에서는 카드 스크롤, 전장 비율은 보존. 실제폰트/클릭영역 검증 후 좌표조정 가능.

**가독성/설정:** 본문18px 이상·조작영역44px 이상을 기준으로720p/1080p 검수; 텍스트 배율100/125/150%, master/music/SFX 분리, 모션감소·화면흔들림0옵션, 색+아이콘+텍스트 병행. 키보드 focus 순서/Enter/ESC/Tab, 입력 재지정 충돌 안내. Android터치는 이후 실제기기 gate이며 PC캡처로 PASS 금지.

**합격:** 새 원정→건설→전문화→징조륜→출전→영웅→재정비→저장→메인→이어하기→결과를 실제 입력으로 수행. tab교체/정지/배속이 모델에 추가 명령을 만들지 않음. 불가 버튼에 이유, 만석·골드부족·잠긴시설·손상저장 경로,150%텍스트 잘림,키보드전용 왕복 검사.

### P07 — 투명 아트·아틀라스·모션·5개 맵

**Modify:** `front_art.gd`, 상태 사건을 읽는 `front_screen.gd`, 기존 `ROSTER_PROVENANCE.md`, 해당 자산 카탈로그/QA/캡처. 신규 경로는 소비처 Visual Requirement가 고정된 뒤 exact scope에 등록한다. 이 계획은 실제 생성/최종승인 기록이 아니다.

| 자산군 | 준비할 범위 | 연결·합격 조건 |
|---|---|---|
| Ward10+Veil10 병종 | 각 idle/move/attack/hit/death, 지원은 cast/heal; 기병 charge·창병 brace·비행 glide·암살 approach | 최소5상태×20외형의 커버리지표. 정적 원화 복제는 move/attack 완료가 아님 |
| 영웅3 | 기본5상태+active cast, 죽음/라운드복귀 | P05 actor/state/event와 결합, 카드 원화와 전투 sprite 분리 |
| 시설 | 현재 catalog13종(2뿌리+10전문화+군수소), T3 심화 식별 | 13개별 식별 그림, 잠김/선택/생산중은 UI 상태, T3는 원화+표식 조합 가능. 카드 불투명 종이 배경을 전장 오브젝트로 쓰지 않음 |
| 방어탑 | 한 개 형태의 중립/Ward/Veil 소유 상태, 발사·파손 필요 상태 | 한 전선 한 개. 소유색만 아닌 문장/형태 표식, RGBA 발사효과 |
| 전장5 | 성채외곽→수호전진→접전→장막전진→베일성채 | 각 별도맵 배경, 중앙 통행 영역 유지. 금빛/청색에서 자색으로 소재·조명 연속성 |
| 분리소품 | 성벽조각/깃발/수목/바위/침식체 등 필요한 종류 | 배경과 별도 RGBA, 중앙 이동영역 외부 anchor만 허용. 생성 개수보다 재배치 가능성 검증 |
| UI/효과 | 병종/영웅/시설 아이콘, 투사체/보호막/둔화/경직/표식/치료, 메인/워드마크 | 실제 버튼/상태/사건 ID를 소유하며 장식용 대량 후보 금지 |

**스타일:** 동화풍 판타지 수채 SD2.5~3등신, 궁병/마법사와 재질·윤곽 일치. Veil은 인간의 검은 갑옷 색변경이 아니라 catalog의 갑각수·포자괴 등 몬스터 실루엣. 기존 이미지들은 비교자료이며 재기획 이전 승인을 자동 복원하지 않는다.

**공정:** 이미지 모델 자세별 원화→실알파 검수→공통발피벗/방향 정렬→Aseprite frame/tag/duration 조립→PNG/JSON export→원화/출력 hash·alpha QA→모델사건 연결→GPU실전캡처. Aseprite 사용 여부는 자산별 `source_generation`, `alpha_processing`, `aseprite_assembly`, `runtime_animation`을 따로 기록한다.

현재 방패4자세는768셀/pivot(384,700)을 보존한다. 과거512/pivot(256,448) 문구에 맞추려고 승인 픽셀을 무조건 축소하지 않는다. 소비자는 자산별 frame_size/pivot를 읽는다. 정적 Veil의 Aseprite 왕복과 Ward 파생본의 Aseprite 미사용을 혼합 표기하지 않는다.

**모션 계약:** 공격은 windup→release/contact→recover. 모델 attack_id에당 피해1회, 경직/사망으로 발사전 취소, 발사후 투사체는 원진영/목표ID/위치/잔여tick 저장. 단일탄 표적 사망은 소멸, 범위탄은 발사지정위치 착탄이라는 권장값. 모션 감소에서도 피해시점과 판독 가능한 최소 효과는 유지. 장식 흔들림이 공격 준비를 가리지 않음.

**합격:** RGBA 알파0 실제존재·가짜체커보드0·흰테두리/잔여종이 검수·셀침범0·발위치 흔들림·무기/손/날개 연속성; 밝은/어두운/실전 배경 모두 확인. 20외형 혼합720/1080과23캐릭터 상태 전이, 빗나감/취소/사망 실제 타격동기화. 사람 최종아트는 별도. 새 파일/이미지는 사용 끝난 임시파일과 원본 provenance를 구별한다.

### P08 — 53라운드 콘텐츠·경제·오디오·밸런스

**Modify:** JSON `wave_templates/wave_cycle/maps`, 모델의 공세 읽기, 예보/결과 소비처. **Create 제안:** `tests/replan_campaign_test.gd`(자원주입 없는 정책 실행/로그), `scripts/replan/front_audio.gd`(사건 기반 SFX와 music bus). 유닛/효과 사양 완료 전에 단순 pressure하향을 최종안으로 고정하지 않는다.

**콘텐츠:** 10/10/10/11/12라운드, 각3공세=159공세 슬롯에 stable `map_id/round_id/wave_id`와 등장순서·지연·병종·수·등급을 매핑. 생성식 유지 가능하지만 expanded 결과가 예보와 같아야 한다. 현재 빠진 창병/암살자/비행병을 단계적으로 도입한다. 처음 등장하기 전 위협/두 대응을 예고하고 해당 준비 시점에 적어도 두 합법 대응 경로가 있어야 한다. 고정 RNG 결과가 모든 대응을 제거하면 설계 실패다.

**권장 학습 순서:** 1맵 전열/궁병/치료,2맵 기병/창병과 점령,3맵 범위/특수후열,4맵 공중/공성/유지,5맵 기존 역할 혼합. 이는 독립 보스 시스템이나 추가병종 약속이 아니다. 각 맵 마지막 라운드의 정예 공세는 명시 데이터로 예고한다.

**측정:** 고정 seed 0~29 × 방어/진격/경제전문화/혼합/최소행동 정책. 저장재개 on/off 한 쌍, 조기승리/지연승리 같은 seed 비교. 기록 필수: 완료맵·라운드·승리유형·순자산·원천별수입·치료지출·사망역할·등급생존·시설이용·대기포화·점령상실/회복·실제전투시간. RNG 재굴림·자원주입·결과상태 강제는 자연완주 증거에서 제외한다.

**합격 목표:** 완주 가능한 자연 경로 최소 하나 먼저 확인하고, 그 다음 두 개 이상의 서로 다른 투자정책이 전체원정 성공하는 표본 확보. 전 seed 성공/모든 전략 동률을 요구하지 않는다. 특정 공세에서 합법 대응0, 영구적 UI진행불가, 순자산 무한증식은 차단 결함. 승률 목표/최종난이도는 사람 플레이 후 정하고 자동정책 패배를 인간 불가능으로 단정하지 않는다.

**오디오:** 버튼/건설/동원확정/공세예고/공격/치료/점령/승패를 사건에 연결. 동시 효과음 제한16개 초깃값, 같은 소리 짧은 중복 억제, 중요한 경고 우선. 음량/음소거 저장·재개 실제 적용, 시각 대체 알림. 없는 음원은 무료/현재보유·권리확인 소스 우선, 출시권리 미확인을 자동승인하지 않음.

**성능:** 대상 PC와 해상도를 기록한 실제 export에서 대표/최대병력/장시간을 측정. 초깃목표60FPS의16.7ms 프레임예산, p95/p99·메모리·로딩을 함께 기록. 측정기기 없이 목표를 PASS로 쓰지 않는다. Android는 별도기기와 품질옵션 gate.

### P09 — 정본·패키지·최종 검증

**Modify:** 현재 상태/로드맵/승인 결정/사람용 Blueprint source·생성 결과, `project.godot`와 export 설정(착수 때 실제경로 확인), 플랫폼·자산권리 owner. 과거 PDF를 새 구현의 증거로 인용하지 않는다.

**순서:** 패킷별 실제 coverage 대조→Blueprint milestone 재발행·전페이지확인→현재 PR/부모/중첩 재조회→허용된 보호절차로 통합→main exact SHA readback→동일 SHA export→시작/이어하기/원정/결과/종료 smoke→사용자 실행파일·조작법·알려진 제한 전달. 부모 PR의 미해결 정본 충돌을 우회해 현재main에 직접 push하지 않는다.

**필수 분리:** 문서 검사 / 모델 자동검사 / GPU실행·입력 / 기기·성능·접근성 / 사용자 재미·최종아트 / main통합 / 실제 출시·등급·권리. 앞 단계PASS가 다음 단계PASS가 아니다. Steam PC가 주대상, Android는 기존 약속대로 출시근접 실제기기 검증을 남긴다. 공개배포·유료계정·법률/스토어 제출은 이 명세로 자동 실행하지 않는다.

### 4. 이번 문서 작업의 검증과 다음 인계

현재 코드/씬/JSON/Blueprint/열린PR/채택Base를 대조했다. 발견한 instant capture·가변시계·T3출생정보 누락·군수 한도 고정·메인/전체모션 공백은 위 패킷의 반례로 연결했다. 이전 268모델 검사 및 GPU 결과는 **이전 구현의 증거**이며 이번에 신규 기능을 검증한 결과가 아니다.

5회 문서 자체 검토 관점: (1) 사용자 확정/권장값 구분 (2) 시계·저장·retry 안전성 (3) 경제·출생·효과 상호작용 (4) UI·투명아트·모션 실제소비처 (5) Git/계약/완료 주장 경계. 이 검토는 독립 작업자의 실행검증이나 Human 승인으로 표기하지 않는다.

이번 문서 정적 검증: P00~P09 10개 섹션·신규 절의 로컬 Markdown 링크·코드 fence 짝 검사 PASS, 변경4문서 `git diff --check` PASS, 기존 scope 회귀6개 PASS, 채택 Base 검사에 대한 `PROJECT_SCOPED_BUILD: PASS`. `BASE_RAW_RESULT: FAIL`은 기존 승인 예외8개 protected runtime 경로로 남아 있으며 이번에 우회/수정하지 않았다. 검토 중 예제의 새 run ID 차이와 30Hz 점령 경계 표현을 교정했다. 게임 실행/신규아트/전체원정/Human은 이번 작업에서 NOT_RUN.

다음 구현 시작점은 P00→P01이다. 이유는 점령·스킬·영웅·투사체를 더하기 전에 시간과 저장 계약이 안정되어야 이후 구현을 다시 뜯지 않기 때문이다. 최종수치/영웅서사/아트확정은 아직 별도이며, 전체작업 준비 문서가 존재한다고 전체제품 또는 모든 패킷의 런타임 준비가 완료된 것은 아니다.

## 이전 구현 계획과 검증 이력

## 2026-09-13 transparent Ward and facility continuation

Bounded consumer fix: non-shield Ward currently uses opaque ward-roster, special upper-row and building-tree. Reuse explicitly user-approved local alpha-only processor, preserve RGB/source hashes, no redrawing or new art approval. Alternatives: image-model re-extraction (identity/alpha drift risk observed), whole pale-color removal (reject armor damage), edge-connected paper removal with enclosed pale details retained (ADAPT existing tested tool). Outputs ward-roster-alpha.png, ward-special-alpha.png (upper610px verified gutter), building-tree-alpha.png. Existing shield motion and Veil remain unchanged. Native static Aseprite only if available; never claim motion. Tests fail on missing alpha outputs, RGB changes or pale anatomy erasure; actual Godot consumer alpha and mixed/building GPU after wiring. Margins/weapon cross-cell and enclosed paper remain explicit quality limits; don't mislabel as final animation.

## Survival progression foundation and first consumers

Current Blueprint recommends surviving2 completed rounds -> veteran,5 -> elite, no blanket HP/ATK multiplier. Add optional integer survived0..53 to each unit, increment living Ward survivors once on BATTLE -> REFIT/VICTORY (including early capture), not defeat/pause/reload. Carry through map/retry snapshots. Label grade in hover without claiming all grade skills implemented. First actual consumers: veteran greatsword primary hit+20%; veteran archer same-target third and later streak? Resolve literal '연속3타째' as every third consecutive same-target hit, reset on target change. Store attack streak/target to preserve reload; no recursive extra hits. Grade0 unchanged. Remaining grade skills require shared timed status system and follow in later steps. RED2/5 thresholds, no duplicate completion, defeat exclusion, disk/retry, target-switch streak and primary-only bonus. No new art.

Target-role detail readback correction: progression row constrains assassin backline search to4 combat distance (12 model x); nearest fallback outside. Movement target-facing is restricted to assassin/flying to preserve other roles.224 model checks plus UI/save/default PASS,5-view static review no blocking findings, later tests cover both-side backward approach and frozen cooldown. Full campaign still loses second map in3seed; no balance success inflation.

## Target-role completion

Connect catalog archer anti-air priority, flying/assassin backline priority and assassin first backline hit1.4x/10s cooldown. Technical defaults: backline roles archer/mage/priest; archer prefers flying only within current attack reach, otherwise nearest target; flying prefers nearest enemy ground backline, assassin nearest backline. No teleport/invulnerability or physical collision engine invented. Move toward selected target (including behind) rather than always toward enemy base. Existing nearest fallback and priest ally heal retained. Both factions. Assassin cooldown advances only BATTLE, stores optional0..10 unit field, clears at map entry. RED target ordering/air-out-of-range fallback/first burst and repeat cooldown; local+GPU+independent review. Reuse role-counter benchmark in earlier section, no new art claimed.

## Campaign retry transaction

Next dependency: capture map-entry state before any preparation purchase or spin; defeat-only retry restores exactly gold/HP/facilities/queue/RNG/previous completed points, rolling back failed-map gains. Store one nonrecursive checkpoint in v6. Validate checkpoint with same model validator before live mutation, require same map/history and pristine PREPARE round1/time0, reject nested checkpoints. Old v1–v5 saves have no authentic entry evidence: keep playing but retry unavailable until next map; do not invent historical gold/RNG. UI uses existing outcome button with explicit unavailable reason. RED no retry during battle, loss rollback, repeat retry after disk, malformed checkpoint atomic rejection. No new images or save-file deletion.

## Whole-game continuation: sequential campaign

Latest user explicitly sets whole-game implementation as goal, superseding slice-only stopping. First missing dependency: five labels currently decorative, model always maps[0]. Implement current_map, archived global owned-point ids, next-map transaction only from victory, survivor HP/gold/buildings/reserve carryover, reset combat references/clocks/bases, dynamic round count and terminal final-map UI. Savev5 defaults old saves to map0/no prior points, validates ids before mutation. RED blocked early advance, carryover/no healing/no enemy carry, no duplicate points, all five maps/final boundary, disk resume. ADAPT campaign continuity from official Kingdom developer interview https://news.xbox.com/en-us/2024/10/08/kingdom-two-crowns-call-of-olympus-out-now/; REJECT its island revisiting, use project sequential canon. Reuse existing background as explicit temporary visual, not five-map art completion. Entry snapshot retry is next dependent step, not falsely included in this first transaction. Full product authorization does not authorize main bypass or final art approval.

## First-map pressure experiment and provisional adoption

After role connections, compare unchanged starting resources across four scripted policies/three seeds, then pressure0.4/0.5/0.6/0.8. Baseline1.0:12 losses. Pressure0.4 paid mobilization:3 seeds win round2 by citadel capture; other6 tested runs lose rounds3–4. Pressure0.5:8 losses. Adopt catalog first map0.4 provisionally, not final balance; other maps unchanged. Persist run pressure with savev4; v1–v3 migrate1.0. Regression covers v3 staggered composition, v4 JSON roundtrip and invalid/missing pressure atomic rejection. Existing PDF predates tune. Cavalry role multiplier currently targets unit combat, not structure damage; siege multiplier remains giant-specific. Five-view independent review corrected partial charge accumulation across interrupted advances; no other blocking findings. Strategic diversity remains unverified.

## Follow-on cavalry / spear counter

Existing blueprint defines cavalry2distance continuous advance then first hit1.5x and spear stationary0.6s halves charge damage. Implement as paired roles, not isolated cavalry buff. Reuse _tick/_hit/unit snapshot; movement accumulates charge capped2 for cavalry, stationary brace capped0.6 for spear, movement clears brace, attack consumes charge. No added manual command/art. Both factions. Optional per-unit charge/brace fields default0 for old saves, strict finite bounded validation before restore. UI keeps base stats plus implemented capability. RED charge versus ordinary target, uncharged normal hit, braced spear50%, unbraced spear normal, real movement/stop/save continuations; GREEN local+GPU+review. Numeric base stats unchanged. AOE official unit-counter benchmark reused, role mechanics from project not copied.

## 2026-09-13 shield role connection

Bounded existing combat completion, user explicitly delegates technical decisions without repeated approvals. Source: Blueprint build input shield row, frontal ranged25% defense stance. Definition: automatic stance when live shield has a live enemy within its melee reach (therefore holds position); forward is +x Ward/-x Veil. Only archer physical shots reduced, not magic/melee/rear attacks. Derived state avoids new save fields, applies to both factions' shield equivalents. No base HP/damage/production tuning.

Benchmark https://www.ageofempires.com/learn-to-play/military-and-economy-aoe2/ differentiates arrow-resistant frontliners from generic HP; ADAPT role-specific counter, REJECT importing its numeric armor system. Alternatives: global shield HP buff (reject blurs weaknesses), always-on ranged reduction (reject removes stance), derived engaged stance (selected fits auto-combat and existing25% spec). REUSE _hit and tooltip; no new art/toolkit. RED frontal25%, rear/magic/unengaged unaffected, symmetry; GREEN model/UI/default/GPU and independent review, then multi-seed policy diagnostics. Existing front_run/front_screen/test scope only.

## Follow-on: wave data parity

Final109 checks add full-state midwave comparison (absolute1e-9 floating tolerance, exact categorical/RNG strings) and v3 legacy resave. Five-perspective independent static review found no blocker. Exact JSON text initially differed by int/float representation and ~3e-15 timer rounding; no production quantization introduced to hide this. Scope5PASS, project-scoped PASS / Base raw protected-path FAIL retained.

Executed RED missing wave API -> GREEN107 model/UI/save/default. New firstwave arrives1enemy at5s,5by6.6s; thirdwave B5shield+2greatsword; round2A4shield+3archer. Midwave save restores no duplicate; v2 legacy instantaneous behavior retained and unknown profile rejected atomically. GPU20damage15units and3shieldposes. Current four baseline policies still lose round2; paid_mobilization first refit5allies11enemies and2G healing. No optimal shift search or multi-seed fairness evidence yet. This is implementation parity, not tuning success. Renderer inspected at720p/1080p outputs; independent review separate.

Compare actual `_tick` repeated instantaneous wave against Blueprint cycle, 3% round scale and0.4s arrival. ADAPT Into the Breach official https://www.subsetgames.com/itb.html telegraphed threats: forecast and spawning share composition, not separate hard-coded guesses. Alternatives: tune counts now (reject until parity), merely change preview (reject mismatch), shared data-driven composition with scheduled arrivals (selected). Existing first-map pressure1.0, no invented difficulty modifier.

Plan: RED first event count1 at5s, five events by6.6s, third wave B, round2 ceil count4/3, mid-wave save no duplicate; implement `wave_composition(round,wave)` plus event crossing at0.4s. Existing elapsed and wave cursor suffice; do not add redundant scheduled queue. Save v3 records `wave_rules`; older v1/v2 keeps legacy instant-wave rules for that run, new runs use staggered rules. UI/forecast, automatic policy comparison, GPU, review and owners updated together. Same exact runtime/test paths; no asset or combat-stat change.

## 2026-09-13 Omen transaction implementation

Execution complete for this transaction: RED missing API/UI then GREEN99 model checks + UI/save/default + scope5. GPU front-omen.png and natural combat19damage/17units/3shieldposes. Review found pending saves could inject unavailable units; corrected allowed-pool validation before state mutation with RED regression. JSON version membership was type-sensitive; explicit numeric comparison fixes real disk load. v1 overflow rejected without mutation, no truncation. Five-perspective independent rereview clean (not independent runtime). Real-resource paid_mobilization policy reaches first refit with5allies/9enemies versus0allies in three free-only policies, but all lose round2. Policy does not optimize shifts and does not establish balance/Human PASS. No new Base reusable module proven; project-only lesson is validate pending reward source and reservation together. Below checklist records original plan.

User continuation authorizes existing blueprint completion without routine approval. Scope: front_run.gd/front_screen.gd, existing model/UI/capture tests and current owners. Spec: Human Blueprint 룰렛의 구체 처리 / 경제. No new art/combat stat tuning/Base lock change.

Research: Slotbound official https://store.steampowered.com/app/4906570/ (3x3 + autobattle, ADAPT acquisition-to-battle connection; REJECT jackpot positioning); Commander Quest https://flywaygames.com/en/game/commander-quest (composition/synergy, ADAPT visible unit outcome). Current immediate-award preview is not the specified choice loop. Alternatives: tune combat now (defer: acquisition incomplete); weighted capacity only (leaves decision absent); complete observation/adjust/confirm transaction (selected: connects player agency). REUSE existing model/UI/catalog/art, no toolkit.

- [ ] RED: confirm API; no early grant; weighted capacity rejection without RNG/payment; three shifts; line bonus choice; repeat confirmation; pending save restoration.
- [ ] Model interfaces: queue_used, spin_required_capacity, can_spin, shift_board, bonus_options, omen_rewards, confirm_omen. spin starts pending transaction, reserves 4*maximum pool unit cost. Building mutation/round start locked while pending. Snapshot v2; accept v1 only when weighted queue fits, no unit discard or rejected-save overwrite.
- [ ] UI: 3x3 cards, six cyclic row/column controls, remaining moves, eligible bonus choice, predicted rewards, single confirmation. Shared spin guard, existing art.
- [ ] Local model/UI/default + scope + GPU + review, then real-resource policy comparison using confirmation.
- [ ] Current owners/readback, selective commit/current branch CI, disposable test saves to user deletion review folder.

## Current completion loop: research -> specification -> connected implementation -> playtest

Latest execution evidence (supersedes the single-policy 79-check sample below): 81 model checks, UI/save/default scene PASS. Three actual-resource policies at seed1947 and 0.1-second steps: reinforcement/ranged/mixed all DEFEAT in round2; first refit allied0, enemy12/12/13, gold22/101/25, home HP1000; recovery spend0. No resource injection. These are reproducible policy diagnostics, not proof of optimal-play impossibility. Next investigate production, surviving enemy carryover and unimplemented acquisition decisions before tuning numbers. Independent five-perspective read-only review found no P0-P2 blocker; execution evidence remains separately owned by local test output and GPU capture. Recovery dialog first had overlapping direct children; fixed with one VBox content owner and visually rechecked.

Latest user correction: the loop is whole-game completion through comparable-game research, specification, integration and testing, not cosmetic-only iteration. Each unit starts with an implementation plan and covers model/data/UI/assets/save/tests as applicable. Do not stop merely because one screenshot improves; identify the next gameplay gap. Routine technical decisions are delegated; core user rules, protected Git and final art/Human boundaries remain.

Current gap map: (1) first-map preparation/combat/refit/result and viable initial choices, (2) roulette adjustment/commit/reserved capacity, (3) remaining troop abilities/T3/grades, (4) heroes, (5) five-map campaign/retention, (6) complete transparent art/motion, (7) front door/settings/release. Current UI-only next priority is superseded by connected first-map loop; opaque Ward art remains required, not discarded.

### Paid recovery integration

PLAN before code: connect existing Blueprint economics/recovery to refit decisions. ADAPT Thronefall economy-versus-defense preparation (https://store.steampowered.com/app/2239150/Thronefall/), The Last Spell rebuilding between attacks (https://store.steampowered.com/app/1105670/The_Last_Spell/), Commander Quest army composition (https://store.steampowered.com/app/2697930/Commander_Quest/). REJECT adopting kill-all night endings, hero turn control or new resources. Price is our existing Blueprint formula, not a copied game's price.

Spec: heal_cost reads replenishment price units[row12], missingHP/maxHP and economy.heal_coefficient; heal_unit accepts living allied injured units only during PREPARE/REFIT, charges once and restores maxHP. No resurrection/automatic healing/combat-command heal. UI previews each target cost and remaining gold; insufficient funds disables actions. No save-schema change. This creates the concrete choice of recovery versus construction/specialization using the same gold.

Implemented model and real frontline recovery dialog. RED missing transaction/entry -> GREEN 79model checks and UI/save/default gate. Tests include rounding, repeated request, enemy/dead/absent target, affordability, combat rejection, two buttons targeting separate units and save readback. GPU revealed overlapping dialog children: replaced separate auto-fitted children with a vertical content container, re-rendered successfully. Capture output/front-recovery.png is a labeled UI boundary fixture, not proof that the mixed army survived a full round.

Real-resource first-map policy (no HP/gold injections): one general barracks per preparation until two, then archer specialization, free spin, affordable healing, deploy reserves and advance. Result DEFEAT round2, refits1, recovery_spend0. This is a reproducible weak-policy observation, NOT evidence all strategies fail or healing is balanced. Next loop compares multiple initial spend/production policies and identifies missing role/queue rules before tuning numbers. Do not silently tune the blueprint to make one scripted policy win.

## Mixed-role follow-up: plan, implementation, evidence

User approved continuing the mixed-role readability loop. PLAN: reproduce shields/archers/mages/priests/spears on both sides, add bounded read-only hover inspection instead of increasing physical spacing or shrinking art, verify unchanged model and two resolutions. Existing Control tooltip is reused (https://docs.godotengine.org/en/stable/classes/class_control.html#class-control-private-method-get-tooltip); no third-party component or art replacement.

RED missing inspection → GREEN actual faction/role/current-max HP, outside-field blank, dead exclusion, snapshot preservation, maximum6 rows plus overflow. Model68/UI-save/default PASS, scope5 PASS. Natural scenario19damage/16units/shield3poses unchanged. Separate TEST-ONLY mixed fixture spawns5roles per side then runs0.6s actual combat:10units/10damage. Not ordinary acquisition, encounter balance, whole campaign or Human evidence.

GPU720/1080 captures are output/front-mixed.png and front-mixed-1080.png. Added actual InputEventMouseMotion through viewport and waited0.8s;720 capture shows native tooltip with live Ward names/HP. Independent five-pass reviewer found no blocking code issue; hover runtime capture was added after that review and inspected by main agent. Remaining: Ward non-shield cards are opaque (visible white rectangles), some Veil edges remain, mixed units overlap, hover-only is not keyboard/touch accessibility. Next plan prioritizes Ward transparent combat consumers; do not label mixed art complete. Model/save/approved art untouched.

## 2026-09-13 approved bounded combat-readability plan and readback

User approved the preceding plan: reproduce crowding, compare shrink/stagger/status approaches, keep combat rules, verify two resolutions. PLAN was presented before BUILD. REUSE existing atlas/draw consumer; ADAPT stable four-depth stagger (0/24px rear offset); REJECT global shrinking and physical collision changes because those alter readability or combat tuning beyond this unit. Godot custom drawing order supports the final status overlay: https://docs.godotengine.org/en/stable/tutorials/2d/custom_drawing_in_2d.html . Existing Into the Breach threat-readability research remains context, not a claim that this layout replicates that game.

- [x] RED: screen test rejects missing bounded projection.
- [x] BUILD: front_screen.gd owns display-only unit_draw_anchor; depth-sort a copied array, preserve all model coordinates, draw health status after sprites, remove repeated attack text/placeholder unit frames.
- [x] VERIFY: eight co-located consecutive IDs have distinct bounded anchors; projection does not mutate snapshot; 230 simulation steps match control snapshot; existing 68 model checks/UI-save/default gate pass.
- [x] GPU: real natural battle remains19damage/16units and shield3/3poses. 1280x720 and1920x1080 inspected. Extra capture path exact-scoped. No new art generated.
- [x] REVIEW: independent five-pass scope/rules/state/visual/tests review found no blocker. Residual sprite/bar overlap remains; eight-ID pattern repeats. Not collision-free or Human PASS. Current capture is predominantly shields/Veil; full mixed-role visual stress remains pending.

Base remote still d830c0f6; pinned v9.4.3 unchanged, raw protected-path FAIL/scoped BUILD PASS. Parent PR/main remain unmerged. Next plan: mixed-role crowding stress and role/status readability before first-map end-to-end completion. Rollback this display/test change; save schema and simulation need no migration.

## 2026-09-12 continuous improvement: forecast and supply observability

Outcome: RED missing-query/UI checks preceded implementation; GREEN model 68/68, actual UI/save/default-scene gate, 109 selected existing contract tests and 12 scoped/alpha/motion tests. GPU 1280×720 capture: 19 damage events /16 units, shield windup/impact/recovery 3/3. Five-scope independent review found paused/terminal production wording; corrected and tested, including paused+locked substring regression. `git diff --check` clean. Base raw FAIL is the same eight approved runtime paths; project scoped BUILD PASS, not Base raw PASS. Full 559-test suite not rerun in this iteration; the historical `_base_recovery` fixture problem remains unverified. Human/device/accessibility/1920×1080/full-product NOT_RUN. Exact remote CI is checked after commit, not inferred from these local results.

Next continuous unit: reproduce overlapping active soldiers at normal display size and improve combat readability without changing combat rules; then complete missing motion and blueprint/runtime gaps in bounded, researched units. No repeat approval for routine implementation; final art/core semantic decisions and protected integration remain distinct. This is not whole-game completion.

Direction: keep the approved single-front / three-tab / time-limited-round loop; let players read actual incoming pressure and why a selected facility is not supplying units. Approval: latest user requested fresh Base read, benchmarking and implementation/improvement without routine reapproval. This is existing UI/production scope, not approval for unrelated PR absorption, release or core-rule replacement.

Freshness: project implementation source47726ad79e0c49fffbee9b8b9ff2778d44137723; current-task PR259 remains stacked/draft, main and other PRs read-only. Base remote main d830c0f6 was fetched and its AGENTS, intake and continuous-work owners read. Its receipt/HiGodot/2-round-review policies are DRIFT_REFERENCE_ONLY; project v9.4.3 lock, scoped validator and explicit five-pass review are retained. No migration of adapter/generated contracts. Root planning checkout and historical three-front owners are COMPATIBILITY/history; this worktree's current context and actual preview consumer own implementation status. No age-based deletion.

Work modes: PLAN benchmark/alternatives → BUILD existing FrontRun/FrontScreen queries and labels → REVIEW tests/render/readback. Project UX skill supplies the hypothesis: can players identify the next threat and explain why production is paused? Human task/think-aloud remains NOT_RUN; tests establish only correct displayed information.

benchmark_preflight_state: PASS for this bounded UI improvement. Existing 12-game research and current actual consumer were compared before selecting new work. No reusable external system is needed: REUSE FrontRun clocks/catalog and Godot controls, ADAPT presentation. No cross-project code absorption or new plugin/framework.

| Source and evidence (read2026-09-12) | Observed pattern | Project fit / disposition |
|---|---|---|
| https://media.gdcvault.com/gdc2019/presentations/Into%20the%20Breach%20Postmortem%20Final.pdf, pp13–17 text | Telegraphed attacks shape threat/response decisions | ADAPT actual upcoming wave preview; REJECT replacing real-time combat with fully deterministic grid turns. PDF text inspected, not full talk watched. Official homepage timeout was not substituted for body evidence. |
| https://store.steampowered.com/app/2239150/Thronefall/ About | Build by day, defend by night; economy/defense trade-off | ADAPT clear preparation/production freeze feedback; REJECT kill-all night ending because user requires timed rounds. |
| https://store.steampowered.com/app/2697930/Commander_Quest/ About | Deck/army synergy and covering weaknesses | ADAPT implemented role labels and troop capacity information; no claim to reproduce its proprietary systems. |
| https://store.steampowered.com/app/4906570/Slotbound_Demo/ About | 3×3 summons feed an autobattler; absorption/evolution | REFERENCE_ONLY for summon-to-army readability; REJECT jackpot rescue/absorption as automatic additions. Demo marketing is not measured balance evidence. |
| https://docs.godotengine.org/en/stable/classes/class_progressbar.html | Native percentage control and shared Range/Control behavior | ADOPT native progress bar bound to actual production clock, no bitmap progress decoration. |
| https://www.aseprite.org/docs/frame-duration/ | Frame properties define duration | RETAIN shield native timing checks; static pose reuse is not newly drawn motion. |

Three alternatives: (A) modal next-wave popup, clear but interrupts viewing/input; (B) permanent full army dashboard, rich but crowds1280×720; (C) compact shared two-line forecast plus selected-facility status. ADOPT C for lowest display cost, same game rules, easy removal, and no new save schema. Risk: incorrect future prediction; mitigation: read-only model query and equality test against actual spawned role counts. Risk: masking battlefield; mitigate upper strip outside soldier path. No game assets copied from references.

Acceptance: preview first/next/refit waves and none after victory; queries do not mutate RNG/snapshot; production distinguishes producing/frozen/full/locked/empty; UI reads model each frame without recreating panels every clock tick; locked selected facility cannot appear upgradeable; save/production/combat regressions and native motion remain valid. Existing numeric data is unchanged. Blueprint's more elaborate per-wave variation remains unimplemented; preview intentionally tells the truth about current runtime, not a fictional future implementation.

Learning: reuse existing catalog/clock owner for UI and verify against spawn behavior, rather than a second authored forecast table. Project-only lesson retained here; no Base promotion claimed. Rollback: revert this UI/query commit without touching saves, art, Base locks or other PRs.

**Goal:** 사용자가 병영 건설 → 생산 → 출전 → 단일 전선 전투를 직접 확인한다.
**Authority:** 2026-09-11 최신 사용자 ‘인게임에서 전투하는 거, 병종건설도 볼 수 있게. 이미지 연결’. 기존 기획-only 상태를 이 구간에 한해 supersede한다.
**Spec:** `docs/design/OMENWARD_BLUEPRINT_BUILD_INPUT_20260911.json` 및 사람용 Blueprint v3.
**Architecture:** 기존 3전선 빌드는 보존한다. 별도 `scripts/replan/` 모델과 화면, `scenes/replan/front_slice.tscn`을 추가한다. 검토 JSON을 직접 읽어 병종/가격을 중복 정의하지 않는다. 카드형 후보 이미지를 검토용 실행 장면에서만 사용한다.
**Scope:** 수호 성채 1맵, 60초 라운드, 3웨이브, 재정비, 기본 자동전투, 병영 두 계열/T2 전문화, 생산/출전, 저장. 10라운드 생존/본진 점령 조건. 테스트는 2라운드 경계를 집중 검증한다.
**Excluded:** 영웅, T3/숙련/정예 능력, 전 캠페인, 최종 아트 승인, 출시. 기본형 공격/범위/치료 이외 병종 특수 능력은 미구현 표시.

## Tasks and acceptance

- [ ] `tests/replan_slice_test.gd`: 실 모델의 건설 비용, 계열 경계, 생산, 전투 피해, 라운드 동결, 저장 동일성, 슬롯 잠금 RED → GREEN.
- [ ] `scripts/replan/front_run.gd`: `construct(id)`, `upgrade(slot,id)`, `deploy(id)`, `begin_round()`, `advance(delta)`, `snapshot()`, `restore(data)` 구현. 준비 중 경제/전투 동결, 잘못된 입력은 비용 차감 없이 실패.
- [ ] `scripts/replan/front_screen.gd`, `front_art.gd`, `scenes/replan/front_slice.tscn`: 상단 1줄 지도, 중앙 전투, 하단 내정/징조륜/전선. 이미지 아틀라스는 원본 중복 없이 region으로 소비. 불투명 카드임을 명시.
- [ ] 실제 버튼 경로/전투 화면 캡처와 headless 테스트. 기존 기본 장면 진입은 유지하고 새 장면 직접 실행.
- [ ] Decisions/Active Context/Roadmap에 실행 경로와 증거 한계를 함께 갱신. 기존 v3 PDF는 구현 전 검토판으로 유지.

## Learning map

Blueprint JSON → FrontRun (비용/계열/생산/전투 판정) → FrontScreen (입력/표시)
Candidate atlas → FrontArt (region cache) → 병종 카드 / 내정 카드 / 전장 토큰
FrontRun snapshot → user://replan-front-v1.json → validation → restore

## Sources / choices

- ADOPT Godot AtlasTexture region/filter_clip: https://docs.godotengine.org/en/stable/classes/class_atlastexture.html
- ADAPT Godot saving games: versioned all-or-nothing local snapshot; no arbitrary resource path loading. https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html
- REJECT replacing old three-front services in-place: unrelated open PR overlap and rollback risk.

## Rollback and evidence ceiling

Launch the unchanged `scenes/main/main.tscn` for legacy build. No old saves overwritten. New art remains GENERATED_CANDIDATE; Aseprite NOT_USED for these static atlas sources. A test PASS is not animation/Human/balance approval.

## Actual result / implementation learning map

**PARTIAL / INTEGRATION_BLOCKED**. This worktree now starts at the new preview (1280×720); original scene remains available. The new application name isolates preview saves from the old build. Current source is the three `scripts/replan/` files and the shared Blueprint JSON; the review PDF remains the pre-implementation edition.

| Input / owner | Processing | Visible output / verification |
|---|---|---|
| Build button, Blueprint building_tree | FrontRun.construct/upgrade checks phase, cost, family and slots | List portrait and supply role; model and UI tests |
| Combat time | FrontRun.advance fixed substeps, waves, production, nearest target damage/healing | Single battle area, HP bars, reserve; GPU capture |
| Candidate source PNG | FrontArt caches AtlasTexture region, no new pixel copies | Building cards / allied and Veil tokens; candidates only |
| Save button | JSON snapshot, temporary write then rename; restore validates before mutation | Same economy/units/production; isolated test save round-trip |

### Verification performed

- RED: missing model. GREEN: 39 behavioral checks covering construction, tier/family rejection, affordability, production, damage, refit, capture slots, disk-format restoration and malformed saves.
- UI RED: atlas image escaped allocation at 443×443. GREEN: texture sizing order corrected, real build button/price and file save/load paths pass.
- Default scene headless smoke and live Godot 4.7.1 editor launch. Actual build / roulette / start / pause buttons were exercised with the editor scoped to this worktree. Other projects were not mutated.
- Reproducible GPU capture: `tests/replan_capture.gd`; 23 simulated seconds, 19 damage events, 16 active units. Output `output/front-building.png` and `output/front-battle.png`; no compositing or edited screenshot.
- Local gate: `tools/validate_replan_slice.ps1 -Godot <console executable>`. It fails immediately on a failed test. Remote workflow consumption is not yet established.
- Pinned operating validator: **FAIL** because protected runtime paths changed. New user BUILD authorization is recorded, but the old planning-only policy still prohibits these paths. No policy removal, version-lock replacement or bypass performed.
- Parent planning PR exact head 42498548: fresh read found canon-v45/contract/validate-contract-binding failures. No main merge claimed.

### Five full-scope review passes / corrections

1. Authority + code/data/UI/art/tests: preserve old build, scope new run, reject cross-family upgrades; candidate images not final sprites.
2. Authority + code/data/UI/art/tests: corrupt save checks found negative gold/faction/NaN/facility mismatch acceptance; validate before mutation.
3. Authority + code/data/UI/art/tests: real JSON converts numbers to float; normalize occupation owners to integers to preserve unlocked slots. Round-1 refit now unlocks next-round T2.
4. Authority + code/data/UI/art/tests: GPU/UI inspection found oversized images and stale capacity label; fixed layout and refresh key. Remaining token overlap and static art are not cleared.
5. Authority + code/data/UI/art/tests + Git: rerun gates, retain protected-path failure, parent CI failures and unimplemented requirements. No full-completion claim; worktree remains active for correction.

### Material claims / remaining work

- Visible construction and damage simulation: MACHINE + RENDER evidence, not player approval.
- Image connection: candidate card/atlas consumption only. No Aseprite in these seven source sheets. The historical Aseprite slash pilot is not connected.
- NOT IMPLEMENTED: transparent battle sprites, slash frames, true tower artwork, full body movement/attack, full roulette manipulation/bonus, T3/rank/hero skills, specialized assassin/flying/cavalry effects, five-map campaign.
- Balance, accessibility (full), performance profiling, release rights/compliance, Human: NOT_RUN. Dense tokens overlap; this is not acceptable as final combat art.
- Operating contract and parent PR reconciliation must happen before normal main integration. Automated tests do not override this boundary.

### Use

Open this worktree's `project.godot`, press F5. Build a general barracks in 내정; use the free 징조륜; deploy reserve cards in 전선; start the assault. Production queues more units during combat. At refit, select the barracks to specialize. Save/load keeps this preview run only.
## 2026-09-13 shared status consumers

Final local readback:268 model checks/0failures; UI/save/default gate PASS; alpha/scope13 PASS; GPU14damage13units, shield3/3 and mixed10/10 plus status fixture true. Existing art bytes unchanged. Raw Base protected-path result remains FAIL and PROJECT_SCOPED_BUILD PASS. No natural five-map completion; three seeded campaign policies still lose map2round2. Reusable lesson remains project-local: cleanse cardinality and interrupted charge are cross-status invariants, and pending attacks must be invalidated both at status application and save restore.

Execution: RED missing API; GREEN265 model; independent review found cleanse removed all slows and interrupted partial charge persisted; RED corrections ->267. Saved stunned+pending strike RED ->validation correction. UI missing status RED ->actual tooltip fields. GPU fixture initially consumed barrier on same-step giant attack, then delayed only fixture enemy cooldown to observe actual barrier7/stun0.3/movement0.85 after0.25s. No fake progression or new animation claim. Five-pass independent re-review found no additional blocker; model final count and exact remote checks require final readback.

Bounded implementation under continuing whole-game delegation. Spec: HUMAN_BLUEPRINT_REVIEW common-effect paragraph and build input unit_progression. Reuse existing fixed substep model and dictionary save, no timer/plugin dependency. ADOPT Godot delta-based simulation (https://docs.godotengine.org/en/stable/tutorials/scripting/idle_and_physics_processing.html); ADAPT control/immunity separation illustrated by Guild Wars 2 defiance (https://wiki.guildwars2.com/wiki/Defiance_Bar), not its boss bar or numbers. REJECT per-actor wall-clock timers (pause/save drift) and additive slow/shield stacks (contradict spec).

- [ ] RED in existing model tests: capped strongest slow with independent expiry, shield absorption/expiry/no sum, stun cancel/immune/freeze, actual veteran shield fourth hit/cavalry charge/mage slow/priest cleanse+elite overheal, save rejection without mutation and map reset.
- [ ] GREEN existing front_run: optional statuses dictionary {barrier,barrier_time,stun,immune,slows:[{amount,time}]}; missing means inactive. At most16 slow strengths, finite0..0.5 and time0..60. Reject malformed effects. Tick all statuses before actions; active-at-step-start stun blocks that substep, cancels unlaunched windup. Same/lower active stun cannot refresh. Barrier strongest remaining, replace timer only when new amount is at least existing; cap1000/time60. Slows equal strengths refresh duration, distinct strengths expire independently. Production consumers use existing spec values only. Map transition clears temporary states/counters. Refit freezes them.
- [ ] Add read-only status text to existing unit hover, preserve alpha/motion assets, exercise native screen/GPU plus model suite. Record exact evidence/remaining effects and five-view independent review; commit/push current task PR only.
# 2026-09-16 current user override — three-front overview

This section supersedes the single-front presentation/assignment only; P04 remainder is paused for this request. Three fronts simulate concurrently under one clock, shared economy/queue/facilities/capacity and common Ward/Veil bases. Default view is a schematic strategic minimap; choosing north/center/south inspects that front at existing close-battle character scale. Camera changes do not advance, stop, heal or redeploy units. Deployment commits to the selected front. New games use an explicit three_v1 marker; old saves remain single-front, never auto-repartitioned.

Recommended implementation detail under delegated authority: existing three control points become one midpoint/tower per front in new games; ownership continues to unlock 6+held slots and income. Existing five maps and round/wave sequence stay; distribute the existing wave total cyclically across fronts instead of tripling enemies or resources. Four initial soldiers distribute 2/1/1. Defend the common base; enemy base capture remains one common endpoint. No jungle, river, extra currency, cross-front movement or copied reference artwork introduced.

ADAPT Riot's three routes between shared bases and overview readability; REJECT its three towers per lane, jungle and hero economy. Source: https://www.leagueoflegends.com/en-sg/how-to-play/ . ADOPT Godot CanvasItem dynamic indicators for the functional minimap, not replacement raster art: https://docs.godotengine.org/en/stable/classes/class_canvasitem.html . Reuse current transparent units and battle backdrop in inspection.

Order: (1) model/save RED tests for isolation/capture/towers/dispatch/roundtrip/legacy/future markers; (2) minimum front field and point mapping; (3) overview/select/back UI and runtime inspection; (4) whole regression and independent five-pass review; (5) append 2026-09-16 daily summary to the existing monthly worklog/PDF, no new versioned worklog; (6) push the current task branch and exact-head CI readback. Do not bypass protected main or integrate unrelated PRs.
# 2026-09-20 현재 승인 묶음: 통합 준비 + 첫 맵 정보/입력 검증

기존 계획 누적. 게임 수치/저장/자산 승인과 다른 작업 폴더를 보호한다. 부모 PR258의 정확한 준비 파일 분류와 PDF 바이너리 교정을 연결했다. PR258/259는 Draft 유지하며 이번 묶음으로 전체 병합을 승인한 것으로 보지 않는다.

실행 순서: 기존 Godot gate → 예보 회귀 테스트 RED → 실제 순환 배분 그대로 전선별 읽기 전용 예보/UI → 신규 출정의 건설/징조륜/전선 선택/배치/전투/재정비/결과를 실제 화면·공개 조작 경로로 확인 → 독립 검토/범위 검사/원격 정확한 HEAD 확인. 기존 전체 gate PASS, 저장 59 checks PASS, 화면 PASS를 확인한 뒤 시작했다.

재미 가설 F1: 플레이어가 어느 전선으로 증원할지 예보·현재 병력을 보고 설명할 수 있다. 반례: 숫자만 보고도 전선 배분을 오해하거나 확대 후 다른 전선이 멈춘다고 생각한다. 자동 검사는 예보/실제 배분 일치와 화면 전환의 무변경만 확인한다. F2: 시설/징조륜 선택의 자원 비용과 실제 입대 결과가 이해된다. F3: 재정비의 회복/건설 선택이 다음 공세 대응으로 이어진다. 사람 관찰은 첫 맵 한 판에서 선택 이유·예상과 실제 차이·반복 피로를 짧게 기록하며 현재 HUMAN_NOT_RUN이다. 화면 캡처/AI 평가로 재미 PASS를 선언하지 않는다.

실행 근거: 첫 예보의 전선 키 누락 RED → `wave_forecast().fronts`의 실제 병종 순서/공세 offset 순환 배분 → 화면의 전선별 합계/선택 병종 및 legacy 회귀 GREEN. 초기 숫자를 잘못 가정한 테스트는 실제 pressure0.4의 2갑각수+1절단수로 교정했다(전선별1명); 제품 수치는 건드리지 않았다. 예보 query는 snapshot/RNG를 변경하지 않고 반환 배열 수정은 모델에 전파되지 않는다.

Godot4.7.1 `tools/validate_replan_slice.ps1` 전체 local gate PASS(모델, 저장59, 화면, 기본씬). Python 기획 관련63개와 BUILD exact scope9개 PASS. GPU `--first-map-only`는 병영1개/초기120G에서 정상40G 지불, 정상 무료 징조, 적은 아군 수 전선으로 실제 배치, 실제 마우스 확대/버튼 복귀, 재정비2회 후 3라운드 본진 점령으로 끝났다. 251G/아군 본진1000; 회복·특화·다른 정책 또는 모든 맵 성공 근거는 아니다. 화면은 `output/front-first-map-prepare.png`, `front-overview.png`, `front-inspection.png`, `front-first-map-refit.png`, `front-first-map-result.png`. capture의 UI 갱신 지연은 촬영 전 기존 refresh 호출로 보정했으며 제품 UI를 우회해 규칙을 바꾸지 않았다.

독립 검토1/2: 준비 모드가 작은 운영-only 변경을 가로채는 P2 발견 → 부모8810ae00에서 기존 모드 우선순위 보존, 동일반례 RED→GREEN. 그 외 제품 수치/저장/승인 자산 변경 없음. 사람 재미·접근성·기기·최종아트·전체캠페인·release NOT_RUN. 실제 원본 Base 보호경로 FAIL9개와 승인된 PROJECT_SCOPED_BUILD PASS를 함께 유지한다.

마감 readback(2026-09-20): 독립 검토자의 한정 재확인에서 기존 운영-only 허용/누락 intake 거절/제품 경로 거절 5개 PASS로 finding 해결. 부모 PR258 `8810ae00` 원격10 PASS/1조건부SKIP. 첫 Linux Godot import 종료가 native double-free(134)로 실패했으며 같은 HEAD 실패 작업을1회 재실행해 PASS(35505734755 attempt2); 원인을 영구 수정한 것은 아니다. BUILD PR259 `e5a5bb92` 원격6 PASS(기존5개 workflow + adapter1개), 로컬=origin 확인. 두 PR은 Draft 유지; main `90493888` 그대로. GitHub 병합·전체게임 완료로 표현하지 않는다.

기록/정리: 기존 `C:/Users/user/Documents/증빙서류/9월 증빙서류/OMENWARD_원본근거/README.md`에 당일 수행·입력 한계·커밋·검증·실패 이력을 추가했다. 이번에는 PDF 재발행 없이 원본만 누적하며 다음 월간 발행 대기다. 새 저장 테스트2폴더40파일은 SHA256 대조 후 `C:/Users/user/Downloads/OMENWARD_DELETE_REVIEW_20260912/first-map-review-20260920`에 복구 manifest와 함께 이동했다. 실사용 저장·기존 사용자 파일·27개 addon import 변경은 보존; 직접 삭제 없음.
