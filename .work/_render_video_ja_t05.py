#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render picture.mp4 cho JA Tap05 (build_video3 --workers 6).

Độ dài picture.mp4 phải khớp timeline.total ± 0.05 s (H14/A9.4).
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "05"
os.environ["PYTHONIOENCODING"] = "utf-8"

WORKERS = int(sys.argv[1]) if len(sys.argv) > 1 else 6
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
PIC = W / "video3_JA_t05" / "picture.mp4"
LOG = W / "_build_video3_ja_t05.log"

tl = json.loads((W / "timeline_s_JA_t05.json").read_text(encoding="utf-8-sig"))
total = tl["total"]
nframes = int(round(total * 30))
print(f"timeline.total = {total:.2f} s · {nframes} khung · workers = {WORKERS}", flush=True)

t0 = time.time()
with open(LOG, "w", encoding="utf-8") as fh:
    r = subprocess.run([sys.executable, str(W / "build_video3.py"), "--workers", str(WORKERS)],
                       cwd=ROOT, stdout=fh, stderr=subprocess.STDOUT)
dt = time.time() - t0
print(f"rc={r.returncode} · {dt/60:.1f} phút · log={LOG.name}", flush=True)
print("--- 8 dòng cuối log ---")
for line in LOG.read_text(encoding="utf-8", errors="replace").splitlines()[-8:]:
    print("   ", line)
if r.returncode != 0:
    raise SystemExit(f"build_video3 THẤT BẠI rc={r.returncode}")

print("\n=== ĐO picture.mp4 ===")
p = subprocess.run([str(FF), "-i", str(PIC)], capture_output=True, text=True,
                   encoding="utf-8", errors="replace")
dur = None
for line in (p.stderr or "").splitlines():
    if "Duration:" in line:
        h, m, s = line.split("Duration:")[1].split(",")[0].strip().split(":")
        dur = int(h) * 3600 + int(m) * 60 + float(s)
print(f"  picture.mp4 = {dur} s")
print(f"  timeline    = {total} s")
print(f"  lệch        = {abs(dur - total):.3f} s  (cho phép +-0.05)")
ok = dur is not None and abs(dur - total) <= 0.05
print("  KẾT QUẢ:", "PASS" if ok else "FAIL")
if not ok:
    sys.exit(1)
