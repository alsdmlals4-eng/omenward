#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXPECTED_MAIN = "69c571c5a49502f9da57e1c8d8eba04455380c0f"


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def write(relative: str, content: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def replace_once(relative: str, old: str, new: str) -> None:
    text = read(relative)
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{relative} expected one literal match, found {count}: {old[:80]!r}")
    write(relative, text.replace(old, new, 1))


def replace_regex(relative: str, pattern: str, replacement: str) -> None:
    text = read(relative)
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"{relative} expected one regex match, found {count}: {pattern}")
    write(relative, updated)


run("git", "merge-base", "--is-ancestor", EXPECTED_MAIN, "HEAD")

write("docs/PROJECT_CORE.md", '# 오멘워드 프로젝트 코어\n\n- 판정일: 2026-07-22\n- 기준 커밋: `69c571c5a49502f9da57e1c8d8eba04455380c0f`\n- 상태: `EXISTING_CORE_IDENTIFIED`\n- 잠금 상태: `CORE_LOCK_PENDING_USER_CONFIRMATION`\n- 책임: 제품 정체성·핵심 선택·불변 조건·검증 게이트의 최상위 책임 원본\n\n이 문서는 기존 승인 기획과 실제 구현을 대조해 오멘워드의 프로젝트 코어를 분리한 책임 원본이다. 세부 수치와 콘텐츠는 관련 `APPROVED_*.md`가 소유하지만, 기능의 우선순위와 제거 가능성은 이 문서를 기준으로 판단한다.\n\n`CORE_LOCK_PENDING_USER_CONFIRMATION`은 코어를 새로 발명했다는 뜻이 아니다. 기존 코어를 식별해 기록했으며, 문구를 변경 불가 상태로 잠그는 행위만 사용자의 명시적 확인을 기다린다는 뜻이다.\n\n## 1. 정체성 한 문장\n\n> **예고된 세 전선의 위협을 읽고, 제한된 건물 노드로 룰렛 확률을 설계한 뒤, 당첨된 증원을 어느 전선에 투입할지 결정해 전황을 뒤집는 실시간 전략 오토배틀 게임.**\n\n## 2. 플레이어 판타지\n\n플레이어는 직접 병사 한 명을 조종하는 영웅이 아니라, 불완전한 증원 체계를 설계하고 세 전선의 위험을 배분하는 지휘관이다.\n\n플레이어가 책임지는 것은 다음 세 가지다.\n\n1. **예측** — 베일의 징조로 다음 공세의 라인·병종·수량·특수 행동을 읽는다.\n2. **확률 설계** — 제한된 건물 노드와 전문화로 룰렛 토큰·출처·확률을 바꾼다.\n3. **전선 커밋** — 얻은 병력을 어느 라인에 배치할지 결정하고 다른 라인의 위험을 감수한다.\n\n## 3. 핵심 루프\n\n```text\n베일의 징조 확인\n→ 건설 후보와 룰렛 확률 변화 비교\n→ 제한 노드에 건설·전문화\n→ 3×3 룰렛 회전·허용된 조작·최종 확정\n→ 생성된 보상 확인\n→ 상·중·하 라인 중 하나에 배치\n→ 자동 교전·접전지·중간거점·성문 공방\n→ 라인별 성공·실패 원인 확인\n→ 다음 공세에 맞춰 건설·확률·배치를 수정\n```\n\n루프의 시작은 정보이며 끝은 학습이다. 무작위 결과만 소비하거나 전투를 관전하는 것으로 끝나면 코어 루프가 닫힌 것으로 판정하지 않는다.\n\n## 4. 프로젝트 코어\n\n### 4.1 기획 코어\n\n- 적 공세는 대응 가능한 시간 전에 공개된다.\n- 건설은 경제·방어뿐 아니라 미래 룰렛 결과의 확률과 출처를 바꾼다.\n- 룰렛은 결과를 직접 선택하는 장치가 아니라, 플레이어가 사전에 설계한 확률을 시험하는 장치다.\n- 당첨 결과를 어느 라인에 투입할지가 최종 전술 선택이다.\n- 자동전투 결과는 거점·성문·승패와 다음 경제에 실제 영향을 준다.\n- 실패 원인이 다음 건설·확률·배치 판단으로 환류한다.\n\n### 4.2 시스템 코어\n\n- 좌우 대칭의 독립된 상·중·하 3라인.\n- 제한된 후방·전방 건설 노드와 점령에 따른 건설권·생산권 이전.\n- 3×3 룰렛의 중앙 가로줄 기본 판정과 동일 심벌 완성선 기반 등급.\n- 룰렛 결과 보관·배치와 재회전 잠금.\n- 공용 병종 데이터와 진영별 표현 분리.\n- 접전지·중간거점·성문·같은 라인 암살자 우회.\n- 결정론적 시드·입력 로그·재현 가능한 핵심 결과.\n\n### 4.3 기술 코어\n\n기술 코어는 제품 정체성이 아니라 제품 코어를 안전하게 보존하는 기반이다.\n\n- Godot + GDScript.\n- typed Resource 기반 공용 데이터.\n- 전투 규칙과 진영 Visual 데이터 분리.\n- 이름 기반 RNG stream과 입력 기록.\n- 승인 계약을 직접 검증하는 headless·정적 테스트.\n\n## 5. 분류\n\n| 분류 | 현재 포함 요소 | 변경 원칙 |\n|---|---|---|\n| `PROJECT_CORE` | 공세 예측, 건물 기반 확률 설계, 룰렛 판정, 라인 투입, 자동전투 결과, 원인 피드백 | 제거·대체 시 사용자 승인과 코어 재개 필요 |\n| `CORE_SUPPORT` | 거점·성문·암살자 우회, 확률 미리보기, 토큰 장부, 상성·사거리 표시, 라인 원인 보고 | 코어 인과를 약화시키지 않는 범위에서 조정 |\n| `MVP_SUPPORT` | 대표 병종 3~5개, 최소 건물 2~4개, 튜토리얼, 짧은 공세 묶음, 회색상자 UI | 코어 검증에 필요한 최소치로 제한 |\n| `CONTENT_VARIANT` | 공용 10병종 전체, Tier 3 세부 분화, W1~W20 전체, 다수 보스·캠페인 | 코어 플레이테스트 뒤 확장 |\n| `PRESENTATION_SHELL` | 벨루, 세계관 명칭, 픽셀 아트, 대사·연출·오디오 | 이해도·정체성을 높이되 코어 미완성을 가리지 않음 |\n| `TECHNICAL_FOUNDATION` | 엔진, Scene·Resource 구조, 결정론, 테스트·검증 도구 | 제품 코어와 혼동하지 않음 |\n\n## 6. 불변 조건\n\n1. 세 라인은 일반 유닛이 자유롭게 횡단하지 않는 독립 전선이다.\n2. 기본·일반 난이도에서는 치명적 공세 정보를 숨겨 난이도를 만들지 않는다.\n3. 건물 선택은 룰렛 토큰·확률·출처 중 하나 이상에 관찰 가능한 영향을 준다.\n4. 기본 룰렛 보상은 중앙 판정 줄이 성립할 때만 생성된다.\n5. 룰렛 등급은 승인된 동일 심벌 완성선 규칙으로 계산한다.\n6. 자동전투는 거점·성문·승패 상태를 실제로 변화시킨다.\n7. 플레이어가 얻은 보상을 어느 라인에 투입할지 결정한다.\n8. 패배와 손실의 핵심 원인을 플레이어가 확인할 수 있다.\n9. 아군과 일반 적군의 병종 전투 데이터를 별도 복제하지 않는다.\n10. 새 콘텐츠가 위 인과를 우회해 단독 정답이 되지 않도록 한다.\n\n## 7. 제거·대체 스트레스 테스트\n\n| 제거·대체 가정 | 결과 | 판정 |\n|---|---|---|\n| 룰렛 제거 | 일반적인 3라인 디펜스가 됨 | 코어 훼손 |\n| 건물이 확률에 영향 없음 | 건설과 룰렛이 분리된 장르 혼합이 됨 | 코어 훼손 |\n| 공세 전조 제거 | 대응 설계가 불가능하고 RNG 의존이 커짐 | 코어 훼손 |\n| 라인 선택 제거 | 플레이어의 마지막 전술 책임이 사라짐 | 코어 훼손 |\n| 거점·성문 제거 | 세 라인이 세 개의 체력 막대로 축소됨 | 핵심 지원 훼손 |\n| 결과 원인 보고 제거 | 실패가 학습으로 이어지지 않음 | 재도전 루프 훼손 |\n| 벨루 제거 | 게임은 작동하지만 세계관·학습 전달력이 약해짐 | 외피·지원 조정 가능 |\n| 공용 10병종 전체를 4종으로 축소 | 코어 검증은 가능 | MVP 범위 조정 가능 |\n| 최종 픽셀 아트 제거 | 회색상자에서도 코어 검증 가능 | 표현 외피 조정 가능 |\n\n## 8. 코어 검증 게이트\n\n### C0 — 정본 일치\n\n- 프로젝트 코어, GDD, 로드맵, 현재 상태와 Issue가 같은 구현 단계를 가리킨다.\n- `구현 전`, `완료`, `검증됨`을 실제 증거 없이 사용하지 않는다.\n\n### C1 — 룰렛 인과\n\n- 건물 전후 확률 변화가 실제 판정 데이터와 일치한다.\n- 중앙 판정 줄·완성선·등급·출처·보상이 승인 계약대로 동작한다.\n- 같은 시드와 확정 보드는 같은 결과를 만든다.\n\n### C2 — 전장 목적 루프\n\n- 배치된 유닛이 전투를 통해 접전지·거점·성문·승패를 바꾼다.\n- 경제가 실제 점령 상태를 반영한다.\n- 승리·패배는 외부 디버그 명령이 아니라 전장 상태에서 발생한다.\n\n### C3 — 코어 UX\n\n- 건설 전 확률 미리보기.\n- 룰렛 토큰 장부.\n- T-30/T-15/T-5 공세 전조.\n- 상성·사거리·타기팅 오버레이.\n- 웨이브 종료 후 라인별 원인 보고.\n- 건설 선택 비교 UI.\n\n### C4 — 사람 플레이\n\n- 10~15분 안에 코어 루프를 최소 두 번 경험한다.\n- 플레이어가 위협·확률 변화·배치 이유·패배 원인을 설명할 수 있다.\n- 1920×1080과 1280×720에서 세 전선과 핵심 경고를 읽을 수 있다.\n\n### C5 — 안정성\n\n- 승인 계약 자동 테스트.\n- Godot editor import와 headless 테스트.\n- runtime smoke.\n- 결정론 회귀와 성능 기준.\n\n## 9. 현재 제외\n\n다음은 코어 검증 전에 확대하지 않는다.\n\n- 신규 병종과 복합 친화도.\n- 대규모 영구 성장 트리.\n- 직접 조작 영웅 전투.\n- PvP·랭크·시즌.\n- 랜덤 개별 능력치·각인·흡수 진화.\n- 전체 캠페인 대사와 최종 아트 대량 생산.\n\n## 10. 변경·잠금 규칙\n\n- 이 문서의 분류와 불변 조건을 변경하려면 제거 테스트와 대안을 먼저 기록한다.\n- `PROJECT_CORE` 변경은 단순 구현 편의나 콘텐츠 추가를 이유로 자동 승인하지 않는다.\n- `CORE_CONFIRMED`와 `CORE_LOCKED` 전환은 사용자의 명시적 확인 뒤 별도 기록한다.\n- 잠금 전에도 현재 작업의 우선순위와 수직 슬라이스 검증 기준은 이 문서를 따른다.\n')
write("docs/CURRENT_IMPLEMENTATION_STATUS.md", '# 오멘워드 현재 구현 상태\n\n- 조사일: 2026-07-22\n- 기준 브랜치: `main`\n- 기준 커밋: `69c571c5a49502f9da57e1c8d8eba04455380c0f`\n- 판정:\n  - `TECHNICAL_BASELINE_IMPLEMENTED`\n  - `CORE_VERTICAL_SLICE_PARTIAL`\n  - `CORE_LOOP_NOT_PROVEN`\n  - `HUMAN_QA_NOT_RUN`\n\n이 문서는 “파일이 존재하는가”, “승인 계약이 구현됐는가”, “사람이 플레이해 재미와 가독성을 검증했는가”를 분리한다. 상태 문구가 다른 문서와 충돌하면 최신 실제 파일·테스트와 이 문서를 우선 확인한다.\n\n## 1. 상태 용어\n\n| 용어 | 의미 |\n|---|---|\n| `IMPLEMENTED` | 실제 파일과 실행 경로가 존재함 |\n| `PARTIAL` | 구성요소 일부가 존재하지만 승인된 End-to-End 계약이 닫히지 않음 |\n| `PROVEN` | 요구 계약과 실제 실행 증거가 함께 존재함 |\n| `NOT_PROVEN` | 파일 또는 테스트가 있어도 제품 계약 전체 증거가 없음 |\n| `NOT_RUN` | 이번 기준점에서 해당 실행·수동 검증을 하지 않음 |\n| `DIVERGENT` | 현재 구현·테스트가 승인 책임 문서와 다름 |\n\n## 2. 구현된 기술 기준선\n\n| 영역 | 현재 증거 | 판정 |\n|---|---|---|\n| Godot 프로젝트 | `project.godot`, main Scene, 960×540 논리 화면, 1920×1080 출력, Compatibility renderer | `IMPLEMENTED` |\n| 상태 소유 | `GameSession`, `StageRun`, `CombatClock`, `DataRegistry`, `DeterminismService` | `IMPLEMENTED` |\n| 공용 데이터 | 공용 archetype·Tier·Rank·FactionVisual·Animation 계약과 bootstrap catalog | `IMPLEMENTED` |\n| 경제 | 기본·접전지·거점 수입 계산 서비스, 금화·식량 | `IMPLEMENTED_COMPONENT` |\n| 건설 | 소유·안정화·점령 revision을 검사하는 건설 서비스 | `IMPLEMENTED_COMPONENT` |\n| 전투 | 독립 3라인, 공용 유닛, 기본 이동·타기팅·공격, 암살자 우회 상태 | `IMPLEMENTED_COMPONENT` |\n| 웨이브 | 튜토리얼 W1~4, 정규 W1~20 데이터와 60초 출격 시계 | `IMPLEMENTED_COMPONENT` |\n| 테스트 | bootstrap·데이터·경제·룰렛 placeholder·전투·웨이브·우회 관련 headless 테스트 파일 | `IMPLEMENTED` |\n\n## 3. 부분 구현 또는 승인 계약과 다른 영역\n\n### 3.1 룰렛 — `DIVERGENT`\n\n승인 계약:\n\n```text\n3×3 보드\n→ 중앙 가로줄 동일 비-X 심벌 판정\n→ 동일 심벌 완성선 계산\n→ 일반·엘리트·영웅·전설 등급\n→ 실제 보상 1개 생성\n→ 결과 보관·배치\n```\n\n현재 구현:\n\n- 20 Gold를 지불하고 9개의 `UnitSpawnDefinition`을 직접 반환한다.\n- 중앙 판정 줄, X·금화, 완성선, 등급, 전설 제한, 럭키 찬스, 이동권이 없다.\n- 현재 테스트도 9개 카드 반환을 기대하므로 승인 계약이 아니라 placeholder 계약을 고정한다.\n\n판정: `CORE_CONTRACT_DIVERGENT`.\n\n### 3.2 전투 목적 루프 — `PARTIAL`\n\n- 유닛끼리 이동·공격하는 기본 전투는 존재한다.\n- `OutpostState`, `GateState`, 암살자 우회 상태는 존재한다.\n- 정상 전투 흐름에서 유닛 점령력과 거점 점령 시작이 연결되지 않는다.\n- 성문 공격·본진 파괴·전장 상태 기반 승리·패배가 닫히지 않았다.\n- 현재 승패는 외부 `stage_victory`·`stage_defeat` 명령으로 기록한다.\n- `StageEconomy.advance()`에 전달되는 접전지 소유 수가 현재 `0`으로 고정돼 있다.\n\n판정: `CORE_LOOP_PARTIAL`.\n\n### 3.3 베일의 징조 — `PARTIAL`\n\n- 다음 공세까지의 시간 계산과 HUD 텍스트는 존재한다.\n- 승인된 T-30 라인·병종·수량, T-15 집결·경로, T-5 위험 라인 강조가 없다.\n\n판정: `CORE_INFORMATION_LOOP_PARTIAL`.\n\n### 3.4 코어 UX — `NOT_IMPLEMENTED`\n\n현재 HUD는 금화·식량·웨이브·전조 초·Spin·Tower·Farm·문자열 카드·라인 버튼을 제공한다.\n\n다음 승인 UX는 아직 실제 데이터와 연결되지 않았다.\n\n1. 건설 전 룰렛 확률 미리보기.\n2. 룰렛 토큰 장부.\n3. T-30/T-15/T-5 공세 전조.\n4. 상성·사거리·타기팅 오버레이.\n5. 웨이브 종료 후 라인별 원인 보고.\n6. 건설 선택 비교 UI.\n\n### 3.5 콘텐츠 검증력 — `INSUFFICIENT_FOR_CORE_PLAYTEST`\n\n- W1~W20 시간표와 보스 표식은 존재한다.\n- 다수 웨이브가 단일 유닛 중심이라 라인 분산·상성·복합 대응의 재미를 검증하기 어렵다.\n- 콘텐츠 확대보다 코어 계약 복구가 먼저다.\n\n## 4. 검증 증거 경계\n\n### 확인한 것\n\n- 저장소 정적 파일.\n- 현재 코드·데이터·headless 테스트의 계약.\n- 승인 책임 문서와 구현 간 차이.\n- 최근 `main`과 열린 PR·Issue 상태.\n\n### 이번 문서 복구에서 실행하지 않은 것\n\n- Godot editor import.\n- headless 테스트 재실행.\n- runtime smoke.\n- 1920×1080 사람 플레이.\n- 1280×720 가독성 QA.\n- W1~W20 연속 플레이.\n- 재미·밸런스·성능 계측.\n\n따라서 “프로젝트가 실행된다”는 과거 증거와 “현재 기준점에서 재검증했다”는 주장을 혼동하지 않는다.\n\n## 5. 현재 우선순위\n\n```text\n1. 정본·프로젝트 코어 복구\n2. 승인 룰렛 계약 복구\n3. 전투 → 거점·성문·승패 목적 루프 연결\n4. 승인 코어 UX 6종 최소 구현\n5. 10~15분 코어 플레이테스트\n6. 밸런스 안정화와 콘텐츠·아트 확장\n```\n\n## 6. 다음 완료 게이트\n\n정본 복구 완료 조건:\n\n- `PROJECT_CORE.md`가 제품 코어와 변경 가능한 외피를 분리한다.\n- README·GDD·로드맵·상태·인수인계·미확정 목록이 같은 단계 용어를 사용한다.\n- 현재 구현과 미구현을 파일 증거로 분리한다.\n- 과거 `구현 전`과 과도한 `수직 슬라이스 완료` 주장을 현재 상태로 사용하지 않는다.\n- 다음 변경은 게임 코드 전체가 아니라 승인 룰렛 계약 복구로 한정한다.\n')
write("docs/CORE_RECOVERY_AUDIT_2026-07-22.md", '# 프로젝트 코어·정본 복구 감사 — 2026-07-22\n\n## 1. 목적\n\n현재 저장소의 승인 기획, 상태 문서, 실제 코드, 데이터, 테스트와 열린 Issue·PR을 대조해 프로젝트 단계 오판을 제거한다.\n\n이번 작업은 문서 책임과 검증 계약만 바꾼다. 게임 코드·Scene·Resource·게임 데이터·승인 수치·시각자료는 변경하지 않는다.\n\n## 2. 기준점\n\n- Omenward `main`: `69c571c5a49502f9da57e1c8d8eba04455380c0f`\n- Skill 최적화 PR #47: Draft·미병합\n- 조사일: 2026-07-22\n\nPR #47의 프로젝트 코어·적대적 검토 Skill은 분석 방법으로 참고했지만, 이번 브랜치는 #47의 코드에 의존하지 않고 현재 `main`에서 생성한다.\n\n## 3. 발견한 정본 충돌\n\n| 위치 | 기존 주장 | 실제 증거 | 조치 |\n|---|---|---|---|\n| `README.md` | 플레이 가능한 수직 슬라이스 구현 완료 | 기술·데이터 구성요소는 있으나 룰렛·전투 목적·코어 UX가 미완결 | `CORE_VERTICAL_SLICE_PARTIAL`로 교정 |\n| `OMENWARD_GAME_DESIGN.md` | Phase 0 대기·구현 전 | Godot 프로젝트·Scene·GDScript·Resource·테스트 존재 | 기술 기준선 구현과 코어 미완결을 분리 |\n| `OMENWARD_ROADMAP.md` | Phase 0 Plan Mode 대기 | P1 기반과 P2 일부가 이미 구현 | 현재 복구 단계 중심으로 재작성 |\n| `DECISIONS_PENDING.md` | 엔진·화면·상태 소유를 최초 승인 대기 | 실제 project·GameSession·Resource 구조 존재 | 구현 사실과 재검증 필요를 분리 |\n| 열린 Issue 다수 | 구현 금지·과거 브랜치 정본 | 현재 main과 상태가 다름 | 본 PR에서 문서 정본을 먼저 복구하고 후속 Issue 정리 대상으로 기록 |\n| 기존 테스트 | 9개 룰렛 카드 반환을 성공 계약으로 간주 | 승인 룰렛은 중앙 줄·완성선·등급·단일 보상 | 다음 단계의 P0 계약 복구 항목으로 지정 |\n\n## 4. 채택한 상태 모델\n\n```text\nTECHNICAL_BASELINE_IMPLEMENTED\n+ CORE_VERTICAL_SLICE_PARTIAL\n+ CORE_LOOP_NOT_PROVEN\n+ HUMAN_QA_NOT_RUN\n```\n\n이 네 상태를 동시에 사용한다. 어느 하나만 사용하면 다음 오판이 생긴다.\n\n- `구현 전`만 사용: 이미 존재하는 기술 기반과 파일을 다시 설계한다.\n- `수직 슬라이스 완료`만 사용: 승인 룰렛·전투 목적·UX 미완성을 놓친다.\n- `테스트 통과`만 사용: placeholder 테스트를 제품 계약 검증으로 오인한다.\n- `플레이 가능`만 사용: 사람 플레이·가독성·재미 검증을 완료로 오인한다.\n\n## 5. 프로젝트 코어 스트레스 테스트\n\n### 공격 1 — 룰렛 없이도 같은 게임인가\n\n아니다. 룰렛을 제거하면 제한 노드 기반 3라인 디펜스가 된다.\n\n### 공격 2 — 건물이 확률을 바꾸지 않아도 되는가\n\n아니다. 건설과 룰렛이 분리돼 장르 혼합의 인과가 사라진다.\n\n### 공격 3 — 공세 정보를 숨기면 더 전략적인가\n\n아니다. 대응 자원 부족이 아니라 정보 부족으로 난이도를 만들면 RNG 좌절이 커진다.\n\n### 공격 4 — 배치를 자동화해도 되는가\n\n아니다. 당첨 결과를 어느 전선에 커밋할지가 플레이어의 마지막 전술 책임이다.\n\n### 공격 5 — 전체 10병종과 W1~W20이 지금 필요한가\n\n아니다. 대표 병종 3~5개와 짧은 공세 묶음으로 코어를 먼저 검증할 수 있다.\n\n## 6. Critique–Refine 결과\n\n초기 비판:\n\n- 상태 문서만 갱신하면 다시 드리프트할 수 있다.\n- 새 코어 문서가 기존 GDD를 중복할 수 있다.\n- 파일 존재를 구현 완료로 오인할 수 있다.\n- 코어 문구를 사용자 승인 없이 잠글 수 있다.\n\n개선:\n\n- `PROJECT_CORE.md`는 기능 상세가 아니라 분류·불변·제거 테스트·게이트만 소유한다.\n- `CURRENT_IMPLEMENTATION_STATUS.md`는 실제 증거와 미검증 경계만 소유한다.\n- 기존 GDD는 전체 설계, APPROVED 문서는 세부 규칙을 계속 소유한다.\n- 문서 Validator가 stale 상태 문구와 필수 참조 누락을 차단한다.\n- 코어 상태는 `EXISTING_CORE_IDENTIFIED`로 기록하고 잠금은 사용자 확인을 기다린다.\n\n## 7. 변경 범위\n\n추가:\n\n- `docs/PROJECT_CORE.md`\n- `docs/CURRENT_IMPLEMENTATION_STATUS.md`\n- `docs/CORE_RECOVERY_AUDIT_2026-07-22.md`\n- `tools/validate_project_core_docs.py`\n- `tests/python/test_project_core_docs.py`\n- `.github/workflows/validate-project-core-docs.yml`\n\n동기화:\n\n- `README.md`\n- `docs/ACTIVE_CONTEXT.md`\n- `docs/HANDOFF_CONTEXT.md`\n- `docs/DOCUMENTATION_MAP.md`\n- `docs/OMENWARD_GAME_DESIGN.md`\n- `docs/OMENWARD_ROADMAP.md`\n- `docs/DECISIONS_PENDING.md`\n\n## 8. 후속 순서\n\n1. 이 문서 전용 Draft PR 검토.\n2. 사용자가 프로젝트 코어 문구 잠금 여부를 확인.\n3. 승인 룰렛 계약 복구를 별도 Plan·Build·Review PR로 수행.\n4. 전투 목적 루프, 코어 UX, 사람 플레이 순으로 분리 진행.\n\n## 9. 판정\n\n- 정본 충돌: `FOUND`\n- 코어 식별: `COMPLETE`\n- 코어 잠금: `PENDING_USER_CONFIRMATION`\n- 게임 기능 변경: `NONE`\n- Godot 실행 검증: `NOT_RUN`\n- 사람 플레이 검증: `NOT_RUN`\n')
write("tools/validate_project_core_docs.py", '#!/usr/bin/env python3\n"""Validate Omenward project-core and current-state documentation contracts."""\n\nfrom __future__ import annotations\n\nimport pathlib\nimport re\nimport sys\nfrom typing import Iterable\n\nROOT = pathlib.Path(__file__).resolve().parents[1]\n\nREQUIRED_FILES = (\n    "docs/PROJECT_CORE.md",\n    "docs/CURRENT_IMPLEMENTATION_STATUS.md",\n    "docs/CORE_RECOVERY_AUDIT_2026-07-22.md",\n    "README.md",\n    "docs/ACTIVE_CONTEXT.md",\n    "docs/HANDOFF_CONTEXT.md",\n    "docs/DOCUMENTATION_MAP.md",\n    "docs/OMENWARD_GAME_DESIGN.md",\n    "docs/OMENWARD_ROADMAP.md",\n    "docs/DECISIONS_PENDING.md",\n)\n\nREFERENCE_FILES = (\n    "README.md",\n    "docs/ACTIVE_CONTEXT.md",\n    "docs/HANDOFF_CONTEXT.md",\n    "docs/DOCUMENTATION_MAP.md",\n    "docs/OMENWARD_GAME_DESIGN.md",\n    "docs/OMENWARD_ROADMAP.md",\n    "docs/DECISIONS_PENDING.md",\n)\n\nSTALE_CURRENT_CLAIMS = {\n    "README.md": (\n        "플레이 가능한 수직 슬라이스 구현 완료",\n        "Issue #1 Phase 0 Plan Mode",\n        "정확한 경로와 파일은 Phase 0 Plan Mode 승인 후 확정합니다.",\n    ),\n    "docs/OMENWARD_GAME_DESIGN.md": (\n        "Phase 0 Plan Mode 대기 / 구현 전",\n    ),\n    "docs/OMENWARD_ROADMAP.md": (\n        "Codex Plan Mode 실행 대기 / 구현 전",\n        "현재는 Phase 0 구현이나 수직 슬라이스 구현을 시작하지 않는다.",\n    ),\n    "docs/DECISIONS_PENDING.md": (\n        "1. Phase 0 기술 제안서 사용자 검토",\n    ),\n}\n\nREQUIRED_CORE_TERMS = (\n    "EXISTING_CORE_IDENTIFIED",\n    "CORE_LOCK_PENDING_USER_CONFIRMATION",\n    "## 3. 핵심 루프",\n    "## 5. 분류",\n    "## 6. 불변 조건",\n    "## 7. 제거·대체 스트레스 테스트",\n    "## 8. 코어 검증 게이트",\n)\n\nREQUIRED_STATUS_TERMS = (\n    "TECHNICAL_BASELINE_IMPLEMENTED",\n    "CORE_VERTICAL_SLICE_PARTIAL",\n    "CORE_LOOP_NOT_PROVEN",\n    "HUMAN_QA_NOT_RUN",\n    "CORE_CONTRACT_DIVERGENT",\n)\n\n\ndef _read(root: pathlib.Path, relative: str) -> str:\n    return (root / relative).read_text(encoding="utf-8")\n\n\ndef _contains_all(text: str, values: Iterable[str]) -> list[str]:\n    return [value for value in values if value not in text]\n\n\ndef validate(root: pathlib.Path = ROOT) -> list[str]:\n    errors: list[str] = []\n\n    for relative in REQUIRED_FILES:\n        path = root / relative\n        if not path.is_file():\n            errors.append(f"missing required file: {relative}")\n\n    if errors:\n        return errors\n\n    core = _read(root, "docs/PROJECT_CORE.md")\n    status = _read(root, "docs/CURRENT_IMPLEMENTATION_STATUS.md")\n\n    for missing in _contains_all(core, REQUIRED_CORE_TERMS):\n        errors.append(f"PROJECT_CORE missing contract term: {missing}")\n    for missing in _contains_all(status, REQUIRED_STATUS_TERMS):\n        errors.append(f"CURRENT_IMPLEMENTATION_STATUS missing state term: {missing}")\n\n    if "CORE_CONFIRMED" in core or "CORE_LOCKED" in core:\n        errors.append("project core may not claim confirmed/locked without explicit user approval")\n\n    for relative in REFERENCE_FILES:\n        text = _read(root, relative)\n        if "PROJECT_CORE.md" not in text:\n            errors.append(f"{relative} does not reference PROJECT_CORE.md")\n        if "CURRENT_IMPLEMENTATION_STATUS.md" not in text:\n            errors.append(f"{relative} does not reference CURRENT_IMPLEMENTATION_STATUS.md")\n\n    for relative, phrases in STALE_CURRENT_CLAIMS.items():\n        text = _read(root, relative)\n        for phrase in phrases:\n            if phrase in text:\n                errors.append(f"{relative} retains stale current-state claim: {phrase}")\n\n    readme = _read(root, "README.md")\n    if "기술·데이터 그레이박스" not in readme or "코어 루프 미완결" not in readme:\n        errors.append("README does not expose the partial vertical-slice boundary")\n\n    roadmap = _read(root, "docs/OMENWARD_ROADMAP.md")\n    required_sequence = (\n        "정본·프로젝트 코어 복구",\n        "승인 룰렛 계약 복구",\n        "전투 목적 루프 연결",\n        "승인 코어 UX 6종",\n        "코어 플레이테스트",\n    )\n    for missing in _contains_all(roadmap, required_sequence):\n        errors.append(f"roadmap missing recovery sequence item: {missing}")\n\n    decisions = _read(root, "docs/DECISIONS_PENDING.md")\n    if "Godot 4.7.1·Compatibility·960×540" not in decisions:\n        errors.append("DECISIONS_PENDING does not distinguish implemented technical baseline")\n    if "승인 룰렛 계약 복구" not in decisions:\n        errors.append("DECISIONS_PENDING does not point to the next decision gate")\n\n    map_text = _read(root, "docs/DOCUMENTATION_MAP.md")\n    if re.search(r"\\|\\s*프로젝트 코어\\s*\\|\\s*`PROJECT_CORE\\.md`", map_text) is None:\n        errors.append("DOCUMENTATION_MAP has no project-core responsibility row")\n    if re.search(r"\\|\\s*현재 구현 증거\\s*\\|\\s*`CURRENT_IMPLEMENTATION_STATUS\\.md`", map_text) is None:\n        errors.append("DOCUMENTATION_MAP has no implementation-status responsibility row")\n\n    for relative in ("docs/PROJECT_CORE.md", "docs/CURRENT_IMPLEMENTATION_STATUS.md"):\n        text = _read(root, relative)\n        for target in re.findall(r"\\[[^\\]]+\\]\\(([^)]+)\\)", text):\n            if "://" in target or target.startswith("#"):\n                continue\n            resolved = (root / relative).parent / target.split("#", 1)[0]\n            if not resolved.exists():\n                errors.append(f"broken local link in {relative}: {target}")\n\n    return errors\n\n\ndef main() -> int:\n    errors = validate()\n    if errors:\n        print("Project core documentation validation FAILED")\n        for error in errors:\n            print(f"- {error}")\n        return 1\n    print("Project core documentation validation PASSED")\n    return 0\n\n\nif __name__ == "__main__":\n    raise SystemExit(main())\n')
write("tests/python/test_project_core_docs.py", 'from __future__ import annotations\n\nimport pathlib\nimport runpy\nimport shutil\nimport tempfile\nimport unittest\n\nROOT = pathlib.Path(__file__).resolve().parents[2]\nMODULE = runpy.run_path(str(ROOT / "tools" / "validate_project_core_docs.py"))\nvalidate = MODULE["validate"]\n\n\nclass ProjectCoreDocumentationTests(unittest.TestCase):\n    def test_current_repository_passes(self) -> None:\n        self.assertEqual([], validate(ROOT))\n\n    def test_stale_completion_claim_is_rejected(self) -> None:\n        with tempfile.TemporaryDirectory() as directory:\n            temp_root = pathlib.Path(directory)\n            self._copy_contract_files(temp_root)\n            readme = temp_root / "README.md"\n            readme.write_text(\n                readme.read_text(encoding="utf-8")\n                + "\\n플레이 가능한 수직 슬라이스 구현 완료\\n",\n                encoding="utf-8",\n            )\n            errors = validate(temp_root)\n            self.assertTrue(any("stale current-state claim" in error for error in errors))\n\n    def test_missing_core_reference_is_rejected(self) -> None:\n        with tempfile.TemporaryDirectory() as directory:\n            temp_root = pathlib.Path(directory)\n            self._copy_contract_files(temp_root)\n            active = temp_root / "docs" / "ACTIVE_CONTEXT.md"\n            active.write_text(\n                active.read_text(encoding="utf-8").replace("PROJECT_CORE.md", "PROJECT_CORE_REMOVED.md"),\n                encoding="utf-8",\n            )\n            errors = validate(temp_root)\n            self.assertTrue(any("does not reference PROJECT_CORE.md" in error for error in errors))\n\n    def _copy_contract_files(self, destination: pathlib.Path) -> None:\n        for relative in MODULE["REQUIRED_FILES"]:\n            source = ROOT / relative\n            target = destination / relative\n            target.parent.mkdir(parents=True, exist_ok=True)\n            shutil.copy2(source, target)\n\n\nif __name__ == "__main__":\n    unittest.main()\n')

