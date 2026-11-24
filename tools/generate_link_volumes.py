#!/usr/bin/env python3
"""Generate custom 64x64x64 3D SDF KTX2 volumes for the bottom entry particle showcase (Plan A).

Produces:
  - assets/images/volumes/cv_doc_64.ktx2   (3D Resume / CV document card with dog-ear fold & sculpted lines)
  - assets/images/volumes/mail_64.ktx2     (3D Envelope with crisp front/back V-flap grooves & seal)
  - assets/images/volumes/github_64.ktx2   (3D Extruded GitHub Octocat emblem)

Each volume matches x_64.ktx2 format:
  VK_FORMAT_R8G8B8A8_UNORM, 64x64x64, KTX_SS_ZSTD supercompression
  RGB = outward unit gradient * 0.5 + 0.5
  A   = clamp(signed_distance * 0.25 + 0.5, 0, 1)   (dist < 0 inside, dist > 0 outside, coords in [-0.5, 0.5]^3)
"""
from __future__ import annotations

import math
import struct
import subprocess
from pathlib import Path

import numpy as np
import zstandard
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
VOL_DIR = ROOT / "assets" / "images" / "volumes"
TEMPLATE_KTX2 = VOL_DIR / "x_64.ktx2"
KTXINFO = ROOT / "tools" / "ktx" / "bin" / "ktxinfo"


def edt_1d_parabola(f: np.ndarray) -> np.ndarray:
    """Felzenszwalb & Huttenlocher 1D squared Euclidean distance transform along axis=-1."""
    n = f.shape[-1]
    grid = np.arange(n, dtype=np.float32)
    # Vectorized over all other axes by evaluating min_q ( (x - q)^2 + f[q] )
    # For N=256 this outer-difference matrix is tiny (256x256 = 256KB) and super fast.
    diff2 = (grid[:, None] - grid[None, :]) ** 2  # (x, q)
    # f has shape (..., N) -> compute min over q
    res = np.min(f[..., None, :] + diff2, axis=-1)
    return res


def exact_2d_sdf(mask: np.ndarray) -> np.ndarray:
    """Compute exact 2D signed distance field in normalized [-0.5, 0.5] units.

    mask: bool ndarray (H, W), True = inside shape.
    Returns float32 ndarray (H, W) with negative inside, positive outside.
    """
    H, W = mask.shape
    INF = np.float32(1e9)
    # Outside distance: distance from ~mask to mask
    f_out = np.where(mask, np.float32(0.0), INF)
    d_out = edt_1d_parabola(edt_1d_parabola(f_out).T).T
    # Inside distance: distance from mask to ~mask
    f_in = np.where(~mask, np.float32(0.0), INF)
    d_in = edt_1d_parabola(edt_1d_parabola(f_in).T).T

    dist_out = np.sqrt(np.maximum(d_out, 0.0))
    dist_in = np.sqrt(np.maximum(d_in, 0.0))
    # Sub-pixel half-voxel boundary shift so mask boundary sits cleanly at 0
    sdf_px = np.where(mask, -(dist_in - 0.5), (dist_out - 0.5))
    return (sdf_px / float(H)).astype(np.float32)


def sample_2d_to_volume_grid(sdf_2d: np.ndarray, N: int = 64) -> np.ndarray:
    """Bilinearly sample (H, W) 2D SDF onto (N_y, N_x) grid matching [-0.5, 0.5]^2."""
    H, W = sdf_2d.shape
    coords = (np.arange(N, dtype=np.float32) + 0.5) / N
    u = coords * W - 0.5
    v = (1.0 - coords) * H - 0.5  # flip Y so image top (+row 0) maps to +Y (top of 3D volume)
    # Actually let's place row 0 at Y = N-1 (+Y), row H-1 at Y = 0 (-Y):
    # Wait: in PIL, row 0 is top. In our 3D grid, arr[z, y, x] has y=63 at +Y top!
    # So y=0 (-Y bottom) should sample v = H - 0.5, y=63 (+Y top) should sample v = 0!
    x0 = np.clip(np.floor(u).astype(np.int32), 0, W - 1)
    x1 = np.clip(x0 + 1, 0, W - 1)
    wx = (u - np.floor(u))[None, :]

    y0 = np.clip(np.floor(v).astype(np.int32), 0, H - 1)
    y1 = np.clip(y0 + 1, 0, H - 1)
    wy = (v - np.floor(v))[:, None]

    c00 = sdf_2d[y0[:, None], x0[None, :]]
    c10 = sdf_2d[y0[:, None], x1[None, :]]
    c01 = sdf_2d[y1[:, None], x0[None, :]]
    c11 = sdf_2d[y1[:, None], x1[None, :]]

    top = c00 * (1.0 - wx) + c10 * wx
    bot = c01 * (1.0 - wx) + c11 * wx
    return (top * (1.0 - wy) + bot * wy).astype(np.float32)


