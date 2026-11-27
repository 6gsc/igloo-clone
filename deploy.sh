#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
ROOT="$(pwd)"
SITE_ID="80b576fb-5ec8-4da7-85fb-1c3288d94898"
MSG="${1:-Update site from igloo-clone}"

echo "[1/3] Building latest v8 bundle..."
python3 tools/build_plan_v8.py

echo "[2/3] Staging clean deploy-dist/..."
rm -rf deploy-dist
mkdir -p deploy-dist/assets
cp index.html deploy-dist/
cp _redirects deploy-dist/
rsync -a \
  --exclude='*.bak' \
  --exclude='resume-guishaocong.pdf' \
  --exclude='App3D-d68cb154.js' \
  --exclude='App3D-form-a-v6.js' \
  --exclude='App3D-aurora-preview-v6.js' \
  --exclude='App3D-v8.js' \
  --exclude='index-2e130bc1.js' \
  --exclude='index-form-a-v6.js' \
  --exclude='index-aurora-preview-v6.js' \
  --exclude='index-v8.js' \
  assets/ deploy-dist/assets/

echo "[3/3] Deploying deploy-dist/ to Netlify ($SITE_ID)..."
if command -v netlify >/dev/null 2>&1; then
  NETLIFY_CMD="netlify"
else
  NETLIFY_CMD="npx --yes netlify-cli"
fi

$NETLIFY_CMD deploy --prod \
  --dir="$ROOT/deploy-dist" \
  --site="$SITE_ID" \
  --message="$MSG"
