#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap04 VN — ASR master mp3 theo CHUNK, có checkpoint (JSONL) để chạy lại được.

Ghi từng chunk vào .work/_asr_t04_ja_small_chunks.jsonl (append). Chunk đã xong thì bỏ qua
khi chạy lại -> không mất công nếu tiến trình bị kill.
Cuối cùng ghép thành .work/speech_full_recognized_ja_t04_small.json (định dạng giống
Tập 02: [{index,start,end,duration,text,words}]).
"""
import json
import os
import sys
import time
from pathlib import Path

import numpy as np
import soundfile as sf
from faster_whisper import WhisperModel

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe"
AUDIO_MP3 = ROOT / "02_SAN_XUAT/Tap04_JA/xuat_ban/Tap04_JA_master.mp3"
WAV_16K = WORK / "speech_full_ja_t04_16k.wav"
OUT_JSON = WORK / "speech_full_recognized_ja_t04_small.json"
JSONL = WORK / "_asr_t04_ja_small_chunks.jsonl"

CHUNK = 180.0      # giây mỗi chunk
OVERLAP = 12.0     # chồng lấn giữa 2 chunk
THREADS = 4

# ---- 1. 16k mono wav
if not WAV_16K.exists():
    print("creating 16k wav...", flush=True)
    import subprocess
    subprocess.run([str(FF), "-y", "-v", "error", "-i", str(AUDIO_MP3),
                    "-ar", "16000", "-ac", "1", "-f", "wav", str(WAV_16K)],
                   check=True, capture_output=True)

audio, sr = sf.read(str(WAV_16K), dtype="float32")
dur = len(audio) / sr
print(f"audio {dur:.2f}s @ {sr}Hz", flush=True)

# ---- 2. checkpoint hiện có
done = {}
if JSONL.exists():
    for line in JSONL.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
            done[rec["chunk_start"]] = rec
        except Exception:
            pass
print(f"checkpoint: {len(done)} chunk da xong", flush=True)

# ---- 3. model
model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=THREADS)
print("model loaded", flush=True)

chunks = []
t = 0.0
while t < dur - 0.05:
    chunks.append(t)
    t += CHUNK

t_start = time.time()
with JSONL.open("a", encoding="utf-8") as jf:
    for ci, cs in enumerate(chunks):
        ce = min(dur, cs + CHUNK + OVERLAP)
        if cs in done:
            print(f"[chunk {ci+1}/{len(chunks)}] skip (checkpoint)", flush=True)
            continue
        seg_audio = audio[int(cs * sr): int(ce * sr)]
        segs, _ = model.transcribe(
            seg_audio, language="ja", beam_size=5, word_timestamps=True,
            vad_filter=False, condition_on_previous_text=False,
        )
        out = []
        for s in segs:
            # giữ segment nằm trong lõi chunk (trừ chồng lấn), trừ chunk cuối giữ hết
            if ce < dur - 0.05 and (s.end + cs) > cs + CHUNK:
                continue
            words = []
            if s.words:
                for w in s.words:
                    words.append({"word": w.word,
                                  "start": round(w.start + cs, 3),
                                  "end": round(w.end + cs, 3),
                                  "probability": round(w.probability, 3)})
            out.append({"start": round(s.start + cs, 3), "end": round(s.end + cs, 3),
                        "text": s.text.strip(), "words": words})
        jf.write(json.dumps({"chunk_start": cs, "chunk_end": ce, "segments": out},
                             ensure_ascii=False) + "\n")
        jf.flush()
        el = time.time() - t_start
        print(f"[chunk {ci+1}/{len(chunks)}] {cs:.0f}-{ce:.0f}s "
              f"-> {len(out)} seg | {el:.0f}s elapsed", flush=True)

# ---- 4. gộp
results = []
for cs in sorted(done.keys()):
    pass
# đọc lại toàn bộ checkpoint (bao gồm chunk vừa ghi)
all_chunks = {}
for line in JSONL.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line:
        continue
    rec = json.loads(line)
    all_chunks[rec["chunk_start"]] = rec

for cs in sorted(all_chunks):
    for s in all_chunks[cs]["segments"]:
        results.append(s)

results.sort(key=lambda r: r["start"])
# loại trùng (phòng chồng lấn)
dedup = []
for r in results:
    if dedup and abs(r["start"] - dedup[-1]["start"]) < 0.05 and r["text"] == dedup[-1]["text"]:
        continue
    dedup.append(r)

final = []
for i, r in enumerate(dedup, 1):
    final.append({"index": i, "start": r["start"], "end": r["end"],
                  "duration": round(r["end"] - r["start"], 3),
                  "text": r["text"], "words": r["words"]})

OUT_JSON.write_text(json.dumps(final, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"DONE: {len(final)} segments -> {OUT_JSON}", flush=True)
print(f"first={final[0]['start'] if final else None} last_end={final[-1]['end'] if final else None}", flush=True)