def rounded_extrude_3d(sdf_xy: np.ndarray, half_depth: float, bevel: float = 0.025, N: int = 64) -> np.ndarray:
    """Extrude a (N_y, N_x) 2D SDF into a (N_z, N_y, N_x) 3D SDF with rounded bevel."""
    z = ((np.arange(N, dtype=np.float32) + 0.5) / N - 0.5)[:, None, None]  # (Z, 1, 1)
    d2 = sdf_xy[None, :, :] + bevel  # shrink slightly before rounding back out
    dz = np.abs(z) - (half_depth - bevel)
    outside = np.sqrt(np.maximum(d2, 0.0) ** 2 + np.maximum(dz, 0.0) ** 2)
    inside = np.minimum(np.maximum(d2, dz), 0.0)
    return (outside + inside - bevel).astype(np.float32)


def smin(a: np.ndarray, b: np.ndarray, k: float = 0.02) -> np.ndarray:
    h = np.clip(0.5 + 0.5 * (b - a) / k, 0.0, 1.0)
    return (b * (1.0 - h) + a * h - k * h * (1.0 - h)).astype(np.float32)


def box_sdf_3d(X: np.ndarray, Y: np.ndarray, Z: np.ndarray, cx: float, cy: float, cz: float, hx: float, hy: float, hz: float, r: float = 0.015) -> np.ndarray:
    qx = np.abs(X - cx) - (hx - r)
    qy = np.abs(Y - cy) - (hy - r)
    qz = np.abs(Z - cz) - (hz - r)
    out = np.sqrt(np.maximum(qx, 0.0) ** 2 + np.maximum(qy, 0.0) ** 2 + np.maximum(qz, 0.0) ** 2)
    inn = np.minimum(np.maximum(qx, np.maximum(qy, qz)), 0.0)
    return (out + inn - r).astype(np.float32)


def capsule_sdf_3d(X: np.ndarray, Y: np.ndarray, Z: np.ndarray, ax: float, ay: float, bx: float, by: float, cz: float, radius: float, hz: float) -> np.ndarray:
    """Thickened line segment in XY with rounded Z thickness."""
    px = X - ax
    py = Y - ay
    bax = bx - ax
    bay = by - ay
    denom = bax * bax + bay * bay + 1e-8
    h = np.clip((px * bax + py * bay) / denom, 0.0, 1.0)
    d2 = np.sqrt((px - bax * h) ** 2 + (py - bay * h) ** 2) - radius
    dz = np.abs(Z - cz) - hz
    out = np.sqrt(np.maximum(d2, 0.0) ** 2 + np.maximum(dz, 0.0) ** 2)
    inn = np.minimum(np.maximum(d2, dz), 0.0)
    return (out + inn).astype(np.float32)


def make_grid(N: int = 64):
    c = (np.arange(N, dtype=np.float32) + 0.5) / N - 0.5
    Z, Y, X = np.meshgrid(c, c, c, indexing="ij")
    return X, Y, Z


