# -*- coding: utf-8 -*-
import sys, subprocess, json
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

FFMPEG = Path(r"D:\TEST\Gax\amber-eyes\.work\ffmpeg\ffmpeg-n9.0-latest-win64-lgpl-shared-9.0\bin\ffmpeg.exe")
mp3_in = Path("02_SAN_XUAT/Tap06_EN/xuat_ban/Tap06_EN_master.mp3")
wav_out = Path(".work/audio_master_EN_t06.wav")

print(f"Converting {mp3_in} -> {wav_out}")
cmd = [str(FFMPEG), "-y", "-i", str(mp3_in), "-ar", "48000", "-ac", "2", str(wav_out)]
subprocess.run(cmd, check=True)
print("Converted successfully!")

# Measure volume on wav_out
cmd_vol = [
    str(FFMPEG), "-i", str(wav_out), "-af",
    "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json",
    "-f", "null", "-"
]
res = subprocess.run(cmd_vol, capture_output=True, text=True, encoding="utf-8")
stderr = res.stderr
# parse json block
pos = stderr.rfind("{")
if pos != -1:
    data = json.loads(stderr[pos:])
    print("Master Audio Loudnorm Stats:")
    print(json.dumps(data, indent=2))
