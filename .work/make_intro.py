#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Amber eyes channel intro — 22.41 s, picture only (plan v9, section 5.11).

Timeline (music: assets/bgm/bgm_music_box.mp3, 22.41 s):
  I-01  0.00– 4.00  red thread draws 0–1.4 s, amber eyes flare at 1.5 s,
                    AMBER EYES types 2.2–3.4 s, tagline 3.4 s
  I-02  4.00–12.25  disclaimer card A
  I-03 12.25–20.50  disclaimer card B; 5 role-colour rings light from 18.0 s
  I-04 20.50–22.41  fade to black

Outputs:
  assets/brand/intro_kenh.mov     picture only (reused by every episode)
  assets/brand/intro_preview.mp4  same picture + music box, for review
"""
import math
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).parent))
import make_logo as ml  # noqa: E402
import edition as ED  # noqa: E402  (AE_LANG=en -> intro_kenh_EN.mov)

ROOT = Path(r"D:\TEST\Gax\Audi")
BRAND = ROOT / "assets" / "brand"
FFMPEG = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
MUSIC = ROOT / "assets" / "bgm" / "bgm_music_box.mp3"
FONTS = Path(r"C:\Windows\Fonts")

W, H, FPS = 1920, 1080, 30
DUR = 22.41
NFR = int(round(DUR * FPS))

INK, PAPER, PAPER_INK = ml.INK, (230, 222, 208), (28, 27, 31)
RED, AMBER, TEXT, MUTED = ml.RED, ml.AMBER, ml.TEXT, ml.MUTED
ROLE = [(226, 180, 103), (134, 169, 204), (169, 155, 214), (217, 185, 155), (110, 140, 160)]

CARD_A, CARD_B = ED.CARD_A, ED.CARD_B
A_T0, A_T1, A_LINES = 4.00, 12.25, (4.30, 5.70, 7.10)
B_T0, B_T1, B_LINES = 12.25, 20.50, (12.55, 13.95, 15.35)
RINGS_T = 18.0


def ease(x):
    x = min(1.0, max(0.0, x))
    return x * x * (3 - 2 * x)


def with_alpha(im, k):
    if k >= 0.999:
        return im
    out = im.copy()
    out.putalpha(im.getchannel("A").point(lambda v: int(v * max(0.0, k))))
    return out


# ---------------------------------------------------------------- logo layers
def build_logo_layers():
    """Thread, eye core and eye glow as separate 2048 px layers."""
    N, S = ml.N, ml.S
    r, cy, gap = 300 * S, N // 2, 200 * S
    cxl, cxr = N // 2 - gap // 2 - r, N // 2 + gap // 2 + r
    th = ml.thread((cxl - r * 1.30, cy + r * 0.95), (cxr + r * 1.30, cy - r * 0.95))
    th = ml.over(ml.glow(th, 12 * S, 0.5), th)
    eyes = ml.over(ml.lens(cxl, cy, r), ml.lens(cxr, cy, r))
    eyes = ml.over(eyes, ml.bridge(cxl + r * 0.80, cxr - r * 0.80, cy - r * 0.25, r * 0.30))
    gl = ml.over(ml.glow(eyes, 110 * S, 0.70), ml.glow(eyes, 30 * S, 0.85))
    down = lambda im: im.resize((2048, 2048), Image.LANCZOS)
    # thread x-extent (in 2048 space) for the draw-on reveal
    tx0, tx1 = (cxl - r * 1.30) / S - 30, (cxr + r * 1.30) / S + 30
    return down(th), down(eyes), down(gl), (tx0, tx1)


def wordmark_layer():
    return ml.wordmark(1400), ml.tagline(1400)


# ---------------------------------------------------------------- cards
def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


F_LABEL = font("consola.ttf", 34)

# Hình học thẻ cảnh báo. Mặc định = bản cũ (1 gạch đầu dòng = 1 dòng, cách nhau 112 px).
# Bản EN Tập 02 dùng card_geom trong edition.py: thẻ rộng hơn, chữ nhỏ hơn, mỗi gạch đầu dòng
# tự xuống dòng khi dài (chuỗi CHU_CO_DINH_EN.md §2 viết đầy đủ, không rút gọn).
GEOM = ED.EP.get("card_geom") or {}
CW, CH = GEOM.get("cw", 1400), GEOM.get("ch", 640)
F_SIZE = GEOM.get("size", 48)
LINE_H = GEOM.get("line_h", 72)
LINE_GAP = GEOM.get("gap", 40)
LINE_Y0 = GEOM.get("y0", 190)
TEXT_W = CW - 180                        # lề trái/phải 90 px
F_BODY = font("malgun.ttf", F_SIZE) if ED.KO else (font("YuGothM.ttc", F_SIZE) if ED.JA else font("segoeui.ttf", F_SIZE))
F_BOLD = font("malgunbd.ttf", F_SIZE) if ED.KO else (font("YuGothB.ttc", F_SIZE) if ED.JA else font("segoeuib.ttf", F_SIZE))


def char_bounds():
    """Right edge (px) of each character in ml.wordmark(1400) — for typing."""
    size = int(1400 * 0.085)
    f = ImageFont.truetype(str(FONTS / "georgia.ttf"), size)
    text = "AMBER EYES"
    track = int(size * 0.20)
    xs, x = [], 0
    for c in text:
        w = f.getbbox(c)[2] - f.getbbox(c)[0] if c != " " else int(size * 0.32)
        x += w
        xs.append(x + track // 2)
        x += track
    return xs


def line_image(segs):
    """segs = [(text, bold), ...] -> danh sách ảnh dòng (tự xuống dòng nếu quá rộng)."""
    words = []                      # (mảnh chữ, đậm, có khoảng trắng đầu không)
    for t, b in segs:
        for k, p in enumerate(re.split(r"(\s+)", t)):
            if p:
                words.append((p, b))
    lines, cur, cur_w = [], [], 0.0
    for p, b in words:
        f = F_BOLD if b else F_BODY
        w = f.getlength(p)
        if cur and cur_w + w > TEXT_W and p.strip():
            lines.append(cur)
            cur, cur_w = [], 0.0
            if not p.strip():
                continue
        cur.append((p, b))
        cur_w += w
    if cur:
        lines.append(cur)

    imgs = []
    for ln in lines:
        widths = [(F_BOLD if b else F_BODY).getlength(t) for t, b in ln]
        im = Image.new("RGBA", (int(sum(widths)) + 8, LINE_H), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        x = 0
        for (t, b), w in zip(ln, widths):
            d.text((x, 4), t, font=F_BOLD if b else F_BODY, fill=PAPER_INK + (255,))
            x += w
        imgs.append(im)
    return imgs


def card_base(label, mark_small):
    cw, ch = CW, CH
    rng = np.random.default_rng(7)
    tex = rng.normal(0, 5, (ch, cw, 1)).repeat(3, axis=2)
    paper = np.clip(np.array(PAPER, np.float32)[None, None, :] + tex, 0, 255).astype(np.uint8)
    card = Image.fromarray(paper, "RGB").convert("RGBA")
    d = ImageDraw.Draw(card)
    d.rectangle([0, 0, cw - 1, ch - 1], outline=(196, 186, 168, 255), width=3)
    d.text((90, 66), label, font=F_LABEL, fill=RED + (255,))
    d.line([90, 120, 90 + 130, 120], fill=RED + (255,), width=4)
    card.alpha_composite(mark_small, (cw - mark_small.width - 56, 40))
    # soft drop shadow
    sh = Image.new("RGBA", (cw + 80, ch + 80), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle([40, 52, cw + 40, ch + 52], fill=(0, 0, 0, 150))
    from PIL import ImageFilter
    sh = sh.filter(ImageFilter.GaussianBlur(22))
    sh.alpha_composite(card, (40, 40))
    return sh.rotate(-0.8, resample=Image.BICUBIC, expand=True)


def rings_layer(k_list):
    """5 small role-colour rings; k_list = brightness 0..1 per ring."""
    im = Image.new("RGBA", (5 * 70, 70), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for i, (c, k) in enumerate(zip(ROLE, k_list)):
        cx = 35 + i * 70
        a = int(60 + 195 * k)
        d.ellipse([cx - 20, 15, cx + 20, 55], outline=c + (a,), width=5)
        d.ellipse([cx - 8, 27, cx + 8, 43], fill=c + (int(40 + 120 * k),))
    return im


# ---------------------------------------------------------------- frames
def main():
    th, eyes, gl, (tx0, tx1) = build_logo_layers()
    wm, tg = wordmark_layer()
    mark_small = ml.make_mark().resize((84, 84), Image.LANCZOS)
    card_a = card_base(CARD_A[0], mark_small)
    card_b = card_base(CARD_B[0], mark_small)
    lines_a = [line_image(s) for s in CARD_A[1]]
    lines_b = [line_image(s) for s in CARD_B[1]]
    LOGO = 940                                   # on-screen mark size at zoom 1
    th_s, eyes_s, gl_s = (x.resize((LOGO, LOGO), Image.LANCZOS) for x in (th, eyes, gl))

    # wordmark typing: reveal whole characters only
    bounds = char_bounds()
    n_chars = len(bounds)
    WM_Y = 700
    TG_Y = WM_Y + wm.height + 18

    cmd = [str(FFMPEG), "-y", "-hide_banner", "-loglevel", "error",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-vf", "noise=alls=3:allf=t+u,vignette=PI/5,format=yuv420p",
           "-c:v", "libopenh264", "-b:v", "8M", "-maxrate", "12M", "-bufsize", "16M",
           "-r", str(FPS), str(ED.INTRO_MOV)]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    for fi in range(NFR):
        t = fi / FPS
        fr = Image.new("RGBA", (W, H), INK + (255,))

        # ---- I-01 logo (0–4.0, fades out 3.65–4.0)
        if t < 4.0:
            k_out = 1 - ease((t - 3.65) / 0.35)
            z = 1.00 + 0.04 * (t / 4.0)
            size = int(LOGO * z)
            cx, cy = W // 2, int(360 - 10 * (t / 4.0))
            # thread draw-on 0–1.4 s (reveal left -> right)
            prog = ease(t / 1.4)
            thr = th_s.copy()
            cut = int(((tx0 + (tx1 - tx0) * prog) / 2048) * LOGO)
            if cut < LOGO:
                a = np.array(thr.getchannel("A"))
                a[:, max(0, cut):] = 0
                thr.putalpha(Image.fromarray(a))
            # eyes: faint from 0.5 s, flare at 1.5 s, settle by 2.2 s
            base_k = 0.18 * ease((t - 0.5) / 0.6)
            flare = ease((t - 1.35) / 0.15)
            eyes_k = base_k + (1 - base_k) * flare
            glow_k = eyes_k * (1 + 0.6 * math.exp(-max(0.0, t - 1.5) * 4) * (t >= 1.5))
            layer = Image.new("RGBA", (LOGO, LOGO), (0, 0, 0, 0))
            layer.alpha_composite(with_alpha(gl_s, min(1.0, glow_k)))
            if glow_k > 1.0:                      # extra bloom on the flare
                layer.alpha_composite(with_alpha(gl_s, glow_k - 1.0))
            layer.alpha_composite(with_alpha(thr, 1.0))
            layer.alpha_composite(with_alpha(eyes_s, eyes_k))
            layer = layer.resize((size, size), Image.LANCZOS) if size != LOGO else layer
            fr.alpha_composite(with_alpha(layer, k_out), (cx - size // 2, cy - size // 2))
            # wordmark typing 2.2–3.4 s
            if t >= 2.2:
                chars = min(n_chars, int((t - 2.2) / 1.2 * n_chars) + 1)
                vis = wm.copy()
                a = np.array(vis.getchannel("A"))
                if chars < n_chars:
                    a[:, bounds[chars - 1]:] = 0
                # underline only after typing finished
                if t < 3.4:
                    a[int(vis.height * 0.72):, :] = 0
                vis.putalpha(Image.fromarray(a))
                fr.alpha_composite(with_alpha(vis, k_out), ((W - wm.width) // 2, WM_Y))
            if t >= 3.4:
                k = ease((t - 3.4) / 0.4) * k_out
                fr.alpha_composite(with_alpha(tg, k), ((W - tg.width) // 2, TG_Y))

        # ---- cards
        for (T0, T1, LN, card, lines, has_rings) in (
                (A_T0, A_T1, A_LINES, card_a, lines_a, False),
                (B_T0, B_T1, B_LINES, card_b, lines_b, True)):
            if T0 <= t < (T1 + 0.35 if not has_rings else 22.41):
                k_in = ease((t - T0) / 0.35)
                if has_rings:
                    k_out = 1 - ease((t - 20.5) / 1.1)
                else:
                    k_out = 1 - ease((t - T1) / 0.35)
                k = k_in * k_out
                if k <= 0:
                    continue
                c = card.copy()
                ox, oy = (c.width - CW) // 2, (c.height - CH) // 2
                y = LINE_Y0
                for i, (lt, lis) in enumerate(zip(LN, lines)):
                    for j, li in enumerate(lis):
                        tl = lt + j * 0.16
                        if t >= tl:
                            kk = ease((t - tl) / 0.35)
                            dy = int(24 * (1 - kk))
                            c.alpha_composite(with_alpha(li, kk),
                                              (ox + 90, oy + y + j * LINE_H + dy))
                    y += len(lis) * LINE_H + LINE_GAP
                if has_rings and t >= RINGS_T - 0.3:
                    ks = [ease((t - RINGS_T - i * 0.22) / 0.3) for i in range(5)]
                    rl = rings_layer(ks)
                    c.alpha_composite(with_alpha(rl, ease((t - RINGS_T + 0.3) / 0.3)),
                                      (ox + 90, oy + CH - 110))
                fr.alpha_composite(with_alpha(c, k), ((W - c.width) // 2, (H - c.height) // 2))

        p.stdin.write(fr.convert("RGB").tobytes())
        if fi % 90 == 0:
            print(f"  frame {fi}/{NFR}", flush=True)
    p.stdin.close()
    if p.wait() != 0:
        raise SystemExit("ffmpeg failed")

    # review copy with the music box
    subprocess.run([str(FFMPEG), "-y", "-hide_banner", "-loglevel", "error",
                    "-i", str(ED.INTRO_MOV), "-i", str(MUSIC),
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-t", f"{DUR}", "-movflags", "+faststart",
                    str(BRAND / f"intro_preview{ED.SUF}.mp4")], check=True)
    print("done")


if __name__ == "__main__":
    main()
