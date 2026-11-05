import subprocess
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

W = Path(".work")
FF = W / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe"
MP3 = Path("02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA_master.mp3")

# Extract 23.0 to 45.0s (first few sentences) to a small wav file
out_sample = W / "_ja_audio_sample.wav"
cmd = [str(FF), "-y", "-ss", "22.5", "-t", "30.0", "-i", str(MP3), "-ar", "16000", "-ac", "1", str(out_sample)]
subprocess.run(cmd, capture_output=True)

# Transcribe with whisper
import whisper
model = whisper.load_model("base")
res = model.transcribe(str(out_sample), language="ja")
print("Transcribed audio from 22.5s to 52.5s:")
print(res["text"])
