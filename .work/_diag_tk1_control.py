#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CONTROL: ASR tren audio Viet biet la tot (master Tap 10 + giong mau VoxCPM2)
de chung minh pipeline ASR hoat dong -> chon do ket luan ve TK1."""
import pathlib
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
from faster_whisper import WhisperModel  # noqa: E402


def read_wav(p):
    with wave.open(str(p), "rb") as wf:
        sr = wf.getframerate()
        ch = wf.getnchannels()
        raw = wf.readframes(wf.getnframes())
    x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    if ch > 1:
        x = x.reshape(-1, ch).mean(axis=1)
    return x, sr


def f0_med(x, sr, fmin=60, fmax=450):
    fl = int(sr * 0.04)
    hop = int(sr * 0.01)
    out = []
    for i in range(0, len(x) - fl, hop):
        seg = x[i:i + fl]
        if np.std(seg) < 0.01:
            continue
        c = np.correlate(seg, seg, "full")[fl - 1:]
        if len(c) <= int(sr / fmin):
            continue
        p = int(np.argmax(c[int(sr / fmax):int(sr / fmin)])) + int(sr / fmax)
        if c[0] > 0 and c[p] / c[0] > 0.4:
            out.append(sr / p)
    return float(np.median(out)) if out else 0.0


def main():
    model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=4)
    print("model small loaded", flush=True)

    # 1. giong mau VoxCPM2 (tieng Viet that)
    for name in ["H.wav", "D3_SH.wav", "C2_AB03.wav"]:
        p = ROOT / ".work" / "kaggle_higgs" / "dataset_voxcpm2" / name
        if not p.exists():
            print("  thieu %s" % p, flush=True)
            continue
        x, sr = read_wav(p)
        segs, info = model.transcribe(x, language=None, beam_size=5, vad_filter=False,
                                      condition_on_previous_text=False)
        txt = " ".join(s.text.strip() for s in segs).strip()
        print("  REF %-12s dur=%.1fs F0=%.1f Hz [lang=%s p=%.2f] %s"
              % (name, len(x) / sr, f0_med(x, sr), info.language,
                 info.language_probability, txt[:120]), flush=True)

    # 2. master Tap 10 (audio Higgs v3 da qua QC) - cat 3 doan 8 s
    m = ROOT / ".work" / "audio_master_t10.wav"
    if m.exists():
        x, sr = read_wav(m)
        print("  MASTER t10 dur=%.1f s" % (len(x) / sr), flush=True)
        for t in [0.0, 60.0, 300.0]:
            seg = x[int(t * sr):int((t + 8) * sr)]
            segs, info = model.transcribe(seg, language=None, beam_size=5, vad_filter=False,
                                          condition_on_previous_text=False)
            txt = " ".join(s.text.strip() for s in segs).strip()
            print("  MASTER @%5.0fs [lang=%s p=%.2f] %s"
                  % (t, info.language, info.language_probability, txt[:120]), flush=True)
    else:
        print("  thieu master t10", flush=True)


if __name__ == "__main__":
    main()
