"""Kiem chung reel: do F0 tung file/va tung doan trong reel so voi F0 ky vong cua vai.

Neu doan trong reel lech voi nhan -> loi o file/payload, khong phai o tai nghe.
"""
import json
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from g9_decide import f0_p2, fix_octave, med, read_wav, nc  # noqa: E402

FF = HERE / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
V6 = HERE / "kaggle_higgs" / "out_higgs_v6" / "out_higgs_v6"
REEL = ROOT / "02_SAN_XUAT" / "Tap02" / "xuat_ban" / "DEMO_giong_Higgs.mp3"

# (file pilot, vai, clip, F0 clone ky vong ac/pp2 tu g9_decide)
EXPECT = {
    "P6_H__H__0_H_H_t0.8_s0.wav": ("H", "H.wav", 130.4, 127.1),
    "P6_H__H__1_H_H_t0.8_s0.wav": ("H", "H.wav", 130.4, 127.1),
    "P6_H__H__5_H_H_t0.8_s0.wav": ("H", "H.wav", 130.4, 127.1),
    "P6_D__M_HIGH__2_D_M_HIGH_t0.8_s0.wav": ("D", "M_HIGH.wav", 198.3, 185.8),
    "P6_D__M_HIGH__3_D_M_HIGH_t0.8_s0.wav": ("D", "M_HIGH.wav", 198.3, 185.8),
    "P6_C__C__0_C_C_t0.8_s0.wav": ("C", "C.wav", 214.3, 202.8),
    "P6_C__C__3_C_C_t0.8_s0.wav": ("C", "C.wav", 214.3, 202.8),
    "P6_N1__W6_LOW__0_N1_W6_LOW_t0.8_s0.wav": ("N1", "W6_LOW.wav", 184.6, 173.1),
    "P6_N1__W6_LOW__3_N1_W6_LOW_t0.8_s0.wav": ("N1", "W6_LOW.wav", 184.6, 173.1),
    "P6_N2__W5_HIGH__4_N2_W5_HIGH_t0.8_s0.wav": ("N2", "W5_HIGH.wav", 285.7, 268.0),
    "P6_N2__W5_HIGH__1_N2_W5_HIGH_t0.8_s0.wav": ("N2", "W5_HIGH.wav", 285.7, 268.0),
}


def ac_of(x, sr):
    """AC thuần (khong sua octave) de doi chieu voi bang g9_decide."""
    import math
    win = int(0.045 * sr)
    hop = int(0.010 * sr)
    lo, hi = int(sr / 400.0), int(sr / 70.0)
    out, prev = [], None
    for s in range(0, len(x) - win, hop):
        f = x[s:s + win]
        if np.sqrt((f ** 2).mean()) < 0.01:
            continue
        f = f - f.mean()
        peak = np.max(np.abs(f))
        if peak > 0:
            f = np.clip(f, -0.5 * peak, 0.5 * peak)
        n = len(f)
        nfft = 1 << int(np.ceil(np.log2(2 * n)))
        F = np.fft.rfft(f, nfft)
        ac = np.fft.irfft(F * np.conj(F), nfft)[:n]
        if ac[0] <= 0:
            continue
        acn = ac / ac[0]
        k = lo + int(np.argmax(acn[lo:hi]))
        if acn[k] < 0.25:
            continue
        shift = 0.0
        if 0 < k < n - 1:
            a0, a1, a2 = acn[k - 1], acn[k], acn[k + 1]
            d = a0 - 2 * a1 + a2
            if d != 0:
                shift = 0.5 * (a0 - a2) / d
        out.append(sr / (k + shift))
    return float(np.median(out)) if out else 0.0


def main():
    print("=" * 100)
    print("A) F0 TUNG FILE PILOT DUNG TRONG REEL (ac / pp2) — so voi F0 ky vong cua vai")
    print("=" * 100)
    print("%-42s %-4s %-12s %8s %8s %8s %8s  %s" % (
        "file", "vai", "clip", "ac", "pp2", "ac_kv", "pp2_kv", "chenh"))
    rows = []
    for fn, (role, clip, e_ac, e_pp2) in EXPECT.items():
        p = V6 / fn
        if not p.exists():
            print("!! thieu", fn)
            continue
        x, sr = read_wav(p)
        ac = ac_of(x, sr)
        p2 = f0_p2(x, sr)
        p2f, _ = fix_octave(ac, p2)
        print("%-42s %-4s %-12s %8.1f %8.1f %8.1f %8.1f  nc_ac=%.2f" % (
            fn[:42], role, clip, ac, p2, e_ac, e_pp2, nc(ac, e_ac)))
        rows.append((fn, role, clip, ac, p2f, e_ac, e_pp2))

    print()
    print("=" * 100)
    print("B) F0 TUNG DOAN TRONG REEL (mp3) — tach theo moc thoi gian trong bang")
    print("=" * 100)
    r = subprocess.run([str(FF), "-v", "error", "-i", str(REEL), "-ac", "1", "-ar", "24000",
                        "-f", "f32le", "-"], capture_output=True, check=True)
    reel = np.frombuffer(r.stdout, np.float32).copy()
    segs = [
        (0.0, 19.7, "H / 5.02#4 (dai)"),
        (19.7, 28.8, "H / 2.04#1 + 1.03#1 (ngan)"),
        (28.8, 48.6, "D / 1.17#1 + 3.05#1"),
        (48.6, 75.1, "C / 5.02#4 + 3.05#1"),
        (75.1, 101.6, "N1 / 5.02#4 + 3.05#1"),
        (101.6, 110.8, "N2 / 4.06#1 + 2.04#1"),
    ]
    for a, b, lab in segs:
        seg = reel[int(a * 24000):int(b * 24000)]
        ac = ac_of(seg, 24000)
        p2 = f0_p2(seg, 24000)
        p2f, tag = fix_octave(ac, p2)
        print("%6.1f-%6.1f s  %-32s ac=%7.1f  pp2=%7.1f%s" % (a, b, lab, ac, p2f, (" " + tag) if tag else ""))


if __name__ == "__main__":
    main()
