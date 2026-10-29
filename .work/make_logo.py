#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Amber eyes channel logo — two glowing amber lenses joined by a red thread.

Outputs (assets/brand/):
  logo_mark.png      2048x2048 transparent mark
  logo_folder.png    mark on a dark case-file folder (intro / avatar)
  logo_lockup.png    mark + AMBER EYES wordmark + tagline, transparent
  logo_64.png        64 px mark (legibility check)
  watermark.png      96 px mark, 35% opacity
  avatar_800.png     800x800 YouTube avatar (folder version, solid bg)
  preview.png        contact sheet on ink background
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import edition as ED  # noqa: E402  (AE_LANG=en -> English tagline)
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageFont

ROOT = Path(r"D:\TEST\Gax\Audi")
OUT = ROOT / "assets" / "brand"
FONTS = Path(r"C:\Windows\Fonts")

INK = (14, 14, 17)
SLATE = (28, 31, 43)
AMBER = (226, 180, 103)
AMBER_HOT = (255, 214, 140)
RED = (200, 66, 58)
TEXT = (242, 239, 233)
MUTED = (156, 152, 143)

S = 2          # supersampling factor
N = 2048 * S   # working canvas


def glow(layer, radius, strength=1.0):
    """Blurred copy of an RGBA layer, alpha scaled by strength."""
    g = layer.filter(ImageFilter.GaussianBlur(radius))
    if strength != 1.0:
        a = g.getchannel("A").point(lambda v: min(255, int(v * strength)))
        g.putalpha(a)
    return g


def over(base, top):
    return Image.alpha_composite(base, top)


def lens(cx, cy, r):
    """One amber eye: glowing iris (radial gradient + fibres), dark pupil,
    thin spectacle rim, glint."""
    import math
    import numpy as np
    yy, xx = np.mgrid[0:N, 0:N].astype(np.float32)
    dist = np.hypot(xx - cx, yy - cy)
    ang = np.arctan2(yy - cy, xx - cx)
    pr = r * 0.26                         # pupil radius
    ri = r * 0.90                         # iris outer radius (inside the rim)
    t = np.clip((dist - pr) / (ri - pr), 0, 1)
    hot = np.array(AMBER_HOT, np.float32)
    deep = np.array((150, 92, 30), np.float32)
    col = hot[None, None, :] * (1 - t[..., None]) + deep[None, None, :] * t[..., None]
    fib = 0.88 + 0.12 * np.cos(ang * 46 + np.sin(ang * 7) * 2)      # iris fibres
    col = col * fib[..., None]
    alpha = np.where(dist <= ri, 255, 0).astype(np.float32)
    rgba = np.dstack([np.clip(col, 0, 255), alpha]).astype(np.uint8)
    lay = Image.fromarray(rgba, "RGBA")
    d = ImageDraw.Draw(lay)
    # pupil with soft dark ring
    d.ellipse([cx - pr * 1.12, cy - pr * 1.12, cx + pr * 1.12, cy + pr * 1.12], fill=(60, 34, 10, 255))
    d.ellipse([cx - pr, cy - pr, cx + pr, cy + pr], fill=INK + (255,))
    # thin metal rim
    w = int(r * 0.075)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=AMBER + (255,), width=w)
    # glint (upper-left)
    gr = r * 0.58
    d.arc([cx - gr, cy - gr, cx + gr, cy + gr], start=205, end=240,
          fill=(255, 245, 225, 235), width=int(r * 0.055))
    return lay


def bridge(xl, xr, y, h):
    """Short spectacle bridge arching UP between the rims (not a smile)."""
    lay = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    d.arc([xl, y - h, xr, y + h], start=200, end=340, fill=AMBER + (255,), width=int(18 * S))
    return lay


def thread(p0, p1):
    """Taut red evidence thread with a pin at each end."""
    lay = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    d.line([p0, p1], fill=RED + (255,), width=int(12 * S))
    pr = 20 * S
    for (px, py) in (p0, p1):
        d.ellipse([px - pr, py - pr, px + pr, py + pr], fill=RED + (255,))
        d.ellipse([px - pr * 0.5, py - pr * 0.6, px, py - pr * 0.15], fill=(255, 175, 165, 210))
    return lay


def make_mark():
    base = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    r = 300 * S
    cy = N // 2
    gap = 200 * S                      # distance between rims
    cxl = N // 2 - gap // 2 - r
    cxr = N // 2 + gap // 2 + r
    # 1. thread runs diagonally BEHIND the lenses, visible outside and in the gap
    th = thread((cxl - r * 1.30, cy + r * 0.95), (cxr + r * 1.30, cy - r * 0.95))
    base = over(base, glow(th, 12 * S, 0.5))
    base = over(base, th)
    # 2. lenses + bridge with glow
    eyes = over(lens(cxl, cy, r), lens(cxr, cy, r))
    eyes = over(eyes, bridge(cxl + r * 0.80, cxr - r * 0.80, cy - r * 0.25, r * 0.30))
    base = over(base, glow(eyes, 110 * S, 0.70))
    base = over(base, glow(eyes, 30 * S, 0.85))
    base = over(base, eyes)
    return base.resize((2048, 2048), Image.LANCZOS)