# README
replace_once(
    "README.md",
    "> 현재 상태: **플레이 가능한 수직 슬라이스 구현 완료 / PR 검토·수동 QA 대기**",
    "> 현재 상태: **기술·데이터 그레이박스 수직 슬라이스 존재 / 코어 루프 미완결 / 사람 플레이 검증 대기**",
)
replace_regex("README.md", r"## 먼저 읽을 문서\n.*?(?=## 현재 실행 순서)", '## 먼저 읽을 문서\n\n1. [`AGENTS.md`](AGENTS.md) — 작업 규칙과 승인 게이트\n2. [`docs/PROJECT_CORE.md`](docs/PROJECT_CORE.md) — 제품 정체성, 핵심 선택, 불변 조건과 코어 검증 게이트\n3. [`docs/CURRENT_IMPLEMENTATION_STATUS.md`](docs/CURRENT_IMPLEMENTATION_STATUS.md) — 실제 구현·부분 구현·미검증 증거 경계\n4. [`docs/HANDOFF_CONTEXT.md`](docs/HANDOFF_CONTEXT.md) — 현재 방향, 불변 조건, 데이터 소유와 다음 작업\n5. [`docs/DOCUMENTATION_MAP.md`](docs/DOCUMENTATION_MAP.md) — 작업별 책임 원본 라우터\n6. [`docs/OMENWARD_GAME_DESIGN.md`](docs/OMENWARD_GAME_DESIGN.md) — 공식 전체 기획서\n7. [`docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`](docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md) — 승인 구조 통합 인덱스\n8. [`docs/design/APPROVED_ROULETTE_CORE_RULES.md`](docs/design/APPROVED_ROULETTE_CORE_RULES.md) — 승인 룰렛 판정·등급·보상 계약\n9. [`docs/OMENWARD_ROADMAP.md`](docs/OMENWARD_ROADMAP.md) — 현재 복구 순서와 단계별 완료 기준\n10. [`docs/DECISIONS_PENDING.md`](docs/DECISIONS_PENDING.md) — 현재 결정 게이트와 PoC 조정 항목\n11. [`docs/DOCUMENTATION_MAP.md`](docs/DOCUMENTATION_MAP.md)에서 작업별 추가 책임 원본을 확인\n12. [`docs/ACTIVE_CONTEXT.md`](docs/ACTIVE_CONTEXT.md) — 최신 작업 상태 캡슐\n\n')
replace_regex("README.md", r"## 현재 실행 순서\n.*?## 예정 저장소 구조\n", '## 현재 개선 순서\n\n```text\n[현재] 정본·프로젝트 코어 복구\n→ 승인 룰렛 계약 복구\n→ 전투를 접전지·거점·성문·승패에 연결\n→ 승인 코어 UX 6종 최소 구현\n→ 10~15분 사람 플레이와 1080p·720p 가독성 검증\n→ 밸런스 안정화\n→ 콘텐츠·아트 확장\n```\n\n현재 저장소에는 Godot 기술 기준선과 수직 슬라이스 구성요소가 존재하지만, 승인 룰렛 판정·전투 목적 루프·핵심 UX가 완결되지 않았다. 현재 판정은 `TECHNICAL_BASELINE_IMPLEMENTED`, `CORE_VERTICAL_SLICE_PARTIAL`, `CORE_LOOP_NOT_PROVEN`, `HUMAN_QA_NOT_RUN`이다.\n\n세부 근거와 다음 게이트는 [`docs/CURRENT_IMPLEMENTATION_STATUS.md`](docs/CURRENT_IMPLEMENTATION_STATUS.md)를 따른다. 자동 검증 명령과 수동 QA 항목은 [`docs/VERTICAL_SLICE_VALIDATION.md`](docs/VERTICAL_SLICE_VALIDATION.md)와 [`docs/PHASE_0_VALIDATION.md`](docs/PHASE_0_VALIDATION.md)에 남아 있으며, 실제 재실행 전에는 완료로 보고하지 않는다.\n\n## 현재 저장소 구조\n')
replace_once(
    "README.md",
    "정확한 경로와 파일은 Phase 0 Plan Mode 승인 후 확정합니다.",
    "현재 경로와 파일은 실제 저장소가 권위 원본이며, 구조 변경은 별도 승인·검증 PR에서 수행합니다.",
)

