#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dem mau vượt 0 dBFS (clipping) trong master mp3 va so sanh 15 master."""
import glob
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = glob.glob(str(ROOT / ".work" / "ffmpeg" / "*" / "bin" / "ffmpeg.exe"))[0]


def decode(path, sr=48000):
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", "1",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def main():
    rows = []
    for ld in ["Tap04", "Tap04_EN", "Tap04_JA"]:
        for n in ["TK1", "TK2", "TK3", "TK4", "TK5"]:
            p = ROOT / "02_SAN_XUAT" / "TIKTOK" / ld / f"{n}_master_audio.mp3"
            a = decode(p)
            over = np.abs(a) > 1.0
            n_over = int(over.sum())
            near = np.abs(a) > 0.988  # ~ -0.1 dBFS
            pk = float(np.max(np.abs(a)))
            rows.append((ld, n, len(a) / 48000, 20 * np.log10(max(pk, 1e-12)), n_over, int(near.sum())))

    print(f"{'lang':10}{'clip':6}{'dur':>8}{'peak dBFS':>11}{'>0dBFS':>10}{'>-0.1dB':>10}")
    for ld, n, d, pk, no, nr in rows:
        flag = "  <<< CLIP" if no else ""
        print(f"{ld:10}{n:6}{d:8.2f}{pk:11.2f}{no:10d}{nr:10d}{flag}")

    # vi tri clip trong file moi
    p = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_EN" / "TK2_master_audio.mp3"
    a = decode(p)
    over = np.where(np.abs(a) > 1.0)[0]
    if len(over):
        print(f"\nFile moi: {len(over)} mau > 0 dBFS, dau-tien tai {over[0]/48000:.3f}s, "
              f"cuoi tai {over[-1]/48000:.3f}s")
        # gom theo co 100 ms
        buckets = sorted(set((over // 4800).tolist()))
        print("  cac doan (0.1 s) bi clip:", ", ".join(f"{b*0.1:.1f}s" for b in buckets[:40]),
              "..." if len(buckets) > 40 else "")


if __name__ == "__main__":
    main()
