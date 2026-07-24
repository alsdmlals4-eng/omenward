# 오멘워드 현재 구현 상태

- 갱신일: 2026-07-24
- 기준 main: `95e5ae225262f2427f21d5b7e4a03fb24e7eed6c`
- V2 설계: `V2_SPEC_APPROVED`
- V2 정본: `V2_CANON_CANDIDATE`
- V2 구현: `V2_IMPLEMENTATION_NOT_STARTED`
- 기존 구현: `LEGACY_C1_C2_C3_PROVEN`
- 사람 검증: `HUMAN_QA_NOT_RUN`

이 문서는 승인된 V2 설계, 현재 main의 실제 구현과 실행 증거를 분리한다. 문서 승인이나 파일 존재만으로 구현·검증 완료를 주장하지 않는다.

## 1. 상태 용어

| 용어 | 의미 |
|---|---|
| `V2_SPEC_APPROVED` | V2 제품 규칙과 열린 계약이 사용자 승인됨 |
| `V2_CANON_CANDIDATE` | 승인 문서가 PR 브랜치에 있으나 main 병합 전 |
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
- 교체: 독립 9칸 생성, 스테이지 전설 제한, 구형 럭키·이동 거래, 기존 보관 계약.

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
- 교체: 점령력 합산, 중앙 접전지에 구형 중간거점 상태기 재사용, 기존 런 수명주기.

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

## 4. V2 미구현 영역

다음은 승인됐지만 아직 실제 구현과 실행 증거가 없다.

- 세 가변 원형 릴.
- 안정 index X 교체와 append.
- 비가역 가로 이동과 세로 이동.
- immutable SpinSnapshot.
- 숨은 럭키 truth table.
- 위험 주기 전설 제한.
- 보관함 4칸과 무손실 결과 대기.
- MapRun 영속 상태와 StageFlow.
- 스테이지 준비·일반 전술계획·위험 실시간 규칙.
- 3기 묶음 웨이브와 10초/20초 전환.
- 고정 8초 전투 반경 기반 접전지.
- V2 전술 UX.
- 100,000시드·경제·판매·비축 시뮬레이션.
- 10~15분 사람 플레이와 1080p·720p 가독성.

## 5. 현재 판정

```text
TECHNICAL_BASELINE_IMPLEMENTED
+ LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
+ LEGACY_C2_BATTLE_OBJECTIVE_REMOTE_PROVEN
+ LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN
+ V2_SPEC_APPROVED
+ V2_CANON_CANDIDATE
+ V2_IMPLEMENTATION_NOT_STARTED
+ CORE_LOOP_V2_NOT_PROVEN
+ HUMAN_QA_NOT_RUN
```

## 6. 다음 게이트

1. V2 문서 PR 병합과 정본 검증.
2. 순수 RouletteBoardResolver 분리 Plan Mode 승인.
3. 물리 릴 도메인과 snapshot 구현.
4. 조작·럭키·전설·보관 거래.
5. MapRun·웨이브·접전지.
6. V2 UX와 사람 플레이.

문서 PR만으로 제품 구현을 시작하거나 `CORE_LOCK_V2`를 선언하지 않는다.