# Active Context
replace_once("docs/ACTIVE_CONTEXT.md", "- 갱신일: 2026-07-16", "- 갱신일: 2026-07-22")
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "- 저장소 상태: **Godot 프로젝트와 플레이 가능한 수직 슬라이스 코드·데이터가 존재함 / 다음 작업 전 실제 main과 검증 문서 재확인 필수**",
    "- 저장소 상태: **기술 기준선 구현 / 핵심 수직 슬라이스 부분 구현 / 코어 루프·사람 플레이 미검증**",
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "- 최초 인수인계: `docs/HANDOFF_CONTEXT.md`",
    "- 프로젝트 코어: `docs/PROJECT_CORE.md`\n- 실제 구현 상태: `docs/CURRENT_IMPLEMENTATION_STATUS.md`\n- 최초 인수인계: `docs/HANDOFF_CONTEXT.md`",
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "## 핵심 정체성\n",
    '## 현재 구현 판정\n\n책임 원본:\n\n- `docs/PROJECT_CORE.md`\n- `docs/CURRENT_IMPLEMENTATION_STATUS.md`\n\n현재 상태는 다음 네 문구를 함께 사용한다.\n\n```text\nTECHNICAL_BASELINE_IMPLEMENTED\n+ CORE_VERTICAL_SLICE_PARTIAL\n+ CORE_LOOP_NOT_PROVEN\n+ HUMAN_QA_NOT_RUN\n```\n\n- Phase 0 기술·데이터 기반과 다수 수직 슬라이스 구성요소는 실제 파일로 존재한다.\n- 승인 룰렛 판정, 전투→거점·성문·승패 연결, 코어 UX 6종은 완결되지 않았다.\n- 자동 테스트 파일의 존재를 최신 runtime·사람 플레이 증거로 간주하지 않는다.\n- 다음 게임 기능 변경은 승인 룰렛 계약 복구로 한정한다.\n\n## 핵심 정체성\n',
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "- 핵심 루프: `베일의 징조 → 건물·토큰 선택 → 룰렛 → 라인 배치 → 거점·성문·우회 공방`.",
    "- 핵심 루프: `베일의 징조 → 건물·확률 설계 → 룰렛 판정 → 라인 배치 → 거점·성문·우회 공방 → 원인 확인 → 다음 설계`.",
)
replace_regex(
    "docs/ACTIVE_CONTEXT.md",
    r"## 다음 작업 원칙\n.*\Z",
    """## 다음 작업 원칙

```text
정본·프로젝트 코어 복구
→ 승인 룰렛 계약 복구
→ 전투 목적 루프 연결
→ 승인 코어 UX 6종
→ 사람 플레이 검증
→ 밸런스·콘텐츠 확장
```

- 새 Codex 채팅은 `docs/PROJECT_CORE.md`와 `docs/CURRENT_IMPLEMENTATION_STATUS.md`를 먼저 읽는다.
- 현재 저장소를 `구현 전` 또는 `수직 슬라이스 완료` 중 하나로 단순화하지 않는다.
- 다음 게임 기능 PR은 승인 룰렛 계약 복구만 포함한다.
- 시각·병종·UI 작업은 새 병종 비주얼 책임 문서와 시각자료 인덱스를 반드시 읽는다.
- 실제 아트 제작 전 대표 병종 5종을 1080p·720p 전장에 삽입해 축소 가독성을 검증한다.
- Base 공용 지식은 방법과 사례 참고용이며 오멘워드 책임 문서를 덮어쓰지 않는다.
""",
)

