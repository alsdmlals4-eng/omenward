# 오멘워드 V2 R1+R2 기획 검수 보고서

- 검수일: 2026-07-26
- 검수 단계: `REVIEW_IN_PROGRESS`
- 대상 Issue: `#69`
- 대상 계획: `docs/superpowers/plans/2026-07-26-omenward-v2-r1-r2-roulette-foundation.md`
- 벤치마크 갱신: `docs/benchmarks/OMENWARD_V2_BENCHMARK_REFRESH_2026-07-26.md`
- 후속 거래 결정: `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`
- 제품 구현: `V2_IMPLEMENTATION_NOT_STARTED`
- 제품 코드 승인: `NO`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- 프로젝트 코어: `docs/PROJECT_CORE.md`
- 실제 구현 상태: `docs/CURRENT_IMPLEMENTATION_STATUS.md`

이 문서는 사용자의 정확한 단계 명령 `기획 완료` 이후 수행한 적대적 검수 결과다. 제품 코드 구현이나 최종 Codex 인계가 아니다. R1+R2 검수 PR 병합 뒤 사용자의 요청으로 live V2 통합 범위까지 적대적 검토를 확장했다.

## 1. 검수 대상

1. R1+R2 패키지 목표와 포함·제외 범위.
2. Issue #69와 구현 계획 초안의 권한·책임 일치 여부.
3. 기존 Legacy C1 보존 경계.
4. 물리 릴·snapshot·session 순수 도메인 경계.
5. 2026-07-26 유사 장르 벤치마크의 근거와 적용 범위.
6. Codex Plan Mode가 다시 결정해야 할 항목과 검증만 해야 할 항목.
7. 제품 구현 승인·완료 표현의 조기 사용 여부.
8. live V2 spin, StageRun/MapRun, 건물·경제·UI, 이동·럭키·확정·보상 거래의 후속 통합 위험.

## 2. 검수 요약

```text
R1_PLUS_R2_SCOPE: SOUND
LEGACY_C1_PRESERVATION: SOUND
PURE_DOMAIN_ISOLATION: SOUND
BENCHMARK_DIRECTION: SOUND
DOCUMENT_AUTHORITY: CORRECTED
BASELINE_REFERENCE: CORRECTED
UX_SCOPE_BOUNDARY: CORRECTED
FULL_INTEGRATION_REVIEW: IN_PROGRESS
TRANSACTION_FOUNDATION_SEQUENCE: APPROVED
PRODUCT_CODE: NOT_AUTHORIZED
```

R1+R2의 기술적 방향과 범위는 유지한다. 후속 적대적 검토는 R1+R2를 확장하지 않고 R3 이후 패키지의 의존성·원자성·수명주기 충돌을 하나씩 사용자에게 제시한다.

## 3. 발견 사항과 조치

### F-01 — 벤치마크 결론이 현재 입력에 기록되지 않음

- 심각도: `BLOCKING_DOCUMENTATION`
- 발견:
  - 유사 장르 비교와 다섯 개선안은 대화에서 승인됐으나 Issue #69와 현재 계획에 기록되지 않았다.
  - Codex가 저장소만 읽으면 해당 결론을 알 수 없었다.
- 조치:
  - `docs/benchmarks/OMENWARD_V2_BENCHMARK_REFRESH_2026-07-26.md`를 추가했다.
  - 채택·UX 한정 채택·후속·제외를 구분했다.
- 판정: `RESOLVED_BY_REVIEW_PR_71`

### F-02 — 기존 벤치마크는 Pre-V2 규칙을 포함함

- 심각도: `HIGH`
- 발견:
  - Issue #2와 기존 벤치마크 문서는 `Roulettebound`, 독립 9칸, T-30/T-15/T-5 등 현재 V2가 대체한 규칙을 포함한다.
  - 기존 문서를 현재 제품 구현 입력으로 직접 사용하면 stale-reference 위험이 있다.
- 조치:
  - 기존 자료는 역사·반응 조사 자료로 유지한다.
  - V2 갱신 문서가 현재 적용 판정을 소유한다.
  - 최신 통합 결정 원장과 충돌하면 기존 벤치마크를 사용하지 않는다.
- 판정: `RESOLVED_BY_ROUTING`

### F-03 — Issue #69의 조사 질문과 계획의 확정 조건이 충돌함

- 심각도: `HIGH`
- 발견:
  - Issue #69는 `RefCounted` 대 `Resource`, token ID 생성 책임을 Codex가 비교·결정하도록 요구한다.
  - 계획은 이미 `RefCounted`와 caller-injected token ID를 전역 제약으로 확정한다.
- 검수 결정:
  - 사용자의 `현재 구조로 일단 잡고` 지시에 따라 다음을 기획 확정으로 처리한다.
    - transient V2 runtime state는 `RefCounted`.
    - token instance ID는 caller가 주입.
    - R1+R2에서 global ID generator를 만들지 않음.
  - Codex는 이를 다시 자유 선택하지 않는다.
  - Codex는 Godot 4.7.1과 실제 저장소 패턴에서 성립하는지 검증하고, 불가능하거나 중대한 위험이 있으면 구현하지 말고 blocker로 보고한다.
