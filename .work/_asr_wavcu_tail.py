#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra duoi WAV CU co chua 2 cau cuoi khong (ASR rieng 15 s cuoi)."""
import glob
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = glob.glob(str(ROOT / ".work" / "ffmpeg" / "*" / "bin" / "ffmpeg.exe"))[0]
SRC = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_EN" / "TK2_master_audio.wav"


def main():
    raw = subprocess.run([FF, "-v", "error", "-i", str(SRC), "-ar", "16000", "-ac", "1",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    a = np.frombuffer(raw, dtype=np.float32).copy()
    total = len(a) / 16000
    print(f"wav cu: {total:.2f}s")
    from faster_whisper import WhisperModel
    m = WhisperModel("small", device="cpu", compute_type="int8")
    for st in [total - 20.0, total - 14.0, total - 8.0]:
        seg = a[int(st * 16000):]
        segs, _ = m.transcribe(seg, language="en", beam_size=5, vad_filter=False,
                               condition_on_previous_text=False, word_timestamps=True)
        segs = list(segs)
        print(f"\n--- tu {st:.2f}s den het ({len(seg)/16000:.2f}s)  nseg={len(segs)}")
        for s in segs:
            print(f"   {st + float(s.start):6.2f}-{st + float(s.end):6.2f}  {s.text.strip()}")


if __name__ == "__main__":
    main()
