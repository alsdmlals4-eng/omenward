from __future__ import annotations

import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE_COMMIT = "6c63f70e3b0993429492cd033cfeb0d91a0a9f2d"
RUNTIME_PATH = ROOT / "tools" / "_apply_c1_roulette_contract_runtime.py"

body = subprocess.check_output(
    ["git", "show", f"{SOURCE_COMMIT}:tools/_apply_c1_roulette_contract.py"],
    cwd=ROOT,
    text=True,
)
body = body.replace(
    '+ "\\n# return cards\\n", encoding="utf-8")',
    '+ "\\\\n# return cards\\\\n", encoding="utf-8")',
)
body = body.replace(
    '+ "\\n`docs/work_orders/0001-phase-0-codex-plan-mode.md`\\n", encoding="utf-8")',
    '+ "\\\\n`docs/work_orders/0001-phase-0-codex-plan-mode.md`\\\\n", encoding="utf-8")',
)
cleanup_marker = '    "docs/_C1_SHORTLIST_FAILURE.log",\n'
if cleanup_marker not in body:
    raise RuntimeError("C1 cleanup marker missing")
body = body.replace(
    cleanup_marker,
    cleanup_marker
    + '    "docs/_C1_APPLY_FAILURE.log",\n'
    + '    "docs/_C1_FINAL_APPLY_FAILURE.log",\n'
    + '    "docs/_EXECUTION_FAILURE.log",\n'
    + '    "contract-execution.log",\n'
    + '    "tools/_apply_c1_roulette_contract_runtime.py",\n'
    + '    ".github/workflows/apply-c1-roulette-contract-final-once.yml",\n',
    1,
)
insertion_marker = "# Documentation map: remove task-specific legacy files from active routing."
insertion = '''replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "- 현재 조사 입력: `docs/work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md`",
    "- 현재 구현·감사 입력: `docs/C1_ROULETTE_RECOVERY_REPORT_2026-07-22.md`",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "- 사전 기술 추천안: `docs/design/proposals/0001-phase-0-godot-bootstrap.md`",
    "- 기술 기준선: 실제 `project.godot`, 코드·데이터·테스트와 `docs/CURRENT_IMPLEMENTATION_STATUS.md`",
)
old_plan = ROOT / "docs/superpowers/plans/2026-07-16-vertical-slice-stage-progression.md"
if old_plan.exists():
    old_plan.unlink()

'''
if insertion_marker not in body:
    raise RuntimeError("C1 documentation insertion marker missing")
body = body.replace(insertion_marker, insertion + insertion_marker, 1)
validator_marker = "# Delete temporary audit payloads and bootstrap files."
validator_sync = '''replace_once(
    "tools/validate_project_core_docs.py",
    '    "CORE_CONTRACT_DIVERGENT",',
    '    "C1_IMPLEMENTED_CANDIDATE",',
)
replace_once(
    "tools/validate_project_core_docs.py",
    '        "승인 룰렛 계약 복구",',
    '        "승인 룰렛 핵심 계약 복구",',
)

'''
if validator_marker not in body:
    raise RuntimeError("project core validator sync marker missing")
body = body.replace(validator_marker, validator_sync + validator_marker, 1)
workflow_start = body.index('write(\n    ".github/workflows/validate-c1-roulette.yml",')
workflow_end = body.index("# Delete temporary audit payloads and bootstrap files.", workflow_start)
body = body[:workflow_start] + body[workflow_end:]
RUNTIME_PATH.write_text(body, encoding="utf-8", newline="\n")
subprocess.run(["python", str(RUNTIME_PATH)], cwd=ROOT, check=True)
