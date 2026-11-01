#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chai 2: cho chain 1 xong -> sinh bao cao giam sat + cap nhat ho so + chay lai G10."""
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
os.environ["AE_LANG"] = "en"
os.environ["AE_EP"] = "02"
os.environ["PYTHONIOENCODING"] = "utf-8"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
PY = sys.executable


def log(p):
    print(p, flush=True)


QC_DEEP = W / "_qc__qc_t02en_deep_t02en.log"
CHAIN_LOG = W / "_chain_t02en.log"

log("[chain2] cho chain 1 xong ...")
t0 = time.time()
while True:
    txt = CHAIN_LOG.read_text(encoding="utf-8", errors="replace") if CHAIN_LOG.exists() else ""
    if "[chain] XONG" in txt:
        log("[chain2] chain 1 xong")
        break
    if "TIMEOUT" in txt or "Traceback" in txt:
        log("[chain2] chain 1 co van de:")
        log(txt[-3000:])
        raise SystemExit(2)
    if time.time() - t0 > 7200:
        log("[chain2] TIMEOUT")
        raise SystemExit(3)
    time.sleep(15)

for script, args, name in (
    ("_make_qc_report_t02en.py", [], "sinh BAO_CAO_GIAM_SAT"),
    ("_update_plan_t02en.py", [], "cap nhat ho so"),
    ("voice_role_check.py", [], "G10 chay lai"),
):
    log("[chain2] === %s ===" % name)
    t = time.time()
    r = subprocess.run([PY, str(W / script), *args], cwd=ROOT,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    out = (r.stdout or "") + (r.stderr or "")
    log(out[-3000:])
    log("--- %s: exit=%d · %.0f s" % (name, r.returncode, time.time() - t))

log("[chain2] XONG")
