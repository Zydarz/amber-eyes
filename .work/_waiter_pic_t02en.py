#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Waiter: bao hieu khi picture.mp4 san xong (de task sau bat dau viec nang)."""
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIC = ROOT / ".work" / "video3_EN_t02" / "picture.mp4"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
print("[waiter] cho picture.mp4 ...", flush=True)
t0 = time.time()
while True:
    if PIC.exists() and PIC.stat().st_size > 1_000_000:
        sz = PIC.stat().st_size
        time.sleep(25)
        if PIC.exists() and PIC.stat().st_size == sz:
            print("[waiter] picture.mp4 SAN XONG (%d byte)" % sz, flush=True)
            break
    if time.time() - t0 > 3300:
        print("[waiter] het gio, chua co picture.mp4", flush=True)
        raise SystemExit(2)
    time.sleep(15)
print("[waiter] XONG", flush=True)