# Handoff
replace_once("docs/HANDOFF_CONTEXT.md", "- 갱신일: 2026-07-16", "- 갱신일: 2026-07-22")
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "- 현재 상태: **Godot 프로젝트·수직 슬라이스 코드와 데이터 존재 / 다음 작업 전 실제 main·검증 문서·Issue 재조사 필수**",
    "- 현재 상태: **기술 기준선 구현 / 핵심 수직 슬라이스 부분 구현 / 코어 루프·사람 플레이 미검증**",
)
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "- 전체 기획: `docs/OMENWARD_GAME_DESIGN.md`",
    "- 프로젝트 코어: `docs/PROJECT_CORE.md`\n- 실제 구현 상태: `docs/CURRENT_IMPLEMENTATION_STATUS.md`\n- 전체 기획: `docs/OMENWARD_GAME_DESIGN.md`",
)
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "2. 저장소에는 `project.godot`, Scene, GDScript, Resource, 테스트와 수직 슬라이스 관련 파일이 존재한다.\n3. 과거 Phase 0 Work Order의 `구현 전` 문구를 현재 상태로 재사용하지 않는다.\n4. 새 Codex 채팅은 실제 main, validation 문서, Issue·PR·최근 커밋을 먼저 조사한 뒤 다음 Plan Mode 제안서를 작성한다.",
    "2. 저장소에는 Phase 0 기술 기준선과 수직 슬라이스 구성요소가 존재하지만 승인 룰렛·전투 목적·코어 UX는 미완결이다.\n3. 과거 Phase 0 Work Order의 `구현 전`과 README의 과도한 `수직 슬라이스 완료`를 현재 상태로 재사용하지 않는다.\n4. 새 Codex 채팅은 `PROJECT_CORE.md`, `CURRENT_IMPLEMENTATION_STATUS.md`, 실제 main, validation 문서와 Issue·PR을 대조한 뒤 다음 최소 변경을 제안한다.",
)
replace_regex(
    "docs/HANDOFF_CONTEXT.md",
    r"```text\n1\. 최신 사용자 지시\n.*?14\. docs/ACTIVE_CONTEXT\.md\n```",
    """```text
1. 최신 사용자 지시
2. AGENTS.md
3. docs/BASE_RULES_VERSION.md
4. docs/PROJECT_CORE.md
5. docs/CURRENT_IMPLEMENTATION_STATUS.md
6. docs/HANDOFF_CONTEXT.md
7. docs/DOCUMENTATION_MAP.md
8. 현재 작업의 work_orders 문서
9. docs/OMENWARD_GAME_DESIGN.md
10. 관련 APPROVED 책임 문서
11. 시각 작업이면 docs/images/VISUAL_REFERENCE_INDEX.md
12. docs/OMENWARD_ROADMAP.md
13. 현재 Issue / Goal / 승인 제안서
14. project.godot, Scene, scripts, data, tests
15. validation 문서와 실제 실행 결과
16. docs/ACTIVE_CONTEXT.md
```""",
)
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "> 건물을 지어 룰렛 확률과 증원 체계를 설계하고, 베일의 징조로 예고된 공세를 세 전선에서 뒤집는 판타지 전략 오토배틀 게임.",
    "> 예고된 세 전선의 위협을 읽고, 제한된 건물 노드로 룰렛 확률을 설계한 뒤, 당첨된 증원을 어느 전선에 투입할지 결정해 전황을 뒤집는 실시간 전략 오토배틀 게임.",
)
replace_once("docs/HANDOFF_CONTEXT.md", "## 4. 전장 불변 구조\n", '## 3.1 현재 구현 판정\n\n- 프로젝트 코어 책임 원본: `docs/PROJECT_CORE.md`\n- 구현 증거 책임 원본: `docs/CURRENT_IMPLEMENTATION_STATUS.md`\n\n```text\nTECHNICAL_BASELINE_IMPLEMENTED\n+ CORE_VERTICAL_SLICE_PARTIAL\n+ CORE_LOOP_NOT_PROVEN\n+ HUMAN_QA_NOT_RUN\n```\n\n현재 Godot 프로젝트는 기술·데이터 그레이박스와 여러 수직 슬라이스 구성요소를 포함한다. 그러나 승인 룰렛 판정, 전투 상태 기반 승패, 접전지·거점·성문 연결과 승인 UX 6종이 닫히지 않았으므로 “핵심 수직 슬라이스 완료”로 부르지 않는다.\n\n다음 순서는 정본 복구 뒤 승인 룰렛 계약, 전투 목적 루프, 코어 UX, 사람 플레이 검증이다.\n\n## 4. 전장 불변 구조\n')

