#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-cut the 5 mascots from the 2048 px originals (plan v9, section 5.4).

BiRefNet mask -> keep the main body -> fill interior holes (dark clothing on a
black background must stay opaque) -> soft edge.

Outputs per role in assets/cast/<ROLE>/:
  full.png   2048 px RGBA cutout
  P1.png     840x1000 bust (shown at 420x500), bottom 25% fades to transparent
  P0.png     256 px round head icon (badge, guests line-up, thumbnail)
"""
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw
from rembg import new_session, remove

ROOT = Path(__file__).resolve().parents[1]
CAST = ROOT / "assets" / "cast"
ROLES = {"H": "host_owl", "D": "detective_wolf", "C": "psychologist_fox",
         "N1": "neighbor_sheep", "N2": "observer_cat"}


def clean_mask(m, lum):
    m = (m > 127).astype(np.uint8)
    n, lab, stats, _ = cv2.connectedComponentsWithStats(m, 8)
    if n > 1:                                   # keep the largest component
        big = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
        m = (lab == big).astype(np.uint8)
    # fill interior holes ONLY when they contain artwork (dark clothing);
    # holes that are pure black void (e.g. between a mic arm and the body)
    # stay transparent
    holes = (1 - m).astype(np.uint8)
    n, lab, stats, _ = cv2.connectedComponentsWithStats(holes, 4)
    h, w = m.shape
    for i in range(1, n):
        x, y, bw, bh, area = stats[i]
        if x == 0 or y == 0 or x + bw >= w or y + bh >= h:
            continue                            # touches the border = outside
        if lum[lab == i].mean() > 12:
            m[lab == i] = 1
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    soft = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 1.6)
    return np.clip(soft * 255, 0, 255).astype(np.uint8)


def main():
    sess = new_session("birefnet-general")
    report = []
    for role, name in ROLES.items():
        src = Image.open(CAST / f"{name}_mascot.png").convert("RGB")
        raw = remove(src, session=sess, only_mask=True)
        lum = np.array(src.convert("L"), np.float32)
        mask = clean_mask(np.array(raw), lum)
        out_dir = CAST / role
        out_dir.mkdir(exist_ok=True)
        full = src.copy().convert("RGBA")
        full.putalpha(Image.fromarray(mask))
        full.save(out_dir / "full.png")

        ys, xs = np.where(mask > 128)
        x0, x1, y0 = xs.min(), xs.max(), ys.min()
        bw = x1 - x0
        cw = int(bw * 1.06)
        ch = int(cw / 0.84)
        cx = (x0 + x1) // 2
        top = max(0, y0 - int(ch * 0.03))
        if top + ch > 2048:                     # keep the crop inside the source
            ch = 2048 - top
            cw = int(ch * 0.84)
        left = min(max(0, cx - cw // 2), 2048 - cw)
        crop = full.crop((left, top, left + cw, top + ch))
        p1 = crop.resize((840, 1000), Image.LANCZOS)
        a = np.array(p1.getchannel("A")).astype(np.float32)
        rows = np.where(a.max(axis=1) > 20)[0]
        bot = int(rows.max()) if len(rows) else 999
        fade = np.ones(1000, np.float32)
        f0 = int(bot - 0.28 * bot)
        fade[f0:bot + 1] = np.linspace(1, 0, bot + 1 - f0)
        fade[bot + 1:] = 0
        p1.putalpha(Image.fromarray((a * fade[:, None]).astype(np.uint8)))
        p1.save(out_dir / "P1.png")

        # head icon: x from the top 25% of the figure, circle starts just
        # above the top of the head
        fig_h = ys.max() - y0
        top_rows = mask[y0:y0 + int(fig_h * 0.25)]
        hy, hx = np.where(top_rows > 128)
        hcx = int(np.median(hx))
        side = int(bw * 0.72)
        hcy = y0 + int(side * 0.46)
        head = src.crop((hcx - side // 2, hcy - side // 2, hcx + side // 2, hcy + side // 2))
        head = head.resize((256, 256), Image.LANCZOS).convert("RGBA")
        circ = Image.new("L", (256, 256), 0)
        ImageDraw.Draw(circ).ellipse([2, 2, 253, 253], fill=255)
        head.putalpha(circ)
        head.save(out_dir / "P0.png")

        core = mask[y0 + int((ys.max() - y0) * 0.25): y0 + int((ys.max() - y0) * 0.75), x0 + bw // 4: x1 - bw // 4]
        report.append(f"{role} {name}: alpha vùng thân TB {core.mean():.0f}/255, "
                      f"điểm < 200 trong thân {100 * (core < 200).mean():.1f}%")
    print("\n".join(report))


if __name__ == "__main__":
    main()
