import sys
import time
import wave
from pathlib import Path
from mlx_audio.tts.utils import load as load_higgs
from mlx_audio.tts.generate import audio_write

ROOT = Path(".")
print("Loading model...")
t0 = time.time()
model = load_higgs("bosonai/higgs-audio-v3-tts-4b")
print(f"Model loaded in {time.time()-t0:.2f}s")

ref_wav = ROOT / "assets/voice_ref_voxcpm2/H.wav"
ref_txt = (ROOT / "assets/voice_ref_voxcpm2/H.txt").read_text(encoding="utf-8").strip()

print("Pre-encoding reference...")
ref_codes = model.encode_audio(str(ref_wav))
print(f"Ref encoded shape: {getattr(ref_codes, 'shape', None)}")

print("Generating 1 sentence...")
t1 = time.time()
res = list(model.generate(
    text="Một kẻ sát nhân 30 năm lẩn trốn. Lại tự nộp mạng vì một chiếc đĩa mềm màu tím.",
    ref_audio_codes=ref_codes,
    ref_text=ref_txt,
    temperature=0.8,
    top_p=0.95,
    seed=12345,
    fade_in_ms=30.0,
    fade_out_ms=15.0
))
out_test = Path(".work/test_h_out.wav")
audio_write(str(out_test), res[0].audio, res[0].sample_rate)
print(f"Generated test audio in {time.time()-t1:.2f}s, saved to {out_test}")
