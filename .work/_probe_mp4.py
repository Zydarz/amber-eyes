import json
import subprocess
from pathlib import Path

ffprobe = Path(r".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffprobe.exe")
mp4 = Path(r"02_SAN_XUAT/Tap05_EN/xuat_ban/Tap05_EN_master.mp4")

cmd = [
    str(ffprobe), "-v", "error", "-show_entries",
    "format=duration,size,bit_rate:stream=index,codec_type,codec_name,width,height,r_frame_rate,duration,nb_frames",
    "-of", "json", str(mp4)
]
r = subprocess.run(cmd, capture_output=True, text=True, check=True)
data = json.loads(r.stdout)
fmt = data.get("format", {})
streams = data.get("streams", [])
print(f"Master Video Size: {int(fmt.get('size', 0)) / (1024*1024):.2f} MB")
print(f"Format duration: {float(fmt.get('duration', 0)):.4f} s")
for s in streams:
    c_type = s.get("codec_type")
    dur = float(s.get("duration", 0))
    codec = s.get("codec_name")
    if c_type == "video":
        v_dur = dur
        print(f"Video Stream: {codec}, {s.get('width')}x{s.get('height')} @ {s.get('r_frame_rate')} fps, duration = {v_dur:.4f} s, frames = {s.get('nb_frames')}")
    elif c_type == "audio":
        a_dur = dur
        print(f"Audio Stream: {codec}, duration = {a_dur:.4f} s")

delta = abs(v_dur - a_dur)
print(f"Sync Delta |v_dur - a_dur|: {delta:.4f} s (Threshold <= 0.05 s: {'PASS' if delta <= 0.05 else 'FAIL'})")
