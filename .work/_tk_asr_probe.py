#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Probe: chay ASR cho 1 clip/lang va ghi cache dung ten ma _tk_asr_tk03_<clip>_<lang>.json
Dung:  py -3 .work/_tk_asr_probe.py EN TK1
"""
import json
import pathlib
import sys

import numpy as np
from scipy.signal import resample_poly

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
LANGDIR = {"VN": "Tap03", "EN": "Tap03_EN", "JA": "Tap03_JA"}
LANG_CODE = {"VN": "vi", "EN": "en", "JA": "ja"}


def load16k(path):
    import wave
    w = wave.open(str(path), "rb")
    n, sr, ch = w.getnframes(), w.getframerate(), w.getnchannels()
    d = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0
    w.close()
    if ch > 1:
        d = d.reshape(-1, ch).mean(axis=1)
    if sr != 16000:
        d = resample_poly(d, 16000, sr).astype(np.float32)
    return d


def main():
    lang = sys.argv[1].upper()
    cid = sys.argv[2].upper()
    d = ROOT / "02_SAN_XUAT" / "TIKTOK" / LANGDIR[lang]
    cache = WORK / f"_tk_asr_tk03_{cid}_{lang}.json"
    from faster_whisper import WhisperModel
    m = WhisperModel("small", device="cpu", compute_type="int8")
    audio = load16k(d / f"{cid}_master_audio.wav")
    segs, info = m.transcribe(audio, language=LANG_CODE[lang], beam_size=5, vad_filter=False,
                              word_timestamps=True, condition_on_previous_text=False)
    segs = list(segs)
    words = []
    for s in segs:
        for w in (s.words or []):
            if w.start is None:
                continue
            words.append({"w": w.word.strip(), "s": round(float(w.start), 3), "e": round(float(w.end), 3)})
    data = {"duration": float(info.duration), "words": words,
            "segments": [{"s": round(float(s.start), 3), "e": round(float(s.end), 3), "t": s.text.strip()}
                         for s in segs]}
    cache.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{lang} {cid}: dur={info.duration:.2f}s  segments={len(segs)}  words={len(words)} -> {cache.name}")
    print("--- segments:")
    for s in segs:
        print(f"[{s.start:6.2f}-{s.end:6.2f}] {s.text.strip()[:120]}")
    print("--- first 40 words:")
    for w in words[:40]:
        print(f"  {w['s']:6.2f}-{w['e']:6.2f}  {w['w']!r}")


if __name__ == "__main__":
    main()
