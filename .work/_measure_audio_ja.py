import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
mp3 = ROOT / "02_SAN_XUAT" / "Tap02_JA" / "xuat_ban" / "Tap02_JA_master.mp3"
wav = ROOT / ".work" / "audio_master_JA_t02.wav"

target = mp3 if mp3.exists() else wav
print(f"Measuring {target} (exists: {target.exists()})...")

# Loudness
r = subprocess.run([str(FF), "-hide_banner", "-i", str(target), "-af",
                    "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
js = r.stderr[r.stderr.rfind("{"): r.stderr.rfind("}") + 1]
m = json.loads(js)
print(f"LUFS: {m['input_i']} (target: -16 ± 1)")
print(f"True Peak: {m['input_tp']} dBFS (target: <= -1.5)")
print(f"LRA: {m['input_lra']}")

# Silences > 0.3s below -60dB
r_sil = subprocess.run([str(FF), "-hide_banner", "-i", str(target), "-af",
                        "silencedetect=noise=-60dB:d=0.3", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
silences = []
for line in r_sil.stderr.splitlines():
    if "silence_duration" in line:
        silences.append(line)
print(f"Silences > 0.3s at -60dB: {len(silences)}")
for s in silences[:10]:
    print("  ", s)
