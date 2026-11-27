# -*- coding: utf-8 -*-
"""Dinh danh bed bang cross-correlation SONG THO tren tung doan nghi (co tim lag).

Doi voi tung doan nghi 2-4 s: so sanh voi MOI file BGM (va ca phien ban tile) bang
FFT cross-correlation, tim lag toi uu => gia tri cao + vi tri lag khop giua cac doan
=> bang chung manh file BGM nao that su.
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
SR = 16000


def decode(path, sr=SR):
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", "1",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def best_corr(seg, ref):
    """Cross-correlation chuan hoa giua seg va ref (ref lai lap >= len seg)."""
    n = len(seg)
    if len(ref) < n:
        return 0.0, 0
    # dung FFT: corr(seg, ref) = ifft(conj(FFT(seg)) * FFT(ref))
    N = 1
    while N < n + len(ref):
        N *= 2
    A = np.fft.rfft(seg, N)
    B = np.fft.rfft(ref[:n + len(ref)], N)
    cc = np.fft.irfft(A * np.conj(B), N)
    # cc[k] = sum seg[n] * ref[n-k]; normalize theo chuoi ref
    csum = np.concatenate([[0.0], np.cumsum(ref ** 2)])
    e = float(np.sum(seg ** 2))
    if e < 1e-12:
        return 0.0, 0
    best, blag = 0.0, 0
    # lag 0..len(ref)-n
    for k in range(0, min(len(ref) - n + 1, 4000)):
        p = csum[k + n] - csum[k]
        if p < 1e-12:
            continue
        v = cc[k] / np.sqrt(e * p)
        if abs(v) > abs(best):
            best = float(v)
            blag = k
    return best, blag


def main():
    bgms = sorted((ROOT / "assets" / "bgm").glob("*.mp3"))
    bgm_raw = {b.name: decode(b) for b in bgms}
    # ban tile dai 4 lan cho moi file
    bgm_tiled = {k: np.tile(v, 4) for k, v in bgm_raw.items()}

    for ld in ["Tap04", "Tap04_EN", "Tap04_JA"]:
        for n in ["TK1", "TK2", "TK3", "TK4", "TK5"]:
            d = ROOT / "02_SAN_XUAT" / "TIKTOK" / ld
            mp3 = d / f"{n}_master_audio.mp3"
            tl = json.loads((d / f"timeline_{n.lower()}.json").read_text(encoding="utf-8"))
            a = decode(mp3)
            # 3 doan nghi dai nhat
            gaps = [(tl[i]["end"], tl[i + 1]["start"]) for i in range(len(tl) - 1)
                    if tl[i + 1]["start"] - tl[i]["end"] > 0.45]
            gaps.sort(key=lambda x: -(x[1] - x[0]))
            gaps = gaps[:3]
            if not gaps:
                print(f"{ld:9} {n}: khong co doan nghi >0,45s")
                continue
            agg = {}
            for g0, g1 in gaps:
                s = a[int((g0 + 0.05) * SR): int(min(g1 - 0.05, g0 + 3.0) * SR)]
                if len(s) < SR:
                    continue
                for k, ref in bgm_tiled.items():
                    c, lag = best_corr(s, ref)
                    if k not in agg or abs(c) > abs(agg[k][0]):
                        agg[k] = (c, lag, g0)
            items = sorted(agg.items(), key=lambda kv: -abs(kv[1][0]))
            top = ", ".join(f"{k}={v[0]:+.3f}" for k, v in items[:4])
            print(f"{ld:9} {n}: {len(gaps)} doan | {top}")


if __name__ == "__main__":
    main()
