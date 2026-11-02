#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render lai TOAN BO anh tinh JA Tap02 + kiem tra tinh trang (stderr -> file, tranh PowerShell)."""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "02"
os.environ["PYTHONIOENCODING"] = "utf-8"

LOG = W / "_stills_ja_t02.log"
t0 = time.time()
with open(LOG, "w", encoding="utf-8") as fh:
    r = subprocess.run([sys.executable, str(W / "build_video3.py"), "--stills", "all"],
                       cwd=ROOT, stdout=fh, stderr=subprocess.STDOUT)
dt = time.time() - t0
print(f"rc={r.returncode} · {dt:.0f} s · log={LOG.name}")
tail = LOG.read_text(encoding="utf-8", errors="replace").splitlines()
print("--- 6 dong cuoi log ---")
for line in tail[-6:]:
    print("   ", line)

sd = W / "video3_JA_t02" / "stills"
shots = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]
ids = [s["id"] for s in shots]
missing, zero, badsize, stale = [], [], [], []
cutoff = time.time() - dt - 5
for sid in ids:
    p = sd / f"shot_{sid}.png"
    if not p.exists():
        missing.append(sid)
        continue
    if p.stat().st_size == 0:
        zero.append(sid)
        continue
    with Image.open(p) as im:
        if im.size != (1920, 1080):
            badsize.append((sid, im.size))
    if p.stat().st_mtime < cutoff:
        stale.append(sid)

print(f"\n=== KIEM TRA {len(ids)} shot ===")
print(f"  thieu file = {len(missing)} {missing[:10]}")
print(f"  0 byte     = {len(zero)} {zero[:10]}")
print(f"  sai kich thuoc = {len(badsize)} {badsize[:6]}")
print(f"  cu (khong render moi) = {len(stale)} {stale[:10]}")
extra = sorted(p.stem.replace("shot_", "") for p in sd.glob("shot_*.png")
               if p.stem.replace("shot_", "") not in set(ids))
print(f"  file thua = {len(extra)} {extra[:10]}")
print("\nKET QUA:", "PASS" if not (missing or zero or badsize or stale) else "FAIL")
