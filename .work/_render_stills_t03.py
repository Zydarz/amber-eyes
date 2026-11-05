#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 03 — render lại ảnh tĩnh cho 3 ngôn ngữ (VN / EN / JA).

Mỗi ngôn ngữ: build_video3.py --stills all  ->  .work/video3{,_EN,_JA}_t03/stills/
Không đụng video, không đụng audio, không đụng phụ đề.

Dùng:  py -3 .work/_render_stills_t03.py
"""
import os
import subprocess
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

LANGS = [("vi", ""), ("en", "en"), ("ja", "ja")]

only = sys.argv[1].lower() if len(sys.argv) > 1 else ""
if only:
    LANGS = [x for x in LANGS if x[0] == only]
    if not LANGS:
        raise SystemExit(f"ngon ngu khong hop le: {only}")

for lang, ae in LANGS:
    env = dict(os.environ)
    env["AE_EP"] = "03"
    env["AE_LANG"] = ae
    env["PYTHONIOENCODING"] = "utf-8"
    t0 = time.time()
    print(f"\n===== RENDER [{lang}] AE_EP=03 AE_LANG={ae or '(vi)'} =====", flush=True)
    r = subprocess.run([sys.executable, str(WORK / "build_video3.py"), "--stills", "all"],
                       cwd=ROOT, env=env, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    out = ((r.stdout or "") + (r.stderr or "")).strip()
    for line in out.splitlines()[-12:]:
        print("   " + line)
    print(f"----- rc={r.returncode} · {time.time() - t0:.1f}s", flush=True)
    if r.returncode != 0:
        print("!!! LOI KHI RENDER", lang, flush=True)
        sys.exit(r.returncode)

print("\nDA RENDER XONG 3 NGON NGU", flush=True)
