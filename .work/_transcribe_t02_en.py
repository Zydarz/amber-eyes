import sys
import time
import json
import subprocess
from pathlib import Path
import soundfile as sf
from faster_whisper import WhisperModel

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe"
AUDIO_MP3 = ROOT / "02_SAN_XUAT/Tap02_EN/xuat_ban/Tap02_EN_master.mp3"
AUDIO_MASTER_WAV = WORK / "audio_master_EN_t02.wav"
WAV_16K = WORK / "speech_full_en_t02_16k.wav"
OUT_JSON = WORK / "speech_full_recognized_en_t02.json"

print(f"Target audio: {AUDIO_MP3}")
if not AUDIO_MP3.exists():
    print("ERROR: Audio master file not found!")
    sys.exit(1)

# 1. Convert to master WAV if not exist or smaller
print("1. Creating audio_master_EN_t02.wav (44.1kHz stereo)...")
t0 = time.time()
subprocess.run([
    str(FF), "-y", "-i", str(AUDIO_MP3),
    "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le",
    str(AUDIO_MASTER_WAV)
], check=True, capture_output=True)
print(f"   audio_master_EN_t02.wav created in {time.time() - t0:.2f}s")

# 2. Convert to 16kHz mono WAV for Whisper
print("2. Creating speech_full_en_t02_16k.wav (16kHz mono)...")
t0 = time.time()
subprocess.run([
    str(FF), "-y", "-i", str(AUDIO_MP3),
    "-ar", "16000", "-ac", "1", "-f", "wav",
    str(WAV_16K)
], check=True, capture_output=True)
print(f"   speech_full_en_t02_16k.wav created in {time.time() - t0:.2f}s")

# 3. Read audio data with soundfile
print("3. Reading 16kHz audio array with soundfile...")
t0 = time.time()
audio_data, sr = sf.read(str(WAV_16K), dtype="float32")
dur = len(audio_data) / sr
print(f"   Read {len(audio_data)} samples ({dur:.2f}s) in {time.time() - t0:.2f}s")

# 4. Transcribe with WhisperModel
print("4. Loading Whisper 'base' model...")
t0 = time.time()
model = WhisperModel("base", device="cpu", compute_type="int8")
print(f"   Model loaded in {time.time() - t0:.2f}s")

print("5. Transcribing audio with VAD filter (language='en')...")
t0 = time.time()
segments, info = model.transcribe(
    audio_data,
    language="en",
    beam_size=5,
    word_timestamps=True,
    vad_filter=True,
    vad_parameters=dict(min_silence_duration_ms=300)
)

results = []
count = 0
for seg in segments:
    count += 1
    words_list = []
    if seg.words:
        for w in seg.words:
            words_list.append({
                "word": w.word,
                "start": round(w.start, 3),
                "end": round(w.end, 3),
                "probability": round(w.probability, 3)
            })
    item = {
        "index": count,
        "start": round(seg.start, 3),
        "end": round(seg.end, 3),
        "duration": round(seg.end - seg.start, 3),
        "text": seg.text.strip(),
        "words": words_list
    }
    results.append(item)
    if count % 20 == 0:
        print(f"   Recognized {count} segments, at audio time {seg.end:.1f}s ({time.time() - t0:.1f}s elapsed)...")

OUT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"6. Done! Total segments: {len(results)} saved to {OUT_JSON} in {time.time() - t0:.2f}s")
