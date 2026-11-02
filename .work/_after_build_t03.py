#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Watcher: cho build segment xong -> chay package.py --mux -> chay QC cuoi.

Khong dung `>` hay Out-File: tu ghi file UTF-8.
Chay:  py -3 .work/_after_build_t03.py
"""
import os
import subprocess
import sys
import time
from pathlib import Path

W = Path(r"D:\TEST\Gax\amber-eyes\.work")
LOG = W / "_after_build_t03.log"
BUILD_LOG = W / "_build_seg_t03.log"

env = dict(os.environ)
env["AE_EP"] = "03"
env["PYTHONIOENCODING"] = "utf-8"
env["OPENBLAS_NUM_THREADS"] = "1"
env["OMP_NUM_THREADS"] = "1"


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


def main():
    log("cho build picture.mp4 xong ...")
    deadline = time.time() + 5 * 3600
    while time.time() < deadline:
        txt = ""
        if BUILD_LOG.exists():
            txt = BUILD_LOG.read_text(encoding="utf-8-sig", errors="replace")
        if "DONE picture.mp4" in txt:
            log("build XONG")
            break
        if "LOI" in txt and "concat LOI" in txt:
            log("build LOI (xem _build_seg_t03.log)")
            sys.exit(1)
        time.sleep(20)
    else:
        log("het thoi gian cho build")
        sys.exit(1)

    pic = W / "video3_t03" / "picture.mp4"
    if not pic.exists():
        log("KHONG CO picture.mp4")
        sys.exit(1)
    log(f"picture.mp4 = {pic.stat().st_size / 1e6:.0f} MB")

    log("chay package.py --mux ...")
    t0 = time.time()
    r = subprocess.run([sys.executable, str(W / "package.py"), "--mux"], env=env,
                       cwd=str(W.parent), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       text=True, encoding="utf-8", errors="replace")
    log(f"package.py rc={r.returncode} ({time.time() - t0:.0f}s)")
    tail = (r.stdout or "").strip().splitlines()
    for l in tail[-25:]:
        log("   " + l)
    if r.returncode != 0:
        sys.exit(1)

    log("chay _qc_final_t03.py ...")
    t0 = time.time()
    r = subprocess.run([sys.executable, str(W / "_qc_final_t03.py")], env=env,
                       cwd=str(W.parent), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       text=True, encoding="utf-8", errors="replace")
    log(f"QC rc={r.returncode} ({time.time() - t0:.0f}s)")
    for l in (r.stdout or "").splitlines():
        log(l)
    log("XONG TOAN BO")
    sys.exit(r.returncode)


if __name__ == "__main__":
    main()
