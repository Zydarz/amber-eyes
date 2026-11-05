import os
import subprocess
import sys
import json
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("D:/TEST/Gax/amber-eyes")
W = ROOT / ".work"
PUB = ROOT / "02_SAN_XUAT/Tap02_JA/xuat_ban"
FF = W / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffprobe.exe"
MP4 = PUB / "Tap02_JA_master.mp4"

print("=== 1. FILE MASTER MP4 ===")
if MP4.exists():
    sz = MP4.stat().st_size
    print(f"File: {MP4.name}")
    print(f"Size: {sz} bytes ({sz / (1024*1024):.2f} MB)")
    
    # ffprobe format & stream
    cmd = [
        str(FF), "-v", "error", "-show_entries",
        "format=duration,size,bit_rate:stream=codec_name,width,height,r_frame_rate,nb_frames",
        "-of", "json", str(MP4)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    data = json.loads(res.stdout)
    print("Format info:", data.get("format"))
    print("Streams info:", data.get("streams"))
else:
    print("MP4 NOT FOUND!")

print("\n=== 2. PROVENANCE.JSON ===")
prov_path = ROOT / "provenance.json"
if prov_path.exists():
    prov = json.loads(prov_path.read_text(encoding="utf-8"))
    found = [k for k in prov if "Tap02_JA" in k or "Tap02" in k and "_JA" in k]
    print(f"Entries for Tap02 JA in provenance: {found}")
