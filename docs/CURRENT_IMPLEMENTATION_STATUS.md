# 오멘워드 현재 구현 상태

- 조사일: 2026-07-23
- 기준 main: `227f6678839d32b8ec3d0f109664bcb63356fe08`
- C1 구현 검증 head: `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9`
- C1 최종 검증 run: `29926598807`
- C2 구현 검증 head: `496157d0b87ab71ea2c9f25780f21df9f68b67f3`
- C2 최종 검증 run: `29936497790` (`Validate Core Contracts`)
- 프로젝트 코어: `CORE_CONFIRMED` / `CORE_LOCKED`
- 판정:
  - `TECHNICAL_BASELINE_IMPLEMENTED`
  - `C1_ROULETTE_CORE_REMOTE_PROVEN`
  - `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`
  - `CORE_VERTICAL_SLICE_PARTIAL`
  - `CORE_LOOP_NOT_PROVEN`
  - `HUMAN_QA_NOT_RUN`

이 문서는 파일 존재, 승인 계약 구현, 원격 실행 증거, 사람 플레이 증거를 분리한다. 상태가 충돌하면 최신 실제 코드·데이터·테스트와 이 문서를 우선 확인한다.

## 1. 상태 용어

| 용어 | 의미 |
|---|---|
| `IMPLEMENTED` | 실제 파일과 실행 경로가 존재함 |
| `PARTIAL` | 구성요소 일부가 존재하지만 제품 End-to-End 계약 전체가 닫히지 않음 |
| `PROVEN` | 요구 계약과 최신 원격 실행 증거가 함께 존재함 |
| `NOT_PROVEN` | 파일 또는 테스트가 있어도 제품 계약 전체 증거가 없음 |
| `NOT_RUN` | 해당 실행·사람 검증을 하지 않음 |
| `FALLBACK` | 승인값 부재를 숨기지 않고 기존 승인 계약을 재사용한 가역 기술값 |

## 2. 기술·데이터 기준선

| 영역 | 현재 증거 | 판정 |
|---|---|---|
| Godot 프로젝트 | Godot 4.7.1 Standard, Compatibility, 960×540 논리 화면, 1920×1080 출력 | `REMOTE_PROVEN` |
| 상태 소유 | `GameSession`, `StageRun`, `BattleSimulator`, `CombatClock`, `DataRegistry`, `DeterminismService` | `IMPLEMENTED` |
| 공용 병종 | 공용 10 archetype, Tier·Rank·FactionVisual, 공용 점령력·구조물 피해 태그 | `REMOTE_PROVEN` |
| 경제·건설 | 기본·접전지·거점 수입, 식량, 거점 revision 기반 건물 활성·비활성·폐허 | `REMOTE_PROVEN` |
| 웨이브 | 튜토리얼 W1~4, 정규 W1~20, 60초 출격 시계 | `IMPLEMENTED_COMPONENT` |
| 테스트 | C1·C2·전투·경제·건설·웨이브·우회 headless 및 Python mutation 계약 | `REMOTE_PROVEN` |

## 3. 검증된 C1 룰렛 핵심

`C1_ROULETTE_CORE_REMOTE_PROVEN`:

```text
3×3 결정론적 보드
→ 중앙 가로줄 선행 판정
→ 8개 완성선·등급
→ 출처 병영·유닛 또는 금화
→ StageRun 보관·라인 배치
```

- 최종 C1 증거는 run `29926598807`이다.
- 이동권·럭키·고정 상위 템플릿·100,000시드 분포는 `C1U_PENDING_USER_DECISION`이다.

## 4. C2 전투 목적 루프 — 검증 완료

검증된 구현:

```text
같은 라인 유닛 교전
→ 중앙 접전지 점령·교착
→ 적 중간거점 점령
→ 건설권·건물 효과·시간 경제 전환
→ 라인별 성문 공격·붕괴
→ 적 본진 공격 또는 W15 전설 보스 처치
→ 전장 상태 기반 승리·패배
```

구현된 책임:

- `UnitArchetypeProfile`이 공용 `capture_power`와 `structure_damage_tags`를 소유한다.
- 방패 1.25, 일반 근접·기병 1.0, 원거리·지원·거인 0.5, 암살자·비행 0을 공용 10병종 데이터에 적용했다.
- 각 라인은 중앙 접전지, 양측 중간거점, 양측 성문을 독립 상태로 가진다.
- 한 진영만 범위에 있으면 점령력이 진행되고 양 진영이 있으면 교착으로 정지한다.
- 3초 이탈 유지, 초당 10% 복귀, 5초 안정화와 점령력 상한 2.0을 적용했다.
- 거점 중립화 시 기존 건물 효과를 해제하고, 소유권 변경 시 이전 revision 건물을 폐허화하며, 재점령 뒤 재건설한다.
- 접전지 4금화/60초와 안정 중간거점 2금화/30초를 실제 전투 소유 수에서 계산한다.
- 성문은 라인별 독립 HP·저항·일반/공성 배율·2초 붕괴를 사용한다.
- 적 본진 파괴와 W15 전설 보스 처치는 승리, 아군 본진 파괴는 패배로 `StageRun`을 닫는다.
- 디버그 `stage_victory`·`stage_defeat` 명령은 테스트·개발 fallback으로 남지만 정상 승패의 유일 경로가 아니다.

판정: `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN` — 통합 `Validate Core Contracts`에서 Godot 4.7.1 editor import·전체 headless·runtime smoke와 Ubuntu/Windows × Python 3.12/3.13 계약·문서·Skill 검증을 통과했다 (head `496157d0b87ab71ea2c9f25780f21df9f68b67f3`, run `29936497790`).

## 5. 가역 기술 fallback

다음은 새 밸런스 확정이 아니다.

- 본진의 독립 HP·방어 수치가 승인되지 않아 `StageDefinition.base_max_health`를 선택 입력으로 두고, 미지정 시 승인된 성문 HP·저항·구조물 배율을 재사용한다.
- 중앙 접전지의 별도 점령 시간이 승인되지 않아 승인된 중간거점 점령·교착·안정화 상태기를 재사용한다.
- 전투 시뮬레이터의 0~100 좌표와 목적 반경은 결정론적 테스트 좌표이며 시각 전장 scale이 아니다.

위 항목은 `DECISIONS_PENDING.md`에서 플레이테스트·밸런스 결정으로 관리한다.

## 6. 아직 완결되지 않은 영역

### 6.1 베일의 징조 — `PARTIAL`

- 다음 공세 초 표시는 존재한다.
- 승인된 T-30 라인·병종·수량, T-15 집결·경로, T-5 위험 라인 강조가 없다.

### 6.2 코어 UX — `NOT_IMPLEMENTED`

1. 건설 전 룰렛 확률 미리보기.
2. 룰렛 토큰 장부.
3. T-30/T-15/T-5 공세 전조.
4. 상성·사거리·타기팅 오버레이.
5. 웨이브 종료 후 라인별 원인 보고.
6. 건설 선택 비교 UI.

### 6.3 사람 플레이·콘텐츠 검증 — `NOT_RUN`

- 1920×1080·1280×720 실제 플레이와 가독성 QA.
- 10~15분 코어 재미·학습 검증.
- W1~W20 연속 플레이.
- 100,000시드 룰렛·경제 분포.
- 전투 성능·밸런스 계측.

## 7. 현재 우선순위

```text
1. C3 승인 코어 UX 6종 최소 구현
2. C1U 이동권·럭키·상위 템플릿 사용자 결정 게이트
3. 10~15분 사람 플레이·1080p·720p QA
4. 밸런스 안정화
5. 콘텐츠·아트 확장
```

C3와 사람 플레이 완료 전에는 전체 코어 루프를 `PROVEN`으로 부르지 않는다. 사람 플레이 완료 전에는 `CORE_LOOP_PROVEN` 또는 `CORE_VERTICAL_SLICE_COMPLETE`를 사용하지 않는다.