- 판정: `RESOLVED_BY_REVIEW_AUTHORITY`

### F-04 — 고정 baseline SHA가 현재 main보다 오래됨

- 심각도: `MEDIUM`
- 발견:
  - Issue와 계획은 Plan Mode 기준으로 `46f6952d...`를 기록한다.
  - 계획 문서가 PR #70으로 병합된 뒤 main이 계속 갱신됐다.
- 검수 결정:
  - Codex의 기준선은 실행 시작 시점의 최신 `origin/main`이다.
  - 최소 조건은 PR #70과 후속 검수 문서 PR이 포함돼 있어야 한다.
  - 오래된 SHA는 계획 생성 당시 조사 기준 이력으로만 해석한다.
- 판정: `RESOLVED_BY_DYNAMIC_BASELINE_RULE`

### F-05 — 설계 점검 구간이 새 정지 페이즈로 해석될 수 있음

- 심각도: `HIGH_PRODUCT_SCOPE`
- 발견:
  - 벤치마크 제안의 `설계 점검 구간`은 강제 일시정지나 라운드제 준비 페이즈로 해석될 수 있다.
  - 이는 실시간 압박과 기존 V2 시간 구조를 변경할 수 있다.
- 검수 결정:
  - 새 코어 시간 규칙을 추가하지 않는다.
  - 기존 Stage·Wave 전환 또는 압력이 낮은 시점에 정보를 묶는 UX surface로만 정의한다.
  - 강제 pause와 별도 planning phase는 미승인이다.
- 판정: `RESOLVED_BY_SCOPE_CLARIFICATION`

### F-06 — 런 청사진 기록이 저장·리플레이 범위로 확장될 수 있음

- 심각도: `MEDIUM_PRODUCT_SCOPE`
- 발견:
  - 런 기록은 프리셋, 리플레이, 온라인 공유, 영구 통계로 쉽게 확대될 수 있다.
  - 코어 PoC의 mid-run save 제외와 충돌할 위험이 있다.
- 검수 결정:
  - 현재 채택은 맵 종료 시 로컬 결과 요약뿐이다.
  - 프리셋 자동 적용, 온라인 공유, 리플레이, 영구 통계 서비스는 후속이다.
- 판정: `RESOLVED_BY_SCOPE_CLARIFICATION`

### F-07 — 벤치마크가 R1+R2 구현 범위를 확장할 위험

- 심각도: `HIGH`
- 발견:
  - 설계 청사진, 브리핑, 인과 보고는 UI·telemetry를 요구한다.
  - R1+R2에 섞으면 순수 도메인 seam과 실행 위험이 커진다.
- 검수 결정:
  - R1+R2 범위는 변경하지 않는다.
  - R1+R2는 primitive snapshot과 결정론적 도메인 결과만 소유한다.
  - UI·브리핑·인과 보고·런 요약은 별도 Plan Mode 패키지다.
- 판정: `RESOLVED_BY_PACKAGE_BOUNDARY`

### F-08 — 휘발성 평가·판매 수치의 장기 정본 사용 위험

- 심각도: `LOW`
- 발견:
  - 사용자 평가 비율과 판매량은 시점에 따라 변하며 일부 과거 자료는 2차 출처에 의존한다.
- 조치:
  - V2 갱신 문서는 공식 상점의 기능 설명만 근거로 사용한다.
  - 가격, 평가 비율, 판매량을 제품 규칙 근거로 사용하지 않는다.
- 판정: `RESOLVED`

### F-09 — R4가 U1·S1 기반보다 먼저 배치됨

- 심각도: `BLOCKING_ARCHITECTURE_SEQUENCE`
- 발견:
  - 기존 로드맵은 R4 원자 확정 뒤에 U1 보상 구성과 S1 PendingReward 저장을 배치했다.
  - 이 순서는 임시 reward payload, 확정 후 live 건물 재조회, 보상 없는 확정 중간 상태, 중복 지급을 유발할 수 있다.
  - Legacy 결과 DTO와 pending 배열에는 `spin_session_id`, `confirm_transaction_id`, `pending_reward_id`, `reward_index`가 없다.
- 사용자 결정:
  - 권장안 `R3 → U1-F → S1-F → R4 → U1-C → S1-C` 승인.
- 조치:
  - `APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`가 U1-F·S1-F·R4 원자성 경계를 소유한다.
  - U1-F는 snapshot-only immutable `UnitRewardPayload`만 소유한다.
  - S1-F는 ID·put-once pending 저장소·ConfirmReceipt 복구만 소유한다.
  - 실제 spawn·AI는 U1-C, 보관·판매·배치·식량은 S1-C가 소유한다.
