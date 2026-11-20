#!/bin/bash
# 一键本地运行 igloo.inc 复刻
cd "$(dirname "$0")"
PORT="${1:-8791}"
if lsof -nP -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  echo "port $PORT already in use — open http://127.0.0.1:$PORT/"
else
  echo "serving on http://127.0.0.1:$PORT/"
  python3 -m http.server "$PORT"
fi
