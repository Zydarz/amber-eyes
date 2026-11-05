# -*- coding: utf-8 -*-
import sys, subprocess, json
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

FFPROBE = Path(r"D:\TEST\Gax\amber-eyes\.work\ffmpeg\ffmpeg-n9.0-latest-win64-lgpl-shared-9.0\bin\ffprobe.exe")
pic = Path(".work/video3_EN_t06/picture.mp4")

print(f"Picture file exists: {pic.exists()} (size: {pic.stat().st_size / (1024*1024):.2f} MB)")

cmd = [
    str(FFPROBE), "-v", "error", "-show_entries",
    "format=duration:stream=nb_frames,width,height,r_frame_rate,codec_name",
    "-of", "json", str(pic)
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
print("Probe output:")
info = json.loads(res.stdout)
print(json.dumps(info, indent=2))

dur = float(info["format"]["duration"])
tl = json.load(open(".work/timeline_s_EN_t06.json", encoding="utf-8"))
diff = abs(dur - tl["total"])
print(f"Video duration: {dur:.3f} s | Timeline total: {tl['total']:.3f} s | Diff: {diff:.4f} s")
assert diff <= 0.05, f"Duration mismatch {diff} > 0.05s"
print("PASS: picture.mp4 matches timeline ±0.05 s!")
