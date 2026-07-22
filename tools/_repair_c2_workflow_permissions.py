from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
FINALIZER = ROOT / "tools/_finalize_c2_remote_proof.py"
text = FINALIZER.read_text(encoding="utf-8")

text = text.replace(
    'write(".github/workflows/validate-core-contracts.yml", core_workflow)',
    '# Workflow creation is applied separately through the user-authorized GitHub connector.',
    1,
)
old_cleanup = '''for relative in (
    ".github/workflows/validate-c1-roulette.yml",
    ".github/workflows/finalize-c2-remote-proof.yml",
    "tools/_finalize_c2_remote_proof.py",
):'''
new_cleanup = '''for relative in (
    "tools/_finalize_c2_remote_proof.py",
):'''
if old_cleanup not in text:
    raise RuntimeError("workflow cleanup block missing")
text = text.replace(old_cleanup, new_cleanup, 1)
text = text.replace(
    '''if (ROOT / ".github/workflows/validate-c1-roulette.yml").exists():
    raise RuntimeError("legacy C1-only workflow remains")
''',
    '',
    1,
)
FINALIZER.write_text(text, encoding="utf-8", newline="\n")
pathlib.Path(__file__).unlink()