# GDD
replace_once("docs/OMENWARD_GAME_DESIGN.md", "- 문서 버전: **v0.19**", "- 문서 버전: **v0.20**")
replace_once("docs/OMENWARD_GAME_DESIGN.md", "- 갱신일: 2026-07-16", "- 갱신일: 2026-07-22")
replace_once(
    "docs/OMENWARD_GAME_DESIGN.md",
    "- 상태: **프리프로덕션 구조 승인 완료 / 공용 병종 데이터·진영 비주얼 분리 승인 / Phase 0 Plan Mode 대기 / 구현 전**",
    "- 상태: **프리프로덕션 계약 승인 / Godot 기술·데이터 기준선 구현 / 핵심 수직 슬라이스 부분 구현·코어 루프 미검증**",
)
replace_once(
    "docs/OMENWARD_GAME_DESIGN.md",
    "최초 인수인계 문서는 `docs/HANDOFF_CONTEXT.md`다. 세부 승인 규칙은 `docs/design/APPROVED_*.md`가 우선하며, 통합 인덱스는 `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`다.",
    "프로젝트 코어는 `docs/PROJECT_CORE.md`, 실제 구현 증거는 `docs/CURRENT_IMPLEMENTATION_STATUS.md`, 최초 인수인계는 `docs/HANDOFF_CONTEXT.md`가 소유한다. 세부 승인 규칙은 `docs/design/APPROVED_*.md`가 우선하며, 통합 인덱스는 `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`다.",
)
replace_once("docs/OMENWARD_GAME_DESIGN.md", "---\n\n## 4. 세계관\n", '## 3.1 현재 구현 경계\n\n프로젝트 코어와 실제 구현 상태는 다음 문서를 따른다.\n\n- `docs/PROJECT_CORE.md`\n- `docs/CURRENT_IMPLEMENTATION_STATUS.md`\n\n현재 판정:\n\n```text\nTECHNICAL_BASELINE_IMPLEMENTED\n+ CORE_VERTICAL_SLICE_PARTIAL\n+ CORE_LOOP_NOT_PROVEN\n+ HUMAN_QA_NOT_RUN\n```\n\n이 기획서의 전체 설계와 승인된 초기값이 모두 현재 실행 코드로 완결됐다는 뜻이 아니다. 실제 구현 여부는 상태 문서와 코드·데이터·테스트를 대조한다.\n\n---\n\n## 4. 세계관\n')

