#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ghép 11 file SFX thành 1 file liên tục (kèm 1,2 s im lặng giữa các đoạn)
để AI nghe phân tích trong 1 lần gọi. In ra bảng mốc thời gian."""
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SFX = ROOT / "assets" / "sfx"
OUT = ROOT / ".work" / "sfx_contact.wav"
SR = 44100
GAP = 1.2
ORDER = [
    ("gavel.wav", "bua toa an go Cop"),
    ("lock_door.wav", "khoa cua sat Cach"),
    ("chains.wav", "xieng xich kim loai"),
    ("keyboard_night.wav", "ban phim go trong dem"),
    ("paper_rustle.wav", "lat giay ho so sot sot"),
    ("folder_close.wav", "gap ho so giay Bup"),
    ("police_siren_distant.wav", "coi xe canh sat vong xa"),
    ("door_knock.wav", "go cua don dap trong dem"),
    ("radio_chatter.wav", "bo dam canh sat re nhe + mo cua"),
    ("heart_beep.wav", "may do nhip tim Bip Bip"),
    ("heartbeat_slow.wav", "nhip tim dap cham"),
]


def read(p):
    with wave.open(str(p), "rb") as w:
        assert w.getframerate() == SR and w.getnchannels() == 1
        d = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype(np.float32) / 32768.0
    return d


buf = []
marks = []
t = 0.0
for name, desc in ORDER:
    x = read(SFX / name)
    marks.append((t, t + len(x) / SR, name, desc))
    buf.append(x)
    buf.append(np.zeros(int(GAP * SR), np.float32))
    t += len(x) / SR + GAP

y = np.concatenate(buf)
with wave.open(str(OUT), "wb") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((np.clip(y, -1, 1) * 32767).astype("<i2").tobytes())

print(f"{OUT}  ({OUT.stat().st_size/1024:.0f} KB, {len(y)/SR:.1f}s)")
print("MOC THOI GIAN:")
for a, b, n, d in marks:
    print(f"  {a:>6.2f}s - {b:>6.2f}s  {n:<26} ({d})")
