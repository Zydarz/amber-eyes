import subprocess
import sys
from pathlib import Path
import soundfile as sf
from faster_whisper import WhisperModel

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

W = Path(".work")
FF = W / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe"
MP3 = Path("02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA_master.mp3")

out_sample = W / "_ja_audio_sample.wav"
cmd = [str(FF), "-y", "-ss", "22.5", "-t", "30.0", "-i", str(MP3), "-ar", "16000", "-ac", "1", str(out_sample)]
subprocess.run(cmd, capture_output=True, check=True)

audio_data, sr = sf.read(str(out_sample), dtype="float32")
model = WhisperModel("base", device="cpu", compute_type="int8")
segments, info = model.transcribe(audio_data, language="ja")
for s in segments:
    print(f"[{s.start:.2f} -> {s.end:.2f}] {s.text}")
