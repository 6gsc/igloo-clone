#!/usr/bin/env python3
"""重新生成左上角 logo 纹理（白字位图 + 满铺平铺单元 + 原版容器移植）。
用法: python3 tools/fonts/make_logo.py "Gui"

关键: 文字必须铺满 128px 宽——小视口下纹理会被水平平铺采样，
居中留白版会在手机宽度窗口里平铺出错位重叠。
"""
import sys, struct, zstandard as zstd
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

TOOLS = Path(__file__).parent
ROOT = TOOLS.parent.parent

def main(text):
    n = max(len(text), 1)
    cell = 128 / n
    font = ImageFont.truetype(str(TOOLS / 'plex.ttf'), 36)
    img = Image.new('L', (128, 128), 0)
    d = ImageDraw.Draw(img)
    for i, ch in enumerate(text):
        bbox = d.textbbox((0, 0), ch, font=font)
        w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
        cx = i*cell + (cell-w)/2 - bbox[0]
        cy = (128-h)/2 - bbox[1]
        d.text((cx, cy), ch, font=font, fill=255)

    gray = np.array(img)
    rgba = np.concatenate([np.stack([gray]*3, axis=2),
                           np.zeros((128,128,1), dtype=np.uint8)], axis=2)

    cache = TOOLS / 'logo_container.ktx2'
    if not cache.exists():
        import urllib.request
        req = urllib.request.Request(
            'https://www.igloo.inc/assets/images/ui/logo-datatexture.ktx2',
            headers={'User-Agent': 'Mozilla/5.0'})
        cache.write_bytes(urllib.request.urlopen(req).read())
    orig = cache.read_bytes()

    comp = zstd.ZstdCompressor(level=5).compress(rgba.tobytes())
    new = bytearray(orig[:220])
    struct.pack_into('<I', new, 88, len(comp))
    new += comp
    out = ROOT / 'assets/images/ui/logo-custom-datatexture.ktx2'
    out.write_bytes(bytes(new))
    print(f'生成 {out} (文本: {text}, {len(new)} 字节) — 记得同步改 bundle 里的引用文件名')

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'Gui')
