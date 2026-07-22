from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]


def write(relative: str, content: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.lstrip("\n"), encoding="utf-8", newline="\n")


def replace_once(relative: str, old: str, new: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{relative}: expected one occurrence, found {count}: {old[:120]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


def replace_all(relative: str, old: str, new: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"{relative}: missing replacement source: {old[:120]!r}")
    path.write_text(text.replace(old, new), encoding="utf-8", newline="\n")


def append_section(relative: str, heading: str, body: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8").rstrip()
    if heading in text:
        start = text.index(heading)
        text = text[:start].rstrip()
    path.write_text(text + "\n\n---\n\n" + body.strip() + "\n", encoding="utf-8", newline="\n")


write("docs/CURRENT_IMPLEMENTATION_STATUS.md", r'''
# 오멘워드 현재 구현 상태

- 조사일: 2026-07-22
- 기준 main: `227f6678839d32b8ec3d0f109664bcb63356fe08`
- C1 최종 검증: head `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9` / run `29926598807`
- C2 구현 후보 head: `a97eb0a68f418c2f0a94f1f1fbfca243c82731bd`
- 프로젝트 코어: `CORE_CONFIRMED` / `CORE_LOCKED`
- 판정:
  - `TECHNICAL_BASELINE_IMPLEMENTED`
  - `C1_ROULETTE_CORE_REMOTE_PROVEN`
  - `C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE`
  - `C2_REMOTE_VALIDATION_PENDING`
  - `CORE_VERTICAL_SLICE_PARTIAL`
  - `CORE_LOOP_NOT_PROVEN`
  - `HUMAN_QA_NOT_RUN`

이 문서는 파일 존재, 승인 계약 구현, 원격 실행 증거, 사람 플레이 증거를 분리한다. 상태가 충돌하면 최신 실제 코드·데이터·테스트와 이 문서를 우선 확인한다.

## 1. 상태 용어

| 용어 | 의미 |
|---|---|
| `IMPLEMENTED` | 실제 파일과 실행 경로가 존재함 |
| `IMPLEMENTED_CANDIDATE` | 구현과 로컬·부분 원격 회귀가 존재하지만 최종 공통 CI 증거가 아직 고정되지 않음 |
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
| 공용 병종 | 공용 10 archetype, Tier·Rank·FactionVisual, 공용 점령력·구조물 피해 태그 | `IMPLEMENTED_CANDIDATE` |
| 경제·건설 | 기본·접전지·거점 수입, 식량, 거점 revision 기반 건물 활성·비활성·폐허 | `IMPLEMENTED_CANDIDATE` |
| 웨이브 | 튜토리얼 W1~4, 정규 W1~20, 60초 공세 시계 | `IMPLEMENTED_COMPONENT` |
| 테스트 | C1·C2·전투·경제·건설·웨이브·우회 headless 및 Python mutation 계약 | `C2_REMOTE_VALIDATION_PENDING` |

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

## 4. C2 전투 목적 루프 — 구현 후보

구현 후보:

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

판정: `C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE / C2_REMOTE_VALIDATION_PENDING`.

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
1. C2 공통 코어 계약 원격 검증과 PR #50 검토
2. C1U 이동권·럭키·상위 템플릿 사용자 결정
3. 승인 코어 UX 6종 최소 구현
4. 10~15분 사람 플레이·1080p·720p QA
5. 밸런스 안정화와 콘텐츠·아트 확장
```

C2 원격 검증 완료 전에는 전체 코어 루프를 `PROVEN`으로 부르지 않는다. 사람 플레이 완료 전에는 `CORE_LOOP_PROVEN` 또는 `CORE_VERTICAL_SLICE_COMPLETE`를 사용하지 않는다.
''')

write("docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md", r'''
# C2 전투 목적 루프 감사·복구 기록

- 기준 main: `227f6678839d32b8ec3d0f109664bcb63356fe08`
- 작업 상태: `C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE / C2_REMOTE_VALIDATION_PENDING`
- 프로젝트 코어: `CORE_CONFIRMED / CORE_LOCKED`
- 선행 완료: `C1_ROULETTE_CORE_REMOTE_PROVEN`
- 별도 결정 게이트: `C1U_PENDING_USER_DECISION`

## 1. 적용 Skill

- `foundation.project-intake` — 범위·보호 대상·중단 조건 고정.
- `foundation.project-core` — 예측→확률 설계→전선 커밋의 결과 인과 보호.
- `foundation.pruning` — C1 완료 뒤 구형 현재 상태·실행 입력 참조 제거.
- `discipline.game-design` — 접전지·거점·성문·본진·승패 계약 대조.
- `discipline.engineering` — 상태 소유·고정 틱·결정론·경제 연결.
- `discipline.qa` — 점령·교착·성문·본진·경제·건물·라인 격리 회귀.
- `foundation.adversarial-review` — 유닛 공격 우회 테스트·영구 교착·유령 건물·허위 승패 공격.
- `foundation.validation-review`, `discipline.integration-review` — 정본·코드·테스트·문서·PR 일치.

## 2. 기계 감사

저장소 텍스트 248개를 조사했다.

- 전투 목적 관련 파일: 88개.
- 구형 현재 상태 후보: 4개.
- 깨진 내부 Markdown 링크: 0개.
- 본진·승리·패배 문맥: 177개.

실제 활성 문제는 C1 진행 중·PR #49 대기·C2 미구현 표현이었으며, Validator·mutation fixture의 구형 문자열은 공격 입력으로 분리했다. 임시 감사 입력과 수집 Workflow는 제거했다.

## 3. 복구한 인과

```text
3라인 교전
→ 접전지 점령 또는 교착
→ 적 중간거점 점령
→ 건설권·생산 효과·경제 전환
→ 같은 라인 성문 공성
→ 적 본진 파괴 또는 W15 전설 보스 처치
→ 자연 승리·패배
```

## 4. 핵심 구현

- 중앙 접전지 3개, 양측 중간거점 6개, 성문 6개, 본진 2개를 `BattleSimulator`가 소유한다.
- 유닛은 적이 없을 때 idle이 아니라 같은 라인의 다음 목적 객체로 전진한다.
- 공용 10병종 데이터에 점령력·구조물 피해 태그를 추가하며 적군 복사본을 만들지 않는다.
- 승인 점령력 0.5·1.0·1.25와 상한 2.0을 실수로 보존한다.
- 양 진영이 범위에 있으면 진행·유지·복귀 없이 교착으로 정지한다.
- 양측 이탈 시 안정 접전지의 교착 표시를 해제한다.
- 거점 소유권과 capture revision이 건물 활성·비활성·폐허·재건설과 식량 한도에 반영된다.
- 실제 전투 소유 수가 접전지·중간거점 시간 수입에 전달된다.
- 같은 라인 공성 유닛의 실제 공격 틱이 해당 성문과 본진에 피해를 준다.
- 적 본진 파괴, 아군 본진 파괴, W15 전설 보스 사망이 `StageRun` 결과를 만든다.
- 전투 목적 상태 변화와 결과를 결정론적 input log에 기록한다.

## 5. 적대적 검토로 추가 수정한 사항

1. `BuildingService`의 Variant 비교를 명시적 bool로 고쳐 Godot 경고-오류 정책을 통과시켰다.
2. 안정 중립 접전지에서도 양 진영 동시 도착을 교착으로 표시하도록 했다.
3. 양측 이탈 뒤 안정 접전지의 교착 표시가 영구 잔류하지 않도록 했다.
4. 성문·본진 회귀가 구조물 메서드를 직접 호출해 실제 유닛 공격 경로를 우회하던 문제를 제거했다.
5. 목적 좌표를 넘나드는 고정 틱 overshoot를 clamp했다.
6. 거점 중립화 시 농장 식량 효과를 해제하고 소유권 변경 시 이전 건물을 폐허화했다.

## 6. 가역 기술 fallback

- 본진 독립 방어 수치 미승인: 미지정 시 승인 성문 프로필 재사용.
- 중앙 접전지 별도 점령 시간 미승인: 승인 중간거점 상태기 재사용.
- 정규화 0~100 좌표: 결정론적 테스트 좌표이며 시각 scale 아님.

이 값은 최종 밸런스 확정이 아니며 사용자 결정·플레이테스트 전 교체 가능하다.

## 7. 검증 현황

구현·적대적 보강 단계에서 다음이 통과했다.

- Godot 4.7.1 editor import.
- 모든 `tests/headless/*_test.gd`.
- runtime smoke.
- C1·C2 Python 계약과 mutation tests.
- 프로젝트 코어·Skill Validator·whitespace.

최종 공통 `Core Contracts` Workflow의 head·run을 고정하기 전이므로 현재 판정은 `C2_REMOTE_VALIDATION_PENDING`이다.

## 8. 미실행

- 1920×1080·1280×720 사람 플레이.
- 실제 전장 가독성과 목적 상태 표현 QA.
- 10~15분 코어 재미·학습 검증.
- W1~W20 연속 플레이.
- 룰렛 100,000시드·경제·전투 밸런스·성능 계측.
''')

# README
replace_once("README.md", "> 현재 상태: **C1 룰렛 핵심 계약 원격 검증 완료 / 전투 목적 루프·사람 플레이 미완결**", "> 현재 상태: **C1 룰렛 REMOTE_PROVEN / C2 전투 목적 루프 구현 후보·원격 검증 진행 / 사람 플레이 미완결**")
replace_once("README.md", "→ [다음] C1U 이동권·럭키·100,000시드 결정\n→ 전투를 접전지·거점·성문·승패에 연결", "→ C2 전투 목적 루프 구현 후보·원격 검증\n→ [결정 게이트] C1U 이동권·럭키·100,000시드\n→ 승인 코어 UX 6종 최소 구현")
replace_once("README.md", "→ 승인 코어 UX 6종 최소 구현\n→ 승인 코어 UX 6종 최소 구현", "→ 승인 코어 UX 6종 최소 구현")
replace_once("README.md", "현재 저장소에는 Godot 기술 기준선과 원격 검증된 C1 룰렛 핵심 계약이 존재하지만, 룰렛 유틸리티·전투 목적 루프·핵심 UX는 완결되지 않았다. 현재 판정은 `TECHNICAL_BASELINE_IMPLEMENTED`, `CORE_VERTICAL_SLICE_PARTIAL`, `CORE_LOOP_NOT_PROVEN`, `HUMAN_QA_NOT_RUN`이다.", "현재 저장소에는 C1 룰렛 핵심 계약과 C2 전투 목적 루프 구현 후보가 존재한다. C2는 접전지·거점·성문·본진·자연 승패·경제를 연결했지만 최종 공통 원격 검증과 사람 플레이는 남아 있다. 현재 판정은 `C1_ROULETTE_CORE_REMOTE_PROVEN`, `C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE`, `C2_REMOTE_VALIDATION_PENDING`, `CORE_VERTICAL_SLICE_PARTIAL`, `CORE_LOOP_NOT_PROVEN`, `HUMAN_QA_NOT_RUN`이다.")
replace_once("README.md", "C1 변경과 증거 경계는 [`docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md`](docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md), 자동·수동 검증은", "C1 증거는 [`docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md`](docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md), C2 구현·감사는 [`docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md`](docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md), 자동·수동 검증은")

# Active Context
replace_once("docs/ACTIVE_CONTEXT.md", "- 저장소 상태: **C1 룰렛 핵심 계약 REMOTE_PROVEN / 전투 목적 루프·사람 플레이 미검증**", "- 저장소 상태: **C1 룰렛 REMOTE_PROVEN / C2 전투 목적 구현 후보·원격 검증 진행 / 사람 플레이 미검증**")
replace_once("docs/ACTIVE_CONTEXT.md", "+ C1_ROULETTE_CORE_REMOTE_PROVEN\n+ CORE_VERTICAL_SLICE_PARTIAL", "+ C1_ROULETTE_CORE_REMOTE_PROVEN\n+ C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE\n+ C2_REMOTE_VALIDATION_PENDING\n+ CORE_VERTICAL_SLICE_PARTIAL")
replace_all("docs/ACTIVE_CONTEXT.md", "29919925777", "29926598807")
replace_once("docs/ACTIVE_CONTEXT.md", "- 전투→거점·성문·승패 연결과 코어 UX 6종은 완결되지 않았다.", "- C2 구현 후보는 같은 라인 교전→접전지→중간거점→성문→본진·W15 보스→승패와 실제 소유 수 경제를 연결한다.\n- 최종 공통 원격 검증·코어 UX 6종·사람 플레이는 아직 완료되지 않았다.")
replace_once("docs/ACTIVE_CONTEXT.md", "→ [다음] C1U 이동권·럭키·100,000시드\n→ 전투 목적 루프 연결", "→ C2 전투 목적 루프 구현 후보·원격 검증\n→ [결정 게이트] C1U 이동권·럭키·100,000시드")
replace_once("docs/ACTIVE_CONTEXT.md", "- PR #49는 C1 룰렛 핵심 계약과 구형 활성 참조 정리를 원격 검증했다. 이동권·럭키·고정 상위 템플릿은 C1U 결정 전 확정하지 않는다.", "- PR #49는 main에 병합됐다. PR #50은 C2 전투 목적 루프 구현 후보와 문서·검증 동기화를 다룬다.\n- 이동권·럭키·고정 상위 템플릿은 C1U 사용자 결정 전 확정하지 않는다.")

# Handoff
replace_once("docs/HANDOFF_CONTEXT.md", "- 현재 상태: **CORE_LOCKED / C1 룰렛 핵심 계약 REMOTE_PROVEN / C1U·전투 목적 루프·사람 플레이 미검증**", "- 현재 상태: **CORE_LOCKED / C1 룰렛 REMOTE_PROVEN / C2 전투 목적 구현 후보·원격 검증 진행 / C1U·사람 플레이 미검증**")
replace_once("docs/HANDOFF_CONTEXT.md", "2. 저장소에는 기술 기준선과 원격 검증된 C1 룰렛 핵심 계약이 있다. C1U 유틸리티·전투 목적·코어 UX는 아직 미완결이다.", "2. 저장소에는 원격 검증된 C1 룰렛 핵심과 C2 전투 목적 구현 후보가 있다. C2 최종 공통 원격 검증, C1U 유틸리티 결정, 코어 UX와 사람 플레이는 남아 있다.")
replace_once("docs/HANDOFF_CONTEXT.md", "+ C1_ROULETTE_CORE_REMOTE_PROVEN\n+ CORE_VERTICAL_SLICE_PARTIAL", "+ C1_ROULETTE_CORE_REMOTE_PROVEN\n+ C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE\n+ C2_REMOTE_VALIDATION_PENDING\n+ CORE_VERTICAL_SLICE_PARTIAL")
replace_all("docs/HANDOFF_CONTEXT.md", "29919925777", "29926598807")
replace_once("docs/HANDOFF_CONTEXT.md", "현재 Godot 프로젝트는 기술·데이터 그레이박스와 run `29926598807`에서 원격 검증된 C1 룰렛 핵심 계약을 포함한다. 전투 상태 기반 승패, 접전지·거점·성문 연결과 승인 UX 6종은 닫히지 않았으므로 “핵심 수직 슬라이스 완료”로 부르지 않는다.", "현재 Godot 프로젝트는 run `29926598807`에서 검증된 C1 룰렛 핵심과 C2 전투 목적 구현 후보를 포함한다. C2는 접전지·중간거점·성문·본진·W15 보스·자연 승패·경제를 연결했지만 최종 공통 원격 검증과 승인 UX 6종·사람 플레이는 남아 있으므로 ‘핵심 수직 슬라이스 완료’로 부르지 않는다.")
replace_once("docs/HANDOFF_CONTEXT.md", "다음 순서는 PR #49 검토 뒤 C1U 결정, 전투 목적 루프, 코어 UX, 사람 플레이 검증이다.", "다음 순서는 PR #50 C2 공통 원격 검증, C1U 사용자 결정, 코어 UX, 사람 플레이 검증이다.")

# GDD
replace_once("docs/OMENWARD_GAME_DESIGN.md", "- 문서 버전: **v0.21**", "- 문서 버전: **v0.22**")
replace_once("docs/OMENWARD_GAME_DESIGN.md", "- 상태: **프리프로덕션 계약 승인 / C1 룰렛 핵심 계약 REMOTE_PROVEN / 전투 목적 루프·사람 플레이 미검증**", "- 상태: **프리프로덕션 계약 승인 / C1 룰렛 REMOTE_PROVEN / C2 전투 목적 구현 후보·원격 검증 진행 / 사람 플레이 미검증**")
replace_once("docs/OMENWARD_GAME_DESIGN.md", "+ C1_ROULETTE_CORE_REMOTE_PROVEN\n+ CORE_VERTICAL_SLICE_PARTIAL", "+ C1_ROULETTE_CORE_REMOTE_PROVEN\n+ C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE\n+ C2_REMOTE_VALIDATION_PENDING\n+ CORE_VERTICAL_SLICE_PARTIAL")
replace_once("docs/OMENWARD_GAME_DESIGN.md", "이 기획서의 전체 설계와 승인된 초기값이 모두 현재 실행 코드로 완결됐다는 뜻이 아니다. 실제 구현 여부는 상태 문서와 코드·데이터·테스트를 대조한다.", "C2 구현 후보는 `같은 라인 교전 → 접전지 → 중간거점 → 성문 → 본진·W15 보스 → 자연 승패`와 점령 기반 건물·경제를 연결한다. 본진 독립 방어 수치와 접전지 별도 점령 시간은 미승인이므로 기존 승인 계약을 가역 fallback으로 재사용한다. 전체 설계와 사람 경험이 완결됐다는 뜻은 아니며 실제 구현 여부는 상태 문서와 코드·데이터·테스트를 대조한다.")

# Roadmap
replace_once("docs/OMENWARD_ROADMAP.md", "- 현재 상태: **C0 완료 / C1 룰렛 핵심 계약 REMOTE_PROVEN / PR #49 사용자 검토 대기**", "- 현재 상태: **C0·C1 완료 / C2 전투 목적 구현 후보·원격 검증 진행 / C1U 사용자 결정 대기**")
replace_once("docs/OMENWARD_ROADMAP.md", "- 현재 구현·감사 입력: `docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md`", "- 현재 구현·감사 입력: `docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md`")
replace_once("docs/OMENWARD_ROADMAP.md", "→ [다음] C1U 이동권·럭키 규칙 통합·100,000시드 검증\n→ 전투 목적 루프 연결", "→ [현재] C2 전투 목적 구현 후보·공통 원격 검증\n→ [결정 게이트] C1U 이동권·럭키 규칙 통합·100,000시드 검증")
replace_once("docs/OMENWARD_ROADMAP.md", "| C1 룰렛 핵심 계약 | 중앙 판정 줄·완성선·등급·보상·보관 | **REMOTE_PROVEN** | PR #49 사용자 검토 |", "| C1 룰렛 핵심 계약 | 중앙 판정 줄·완성선·등급·보상·보관 | **REMOTE_PROVEN / main 병합** | 정본 유지 |")
replace_once("docs/OMENWARD_ROADMAP.md", "| C1U 룰렛 유틸리티 | 이동권·럭키 정본 통합·100,000시드 | **다음** | 사용자 결정·분포 기준 |", "| C1U 룰렛 유틸리티 | 이동권·럭키 정본 통합·100,000시드 | 사용자 결정 대기 | 결정·분포 기준 |")
replace_once("docs/OMENWARD_ROADMAP.md", "| C2 전투 목적 루프 | 접전지·거점·성문·승패·경제 연결 | 부분 구현 | End-to-End 전투 PASS |", "| C2 전투 목적 루프 | 접전지·거점·성문·승패·경제 연결 | **IMPLEMENTED_CANDIDATE / REMOTE_VALIDATION_PENDING** | 공통 Core Contracts PASS |")
replace_once("docs/OMENWARD_ROADMAP.md", "PR #49 C1 원격 검증 결과·diff 사용자 검토\n→ 병합 결정\n→ C1U 이동권·럭키·고정 상위 템플릿·100,000시드 Plan", "PR #50 C2 공통 Core Contracts 원격 검증\n→ 구현·문서·구형 참조 적대적 검토\n→ 병합 결정\n→ C1U 사용자 결정 또는 C3 코어 UX Plan")
replace_once("docs/OMENWARD_ROADMAP.md", "C1 핵심 계약은 run `29919925777`에서 원격 검증됐다. 전투 목적 루프·코어 UX·신규 콘텐츠는 같은 PR에 섞지 않는다.", "C1 핵심 계약은 최종 run `29926598807`에서 검증되고 main에 병합됐다. C2는 별도 PR #50에서 구현 후보를 검증한다. C1U·코어 UX·신규 콘텐츠는 같은 PR에 섞지 않는다.")

# Decisions
replace_once("docs/DECISIONS_PENDING.md", "- 현재 작업: PR #49 C1 원격 검증 결과 검토 / 다음 결정: C1U 이동권·럭키·분포", "- 현재 작업: PR #50 C2 공통 원격 검증 / 다음 사용자 결정: C1U 이동권·럭키·분포")
replace_all("docs/DECISIONS_PENDING.md", "29919925777", "29926598807")
replace_once("docs/DECISIONS_PENDING.md", "### B.1 C1U 별도 결정", "### B.1 C1U 별도 결정")
insert_marker = "### C. 검증 증거"
insert_text = r'''### B.2 C2 전투 목적 루프 구현 후보

- [x] 공용 10병종 `capture_power`와 `structure_damage_tags` 복구.
- [x] 접전지·중간거점·성문·본진의 라인별 상태 소유.
- [x] 교착·점령·안정화·건설 revision·시간 경제 연결.
- [x] 같은 라인 유닛의 실제 성문·본진 공격.
- [x] 적 본진·W15 전설 보스 승리와 아군 본진 패배.
- [ ] 최종 공통 `Core Contracts` 원격 검증과 PR #50 병합.

가역 fallback·추가 결정:

- [ ] 본진 독립 HP·방어·저항 최종값. 현재 미지정 시 승인 성문 프로필을 재사용한다.
- [ ] 중앙 접전지 전용 점령·안정화 시간. 현재 승인 중간거점 상태기를 재사용한다.
- [ ] 정규화 0~100 시뮬레이션 좌표를 실제 전장 좌표·Scene과 연결하는 시점.
- [ ] 본진·성문·거점 상태의 월드 표시와 HUD 정보 계층은 C3 UX에서 검증.

'''
path = ROOT / "docs/DECISIONS_PENDING.md"
text = path.read_text(encoding="utf-8")
if insert_text.strip() not in text:
    if text.count(insert_marker) != 1:
        raise RuntimeError("DECISIONS_PENDING C section marker mismatch")
    text = text.replace(insert_marker, insert_text + insert_marker, 1)
path.write_text(text, encoding="utf-8", newline="\n")
replace_once("docs/DECISIONS_PENDING.md", "1. PR #49 C1 원격 검증 결과 검토·병합 결정\n2. C1U 이동권·럭키 정본 통합과 100,000시드 검증\n3. 전투 목적 루프 연결\n4. 승인 코어 UX 6종", "1. PR #50 C2 공통 원격 검증·병합 결정\n2. C1U 이동권·럭키 정본 통합과 100,000시드 사용자 결정\n3. 승인 코어 UX 6종")
replace_once("docs/DECISIONS_PENDING.md", "현재는 새로운 병종·Tier·보스·캠페인 콘텐츠를 추가하는 단계가 아니다. 다음 기능 변경은 PR #49 병합 뒤 C1U 결정으로 제한한다.", "현재는 새로운 병종·Tier·보스·캠페인 콘텐츠를 추가하는 단계가 아니다. C2는 승인 인과만 복구하며, C1U는 사용자 결정 전 구현하지 않는다.")

# Documentation Map
replace_once("docs/DOCUMENTATION_MAP.md", "현재 C1 시작 문서는 `C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md`와 룰렛 APPROVED 정본이다. 과거 Work Order·Goal·Proposal은 Git 이력에서만 추적한다.", "현재 C2 시작 문서는 `C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md`와 전장·공용 병종·경제 APPROVED 정본이다. C1 증거는 보존 책임 문서이며, 과거 Work Order·Goal·Proposal은 Git 이력에서만 추적한다.")
replace_once("docs/DOCUMENTATION_MAP.md", "| 현재 C1 구현·증거 | `C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md` |", "| C1 구현·증거 | `C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md` |\n| 현재 C2 구현·감사 | `C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md` |")

# Validation
write("docs/VERTICAL_SLICE_VALIDATION.md", r'''
# Vertical Slice Validation

## Automated

Godot 4.7.1 Standard editor binary로 저장소 루트에서 실행한다.

```powershell
Get-ChildItem tests/headless/*_test.gd | ForEach-Object { & Godot_v4.7.1-stable_win64_console.exe --headless --path . -s ("res://tests/headless/" + $_.Name) }
Godot_v4.7.1-stable_win64_console.exe --headless --path . --editor --quit
Godot_v4.7.1-stable_win64_console.exe --headless --path . --quit-after 1
python tools/validate_project_core_docs.py
python tools/validate_c1_roulette.py
python tools/validate_c2_battle_objective.py
python -m unittest discover -s tests/python -v
git diff --check
```

영구 `Validate Core Contracts` Workflow가 다음을 실행한다.

- Ubuntu/Windows × Python 3.12/3.13.
- C1·C2·프로젝트 코어·Skill Validator.
- 전체 Python mutation tests.
- Godot 4.7.1 editor import.
- 모든 `tests/headless/*_test.gd`.
- runtime smoke.
- whitespace와 구형 활성 참조·깨진 링크 검사.

## Current automated scope

- 공용 10병종·양 진영 데이터와 점령력·구조물 태그.
- C1 중앙 판정·등급·금화·전설 제한·보관·배치.
- C2 같은 라인 목적 이동, 접전지·거점 점령·교착, 건물 효과·경제 전환.
- 라인별 성문·본진 공격, 자연 승리·패배, W15 전설 보스 승리.
- 암살자 같은 라인 우회와 점령력 0.
- 결정론적 snapshot·input log.
- 활성 문서의 구형 현재 상태·실행 입력·깨진 링크.

## Manual QA still required

1. 튜토리얼과 정규 스테이지를 1920×1080에서 실행한다.
2. 병영 건설→룰렛→결과 보관→라인 배치→접전지→중간거점→성문→결과를 확인한다.
3. 1280×720에서 보드·등급·보관·세 라인·목적 상태가 읽히는지 확인한다.
4. 이동권·럭키는 C1U 결정 전 최종 동작으로 판정하지 않는다.
5. W1~W20 연속 플레이, 10~15분 재미·학습, 밸런스·성능은 별도 실행한다.
''')

# Godot structure
replace_once("docs/GODOT_PROJECT_STRUCTURE.md", "- 상태: **Phase 0 구현 기준 / 수직 슬라이스 확장은 Issue #32 Plan Mode에서 확정**", "- 상태: **기술 기준선·C1 REMOTE_PROVEN / C2 전투 목적 구현 후보·원격 검증 진행**")
replace_once("docs/GODOT_PROJECT_STRUCTURE.md", "- 갱신일: 2026-07-16", "- 갱신일: 2026-07-22")
replace_once("docs/GODOT_PROJECT_STRUCTURE.md", "## 2. 예정 폴더 구조", "## 2. 현재 폴더 구조")
append_section("docs/GODOT_PROJECT_STRUCTURE.md", "## C2 전투 목적 런타임", r'''
## C2 전투 목적 런타임

- `BattleSimulator`: 고정 0.1초 틱, 3라인, 접전지 3·중간거점 6·성문 6·본진 2와 목적 순서·이벤트 로그.
- `OutpostState`: 중립화·점령·교착·이탈 유지·복귀·안정화·capture revision.
- `GateState` / `BaseState`: 구조물 피해·붕괴·종료 상태.
- `BuildingService`: 거점 revision과 건물 ACTIVE/DISABLED/RUINED·식량 효과 동기화.
- `StageRun`: 실제 소유 수 경제, 적 본진·W15 보스 승리, 아군 본진 패배.
- `UnitArchetypeProfile`: 공용 점령력과 구조물 피해 태그.

본진 방어 프로필·중앙 접전지 점령 시간·0~100 목적 좌표는 승인값 부재를 드러낸 가역 fallback이며 최종 시각·밸런스 계약이 아니다.
''')

# Approved docs and baseline
replace_once("docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md", "- 상태: **구조 및 수직 슬라이스 초기값 승인 / 플레이테스트 조정 가능 / 구현 미승인**", "- 상태: **구조·초기값 승인 / C2 전투 목적 구현 후보·원격 검증 진행 / 플레이테스트 조정 가능**")
replace_once("docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md", "- 최신 갱신일: 2026-07-16", "- 최신 갱신일: 2026-07-22")
append_section("docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md", "## C2 구현 상태", r'''
## C2 구현 상태

C2 구현 후보는 중앙 접전지 3개, 양측 중간거점 6개, 성문 6개, 본진 2개와 같은 라인 목적 순서를 실제 전투 상태로 연결한다. 점령·교착·건설 revision·성문 붕괴·자연 승패 자동 회귀가 존재한다.

- 본진 독립 수치는 아직 승인하지 않았다. 미지정 시 성문 프로필을 기술 fallback으로 재사용한다.
- 중앙 접전지의 별도 점령 시간도 미승인이다. 승인 중간거점 상태기를 재사용한다.
- 정규화 목적 좌표는 시뮬레이션 좌표이며 이 문서의 시각 scale을 변경하지 않는다.
- 사람 플레이·가독성·밸런스 검증 전에는 최종값으로 승격하지 않는다.
''')
replace_once("docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md", "- 상태: **아군·적군 공용 10병종 데이터 구조 승인 / 진영별 차이는 이미지 세트와 소유권·출격 방식으로 제한 / 정확한 Godot Resource 형태는 Plan Mode에서 확정**", "- 상태: **공용 10병종 계약 승인 / Godot Resource 구현 / C2 점령력·구조물 태그 구현 후보·원격 검증 진행**")
append_section("docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md", "## C2 구현 상태", r'''
## C2 구현 상태

`UnitArchetypeProfile`에 공용 `capture_power`와 `structure_damage_tags`를 구현했다. 아군·적군은 같은 값을 사용하며 진영별 전투 데이터 복사본을 만들지 않는다.

- 방패 1.25.
- 일반 근접·기병 1.0.
- 원거리·지원·거인 0.5.
- 암살자·비행 0.
- 거인은 `siege`, 나머지 현재 10병종은 `normal` 구조물 태그.

상세 영웅·전설 템플릿과 추가 고정 피해 태그는 별도 승인 전 확정하지 않는다.
''')
append_section("docs/design/APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md", "## C2 구현 상태", r'''
## C2 구현 상태

C2 구현 후보는 전투 상태에서 실제 아군 접전지 통제 수와 안정 중간거점 소유 수를 계산해 기존 시간 수입 공식에 전달한다.

- 접전지: 1곳당 4금화/60초.
- 안정 중간거점: 1곳당 2금화/30초.
- 거점 중립화 시 농장 식량 효과 해제.
- 소유권 변경 시 이전 capture revision 건물 폐허화.
- 재점령·안정화 뒤 새 revision으로 재건설.

경제 수치 자체는 기존 승인값이며 사람 플레이·100,000시드·시간축 검증 전 조정 가능하다.
''')
replace_once("docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md", "- 상태: **프리프로덕션 구조 승인 / 기술 기준선·C1 룰렛 핵심 계약 REMOTE_PROVEN / C1U·전투 목적 루프 대기**", "- 상태: **프리프로덕션 구조 승인 / C1 REMOTE_PROVEN / C2 구현 후보·원격 검증 진행 / C1U 사용자 결정 대기**")
replace_once("docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md", "- C1 구현 증거: `docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md`", "- C1 구현 증거: `docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md`\n- C2 구현·감사: `docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md`")

# Project core validator candidate state
replace_once("tools/validate_project_core_docs.py", '    "C1_ROULETTE_CORE_REMOTE_PROVEN",\n)', '    "C1_ROULETTE_CORE_REMOTE_PROVEN",\n    "C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE",\n    "C2_REMOTE_VALIDATION_PENDING",\n)')
replace_once("tools/validate_project_core_docs.py", '    if "C1 룰렛 핵심 계약 원격 검증 완료" not in readme or "전투 목적 루프·사람 플레이 미완결" not in readme:\n        errors.append("README does not expose the proven C1 and partial core-loop boundary")', '    if "C1 룰렛 REMOTE_PROVEN" not in readme or "C2 전투 목적 루프 구현 후보" not in readme or "사람 플레이 미완결" not in readme:\n        errors.append("README does not expose the proven C1, candidate C2, and human-QA boundary")')

# C2 validator documentation/stale/temp checks
validator = ROOT / "tools/validate_c2_battle_objective.py"
text = validator.read_text(encoding="utf-8")
text = text.replace("import pathlib\n", "import pathlib\nimport re\n")
text = text.replace(
    '    return errors\n\n\ndef main()',
    '''    required_doc_states = {
        "README.md": ("C2 전투 목적 루프 구현 후보", "사람 플레이 미완결"),
        "docs/ACTIVE_CONTEXT.md": ("C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE", "C2_REMOTE_VALIDATION_PENDING"),
        "docs/HANDOFF_CONTEXT.md": ("C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE", "C2_REMOTE_VALIDATION_PENDING"),
        "docs/CURRENT_IMPLEMENTATION_STATUS.md": ("C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE", "C2_REMOTE_VALIDATION_PENDING"),
        "docs/OMENWARD_GAME_DESIGN.md": ("문서 버전: **v0.22**", "C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE"),
        "docs/OMENWARD_ROADMAP.md": ("C2 전투 목적 구현 후보·공통 원격 검증",),
        "docs/DECISIONS_PENDING.md": ("C2 전투 목적 루프 구현 후보", "본진 독립 HP"),
        "docs/DOCUMENTATION_MAP.md": ("C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md",),
    }
    for relative, phrases in required_doc_states.items():
        body = (root / relative).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in body:
                errors.append(f"{relative} missing C2 candidate state: {phrase}")

    stale_active = (
        "PR #49 사용자 검토 대기",
        "PR #49 C1 원격 검증 결과 검토",
        "PR #49 병합",
        "[현재] 승인 룰렛 핵심 계약 복구",
        "현재 C1 시작 문서",
        "전투 상태 기반 승패, 접전지·거점·성문 연결과 승인 UX 6종은 닫히지 않았다",
    )
    excluded_parts = {"archive", "issues", "goals", "work_orders", "proposals"}
    active_docs = [root / "README.md", root / "AGENTS.md"]
    for path in (root / "docs").rglob("*.md"):
        if not any(part in excluded_parts for part in path.relative_to(root / "docs").parts):
            active_docs.append(path)
    for path in active_docs:
        body = path.read_text(encoding="utf-8")
        relative = path.relative_to(root).as_posix()
        for stale in stale_active:
            if stale in body:
                errors.append(f"active document retains stale C1/C2 state: {relative} -> {stale}")
        for target in re.findall(r"\\[[^\\]]*\\]\\(([^)]+)\\)", body):
            clean = target.split("#", 1)[0].strip()
            if not clean or "://" in clean or clean.startswith(("#", "mailto:")):
                continue
            resolved = (path.parent / clean).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                continue
            if not resolved.exists():
                errors.append(f"broken active Markdown link: {relative} -> {clean}")

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        name = path.name.lower()
        relative = path.relative_to(root).as_posix()
        if path.name.startswith("_C2_") or "_apply_c2_" in name or "_sync_c2_" in name or "apply-c2" in name or "sync-c2" in name:
            errors.append(f"temporary C2 artifact remains: {relative}")
    return errors


def main()'''
)
validator.write_text(text, encoding="utf-8", newline="\n")

# Mutation fixture copies active docs used by the expanded validator.
test_path = ROOT / "tests/python/test_c2_battle_objective_contract.py"
test_text = test_path.read_text(encoding="utf-8")
old_tuple = '''        for relative in (
            "scripts/data/unit_archetype_profile.gd",
            "scripts/core/stage_economy.gd",
            "scripts/buildings/building_state.gd",
        ):
'''
new_tuple = '''        for relative in (
            "scripts/data/unit_archetype_profile.gd",
            "scripts/core/stage_economy.gd",
            "scripts/buildings/building_state.gd",
            "README.md",
            "AGENTS.md",
            "docs/ACTIVE_CONTEXT.md",
            "docs/HANDOFF_CONTEXT.md",
            "docs/CURRENT_IMPLEMENTATION_STATUS.md",
            "docs/OMENWARD_GAME_DESIGN.md",
            "docs/OMENWARD_ROADMAP.md",
            "docs/DECISIONS_PENDING.md",
            "docs/DOCUMENTATION_MAP.md",
            "docs/VERTICAL_SLICE_VALIDATION.md",
            "docs/GODOT_PROJECT_STRUCTURE.md",
            "docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md",
            "docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md",
            "docs/design/APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md",
            "docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md",
        ):
'''
if test_text.count(old_tuple) != 1:
    raise RuntimeError("C2 mutation fixture tuple mismatch")
test_text = test_text.replace(old_tuple, new_tuple, 1)
insert = '''
    def test_stale_pr49_current_state_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            roadmap = root / "docs/OMENWARD_ROADMAP.md"
            roadmap.write_text(roadmap.read_text(encoding="utf-8") + "\nPR #49 사용자 검토 대기\n", encoding="utf-8")
            self.assertTrue(any("stale C1/C2 state" in error for error in validate(root)))

    def test_missing_c2_candidate_state_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            self._copy_contract_files(root)
            status = root / "docs/CURRENT_IMPLEMENTATION_STATUS.md"
            status.write_text(status.read_text(encoding="utf-8").replace("C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE", "C2_STATE_REMOVED"), encoding="utf-8")
            self.assertTrue(any("missing C2 candidate state" in error for error in validate(root)))
'''
if "test_stale_pr49_current_state_is_rejected" not in test_text:
    test_text = test_text.replace("\n\nif __name__ == \"__main__\":", insert + "\n\nif __name__ == \"__main__\":", 1)
test_path.write_text(test_text, encoding="utf-8", newline="\n")

# Remove the synchronizer before validation; durable docs preserve its result.
self_path = ROOT / "tools/_sync_c2_docs.py"
if self_path.exists():
    self_path.unlink()
