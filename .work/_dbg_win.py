#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = glob.glob(str(ROOT / ".work" / "ffmpeg" / "*" / "bin" / "ffmpeg.exe"))[0]
SRC = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_EN" / "TK2_master_audio.mp3"


def decode(path, sr=16000):
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", "1",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def main():
    a = decode(SRC)
    print("dtype", a.dtype, "len", len(a), "contig", a.flags["C_CONTIGUOUS"])
    from faster_whisper import WhisperModel
    m = WhisperModel("small", device="cpu", compute_type="int8")
    for st in [0.0, 19.0, 38.0, 51.84]:
        seg = a[int(st * 16000): int(min(st + 20.5, len(a) / 16000) * 16000)]
        print(f"\n--- window start={st:.2f}  samples={len(seg)}  dur={len(seg)/16000:.2f}s")
        segs, info = m.transcribe(seg, language="en", beam_size=5, vad_filter=False,
                                   condition_on_previous_text=False, word_timestamps=True)
        segs = list(segs)
        print(f"    nseg={len(segs)} info.duration={info.duration:.2f}")
        for s in segs:
            ws = [w.word.strip() for w in (s.words or [])]
            print(f"    {s.start:6.2f}-{s.end:6.2f}  {s.text.strip()[:60]}   nwords={len(ws)}")


if __name__ == "__main__":
    main()
