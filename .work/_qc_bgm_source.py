# -*- coding: utf-8 -*-
"""Test quyết định: trong master, đoạn lặng đang chạy file nhạc nền NÀO?

So tương quan tối đa (FFT) giữa 1 s âm thanh trong master và từng file nguồn
đã resample 48 kHz. File nào khớp cao nhất = file đang được phát.
"""
import pathlib
import subprocess
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
BGM = ROOT / "assets" / "bgm"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
TMP = WORK / "_qc_tmp48"
TMP.mkdir(exist_ok=True)


def to48k_mono(mp3):
    out = TMP / (mp3.stem + "_48k.wav")
    if not out.exists():
        subprocess.run([str(FF), "-y", "-v", "error", "-i", str(mp3), "-ar", "48000",
                        "-ac", "1", str(out)], check=True)
    with wave.open(str(out), "rb") as w:
        n = w.getnframes()
        return np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0


def read_master(p):
    with wave.open(str(p), "rb") as w:
        n, ch, sr = w.getnframes(), w.getnchannels(), w.getframerate()
        d = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0
    return (d.reshape(-1, ch) if ch == 2 else d), sr


def max_corr(window, src):
    """Tương quan tối đa của window (1 s) với src, quét mọi vị trí."""
    L = len(window)
    if len(src) <= L:
        return 0.0
    n = len(src)
    size = 1 << int(np.ceil(np.log2(n + L)))
    S = np.fft.rfft(src, size)
    W = np.fft.rfft(window, size)
    corr = np.fft.irfft(S * np.conj(W), size)
    corr = corr[:n - L + 1]
    k = int(np.argmax(np.abs(corr)))
    denom = float(np.sqrt((window ** 2).sum() * (src[k:k + L] ** 2).sum())) or 1e-12
    return float(corr[k]) / denom


def quietest(mono, sr, a, b, win=1.0):
    k = int(win * sr)
    best, bi = 1e9, int(a * sr)
    for s in range(int(a * sr), min(int(b * sr), len(mono) - k), max(1, k // 4)):
        r = float(np.sqrt((mono[s:s + k] ** 2).mean()))
        if r < best:
            best, bi = r, s
    return bi, best


CANDIDATES = ["bgm_cello_sad.mp3", "bgm_cello_sad_v2.mp3", "bgm_sub_drone.mp3",
              "bgm_piano_minimal.mp3", "bgm_ambient_deep.mp3", "bgm_violin_heart.mp3",
              "bgm_guitar_acoustic_60s.mp3", "bgm_church_organ.mp3", "bgm_piano_warm.mp3"]
SRC = {c: to48k_mono(BGM / c) for c in CANDIDATES}

JOBS = [
    ("T07 VN", WORK / "_cu" / "audio_master_t07.wav.bak_bgm", WORK / "audio_master_t07.wav",
     {1: (23.0, 296.6), 2: (298.6, 565.1), 3: (567.1, 798.0),
      4: (800.0, 1067.5), 5: (1069.5, 1300.6)}),
    ("T02 VN", WORK / "_cu" / "audio_master_t02.wav.bak_bgm", WORK / "audio_master_t02.wav",
     {1: (23.0, 325.7), 2: (327.7, 572.4), 3: (574.4, 918.1),
      4: (920.1, 1258.4), 5: (1260.4, 1596.7)}),
]

for label, old_p, new_p, acts in JOBS:
    if not old_p.exists() or not new_p.exists():
        continue
    print(f"\n{'='*104}\n=== {label}: file nguồn đang chạy trong từng hồi ===\n{'='*104}")
    for tag, p in (("CU ", old_p), ("MOI", new_p)):
        a, sr = read_master(p)
        mono = a.mean(axis=1) if a.ndim > 1 else a
        print(f"\n  --- bản {tag} ---")
        for act, (s, e) in sorted(acts.items()):
            i, rms_q = quietest(mono, sr, s, e)
            j = min(i + sr, len(mono))
            w = mono[i:j]
            scores = sorted(((max_corr(w, SRC[c]), c) for c in CANDIDATES), reverse=True)
            top = "  ".join(f"{c.replace('bgm_', '').replace('.mp3', '')}={v:.3f}" for v, c in scores[:3])
            print(f"    H{act} t={i/sr:7.1f}s  RMS={rms_q:.4f}  ->  {top}")
