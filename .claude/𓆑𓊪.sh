#!/usr/bin/env bash
# 🪝  SessionStart — 🐈✅🐭
set -e
cd "$(dirname "$0")/.."
if command -v python3 >/dev/null 2>&1; then
  python3 𓊪𓄿𓐍.py || echo "🙀❌"
else
  echo "🐍❓"
fi
