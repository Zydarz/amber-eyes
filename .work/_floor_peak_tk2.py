#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So sanh nen im lang giua cac cau: master cu (wav 24/11) vs master moi (mp3 27/11) vs master EN TK3 (mp3).

Muc tieu: xac nhan master moi co BGM nen hay khong, va muc peak/TP co vuot chuan khong.
"""
import glob
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = glob.glob(str(ROOT / ".work" / "ffmpeg" / "*" / "bin" / "ffmpeg.exe"))[0]
D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_EN"

# khoang nghi (giua cac cau) lay tu silence list cua mp3 moi
GAPS = [(0.0, 0.384), (4.295, 4.881), (6.121, 6.851), (9.657, 10.318),
        (20.299, 20.919), (28.576, 29.226), (36.569, 37.214),
        (42.577, 43.218), (48.539, 49.170), (58.296, 59.001), (67.412, 68.255)]


def decode(path, sr=16000):
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", "1",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def gap_stats(a, label):
    print(f"\n=== {label}  dur={len(a)/16000:.2f}s")
    floors = []
    for st, en in GAPS:
        seg = a[int(st * 16000): int(en * 16000)]
        if len(seg) < 100:
            continue
        rms = float(np.sqrt(np.mean(seg ** 2)))
        pk = float(np.max(np.abs(seg)))
        db = 20 * np.log10(max(rms, 1e-12))
        floors.append(db)
        print(f"   gap {st:6.2f}-{en:6.2f}  rms={db:8.2f} dB  peak={20*np.log10(max(pk,1e-12)):8.2f} dB")
    print(f"   -> nen im lang trung binh = {sum(floors)/max(1,len(floors)):.2f} dB")
    return floors


def true_silence(a, thr=-100.0, min_dur=0.05):
    """Dem khoang co tin hieu so 0 (khong phai nhac nen)."""
    n = int(0.05 * 16000)
    cnt, tot = 0, 0.0
    for i in range(0, len(a) - n + 1, n):
        seg = a[i:i + n]
        pk = float(np.max(np.abs(seg)))
        db = 20 * np.log10(max(pk, 1e-12))
        tot += 0.05
        if db < thr:
            cnt += 0.05
    return cnt, tot


def peak_stats(a, label):
    pk = float(np.max(np.abs(a)))
    print(f"   peak tong = {20*np.log10(max(pk,1e-12)):.2f} dBFS")


def main():
    wav = decode(D / "TK2_master_audio.wav")
    mp3 = decode(D / "TK2_master_audio.mp3")
    tk3 = decode(D / "TK3_master_audio.mp3")
    tk1 = decode(D / "TK1_master_audio.mp3")

    gap_stats(wav, "WAV CU 24/11 (TK2)")
    gap_stats(mp3, "MP3 MOI 27/11 (TK2)")
    gap_stats(tk3, "MP3 EN TK3 (master chuan)")
    gap_stats(tk1, "MP3 EN TK1 (master chuan)")

    print("\n=== khoang SILE TUYET DOI (peak < -100 dBFS) ===")
    for a, lb in [(wav, "WAV CU TK2"), (mp3, "MP3 MOI TK2"), (tk3, "EN TK3"), (tk1, "EN TK1")]:
        c, t = true_silence(a)
        print(f"   {lb:12} {c:6.2f}s / {t:.2f}s  ({c/t*100:.1f}%)")

    print("\n=== PEAK ===")
    for a, lb in [(wav, "WAV CU TK2"), (mp3, "MP3 MOI TK2"), (tk3, "EN TK3"), (tk1, "EN TK1")]:
        peak_stats(a, lb)


if __name__ == "__main__":
    main()
