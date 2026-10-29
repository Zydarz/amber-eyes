#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đo envelope (peak dBFS theo cửa sổ 0,25 s) của 1 file mp3/wav.

Dùng để chọn điểm cắt: với tiếng động độc lập (fx_*) lấy quanh đỉnh tiếng;
với nền môi trường (amb_*) lấy đoạn ổn định.

CLI:  py -3 .work/_yt_envelope.py <file> [buoc]
"""
import array
import math
import subprocess
import sys
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

SR = 8000
STEP = 0.25


def envelope(path, step=STEP, sr=SR):
    """[(giay, peak_dBFS), ...]"""
    r = subprocess.run(
        [str(FF), "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"],
        capture_output=True)
    a = array.array("h")
    a.frombytes(r.stdout)
    if sys.byteorder == "big":
        a.byteswap()
    w = int(sr * step)
    out = []
    for i in range(0, len(a) - w + 1, w):
        seg = a[i:i + w]
        peak = max(map(abs, seg))
        db = 20 * math.log10(peak / 32768.0) if peak > 0 else -120.0
        out.append((i / float(sr), db))
    return out


def pick_fx_cut(env, window=8.0, thresh=-45.0, pre=1.0):
    """Trả về (start, dur): lấy cửa sổ quanh đỉnh tiếng rõ nhất.

    Cửa sổ rộng (mặc định 8 s) để giữ được chuỗi bước chân / hơi thở; phần
    lặng cuối sẽ được cắt ở bước import (2 pass).

    LƯU Ý: file rất khẽ (ví dụ "Quiet Breathing") không vượt -45 dB ở bất kỳ
    cửa sổ 0,25 s nào -> phải hạ ngưỡng, nếu không sẽ cắt nhầm đoạn lặng và
    ra file 0 giây.
    """
    if not env:
        return 0.0, window
    active = [(t, db) for t, db in env if db > thresh]
    if not active:
        # nguồn rất khẽ (hơi thở, tiếng máy nhỏ): KHÔNG dùng ngưỡng tuyệt đối,
        # mà lấy vùng gần đỉnh thực tế của chính file (top - 12 dB).
        top = max(db for _, db in env)
        active = [(t, db) for t, db in env if db > top - 12.0]
    if not active:
        return 0.0, window
    best_t, best_db = max(active, key=lambda x: x[1])
    total = env[-1][0]
    start = max(0.0, best_t - pre)
    if start + window > total:
        start = max(0.0, total - window)
    return start, window


def pick_amb_cut(env, maxlen=120.0, thresh=-45.0):
    """Nền: lấy từ đầu đoạn có tiếng đầu tiên, kéo dài tối đa maxlen."""
    if not env:
        return 0.0, maxlen
    start = 0.0
    for t, db in env:
        if db > thresh:
            start = max(0.0, t - 0.5)
            break
    return start, maxlen


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        raise SystemExit(1)
    p = Path(sys.argv[1])
    step = float(sys.argv[2]) if len(sys.argv) > 2 else STEP
    env = envelope(p, step=step)
    print(f"{p.name}: {len(env) * step:.1f}s")
    parts = [f"{t:6.2f}s:{db:6.1f}" for t, db in env if db > -45]
    print("co tieng:", " ".join(parts) if parts else "(khong co gi)")
    print("fx cut :", pick_fx_cut(env))
    print("amb cut:", pick_amb_cut(env))
