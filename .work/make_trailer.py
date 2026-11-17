#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng HÌNH trailer Concept A "Sợi chỉ đỏ" — 50,0 s, 1920×1080@30.

Dùng: py -3 .work/make_trailer.py
Output: .work/trailer_a/picture.mp4

Nguyên tắc:
- Tái dùng nguyên xi `make_intro` (logo layers, wordmark, thẻ giấy, 5 vòng vai) ⇒ đồng bộ thương hiệu.
- Chữ trên màn hình do Pillow vẽ (AI KHÔNG vẽ chữ).
- Ảnh nền lấy từ assets/bg/ có sẵn ⇒ 0 credit AI.
"""
import math
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).parent))
import make_intro as MI  # noqa: E402
import make_logo as ml  # noqa: E402
import edition as ED  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work" / "trailer_a"
FFMPEG = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FONTS = Path(r"C:\Windows\Fonts")
BG = ROOT / "assets" / "bg"
CAST = ROOT / "assets" / "cast"

SUF = "" if not ED.EN else "_EN"      # bản tiếng Anh dùng hậu tố _EN
OUT_PICTURE = WORK / f"picture{SUF}.mp4"

# Lớp video động: clip Hailuo-2.3 (first-frame từ chính nền của kênh) thay cho ảnh tĩnh.
CLIP_DIR = WORK / "h23_norm"
CLIP_FOR_BEAT = {"hook": "hook", "board": "board", "inv": "interrogation", "all": "corridor"}

W, H, FPS = 1920, 1080, 30
DUR = 50.0
NFR = int(round(DUR * FPS))

INK = ml.INK
AMBER = ml.AMBER
AMBER_HOT = ml.AMBER_HOT
RED = ml.RED
TEXT = ml.TEXT
MUTED = ml.MUTED

# ---------------------------------------------------------------- nhịp
BEATS = [
    dict(key="hook", t0=0.00, t1=4.60, bg="void", zoom=(1.05, 1.13), pan=(0.50, 0.50)),
    dict(key="board", t0=4.60, t1=10.60, bg="pinboard", zoom=(1.05, 1.15), pan=(0.35, 0.55)),
    dict(key="host", t0=10.60, t1=16.60, bg="podcast_desk", zoom=(1.05, 1.13), pan=(0.62, 0.42)),
    dict(key="inv", t0=16.60, t1=22.60, bg="interrogation", zoom=(1.08, 1.16), pan=(0.55, 0.40)),
    dict(key="psy", t0=22.60, t1=28.60, bg="brain_desk", zoom=(1.06, 1.14), pan=(0.45, 0.58)),
    dict(key="all", t0=28.60, t1=34.60, bg="corridor", zoom=(1.05, 1.13), pan=(0.55, 0.45)),
    dict(key="card", t0=34.60, t1=38.60, bg="void", zoom=(1.02, 1.04), pan=(0.50, 0.50)),
    dict(key="end", t0=38.60, t1=46.40, bg="void", zoom=(1.02, 1.06), pan=(0.50, 0.50)),
    dict(key="out", t0=46.40, t1=50.00, bg="void", zoom=(1.04, 1.04), pan=(0.50, 0.50)),
]
XFADE = 0.55  # giây chuyển cảnh

LABELS = {
    "host": ("DẪN CHUYỆN", AMBER),
    "inv": ("ĐIỀU TRA VIÊN", (134, 169, 204)),
    "psy": ("CHUYÊN GIA TÂM LÝ", (169, 155, 214)),
}
LABELS_EN = {
    "host": ("HOST", AMBER),
    "inv": ("INVESTIGATOR", (134, 169, 204)),
    "psy": ("PSYCHOLOGIST", (169, 155, 214)),
}
STATS = "29 HỒ SƠ   ·   5 VAI CHÍNH   ·   4 NGÔN NGỮ"
STATS_EN = "29 CASE FILES   ·   5 CHARACTERS   ·   4 LANGUAGES"
MASCOT = {"host": "H", "inv": "D", "psy": "C"}

_cache = {}


def ease(x):
    x = min(1.0, max(0.0, x))
    return x * x * (3 - 2 * x)


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def beat_at(t):
    for b in BEATS:
        if b["t0"] <= t < b["t1"]:
            return b
    return BEATS[-1]


def bg_big(name):
    """Nền phóng to 1,18× (đủ để Ken Burns không méo)."""
    if name not in _cache:
        im = Image.open(BG / f"{name}.png").convert("RGB")
        sc = max(W * 1.18 / im.width, H * 1.18 / im.height)
        _cache[("big", name)] = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    return _cache[("big", name)]


def kb(b, t):
    """Khung nền của nhịp b tại thời điểm t (ken burns: zoom + trôi ngang)."""
    k = ease((t - b["t0"]) / max(0.1, b["t1"] - b["t0"]))
    z = b["zoom"][0] + (b["zoom"][1] - b["zoom"][0]) * k
    px = b["pan"][0] + (b["pan"][1] - b["pan"][0]) * k
    big = bg_big(b["bg"])
    ww, wh = int(W * z), int(H * z)
    mx, my = max(0, big.width - ww), max(0, big.height - wh)
    x0 = int(mx * px)
    y0 = int(my * 0.45)
    x0 = max(0, min(x0, big.width - ww))
    y0 = max(0, min(y0, big.height - wh))
    return big.crop((x0, y0, x0 + ww, y0 + wh)).resize((W, H), Image.BILINEAR)


def bg_at(t):
    """Nền tại thời điểm t, có chuyển cảnh chồng ảnh ở ranh giới nhịp."""
    b = beat_at(t)
    nxt = None
    for nb in BEATS:
        if nb["t0"] > b["t0"]:
            nxt = nb
            break
    if nxt and t >= nxt["t0"] - XFADE:
        k = ease((t - (nxt["t0"] - XFADE)) / XFADE)
        a = kb(b, t).convert("RGBA")
        c = kb(nxt, t).convert("RGBA")
        return Image.blend(a, c, k)
    return kb(b, t).convert("RGBA")


def bottom_scrim():
    """Lớp tối mờ phía dưới ⇒ chữ nhãn vai luôn đủ tương phản (H9)."""
    top = H - 430
    g = np.zeros((430, W), np.float32)
    for y in range(430):
        g[y] = 180 * ease(y / 429)
    a = np.dstack([np.zeros((430, W, 3), np.float32), g[:, :, None]])
    return Image.fromarray(a.astype(np.uint8), "RGBA"), top


def letterspaced(d, xy, text, f, fill, spacing=6, anchor_center=None):
    """Vẽ chữ có giãn cách (dùng cho nhãn vai)."""
    widths = [f.getlength(c) for c in text]
    total = sum(widths) + spacing * (len(text) - 1)
    x, y = xy
    if anchor_center:
        x -= total / 2
    for c, w in zip(text, widths):
        d.text((x, y), c, font=f, fill=fill)
        x += w + spacing


def label_layer(text, color):
    """Nhãn vai: gạch mảnh + chữ in hoa, canh trái dưới."""
    im = Image.new("RGBA", (1100, 190), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 20, 96, 26], fill=color + (255,))
    f = font("segoeuib.ttf", 46)
    letterspaced(d, (0, 52), text, f, color + (255,), spacing=9)
    return im


def mascot_cutout(key, height):
    if ("cast", key, height) not in _cache:
        im = Image.open(CAST / key / "P1.png").convert("RGBA")
        r = height / im.height
        im = im.resize((round(im.width * r), height), Image.LANCZOS)
        _cache[("cast", key, height)] = im
    return _cache[("cast", key, height)]


def fade_alpha(im, k):
    if k >= 0.999:
        return im
    out = im.copy()
    out.putalpha(im.getchannel("A").point(lambda v: int(v * max(0.0, k))))
    return out


class ClipPlayer:
    """Đọc khung hình tuần tự từ một clip mp4 đã chuẩn hoá 1920x1080@30."""

    def __init__(self, path):
        self.cmd = [str(FFMPEG), "-v", "error", "-i", str(path),
                    "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-"]
        self.p = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, bufsize=W * H * 3 * 4)
        self.n = 0
        self.size = W * H * 3

    def next(self):
        data = self.p.stdout.read(self.size)
        if data is None or len(data) < self.size:
            return None
        self.n += 1
        return Image.frombytes("RGB", (W, H), data)

    def close(self):
        try:
            self.p.kill()
        except Exception:  # noqa: BLE001
            pass


# ---------------------------------------------------------------- các lớp riêng
def hook_layer(t):
    """0–4,6 s: sợi chỉ đỏ vẽ tay + đôi mắt hổ phách (tái dùng make_intro)."""
    if ("hook",) not in _cache:
        th, eyes, gl, (tx0, tx1) = MI.build_logo_layers()
        size = 900
        _cache[("hook",)] = (th.resize((size, size), Image.LANCZOS),
                             eyes.resize((size, size), Image.LANCZOS),
                             gl.resize((size, size), Image.LANCZOS), tx0, tx1, size)
    th_s, eyes_s, gl_s, tx0, tx1, size = _cache[("hook",)]
    layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    prog = ease(t / 1.4)
    thr = th_s.copy()
    cut = int(((tx0 + (tx1 - tx0) * prog) / 2048) * size)
    if cut < size:
        a = np.array(thr.getchannel("A"))
        a[:, max(0, cut):] = 0
        thr.putalpha(Image.fromarray(a))
    base_k = 0.18 * ease((t - 0.5) / 0.6)
    flare = ease((t - 1.35) / 0.15)
    eyes_k = base_k + (1 - base_k) * flare
    glow_k = eyes_k * (1 + 0.6 * math.exp(-max(0.0, t - 1.5) * 4) * (t >= 1.5))
    layer.alpha_composite(fade_alpha(gl_s, min(1.0, glow_k)))
    if glow_k > 1.0:
        layer.alpha_composite(fade_alpha(gl_s, glow_k - 1.0))
    layer.alpha_composite(thr)
    layer.alpha_composite(fade_alpha(eyes_s, eyes_k))
    return layer


def board_tags(t):
    """5 thẻ giấy 'HỒ SƠ' lần lượt xuất hiện trên bảng ghim."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    spots = [(196, 168), (392, 262), (250, 402), (452, 470), (318, 566)]
    tags = ["01", "07", "12", "19", "29"]
    for i, ((cx, cy), tg) in enumerate(zip(spots, tags)):
        t0 = 5.6 + i * 1.0
        if t < t0:
            continue
        k = ease((t - t0) / 0.45)
        s = 1 + (1 - k) * 0.25
        w, h = int(132 * s), int(88 * s)
        x, y = cx - w // 2, cy - h // 2
        paper = Image.new("RGBA", (w, h), (226, 218, 200, 255))
        pd = ImageDraw.Draw(paper)
        pd.rectangle([0, 0, w - 1, h - 1], outline=(196, 186, 168, 255), width=2)
        f = font("consola.ttf", int(34 * s))
        tw = pd.textlength(tg, font=f)
        pd.text(((w - tw) / 2, (h - 34 * s) / 2), tg, font=f, fill=(28, 27, 31, 255))
        paper = paper.rotate(-6 + i * 3, resample=Image.BICUBIC, expand=True)
        sh = Image.new("RGBA", paper.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).rectangle([4, 6, paper.width - 4, paper.height - 2], fill=(0, 0, 0, 120))
        sh = sh.filter(ImageFilter.GaussianBlur(8))
        sh = fade_alpha(sh, k)
        layer.alpha_composite(sh, (x - (paper.width - w) // 2, y - (paper.height - h) // 2))
        layer.alpha_composite(fade_alpha(paper, k), (x - (paper.width - w) // 2, y - (paper.height - h) // 2))
    return layer


def card_layer(t):
    """Thẻ giấy miễn trừ (cùng bản trong bumper)."""
    if ("card",) not in _cache:
        mark_small = ml.make_mark().resize((84, 84), Image.LANCZOS)
        base = MI.card_base(MI.CARD_A[0], mark_small)
        lines = [MI.line_image(s) for s in MI.CARD_A[1]]
        _cache[("card",)] = (base, lines)
    base, lines = _cache[("card",)]
    CW, CH = MI.CW, MI.CH
    ox, oy = (base.width - CW) // 2, (base.height - CH) // 2
    c = base.copy()
    y = MI.LINE_Y0
    for i, (lt, lis) in enumerate(zip((4.30, 5.70, 7.10), lines)):
        for j, li in enumerate(lis):
            tl = lt + j * 0.16
            if t >= tl:
                kk = ease((t - tl) / 0.35)
                dy = int(24 * (1 - kk))
                c.alpha_composite(fade_alpha(li, kk), (ox + 90, oy + y + j * MI.LINE_H + dy))
        y += len(lis) * MI.LINE_H + MI.LINE_GAP
    return c


def endcard_layer(k):
    """End card: logo + wordmark + tagline + số liệu."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if ("endcard",) not in _cache:
        wm, tg = MI.wordmark_layer()
        mark = ml.make_mark().resize((400, 400), Image.LANCZOS)
        _cache[("endcard",)] = (wm, tg, mark)
    wm, tg, mark = _cache[("endcard",)]
    d = ImageDraw.Draw(im)
    im.alpha_composite(fade_alpha(mark, k), ((W - mark.width) // 2, 230))
    im.alpha_composite(fade_alpha(wm, k), ((W - wm.width) // 2, 630))
    im.alpha_composite(fade_alpha(tg, k), ((W - tg.width) // 2, 630 + wm.height + 26))
    f = font("seguisb.ttf", 34)
    stats = STATS_EN if ED.EN else STATS
    tw = d.textlength(stats, font=f)
    d.text(((W - tw) / 2, 900), stats, font=f, fill=MUTED + (int(255 * k),))
    d.rectangle([(W - tw) / 2 - 40, 880, (W + tw) / 2 + 40, 882], fill=RED + (int(180 * k),))
    return im


def watermark_layer(k):
    """End slate: wordmark + tagline ở góc trái dưới, tồn tại tới hết video."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if ("wm420",) not in _cache:
        _cache[("wm420",)] = (ml.wordmark(520), MI.wordmark_layer()[1].resize((980, 42), Image.LANCZOS))
    wm, tg = _cache[("wm420",)]
    im.alpha_composite(fade_alpha(wm, k), (96, H - 230))
    im.alpha_composite(fade_alpha(tg, k * 0.85), (98, H - 120))
    return im


# ---------------------------------------------------------------- dựng
def main():
    WORK.mkdir(parents=True, exist_ok=True)
    scrim, scrim_top = bottom_scrim()
    use_clips = True
    players = {}
    cmd = [str(FFMPEG), "-y", "-hide_banner", "-loglevel", "error",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-vf", "noise=alls=3:allf=t+u,vignette=PI/5,format=yuv420p",
           "-c:v", "libopenh264", "-b:v", "8M", "-maxrate", "12M", "-bufsize", "16M",
           "-r", str(FPS), str(OUT_PICTURE)]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    for fi in range(NFR):
        t = fi / FPS
        fr = bg_at(t)
        b = beat_at(t)
        key = b["key"]

        # lớp clip động: nếu có clip Hailuo-2.3 cho nhịp này thì trộn vào nền
        clip_name = CLIP_FOR_BEAT.get(key) if use_clips else None
        clip_path = CLIP_DIR / f"{clip_name}.mp4" if clip_name else None
        if clip_path and clip_path.exists():
            if key not in players:
                players[key] = ClipPlayer(clip_path)
            cf = players[key].next()
            if cf is not None:
                k_in = ease((t - b["t0"]) / XFADE)
                k_out = 1 - ease((t - (b["t1"] - XFADE)) / XFADE)
                w = max(0.0, min(1.0, k_in) * max(0.0, min(1.0, k_out)))
                if w > 0:
                    fr = Image.blend(fr.convert("RGBA"), cf.convert("RGBA"), w)

        if key == "hook":
            layer = hook_layer(t)
            k_out = 1 - ease((t - 4.0) / 0.6)
            fr.alpha_composite(fade_alpha(layer, k_out), ((W - layer.width) // 2, 120))

        elif key == "board":
            fr.alpha_composite(board_tags(t))

        elif key in ("host", "inv", "psy"):
            k_in = ease((t - b["t0"]) / 0.7)
            k_out = 1 - ease((t - (b["t1"] - 0.55)) / 0.55)
            m = mascot_cutout(MASCOT[key], 720)
            fr.alpha_composite(fade_alpha(m, k_in * k_out), (W - m.width - 40, H - m.height + 40))
            fr.alpha_composite(scrim, (0, scrim_top))
            lab = label_layer(*(LABELS_EN if ED.EN else LABELS)[key])
            fr.alpha_composite(fade_alpha(lab, k_in), (96, H - 190))

        elif key == "all":
            k_in = ease((t - b["t0"]) / 0.8)
            for mk, h, pos in (("H", 540, (40, H - 480)), ("C", 500, (W // 2 - 250, H - 450)),
                               ("D", 540, (W - 580, H - 480))):
                m = mascot_cutout(mk, h)
                fr.alpha_composite(fade_alpha(m, k_in), pos)
            fr.alpha_composite(scrim, (0, scrim_top))

        elif key == "card":
            k_in = ease((t - b["t0"]) / 0.5)
            k_out = 1 - ease((t - (b["t1"] - 0.5)) / 0.5)
            # thời gian tương đối (bắt đầu tại 4,00 s như bumper) để các dòng hiện lần lượt
            c = card_layer(t - b["t0"] + 4.00)
            fr.alpha_composite(fade_alpha(c, k_in * k_out), ((W - c.width) // 2, (H - c.height) // 2))

        elif key == "end":
            k = ease((t - b["t0"]) / 1.3)
            fr.alpha_composite(endcard_layer(k))

        elif key == "out":
            k = ease((t - b["t0"]) / 0.8)
            dark = Image.new("RGBA", (W, H), INK + (int(238 * k),))
            fr.alpha_composite(dark)
            wm_k = k * (1 - 0.5 * ease((t - 49.3) / 0.7))
            fr.alpha_composite(watermark_layer(wm_k))

        p.stdin.write(fr.convert("RGB").tobytes())
        if fi % 150 == 0:
            print(f"  frame {fi}/{NFR}  t={t:.1f}s  [{key}]", flush=True)

    p.stdin.close()
    if p.wait() != 0:
        raise SystemExit("ffmpeg failed")
    for pl in players.values():
        pl.close()
    print("done ->", OUT_PICTURE)


if __name__ == "__main__":
    main()