# Roadmap
replace_once("docs/OMENWARD_ROADMAP.md", "- 갱신일: 2026-07-16", "- 갱신일: 2026-07-22")
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "- 기준: `docs/HANDOFF_CONTEXT.md`, `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`",
    "- 기준: `docs/PROJECT_CORE.md`, `docs/CURRENT_IMPLEMENTATION_STATUS.md`, `docs/HANDOFF_CONTEXT.md`",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "- 현재 상태: **프리프로덕션 구조 승인 완료 / 새 Codex 채팅용 Phase 0 Work Order 준비 완료 / Codex Plan Mode 실행 대기 / 구현 전**",
    "- 현재 상태: **기술 기준선 구현 / 핵심 수직 슬라이스 부분 구현 / C0 정본·프로젝트 코어 복구 진행**",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "- 현재 Work Order: `docs/work_orders/0001-phase-0-codex-plan-mode.md`",
    "- 현재 조사 입력: `docs/work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md`",
)
replace_regex("docs/OMENWARD_ROADMAP.md", r"## 1\. 현재 위치\n.*?(?=---\n\n## 2\.)", '## 1. 현재 위치\n\n책임 원본:\n\n- 프로젝트 코어: `docs/PROJECT_CORE.md`\n- 실제 구현 상태: `docs/CURRENT_IMPLEMENTATION_STATUS.md`\n\n```text\n프리프로덕션 구조 승인\n→ Phase 0 기술·데이터 기준선 구현\n→ 수직 슬라이스 구성요소 부분 구현\n→ [현재] 정본·프로젝트 코어 복구\n→ 승인 룰렛 계약 복구\n→ 전투 목적 루프 연결\n→ 승인 코어 UX 6종\n→ 10~15분 코어 플레이테스트\n→ 시스템 안정화\n→ 콘텐츠·아트 확장\n→ 캠페인·데모 통합\n```\n\n현재 `구현됨`은 파일과 실행 경로가 있다는 뜻이며 `검증됨`과 같지 않다.\n\n```text\nTECHNICAL_BASELINE_IMPLEMENTED\n≠ CORE_VERTICAL_SLICE_COMPLETE\n≠ CORE_LOOP_PROVEN\n≠ HUMAN_QA_COMPLETE\n```\n\n')
replace_regex(
    "docs/OMENWARD_ROADMAP.md",
    r"\| 단계 \| 목표 \| 현재 상태 \| 다음 게이트 \|\n\|---\|---\|---\|---\|\n(?:\|.*\n)+?(?=\n---)",
    '| 단계 | 목표 | 현재 상태 | 다음 게이트 |\n|---|---|---|---|\n| P0 프리프로덕션 | 제품·전장·공용 데이터·아트·연출 계약 | 완료 | 정본 유지 |\n| P1 기술 기준선 | 실행·데이터·결정론·검증 골격 | **구현됨 / 최신 runtime 재검증 필요** | C0 정본 일치 |\n| C0 정본·코어 복구 | 프로젝트 코어·상태·로드맵 일치 | **진행 중** | 사용자 코어 문구 확인·문서 PR |\n| C1 룰렛 계약 복구 | 중앙 판정 줄·완성선·등급·단일 보상 | 미시작 | 승인 계약 테스트 PASS |\n| C2 전투 목적 루프 | 접전지·거점·성문·승패·경제 연결 | 부분 구현 | End-to-End 전투 PASS |\n| C3 코어 UX | 승인 UX 6종을 실제 데이터와 연결 | 미시작 | 이해도·가독성 기준 |\n| C4 코어 플레이테스트 | 10~15분 핵심 재미와 학습 검증 | 미실행 | 사람 플레이 기준 충족 |\n| P3 시스템 안정화 | 확률·경제·전투·성능 조정 | 미시작 | 반복 가능한 기준선 |\n| P4 콘텐츠·아트 확장 | 10병종·건물·보스·UI·자산 확대 | 미시작 | 제작 QA 통과 |\n| P5 캠페인·데모 | 튜토리얼+정규 스테이지 통합 | 미시작 | 외부 플레이테스트 |\n| P6 출시 준비 | 저장·옵션·패키징·최적화 | 장기 | 릴리스 후보 |',
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "## 4. G1 — Phase 0 Work Order",
    "위 표가 현재 상태의 권위 원본이다. 아래 기존 Phase 정의는 목적·완료 기준의 변경 이력으로 유지하며, 각 절의 과거 상태 문구가 현재 위치를 덮지 않는다.\n\n---\n\n## 4. G1 — Phase 0 Work Order",
)
replace_regex("docs/OMENWARD_ROADMAP.md", r"## 15\. 지금 실행할 단 하나의 작업\n.*\Z", '## 15. 지금 실행할 단 하나의 작업\n\n```text\n정본·프로젝트 코어 복구 Draft PR 검토\n→ 프로젝트 코어 문구의 사용자 확인\n→ 문서 PR 병합\n→ 승인 룰렛 계약 복구를 별도 Plan·Build·Review 작업으로 시작\n```\n\n현재 작업에서는 게임 코드·Scene·Resource·게임 데이터와 승인 수치를 변경하지 않는다. 다음 기능 PR도 룰렛 계약 복구만 포함하며 전투 목적 루프·UX·콘텐츠 확대를 섞지 않는다.\n')

