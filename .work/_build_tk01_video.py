#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dung video clip TikTok TK1 9:16 (1080x1920, 30 fps) tu:
  - nen doc 1080x1920 san xuat (assets/bg/tk01_<nen>.png)
  - chu Pillow ve (H6: chu = nguyen van loi doc) + scrim (H9)
  - camera move pull/push/pan/still theo SPEC
  - logo goc duoi x120-260 y60-160

Output: .work/_tk1_video_nosound.mp4 + .work/_tk1_build_manifest.json
"""
import json
import pathlib
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
HERE = ROOT / ".work"
FF = HERE / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FONTDIR = pathlib.Path("C:/Windows/Fonts")
F_BOLD = FONTDIR / "segoeuib.ttf"
F_SEMI = FONTDIR / "seguisb.ttf"
F_REG = FONTDIR / "segoeui.ttf"

W, H, FPS = 1080, 1920, 30
D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap01"
TL = D / "timeline_tk1.json"
SPEC = D / "SPEC_AUDIO_CLIP_TAP01.json"
BG = ROOT / "assets" / "bg"
LOGO = ROOT / "assets" / "brand" / "logo.png"
OUT = HERE / "_tk1_video_nosound.mp4"
MANIFEST = HERE / "_tk1_build_manifest.json"

# ---- bo cuc (KE_HOACH_CLIP_TAP01.md muc 4) ----
SX0, SX1 = 120, 780              # vung chu an toan
HOOK_Y0, HOOK_Y1 = 300, 700
SUB_Y0, SUB_Y1 = 1020, 1230
CARD_Y0, CARD_Y1 = 780, 980
LOGO_X0, LOGO_X1, LOGO_Y0, LOGO_Y1 = 120, 260, 60, 160

C_TEXT = (242, 239, 233, 255)   # #F2EFE9
C_HOOK = (255, 214, 140, 255)   # #FFD68C
C_CARD = (255, 214, 140, 255)

HOOK_TEXT = "cô ấy bước vào phòng thẩm vấn"   # nguyen van trong TK1.01#1
HOOK_END = 3.0
CARD_TEXT = "THỦ ĐOẠN (MODUS OPERANDI) ≠ CHỮ KÝ TÂM LÝ (SIGNATURE)"
CARD_DUR = 2.5
CARD_FADE = 0.4
CHUNK_TARGET = 2.6              # giay/chunk phu de


def font(path, size):
    return ImageFont.truetype(str(path), size)


def wrap(words, fnt, maxw):
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if fnt.getlength(t) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_lines(words, path, sizes, maxw, max_lines):
    """Chu toi da: giam co chu cho den khi vua <= max_lines dong."""
    for s in sizes:
        f = font(path, s)
        ls = wrap(words, f, maxw)
        if len(ls) <= max_lines:
            return f, ls, s
    f = font(path, sizes[-1])
    return f, wrap(words, f, maxw), sizes[-1]


def scrim_band(y0, y1, alpha=150, feather=90):
    """Lop toi MEM phu kin CHI_DOC chu de chu khong 'chim' (H9).
    Tran het chieu rong (x 0..1080) de khong thay canh doc cua vung toi."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    for y in range(max(0, y0 - feather), min(H, y1 + feather)):
        if y < y0:
            k = (y - (y0 - feather)) / max(feather, 1)
        elif y > y1:
            k = ((y1 + feather) - y) / max(feather, 1)
        else:
            k = 1.0
        k = max(0.0, min(1.0, k))
        a = int(alpha * k)          # ramp ve 0 het (truoc day la 0,35 -> thay canh nhin thay)
        if a > 0:
            d.rectangle([0, y, W, y], fill=(0, 0, 0, a))
    return lay


def draw_text_block(d, lines, fnt, y_top, color, stroke=3):
    lh = int(fnt.size * 1.30)
    y = y_top
    for ln in lines:
        d.text((SX0, y), ln, font=fnt, fill=color,
               stroke_width=stroke, stroke_fill=(0, 0, 0, 235))
        y += lh
    return y


def build_sub_overlay(text, size=52, scrim_alpha=150):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lay.alpha_composite(scrim_band(SUB_Y0 - 24, SUB_Y1 + 24, alpha=scrim_alpha))
    d = ImageDraw.Draw(lay)
    words = text.split()
    f, lines, s = fit_lines(words, F_SEMI, [size, 50, 48, 46, 44], SX1 - SX0, 2)
    lh = int(f.size * 1.30)
    total = lh * len(lines)
    y = SUB_Y0 + ((SUB_Y1 - SUB_Y0) - total) // 2
    draw_text_block(d, lines, f, y, C_TEXT, stroke=3)
    return lay, {"text": text, "lines": lines, "size": s,
                 "box": [SX0, y, SX0 + max(f.getlength(l) for l in lines), y + total]}


