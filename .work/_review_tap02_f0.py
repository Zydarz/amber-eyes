# -*- coding: utf-8 -*-
"""Đo F0 (cao độ) theo vai từ file TTS rời của tập 02 — không lẫn nhạc/SFX.
Dùng tự tương quan (autocorrelation) trên khung 40 ms, lọc 60–400 Hz.
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
AUDIO = WORK / "audio_s_t02"

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
    """Trả về mảng F0 (Hz) cho các khung có năng lượng và tìm được F0 hợp lệ."""
    out = []
    if x is None or len(x) < FRAME * 3:
        return out
    # tiền xử lý: bỏ DC, cửa sổ Hann
    x = x - x.mean()
    win = np.hanning(FRAME).astype(np.float32)
    for i in range(0, len(x) - FRAME, HOP):
        fr = x[i:i + FRAME] * win
        rms = np.sqrt(np.mean(fr ** 2))
        if rms < 0.012:      # khung im
            continue
        ac = np.correlate(fr, fr, mode="full")[FRAME - 1:]
        lo = int(SR / FMAX)
        hi = min(int(SR / FMIN), len(ac) - 1)
        if hi <= lo + 1:
            continue
        seg = ac[lo:hi]
        k = int(np.argmax(seg))
        # parabolic interpolation
        if 0 < k < len(seg) - 1:
            a0, a1, a2 = seg[k - 1], seg[k], seg[k + 1]
            denom = (a0 - 2 * a1 + a2)
            delta = 0.5 * (a0 - a2) / denom if denom != 0 else 0.0
        else:
            delta = 0.0
        lag = lo + k + delta
        if lag <= 0:
            continue
        f = SR / lag
        # buoc nhay so voi mau dau (voiced check don gian)
        if ac[0] > 0 and seg[k] / ac[0] < 0.28:
            continue
        out.append(f)
    return out


tl = json.loads((WORK / "timeline_s_t02.json").read_text(encoding="utf-8"))
items = tl["items"]

per_role = {}
missing = []
for it in items:
    # id "1.03#1" -> element "1.03", so "s1_03_01.mp3"
    el, _, idx = it["id"].partition("#")
    sid = el.replace(".", "_") + "_" + idx.zfill(2)
    p = AUDIO / f"s{sid}.mp3"
    if not p.exists():
        missing.append(it["id"])
        continue
    x = load_mono(p)
    f0s = f0_track(x)
    if not f0s:
        continue
    per_role.setdefault(it["role"], []).extend(f0s)

rows = []
for role, f0s in per_role.items():
    a = np.array(f0s)
    q = np.percentile(a, [5, 25, 50, 75, 95])
    rows.append({
        "role": role,
        "n_frames": len(a),
        "f0_p5": round(float(q[0]), 1),
        "f0_p25": round(float(q[1]), 1),
        "f0_median": round(float(q[2]), 1),
        "f0_p75": round(float(q[3]), 1),
        "f0_p95": round(float(q[4]), 1),
        "f0_spread_semitone_p5_p95": round(12 * np.log2(q[4] / q[0]), 2),
    })

rows.sort(key=lambda r: r["f0_median"])
# khoang cach nua cung giua cac vai
for i in range(1, len(rows)):
    d = 12 * np.log2(rows[i]["f0_median"] / rows[i - 1]["f0_median"])
    rows[i]["sep_semitone_vs_prev"] = round(float(d), 2)

print(json.dumps({"rows": rows, "missing_audio_files": missing[:20],
                  "missing_count": len(missing),
                  "note": "F0 do tren TTS roi (audio_s_t02), khong co nhac nen"},
                 ensure_ascii=False, indent=2))
