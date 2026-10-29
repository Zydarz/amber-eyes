import subprocess, json, sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

FF = Path(".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe")
mp3 = Path("02_SAN_XUAT/Tap05/xuat_ban/Tap05_master.mp3")

# Loudnorm measurement
r = subprocess.run([str(FF), "-hide_banner", "-i", str(mp3), "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8")
js = r.stderr[r.stderr.rfind("{"): r.stderr.rfind("}") + 1]
m = json.loads(js)

print("LUFS đo được (Input I):", m.get("input_i"))
print("True Peak đo được (Input TP):", m.get("input_tp"))
print("LRA đo được:", m.get("input_lra"))

# Silence detect for silence > 0.3s at -60dB
r2 = subprocess.run([str(FF), "-hide_banner", "-i", str(mp3), "-af", "silencedetect=noise=-60dB:d=0.3", "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8")
silences = [line for line in r2.stderr.splitlines() if "silence_duration" in line]
print(f"Số khoảng câm > 0.3s ở -60dB: {len(silences)}")
if silences:
    for s in silences[:5]:
        print(" ", s)
