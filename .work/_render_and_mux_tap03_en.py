#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render video + mux + final QC for Episode 03 EN (Kemper case).

Usage:
  $env:AE_EP="03"; $env:AE_LANG="en"; py -3 .work/_render_and_mux_tap03_en.py
"""
import os
import subprocess
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
os.environ["AE_LANG"] = "en"
os.environ["AE_EP"] = "03"
os.environ["PYTHONIOENCODING"] = "utf-8"
PY = sys.executable


def run(script, args=(), label=None):
    label = label or script
    print(f"\n=== {label} ===", flush=True)
    t0 = time.time()
    cmd = [PY, str(W / script), *args]
    print("CMD:", " ".join(cmd), flush=True)
    proc = subprocess.Popen(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            text=True, encoding="utf-8", errors="replace")
    for line in iter(proc.stdout.readline, ""):
        print(line, end="", flush=True)
    proc.stdout.close()
    rc = proc.wait()
    print(f"--- {label}: exit={rc} · {time.time() - t0:.0f}s", flush=True)
    if rc != 0:
        raise SystemExit(f"FAILED at {label} (exit {rc})")


# 1. Render picture (4 workers for stable Windows handle limits)
run("build_video3.py", ["--workers", "4"], label="Render video frames (build_video3.py --workers 4)")

# 2. Package (mux video + master audio + intro)
run("package.py", ["--mux"], label="Mux package (package.py --mux)")

# 3. Final QC checks
run("_qc_final_generic.py", label="Final QC Verification (_qc_final_generic.py)")

print("\n🎉 ALL STEPS COMPLETED SUCCESSFULLY!")
