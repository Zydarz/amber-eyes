import os
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("D:/TEST/Gax/amber-eyes")
W = ROOT / ".work"
PUB = ROOT / "02_SAN_XUAT/Tap02_JA/xuat_ban"
FF = W / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffprobe.exe"

print("--- 3. Tap02_JA.srt ---")
srt_p = PUB / "Tap02_JA.srt"
if srt_p.exists():
    lines = srt_p.read_text(encoding="utf-8").splitlines()
    print(f"SRT exists, {len(lines)} lines")
    print("Last 10 lines of SRT:")
    for l in lines[-10:]:
        print(l)
else:
    print("SRT does not exist!")

print("\n--- 4. Brand Intro ---")
for f in (ROOT / "assets/brand").glob("*JA*"):
    print(f"Found brand: {f.name} ({f.stat().st_size} bytes)")

print("\n--- 5. Stems ---")
stems_dir = W / "stems_JA_t02"
if stems_dir.exists():
    stems = list(stems_dir.glob("*.wav"))
    print(f"Stems: {[s.name for s in stems]}")
else:
    print("Stems dir does not exist!")

print("\n--- 6. Audio master wav ---")
wav_p = W / "audio_master_JA_t02.wav"
if wav_p.exists():
    print(f"WAV exists ({wav_p.stat().st_size} bytes)")
else:
    print("WAV does not exist!")

print("\n--- 7. Stills ---")
stills_dir = W / "video3_JA_t02/stills"
if stills_dir.exists():
    stills = list(stills_dir.glob("*.png"))
    print(f"Stills count: {len(stills)}")
else:
    print("Stills dir does not exist!")
