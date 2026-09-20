#!/bin/bash
# 測試用的小腳本，給 shellcheck 一點東西看。
set -euo pipefail

CONFIG="${1:-config.json}"

if [ ! -f "$CONFIG" ]; then
  echo "找不到設定檔：$CONFIG" >&2
fi

python3 app.py
