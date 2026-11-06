#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap03 VN — kiểm riêng các câu bị cờ (audio trong cửa sổ câu đó có đúng lời không?).

Cắt đúng đoạn [start-0.4, end+0.6] của master mp3, chạy Whisper riêng cho từng
đoạn (không VAD để không bỏ sót câu ngắn), rồi so với câu trong timeline.
"""
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import numpy as np
from faster_whisper import WhisperModel

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe"
MP3 = ROOT / "02_SAN_XUAT/Tap03/xuat_ban/Tap03_master.mp3"
WAV16 = WORK / "speech_full_vi_t03_16k.wav"

tl = json.loads((WORK / "timeline_s_t03.json").read_text(encoding="utf-8"))
recog = json.loads((WORK / "speech_full_recognized_vi_t03.json").read_text(encoding="utf-8"))
items = tl["items"]

STOP = set("và của là có được cho trong với những một các như đã khi đến ra "
           "thì nhưng cũng để từ mà này người không".split())
WORD_RE = re.compile(r"[a-z0-9]+", re.I)


def key(t):
    t = unicodedata.normalize("NFC", t or "").lower()
    return [w for w in WORD_RE.findall(t) if w not in STOP]


def sim(a, b):
    if not a or not b:
        return 0.0
    A, B = set(a), set(b)
    return len(A & B) / (len(A | B) ** 0.5) if (A & B) else 0.0


# các câu bị cờ ở cổng trước
FLAG = ["1.03#1", "1.05#6", "1.10#12", "1.13#2", "2.04#7", "4.05#13", "4.05#14"]

import soundfile as sf
audio, sr = sf.read(str(WAV16), dtype="float32")

model = WhisperModel("base", device="cpu", compute_type="int8", cpu_threads=4)

print(f"{'cau':>10s} | {'sim':>5s} | giong do doc")
print("-" * 100)
allok = True
for sid in FLAG:
    it = next(i for i in items if i["id"] == sid)
    a = max(0.0, it["start"] - 0.4)
    b = min(len(audio) / sr, it["end"] + 0.6)
    seg = audio[int(a * sr): int(b * sr)]
    segs, _ = model.transcribe(seg, language="vi", beam_size=5,
                                vad_filter=False, condition_on_previous_text=False)
    txt = " ".join(s.text.strip() for s in segs).strip()
    s = sim(key(it["text"]), key(txt))
    flag = "OK " if s >= 0.45 else "BAD"
    if s < 0.45:
        allok = False
    print(f"{sid:>10s} | {s:5.2f} | {flag} audio[{a:.1f}-{b:.1f}]")
    print(f"{'':>10s} |       |   script: {it['text'][:95]}")
    print(f"{'':>10s} |       |   asr   : {txt[:95]}")
print("-" * 100)
print("KET LUAN:", "TAT CA CAU BI CO KHOIP VOI LUA DOC DUNG" if allok else "CO CAU CHUA KHOIP")
