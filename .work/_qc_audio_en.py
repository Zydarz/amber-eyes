import subprocess
from pathlib import Path

ff = Path(r".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe")
mp3 = Path(r"02_SAN_XUAT/Tap05_EN/xuat_ban/Tap05_EN_master.mp3")

print(f"Checking {mp3} (exists: {mp3.exists()}, size: {mp3.stat().st_size} bytes)")

# Check silence > 0.3s at -60dB
cmd = [str(ff), "-i", str(mp3), "-af", "silencedetect=noise=-60dB:d=0.3", "-f", "null", "-"]
r = subprocess.run(cmd, capture_output=True, text=True)
silences = [line for line in r.stderr.splitlines() if "silence_start" in line]
print(f"Silences > 0.3s at -60dB: {len(silences)}")
for s in silences[:5]:
    print("  ", s)

# Check ebur128
cmd2 = [str(ff), "-i", str(mp3), "-af", "ebur128=peak=true", "-f", "null", "-"]
r2 = subprocess.run(cmd2, capture_output=True, text=True)
for line in r2.stderr.splitlines()[-20:]:
    if any(k in line for k in ["Integrated loudness", "Loudness range", "True peak"]):
        print("  ", line.strip())
