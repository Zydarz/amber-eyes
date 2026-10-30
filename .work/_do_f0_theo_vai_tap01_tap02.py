# -*- coding: utf-8 -*-
"""B: Do F0 (cao độ) theo vai tren file TTS ROI cua Tap01 va Tap02 — khong nhac/SFX.
Tu vay do, dung file TTS roi + manifest (nguon su that), khong dung master da mix.
"""
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

SR = 16000
FRAME = int(0.04 * SR)
HOP = int(0.01 * SR)
FMIN, FMAX = 60.0, 400.0
ROLE_VN = {"H": "Host", "D": "Dieu tra vien", "C": "Chuyen gia", "N1": "N1", "N2": "N2"}


def load_mono(p):
    r = subprocess.run([str(FF), "-v", "error", "-i", str(p), "-ac", "1", "-ar", str(SR),
                        "-f", "s16le", "-"], capture_output=True)
    if not r.stdout:
        return None
    return np.frombuffer(r.stdout, dtype=np.int16).astype(np.float32) / 32768.0


def f0_track(x):
    out = []
    if x is None or len(x) < FRAME * 3:
        return out
    x = x - x.mean()
    win = np.hanning(FRAME).astype(np.float32)
    for i in range(0, len(x) - FRAME, HOP):
        fr = x[i:i + FRAME] * win
        if np.sqrt(np.mean(fr ** 2)) < 0.012:
            continue
        ac = np.correlate(fr, fr, mode="full")[FRAME - 1:]
        lo = int(SR / FMAX)
        hi = min(int(SR / FMIN), len(ac) - 1)
        if hi <= lo + 1:
            continue
        seg = ac[lo:hi]
        k = int(np.argmax(seg))
        lag = lo + k
        if lag <= 0:
            continue
        f = SR / lag
        if ac[0] > 0 and seg[k] / ac[0] < 0.28:
            continue
        out.append(f)
    return out


def fname(sid):
    ma, k = sid.split("#")
    a, b = ma.split(".")
    return f"s{a}_{b}_{int(k):02d}.mp3"


live = json.loads((WORK / "_voice_list_live_20261027.json").read_text(encoding="utf-8-sig"))
names = {v["voice_id"]: v["voice_name"] for v in live["available_voices"]}

for ep, man, audio in [("Tap01", "tts_manifest.json", "audio_s"),
                       ("Tap02", "tts_manifest_t02.json", "audio_s_t02")]:
    items = json.loads((WORK / man).read_text(encoding="utf-8"))
    per = defaultdict(list)
    nfile = 0
    for it in items:
        p = WORK / audio / fname(it["id"])
        if not p.exists():
            continue
        f0s = f0_track(load_mono(p))
        if not f0s:
            continue
        nfile += 1
        per[it["role"]].append((np.median(f0s), it["voice"]))
    print(f"===== {ep} · do tren {nfile}/{len(items)} file TTS roi ({audio}/) =====")
    rows = []
    for role, vals in per.items():
        a = np.array([v[0] for v in vals])
        vid = max(set(v[1] for v in vals), key=lambda x: sum(1 for v in vals if v[1] == x))
        rows.append((float(np.median(a)), role, vid, len(a), float(np.percentile(a, 5)), float(np.percentile(a, 95))))
    rows.sort()
    prev = None
    for med, role, vid, n, p5, p95 in rows:
        sep = "" if prev is None else f"  | cach vai truoc {12*np.log2(med/prev):+.1f} nua cung"
        prev = med
        nm = names.get(vid, "<<khong co trong catalog live>>")
        print(f"  {ROLE_VN.get(role, role):15s} F0 trung viet {med:6.1f} Hz  (p5 {p5:5.1f} / p95 {p95:5.1f})"
              f"  n={n:3d}  voice_id={vid}  ({nm}){sep}")
    print()
