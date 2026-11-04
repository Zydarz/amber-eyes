#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đo số đo audio master JA Tap02: true peak, LUFS, LRA, khoảng lặng, đỉnh mẫu."""
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
WAV = W / "audio_master_JA_t02.wav"
MP3 = ROOT / "02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA_master.mp3"


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def measure(path, label):
    print("=" * 70)
    print(label, path.name)
    print("=" * 70)
    # ebur128: LUFS / LRA / true peak
    r = run([str(FF), "-hide_banner", "-nostats", "-i", str(path),
             "-af", "ebur128=peak=true", "-f", "null", "-"])
    tail = (r.stderr or "")[-1400:]
    i = tail.rfind("Integrated loudness")
    blk = tail[i:] if i >= 0 else tail
    for key, pat in [("LUFS", r"I:\s*(-?[\d.]+) LUFS"), ("LRA", r"LRA:\s*(-?[\d.]+) LU"),
                     ("Peak", r"Peak:\s*(-?[\d.]+) dBFS")]:
        m = re.findall(pat, blk)
        print(f"  {key:5s} = {m[-1] if m else '?'}")
    # astats: sample peak
    r2 = run([str(FF), "-hide_banner", "-nostats", "-i", str(path),
              "-af", "astats=metadata=0:reset=0", "-f", "null", "-"])
    pk = re.findall(r"Peak level dB:\s*(-?[\d.]+|-?inf)", r2.stderr or "")
    rms = re.findall(r"RMS level dB:\s*(-?[\d.]+|-?inf)", r2.stderr or "")
    print(f"  Peak level dB (sample) = {pk[-1] if pk else '?'}")
    print(f"  RMS level dB            = {rms[-1] if rms else '?'}")
    # khoảng lặng
    r3 = run([str(FF), "-hide_banner", "-nostats", "-i", str(path),
              "-af", "silencedetect=n=-60dB:d=0.3", "-f", "null", "-"])
    s1 = re.findall(r"silence_start: ([\d.]+)", r3.stderr or "")
    s1e = re.findall(r"silence_end: ([\d.]+)", r3.stderr or "")
    print(f"  doan im > 0,3 s @ -60 dB : {len(s1)}  {s1[:10]}")
    r4 = run([str(FF), "-hide_banner", "-nostats", "-i", str(path),
              "-af", "silencedetect=n=-35dB:d=2.5", "-f", "null", "-"])
    s2 = re.findall(r"silence_start: ([\d.]+)", r4.stderr or "")
    print(f"  doan im >= 2,5 s @ -35 dB: {len(s2)}  {s2[:10]}")


if WAV.exists():
    measure(WAV, "JA TAP02 MASTER WAV")
if MP3.exists():
    measure(MP3, "JA TAP02 MASTER MP3")
