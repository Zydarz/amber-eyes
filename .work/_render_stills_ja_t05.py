# -*- coding: utf-8 -*-
"""Render TOÀN BỘ ảnh tĩnh JA Tap05 + kiểm tra chất lượng (H9)."""
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
os.environ["AE_EP"] = "05"
os.environ["PYTHONIOENCODING"] = "utf-8"

LOG = W / "_stills_ja_t05.log"
t0 = time.time()
with open(LOG, "w", encoding="utf-8") as fh:
    r = subprocess.run([sys.executable, str(W / "build_video3.py"), "--stills", "all"],
                       cwd=ROOT, stdout=fh, stderr=subprocess.STDOUT)
dt = time.time() - t0
print(f"rc={r.returncode} · {dt:.0f} s · log={LOG.name}")
tail = LOG.read_text(encoding="utf-8", errors="replace").splitlines()
print("--- 8 dòng cuối log ---")
for line in tail[-8:]:
    print("   ", line)

sd = W / "video3_JA_t05" / "stills"
shots = json.loads((W / "shots_JA_t05.json").read_text(encoding="utf-8"))["shots"]
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

print(f"\n=== KIỂM TRA {len(ids)} shot ===")
print(f"  thiếu file = {len(missing)} {missing[:10]}")
print(f"  0 byte     = {len(zero)} {zero[:10]}")
print(f"  sai kích thước = {len(badsize)} {badsize[:6]}")
print(f"  cũ (không render mới) = {len(stale)} {stale[:10]}")
extra = sorted(p.stem.replace("shot_", "") for p in sd.glob("shot_*.png")
               if p.stem.replace("shot_", "") not in set(ids))
print(f"  file thừa = {len(extra)} {extra[:10]}")
pass_ok = not (missing or zero or badsize or stale)
print("\nKẾT QUẢ:", "PASS" if pass_ok else "FAIL")
if not pass_ok:
    sys.exit(1)
