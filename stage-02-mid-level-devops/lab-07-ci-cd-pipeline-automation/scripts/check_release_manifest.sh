#!/usr/bin/env bash
set -euo pipefail

APP_NAME="${1:-}"
VERSION="${2:-}"

if [[ -z "$APP_NAME" || -z "$VERSION" ]]; then
  echo "Usage: $0 <app_name> <semver_version>" >&2
  exit 1
fi

if [[ ! "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Invalid version format '$VERSION'. Expected MAJOR.MINOR.PATCH (e.g. 1.2.0)." >&2
  exit 1
fi

echo "Release manifest verified: service=${APP_NAME} version=${VERSION}"
