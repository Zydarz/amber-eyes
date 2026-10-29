# -*- coding: utf-8 -*-
"""E: Do cac nhom giong (F0) tren MASTER da phat (co nhac/SFX) + bang vai->giong chuan hoa.
Gender suy ra tu F0 trung viet, KHONG tu ten giong (ten giong de sai: 'female' chua 'male')."""
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:\TEST\Gax\Audi")
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


def frames_f0(x):
    out = []
    win = np.hanning(FRAME).astype(np.float32)
    for i in range(0, max(0, len(x) - FRAME), HOP):
        fr = x[i:i + FRAME]
        if len(fr) < FRAME:
            break
        fr = fr - fr.mean()
        if np.sqrt(np.mean(fr ** 2)) < 0.018:
            out.append(0.0)
            continue
        frw = fr * win
        ac = np.correlate(frw, frw, mode="full")[FRAME - 1:]
        lo = int(SR / FMAX)
        hi = min(int(SR / FMIN), len(ac) - 1)
        seg = ac[lo:hi]
        k = int(np.argmax(seg))
        f = SR / (lo + k)
        ok = ac[0] > 0 and seg[k] / ac[0] >= 0.32 and FMIN <= f <= FMAX
        out.append(f if ok else 0.0)
    return out


def bands(path, label):
    x = load_mono(path)
    if x is None:
        print("  khong doc duoc:", path)
        return
    fs = frames_f0(x)
    # nhom cac khung lien tiep cung F0 (chuyen nghiep)
    groups = []
    for f in fs:
        if f <= 0:
            continue
        if groups and abs(12 * np.log2(f / groups[-1]["med"])) < 1.8:
            g = groups[-1]
            g["f0s"].append(f)
            g["med"] = float(np.median(g["f0s"]))
        else:
            groups.append({"med": f, "f0s": [f]})
    groups = [g for g in groups if len(g["f0s"]) >= 40]   # >= 0.4 s
    groups.sort(key=lambda g: -len(g["f0s"]))
    print(f"  {label}")
    print(f"    nhom giong: {len(groups)}")
    for g in groups[:8]:
        med = g["med"]
        tag = "NAM" if med < 165 else ("NUA" if med < 195 else "NU")
        print(f"      F0 {med:6.1f} Hz  ({tag})   {len(g['f0s'])*HOP/SR:6.1f} s")


for path, label in [
    (ROOT / "02_SAN_XUAT" / "Tap03" / "xuat_ban" / "Tap03_master.mp3", "Tap03_master.mp3 (bo A, VN)"),
    (WORK / "_cu" / "Tap01_master.cu.mp3", "Tap01_master.cu.mp3 (bo cu, VN)"),
]:
    if path.exists():
        bands(path, label)
        print()

# ---- bang chuan hoa vai -> giong -> F0 do duoc (tu file TTS roi, khong nhac) ----
print("########## BANG VAI -> GIONG (do F0 tren file TTS roi) ##########")
print("  (Tap01 = bo giong cu | Tap02+ = bo A)")
rows = [
    ("Tập 01", "Host", "audiobook_male_1", 114.3, "audiobook_male_1", "NAM"),
    ("Tập 01", "Điều tra viên", "male-qn-qingse", 136.8, "male-qn-qingse", "NAM"),
    ("Tập 01", "Chuyên gia", "audiobook_female_1", 230.2, "audiobook_female_1", "NU"),
    ("Tập 01", "N1", "Vietnamese_kindhearted_girl", 250.0, "Vietnamese_kindhearted_girl", "NU"),
    ("Tập 01", "N2", "English_captivating_female1", 231.9, "English_captivating_female1", "NU"),
    ("Tập 02+", "Host", "English_CaptivatingStoryteller", 102.6, "English_CaptivatingStoryteller", "NAM"),
    ("Tập 02+", "Điều tra viên", "Korean_ColdYoungMan", 140.4, "Korean_ColdYoungMan", "NAM"),
    ("Tập 02+", "Chuyên gia", "English_AssertiveQueen", 207.8, "English_AssertiveQueen", "NU"),
    ("Tập 02+", "N1", "Vietnamese_kindhearted_girl", 248.1, "Vietnamese_kindhearted_girl", "NU"),
    ("Tập 02+", "N2", "English_captivating_female1", 230.3, "English_captivating_female1", "NU"),
]
for ep, role, vid, f0, _, g in rows:
    lang = vid.split("_")[0] if "_" in vid else "(legacy)"
    print(f"  {ep:8s} {role:15s} {vid:32s} lang-goc={lang:22s} F0 {f0:6.1f} Hz  -> {g}")
