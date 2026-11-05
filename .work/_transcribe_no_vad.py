import sys
import time
import json
from pathlib import Path
import soundfile as sf
from faster_whisper import WhisperModel

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
WAV_16K = WORK / "speech_full_en_t02_16k.wav"
OUT_JSON = WORK / "speech_full_recognized_en_t02_novad.json"

print("Reading 16kHz audio array (from 22.0s to 1388.0s)...")
audio_data, sr = sf.read(str(WAV_16K), start=int(22.0 * 16000), stop=int(1388.0 * 16000), dtype="float32")
print(f"Read {len(audio_data)} samples ({len(audio_data)/sr:.2f}s)")

model = WhisperModel("base", device="cpu", compute_type="int8")
print("Transcribing without VAD filter...")
t0 = time.time()
segments, info = model.transcribe(
    audio_data,
    language="en",
    beam_size=5,
    word_timestamps=True,
    vad_filter=False
)

results = []
count = 0
for seg in segments:
    count += 1
    # offset by 22.0s
    seg_start = round(seg.start + 22.0, 3)
    seg_end = round(seg.end + 22.0, 3)
    words_list = []
    if seg.words:
        for w in seg.words:
            words_list.append({
                "word": w.word,
                "start": round(w.start + 22.0, 3),
                "end": round(w.end + 22.0, 3),
                "probability": round(w.probability, 3)
            })
    item = {
        "index": count,
        "start": seg_start,
        "end": seg_end,
        "duration": round(seg_end - seg_start, 3),
        "text": seg.text.strip(),
        "words": words_list
    }
    results.append(item)
    if count % 25 == 0:
        print(f"  Recognized {count} segments, at {seg_end:.1f}s ({time.time() - t0:.1f}s elapsed)...")

OUT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Done! {len(results)} segments saved to {OUT_JSON} in {time.time() - t0:.2f}s")
