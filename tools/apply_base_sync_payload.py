#!/usr/bin/env python3
from __future__ import annotations

import base64
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / ".base-sync"
CHUNKS = [STAGING / f"payload-{index}.txt" for index in range(3)]
EXPECTED_SHA256 = "0fec45c4f8acd191116e810f62eb828f1aebd91c7a801a577d9c6ae4c856709b"
EXPECTED_FILES = 44


def main() -> int:
    encoded = "".join(path.read_text(encoding="ascii") for path in CHUNKS)
    actual_hash = hashlib.sha256(encoded.encode("ascii")).hexdigest()
    if actual_hash != EXPECTED_SHA256:
        raise RuntimeError(f"Base-sync payload hash mismatch: {actual_hash}")

    raw = gzip.decompress(base64.b64decode(encoded))
    payload = json.loads(raw.decode("utf-8"))
    if not isinstance(payload, dict) or len(payload) != EXPECTED_FILES:
        raise RuntimeError(f"Expected {EXPECTED_FILES} files, got {len(payload)}")

    for relative, content in sorted(payload.items()):
        target = (ROOT / relative).resolve()
        if ROOT.resolve() not in target.parents:
            raise RuntimeError(f"Refusing path outside repository: {relative}")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8", newline="\n")

    for path in CHUNKS:
        path.unlink()
    STAGING.rmdir()
    Path(__file__).unlink()
    print(f"Applied {len(payload)} Base-sync source files and removed staging files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
