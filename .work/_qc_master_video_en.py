import json
import subprocess
from pathlib import Path

ff = Path(r".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe")
mp4 = Path(r"02_SAN_XUAT/Tap05_EN/xuat_ban/Tap05_EN_master.mp4")
mp3 = Path(r"02_SAN_XUAT/Tap05_EN/xuat_ban/Tap05_EN_master.mp3")

print(f"Master MP4: {mp4} ({mp4.stat().st_size / (1024*1024):.2f} MB)")

# 1. Probing streams
cmd_probe = [
    "ffprobe", "-v", "error", "-show_entries",
    "format=duration,size,bit_rate:stream=index,codec_type,codec_name,width,height,r_frame_rate,duration,nb_frames",
    "-of", "json", str(mp4)
]
try:
    r_probe = subprocess.run(cmd_probe, capture_output=True, text=True, check=True)
    probe_data = json.loads(r_probe.stdout)
    fmt = probe_data.get("format", {})
    streams = probe_data.get("streams", [])
    print(f"Format duration: {float(fmt.get('duration', 0)):.3f} s, bitrate: {int(fmt.get('bit_rate', 0))/1000:.1f} kbps")
    for s in streams:
        print(f"Stream #{s.get('index')} ({s.get('codec_type')}): {s.get('codec_name')}, duration: {float(s.get('duration', 0)):.3f} s, frames: {s.get('nb_frames')}")
        if s.get("codec_type") == "video":
            v_dur = float(s.get("duration", 0))
            v_fps = s.get("r_frame_rate")
            w, h = s.get("width"), s.get("height")
            print(f"  Resolution: {w}x{h}, FPS: {v_fps}")
        elif s.get("codec_type") == "audio":
            a_dur = float(s.get("duration", 0))
    delta = abs(v_dur - a_dur)
    print(f"Sync delta |v_dur - a_dur|: {delta:.4f} s (Threshold <= 0.05 s: {'PASS' if delta <= 0.05 else 'FAIL'})")
except Exception as e:
    print(f"Probe error or fallback: {e}")

# 2. Decode integrity check (0 decode errors)
print("Running full decode test (-f null -)...")
cmd_dec = [str(ff), "-v", "error", "-i", str(mp4), "-f", "null", "-"]
r_dec = subprocess.run(cmd_dec, capture_output=True, text=True)
errs = [l for l in r_dec.stderr.splitlines() if l.strip()]
print(f"Decode errors count: {len(errs)}")
if errs:
    for err in errs[:10]:
        print("  Error:", err)
else:
    print("Full video decode passed with 0 errors!")
