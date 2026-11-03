#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đo RMS theo cửa sổ + silence detect cho 1 file audio (dùng khi QC master).

Dùng: py -3 .work/_qa_measure_audio.py <file> [so giay_dau] [so giay_cuoi]
"""
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def decode(path, start=None, dur=None):
    cmd = [str(FF), "-hide_banner", "-nostats", "-v", "error"]
    if start is not None:
        cmd += ["-ss", f"{start:.3f}"]
    cmd += ["-i", str(path)]
    if dur is not None:
        cmd += ["-t", f"{dur:.3f}"]
    cmd += ["-f", "f32le", "-ac", "1", "-ar", "16000", "-"]
    raw = subprocess.run(cmd, capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).astype(np.float64)


def main():
    path = Path(sys.argv[1])
    start = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
    dur = float(sys.argv[3]) if len(sys.argv) > 3 else 60.0
    x = decode(path, start, dur)
    sr = 16000
    print(f"file={path.name}  start={start}  dur={dur}  mau={len(x)} ({len(x)/sr:.3f}s)")
    if len(x) == 0:
        raise SystemExit("khong giai ma duoc")
    win = int(1.0 * sr)
    n = len(x) // win
    rows = []
    for i in range(n):
        seg = x[i * win:(i + 1) * win]
        rms = float(np.sqrt(np.mean(seg ** 2)))
        db = 20 * np.log10(rms) if rms > 0 else -99.0
        rows.append((start + i, db))
    for t, db in rows:
        bar = "#" * max(0, int((db + 60) / 2))
        print(f"  {t:8.1f}s  {db:7.1f} dBFS  {bar}")
    peak = float(np.abs(x).max())
    print(f"PEAK trong doan: {20*np.log10(peak):.2f} dBFS")
    # silence detect toan bo file
    r = subprocess.run([str(FF), "-hide_banner", "-nostats", "-i", str(path),
                        "-af", "silencedetect=noise=-45dB:d=0.8", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    sil = re.findall(r"silence_start: ([\d.]+) \| silence_end: ([\d.]+)", r.stderr)
    if sil:
        print(f"khoang cam >=0,8s @ -45dBFS: {len(sil)}")
        for a, b in sil:
            print(f"   {float(a):.2f} -> {float(b):.2f}  ({float(b)-float(a):.2f}s)")
    else:
        print("khoang cam >=0,8s @ -45dBFS: 0")


if __name__ == "__main__":
    main()
