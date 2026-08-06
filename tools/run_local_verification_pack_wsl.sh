#!/usr/bin/env bash
set -euo pipefail

# Required launcher: python3.12
PYTHON_BIN="${PYTHON_BIN:-python3.12}"
OUTPUT_DIRECTORY="${1:-artifacts/local-verification}"
REPOSITORY_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPOSITORY_ROOT"
EXPECTED_HEAD="$(git rev-parse HEAD)"

"$PYTHON_BIN" tools/run_local_verification_pack.py \
  --environment-id wsl2-ubuntu-py312 \
  --expected-head "$EXPECTED_HEAD" \
  --output "$OUTPUT_DIRECTORY/wsl2-ubuntu-py312.json"

echo "WSL2 Ubuntu Python 3.12 local verification receipt is complete."
