#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh .work/stems_JA_t02/{H,D,C,N1,N2}.wav từ master audio JA Tap02.

Vai trò: build_video3 dùng envelope RMS của stem theo vai để vẽ badge "đang nói".
Stem = 16 kHz mono int16, giữ đúng trục thời gian của tập (câu rỗng = im lặng).
"""
import json
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

EPN = "02"
MASTER = ROOT / f"02_SAN_XUAT/Tap{EPN}_JA/xuat_ban/Tap{EPN}_JA_master.mp3"
TL = W / f"timeline_s_JA_t{EPN}.json"
OUT = W / f"stems_JA_t{EPN}"
SR = 16000

tl = json.loads(TL.read_text(encoding="utf-8-sig"))
total = float(tl["total"])
items = tl["items"]
print(f"master = {MASTER.name} · total = {total:.2f} s · {len(items)} câu")

raw = subprocess.run([str(FF), "-v", "error", "-i", str(MASTER),
                      "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                     capture_output=True).stdout
x = np.frombuffer(raw, dtype=np.float32).astype(np.float64)
print(f"giải mã {len(x)} mẫu = {len(x)/SR:.2f} s")

OUT.mkdir(parents=True, exist_ok=True)
N = int(total * SR) + SR
roles = ("H", "D", "C", "N1", "N2")
stems = {r: np.zeros(N, dtype=np.float64) for r in roles}
missing = []
for it in items:
    r = it.get("role")
    if r not in stems:
        missing.append((it["id"], r))
        continue
    a = int(round(it["start"] * SR))
    b = int(round(it["end"] * SR))
    seg = x[a:b]
    if len(seg) == 0:
        continue
    stems[r][a:a + len(seg)] = seg

if missing:
    print("CAU THIEU ROLE:", missing[:10])

for r, s in stems.items():
    peak = float(np.abs(s).max())
    rms = float(np.sqrt(np.mean(s ** 2)))
    out = (np.clip(s, -1, 1) * 32767).astype(np.int16)
    with wave.open(str(OUT / f"{r}.wav"), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SR)
        wf.writeframes(out.tobytes())
    print(f"  {r}.wav · peak {20*np.log10(peak+1e-12):.1f} dBFS · rms {20*np.log10(rms+1e-12):.1f} dBFS")
print("xong ->", OUT)
