#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap03 VN — dựng 5 stem giọng (H,D,C,N1,N2) từ master mp3 + timeline đo được.

Mục đích: sóng âm trên badge vai trong ảnh tĩnh/video.
Nếu thiếu stem, ảnh VẪN render được nhưng KHÔNG có sóng (bẫy đã gặp 05/11).
"""
import json
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe"
AUDIO_MASTER = ROOT / "02_SAN_XUAT/Tap03/xuat_ban/Tap03_master.mp3"
TL_PATH = WORK / "timeline_s_t03.json"
OUT_DIR = WORK / "stems_t03"
SR = 16000

tl = json.loads(TL_PATH.read_text(encoding="utf-8"))
total = float(tl["total"])
items = tl["items"]
print(f"Master : {AUDIO_MASTER.name}")
print(f"Timeline total = {total:.3f}s | sentences = {len(items)}")

raw = subprocess.run([
    str(FF), "-v", "error", "-i", str(AUDIO_MASTER),
    "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"
], capture_output=True, check=True).stdout
x = np.frombuffer(raw, dtype=np.float32)
print(f"decoded {len(x)/SR:.3f}s")

OUT_DIR.mkdir(parents=True, exist_ok=True)
N = int(total * SR) + SR
roles = ("H", "D", "C", "N1", "N2")
stems = {r: np.zeros(N, dtype=np.float32) for r in roles}
n_missing = 0
for it in items:
    r = it.get("role")
    if r not in stems:
        n_missing += 1
        continue
    a = int(round(it["start"] * SR))
    b = int(round(it["end"] * SR))
    seg = x[a:b]
    if len(seg):
        stems[r][a:a + len(seg)] = seg
if n_missing:
    print(f"WARNING: {n_missing} sentence co role la (skip)")

for r in roles:
    s = stems[r]
    s16 = (np.clip(s, -1.0, 1.0) * 32767.0).astype(np.int16)
    out = OUT_DIR / f"{r}.wav"
    with wave.open(str(out), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SR)
        wf.writeframes(s16.tobytes())
    rms = float(np.sqrt(np.mean(s ** 2))) if len(s) else 0.0
    peak = float(np.max(np.abs(s))) if len(s) else 0.0
    # so doan co tieng that su
    voiced = int((np.abs(s) > 0.01).sum())
    print(f"  {r:2s} -> {out.name} | peak={peak:.3f} rms={rms:.4f} voiced={voiced/SR:.1f}s")

print("OK")