def build_hook_overlay():
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lay.alpha_composite(scrim_band(HOOK_Y0 - 30, HOOK_Y1 + 30, alpha=140))
    d = ImageDraw.Draw(lay)
    words = HOOK_TEXT.split()
    f, lines, s = fit_lines(words, F_BOLD, [76, 72, 68, 64, 60], SX1 - SX0, 2)
    lh = int(f.size * 1.26)
    total = lh * len(lines)
    y = HOOK_Y0 + ((HOOK_Y1 - HOOK_Y0) - total) // 2
    draw_text_block(d, lines, f, y, C_HOOK, stroke=4)
    return lay, {"text": HOOK_TEXT, "lines": lines, "size": s,
                 "box": [SX0, y, SX0 + max(f.getlength(l) for l in lines), y + total]}


def build_card_overlay():
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    words = CARD_TEXT.split()
    f, lines, s = fit_lines(words, F_BOLD, [44, 42, 40, 38, 36], SX1 - SX0 - 60, 3)
    lh = int(f.size * 1.26)
    total = lh * len(lines)
    y = CARD_Y0 + ((CARD_Y1 - CARD_Y0) - total) // 2
    d.rounded_rectangle([SX0, CARD_Y0, SX1, CARD_Y1], radius=12,
                        fill=(10, 10, 14, 153), outline=(255, 214, 140, 120), width=2)
    yy = y
    for ln in lines:
        d.text((SX0 + 30, yy), ln, font=f, fill=C_CARD,
               stroke_width=2, stroke_fill=(0, 0, 0, 220))
        yy += lh
    return lay, {"text": CARD_TEXT, "lines": lines, "size": s,
                 "box": [SX0, CARD_Y0, SX1, CARD_Y1]}


