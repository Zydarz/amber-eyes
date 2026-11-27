#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So sanh bien so ASR tren mp3 moi EN TK2 de tim cau hinh bat duoc duoi file."""
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = sorted(str(p) for p in (ROOT / ".work" / "ffmpeg").glob("*/bin/ffmpeg.exe"))[0]
SRC = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_EN" / "TK2_master_audio.mp3"


def decode(path, sr=16000, fmt="s16le"):
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", "1",
                          "-f", fmt, "-"], capture_output=True, check=True).stdout
    if fmt == "s16le":
        return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    return np.frombuffer(raw, dtype=np.float32).copy()


def run(label, audio, **kw):
    from faster_whisper import WhisperModel
    m = WhisperModel("small", device="cpu", compute_type="int8")
    segs, info = m.transcribe(audio, language="en", **kw)
    segs = list(segs)
    last = segs[-1].end if segs else 0.0
    print(f"\n### {label}")
    print(f"    segs={len(segs)}  info.duration={info.duration:.2f}  last_end={last:.2f}")
    for s in segs[-4:]:
        print(f"      {s.start:6.2f}-{s.end:6.2f}  {s.text.strip()[:70]}")
    return segs


def main():
    a16 = decode(SRC, 16000, "s16le")
    af32 = decode(SRC, 16000, "f32le")
    print(f"decoded s16le={len(a16)/16000:.2f}s  f32le={len(af32)/16000:.2f}s")

    base = dict(beam_size=5, vad_filter=False, condition_on_previous_text=False, word_timestamps=True)
    run("A: s16le beam5 vadF condF", a16, **base)
    run("A2: f32le beam5 vadF condF", af32, **base)
    run("D: s16le vad=True (default params)", a16,
        beam_size=5, vad_filter=True, condition_on_previous_text=False, word_timestamps=True)
    run("E: s16le cond_on_previous_text=True", a16,
        beam_size=5, vad_filter=False, condition_on_previous_text=True, word_timestamps=True)


if __name__ == "__main__":
    main()
