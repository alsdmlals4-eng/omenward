from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
C2_HEAD = "85e2930a839fd210548c7aa2a53125d18c4de875"
C2_RUN = "29934172758"

ACTIVE_DOCS = (
    "README.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/OMENWARD_GAME_DESIGN.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/DECISIONS_PENDING.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/VERTICAL_SLICE_VALIDATION.md",
    "docs/GODOT_PROJECT_STRUCTURE.md",
    "docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md",
    "docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md",
    "docs/design/APPROVED_SHARED_UNIT_ARCHETYPE_AND_FACTION_VISUAL_DATA_V1.md",
    "docs/design/APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md",
    "docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md",
)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def write(relative: str, text: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def replace_required(relative: str, old: str, new: str) -> None:
    text = read(relative)
    if old not in text:
        raise RuntimeError(f"{relative}: missing required transition source: {old!r}")
    write(relative, text.replace(old, new))


for relative in ACTIVE_DOCS:
    text = read(relative)
    replacements = (
        ("C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE / C2_REMOTE_VALIDATION_PENDING", "C2_BATTLE_OBJECTIVE_REMOTE_PROVEN"),
        ("C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE", "C2_BATTLE_OBJECTIVE_REMOTE_PROVEN"),
        ("C2_REMOTE_VALIDATION_PENDING", "C2_BATTLE_OBJECTIVE_REMOTE_PROVEN"),
        ("C2_BATTLE_OBJECTIVE_REMOTE_PROVEN / C2_BATTLE_OBJECTIVE_REMOTE_PROVEN", "C2_BATTLE_OBJECTIVE_REMOTE_PROVEN"),
        ("C2 전투 목적 루프 구현 후보·원격 검증 진행", "C2 전투 목적 루프 REMOTE_PROVEN"),
        ("C2 전투 목적 구현 후보·원격 검증 진행", "C2 전투 목적 REMOTE_PROVEN"),
        ("[현재] C2 전투 목적 구현 후보·공통 원격 검증", "C2 전투 목적 루프 원격 검증 완료"),
        ("C2 전투 목적 구현 후보·공통 원격 검증", "C2 전투 목적 루프 원격 검증 완료"),
        ("C2 전투 목적 루프 구현 후보·원격 검증", "C2 전투 목적 루프 원격 검증 완료"),
        ("C2 전투 목적 루프 구현 후보", "C2 전투 목적 루프 검증 구현"),
        ("C2 구현 후보", "C2 검증 구현"),
        ("최종 공통 원격 검증과 사람 플레이는 남아 있다", "공통 원격 검증은 완료됐고 사람 플레이는 남아 있다"),
        ("C2 원격 검증 완료 전에는", "C3와 사람 플레이 완료 전에는"),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    text = re.sub(
        r"(?m)^(\s*[-+]\s*`?C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`?\s*)\n\1$",
        r"\1",
        text,
    )
    write(relative, text)

# Status evidence and exact current-state boundaries.
status = read("docs/CURRENT_IMPLEMENTATION_STATUS.md")
status = re.sub(r"- C2 구현 (?:후보|검증) head: `[^`]+`", f"- C2 구현 검증 head: `{C2_HEAD}`", status)
if "- C2 최종 검증 run:" not in status:
    status = status.replace(
        f"- C2 구현 검증 head: `{C2_HEAD}`",
        f"- C2 구현 검증 head: `{C2_HEAD}`\n- C2 최종 검증 run: `{C2_RUN}`",
        1,
    )
status = status.replace("| `IMPLEMENTED_CANDIDATE` | 구현과 로컬·부분 원격 회귀가 존재하지만 최종 공통 CI 증거가 아직 고정되지 않음 |\n", "")
status = status.replace("| 공용 병종 | 공용 10 archetype, Tier·Rank·FactionVisual, 공용 점령력·구조물 피해 태그 | `IMPLEMENTED_CANDIDATE` |", "| 공용 병종 | 공용 10 archetype, Tier·Rank·FactionVisual, 공용 점령력·구조물 피해 태그 | `REMOTE_PROVEN` |")
status = status.replace("| 경제·건설 | 기본·접전지·거점 수입, 식량, 거점 revision 기반 건물 활성·비활성·폐허 | `IMPLEMENTED_CANDIDATE` |", "| 경제·건설 | 기본·접전지·거점 수입, 식량, 거점 revision 기반 건물 활성·비활성·폐허 | `REMOTE_PROVEN` |")
status = status.replace("| 테스트 | C1·C2·전투·경제·건설·웨이브·우회 headless 및 Python mutation 계약 | `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN` |", "| 테스트 | C1·C2·전투·경제·건설·웨이브·우회 headless 및 Python mutation 계약 | `REMOTE_PROVEN` |")
status = status.replace("판정: `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`.", f"판정: `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN` — Godot 4.7.1 전체 회귀와 4환경 계약 검증 통과 (head `{C2_HEAD}`, run `{C2_RUN}`).")
status = status.replace("1. C2 공통 코어 계약 원격 검증과 PR #50 검토", "1. C3 승인 코어 UX 6종 최소 구현")
status = status.replace("2. C1U 이동권·럭키·상위 템플릿 사용자 결정", "2. C1U 이동권·럭키·상위 템플릿 사용자 결정 게이트")
write("docs/CURRENT_IMPLEMENTATION_STATUS.md", status)

audit = read("docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md")
audit = re.sub(r"- 작업 상태: `[^`]+`", "- 작업 상태: `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`", audit, count=1)
audit = audit.replace(
    "최종 공통 `Core Contracts` Workflow의 head·run을 고정하기 전이므로 현재 판정은 `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`이다.",
    f"최종 공통 검증은 구현 head `{C2_HEAD}`, GitHub Actions run `{C2_RUN}`에서 통과했다. 판정은 `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`이다.",
)
write("docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md", audit)

roadmap = read("docs/OMENWARD_ROADMAP.md")
roadmap = roadmap.replace("- 현재 상태: **C0·C1 완료 / C2 전투 목적 REMOTE_PROVEN / C1U 사용자 결정 대기**", "- 현재 상태: **C0·C1·C2 REMOTE_PROVEN / C1U 사용자 결정 대기 / C3 코어 UX 다음 구현**")
roadmap = roadmap.replace("| C2 전투 목적 루프 | 접전지·거점·성문·승패·경제 연결 | **IMPLEMENTED_CANDIDATE / REMOTE_VALIDATION_PENDING** | 공통 Core Contracts PASS |", "| C2 전투 목적 루프 | 접전지·거점·성문·승패·경제 연결 | **REMOTE_PROVEN** | 정본 유지 |")
roadmap = roadmap.replace("| C3 코어 UX | 승인 UX 6종을 실제 데이터와 연결 | 미시작 | 이해도·가독성 기준 |", "| C3 코어 UX | 승인 UX 6종을 실제 데이터와 연결 | **다음 구현** | 이해도·가독성 기준 |")
roadmap = roadmap.replace("PR #50 C2 공통 Core Contracts 원격 검증\n→ 구현·문서·구형 참조 적대적 검토\n→ 병합 결정\n→ C1U 사용자 결정 또는 C3 코어 UX Plan", "PR #50 C2 검증 결과 병합\n→ C3 승인 코어 UX 6종 최소 구현\n→ C1U는 사용자 결정 전 보류\n→ 10~15분 사람 플레이 준비")
roadmap = roadmap.replace("C2는 별도 PR #50에서 구현 후보를 검증한다.", f"C2는 head `{C2_HEAD}`, run `{C2_RUN}`에서 원격 검증됐다.")
write("docs/OMENWARD_ROADMAP.md", roadmap)

readme = read("README.md")
readme = readme.replace("→ C2 전투 목적 루프 원격 검증 완료\n→ [결정 게이트] C1U", "→ C2 전투 목적 루프 원격 검증 완료\n→ [다음 구현] C3 승인 코어 UX 6종\n→ [결정 게이트] C1U")
readme = readme.replace("→ 승인 코어 UX 6종 최소 구현\n", "")
readme = readme.replace("현재 저장소에는 C1 룰렛 핵심 계약과 C2 전투 목적 루프 검증 구현가 존재한다.", "현재 저장소에는 원격 검증된 C1 룰렛 핵심 계약과 C2 전투 목적 루프가 존재한다.")
readme = readme.replace("현재 저장소에는 C1 룰렛 핵심 계약과 C2 전투 목적 루프 검증 구현이 존재한다.", "현재 저장소에는 원격 검증된 C1 룰렛 핵심 계약과 C2 전투 목적 루프가 존재한다.")
write("README.md", readme)

# Validator transition: proven state, stale-candidate rejection, and durable Core Contracts workflow.
c2_validator = read("tools/validate_c2_battle_objective.py")
c2_validator = c2_validator.replace('"README.md": ("C2 전투 목적 루프 구현 후보", "사람 플레이 미완결")', '"README.md": ("C2 전투 목적 루프 REMOTE_PROVEN", "사람 플레이 미완결")')
c2_validator = c2_validator.replace('("C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE", "C2_REMOTE_VALIDATION_PENDING")', '("C2_BATTLE_OBJECTIVE_REMOTE_PROVEN",)')
c2_validator = c2_validator.replace('("문서 버전: **v0.22**", "C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE")', '("문서 버전: **v0.22**", "C2_BATTLE_OBJECTIVE_REMOTE_PROVEN")')
c2_validator = c2_validator.replace('("C2 전투 목적 구현 후보·공통 원격 검증",)', '("C2 전투 목적 루프 원격 검증 완료",)')
c2_validator = c2_validator.replace('("C2 전투 목적 루프 구현 후보", "본진 독립 HP")', '("C2 전투 목적 루프 원격 검증 완료", "본진 독립 HP")')
c2_validator = c2_validator.replace('errors.append(f"{relative} missing C2 candidate state: {phrase}")', 'errors.append(f"{relative} missing proven C2 state: {phrase}")')
c2_validator = c2_validator.replace('        "전투 상태 기반 승패, 접전지·거점·성문 연결과 승인 UX 6종은 닫히지 않았다",', '        "전투 상태 기반 승패, 접전지·거점·성문 연결과 승인 UX 6종은 닫히지 않았다",\n        "C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE",\n        "C2_REMOTE_VALIDATION_PENDING",')
c2_validator = c2_validator.replace('    for path in root.rglob("*"):', f'    status = (root / "docs/CURRENT_IMPLEMENTATION_STATUS.md").read_text(encoding="utf-8")\n    for evidence in ("C2 구현 검증 head: `{C2_HEAD}`", "C2 최종 검증 run: `{C2_RUN}`"):\n        if evidence not in status:\n            errors.append(f"CURRENT_IMPLEMENTATION_STATUS missing C2 proof: {{evidence}}")\n    audit = (root / "docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md").read_text(encoding="utf-8")\n    for evidence in ("C2_BATTLE_OBJECTIVE_REMOTE_PROVEN", "`{C2_HEAD}`", "`{C2_RUN}`"):\n        if evidence not in audit:\n            errors.append(f"C2 audit missing final proof: {{evidence}}")\n\n    for path in root.rglob("*"):', 1)
write("tools/validate_c2_battle_objective.py", c2_validator)

c2_test = read("tests/python/test_c2_battle_objective_contract.py")
c2_test = c2_test.replace("test_missing_c2_candidate_state_is_rejected", "test_missing_c2_proven_state_is_rejected")
c2_test = c2_test.replace("C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE", "C2_BATTLE_OBJECTIVE_REMOTE_PROVEN")
c2_test = c2_test.replace("missing C2 candidate state", "missing proven C2 state")
if "test_stale_c2_candidate_state_is_rejected" not in c2_test:
    insert = '''\n    def test_stale_c2_candidate_state_is_rejected(self) -> None:\n        with tempfile.TemporaryDirectory() as directory:\n            root = pathlib.Path(directory)\n            self._copy_contract_files(root)\n            status = root / "docs/CURRENT_IMPLEMENTATION_STATUS.md"\n            status.write_text(status.read_text(encoding="utf-8") + "\\nC2_REMOTE_VALIDATION_PENDING\\n", encoding="utf-8")\n            self.assertTrue(any("stale C1/C2 state" in error for error in validate(root)))\n'''
    c2_test = c2_test.replace("\n\nif __name__ == \"__main__\":", insert + "\n\nif __name__ == \"__main__\":")
write("tests/python/test_c2_battle_objective_contract.py", c2_test)

core_validator = read("tools/validate_project_core_docs.py")
core_validator = core_validator.replace('    "C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE",\n    "C2_REMOTE_VALIDATION_PENDING",', '    "C2_BATTLE_OBJECTIVE_REMOTE_PROVEN",')
core_validator = core_validator.replace('"C2 전투 목적 루프 구현 후보" not in readme', '"C2 전투 목적 루프 REMOTE_PROVEN" not in readme')
core_validator = core_validator.replace('"README does not expose the proven C1, candidate C2, and human-QA boundary"', '"README does not expose proven C1/C2 and the human-QA boundary"')
core_validator = core_validator.replace('        "C2 전투 목적 구현 후보",', '        "C2 전투 목적 루프 원격 검증 완료",')
write("tools/validate_project_core_docs.py", core_validator)

vertical = read("docs/VERTICAL_SLICE_VALIDATION.md")
vertical = vertical.replace("python tools/validate_c1_roulette.py\n", "python tools/validate_c1_roulette.py\npython tools/validate_c2_battle_objective.py\n")
vertical = vertical.replace("GitHub Actions의 `Validate C1 Roulette Contract`", "GitHub Actions의 `Validate Core Contracts`")
write("docs/VERTICAL_SLICE_VALIDATION.md", vertical)

core_workflow = '''name: Validate Core Contracts

on:
  pull_request:
    paths:
      - "scripts/**"
      - "scenes/**"
      - "data/**"
      - "tests/**"
      - "docs/**"
      - "README.md"
      - "tools/validate_*.py"
      - ".github/workflows/validate-core-contracts.yml"
  workflow_dispatch:

permissions:
  contents: read

jobs:
  contracts:
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest]
        python-version: ["3.12", "3.13"]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - name: Compile Python contracts
        run: python -m py_compile tools/validate_c1_roulette.py tools/validate_c2_battle_objective.py tools/validate_project_core_docs.py tests/python/test_c1_roulette_contract.py tests/python/test_c2_battle_objective_contract.py
      - name: Validate C1 and C2 contracts
        run: |
          python tools/validate_c1_roulette.py
          python tools/validate_c2_battle_objective.py
      - name: Run all Python repository tests
        run: python -m unittest discover -s tests/python -v
      - name: Validate project core documents
        run: python tools/validate_project_core_docs.py
      - name: Validate Skill system when present
        shell: bash
        run: |
          if [ -f tools/validate_skill_system.py ]; then python tools/validate_skill_system.py; fi
      - name: Check whitespace
        run: git diff --check

  godot:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Godot 4.7.1 Standard
        shell: bash
        run: |
          curl -fL "https://github.com/godotengine/godot-builds/releases/download/4.7.1-stable/Godot_v4.7.1-stable_linux.x86_64.zip" -o godot.zip
          unzip -q godot.zip
          chmod +x Godot_v4.7.1-stable_linux.x86_64
          ./Godot_v4.7.1-stable_linux.x86_64 --version
      - name: Import project
        run: ./Godot_v4.7.1-stable_linux.x86_64 --headless --path . --editor --quit
      - name: Run all headless contract tests
        shell: bash
        run: |
          set -euo pipefail
          for test_file in tests/headless/*_test.gd; do
            echo "Running ${test_file}"
            ./Godot_v4.7.1-stable_linux.x86_64 --headless --path . -s "res://${test_file}"
          done
      - name: Runtime smoke
        run: ./Godot_v4.7.1-stable_linux.x86_64 --headless --path . --quit-after 1
'''
write(".github/workflows/validate-core-contracts.yml", core_workflow)

for relative in (
    ".github/workflows/validate-c1-roulette.yml",
    ".github/workflows/finalize-c2-remote-proof.yml",
    "tools/_finalize_c2_remote_proof.py",
):
    path = ROOT / relative
    if path.exists():
        path.unlink()

# Final no-loss and stale-state assertions.
for relative in ACTIVE_DOCS:
    text = read(relative)
    for stale in ("C2_BATTLE_OBJECTIVE_IMPLEMENTED_CANDIDATE", "C2_REMOTE_VALIDATION_PENDING"):
        if stale in text:
            raise RuntimeError(f"{relative}: stale C2 state remains: {stale}")
if (ROOT / ".github/workflows/validate-c1-roulette.yml").exists():
    raise RuntimeError("legacy C1-only workflow remains")
