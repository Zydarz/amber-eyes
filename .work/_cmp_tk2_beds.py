# -*- coding: utf-8 -*-
"""3 phien ban TK2 (VN/EN/JA) co dung CUNG mot bed khong?

So sanh cross-correlation giua cac doan nghi cua 3 master TK2 + voi WAV CU EN TK2
(ban 24/11 - co bed) => xac nhan bed la tai san dung chung hay khac.
"""
import glob
import json
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = sorted(str(p) for p in (ROOT / ".work" / "ffmpeg").glob("*/bin/ffmpeg.exe"))[0]
SR = 16000


def decode(path, sr=SR):
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", "1",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def xcorr_max(seg, ref):
    n = len(seg)
    if len(ref) < n:
        return 0.0
    e = float(np.sum(seg ** 2))
    if e < 1e-12:
        return 0.0
    # dot product truc tiep tren moi lag (n <= 48000 -> 48000*len(ref) la qua lon) => dung FFT
    N = 1
    while N < n + len(ref):
        N *= 2
    A = np.fft.rfft(seg, N)
    B = np.fft.rfft(ref, N)
    cc = np.fft.irfft(A * np.conj(B), N)
    csum = np.concatenate([[0.0], np.cumsum(ref ** 2)])
    lim = min(len(ref) - n + 1, len(cc))
    best = 0.0
    for k in range(lim):
        p = csum[k + n] - csum[k]
        if p < 1e-12:
            continue
        v = cc[k] / np.sqrt(e * p)
        if abs(v) > abs(best):
            best = float(v)
    return best


def gaps_of(a, tl, min_len=0.5, k=3):
    out = []
    for i in range(len(tl) - 1):
        g0, g1 = tl[i]["end"], tl[i + 1]["start"]
        if g1 - g0 >= min_len:
            out.append(a[int((g0 + 0.05) * SR):int(min(g1 - 0.05, g0 + 3.0) * SR)])
    out = [s for s in out if len(s) >= SR]
    out.sort(key=len, reverse=True)
    return out[:k]


def main():
    srcs = {}
    for ld in ["Tap04", "Tap04_EN", "Tap04_JA"]:
        d = ROOT / "02_SAN_XUAT" / "TIKTOK" / ld
        a = decode(d / "TK2_master_audio.mp3")
        tl = json.loads((d / "timeline_tk2.json").read_text(encoding="utf-8"))
        srcs[ld] = gaps_of(a, tl)
        print(f"{ld} TK2: {len(srcs[ld])} doan nghi")

    w = decode(ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_EN" / "TK2_master_audio.wav")
    tlw = json.loads((ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_EN" / "timeline_tk2.json").read_text(encoding="utf-8"))
    srcs["EN_WAV_CU"] = gaps_of(w, tlw)
    print(f"EN_WAV_CU: {len(srcs['EN_WAV_CU'])} doan nghi")

    keys = list(srcs)
    print("\n=== cross-correlation giua cac doan nghi (cua cac phien ban TK2) ===")
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            best = 0.0
            for s1 in srcs[keys[i]]:
                for s2 in srcs[keys[j]]:
                    best = max(best, abs(xcorr_max(s1, s2)))
            print(f"  {keys[i]:10} vs {keys[j]:10}  max|corr| = {best:+.3f}")


if __name__ == "__main__":
    main()
