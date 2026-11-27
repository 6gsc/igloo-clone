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
import os, sys
root, work = sys.argv[1], sys.argv[2]
chars = set(chr(c) for c in range(0x20, 0x7F)) | set('©®´·‘’“”€→↓↑←×—…')
for fn in [
    'assets/App3D-d68cb154.js',
    'assets/App3D-form-a-v6.js',
    'assets/App3D-v8.js',
    'assets/App3D-aurora-preview-v8.js',
]:
    p = os.path.join(root, fn)
    if os.path.exists(p):
        s = open(p, encoding='utf-8', errors='ignore').read()
        for ch in s:
            o = ord(ch)
            if o >= 0x80 and not (0xD800 <= o <= 0xDFFF) and o < 0x10000:
                chars.add(ch)
chars_sorted = sorted(chars)
open(f'{work}/charset.txt', 'w').write('\n'.join('0x%04X' % ord(c) for c in chars_sorted) + '\n')
print(f'  字符总数: {len(chars_sorted)} (全量非ASCII + 可打印ASCII, 零漏字)')
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
