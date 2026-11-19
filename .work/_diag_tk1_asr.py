#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thu nghiem ASR tren TK1: tu nhan dien ngon ngu + nhieu model + prompt tieng Viet."""
import json
import pathlib
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap01"

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


def main():
    tl = json.loads((D / "timeline_tk1.json").read_text(encoding="utf-8-sig"))
    x, sr = read_wav(D / "TK1_master_audio.wav")
    picks = [tl[0], tl[2], tl[5]]
    prompt_vi = ("Hồ sơ có thật, dữ kiện có nguồn. Từ đây, tâm lý học tội phạm tách làm "
                 "hai khái niệm: thủ đoạn và chữ ký tâm lý.")

    for mname in ["tiny", "base", "small"]:
        print("\n=== MODEL %s ===" % mname, flush=True)
        model = WhisperModel(mname, device="cpu", compute_type="int8", cpu_threads=4)
        for l in picks:
            seg = x[int(l["start"] * sr):int(l["end"] * sr)]
            # 1. tu nhan dien ngon ngu
            segs, info = model.transcribe(seg, language=None, beam_size=1,
                                          vad_filter=False, condition_on_previous_text=False)
            txt_auto = " ".join(s.text.strip() for s in segs).strip()
            print("  %-11s [auto lang=%s p=%.2f] %s"
                  % (l["id"], info.language, info.language_probability, txt_auto[:110]), flush=True)
            # 2. ep vi + prompt
            segs2, _ = model.transcribe(seg, language="vi", beam_size=5, initial_prompt=prompt_vi,
                                        vad_filter=False, condition_on_previous_text=False)
            txt_vi = " ".join(s.text.strip() for s in segs2).strip()
            print("  %-11s [vi +prompt ] %s" % (l["id"], txt_vi[:110]), flush=True)


if __name__ == "__main__":
    main()
