#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""package.py --mux cho JA Tap02 + do ket qua (stderr -> file)."""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "02"
os.environ["PYTHONIOENCODING"] = "utf-8"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

LOG = W / "_package_mux_ja_t02.log"
with open(LOG, "w", encoding="utf-8") as fh:
    r = subprocess.run([sys.executable, str(W / "package.py"), "--mux"], cwd=ROOT,
                       stdout=fh, stderr=subprocess.STDOUT)
print("rc =", r.returncode)
print("--- 12 dong cuoi ---")
for line in LOG.read_text(encoding="utf-8", errors="replace").splitlines()[-12:]:
    print("   ", line[:150])

mp4 = ROOT / "02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA_master.mp4"
if mp4.exists():
    p = subprocess.run([str(FF), "-i", str(mp4)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    for line in (p.stderr or "").splitlines():
        if "Duration:" in line or "Stream #" in line:
            print("   ", line.strip()[:130])
    print(f"   file: {mp4.stat().st_size} byte")
else:
    print("KHONG CO file cuoi")
