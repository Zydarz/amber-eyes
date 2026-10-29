import json
import re
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

FF = Path(".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe")
mp3 = Path("02_SAN_XUAT/Tap04/xuat_ban/Tap04_master.mp3")

# 1. Đo loudness (ebur128)
r1 = subprocess.run([str(FF), "-hide_banner", "-i", str(mp3), "-af", "ebur128", "-f", "null", "-"],
                    capture_output=True, text=True, encoding="utf-8", errors="replace")
print("=== LOUDNORM STATS ===")
print(r1.stderr[-800:])

# 2. Đo silence > 0.3s ở -60 dB (Rule A1 / V4)
r2 = subprocess.run([str(FF), "-hide_banner", "-i", str(mp3), "-af", "silencedetect=noise=-60dB:d=0.3", "-f", "null", "-"],
                    capture_output=True, text=True, encoding="utf-8", errors="replace")
silences = re.findall(r"silence_duration:\s*([\d.]+)", r2.stderr)
print(f"=== SILENCE DETECT (-60dB, >0.3s) ===")
print(f"  Total silence occurrences > 0.3s: {len(silences)}")
if silences:
    print(f"  Durations: {silences[:5]}")
else:
    print("  PASS: 0 khoảng câm tuyệt đối > 0.3 s (ĐẠT Rule A1 / V4)!")

# 3. Timeline check
tl = json.loads(Path(".work/timeline_s_t04.json").read_text(encoding="utf-8"))
print(f"=== TIMELINE STATS ===")
print(f"  Total duration: {tl['total']:.2f} s ({tl['total']/60:.2f} min)")
print(f"  First sentence: {tl['items'][0]['start']} s (yêu cầu 22.8 - 23.5 s)")
print(f"  Last sentence end: {tl['items'][-1]['end']} s")
print(f"  Total sentences: {len(tl['items'])}")

