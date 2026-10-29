# -*- coding: utf-8 -*-
"""Tách phần lệch thành (a) đổi gain toàn cục do loudnorm và (b) đổi nội dung nhạc."""
import pathlib
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"


def read(p):
    with wave.open(str(p), "rb") as w:
        n, ch, sr = w.getnframes(), w.getnchannels(), w.getframerate()
        d = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0
    return (d.reshape(-1, ch) if ch == 2 else d), sr


REGIONS = [
    ("intro 0-22,4s   (KHONG doi)", 0.0, 22.4),
    ("H1 23-325,7s    (DA SUA)", 23.0, 325.7),
    ("H2 327,7-572,4s (giu)", 327.7, 572.4),
    ("H3 574,4-918,1s (DA SUA)", 574.4, 918.1),
    ("H4 920,1-1258,4s(giu)", 920.1, 1258.4),
    ("H5 1260,4-1596,7s(giu)", 1260.4, 1596.7),
]

for label, old_p, new_p in [
    ("T02 VN", WORK / "_cu" / "audio_master_t02.wav.bak_bgm", WORK / "audio_master_t02.wav"),
    ("T07 VN", WORK / "_cu" / "audio_master_t07.wav.bak_bgm", WORK / "audio_master_t07.wav"),
]:
    if not old_p.exists() or not new_p.exists():
        continue
    a, sr = read(old_p)
    b, _ = read(new_p)
    n = min(len(a), len(b))
    print(f"\n=== {label}  (sr={sr}) ===")
    print(f"{'vung':<30}{'a (gain toi uu)':>16}{'gain dB':>10}{'residual sau gain':>20}{'tuong quan':>12}")
    print("-" * 90)
    for name, s, e in REGIONS:
        i, j = int(s * sr), min(int(e * sr), n)
        x, y = a[i:j], b[i:j]
        if x.size == 0:
            continue
        rms_x = float(np.sqrt((x ** 2).mean()))
        a_opt = float((x * y).sum() / max((x * x).sum(), 1e-12))
        gain_db = 20 * np.log10(a_opt) if a_opt > 1e-9 else -99
        res = float(np.sqrt(((y - a_opt * x) ** 2).mean()))
        num = float((x * y).sum())
        den = float(np.sqrt((x * x).sum() * (y * y).sum())) or 1e-12
        corr = num / den
        print(f"{name:<30}{a_opt:>16.5f}{gain_db:>10.2f}{res:>20.6f}{corr:>12.5f}")