def folder_bg(size):
    """Dark case-file folder with a tab."""
    W = H = size
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    m = int(W * 0.06)
    tab_w, tab_h = int(W * 0.34), int(H * 0.07)
    rad = int(W * 0.03)
    d.rounded_rectangle([m, m + tab_h, W - m, H - m], radius=rad, fill=SLATE + (255,))
    d.rounded_rectangle([m, m, m + tab_w, m + tab_h * 2], radius=rad, fill=SLATE + (255,))
    # subtle top edge highlight + red stamp line
    d.line([m + rad, m + tab_h + 3, W - m - rad, m + tab_h + 3], fill=(60, 64, 80, 255), width=4)
    return im


def wordmark(width):
    """AMBER EYES in Georgia caps, +20% tracking, amber underline."""
    size = int(width * 0.085)
    f = ImageFont.truetype(str(FONTS / "georgia.ttf"), size)
    text = "AMBER EYES"
    track = int(size * 0.20)
    widths = [f.getbbox(c)[2] - f.getbbox(c)[0] if c != " " else int(size * 0.32) for c in text]
    total = sum(widths) + track * (len(text) - 1)
    h = int(size * 1.6)
    im = Image.new("RGBA", (total + 8, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x = 0
    for c, w in zip(text, widths):
        if c != " ":
            bx = f.getbbox(c)[0]
            d.text((x - bx, 0), c, font=f, fill=TEXT + (255,))
        x += w + track
    uy = int(size * 1.25)
    d.line([0, uy, total, uy], fill=AMBER + (255,), width=max(2, size // 40))
    return im


def tagline(width):
    font_name = "malgun.ttf" if ED.KO else ("YuGothM.ttc" if ED.JA else "segoeui.ttf")
    f = ImageFont.truetype(str(FONTS / font_name), int(width * 0.03))
    t = ED.TAGLINE
    bb = f.getbbox(t)
    im = Image.new("RGBA", (bb[2] - bb[0] + 4, bb[3] - bb[1] + 12), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((-bb[0], -bb[1]), t, font=f, fill=MUTED + (255,))
    return im


def paste_center(base, im, cy):
    base.alpha_composite(im, ((base.width - im.width) // 2, int(cy - im.height / 2)))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    mark = make_mark()
    mark.save(OUT / "logo_mark.png")
    mark.save(OUT / "logo.png")

    # folder version
    fold = folder_bg(2048)
    m2 = mark.resize((1640, 1640), Image.LANCZOS)
    fold.alpha_composite(m2, ((2048 - 1640) // 2, (2048 - 1640) // 2 + 60))
    fold.save(OUT / "logo_folder.png")

    # lockup: mark + wordmark + tagline (transparent, 2400x1400)
    W, H = 2400, 1400
    lock = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    m3 = mark.resize((1100, 1100), Image.LANCZOS)
    lock.alpha_composite(m3, ((W - 1100) // 2, -120))
    paste_center(lock, wordmark(W), 1010)
    paste_center(lock, tagline(W), 1230)
    lock.save(OUT / "logo_lockup.png")

    # small sizes
    mark.resize((64, 64), Image.LANCZOS).save(OUT / "logo_64.png")
    wm = mark.resize((96, 96), Image.LANCZOS)
    a = wm.getchannel("A").point(lambda v: int(v * 0.35))
    wm.putalpha(a)
    wm.save(OUT / "watermark.png")

    # YouTube avatar: mark only, centred inside the circle-safe area
    av = Image.new("RGBA", (800, 800), INK + (255,))
    vg = Image.new("L", (800, 800), 0)
    ImageDraw.Draw(vg).ellipse([90, 90, 710, 710], fill=70)
    vg = vg.filter(ImageFilter.GaussianBlur(120))
    av.paste(Image.new("RGBA", (800, 800), SLATE + (255,)), (0, 0), vg)
    av.alpha_composite(mark.resize((820, 820), Image.LANCZOS), (-10, -10))
    av.convert("RGB").save(OUT / "avatar_800.png")

    # preview sheet
    pv = Image.new("RGBA", (1920, 1080), INK + (255,))
    pv.alpha_composite(lock.resize((1200, 700), Image.LANCZOS), (40, 190))
    pv.alpha_composite(fold.resize((520, 520), Image.LANCZOS), (1330, 60))
    circ = Image.new("L", (300, 300), 0)
    ImageDraw.Draw(circ).ellipse([0, 0, 299, 299], fill=255)
    avs = av.resize((300, 300), Image.LANCZOS)
    pv.paste(avs, (1440, 620), circ)
    pv.alpha_composite(mark.resize((64, 64), Image.LANCZOS), (1350, 900))
    pv.alpha_composite(mark.resize((32, 32), Image.LANCZOS), (1440, 916))
    d = ImageDraw.Draw(pv)
    f = ImageFont.truetype(str(FONTS / "segoeui.ttf"), 22)
    d.text((1330, 588), "avatar 800 (cắt tròn)", font=f, fill=MUTED)
    d.text((1350, 975), "64 px · 32 px", font=f, fill=MUTED)
    pv.convert("RGB").save(OUT / "preview.png")
    print("done", sorted(p.name for p in OUT.iterdir()))


if __name__ == "__main__":
    main()