# Decisions
replace_once("docs/DECISIONS_PENDING.md", "- 갱신일: 2026-07-16", "- 갱신일: 2026-07-22")
replace_once(
    "docs/DECISIONS_PENDING.md",
    "- 기준: `docs/HANDOFF_CONTEXT.md`, `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`",
    "- 기준: `docs/PROJECT_CORE.md`, `docs/CURRENT_IMPLEMENTATION_STATUS.md`, `docs/HANDOFF_CONTEXT.md`",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "- 현재 제안서: `docs/design/proposals/0001-phase-0-godot-bootstrap.md`",
    "- 현재 작업: 정본·프로젝트 코어 복구 / 다음 기능 게이트: 승인 룰렛 계약 복구",
)
replace_regex("docs/DECISIONS_PENDING.md", r"## 1\. 현재 가장 먼저 결정할 항목\n.*?(?=---\n\n## 2\.)", '## 1. 현재 가장 먼저 결정할 항목\n\n### A. 프로젝트 코어 문구 잠금\n\n`docs/PROJECT_CORE.md`는 기존 기획과 실제 구현에서 코어를 식별해 `EXISTING_CORE_IDENTIFIED`로 기록한다.\n\n- [ ] 정체성 한 문장과 세 기둥을 사용자 확인 후 `CORE_CONFIRMED`로 전환.\n- [ ] 제거 테스트와 불변 조건을 사용자 확인 후 `CORE_LOCKED`로 전환.\n- 잠금 전에도 수직 슬라이스의 우선순위와 검증 게이트는 해당 문서를 따른다.\n\n### B. 다음 기능 작업 — 승인 룰렛 계약 복구\n\n현재 구현은 9개의 카드를 직접 반환하지만 승인 계약은 중앙 가로줄 판정, 동일 심벌 완성선, 등급과 단일 보상 생성이다.\n\n- [ ] 현재 placeholder 테스트를 승인 계약 테스트로 교체하는 Plan 승인.\n- [ ] X·금화·럭키 찬스·이동권을 한 번에 구현할지 핵심 판정 뒤 순차 구현할지 선택.\n- [ ] 결과 보관함 기본 용량과 UI는 기존 미확정 상태를 유지.\n- [ ] 전투 목적 루프와 코어 UX를 같은 PR에 섞지 않음.\n\n### C. 검증 증거\n\n- [ ] 문서 PR 뒤 Godot editor import와 기존 headless suite 재실행.\n- [ ] 룰렛 복구 PR에서 같은 시드·보드·결과 결정론 검증.\n- [ ] 코어 UX 뒤 1920×1080·1280×720 사람 플레이.\n- [ ] W1~W20 전체 플레이는 코어 루프 완결 뒤 실행.\n\n### D. 이미 구현된 기술 기준선\n\n| 항목 | 현재 상태 |\n|---|---|\n| Godot 4.7.1·Compatibility·960×540 논리 화면·1920×1080 출력 | 실제 `project.godot`에 존재 |\n| Main·GameSession·CombatClock·DeterminismService·DataRegistry | 실제 코드에 존재 |\n| typed Resource·StageManifest·input log | 실제 코드·데이터에 존재 |\n| 공용 10병종과 진영 Visual 분리 골격 | 실제 Resource·validator에 존재 |\n| headless 테스트 파일 | 존재하지만 이번 문서 PR에서 재실행하지 않음 |\n\n과거 Phase 0 추천 항목은 최초 승인 대기 목록으로 사용하지 않는다. 현재 결정은 구현의 존재 여부가 아니라 최신 재검증, 승인 계약과의 차이, 다음 최소 변경 범위다.\n\n')
replace_regex("docs/DECISIONS_PENDING.md", r"## 10\. 기술·성능·테스트\n.*?(?=### 성능 첫 가설)", '## 10. 기술·성능·테스트\n\n### 현재 구현됨 / 최신 재검증 필요\n\n- [x] Godot 4.7.1 standard 기준 프로젝트 파일.\n- [x] Compatibility renderer.\n- [x] 960×540 viewport·integer scale·1920×1080 출력.\n- [x] 현재 Phase 0 AutoLoad 없음.\n- [x] typed Resource와 StageManifest·input log 경계.\n- [x] 이름 기반 RNG stream과 input log 구조.\n- [x] GDScript headless test 파일.\n\n현재 전투 고정 스텝은 `BattleSimulator.FIXED_STEP_SECONDS = 0.1`이다. 과거 60Hz 제안과 같다고 간주하지 않으며, 성능·판정 요구를 근거로 별도 결정한다.\n\n### 성능 첫 가설')
replace_regex("docs/DECISIONS_PENDING.md", r"## 12\. 현재 실행 순서\n.*\Z", '## 12. 현재 실행 순서\n\n```text\n1. 정본·프로젝트 코어 복구 PR 검토\n2. 프로젝트 코어 문구 잠금 여부 사용자 확인\n3. 승인 룰렛 계약 복구 Plan\n4. 룰렛 계약 구현·자동 검증\n5. 전투 목적 루프 연결\n6. 승인 코어 UX 6종\n7. 10~15분 사람 플레이와 1080p·720p QA\n8. 밸런스 안정화\n9. 콘텐츠·아트 확장\n```\n\n현재는 새로운 병종·Tier·보스·캠페인 콘텐츠를 추가하는 단계가 아니다. 다음 기능 변경은 승인 룰렛 계약 복구로 제한한다.\n')

