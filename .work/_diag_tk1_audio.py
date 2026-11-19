#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chan doan TK1_master_audio.wav: co that la giong noi tieng Viet khong?"""
import pathlib
import struct
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

ROOT = pathlib.Path(__file__).resolve().parent.parent
WAV = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap01" / "TK1_master_audio.wav"
OUT = ROOT / ".work" / "_tk1_spectrogram.png"


def read_wav(p):
    with wave.open(str(p), "rb") as wf:
        print("  channels=%d rate=%d width=%d frames=%d comp=%s"
              % (wf.getnchannels(), wf.getframerate(), wf.getsampwidth(),
                 wf.getnframes(), wf.getcomptype()))
        sr = wf.getframerate()
        ch = wf.getnchannels()
        raw = wf.readframes(wf.getnframes())
    x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    if ch > 1:
        x = x.reshape(-1, ch).mean(axis=1)
    return x, sr


def main():
    x, sr = read_wav(WAV)
    print("  duration = %.3f s" % (len(x) / sr))

    # --- 1. pho tan so (spectrogram) ---
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        nfft = 1024
        hop = 256
        win = np.hanning(nfft)
        nfr = 1 + (len(x) - nfft) // hop
        S = np.empty((nfr, nfft // 2 + 1), dtype=np.float32)
        for i in range(nfr):
            seg = x[i * hop:i * hop + nfft] * win
            S[i] = np.abs(np.fft.rfft(seg))
        db = 20 * np.log10(S + 1e-9)
        freqs = np.fft.rfftfreq(nfft, 1.0 / sr)
        t = np.arange(nfr) * hop / sr
        fig, ax = plt.subplots(figsize=(16, 6))
        ax.pcolormesh(t, freqs, db.T, vmin=-95, vmax=-15, cmap="magma", shading="auto")
        ax.set_ylim(0, 8000)
        ax.set_xlabel("giay")
        ax.set_ylabel("Hz")
        ax.set_title("TK1_master_audio.wav - spectrogram")
        fig.tight_layout()
        fig.savefig(str(OUT), dpi=110)
        print("  -> %s" % OUT)
    except Exception as e:
        print("  matplotlib fail: %s" % e)

    # --- 2. nang luong theo tung cau (timeline) ---
    import json
    tl = json.loads((ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap01" / "timeline_tk1.json")
                    .read_text(encoding="utf-8-sig"))
    print("\n  RMS / crest theo tung cau:")
    for l in tl:
        seg = x[int(l["start"] * sr):int(l["end"] * sr)]
        rms = float(np.sqrt(np.mean(seg ** 2)))
        pk = float(np.max(np.abs(seg)))
        print("    %-11s %4.2f-%6.2f s  RMS %7.2f dBFS  peak %7.2f dBFS  crest %5.1f dB"
              % (l["id"], l["start"], l["end"], 20 * np.log10(max(rms, 1e-9)),
                 20 * np.log10(max(pk, 1e-9)), 20 * np.log10(max(pk / max(rms, 1e-9), 1e-9))))

    # --- 3. tan so co noi dung (spectral centroid + flatness) ---
    nfft = 1024
    hop = 512
    win = np.hanning(nfft)
    cent, flat = [], []
    for i in range(0, len(x) - nfft, hop):
        seg = x[i:i + nfft] * win
        S = np.abs(np.fft.rfft(seg)) + 1e-10
        ps = S ** 2
        cent.append(float(np.sum(np.fft.rfftfreq(nfft, 1 / sr) * ps) / np.sum(ps)))
        flat.append(float(np.exp(np.mean(np.log(ps))) / np.mean(ps)))
    cent = np.array(cent)
    flat = np.array(flat)
    print("\n  centroid trung viet = %.0f Hz (min %.0f / max %.0f)"
          % (np.median(cent), cent.min(), cent.max()))
    print("  flatness trung viet  = %.5f  (>0.1 => nhac/hon, <0.01 => tieng noi)"
          % np.median(flat))

    # --- 4. thu khu tuoc tai do / doi chieu mau ---
    seg = x[:int(10 * sr)]
    env = np.abs(seg)
    # tan so nhanh nhat trong 0-8 kHz theo FFT lon
    S = np.abs(np.fft.rfft(seg * np.hanning(len(seg))))
    f = np.fft.rfftfreq(len(seg), 1 / sr)
    band = (f > 60) & (f < 8000)
    idx = np.argsort(S[band])[-8:]
    fb = f[band][idx]
    print("  8 dinh pho lon nhat trong 0-10 s (Hz): %s"
          % " ".join("%.0f" % v for v in sorted(fb)))


if __name__ == "__main__":
    main()
