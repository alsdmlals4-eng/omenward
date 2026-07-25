# 오멘워드 현재 구현 상태

- 갱신일: 2026-07-26
- 현재 main 기준: `5a9c02b0ed4757c379fd8dfcb89fcc362b8cf185`
- V2 설계: `V2_SPEC_APPROVED`
- V2 정본: `V2_CANON_CURRENT_BY_PR_57_MERGE`
- V2 구현: `V2_IMPLEMENTATION_NOT_STARTED`
- 기존 구현: `LEGACY_C1_C2_C3_PROVEN`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- 잠금: `CORE_LOCK_V2_PENDING`

이 문서는 승인된 V2 설계, 현재 main의 실제 구현과 실행 증거를 분리한다. 문서 승인이나 파일 존재만으로 구현·검증 완료를 주장하지 않는다.

최신 사용자 승인 원본은 `design/APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md`, `design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`, `design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md` 순으로 적용한다. 전설 획득·배치 제한은 후속 승인 문서가 기존 전설 위험 주기 규칙을 대체한다.

## 1. 상태 용어

| 용어 | 의미 |
|---|---|
| `V2_SPEC_APPROVED` | V2 제품 규칙과 통합 결정이 사용자 승인됨 |
| `V2_CANON_CURRENT_BY_PR_57_MERGE` | 승인된 V2 책임 문서와 결정 원장이 PR #57로 main에 병합됨 |
| `IMPLEMENTED` | 실제 파일과 실행 경로가 존재함 |
| `LEGACY_IMPLEMENTED` | 기존 설계 기준 구현은 존재하나 V2와 충돌해 교체 필요 |
| `PROVEN` | 요구 계약과 최신 실행 증거가 함께 존재함 |
| `MIGRATION_REQUIRED` | 보존·교체 경계가 정의됐고 V2 구현이 필요함 |
| `NOT_STARTED` | 해당 제품 구현을 시작하지 않음 |
| `NOT_RUN` | 자동 또는 사람 검증을 실행하지 않음 |

## 2. 기술 기준선

- Godot 4.7.1 Standard.
- Compatibility renderer.
- 960×540 논리 화면, 1920×1080 출력.
- GDScript.
- `GameSession`, `StageRun`, `BattleSimulator`, `WaveDirector`, `RouletteService`, `CoreUxService` 등 기존 상태·서비스 존재.
- 공용 10 `UnitArchetypeProfile`, Tier·Rank·FactionVisual 분리.

기술 기준선 자체는 유지 대상이다.

## 3. 보존하는 기존 실행 증거

### Legacy C1

```text
독립 3×3 결정론적 보드
→ 중앙 가로줄 선행 판정
→ 8개 완성선·등급
→ 출처 병영·유닛 또는 금화
→ StageRun 보관·라인 배치
```

- 검증 run: `29926598807`.
- 보존: 중앙 판정, 완성선, 등급, 금화 75/200/500%, 출처 결정론.
- 교체: 독립 9칸 생성, 스테이지 전설 제한, 구형 럭키·이동 거래, 기존 보관 계약, 상위 등급 계열 고정 템플릿.

판정: `LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN / V2_MIGRATION_REQUIRED`.

### Legacy C2

```text
같은 라인 교전
→ 접전지·중간거점
→ 성문·본진
→ 전장 상태 기반 승패
```

- 검증 run: `29938742864`.
- 보존: 3라인, 공용 병종, 구조물 피해, 전장 상태 기반 승패.
- 교체: 점령력 합산, 중앙 접전지에 구형 중간거점 상태기 재사용, 기존 런 수명주기, 아군 주기적 배치 묶음.

판정: `LEGACY_C2_BATTLE_OBJECTIVE_REMOTE_PROVEN / V2_MIGRATION_REQUIRED`.

### Legacy C3

- 건설 전 확률 미리보기.
- 토큰·출처 장부.
- T-30/T-15/T-5 징조.
- 상성·사거리·현재 대상.
- 라인별 원인 보고.
- 건설 비교.

- 검증 head: `1976c5355124b2ce7d7ef77b8835df0c95710038`.
- 검증 run: `29965348284`.
- 보존: 도메인 snapshot→HUD 경계, 원인 보고, 표시와 규칙 계산 분리.
- 교체: T-30/T-15/T-5 의미, 독립 9칸 확률 미리보기, 구형 토큰 장부.

판정: `LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_NOT_RUN / V2_MIGRATION_REQUIRED`.

## 4. 병합됐지만 제품 구현이 아닌 작업

- PR #57: V2 통합 정본과 GM-01~GM-106 결정 원장.
- PR #65: Skill System v4 재구성 및 사람 플레이 검증 Skill 흡수.
- PR #66: Base 레거시·아카이브 거버넌스 adapter-only 채택.
- PR #67: Base 공용 Skill route와 Godot 에셋 우선 탐색 연결.
- PR #72: R3→U1-F→S1-F→R4→U1-C→S1-C 거래 기반 순서 승인.

