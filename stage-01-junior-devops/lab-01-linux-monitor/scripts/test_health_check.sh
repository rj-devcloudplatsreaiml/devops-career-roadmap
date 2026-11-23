#!/usr/bin/env bash
set -euo pipefail

./scripts/health_check.sh 99 >/dev/null
echo "PASS: Normal threshold check succeeded."

set +e
./scripts/health_check.sh 0 >/dev/null
RC=$?
set -e

if [ "$RC" -eq 1 ]; then
  echo "PASS: Threshold alert triggered as expected."
else
  echo "FAIL: Expected exit code 1, got $RC" >&2
  exit 1
fi
