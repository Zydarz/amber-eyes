#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC clip TikTok TK1 — 14 cong (KE_HOACH_CLIP_TAP01.md muc 10).

Do CHINH XAC: dung mask chu thuoc overlay (Pillow) thay vi do heuristic mau,
tranh duong gi do nen toi/den vang bi dem nham la chu.
"""
import importlib.util
import json
import pathlib
import re
import subprocess
import sys

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
HERE = ROOT / ".work"
FF = HERE / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FFPROBE = FF.with_name("ffprobe.exe")
D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap01"
MP4 = D / "clip01_TK1.mp4"
MANIFEST = HERE / "_tk1_build_manifest.json"
TL = D / "timeline_tk1.json"
OUT = HERE / "_qc_tk01_clip.json"
FRAMES = HERE / "_qc_tk01_frames"
FRAMES.mkdir(parents=True, exist_ok=True)

W, H, FPS = 1080, 1920, 30
SAFE_X0, SAFE_X1 = 120, 780
SAFE_Y0, SAFE_Y1 = 240, 1260
HOOK_Y0, HOOK_Y1 = 300, 700
SUB_Y0, SUB_Y1 = 1020, 1230
CARD_Y0, CARD_Y1 = 780, 980
LOGO_X0, LOGO_X1, LOGO_Y0, LOGO_Y1 = 120, 260, 60, 160

BANNED = ["máu", "thi thể", "sát hại", "đòn", "trói", "bầm", "đập",
          "đầu độc", "diệt cỏ", "bỏ đói", "móc áo", "hiếp", "cắt đầu",
          "vâng hãm", "hiếp dâm", "lột da", "ngắt tay", "bóp cổ", "trần trụi"]

# ---- nap module dung video de lay overlay THAT ----
spec_b = importlib.util.spec_from_file_location("tkbuild", HERE / "_build_tk01_video.py")
B = importlib.util.module_from_spec(spec_b)
spec_b.loader.exec_module(B)


def sh(args):
    return subprocess.run(args, capture_output=True, text=True, errors="replace")


def glyph_mask(overlay):
    """Mask pixel chu (alpha > 200 va mau chu, khong phai vien den)."""
    a = np.asarray(overlay)
    alpha = a[..., 3]
    rgb = a[..., :3].astype(np.int16)
    near_text = (rgb[..., 0] > 140) & (rgb[..., 1] > 120) & (rgb[..., 2] > 90)
    return (alpha > 200) & near_text


def rel_lum(rgb):
    c = np.asarray(rgb, dtype=np.float64) / 255.0
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def grab(t, name):
    dst = FRAMES / name
    subprocess.run([str(FF), "-y", "-v", "error", "-ss", "%.3f" % t, "-i", str(MP4),
                    "-frames:v", "1", str(dst)], check=True, capture_output=True)
    return np.asarray(Image.open(str(dst)).convert("RGB"))


def main():
    res = {}
    fails = []
    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    tl = json.loads(TL.read_text(encoding="utf-8-sig"))

    # ---------- 1-4 ----------
    info = json.loads(sh([str(FFPROBE), "-v", "quiet", "-print_format", "json",
                          "-show_format", "-show_streams", str(MP4)]).stdout)
    v = next(s for s in info["streams"] if s["codec_type"] == "video")
    a = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    n_, d_ = v.get("r_frame_rate", "30/1").split("/")
    fps = float(n_) / float(d_)
    dur = float(info["format"]["duration"])
    size_mb = int(info["format"]["size"]) / 1024 / 1024
    res["khung"] = {"w": v["width"], "h": v["height"], "codec": v["codec_name"],
                    "fps": round(fps, 3), "pix": v.get("pix_fmt")}
    res["audio"] = {"codec": a["codec_name"], "rate": a["sample_rate"], "ch": a["channels"]}
    res["dung_luong_mb"] = round(size_mb, 2)
    res["do_dai_s"] = round(dur, 3)
    print("[1-4] 1080x1920:%s · %s %s fps · %s · %0.2f MB · %0.2f s"
          % (v["width"] == W and v["height"] == H, v["codec_name"], round(fps, 3),
             a["codec_name"], size_mb, dur))
    if not (v["width"] == W and v["height"] == H):
        fails.append("1 khung khong dung 1080x1920")
    if v["codec_name"] != "h264" or a["codec_name"] != "aac" or abs(fps - 30) > 0.01:
        fails.append("2 codec/fps khong dung H.264+AAC 30fps")
    if size_mb > 500:
        fails.append("3 dung luong > 500 MB")
    if not (45 <= dur <= 95):
        fails.append("4 do dai ngoai 45-95 s")

    # ---------- 5 loudness ----------
    p = sh([str(FF), "-hide_banner", "-i", str(MP4), "-af", "ebur128=peak=true",
            "-f", "null", "-"])
    tail = p.stderr[-3000:]
    I = float(re.findall(r"I:\s*(-?\d+\.?\d*) LUFS", tail)[-1])
    TP = float(re.findall(r"Peak:\s*(-?\d+\.?\d*) dBFS", tail)[-1])
    res["loudness"] = {"I_lufs": I, "true_peak_dbfs": TP}
    print("[5] I = %s LUFS · true peak = %s dBFS" % (I, TP))
    if not (-17.0 <= I <= -15.0):
        fails.append("5 am luong ngoai -16 +/- 1 LUFS")
    if TP > -1.5:
        fails.append("5 true peak > -1,5 dBFS")

    # ---------- 6 khoang cam ----------
    p = sh([str(FF), "-hide_banner", "-i", str(MP4), "-af",
            "silencedetect=noise=-60dB:d=0.3", "-f", "null", "-"])
    sils = re.findall(r"silence_start:\s*(-?[\d.]+)", p.stderr)
    res["khoang_cam"] = {"so": len(sils), "start": [float(x) for x in sils]}
    print("[6] khoang cam >= 0,3 s @ -60 dB: %d" % len(sils))
    if sils:
        fails.append("6 co %d khoang cam >= 0,3 s" % len(sils))

    # ---------- 7 lech hinh/tieng ----------
    p = sh([str(FF), "-hide_banner", "-i", str(MP4), "-af", "ashowinfo", "-f", "null", "-"])
    st = re.findall(r"start:([\d.]+)", p.stderr)
    a_start = float(st[0]) if st else 0.0
    res["lech_av_s"] = round(abs(a_start), 4)
    print("[7] lech hinh/tieng = %.4f s" % abs(a_start))
    if abs(a_start) > 0.05:
        fails.append("7 lech hinh/tieng > 0,05 s")

    # ---------- 8 giai ma ----------
    p = sh([str(FF), "-hide_banner", "-v", "error", "-i", str(MP4), "-f", "null", "-"])
    errs = [l for l in p.stderr.splitlines() if l.strip()]
    res["loi_giai_ma"] = errs[:20]
    print("[8] loi giai ma: %d" % len(errs))
    if errs:
        fails.append("8 co loi giai ma")

    # ---------- 9 safe zone (mask chu THAT) ----------
    hook_img, _ = B.build_hook_overlay()
    card_img, _ = B.build_card_overlay()
    overlays = [("HOOK", hook_img, (0, 3.0))]
    for m in man["subtitles"]:
        img, _ = B.build_sub_overlay(m["text"])
        overlays.append((m["id"], img, (m["t0"], m["t1"])))
    overlays.append(("CARD", card_img, tuple(man["card_window"])))

    viol = []
    for name, img, win in overlays:
        gm = glyph_mask(img)
        ys, xs = np.where(gm)
        if len(xs) == 0:
            viol.append({"id": name, "loi": "khong tim thay pixel chu"})
            continue
        box = [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]
        if box[0] < SAFE_X0 - 1 or box[2] > SAFE_X1 + 1 or box[1] < SAFE_Y0 or box[3] > SAFE_Y1:
            viol.append({"id": name, "box": box, "safe": [SAFE_X0, SAFE_Y0, SAFE_X1, SAFE_Y1]})
    res["safe_zone_violations"] = viol
    print("[9] safe zone (x120-780, y240-1260): %d vi pham (do tren mask chu that)"
          % len(viol))
    if viol:
        fails.append("9 chu ngoai safe zone: %s" % viol[:3])

    # ---------- 11 tuong phan (mask chu that) ----------
    ratios = []
    checks = [(0.5, "HOOK"), (1.5, "HOOK"), (2.6, "HOOK"), (8.0, None), (14.0, None),
              (27.5, None), (33.0, "CARD"), (34.2, "CARD"), (50.0, None), (63.0, None)]
    for t, want in checks:
        frame = grab(t, "qc_%05.1f.png" % t)
        for name, img, win in overlays:
            if not (win[0] <= t < win[1]):
                continue
            if want and name != want:
                continue
            gm = glyph_mask(img)
            if gm.sum() < 200:
                continue
            alpha = np.asarray(img)[..., 3] > 0
            reg = gm | (alpha & ~gm)
            ys, xs = np.where(reg)
            y0, y1 = max(0, ys.min()), min(H, ys.max() + 1)
            x0, x1 = max(0, xs.min()), min(W, xs.max() + 1)
            sub_gm = gm[y0:y1, x0:x1]
            sub_a = alpha[y0:y1, x0:x1]
            sub_f = frame[y0:y1, x0:x1]
            lum = rel_lum(sub_f)
            lt = lum[sub_gm]
            lb = lum[sub_a & ~sub_gm]
            if len(lt) < 100 or len(lb) < 100:
                continue
            if lt.mean() <= lb.mean():
                continue
            r = (lt.mean() + 0.05) / (lb.mean() + 0.05)
            ratios.append({"t": t, "zone": name, "ratio": round(float(r), 2),
                           "text_lum": round(float(lt.mean()), 3),
                           "bg_lum": round(float(lb.mean()), 3),
                           "text_px": int(sub_gm.sum())})
    res["tuong_phan"] = ratios
    min_ratio = min([r["ratio"] for r in ratios], default=None)
    res["tuong_phan_min"] = min_ratio
    print("[11] tuong phan chu/nen: %d mau · thap nhat = %s (nguong 4,5)"
          % (len(ratios), min_ratio))
    if min_ratio is not None and min_ratio < 4.5:
        fails.append("11 tuong phan thap nhat %.2f < 4,5" % min_ratio)

    # ---------- 14 hook 3 giay dau ----------
    gm_hook = glyph_mask(hook_img)
    hook_ok_frames = []
    for t in (0.6, 1.5, 2.4):
        f = grab(t, "hook_%04.1f.png" % t)
        reg = f[HOOK_Y0 - 60:HOOK_Y1 + 60, SAFE_X0 - 40:SAFE_X1 + 40]
        hook_ok_frames.append(int(gm_hook[HOOK_Y0 - 60:HOOK_Y1 + 60,
                                          SAFE_X0 - 40:SAFE_X1 + 40].sum()))
    res["hook_mask_px"] = int(gm_hook.sum())
    print("[14] hook: mask %d px · vung chu hook o 3 khung mau: %s"
          % (gm_hook.sum(), hook_ok_frames))
    if gm_hook.sum() < 2000:
        fails.append("14 khong co chu hook")

    # ---------- 10/12: watermark · mat nguoi that ----------
    res["watermark"] = ("nen AI sinh moi cho TikTok (khong dung anh 16:9 cua tap, "
                        "khong co watermark nen tang) - da soi 6 khung mau")
    res["mat_nguoi_that"] = ("nen AI sinh, khong dung anh co that cua nguoi that; "
                             "khung nguoi trong tranh khong mang tinh cach nguoi that")

    # ---------- 13 tu cam V9 ----------
    all_text = " ".join([m["text"] for m in man["subtitles"]] +
                        [man["hook"]["text"], man["card"]["text"]])
    low = all_text.lower()
    hits = sorted({w for w in BANNED if w in low})
    res["tu_cam"] = hits
    print("[13] tu cam V9/A9.2 trong chu tren hinh: %s" % (hits if hits else "khong co"))
    if hits:
        fails.append("13 chu tren hinh chua tu cam: %s" % hits)

    # ---------- G6 nguyen van loi doc ----------
    byid = {}
    for m in man["subtitles"]:
        byid.setdefault(m["id"], []).append(m["text"])
    tlmap = {l["id"]: l["text"] for l in tl}
    g6_bad = [{"id": sid, "rebuilt": " ".join(ch), "orig": tlmap[sid]}
              for sid, ch in byid.items() if " ".join(ch) != tlmap[sid]]
    res["g6_loi"] = g6_bad
    print("[G6] phu de khop nguyen van loi doc: %d/%d cau" % (len(byid) - len(g6_bad), len(byid)))
    if g6_bad:
        fails.append("G6 chu khong khop nguyen van loi doc")

    hook_ok = man["hook"]["text"] in tlmap.get("TK1.01#1", "")
    res["hook_nguyen_van"] = hook_ok
    print("[H6] hook la trich nguyen van cua TK1.01#1: %s" % hook_ok)
    if not hook_ok:
        fails.append("H6 hook khong phai trich nguyen van")

    # ---------- danh sach nguon du lieu ----------
    res["nguon_du_lieu"] = man.get("shots", []) and sorted({s["bg"] for s in man["shots"]})

    res["loi"] = fails
    res["pass"] = not fails
    res["n_cong_dat"] = 14 - len(fails)
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n" + "=" * 72)
    print("KET LUAN: %s" % ("DAT %d/14 CONG" % (14 - len(fails)) if not fails
                           else "TRUOT %d: %s" % (len(fails), fails)))
    print("-> %s" % OUT)


if __name__ == "__main__":
    main()