def build_logo():
    im = Image.open(str(LOGO)).convert("RGBA")
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    box_w = LOGO_X1 - LOGO_X0
    box_h = LOGO_Y1 - LOGO_Y0
    sc = min(box_w / im.width, box_h / im.height)
    im = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))), Image.LANCZOS)
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lay.alpha_composite(im, (LOGO_X0 + (box_w - im.width) // 2,
                             LOGO_Y0 + (box_h - im.height) // 2))
    return lay


def camera_box(cam, p, W0, H0):
    z = {"push": 1.0 + 0.05 * p, "pull": 1.05 - 0.05 * p,
         "pan": 1.03, "still": 1.0}.get(cam, 1.0 + 0.05 * p)
    cw, ch = W0 / z, H0 / z
    ox = (W0 - cw) / 2 + ((-60 + 120 * p) if cam == "pan" else 0)
    oy = (H0 - ch) / 2
    # clamp trong khung (Pillow khong cho phep box am)
    ox = max(0.0, min(ox, W0 - cw))
    oy = max(0.0, min(oy, H0 - ch))
    return (ox, oy, ox + cw, oy + ch)


def apply_overlay(frame, overlay, box):
    """Ghep overlay theo VUNG (nhanh hon ca khung) - box = (x0,y0,x1,y1)."""
    x0, y0, x1, y1 = box
    x0 = max(0, x0)
    y0 = max(0, y0)
    x1 = min(frame.width, x1)
    y1 = min(frame.height, y1)
    if x1 <= x0 or y1 <= y0:
        return
    reg = frame.crop((x0, y0, x1, y1)).convert("RGBA")
    reg.alpha_composite(overlay.crop((x0, y0, x1, y1)))
    frame.paste(reg.convert("RGB"), (x0, y0))


def main():
    tl = json.loads(TL.read_text(encoding="utf-8-sig"))
    spec = json.loads(SPEC.read_text(encoding="utf-8-sig"))
    clip = next(c for c in spec["clips"] if c["id"] == "TK1")
    lines_spec = {l["id"]: l for l in clip["lines"]}

    total_s = tl[-1]["end"]
    nframes = int(round(total_s * FPS))

    # ---------- nen ----------
    bgs = {}
    for l in tl:
        name = lines_spec[l["id"]]["nen"]
        p = BG / ("tk01_%s.png" % name)
        if name not in bgs:
            if not p.exists():
                raise SystemExit("THIEU NEN: %s" % p)
            im = Image.open(str(p)).convert("RGB").resize((int(W * 1.12), int(H * 1.12)),
                                                           Image.LANCZOS)
            bgs[name] = im
    print("  nen dung: %d anh" % len(bgs))

    # ---------- overlay chu ----------
    hook_img, hook_meta = build_hook_overlay()
    card_img, card_meta = build_card_overlay()
    logo_img = build_logo()

    sub_imgs = []
    for l in tl:
        dur = l["end"] - l["start"]
        words = l["text"].split()
        nch = max(1, int(round(dur / CHUNK_TARGET)))
        # chia tu theo so tu (uoc luong nhip doc deu)
        per = len(words) / nch
        groups, i = [], 0
        for k in range(nch):
            j = len(words) if k == nch - 1 else min(len(words), int(round(per * (k + 1))))
            groups.append(words[i:j])
            i = j
        if not groups or not groups[-1]:
            groups = [words]
            nch = 1
        for k, g in enumerate(groups):
            if not g:
                continue
            t0 = l["start"] + dur * k / nch
            t1 = l["start"] + dur * (k + 1) / nch
            img, meta = build_sub_overlay(" ".join(g))
            meta.update({"id": l["id"], "t0": round(t0, 3), "t1": round(t1, 3),
                         "words": len(g)})
            sub_imgs.append((t0, t1, img, meta))
    print("  phu de: %d chunk" % len(sub_imgs))

    card_start = None
    for l in tl:
        if l["id"] == "TK1.01#6":
            card_start = l["end"] + l["pause"]
    card_end = card_start + CARD_DUR

    # ---------- render ----------
    cmd = [str(FF), "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", "%dx%d" % (W, H), "-r", str(FPS), "-i", "-",
           "-c:v", "libopenh264", "-b:v", "6000k", "-maxrate", "9000k", "-bufsize", "12000k",
           "-pix_fmt", "yuv420p", "-r", str(FPS), "-movflags", "+faststart", str(OUT)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    shots = []
    for l in tl:
        s = lines_spec[l["id"]]
        shots.append({"id": l["id"], "bg": s["nen"], "cam": s["chuyen_dong"],
                      "start": l["start"], "end": l["end"]})
    SUB_REGION = (0, SUB_Y0 - 24 - 90, W, SUB_Y1 + 24 + 90)
    HOOK_REGION = (0, HOOK_Y0 - 30 - 90, W, HOOK_Y1 + 30 + 90)
    CARD_REGION = (SX0 - 6, CARD_Y0 - 6, SX1 + 6, CARD_Y1 + 6)
    LOGO_REGION = (LOGO_X0, LOGO_Y0, LOGO_X1, LOGO_Y1)
    for fi in range(nframes):
        t = fi / FPS
        # shot hien tai
        shot = shots[0]
        for s in shots:
            if t >= s["start"]:
                shot = s
            else:
                break
        p = 0.0 if shot["end"] <= shot["start"] else \
            max(0.0, min(1.0, (t - shot["start"]) / (shot["end"] - shot["start"])))
        img = bgs[shot["bg"]]
        box = camera_box(shot["cam"], p, img.width, img.height)
        frame = img.resize((W, H), Image.BILINEAR, box=box)

        # phu de
        for t0, t1, simg, meta in sub_imgs:
            if t0 <= t < t1:
                apply_overlay(frame, simg, SUB_REGION)
                break
        # hook 0-3 s
        if t < HOOK_END:
            f = 1.0
            if t < 0.15:
                f = t / 0.15
            elif t > HOOK_END - 0.3:
                f = max(0.0, (HOOK_END - t) / 0.3)
            if f > 0.01:
                ov = hook_img.copy()
                ov.putalpha(ov.getchannel("A").point(lambda v, ff=f: int(v * ff)))
                apply_overlay(frame, ov, HOOK_REGION)
        # the overlay card
        if card_start is not None and card_start <= t < card_end + CARD_FADE:
            f = 1.0
            if t < card_start + 0.2:
                f = (t - card_start) / 0.2
            elif t > card_end:
                f = max(0.0, (card_end + CARD_FADE - t) / CARD_FADE)
            if f > 0.01:
                ov = card_img.copy()
                ov.putalpha(ov.getchannel("A").point(lambda v, ff=f: int(v * ff)))
                apply_overlay(frame, ov, CARD_REGION)
        # logo
        apply_overlay(frame, logo_img, LOGO_REGION)

        proc.stdin.write(frame.tobytes())
        if fi % 300 == 0:
            print("   frame %d/%d (t=%.1fs)" % (fi, nframes, t), flush=True)
    proc.stdin.close()
    proc.wait()
    print("  -> %s" % OUT)

    manifest = {"clip": "TK1", "fps": FPS, "size": [W, H],
                "duration_s": total_s, "nframes": nframes,
                "safe_zone": {"x": [SX0, SX1], "y": [240, 1260]},
                "hook": hook_meta, "card": card_meta,
                "card_window": [card_start, card_end],
                "logo_box": [LOGO_X0, LOGO_Y0, LOGO_X1, LOGO_Y1],
                "subtitles": [{"id": m["id"], "t0": m["t0"], "t1": m["t1"],
                               "text": m["text"], "size": m["size"],
                               "box": m["box"]} for _, _, _, m in sub_imgs],
                "shots": shots}
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print("  -> %s" % MANIFEST)


if __name__ == "__main__":
    main()
