#!/usr/bin/env python3
"""合并 IBM Plex Mono(拉丁) + Arial Unicode(中文) 为单个 MSDF 字体。
拉丁用 Plex 保持原版等宽 metrics(布局不乱)；中文从 Arial 并入并缩放到 Plex 的 unitsPerEm。
用法: python3 merge_font.py <charset.txt> <输出.ttf>
"""
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.misc.transform import Transform
from pathlib import Path

TOOLS = Path(__file__).parent

def main(charset_path, out_path):
    plex = TTFont(TOOLS / 'plex.ttf')
    arial = TTFont(TOOLS / 'font.ttf')
    s = plex['head'].unitsPerEm / arial['head'].unitsPerEm
    ags = arial.getGlyphSet()
    pcmap, acmap = plex.getBestCmap(), arial.getBestCmap()
    cps = [int(l, 16) for l in open(charset_path).read().split() if l.startswith('0x')]
    need = [c for c in cps if c not in pcmap]

    glyf, hmtx = plex['glyf'], plex['hmtx']
    order = list(plex.getGlyphOrder())
    cmap4 = [t for t in plex['cmap'].tables if t.platformID == 3 and t.platEncID == 1][0]

    for cp in need:
        aname = acmap.get(cp)
        if not aname:
            continue
        newname = f'uni{cp:04X}'
        if newname not in order:
            rec = DecomposingRecordingPen(ags)
            trec = TransformPen(rec, Transform().scale(s, s))
            arial['glyf'][aname].draw(trec, arial['glyf'])
            pen = TTGlyphPen(None)
            rec.replay(pen)
            glyf[newname] = pen.glyph()
            aw, lsb = arial['hmtx'][aname]
            hmtx.metrics[newname] = (round(aw * s), round(lsb * s))
            order.append(newname)
        cmap4.cmap[cp] = newname

    glyf.glyphOrder = order
    plex.glyphOrder = order
    plex['maxp'].numGlyphs = len(order)
    plex.save(out_path)
    print(f'并入 {len(need)} 个字形 -> {out_path}')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
