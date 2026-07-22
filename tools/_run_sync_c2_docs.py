from __future__ import annotations

import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tools/_sync_c2_docs.py"
RUNTIME = ROOT / "tools/_sync_c2_docs_runtime.py"

body = SOURCE.read_text(encoding="utf-8")
body = body.replace(
    '- C1 최종 검증: head `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9` / run `29926598807`',
    '- C1 구현 검증 head: `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9`\n- C1 최종 검증 run: `29926598807`',
    1,
)
body = body.replace(
    'roadmap.write_text(roadmap.read_text(encoding="utf-8") + "\\nPR #49 사용자 검토 대기\\n", encoding="utf-8")',
    'roadmap.write_text(roadmap.read_text(encoding="utf-8") + "\\\\nPR #49 사용자 검토 대기\\\\n", encoding="utf-8")',
    1,
)

validator_marker = '# Project core validator candidate state\n'
validator_sync = '''# Preserve C1 proof while allowing C2 candidate-state terminology.
replace_once(
    "tools/validate_c1_roulette.py",
    '    if "문서 버전: **v0.21**" not in gdd:',
    '    if "문서 버전: **v0.22**" not in gdd:',
)
replace_once(
    "tools/validate_c1_roulette.py",
    '        "IMPLEMENTED_CANDIDATE / REMOTE_VALIDATION_PENDING",\\n',
    '',
)
replace_once(
    "tools/validate_project_core_docs.py",
    '        "전투 목적 루프 연결",',
    '        "C2 전투 목적 구현 후보",',
)

'''
if validator_marker not in body:
    raise RuntimeError("project core validator marker missing")
body = body.replace(validator_marker, validator_sync + validator_marker, 1)

cleanup_marker = '# Remove the synchronizer before validation; durable docs preserve its result.\n'
cleanup = '''for relative in (
    ".github/workflows/sync-c2-docs.yml",
    "docs/_C2_DOC_SYNC_FAILURE.log",
    "tools/_run_sync_c2_docs.py",
    "tools/_sync_c2_docs_runtime.py",
):
    path = ROOT / relative
    if path.exists():
        path.unlink()

'''
if cleanup_marker not in body:
    raise RuntimeError("C2 sync cleanup marker missing")
body = body.replace(cleanup_marker, cleanup + cleanup_marker, 1)
RUNTIME.write_text(body, encoding="utf-8", newline="\n")
subprocess.run(["python", str(RUNTIME)], cwd=ROOT, check=True)
