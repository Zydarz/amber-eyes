# -*- coding: utf-8 -*-
"""C: Dem so 'nguoi' (nhom F0) trong 1 file audio: cat doan tieng noi theo khoang im,
do F0 trung viet tung doan, roi gom theo nua cung.
Dung cho file THU GIONG (nhieu ung vien doc) de biet co bao nhieu giong rieng.
"""
import subprocess
import sys
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:\TEST\Gax\Audi")
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

SR = 16000
FRAME = int(0.04 * SR)
HOP = int(0.01 * SR)
FMIN, FMAX = 60.0, 400.0


def load_mono(p):
    r = subprocess.run([str(FF), "-v", "error", "-i", str(p), "-ac", "1", "-ar", str(SR),
                        "-f", "s16le", "-"], capture_output=True)
    if not r.stdout:
        return None
    return np.frombuffer(r.stdout, dtype=np.int16).astype(np.float32) / 32768.0


def f0_track(x):
    out = []
    for i in range(0, max(0, len(x) - FRAME), HOP):
        fr = x[i:i + FRAME]
        if len(fr) < FRAME:
            break
        fr = fr - fr.mean()
        rms = float(np.sqrt(np.mean(fr ** 2)))
        if rms < 0.010:
            out.append((0.0, rms))
            continue
        win = np.hanning(FRAME).astype(np.float32)
        frw = fr * win
        ac = np.correlate(frw, frw, mode="full")[FRAME - 1:]
        lo = int(SR / FMAX)
        hi = min(int(SR / FMIN), len(ac) - 1)
        if hi <= lo + 1:
            out.append((0.0, rms))
            continue
        seg = ac[lo:hi]
        k = int(np.argmax(seg))
        f = SR / (lo + k)
        ok = ac[0] > 0 and seg[k] / ac[0] >= 0.30 and FMIN <= f <= FMAX
        out.append((f if ok else 0.0, rms))
    return out


def segments(path):
    x = load_mono(path)
    if x is None:
        print("  khong doc duoc:", path)
        return
    tr = f0_track(x)
    segs, cur, gap = [], [], 0
    for f, rms in tr:
        if f > 0:
            cur.append(f)
            gap = 0
        else:
            gap += 1
            if cur and gap >= 40:          # 0.4 s im -> het doan
                segs.append(cur)
                cur = []
            elif gap >= 40:
                cur = []
    if cur:
        segs.append(cur)
    segs = [s for s in segs if len(s) >= 25]     # bo qua doan qua ngan
    dur = len(x) / SR
    print(f"  file: {path.name}   ({dur:.1f} s)   so doan tieng noi: {len(segs)}")
    rows = []
    for s in segs:
        a = np.array(s)
        rows.append((float(np.median(a)), len(s) * HOP / SR))
    # gom cac doan lien ke co F0 gan nhau (cua 1 nguoi)
    groups = []
    for med, d in rows:
        if groups and 12 * np.log2(med / groups[-1]["med"]) < 2.0:
            g = groups[-1]
            g["f0s"].append(med)
            g["dur"] += d
            g["med"] = float(np.median(g["f0s"]))
        else:
            groups.append({"med": med, "dur": d, "f0s": [med]})
    groups.sort(key=lambda g: -g["dur"])
    print(f"  -> so nhom giong (nua cung <2): {len(groups)}")
    for g in groups:
        tag = "NAM" if g["med"] < 165 else ("NUA" if g["med"] < 200 else "NU")
        print(f"     F0 {g['med']:6.1f} Hz  ({tag:3s})   tong {g['dur']:5.1f} s")


for p in [ROOT / "90_LUU_TRU" / "thu_giong" / "so_sanh_5_giong.mp3",
          ROOT / "90_LUU_TRU" / "thu_giong" / "so_sanh_giong_nu" / "so_sanh_giong_nu.mp3"]:
    if p.exists():
        segments(p)
        print()
