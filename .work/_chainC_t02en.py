#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chai C: cho picture.mp4 xong -> package --mux -> QC A9 -> QC P1-P6 -> bao cao -> ho so -> G10."""
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
VD = W / "video3_EN_t02"
PIC = VD / "picture.mp4"
os.environ["AE_LANG"] = "en"
os.environ["AE_EP"] = "02"
os.environ["PYTHONIOENCODING"] = "utf-8"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
PY = sys.executable


def log(p):
    print(p, flush=True)


log("[C] cho picture.mp4 ...")
t0 = time.time()
while True:
    if PIC.exists() and PIC.stat().st_size > 1_000_000:
        sz = PIC.stat().st_size
        time.sleep(20)
        if PIC.exists() and PIC.stat().st_size == sz:
            log("[C] picture.mp4 xong (%d byte)" % sz)
            break
    if time.time() - t0 > 3000:
        log("[C] TIMEOUT")
        raise SystemExit(2)
    time.sleep(15)

STEPS = [
    ("package.py", ["--mux"], "_qc_package_t02en.log"),
    ("_qc_tap02_final.py", [], "_qc_tap02_final_t02en.log"),
    ("_qc_t02en_deep.py", [], "_qc_t02en_deep_t02en.log"),
    ("_make_qc_report_t02en.py", [], "_make_qc_report_t02en.log"),
    ("_update_plan_t02en.py", [], "_update_plan_t02en.log"),
    ("voice_role_check.py", [], "_g10_rerun_t02en.log"),
]
for script, args, logname in STEPS:
    log("[C] === %s ===" % script)
    t = time.time()
    r = subprocess.run([PY, str(W / script), *args], cwd=ROOT,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    out = (r.stdout or "") + (r.stderr or "")
    (W / logname).write_text(out, encoding="utf-8")
    log(out[-3500:])
    log("--- %s: exit=%d · %.0f s" % (script, r.returncode, time.time() - t))

log("[C] XONG")
