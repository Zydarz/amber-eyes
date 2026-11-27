#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Do RMS/peak theo thoi gian cho wav cu va mp3 moi EN TK2 de xac dinh phan bi mat."""
import glob
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = glob.glob(str(ROOT / ".work" / "ffmpeg" / "*" / "bin" / "ffmpeg.exe"))[0]
D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_EN"


def decode(path, sr=16000):
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", "1",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def envelope(a, sr=16000, win=0.25):
    n = int(win * sr)
    out = []
    for i in range(0, len(a) - n + 1, n):
        seg = a[i:i + n]
        rms = float(np.sqrt(np.mean(seg ** 2)))
        peak = float(np.max(np.abs(seg)))
        db = 20 * np.log10(max(rms, 1e-9))
        out.append((i / sr, db, peak))
    return out


def report(label, path):
    a = decode(path)
    print(f"\n=== {label}  ({path.name})  dur={len(a)/16000:.2f}s")
    env = envelope(a)
    for t, db, pk in env:
        if t < 55.0:
            continue
        bar = "#" * max(0, int((db + 70) / 2))
        print(f"  {t:6.2f}s  rms={db:7.2f} dB  peak={20*np.log10(max(pk,1e-9)):7.2f} dB  {bar}")


if __name__ == "__main__":
    report("WAV CU (24/11)", D / "TK2_master_audio.wav")
    report("MP3 MOI (27/11)", D / "TK2_master_audio.mp3")
