#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROGRAM="${SCRIPT_DIR}/main.py"
exec "$PROGRAM" "$@"
