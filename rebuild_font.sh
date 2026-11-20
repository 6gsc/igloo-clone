#!/bin/bash
# 一键重建中文字体图集（改完文案后跑这个）
# 前置: pip3 install fonttools brotly
set -euo pipefail
cd "$(dirname "$0")"
ROOT=$(pwd)

WORK=$(mktemp -d /tmp/msdf-rebuild.XXXXXX)
trap 'rm -rf "$WORK"' EXIT

echo "[1/5] 从 App3D bundle 提取全部文案中的字符..."
python3 - "$ROOT" "$WORK" <<'PYEOF'
import re, sys, json
root, work = sys.argv[1], sys.argv[2]
js = open(f'{root}/assets/App3D-d68cb154.js', encoding='utf-8', errors='ignore').read()
# 抓全部字符串字面量内容(单双引号+反引号)，宁多勿漏
lits = re.findall(r'"([^"]*)"', js) + re.findall(r"'([^']*)'", js) + re.findall(r'`([^`]*)`', js)
text = ' '.join(lits)
ascii_set = ''.join(chr(c) for c in range(0x20, 0x7F)) + '©®´·\u2018\u2019\u201c\u201d€'
chars = sorted(set(ascii_set + text))
open(f'{work}/charset.txt', 'w').write('\n'.join('0x%04X' % ord(c) for c in chars) + '\n')
print(f'  字符总数: {len(chars)} (含 bundle 全部字符串, 图集会稍大)')
PYEOF

echo "[2/5] 合并字体 (拉丁=Plex 等宽 metrics, 中文=Arial)..."
python3 tools/fonts/merge_font.py "$WORK/charset.txt" "$WORK/merged.ttf"

echo "[3/5] 生成 MSDF 图集 (size 42 / pxrange 4, 与原版一致)..."
tools/fonts/msdf-atlas-gen -font "$WORK/merged.ttf" -charset "$WORK/charset.txt" \
  -size 42 -pxrange 4 -type msdf -format png \
  -imageout "$WORK/atlas.png" -json "$WORK/atlas.json" | tail -2

echo "[4/5] 编码 UASTC KTX2 (必须 --lower_left_maps_to_s0t0, 否则乱码!)..."
export DYLD_LIBRARY_PATH="$ROOT/tools/ktx/lib"
tools/ktx/bin/toktx --t2 --encode uastc --uastc 4 --linear --lower_left_maps_to_s0t0 --2d \
  "$WORK/font.ktx2" "$WORK/atlas.png"

echo "[5/5] 替换字体文件..."
cp "$WORK/atlas.json" assets/fonts/IBMPlexMono-Medium.json
cp "$WORK/font.ktx2" assets/fonts/IBMPlexMono-Medium-datatexture.ktx2

echo "完成! 浏览器 Cmd+Shift+R 强制刷新查看。"
