# -*- coding: utf-8 -*-
import sys, subprocess, json, re
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

FFMPEG = Path(r"D:\TEST\Gax\amber-eyes\.work\ffmpeg\ffmpeg-n9.0-latest-win64-lgpl-shared-9.0\bin\ffmpeg.exe")
wav_out = Path(".work/audio_master_EN_t06.wav")

cmd_vol = [
    str(FFMPEG), "-i", str(wav_out), "-af",
    "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json",
    "-f", "null", "-"
]
res = subprocess.run(cmd_vol, capture_output=True, text=True, encoding="utf-8")
stderr = res.stderr

m = re.findall(r"\{[\s\S]*?\}", stderr)
if m:
    data = json.loads(m[-1])
    print("Master Audio Loudnorm Stats:")
    print(json.dumps(data, indent=2))
    input_i = float(data["input_i"])
    input_tp = float(data["input_tp"])
    print(f"Input I: {input_i:.2f} LUFS | Input TP: {input_tp:.2f} dBFS")
else:
    print("No loudnorm JSON found in stderr")