- 판정: `RESOLVED_BY_USER_APPROVED_SEQUENCE`

## 4. 검수 후 확정된 R1+R2 패키지 경계

### R1

- `RouletteBoardResolver` 순수 seam.
- 중앙 가로줄 선행 판정.
- 8개 완성선.
- 1 / 2 / 3~7 / 8선 등급.
- 금화 75% / 200% / 500%.
- 동일 입력·시드 출처 결정론.
- Legacy `RouletteService` adapter.
- 기존 C1 관찰 결과 불변.

### R2

- caller-injected ID의 `RouletteTokenInstance`.
- transient `RefCounted` 상태 객체.
- 길이 3 이상 원형 릴 세 개.
- 전역 token ID 유일성.
- cursor 정규화와 3개 wrap 노출.
- 최저 안정 index `NORMAL_X` 교체, 없으면 append.
- `SOURCE_BOUND_X` 일반 교체 제외.
- 동일 상태·시드의 동일 정지 결과.
- copy-out 방식의 깊은 불변 `SpinSnapshot`.
- row-major 3×3 board projection.
- 이동·확정이 없는 stopped-only `SpinSession`.

### R1+R2에서 계속 제외

- live `RouletteService.spin()`의 물리 릴 전환.
- StageRun·MapRun·건물·경제·UI 연결.
- TokenSource lifecycle.
- 가로·세로 이동.
- 럭키·이동 아이템·전설 위험 주기.
- `[확정]`·PendingReward V2 거래.
- 설계 청사진 UI.
- 전선 대응 브리핑.
- 전투 인과 telemetry·보고.
- 런 청사진 저장.
- Scene·아트·사람 플레이·분포 시뮬레이션.

## 5. Codex Plan Mode에서 고정된 것과 검증할 것

### 다시 선택하지 않는 R1+R2 기획 결정

- R1+R2 패키지 범위.
- Legacy live spin 유지.
- V2 domain의 StageRun 비연결.
- `RefCounted` transient runtime state.
- caller-injected token ID.
- global ID generator 미도입.
- snapshot copy-out 불변성.
- stopped-only session.

### Codex가 기술적으로 검증할 것

- 실제 preload·class_name·typed Array 충돌 여부.
- resolver DTO와 Legacy result adapter의 정확한 필드 매핑.
- GDScript deep-copy 경계.
- built-in `hash(StringName)` 안정성 또는 고정 salt 필요성.
- invalid state 처리 방식과 typed 반환.
- C1 validator·mutation fixture 변경 최소 범위.
- CI 비용 계약을 유지하는 validator 연결.
- rollback 시 Legacy C1 경로 복구 가능성.

Codex가 고정 결정을 구현 불가능하거나 안전하지 않다고 판단하면 임의로 대안을 구현하지 않는다. 근거·영향·최소 대안을 제안서에 blocker로 제출한다.

## 6. 문서 권한 순서

현재 작업에서 충돌할 때 다음 순서를 사용한다.

```text
최신 사용자 지시
→ docs/PROJECT_CORE.md
→ 통합 결정 원장
→ APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md
→ V2 통합 명세와 세부 책임 원본
→ Issue #69
→ 이 검수 보고서
→ V2 벤치마크 갱신
→ 2026-07-26 R1+R2 구현 계획 초안
→ 기존 Pre-V2 벤치마크와 역사적 계획
```

이 검수 보고서는 R1+R2 구현 계획의 세부 task를 대체하지 않는다. 후속 거래 기반 결정은 R3 이후 패키지 순서와 원자성만 보정한다.

## 7. 최종 인계 전 게이트

다음 조건을 모두 충족하기 전에는 최종 Codex 구현 인계를 발행하지 않는다.

- [x] 사용자가 정확히 `기획 완료` 선언.
- [x] R1+R2 범위 검수.
- [x] 벤치마크 근거 재검증.
- [x] 채택·후속·제외 분류.
- [x] Issue·계획 권한 충돌 해소.
- [x] stale baseline 해석 교정.
- [x] 최초 검수 문서 PR #71의 문서 CI 성공과 main 병합.
- [ ] 전체 V2 통합 적대적 검토 종료.
- [ ] 사용자의 정확한 `검수 완료` 선언.

## 8. 현재 판정

```text
PLANNING_PHASE: COMPLETE
REVIEW_LOOP: IN_PROGRESS
R1_R2_SCOPE: APPROVED_AND_UNCHANGED
TRANSACTION_FOUNDATION_SEQUENCE: APPROVED
ORDER: R3_TO_U1F_TO_S1F_TO_R4_TO_U1C_TO_S1C
PRODUCT_CODE_AUTHORIZED: NO
FINAL_CODEX_HANDOFF: BLOCKED_UNTIL_EXACT_REVIEW_COMPLETE_COMMAND
V2_IMPLEMENTATION: NOT_STARTED
CORE_LOCK_V2: PENDING
```
