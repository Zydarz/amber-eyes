#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B6–B7 — render the episode picture frame by frame (plan v9 sections 5–7).

usage:
  py -3 .work/build_video3.py                 # full episode, 6 workers
  py -3 .work/build_video3.py --from 20 --to 90 --workers 2 --out .work/video3/test.mp4
  py -3 .work/build_video3.py --stills 30,75,160   # PNG stills to .work/video3/stills
"""
import argparse
import json
import math
import subprocess
import sys
import wave
from functools import lru_cache
from multiprocessing import Pool
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).parent))
import edition as ED  # noqa: E402  (AE_LANG=en -> English edition)

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
BG = ROOT / "assets" / "bg"
CAST = ROOT / "assets" / "cast"
BRAND = ROOT / "assets" / "brand"
FONTS = Path(r"C:\Windows\Fonts")
W, H, FPS = 1920, 1080, 30

C = dict(ink=(14, 14, 17), slate=(28, 31, 43), paper=(230, 222, 208), paper_ink=(28, 27, 31),
         text=(242, 239, 233), muted=(156, 152, 143), pink=(232, 160, 191), red=(200, 66, 58),
         amber=(226, 180, 103), cold=(134, 169, 204), violet=(169, 155, 214), sand=(217, 185, 155),
         cyan=(110, 140, 160))
ROLE_COLOR = {"H": C["amber"], "D": C["cold"], "C": C["violet"], "N1": C["sand"], "N2": C["cyan"]}
ROLE_NAME = ED.ROLE_NAME

TL = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
SH = json.loads(ED.w("shots.json").read_text(encoding="utf-8"))["shots"]
ITEMS = TL["items"]
SENT = {it["id"]: it for it in ITEMS}
TOTAL = TL["total"]
INTRO_END = TL["intro"]

# ---------------------------------------------------------------- turns
TURNS = []
for it in ITEMS:
    if TURNS and TURNS[-1]["element"] == it["element"]:
        TURNS[-1]["end"] = it["end"]
    else:
        TURNS.append({"element": it["element"], "role": it["role"], "start": it["start"],
                      "end": it["end"], "first": it["id"]})
FIRST_TURN = {}
for tu in TURNS:
    FIRST_TURN.setdefault(tu["role"], tu["start"])


# ---------------------------------------------------------------- helpers
@lru_cache(None)
def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def ease(x):
    x = min(1.0, max(0.0, x))
    return x * x * (3 - 2 * x)


def with_alpha(im, k):
    if k >= 0.999:
        return im
    out = im.copy()
    out.putalpha(im.getchannel("A").point(lambda v: int(v * max(0.0, k))))
    return out


def wrap(text, fnt, width):
    if ED.JA:
        lines, cur = [], ""
        # Japanese Kinsoku shori: avoid starting a line with punctuation
        no_start = "、。，．・？！：；ー）〕］｝」』〉》"
        for c in text:
            t = cur + c
            if fnt.getlength(t) <= width or not cur:
                cur = t
            elif c in no_start:
                cur = t
            else:
                lines.append(cur)
                cur = c
        if cur:
            lines.append(cur)
        return lines
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if fnt.getlength(t) <= width or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def text_block(lines_spec, width):
    """lines_spec: [(text, font, color, gap_after_px)] -> RGBA image, text wrapped to width."""
    rows = []                                   # ("t", text, font, color) | ("g", px)
    for text, fnt, col, gap in lines_spec:
        for ln in wrap(text, fnt, width):
            rows.append(("t", ln, fnt, col))
        if gap:
            rows.append(("g", gap))
    hgt = sum(int(r[2].size * 1.25) if r[0] == "t" else r[1] for r in rows)
    im = Image.new("RGBA", (int(width) + 20, max(1, hgt) + 12), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    y = 0
    for r in rows:
        if r[0] == "t":
            d.text((0, y), r[1], font=r[2], fill=r[3] + (255,))
            y += int(r[2].size * 1.25)
        else:
            y += r[1]
    return im


class El:
    """A timed overlay: image placed at (x, y), fading in at t0 (and optional t1 out)."""
    def __init__(self, img, x, y, t0, t1=None, fade=0.35, rise=24):
        self.img, self.x, self.y, self.t0, self.t1, self.fade, self.rise = img, x, y, t0, t1, fade, rise

    def draw(self, fr, t):
        if t < self.t0 or (self.t1 is not None and t > self.t1 + self.fade):
            return
        k = ease((t - self.t0) / self.fade) if self.fade else 1.0
        if self.t1 is not None and t > self.t1:
            k *= 1 - ease((t - self.t1) / self.fade)
        dy = int(self.rise * (1 - k)) if self.rise else 0
        fr.alpha_composite(with_alpha(self.img, k), (int(self.x), int(self.y + dy)))


class Dyn:
    """Overlay drawn by a function f(fr, t) from t0."""
    def __init__(self, f, t0, t1=None):
        self.f, self.t0, self.t1 = f, t0, t1

    def draw(self, fr, t):
        if t >= self.t0 and (self.t1 is None or t <= self.t1):
            self.f(fr, t)


# ---------------------------------------------------------------- timing
def seg_times(shot):
    """Absolute time each text segment appears."""
    sents = shot["sentences"]
    starts = [SENT[s]["start"] for s in sents]
    segs = shot["segments"]
    phr = list(shot["beats"])
    out = []
    for i, sg in enumerate(segs):
        t = None
        if sg["at_sentence"]:
            tgt = [s for s in sents if s.endswith(f"#{sg['at_sentence']}")]
            if tgt:
                t = SENT[tgt[0]]["start"] - 0.15
        if t is None and i > 0:
            if phr:
                t = phrase_time(shot, phr.pop(0))
            elif i < len(starts):
                t = starts[i] - 0.15
            elif starts:
                t = (SENT[sents[-1]]["start"] + SENT[sents[-1]]["end"]) / 2
        if t is None:
            t = shot["start"] + 0.15
        out.append(t)
    if shot.get("hold"):
        out = [shot["start"] - 10] * len(segs)
    return out


def phrase_time(shot, phrase):
    p = phrase.lower()
    for s in shot["sentences"]:
        it = SENT[s]
        txt = it["text"].lower()
        k = txt.find(p)
        if k >= 0:
            return it["start"] + (it["end"] - it["start"]) * k / max(1, len(txt)) - 0.15
    return None


def bust_windows():
    wins = []
    by_start = {}
    for s in SH:
        for sid in s["sentences"]:
            by_start.setdefault(sid, s)
    for tu in TURNS:
        sh = by_start.get(tu["first"])
        if sh and sh["flags"]["nobust"]:
            continue
        wins.append((tu["role"], tu["start"] - 0.3, min(tu["end"], tu["start"] + 6.0), tu["start"]))
    for s in SH:
        if s["flags"]["bust"] and s["role"] in ROLE_COLOR:
            wins.append((s["role"], s["start"], min(s["end"], s["start"] + 6.0), None))
    return wins


BUST_WINS = bust_windows()


def bust_visible_at(t):
    for role, a, b, _ in BUST_WINS:
        if a <= t <= b:
            return role
    return None


# ---------------------------------------------------------------- templates
F_HEAD = lambda s=64: font("YuGothB.ttc", s) if ED.JA else font("segoeuib.ttf", s)
F_LAB = lambda s=26: font("YuGothB.ttc", s) if ED.JA else font("seguisb.ttf", s)
F_SUB = lambda s=32: font("YuGothM.ttc", s) if ED.JA else font("segoeui.ttf", s)
# Georgia lacks 92 Vietnamese glyphs (ơ ư ả ạ ề ể ố…): Cambria is the serif with full coverage
F_QUOTE = lambda s=56: font("YuGothM.ttc", s) if ED.JA else font("cambriai.ttf", s)
F_GEO = lambda s=72: font("YuGothB.ttc", s) if ED.JA else font("cambria.ttc", s)
F_GEOB = lambda s=50: font("YuGothB.ttc", s) if ED.JA else font("cambriab.ttf", s)
F_MONO = lambda s=28: font("YuGothM.ttc", s) if ED.JA else font("consola.ttf", s)
F_NUM = lambda s=260: font("bahnschrift.ttf", s)


def gradient_bottom(frac=0.45, alpha=180):
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    a = np.zeros((H, W), np.uint8)
    h0 = int(H * (1 - frac))
    a[h0:] = np.linspace(0, alpha, H - h0, dtype=np.float32)[:, None].astype(np.uint8)
    g.putalpha(Image.fromarray(a))
    return g


GRAD = None
DARK70 = None


def split_elems(elems):
    lab = [v for k, v in elems if k == "ital"]
    head = [v for k, v in elems if k == "bold"]
    quo = [v for k, v in elems if k == "quote"]
    return lab, head, quo


def role_col(shot):
    return ROLE_COLOR.get(shot.get("role") or "H", C["amber"])


def build_elements(shot):
    """Return list of El/Dyn for the shot (static text, graphics)."""
    global GRAD, DARK70
    if GRAD is None:
        GRAD = gradient_bottom()
        DARK70 = Image.new("RGBA", (W, H), (8, 8, 10, 178))
    if shot.get("hold"):
        # a hold continues the previous shot: everything is already on screen
        shot = dict(shot, start=shot["start"] - 30, sentences=[])
    T = shot["template"]
    st = shot["start"]
    times = seg_times(shot)
    col = role_col(shot)
    els = []
    segs = shot["segments"]
    x_left = 560 if (bust_visible_at(st + 0.4) and T in ("T1",)) else 96

    if T in ("T1", None):
        els.append(El(GRAD, 0, 0, st - 10, fade=0, rise=0))
        for t, sg in zip(times, segs):
            lab, head, quo = split_elems(sg["elems"])
            spec = []
            if lab and (not head or sg["elems"][0][0] == "ital"):
                spec.append((lab[0].upper() if len(lab[0]) < 40 else lab[0], F_LAB(28), col, 14))
            for hd in head:
                spec.append((hd, F_HEAD(66), C["text"], 10))
            for q in quo:
                spec.append((f"“{q}”", F_QUOTE(48), C["text"], 10))
            for lb in lab[1:] if (lab and (not head or sg["elems"][0][0] == "ital")) else lab:
                spec.append((lb, F_SUB(34), C["muted"], 6))
            img = text_block(spec, 1180 if x_left < 200 else 1240)
            # stack segments upward from y=900
            els.append(("stack", t, img))
        els = stack_bottom(els, x_left, 900)

    elif T == "T2":
        els += t2_card(shot, times, col)
    elif T == "T3":
        els += t3_split(shot, times, col)
    elif T == "T4":
        els.append(El(DARK70, 0, 0, st - 10, fade=0, rise=0))
        els += t4_quote(shot, times, col)
    elif T == "T5":
        els.append(El(DARK70 if shot["variant"] != "date" else GRAD, 0, 0, st - 10, fade=0, rise=0))
        els += t5_number(shot, times, col)
    elif T == "T6":
        els.append(El(DARK70, 0, 0, st - 10, fade=0, rise=0))
        els += t6_timeline(shot, times, col)
    elif T == "T7":
        els.append(El(GRAD, 0, 0, st - 10, fade=0, rise=0))
        els += t7_route(shot, times, col)
    elif T == "T8":
        els.append(El(DARK70, 0, 0, st - 10, fade=0, rise=0))
        els += t8_list(shot, times, col)
    elif T == "T9":
        els.append(El(DARK70, 0, 0, st - 10, fade=0, rise=0))
        els += t9_term(shot, times, col)
    elif T == "T10":
        els += t10_chapter(shot, times, col)
    elif T == "T11":
        els.append(El(DARK70, 0, 0, st - 10, fade=0, rise=0))
        els += t11_post(shot, times, col)
    if shot.get("inset"):
        els.append(inset_photo(shot))
    return els


def stack_bottom(items, x, bottom):
    """T1 blocks: later segments push earlier ones up (all aligned to `bottom`)."""
    out = [e for e in items if isinstance(e, (El, Dyn))]
    blocks = [e for e in items if isinstance(e, tuple)]
    if not blocks:
        return out
    # final layout: last block sits on the bottom line, previous above it
    y = bottom
    pos = []
    for _, t, img in reversed(blocks):
        y -= img.height
        pos.append(y)
        y -= 18
    pos.reverse()
    for (_, t, img), yy in zip(blocks, pos):
        out.append(El(img, x, yy, t))
    return out


def t2_card(shot, times, col):
    els = []
    st = shot["start"]
    shade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    a = np.zeros((H, W), np.uint8)
    a[:, :] = np.clip(np.linspace(150, 40, W), 0, 255).astype(np.uint8)[None, :]
    shade.putalpha(Image.fromarray(a))
    els.append(El(shade, 0, 0, st - 10, fade=0, rise=0))
    cw = 860
    y = 70
    parts = []
    closing = bool(shot is SH[-1] and not shot["sentences"])     # thẻ kết tập: tên kênh cỡ lớn, giấy cao hơn
    if closing:
        y = 96
    for t, sg in zip(times, shot["segments"]):
        lab, head, quo = split_elems(sg["elems"])
        spec = []
        first_is_lab = sg["elems"] and sg["elems"][0][0] == "ital"
        if lab and first_is_lab:
            spec.append((lab[0].upper(), F_MONO(30 if closing else 26), C["red"], 16 if closing else 12))
        for hd in head:
            spec.append((hd, F_GEOB(92 if closing else 46), C["paper_ink"], 22 if closing else 12))
        rest = lab[1:] if first_is_lab else lab
        for lb in rest:
            for piece in lb.split(" · ") if len(lb) > 48 else [lb]:
                spec.append(("— " + piece if len(lb) > 48 else piece, F_MONO(34 if closing else 27), C["paper_ink"], 8 if closing else 6))
        for q in quo:
            spec.append((f"“{q}”", F_QUOTE(36), C["red"], 6))
        img = text_block(spec, cw - 130)
        parts.append((t, img, y))
        y += img.height + 16
    ch = max(440 if closing else 340, y + 70)   # card fits its text
    rng = np.random.default_rng(abs(hash(shot["id"])) % 999)
    tex = rng.normal(0, 5, (ch, cw, 1)).repeat(3, axis=2)
    paper = np.clip(np.array(C["paper"], np.float32)[None, None, :] + tex, 0, 255).astype(np.uint8)
    base = Image.fromarray(paper, "RGB").convert("RGBA")
    d = ImageDraw.Draw(base)
    d.rectangle([0, 0, cw - 1, ch - 1], outline=(196, 186, 168, 255), width=3)
    d.rounded_rectangle([cw - 150, -10, cw - 110, 70], radius=18, outline=(120, 120, 128, 255), width=5)
    # static card fades with the shot; text parts appear in turn
    card_rot = lambda im: im.rotate(-1.5, resample=Image.BICUBIC, expand=True)
    X, Y = 960, max(150, 540 - ch // 2)
    els.append(El(card_rot(base), X, Y, st + 0.05, rise=12))
    for t, img, yy in parts:
        layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
        layer.alpha_composite(img, (64, yy))
        els.append(El(card_rot(layer), X, Y, t, rise=0))
    # stamp
    if any(w in (shot["beat_text"] or "") for w in ("Dấu mộc", "dấu", "Dấu")):
        word = ED.UI["stamp_forged"] if "giả mạo" in shot["beat_text"] else ED.UI["stamp_secret"]
        stamp = Image.new("RGBA", (360, 130), (0, 0, 0, 0))
        sd = ImageDraw.Draw(stamp)
        sd.rounded_rectangle([4, 4, 356, 126], radius=14, outline=C["red"] + (230,), width=7)
        fs = 64
        while fs > 30 and F_MONO(fs).getlength(word) > 316:      # longer words (CONFIDENTIAL) shrink to fit
            fs -= 2
        sd.text((180, 66), word, font=F_MONO(fs), fill=C["red"] + (230,), anchor="mm")
        stamp = stamp.rotate(9, resample=Image.BICUBIC, expand=True)
        t = phrase_time(shot, shot["beats"][0]) if shot["beats"] else st + 1.0
        # just below the last text line (y = text bottom inside the card)
        els.append(El(stamp, X + cw - 360, Y + y - 10, t or st + 1, fade=0.15, rise=0))
    return els


def t3_split(shot, times, col):
    els = []
    st = shot["start"]
    shade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    a = np.zeros((H, W), np.uint8)
    a[:, 900:] = 175
    a[:, 780:900] = np.linspace(0, 175, 120).astype(np.uint8)[None, :]
    shade.putalpha(Image.fromarray(a))
    els.append(El(shade, 0, 0, st - 10, fade=0, rise=0))
    line = Image.new("RGBA", (4, 380), col + (255,))
    els.append(El(line, 920, 350, st + 0.1, rise=0))
    m = None
    import re as _re
    m = _re.search(r"`(\d)/(\d)`", shot.get("beat_text", "") or "")
    cnt = _re.search(r"(\d)/(\d)", json.dumps(shot["segments"]))
    if shot["variant"] == "compare":
        els.insert(0, El(Image.new("RGBA", (W, H), (8, 8, 10, 190)), 0, 0, st - 10, fade=0, rise=0))
        segs = shot["segments"]
        el = segs[0]["elems"]
        k = [i for i, (kind, _) in enumerate(el) if kind == "bold"]
        if len(segs) == 1 and len(k) >= 2:            # Tập 01: một đoạn, cột phải từ tiêu đề đậm thứ 2
            left, right = el[:k[1]], el[k[1]:]
            t2 = SENT[shot["sentences"][1]]["start"] - 0.15 if len(shot["sentences"]) > 1 else st + 4
        elif len(segs) >= 2:                           # Tập 02: 'trái → phải', cột phải hiện theo mốc của đoạn sau
            left = el
            right = [e for sg in segs[1:] for e in sg["elems"]]
            t2 = times[1]
        else:                                          # chỉ một cột: để trái, không có cột phải
            left, right, t2 = el, [], st + 4
        def cspec(elems):
            # giữ đúng thứ tự chữ (nhãn nhỏ đứng trước tiêu đề nếu viết trước); câu trích hiện như tiêu đề nghiêng
            out = []
            for kind, txt in elems:
                if kind == "bold":
                    out.append((txt, F_HEAD(62), C["text"], 10))
                elif kind == "quote":
                    out.append((f"“{txt}”", F_QUOTE(44), C["text"], 10))
                else:
                    out.append((txt, F_SUB(36), C["muted"], 6))
            return out
        if not right:
            els.append(El(text_block(cspec(left), 720), 140, 430, st + 0.2))
            return els
        for elems, x, t in ((left, 140, st + 0.2), (right, 980, t2)):
            els.append(El(text_block(cspec(elems), 720), x, 430, t))
        return els
    blocks = []
    for t, sg in zip(times, shot["segments"]):
        lab, head, quo = split_elems(sg["elems"])
        first_is_lab = sg["elems"] and sg["elems"][0][0] == "ital"
        spec = []
        if lab and first_is_lab:
            spec.append((lab[0].upper(), F_LAB(28), col, 12))
        for hd in head:
            spec.append((hd, F_HEAD(60), C["text"], 10))
        for lb in (lab[1:] if first_is_lab else lab):
            spec.append((lb, F_SUB(34), C["muted"], 6))
        blocks.append((t, text_block(spec, 840)))
    y = 540 - sum(b.height + 24 for _, b in blocks) // 2
    for t, img in blocks:
        els.append(El(img, 970, y, t))
        y += img.height + 24
    return els


def t4_quote(shot, times, col):
    els = []
    st = shot["start"]
    if shot["variant"] == "testimony" or shot.get("role") in ("N1", "N2"):
        col = ROLE_COLOR.get(shot.get("role"), col)
    qm = Image.new("RGBA", (260, 260), (0, 0, 0, 0))
    ImageDraw.Draw(qm).text((0, -40), "“", font=font("georgia.ttf", 300), fill=col + (110,))
    els.append(El(qm, 470, 170, st + 0.1, rise=0))
    y = 330
    for t, sg in zip(times, shot["segments"]):
        lab, head, quo = split_elems(sg["elems"])
        spec = [(l.upper() if len(l) < 40 else l, F_LAB(28) if len(l) < 40 else F_SUB(34),
                 col if len(l) < 40 else C["muted"], 14) for l in lab]
        spec += [(h, F_HEAD(56), C["text"], 10) for h in head]
        spec += [(f"“{q}”" if not q.startswith("“") else q, F_QUOTE(54 if len(q) < 90 else 46), C["text"], 14) for q in quo]
        img = text_block(spec, 1180)
        if quo:
            dd = ImageDraw.Draw(img)
            dd.line([0, img.height - 8, 160, img.height - 8], fill=col + (255,), width=4)
        els.append(El(img, 600, y, t))
        y += img.height + 26
    return els


def t5_number(shot, times, col):
    import re as _re
    els = []
    st = shot["start"]
    for t, sg in zip(times, shot["segments"]):
        lab, head, quo = split_elems(sg["elems"])
        first_is_lab = sg["elems"] and sg["elems"][0][0] == "ital"
        top = lab[0] if (lab and first_is_lab) else None
        sub = lab[1:] if first_is_lab else lab
        big = head[0] if head else None
        X = 760
        if shot["variant"] == "date":
            X = 560 if bust_visible_at(t + 0.5) else 140
        if top:
            els.append(El(text_block([(top.upper(), F_LAB(30), col, 0)], 1000), X, 330, t))
        if big:
            m = _re.match(r"^([−-]?)(\d+)(.*)$", big)
            if shot["variant"] == "date":
                def f(fr, tt, big=big, t0=t, X=X):
                    n = max(1, min(len(big), int((tt - t0) / 0.07) + 1))
                    d = ImageDraw.Draw(fr)
                    d.text((X, 400), big[:n], font=F_MONO(150), fill=C["text"] + (255,))
                els.append(Dyn(f, t))
            elif m and len(m.group(2)) <= 3:
                sign, num, rest = m.group(1).replace("−", "-"), int(m.group(2)), m.group(3)  # Bahnschrift has no U+2212
                fz = F_NUM(250 if len(big) < 7 else 170)
                def f(fr, tt, sign=sign, num=num, rest=rest, t0=t, fz=fz, X=X):
                    k = ease((tt - t0) / 1.2)
                    val = int(round(num * k))
                    d = ImageDraw.Draw(fr)
                    d.text((X, 380), f"{sign}{val}{rest}", font=fz, fill=C["text"] + (int(255 * min(1, (tt - t0) / 0.3)),))
                els.append(Dyn(f, t))
            else:
                els.append(El(text_block([(big, F_HEAD(110), C["text"], 0)], 1100), X, 420, t))
        if sub:
            els.append(El(text_block([(s, F_SUB(38), C["muted"], 6) for s in sub], 1000), X, 700, t + 0.3))
    if "Thanh tiến trình" in (shot.get("beat_text") or ""):
        def bar(fr, tt, st=st):
            k = ease((tt - st - 0.5) / 2.5) * 0.85
            d = ImageDraw.Draw(fr)
            d.rectangle([760, 670, 1660, 682], fill=(60, 60, 66, 255))
            d.rectangle([760, 670, 760 + int(900 * k), 682], fill=col + (255,))
        els.append(Dyn(bar, st))
    return els


def t6_timeline(shot, times, col):
    els = []
    st = shot["start"]
    x0 = 600 if bust_visible_at(st + 0.4) else 160
    x1 = 1760
    y = 520
    n = len(shot["segments"])

    def axis(fr, tt):
        k = ease((tt - st) / 0.8)
        d = ImageDraw.Draw(fr)
        d.line([x0, y, x0 + (x1 - x0) * k, y], fill=C["muted"] + (255,), width=4)
    els.append(Dyn(axis, st))
    for i, (t, sg) in enumerate(zip(times, shot["segments"])):
        lab, head, _ = split_elems(sg["elems"])
        txt = (lab + head)[0]
        parts = txt.split(" · ", 1)
        xx = x0 + (x1 - x0) * (i + 0.5) / max(1, n)
        dot = Image.new("RGBA", (40, 40), (0, 0, 0, 0))
        ImageDraw.Draw(dot).ellipse([4, 4, 36, 36], fill=C["pink"] + (255,))
        els.append(El(dot, xx - 20, y - 20, t, rise=0))
        spec = [(parts[0], F_HEAD(42), C["text"], 6)]
        if len(parts) > 1:
            spec.append((parts[1], F_SUB(28), C["muted"], 0))
        img = text_block(spec, max(220, (x1 - x0) / max(1, n) - 20))
        above = i % 2 == 0
        els.append(El(img, xx - 110, (y - 40 - img.height) if above else (y + 40), t))
    return els


def t7_route(shot, times, col):
    els = []
    st = shot["start"]
    A, B = (360, 640), (1560, 420)

    def route(fr, tt):
        k = ease((tt - st - 0.3) / 1.5)
        d = ImageDraw.Draw(fr)
        n = 40
        for i in range(int(n * k)):
            if i % 2 == 0:
                a = i / n; b = (i + 1) / n
                p = lambda u: (A[0] + (B[0] - A[0]) * u, A[1] + (B[1] - A[1]) * u - math.sin(u * math.pi) * 160)
                d.line([p(a), p(b)], fill=C["red"] + (255,), width=6)
        na, nb = ED.EP.get("route_pins", {}).get(shot["id"], ("", ""))   # nhãn ghim theo tập (edition)
        for j, ((px, py), name) in enumerate(((A, na), (B, nb))):
            if j == 1 and k < 0.98:
                continue
            d.ellipse([px - 14, py - 14, px + 14, py + 14], fill=C["red"] + (255,))
            d.text((px, py + 26), name, font=F_LAB(26), fill=C["text"] + (255,), anchor="ma")
    els.append(Dyn(route, st))
    blocks = []
    for t, sg in zip(times, shot["segments"]):
        lab, head, _ = split_elems(sg["elems"])
        spec = [(h, F_HEAD(66), C["text"], 10) for h in head] + [(l, F_SUB(34), C["muted"], 6) for l in lab]
        blocks.append((t, text_block(spec, 1100)))
    # nhiều đoạn (Tập 02): xếp chồng, khối cuối chạm y = 820 + chiều cao khối đầu như cũ
    y = 820 + (blocks[0][1].height if blocks else 0) - sum(b.height + 16 for _, b in blocks) + 16
    for t, img in blocks:
        els.append(El(img, 96, y, t + 1.0))
        y += img.height + 16
    return els


def t8_list(shot, times, col):
    els = []
    st = shot["start"]
    v = shot["variant"]
    if v == "flags" or shot["id"] in ED.EP["flag_hold_shots"]:
        return flags(shot, times, col)
    seg = shot["segments"][0]
    lab, head, _ = split_elems(seg["elems"])
    if v == "strike":
        items = lab[0].split(" · ") if lab else []
        title = None
    elif lab:
        title = lab[0] if len(lab) > 1 else None
        items = (lab[1] if len(lab) > 1 else lab[0]).split(" · ")
    else:                                    # đoạn đầu chỉ có tiêu đề đậm -> làm nhãn trên danh sách
        title, items = (head[0] if head else None), []
    n_struck = len(items)
    # các đoạn sau '→' (Tập 02): mỗi mục hiện đúng lúc đoạn đó tới; tiêu đề đậm thành mục nhấn
    extra = []
    for t_seg, sg in list(zip(times, shot["segments"]))[1:]:
        for kind, txt in sg["elems"]:
            parts = [txt] if kind == "bold" else txt.split(" · ")
            extra += [(p, t_seg, kind == "bold") for p in parts if p.strip()]
    x = 980
    if title:
        els.append(El(text_block([(title.upper(), F_LAB(30), col, 0)], 860), x, 250, st + 0.2))
    y0 = 330
    sents = shot["sentences"]
    rows = [(it, None, False) for it in items] + extra
    step = 88 if len(rows) <= 7 else max(56, 600 // len(rows))
    for i, (it, t_fix, strong) in enumerate(rows):
        if t_fix is not None:
            t_in = t_fix
        elif v == "strike":
            t_in = st + 0.1
        else:
            pt = phrase_time(shot, it.split()[0] + " " + it.split()[1] if len(it.split()) > 1 else it)
            t_in = pt if pt else st + 0.5 + i * 1.2
        num = f"{sum(1 for r in rows[:i + 1] if not r[2]):02d}"     # dòng nhấn (đậm) không đánh số
        font = F_HEAD(44) if strong else F_SUB(42)
        img = text_block([(f"{num}   {it}" if not strong else it, font, C["text"], 0)], 880)
        els.append(El(img, x, y0 + i * step, t_in))
        if v == "strike" and i < n_struck:
            ts = SENT[sents[i]]["start"] - 0.05 if i < len(sents) else st + 1 + i
            w_ = int(F_SUB(42).getlength(f"{num}   {it}"))
            def strike(fr, tt, ts=ts, w_=w_, yy=y0 + i * step + 30):
                k = ease((tt - ts) / 0.4)
                ImageDraw.Draw(fr).line([x, yy, x + w_ * k, yy], fill=C["red"] + (255,), width=6)
            els.append(Dyn(strike, ts))
    return els


FLAG_TITLES = {}


def flags(shot, times, col):
    els = []
    st = shot["start"]
    idx = None
    seg = shot["segments"][0] if shot["segments"] else None
    if seg:
        lab, head, quo = split_elems(seg["elems"])
        if lab and lab[0].isdigit():
            idx = int(lab[0])
            FLAG_TITLES[idx] = head[0] if head else ""
    show_all = idx is None

    def draw_flags(fr, tt):
        d = ImageDraw.Draw(fr)
        for i in range(4):
            x = 260 + i * 380
            filled = show_all or (i + 1 < idx) or (i + 1 == idx and tt >= st + 0.4)
            d.line([x, 220, x, 380], fill=C["muted"] + (255,), width=5)
            poly = [(x, 222), (x + 110, 250), (x, 280)]
            if filled:
                d.polygon(poly, fill=C["red"] + (255,))
            else:
                d.polygon(poly, outline=C["muted"] + (255,))
            d.text((x - 6, 400), f"{i + 1:02d}", font=font("bahnschrift.ttf", 40), fill=(C["text"] if filled else C["muted"]) + (255,))
    els.append(Dyn(draw_flags, st))
    if show_all:
        for i in range(1, 5):
            tt = FLAG_TITLES.get(i, "")
            els.append(El(text_block([(tt, F_SUB(30), C["text"], 0)], 340), 250 + (i - 1) * 380, 470, st + 0.1))
        return els
    lab, head, quo = split_elems(seg["elems"])
    spec = [(h, F_HEAD(58), C["text"], 12) for h in head]
    els.append(El(text_block(spec, 1400), 260, 560, st + 0.3))
    if quo:
        stamp = Image.new("RGBA", (560, 120), (0, 0, 0, 0))
        sd = ImageDraw.Draw(stamp)
        sd.rounded_rectangle([4, 4, 556, 116], radius=14, outline=C["red"] + (230,), width=6)
        sd.text((280, 60), f"“{quo[0]}”", font=F_QUOTE(46), fill=C["red"] + (230,), anchor="mm")
        stamp = stamp.rotate(6, resample=Image.BICUBIC, expand=True)
        t = phrase_time(shot, quo[0]) or st + 2
        els.append(El(stamp, 1180, 760, t, fade=0.15, rise=0))
    return els


def t9_term(shot, times, col):
    els = []
    y = 360
    for t, sg in zip(times, shot["segments"]):
        lab, head, _ = split_elems(sg["elems"])
        first_is_lab = sg["elems"] and sg["elems"][0][0] == "ital" and not sg["elems"][0][1].startswith("(")
        spec = []
        for k, v in sg["elems"]:
            if k == "bold":
                spec.append((v, F_HEAD(70), C["text"], 8))
            elif v.startswith("("):
                spec.append((v, F_MONO(32), C["muted"], 14))
            elif first_is_lab and v == sg["elems"][0][1]:
                spec.append((v.upper(), F_LAB(28), col, 14))
            else:
                spec.append((v, F_SUB(34), C["muted"], 8))
        img = text_block(spec, 1050)
        rule = Image.new("RGBA", (120, 5), col + (255,))
        els.append(El(rule, 760, y - 30, t, rise=0))
        els.append(El(img, 760, y, t))
        y += img.height + 30
    return els


def t10_chapter(shot, times, col):
    els = []
    for t, sg in zip(times, shot["segments"]):
        lab, head, _ = split_elems(sg["elems"])
        spec = []
        for k, v in sg["elems"]:
            if k == "ital":
                spec.append((v.upper() if len(v) < 30 else v, F_MONO(30) if len(v) < 30 else F_SUB(34), C["amber"] if len(v) < 30 else C["muted"], 18))
            else:
                spec.append((v, F_GEO(70), C["text"], 10))
        img = text_block(spec, 1500)
        els.append(El(img, (W - img.width) // 2 + 10, 420, t))
    return els


def t11_post(shot, times, col):
    els = []
    st = shot["start"]
    card = Image.new("RGBA", (780, 430), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, 779, 429], radius=22, fill=(30, 32, 40, 245), outline=(70, 74, 90, 255), width=2)
    d.ellipse([34, 34, 114, 114], fill=C["pink_deep"] if "pink_deep" in C else (168, 82, 115))
    d.polygon([(74, 52), (100, 76), (48, 76)], fill=C["pink"])
    d.rectangle([56, 76, 92, 100], fill=C["pink"])
    d.rounded_rectangle([140, 50, 420, 72], radius=10, fill=(80, 84, 100, 255))
    d.rounded_rectangle([140, 86, 300, 102], radius=8, fill=(60, 64, 78, 255))
    for i, wdt in enumerate((640, 600, 420)):
        d.rounded_rectangle([40, 170 + i * 48, 40 + wdt, 196 + i * 48], radius=12, fill=(70, 74, 90, 255))
    d.text((640, 394), ED.UI["illus"], font=F_LAB(22), fill=C["muted"] + (255,))
    els.append(El(card, 570, 200, st + 0.1))
    for t, sg in zip(times, shot["segments"]):
        lab, head, _ = split_elems(sg["elems"])
        if lab:
            els.append(El(text_block([(l.upper(), F_LAB(28), col, 0) for l in lab], 900), 570, 150, t))
        if head:
            els.append(El(text_block([(h, F_HEAD(58), C["text"], 8) for h in head], 1300), 570, 700, t))
    return els


def inset_photo(shot):
    src = Image.open(BG / f"{shot['inset']}.png").convert("RGB").resize((520, 292), Image.LANCZOS)
    fr = Image.new("RGBA", (552, 324), (236, 232, 222, 255))
    fr.paste(src, (16, 16))
    d = ImageDraw.Draw(fr)
    d.ellipse([262, 2, 290, 30], fill=C["red"] + (255,))
    fr = fr.rotate(3, resample=Image.BICUBIC, expand=True)
    return El(fr, 220, 260, shot["start"] + 0.2)


# ---------------------------------------------------------------- backgrounds
@lru_cache(maxsize=6)
def bg_image(name):
    return Image.open(BG / f"{name}.png").convert("RGB")


VIGNETTE = None
GRAIN = None


def finishing(arr, fi):
    global VIGNETTE, GRAIN
    if VIGNETTE is None:
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        r = np.hypot((xx - W / 2) / (W / 2), (yy - H / 2) / (H / 2))
        VIGNETTE = np.clip(1.08 - 0.32 * r ** 2, 0.55, 1.0)[..., None].astype(np.float32)
        rng = np.random.default_rng(5)
        GRAIN = [rng.normal(0, 5.5, (H, W, 1)).astype(np.float32) for _ in range(6)]
    a = arr.astype(np.float32) * VIGNETTE + GRAIN[fi % 6]
    a[:, 1:, 0] = a[:, :-1, 0]                       # rgbashift ±1 (red one px right)
    return np.clip(a, 0, 255).astype(np.uint8)


def camera_box(shot, t):
    p = min(1.0, max(0.0, (t - shot["start"]) / max(0.1, shot["end"] - shot["start"])))
    cam = shot["camera"]
    if shot.get("inherit"):
        p = 1.0
    z = {"push": 1 + 0.05 * p, "pull": 1.05 - 0.05 * p, "hero": 1 + 0.10 * p,
         "still": 1.0, "pan": 1.03}.get(cam, 1 + 0.05 * p)
    bw, bh = 2112, 1188
    cw, ch = 1920 / z, 1080 / z
    ox = (bw - cw) / 2 + ((-60 + 120 * p) if cam == "pan" else 0)
    oy = (bh - ch) / 2
    return (ox, oy, ox + cw, oy + ch)


def bg_frame(shot, t, fi):
    img = bg_image(shot["bg"])
    frame = img.resize((W, H), Image.BILINEAR, box=camera_box(shot, t))
    if shot.get("bg2"):
        tb = None
        if shot["beats"]:
            tb = phrase_time(shot, shot["beats"][0])
        tb = tb or (shot["start"] + (shot["end"] - shot["start"]) * 0.5)
        k = ease((t - tb) / 1.2)
        if k > 0:
            f2 = bg_image(shot["bg2"]).resize((W, H), Image.BILINEAR, box=camera_box(shot, t))
            frame = Image.blend(frame, f2, k)
    return Image.fromarray(finishing(np.asarray(frame), fi)).convert("RGBA")


# ---------------------------------------------------------------- characters
@lru_cache(None)
def cast_img(role, kind, size=None):
    im = Image.open(CAST / role / f"{kind}.png").convert("RGBA")
    if size:
        im = im.resize(size, Image.LANCZOS)
    return im


ENV = None


def env_load():
    global ENV
    if ENV is not None:
        return
    ENV = {}
    for role in ROLE_COLOR:
        with wave.open(str(ED.w("stems") / f"{role}.wav")) as wf:
            x = np.frombuffer(wf.readframes(wf.getnframes()), np.int16).astype(np.float32) / 32768
            sr = wf.getframerate()
        hop = sr // FPS
        n = len(x) // hop
        e = np.sqrt((x[: n * hop].reshape(n, hop) ** 2).mean(axis=1))
        ENV[role] = np.clip(e / 0.12, 0, 1)


def active_turn(t):
    for tu in TURNS:
        if tu["start"] - 0.3 <= t <= tu["end"] + 0.25:
            return tu
    return None


@lru_cache(None)
def badge_base(role, dim=False, label=None):
    w_, h_ = 470, 124
    im = Image.new("RGBA", (w_, h_), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w_ - 1, h_ - 1], radius=18, fill=C["slate"] + (217,), outline=ROLE_COLOR[role] + (160,), width=2)
    p0 = cast_img(role, "P0", (88, 88))
    im.alpha_composite(p0, (16, 18))
    name, title = ROLE_NAME[role]
    d.text((120, 16), name, font=F_LAB(24), fill=ROLE_COLOR[role] + (255,))
    d.text((120, 46), label or title, font=F_SUB(20), fill=C["muted"] + (255,))
    if dim:
        im = with_alpha(im, 0.55)
    return im


def draw_badge(fr, role, t, fi, x=64, y=56, k=1.0, wave_on=True, label=None, dim=False):
    b = badge_base(role, dim, label).copy()
    if wave_on and not dim:
        env_load()
        e = ENV[role]
        d = ImageDraw.Draw(b)
        for i in range(26):
            j = fi - (25 - i)
            v = float(e[j]) if 0 <= j < len(e) else 0.0
            hh = 3 + int(30 * v)
            xx = 122 + i * 10
            d.rounded_rectangle([xx, 100 - hh // 2 - 4, xx + 5, 100 + hh // 2 - 4], radius=2, fill=ROLE_COLOR[role] + (235,))
    fr.alpha_composite(with_alpha(b, k), (x, y))


def draw_characters(fr, t, fi, shot):
    is_pause_card = shot["template"] == "T10" and not shot["sentences"]
    if is_pause_card or t < INTRO_END - 0.5:
        return
    tu = active_turn(t)
    if shot["flags"]["dual"]:
        for role, x in (("C", 64), ("D", W - 534)):
            on = tu and tu["role"] == role
            draw_badge(fr, role, t, fi, x=x, dim=not on)
    elif tu:
        k = min(ease((t - (tu["start"] - 0.3)) / 0.3), 1 - ease((t - tu["end"] - 0.05) / 0.2))
        slide = int(-440 * (1 - ease((t - (tu["start"] - 0.3)) / 0.3)))
        draw_badge(fr, tu["role"], t, fi, x=64 + slide, k=max(0.0, k))
    for x_ in shot["flags"]["handoff"]:
        for i, r in enumerate(x_.split("+")):
            r = r if r in ROLE_COLOR else {"N": "N1"}.get(r, r)
            if r in ROLE_COLOR:
                draw_badge(fr, r, t, fi, x=W - 534, y=56 + i * 140, dim=True, wave_on=False, label=ED.UI["next"])
    # bust
    for role, a, b, turn_start in BUST_WINS:
        if a - 0.3 <= t <= b + 0.3:
            k = min(ease((t - a) / 0.3), 1 - ease((t - b) / 0.3))
            if k <= 0:
                continue
            p1 = cast_img(role, "P1", (420, 500))
            breathe = 1.0 + 0.006 * (0.5 + 0.5 * math.sin(2 * math.pi * t / 4.0))
            sz = (int(420 * breathe), int(500 * breathe))
            img = p1.resize(sz, Image.BILINEAR)
            # rim flash at sentence starts
            for it in ITEMS:
                if it["role"] == role and 0 <= t - it["start"] < 0.3:
                    glow = img.filter(ImageFilter.GaussianBlur(10))
                    img = Image.alpha_composite(with_alpha(glow, 0.35 * (1 - (t - it["start"]) / 0.3)), img)
                    break
            fr.alpha_composite(with_alpha(img, k), (48 - (sz[0] - 420) // 2, H - sz[1]))
            # first-appearance card
            if turn_start is not None and abs(turn_start - FIRST_TURN.get(role, -99)) < 0.01 and t <= turn_start + 4.0:
                kk = min(ease((t - turn_start) / 0.35), 1 - ease((t - turn_start - 3.6) / 0.4))
                fr.alpha_composite(with_alpha(intro_card(role), kk), (490, H - 250))
            break
    if shot["flags"]["guests"]:
        roles = ["H", "D", "C", "N1", "N2"]
        for i, r in enumerate(roles):
            ti = shot["start"] + 0.5 + i * 0.9
            k = ease((t - ti) / 0.4)
            if k <= 0:
                continue
            p0 = cast_img(r, "P0", (150, 150))
            x = 470 + i * 250
            fr.alpha_composite(with_alpha(p0, k), (x, 300))
            dd = ImageDraw.Draw(fr)
            dd.text((x + 75, 464), ROLE_NAME[r][0], font=F_LAB(18), fill=ROLE_COLOR[r] + (int(255 * k),), anchor="ma")
    wm = watermark()
    fr.alpha_composite(wm, (W - 128, H - 120))


@lru_cache(None)
def intro_card(role):
    name, title = ROLE_NAME[role]
    spec = [(name, F_LAB(34), ROLE_COLOR[role], 6), (title, F_SUB(26), C["text"], 10),
            (ED.UI["intro_line"], F_SUB(22), C["muted"], 0)]
    img = text_block(spec, 700)
    bar = Image.new("RGBA", (img.width + 30, img.height + 10), (0, 0, 0, 0))
    ImageDraw.Draw(bar).rectangle([0, 0, 5, img.height], fill=ROLE_COLOR[role] + (255,))
    bar.alpha_composite(img, (22, 0))
    return bar


@lru_cache(None)
def watermark():
    return Image.open(BRAND / "watermark.png").convert("RGBA")


# ---------------------------------------------------------------- frame
SHOT_ELS = {}


def shot_at(t):
    for i, s in enumerate(SH):
        if s["start"] <= t < s["end"]:
            return i
    return len(SH) - 1 if t >= SH[-1]["start"] else 0


def shot_layer(i, t, fi):
    s = SH[i]
    if i not in SHOT_ELS:
        if len(SHOT_ELS) > 4:
            SHOT_ELS.pop(next(iter(SHOT_ELS)))
        SHOT_ELS[i] = build_elements(s)
    fr = bg_frame(s, t, fi)
    for e in SHOT_ELS[i]:
        e.draw(fr, t)
    return fr


class IntroReader:
    """Streams intro_kenh.mov frame by frame (constant memory, ~6 MB)."""
    def __init__(self):
        self.p, self.idx, self.last = None, -1, None

    def _open(self, start_fi):
        if self.p:
            self.p.kill()
        self.p = subprocess.Popen([str(FF), "-v", "error", "-ss", f"{start_fi / FPS:.3f}",
                                   "-i", str(ED.INTRO_MOV), "-f", "rawvideo",
                                   "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
        self.idx = start_fi - 1

    def get(self, fi):
        if self.p is None or fi <= self.idx - 0 and fi != self.idx or fi > self.idx + 60:
            if not (self.last is not None and fi == self.idx):
                self._open(fi)
        while self.idx < fi:
            buf = self.p.stdout.read(W * H * 3)
            if len(buf) < W * H * 3:                  # past the end: hold the last frame
                break
            self.last = np.frombuffer(buf, np.uint8).reshape(H, W, 3)
            self.idx += 1
        if self.last is None:
            return Image.new("RGBA", (W, H), (0, 0, 0, 255))
        return Image.fromarray(self.last).convert("RGBA")


INTRO = IntroReader()


def intro_frame(fi):
    return INTRO.get(fi)


def render(fi):
    t = fi / FPS
    if t < 20.5:
        return intro_frame(fi)
    i = shot_at(t)
    s = SH[i]
    fr = shot_layer(i, t, fi)
    # transitions
    if i > 0 and s["transition"] == "dissolve" and not s.get("inherit") and t < s["start"] + 0.35:
        prev = shot_layer(i - 1, t, fi)
        fr = Image.blend(prev, fr, ease((t - s["start"]) / 0.35))
    if s["transition"] == "dip" and t < s["start"] + 0.6:
        fr = Image.blend(Image.new("RGBA", (W, H), (0, 0, 0, 255)), fr, ease((t - s["start"]) / 0.6))
    if i + 1 < len(SH) and SH[i + 1]["transition"] == "dip" and t > s["end"] - 0.6:
        fr = Image.blend(fr, Image.new("RGBA", (W, H), (0, 0, 0, 255)), ease((t - (s["end"] - 0.6)) / 0.6))
    if s["id"] == "1-00" and t < 20.5 + 1.9:        # rise out of the intro's black tail
        k = ease((t - 20.5) / 1.9)
        fr = Image.blend(intro_frame(fi), fr, k)
    if i == len(SH) - 1:                           # dòng cuối: mờ ra đen
        fr = Image.blend(fr, Image.new("RGBA", (W, H), (0, 0, 0, 255)), ease((t - s["start"] - 4.0) / 3.0))
    draw_characters(fr, t, fi, s)
    return fr


# ---------------------------------------------------------------- workers
def work(args):
    f0, f1, out = args
    cmd = [str(FF), "-y", "-hide_banner", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libopenh264", "-b:v", "3000k",
           "-maxrate", "5000k", "-bufsize", "8000k", "-pix_fmt", "yuv420p", "-r", str(FPS), str(out)]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for fi in range(f0, f1):
        p.stdin.write(render(fi).convert("RGB").tobytes())
        if (fi - f0) % 600 == 0:
            print(f"  [{out.name}] {fi - f0}/{f1 - f0}", flush=True)
    p.stdin.close()
    return p.wait()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="t0", type=float, default=0.0)
    ap.add_argument("--to", dest="t1", type=float, default=TOTAL)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--out", default=str(ED.w("video3") / "picture.mp4"))
    ap.add_argument("--stills", default="")
    a = ap.parse_args()
    vd = ED.w("video3")
    vd.mkdir(parents=True, exist_ok=True)
    if a.stills:
        sd = vd / "stills"
        sd.mkdir(exist_ok=True)
        by_id = {s["id"]: s for s in SH}
        tokens = [s["id"] for s in SH] if a.stills.strip().lower() == "all" else a.stills.split(",")
        for token in tokens:
            token = token.strip()
            if not token:
                continue
            if token in by_id:
                s = by_id[token]
                t_sec = (s["start"] + s["end"]) / 2
                name = f"shot_{token}.png"
            else:
                t_sec = float(token)
                name = f"t{t_sec:07.1f}.png"
            fi = int(t_sec * FPS)
            render(fi).convert("RGB").save(sd / name)
        print("stills ->", sd)
        return
    f0, f1 = int(a.t0 * FPS), int(a.t1 * FPS)
    n = a.workers
    step = math.ceil((f1 - f0) / n)
    jobs = [(f0 + k * step, min(f1, f0 + (k + 1) * step), vd / f"part_{k:02d}.mp4") for k in range(n)]
    jobs = [j for j in jobs if j[0] < j[1]]
    with Pool(len(jobs)) as pool:
        codes = pool.map(work, jobs)
    if any(codes):
        raise SystemExit(f"worker failed {codes}")
    lst = vd / "parts.txt"
    lst.write_text("".join(f"file '{j[2].as_posix()}'\n" for j in jobs), encoding="utf-8")
    subprocess.run([str(FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-c", "copy", a.out], check=True)
    print("done", a.out)


if __name__ == "__main__":
    main()