def build_cv_doc_sdf(N: int = 64) -> np.ndarray:
    """Sculptural 3D Resume / CV document card with dog-ear fold, avatar badge & resume lines."""
    X, Y, Z = make_grid(N)
    # Main rounded document slab: width 0.54 (hx=0.27), height 0.68 (hy=0.34), depth 0.18 (hz=0.09)
    doc = box_sdf_3d(X, Y, Z, 0.0, 0.0, 0.0, 0.27, 0.34, 0.090, r=0.024)

    # Diagonal dog-ear cut at top-right corner: remove X + Y > 0.42
    cut = ((X + Y) - 0.42) / math.sqrt(2.0)
    doc = np.maximum(doc, cut)

    # Raised dog-ear folded triangle INSIDE the cut edge
    fold_in_x = 0.07 - X
    fold_in_y = 0.15 - Y
    fold_z = np.abs(Z) - 0.105
    fold_inner = np.maximum(np.maximum(fold_in_x, fold_in_y), np.maximum(cut, fold_z))
    doc = smin(doc, fold_inner, k=0.008)

    # Front & Back symmetric shallow reliefs (never punch too deep so slab stays solid from all angles)
    az = np.abs(Z)
    avatar_recess = box_sdf_3d(X, Y, az, -0.125, 0.165, 0.092, 0.070, 0.070, 0.022, r=0.012)
    doc = np.maximum(doc, -avatar_recess)
    head_d = np.sqrt((X + 0.125) ** 2 + (Y - 0.182) ** 2 + (az - 0.085) ** 2) - 0.025
    doc = smin(doc, head_d, k=0.007)
    shoulders_d = box_sdf_3d(X, Y, az, -0.125, 0.130, 0.085, 0.040, 0.018, 0.016, r=0.010)
    doc = smin(doc, shoulders_d, k=0.007)

    # Two short header grooves to the right of avatar
    for cy, cx, hx in [(0.195, 0.045, 0.062), (0.140, 0.065, 0.082)]:
        bar = box_sdf_3d(X, Y, az, cx, cy, 0.092, hx, 0.017, 0.020, r=0.008)
        doc = np.maximum(doc, -bar)

    # Three crisp horizontal resume content grooves
    for cy, cx, hx in [(0.025, 0.0, 0.185), (-0.080, 0.0, 0.185), (-0.185, -0.035, 0.150)]:
        groove = box_sdf_3d(X, Y, az, cx, cy, 0.092, hx, 0.021, 0.022, r=0.010)
        doc = np.maximum(doc, -groove)

    return doc.astype(np.float32)


def build_mail_sdf(N: int = 64) -> np.ndarray:
    """Sculptural 3D Envelope with deep crisp V-flap grooves and floating seal."""
    X, Y, Z = make_grid(N)
    # Rounded horizontal envelope body: width 0.68 (hx=0.34), height 0.48 (hy=0.24), depth 0.17 (hz=0.085)
    env = box_sdf_3d(X, Y, Z, 0.0, 0.0, 0.0, 0.34, 0.24, 0.085, r=0.032)

    az = np.abs(Z)
    # Deep crisp V-flap grooves on front & back
    v_left = capsule_sdf_3d(X, Y, az, -0.30, 0.19, 0.0, -0.04, 0.088, 0.024, 0.036)
    v_right = capsule_sdf_3d(X, Y, az, 0.30, 0.19, 0.0, -0.04, 0.088, 0.024, 0.036)
    # Subtle lower diagonal fold lines
    b_left = capsule_sdf_3d(X, Y, az, -0.30, -0.19, -0.10, -0.02, 0.092, 0.017, 0.026)
    b_right = capsule_sdf_3d(X, Y, az, 0.30, -0.19, 0.10, -0.02, 0.092, 0.017, 0.026)

    grooves = np.minimum(np.minimum(v_left, v_right), np.minimum(b_left, b_right))
    env = np.maximum(env, -grooves)

    # Raised circular wax-seal / @ node at the V apex (0, -0.04)
    seal = np.sqrt(X ** 2 + (Y + 0.04) ** 2 + (np.maximum(az - 0.082, 0.0)) ** 2) - 0.052
    env = smin(env, seal, k=0.012)

    return env.astype(np.float32)