이 작업들은 문서·Skill·운영 계약이며 V2 Godot 실행 경로를 만들지 않았다.

## 5. V2 미구현 영역

다음은 승인됐지만 아직 실제 제품 구현과 실행 증거가 없다.

### 룰렛·결과 거래

- 세 가변 원형 릴.
- `NORMAL_X`와 `SOURCE_BOUND_X`.
- 안정 index X 교체와 append.
- 영구 가로 이동과 세로 이동.
- immutable `SpinSnapshot`과 재개 가능한 `SpinSession`.
- `[확정]` 원자 거래와 idempotency.
- 숨은 럭키 truth table.
- 보관형 이동 아이템 상한 3, pending 보상, 무보상 누적 카운터.
- 세션 내 이동 아이템 점증 가격 `nP`.
- 유닛 `PendingReward`와 금화 즉시 지급.
- 전설 결과를 횟수·stage 주기 제한 없이 항상 전설 PendingReward로 생성.

### 병종·능력 성장

- Tier 1부터 계열 토큰 공급.
- 출처 건물 단위 중복 제거와 완성 Tier 가중치.
- 모든 등급에서 선택 세부 병종 유지.
- Tier별 패시브 생성·강화.
- 등급별 액티브 기술 생성·강화.
- 액티브 AI 자동 발동과 병종별 작성 우선순위.
- 전설 배치 충돌 시 동일 출처·Tier·세부 병종의 영웅 등급 payload 2개 조합.
- 과거 `fixed_grade_unit_template_id` 제거 또는 마이그레이션.

### 전장·건설·구조물

- 배치 즉시 출격.
- 라인별 대기 앵커·공격 명령·`HoldRadius`.
- 같은 맵의 wave·stage 상태 연속성.
- 플레이어 전장 생존 전설 최대 1기.
- 두 번째 전설 배치 경고·명시적 동의·커밋 순간 재검증.
- 충돌이 계속될 때 동일 세부 병종 영웅 2기 원자 배치와 rollback.
- 경고 확인 뒤 기존 전설이 사망하면 원래 전설 그대로 배치.
- 고정 8초 비교전 점령과 소유권 지속.
- 전방 건설 권리.
- blocked 일반 건물과 적 교체 거래.
- source-bound X 복원·영구 제거 거래.
- 시간 기반 건설·업그레이드·철거와 50% 환불 경계.
- 직접 공격 가능한 방어탑 예외와 점령 시 소유권 이전.
- 글로벌 수리 예산, 작업자 임금 곡선, 1초 정산 경계.
- 0.001 금화 글로벌 고정소수점 장부.
- 성문 `BREACHED`, 30초 재건, 진행 치유, footprint 활성화.

### 맵런·메타·검증

- Map→Stage→Wave 계층.
- 맵 하나당 독립 game/run.
- 맵·난이도·기록·도감 영구 진행.
- 단일 메타 재화, 전략 해금, 상한형 시작 강화와 respec.
- 반복 clear 보상 100/50/25% 점감.
- V2 전술 UX.
- 100,000시드·경제·판매·비축 시뮬레이션.
- 10~15분 사람 플레이와 1080p·720p 가독성.

## 6. 현재 판정

```text
TECHNICAL_BASELINE_IMPLEMENTED
+ LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
+ LEGACY_C2_BATTLE_OBJECTIVE_REMOTE_PROVEN
+ LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN
+ V2_SPEC_APPROVED
+ V2_CANON_CURRENT_BY_PR_57_MERGE
+ V2_IMPLEMENTATION_NOT_STARTED
+ CORE_LOOP_V2_NOT_PROVEN
+ HUMAN_QA_NOT_RUN
+ CORE_LOCK_V2_PENDING
```

## 7. 다음 게이트

1. 활성 상태·인계 문서가 같은 V2 current 상태를 말하도록 동기화한다.
2. `docs/superpowers/plans/2026-07-24-omenward-core-v2-implementation.md`를 GM-01~GM-106과 후속 승인 수정 기준으로 재검증한다.
3. 첫 구현 패키지의 목표·플레이어 가치·포함·제외·상태 소유·Red 테스트·회귀·롤백을 설계한다.
4. 검증된 중앙 판정을 보존하는 순수 `RouletteBoardResolver` seam과 물리 릴·SpinSnapshot·SpinSession 경계를 우선 검토한다.
5. 사용자 Plan Mode 승인 뒤에만 Codex 제품 구현을 시작한다.
6. 후속 패키지에서 병종 능력, 결과 처리, 전설 배치 제한, MapRun, 라인 명령, 건설·수리·재건을 연결한다.
7. V2 UX·100,000시드·사람 플레이를 실행한다.

문서 정본 병합만으로 제품 구현을 시작하거나 `CORE_LOCK_V2`를 선언하지 않는다.
