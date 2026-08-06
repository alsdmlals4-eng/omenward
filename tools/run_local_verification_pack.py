#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEAD_COMMAND = "git rev-parse HEAD"
EXPECTED_VERSIONS = {
    "windows-py311": (3, 11),
    "windows-py312": (3, 12),
    "windows-py313": (3, 13),
    "wsl2-ubuntu-py312": (3, 12),
}


def run(command: list[str]) -> dict[str, object]:
    result = subprocess.run(
        command, cwd=ROOT, text=True, capture_output=True, check=False
    )
    return {
        "command": command,
        "exit_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--environment-id", required=True, choices=sorted(EXPECTED_VERSIONS))
    parser.add_argument("--expected-head", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    actual_head_result = run(HEAD_COMMAND.split())
    actual_head = str(actual_head_result["stdout"]).strip()
    receipt: dict[str, object] = {
        "schema_version": 1,
        "environment_id": args.environment_id,
        "expected_head": args.expected_head,
        "actual_head": actual_head,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "started_at_utc": datetime.now(timezone.utc).isoformat(),
        "commands": [actual_head_result],
        "overall": "FAIL",
    }

    expected_version = EXPECTED_VERSIONS[args.environment_id]
    if sys.version_info[:2] != expected_version:
        receipt["failure"] = (
            f"python version mismatch: expected {expected_version}, "
            f"actual {sys.version_info[:2]}"
        )
    elif actual_head_result["exit_code"] != 0:
        receipt["failure"] = "git rev-parse HEAD failed"
    elif actual_head != args.expected_head:
        receipt["failure"] = "exact HEAD mismatch"
    else:
        commands = [
            [
                sys.executable,
                "-m",
                "py_compile",
                "tools/verify_base_recovery_and_local_verification_pack.py",
                "tools/run_local_verification_pack.py",
                "tests/python/test_base_recovery_and_local_verification_pack.py",
                "tests/python/test_local_verification_powershell_root.py",
                "tests/python/test_local_verification_pack_registration.py",
            ],
            [
                sys.executable,
                "-m",
                "unittest",
                "tests.python.test_base_recovery_and_local_verification_pack",
                "tests.python.test_local_verification_powershell_root",
                "tests.python.test_local_verification_pack_registration",
            ],
            [
                sys.executable,
                "tools/verify_base_recovery_and_local_verification_pack.py",
            ],
            ["git", "diff", "--check"],
        ]
        for command in commands:
            result = run(command)
            receipt["commands"].append(result)
            if result["exit_code"] != 0:
                receipt["failure"] = f"command failed: {' '.join(command)}"
                break
        else:
            receipt["overall"] = "PASS"

    receipt["finished_at_utc"] = datetime.now(timezone.utc).isoformat()
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(f"receipt={output}")
    print(f"overall={receipt['overall']}")
    return 0 if receipt["overall"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