def build_github_sdf(N: int = 64) -> np.ndarray:
    """3D Extruded GitHub Invertocat emblem rendered cleanly via high-res 2D mask + exact EDT."""
    S = 256
    img = Image.new("L", (S, S), 0)
    draw = ImageDraw.Draw(img)

    # Official GitHub Invertocat silhouette proportions inside [-0.5, 0.5] -> [0, 256]
    # Note: S=256 so pixel center offset is symmetric around S/2
    def p(nx, ny):
        return (round((nx + 0.5) * (S - 1)), round((0.5 - ny) * (S - 1)))

    def circle(nx, ny, r, fill=255):
        x0, y0 = p(nx - r, ny + r)
        x1, y1 = p(nx + r, ny - r)
        draw.ellipse([x0, y0, x1, y1], fill=fill)

    def ellipse(nx, ny, rx, ry, fill=255):
        x0, y0 = p(nx - rx, ny + ry)
        x1, y1 = p(nx + rx, ny - ry)
        draw.ellipse([x0, y0, x1, y1], fill=fill)

    # Chunky solid Octocat silhouette (head + symmetric ears + body + 4 base lobes + tail)
    ellipse(0.0, 0.08, 0.255, 0.195, 255)
    draw.polygon([p(-0.22, 0.14), p(-0.225, 0.34), p(-0.07, 0.24)], fill=255)
    draw.polygon([p(0.22, 0.14), p(0.225, 0.34), p(0.07, 0.24)], fill=255)
    ellipse(0.0, -0.17, 0.145, 0.165, 255)
    for lx, rx in [(-0.095, 0.042), (-0.032, 0.035), (0.032, 0.035), (0.095, 0.042)]:
        ellipse(lx, -0.30, rx, 0.065, 255)
    tail_pts = [
        p(-0.10, -0.22),
        p(-0.17, -0.22),
        p(-0.23, -0.17),
        p(-0.27, -0.09),
        p(-0.295, -0.04),
    ]
    draw.line(tail_pts, fill=255, width=int(S * 0.058), joint="curve")
    circle(-0.295, -0.04, 0.030, 255)

    mask = np.array(img) > 127
    sdf_2d = exact_2d_sdf(mask)
    sdf_xy = sample_2d_to_volume_grid(sdf_2d, N=N)
    vol = rounded_extrude_3d(sdf_xy, half_depth=0.115, bevel=0.030, N=N)

    # Symmetric Octocat face recess + 2 raised button eyes so front/back read crisply
    X, Y, Z = make_grid(N)
    az = np.abs(Z)
    face_cut = box_sdf_3d(X, Y, az, 0.0, 0.055, 0.115, 0.155, 0.088, 0.045, r=0.040)
    vol = np.maximum(vol, -face_cut)
    # Official GitHub Invertocat silhouette...
    for ex in (-0.065, 0.065):
        eye = np.sqrt(((X - ex) / 1.0) ** 2 + ((Y - 0.062) / 1.45) ** 2 + (np.maximum(az - 0.102, 0.0)) ** 2) - 0.027
        vol = smin(vol, eye, k=0.008)

    return vol.astype(np.float32)


def build_phone_wechat_sdf(N: int = 64) -> np.ndarray:
    """Sculptural 3D WeChat speech bubble with a deeply carved classic phone handset on front & back."""
    S = 256
    img = Image.new("L", (S, S), 0)
    draw = ImageDraw.Draw(img)

    def p(nx, ny):
        return (round((nx + 0.5) * (S - 1)), round((0.5 - ny) * (S - 1)))

    # Plump rounded WeChat-style speech bubble silhouette
    x0, y0 = p(-0.34, 0.30)
    x1, y1 = p(0.34, -0.22)
    draw.ellipse([x0, y0, x1, y1], fill=255)
    # Crisp bottom-left chat bubble tail
    draw.polygon([p(-0.24, -0.11), p(-0.32, -0.32), p(-0.09, -0.18)], fill=255)

    mask = np.array(img) > 127
    sdf_2d = exact_2d_sdf(mask)
    sdf_xy = sample_2d_to_volume_grid(sdf_2d, N=N)
    vol = rounded_extrude_3d(sdf_xy, half_depth=0.105, bevel=0.032, N=N)

    # Sculpt a bold classic diagonal phone handset (recessed cleanly on +Z and -Z faces)
    X, Y, Z = make_grid(N)
    az = np.abs(Z)

    # Curved handset spine in rotated coords (45 deg diagonal from top-left to bottom-right)
    # Rotate (X, Y - 0.04) by +45 deg so handset sits nicely centered in the bubble
    c45 = math.cos(math.pi * 0.25)
    s45 = math.sin(math.pi * 0.25)
    yr = Y - 0.04
    rx = X * c45 - yr * s45
    ry = X * s45 + yr * c45

    # Circular arc segment connecting (-0.12, 0.0) and (+0.12, 0.0) curving upward in ry
    arc_cy = -0.14
    arc_r = 0.185
    # Closest point on circular arc centered at (0, arc_cy) with angle limit
    ang = np.arctan2(rx, ry - arc_cy)
    ang_clamped = np.clip(ang, -0.78, 0.78)
    ax = arc_r * np.sin(ang_clamped)
    ay = arc_cy + arc_r * np.cos(ang_clamped)
    d2_handle = np.sqrt((rx - ax) ** 2 + (ry - ay) ** 2) - 0.030

    # Upper-left earpiece & lower-right mouthpiece pads at ends of the arc
    end_x = arc_r * math.sin(0.78)
    end_y = arc_cy + arc_r * math.cos(0.78)
    # Offset downward along local radial direction for iconic handset cups
    cup_l = np.sqrt(((rx + end_x) / 1.0) ** 2 + ((ry - (end_y - 0.028)) / 1.25) ** 2) - 0.048
    cup_r = np.sqrt(((rx - end_x) / 1.0) ** 2 + ((ry - (end_y - 0.028)) / 1.25) ** 2) - 0.048
    handset_2d = np.minimum(d2_handle, np.minimum(cup_l, cup_r))

    # Carve symmetric recess on front (+Z) & back (-Z) faces
    dz_cut = az - 0.072  # cut down from face 0.105 to 0.072 -> ~2.1 voxels deep
    handset_cut = np.maximum(handset_2d, -dz_cut)
    vol = np.maximum(vol, -handset_cut)

    return vol.astype(np.float32)


