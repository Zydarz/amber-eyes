#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 03 — chạy cổng QC bảng shot (A9.2/V3/H10…) cho 3 ngôn ngữ.

Dùng cổng dùng chung .work/_qc_tap02_shots.py với AE_EP=03 (cổng setdefault
nên biến môi trường bên ngoài thắng) + AE_LANG theo từng bản.

Dùng:  py -3 .work/_qc_t03_gates.py
"""
import os
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

LANGS = [("vi", ""), ("en", "en"), ("ja", "ja")]
bad = 0
for lang, ae in LANGS:
    env = dict(os.environ)
    env["AE_EP"] = "03"
    env["AE_LANG"] = ae
    env["PYTHONIOENCODING"] = "utf-8"
    print("=" * 78)
    print(f"### CỔNG QC BẢNG SHOT [{lang}]  (AE_EP=03 AE_LANG={ae or '(vi)'})")
    r = subprocess.run([sys.executable, str(WORK / "_qc_tap02_shots.py")],
                       cwd=ROOT, env=env, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    out = ((r.stdout or "") + (r.stderr or "")).strip()
    print(out)
    print(f"--- rc={r.returncode}")
    if r.returncode != 0:
        bad += 1

print("=" * 78)
print("KẾT LUẬN CỔNG QC:", "3/3 bản ĐẠT" if bad == 0 else f"{bad}/3 bản LỖI")
sys.exit(0 if bad == 0 else 1)
