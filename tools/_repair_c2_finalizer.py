from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
FINALIZER = ROOT / "tools/_finalize_c2_remote_proof.py"
text = FINALIZER.read_text(encoding="utf-8")

old_regex = 'status = re.sub(r"- C2 구현 (?:후보|검증) head: `[^`]+`", f"- C2 구현 검증 head: `{C2_HEAD}`", status)'
new_regex = 'status = re.sub(r"- C2 [^\\n]* head: `[^`]+`", f"- C2 구현 검증 head: `{C2_HEAD}`", status)'
if old_regex not in text:
    raise RuntimeError("C2 evidence-head transition source missing")
text = text.replace(old_regex, new_regex, 1)

marker = 'write("README.md", readme)\n\n# Validator transition:'
decisions_fix = '''write("README.md", readme)

decisions = read("docs/DECISIONS_PENDING.md")
decisions = decisions.replace("C2 전투 목적 루프 검증 구현", "C2 전투 목적 루프 원격 검증 완료")
if "C2 전투 목적 루프 원격 검증 완료" not in decisions:
    decisions += "\\n- C2 전투 목적 루프 원격 검증 완료.\\n"
write("docs/DECISIONS_PENDING.md", decisions)

# Validator transition:'''
if marker not in text:
    raise RuntimeError("C2 decisions transition marker missing")
text = text.replace(marker, decisions_fix, 1)

FINALIZER.write_text(text, encoding="utf-8", newline="\n")
pathlib.Path(__file__).unlink()