# Documentation Map
replace_regex(
    "docs/DOCUMENTATION_MAP.md",
    r"```text\n최신 사용자 지시\n.*?→ ACTIVE_CONTEXT\.md\n```",
    """```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ PROJECT_CORE.md
→ CURRENT_IMPLEMENTATION_STATUS.md
→ HANDOFF_CONTEXT.md
→ DOCUMENTATION_MAP.md
→ 현재 Codex 작업이면 work_orders 문서
→ OMENWARD_GAME_DESIGN.md
→ 관련 APPROVED 책임 문서
→ 시각 작업이면 docs/images/VISUAL_REFERENCE_INDEX.md
→ OMENWARD_ROADMAP.md
→ 현재 Issue / Goal / 승인 제안서
→ 실제 파일과 테스트
→ ACTIVE_CONTEXT.md
```""",
)
replace_once(
    "docs/DOCUMENTATION_MAP.md",
    "- `HANDOFF_CONTEXT.md`는 현재 방향과 다음 행동을 압축한 최초 인수인계 문서다.",
    "- `PROJECT_CORE.md`는 제품 정체성·핵심 선택·불변 조건·코어 검증 게이트의 최상위 책임 원본이다.\n- `CURRENT_IMPLEMENTATION_STATUS.md`는 구현·부분 구현·미검증 증거 경계의 책임 원본이다.\n- `HANDOFF_CONTEXT.md`는 현재 방향과 다음 행동을 압축한 최초 인수인계 문서다.",
)
replace_once(
    "docs/DOCUMENTATION_MAP.md",
    "| `HANDOFF_CONTEXT.md` | 현재 방향, 불변 조건, 데이터 소유, 다음 실행 순서 |",
    "| `PROJECT_CORE.md` | 제품 정체성, 핵심 선택, 불변 조건, 제거 테스트, 코어 검증 게이트 |\n| `CURRENT_IMPLEMENTATION_STATUS.md` | 실제 구현·부분 구현·승인 계약 차이·미검증 증거 |\n| `HANDOFF_CONTEXT.md` | 현재 방향, 불변 조건, 데이터 소유, 다음 실행 순서 |",
)
replace_once(
    "docs/DOCUMENTATION_MAP.md",
    "| 새 Codex 채팅·현재 main 조사 | `work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md`, `PROPOSAL_WORKFLOW.md`, 현재 Issue·PR·Goal |",
    "| 프로젝트 코어·우선순위·기능 제거 판단 | `PROJECT_CORE.md`, `CURRENT_IMPLEMENTATION_STATUS.md`, 관련 APPROVED 문서 |\n| 새 Codex 채팅·현재 main 조사 | `PROJECT_CORE.md`, `CURRENT_IMPLEMENTATION_STATUS.md`, `work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md`, `PROPOSAL_WORKFLOW.md`, 현재 Issue·PR·Goal |",
)
replace_once(
    "docs/DOCUMENTATION_MAP.md",
    "| 프로젝트 인수인계 | `HANDOFF_CONTEXT.md` |",
    "| 프로젝트 코어 | `PROJECT_CORE.md` |\n| 현재 구현 증거 | `CURRENT_IMPLEMENTATION_STATUS.md` |\n| 프로젝트 인수인계 | `HANDOFF_CONTEXT.md` |",
)

run("python", "tools/validate_project_core_docs.py")
run("python", "-m", "unittest", "discover", "-s", "tests/python", "-v")
run("python", "-m", "py_compile", "tools/validate_project_core_docs.py", "tests/python/test_project_core_docs.py")
run("python", "tools/validate_skill_system.py")

for relative in (
    "tools/_apply_project_core_recovery.py",
    "docs/_CORE_RECOVERY_FAILURE.log",
    "project-core-recovery.log",
):
    path = ROOT / relative
    if path.exists():
        path.unlink()

for cache in ROOT.rglob("__pycache__"):
    for child in cache.iterdir():
        child.unlink()
    cache.rmdir()

run("git", "add", "-A")
run("git", "diff", "--cached", "--check")
run("git", "config", "user.name", "github-actions[bot]")
run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
run("git", "commit", "-m", "restore project core canon and current implementation status")
run("git", "push", "origin", "HEAD:agent/project-core-canon-recovery")
