# -*- coding: utf-8 -*-
"""Transcribe Tap05_JA_master.mp3 using faster-whisper with numpy array input."""
import json
import subprocess
import sys
import time
from pathlib import Path
import soundfile as sf
from faster_whisper import WhisperModel

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
FFMPEG = ROOT / ".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe"
AUDIO_FILE = ROOT / "02_SAN_XUAT/Tap05_JA/xuat_ban/Tap05_JA_master.mp3"
WAV_16K = ROOT / ".work/speech_full_ja_t05_16k.wav"
OUT_JSON = ROOT / ".work/speech_full_recognized_ja_t05.json"

if not WAV_16K.exists():
    print("1. Converting MP3 -> 16kHz mono WAV using ffmpeg...")
    t0 = time.time()
    subprocess.run([
        str(FFMPEG), "-y", "-i", str(AUDIO_FILE),
        "-ar", "16000", "-ac", "1", "-f", "wav", str(WAV_16K)
    ], check=True, capture_output=True)
    print(f"   Converted in {time.time() - t0:.2f}s")
else:
    print("1. Using existing speech_full_ja_t05_16k.wav")

print("2. Reading 16kHz WAV using soundfile...")
audio_data, sr = sf.read(str(WAV_16K), dtype="float32")
print(f"   Audio length: {len(audio_data) / sr:.2f}s, sample rate: {sr}")

print("3. Loading Whisper base model...")
t1 = time.time()
model = WhisperModel("base", device="cpu", compute_type="int8")
print(f"   Model loaded in {time.time() - t1:.2f}s")

print("4. Transcribing audio array (language='ja')...")
t2 = time.time()
segments, info = model.transcribe(
    audio_data,
    language="ja",
    beam_size=5,
    word_timestamps=False,
    vad_filter=True,
    vad_parameters=dict(min_silence_duration_ms=400)
)

results = []
count = 0
for seg in segments:
    count += 1
    item = {
        "index": count,
        "start": round(seg.start, 3),
        "end": round(seg.end, 3),
        "duration": round(seg.end - seg.start, 3),
        "text": seg.text.strip()
    }
    results.append(item)
    if count % 20 == 0:
        print(f"   [{count:3d}] {item['start']:6.2f}s -> {item['end']:6.2f}s: {item['text'][:40]}", flush=True)

OUT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"5. Done! Transcribed {count} segments in {time.time() - t2:.2f}s. Saved to {OUT_JSON}")
