from __future__ import annotations

import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tools" / "_mark_validation_evidence.py"
RUNTIME = ROOT / "tools" / "_mark_validation_evidence_runtime.py"

text = SOURCE.read_text(encoding="utf-8")
marker = "# Self-clean before validation."
insertion = '''replace_once(
    "tests/python/test_c1_roulette_contract.py",
    '            "docs/OMENWARD_GAME_DESIGN.md",\n            "docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md",',
    '            "docs/OMENWARD_GAME_DESIGN.md",\n            "docs/CURRENT_IMPLEMENTATION_STATUS.md",\n            "docs/OMENWARD_ROADMAP.md",\n            "docs/design/APPROVED_ROULETTE_CORE_RULES.md",\n            "docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md",',
)
replace_once(
    "tools/validate_project_core_docs.py",
    '    if "기술·데이터 그레이박스" not in readme or "코어 루프 미완결" not in readme:\n        errors.append("README does not expose the partial vertical-slice boundary")',
    '    if "C1 룰렛 핵심 계약 원격 검증 완료" not in readme or "전투 목적 루프·사람 플레이 미완결" not in readme:\n        errors.append("README does not expose the proven C1 and partial core-loop boundary")',
)
replace_once(
    "tools/validate_project_core_docs.py",
    '    if "승인 룰렛 계약 복구" not in decisions:\n        errors.append("DECISIONS_PENDING does not point to the next decision gate")',
    '    if "C1U 이동권·럭키" not in decisions:\n        errors.append("DECISIONS_PENDING does not point to the C1U decision gate")',
)

'''
if marker not in text:
    raise RuntimeError("evidence synchronizer insertion marker missing")
text = text.replace(marker, insertion + marker, 1)
text = text.replace(
    'script = ROOT / "tools/_mark_validation_evidence.py"\nif script.exists():\n    script.unlink()',
    'for relative in (\n    "tools/_mark_validation_evidence.py",\n    "tools/_sync_evidence_runtime.py",\n    "tools/_mark_validation_evidence_runtime.py",\n    "docs/_EVIDENCE_SYNC_FAILURE.log",\n):\n    path = ROOT / relative\n    if path.exists():\n        path.unlink()',
)
RUNTIME.write_text(text, encoding="utf-8", newline="\n")
subprocess.run(["python", str(RUNTIME)], cwd=ROOT, check=True)
