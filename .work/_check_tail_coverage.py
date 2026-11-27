#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra phu tram cuoi: dong cuoi trong timeline co bao het phan loi noi cuoi khong?

Dung envelope RMS (khong can ASR) de tim moc thoi gian het tieng noi gan nhat sau
dong cuoi cua timeline. Neu |timeline_end - speech_end| > 1.5 s => co nghi vo
(co loi bi ASR bo sot).
"""
import glob
import json
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = glob.glob(str(ROOT / ".work" / "ffmpeg" / "*" / "bin" / "ffmpeg.exe"))[0]
LANGDIR = {"Tap04": "VN", "Tap04_EN": "EN", "Tap04_JA": "JA"}
RMS_DB = -45.0   # nguong co tieng


def decode(path, sr=16000):
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", "1",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def speech_end(a, sr=16000):
    n = int(0.10 * sr)
    last = 0.0
    for i in range(0, len(a) - n + 1, n):
        seg = a[i:i + n]
        rms = float(np.sqrt(np.mean(seg ** 2)))
        db = 20 * np.log10(max(rms, 1e-12))
        if db > RMS_DB:
            last = (i + n) / sr
    return last


def main():
    print(f"{'lang/clip':16}{'dur':>7}{'tl_end':>9}{'speech_end':>12}{'duoi':>8}  ket_qua")
    for ld in ["Tap04", "Tap04_EN", "Tap04_JA"]:
        for n in ["TK1", "TK2", "TK3", "TK4", "TK5"]:
            d = ROOT / "02_SAN_XUAT" / "TIKTOK" / ld
            mp3 = d / f"{n}_master_audio.mp3"
            tl = json.loads((d / f"timeline_{n.lower()}.json").read_text(encoding="utf-8"))
            a = decode(mp3)
            dur = len(a) / 16000
            se = speech_end(a)
            te = max(t["end"] for t in tl)
            gap = se - te
            ok = "OK" if gap <= 1.5 else "<<< NGHI VO (ASR bo sot duoi)"
            print(f"{ld + '/' + n:16}{dur:7.2f}{te:9.2f}{se:12.2f}{gap:8.2f}  {ok}")


if __name__ == "__main__":
    main()