def pack_sdf_to_rgba(sdf: np.ndarray) -> np.ndarray:
    """Compute central-difference outward gradient & normalized signed distance, pack to uint8 RGBA."""
    N = sdf.shape[0]
    h = 1.0 / float(N)
    # Central difference gradients (axis 0 = Z, axis 1 = Y, axis 2 = X)
    dz, dy, dx = np.gradient(sdf, h, edge_order=2)
    norm = np.sqrt(dx * dx + dy * dy + dz * dz) + 1e-8
    gx = dx / norm
    gy = dy / norm
    gz = dz / norm

    r = np.clip(np.round((gx * 0.5 + 0.5) * 255.0), 0, 255).astype(np.uint8)
    g = np.clip(np.round((gy * 0.5 + 0.5) * 255.0), 0, 255).astype(np.uint8)
    b = np.clip(np.round((gz * 0.5 + 0.5) * 255.0), 0, 255).astype(np.uint8)
    # Matches wF shader: float dist = (volData.a * 2.0 - 1.0) * 2.0;
    a = np.clip(np.round((sdf * 0.25 + 0.5) * 255.0), 0, 255).astype(np.uint8)
    return np.stack([r, g, b, a], axis=-1)


def write_ktx2_zstd(rgba: np.ndarray, out_path: Path, template_path: Path) -> None:
    """Write a 64x64x64 VK_FORMAT_R8G8B8A8_UNORM Zstd KTX2 reusing DFD/KVD from template_path."""
    tpl = template_path.read_bytes()
    lvl_off, _, lvl_uncomp = struct.unpack("<QQQ", tpl[80:104])
    assert rgba.nbytes == lvl_uncomp == 64 * 64 * 64 * 4

    cctx = zstandard.ZstdCompressor(level=12)
    compressed = cctx.compress(rgba.tobytes())

    header_prefix = bytearray(tpl[:lvl_off])
    # Update Level0.byteLength at offset 88 (8 bytes, little endian uint64)
    struct.pack_into("<Q", header_prefix, 88, len(compressed))
    out_path.write_bytes(bytes(header_prefix) + compressed)


def preview_ascii(name: str, rgba: np.ndarray) -> None:
    inside = rgba[..., 3] < 128
    print(f"=== {name}: inside voxels = {inside.sum()} (alpha min={rgba[...,3].min()}, max={rgba[...,3].max()}) ===")
    sl = inside[32, :, :]
    for row in sl[::-2]:
        print("".join("#" if v else "." for v in row[::2]))


def main() -> None:
    jobs = [
        ("cv_doc_64.ktx2", build_cv_doc_sdf),
        ("mail_64.ktx2", build_mail_sdf),
        ("github_64.ktx2", build_github_sdf),
        ("phone_wechat_64.ktx2", build_phone_wechat_sdf),
    ]
    for fname, builder in jobs:
        sdf = builder(64)
        rgba = pack_sdf_to_rgba(sdf)
        out = VOL_DIR / fname
        write_ktx2_zstd(rgba, out, TEMPLATE_KTX2)
        preview_ascii(fname, rgba)
        info = subprocess.check_output([str(KTXINFO), str(out)], text=True)
        summary = " | ".join(
            l.strip() for l in info.splitlines()
            if any(k in l for k in ("vkFormat", "pixel", "supercompressionScheme", "Level0.byteLength"))
        )
        print(f"  ktxinfo OK: {summary}\n")


if __name__ == "__main__":
    main()
