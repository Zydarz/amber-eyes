#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chay cho sanh: cho render xong -> package --mux -> QC A9.1/A9.3/A9.4 -> QC P1-P6.

Tu cho toi 1 thong bao khi xong thay vi phai poll lien tuc.
"""
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


def render_running():
    try:
        out = subprocess.run(["tasklist", "/FI", "IMAGENAME eq python.exe", "/FO", "CSV", "/NH"],
                             capture_output=True, text=True, errors="replace").stdout
    except Exception:
        return True
    n = 0
    for line in out.splitlines():
        if "build_video3" in line or "python.exe" in line:
            n += 1
    # khong phan biet duoc command line -> dung tien do log
    return n > 0


def progress():
    lg = W / "_build_video3_t02en.log"
    if not lg.exists():
        return "?"
    lines = [l.strip() for l in lg.read_text(encoding="utf-8", errors="replace").splitlines()
             if "]" in l and "/" in l]
    return lines[-1] if lines else "?"


# ---------------------------------------------------------------- 1. cho render xong
log("[chain] cho build_video3 xong ...")
last = ""
stable = 0
t0 = time.time()
while True:
    p = progress()
    if p != last:
        log("    %s  (%.0f phut)" % (p, (time.time() - t0) / 60))
        last = p
    if PIC.exists() and PIC.stat().st_size > 1_000_000:
        sz = PIC.stat().st_size
        time.sleep(20)
        if PIC.exists() and PIC.stat().st_size == sz:
            stable += 1
            if stable >= 2:
                log("[chain] picture.mp4 da xong (%d byte)" % sz)
                break
        else:
            stable = 0
    time.sleep(15)
    if time.time() - t0 > 7200:
        log("[chain] TIMEOUT 2h")
        raise SystemExit(2)

# ---------------------------------------------------------------- 2. package
for script, args, name in (
    ("package.py", ["--mux"], "package --mux"),
    ("_qc_tap02_final.py", [], "QC A9.1/A9.3/A9.4"),
    ("_qc_t02en_deep.py", [], "QC P1-P6"),
):
    log("[chain] === %s ===" % name)
    t = time.time()
    r = subprocess.run([PY, str(W / script), *args], cwd=ROOT,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    out = (r.stdout or "") + (r.stderr or "")
    lgp = W / ("_qc_%s_t02en.log" % name.split()[0].replace("--", ""))
    lgp.write_text(out, encoding="utf-8")
    log(out[-2500:])
    log("--- %s: exit=%d · %.0f s" % (name, r.returncode, time.time() - t))

log("[chain] XONG")
