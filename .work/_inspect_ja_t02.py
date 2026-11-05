import json
import subprocess
from pathlib import Path

W = Path(".work")
PUB = Path("02_SAN_XUAT/Tap02_JA/xuat_ban")

print("=== 1. AUDIO MASTER ===")
mp3 = PUB / "Tap02_JA_master.mp3"
if mp3.exists():
    print(f"MP3 exists: {mp3.stat().st_size} bytes")
    ff = W / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffprobe.exe"
    cmd = [str(ff), "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(mp3)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(f"MP3 duration: {res.stdout.strip()} s")
else:
    print("MP3 missing!")

print("=== 2. TIMELINE ===")
tl_file = W / "timeline_s_JA_t02.json"
if tl_file.exists():
    with open(tl_file, "r", encoding="utf-8") as f:
        tl = json.load(f)
    print(f"Timeline total: {tl.get('total')} s, count: {len(tl.get('sentences', []))} sentences")
else:
    print("Timeline missing!")

print("=== 3. SHOTS ===")
shots_file = W / "shots_JA_t02.json"
if shots_file.exists():
    with open(shots_file, "r", encoding="utf-8") as f:
        shots = json.load(f)
    print(f"Shots count: {len(shots)}")
    if shots:
        print(f"First shot: {shots[0].get('id')} ({shots[0].get('t_start')} -> {shots[0].get('t_end')})")
        print(f"Last shot: {shots[-1].get('id')} ({shots[-1].get('t_start')} -> {shots[-1].get('t_end')})")
else:
    print("Shots missing!")

print("=== 4. STEMS ===")
stems_dir = W / "stems_JA_t02"
if stems_dir.exists():
    stems = list(stems_dir.glob("*.wav"))
    print(f"Stems found ({len(stems)}): {[s.name for s in stems]}")
else:
    print("Stems dir does not exist!")

print("=== 5. STILLS ===")
stills_dir = W / "video3_JA_t02/stills"
if stills_dir.exists():
    stills = list(stills_dir.glob("*.png"))
    print(f"Stills count in video3_JA_t02/stills: {len(stills)}")
else:
    print("Stills dir does not exist!")

print("=== 6. BRAND INTRO ===")
for brand in Path("assets/brand").glob("*JA*"):
    print(f"Brand asset: {brand}")
