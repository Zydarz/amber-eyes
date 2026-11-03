#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chạy nốt pipeline Tap03 EN sau khi chunk C xong:
   1) dem khung chunk C  2) so anh tinh vs video chunk C
   3) ghep 3 chunk -> picture.mp4  4) mux audio -> thanh pham
   5) QC cuoi (2 bo)    6) do so do      7) do lech A/V
Moi buoc dung env AE_EP=03 AE_LANG=en. Dung lai script da viet, khong viet lai logic.
"""
import os
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
ENV = dict(os.environ)
ENV.update({"AE_EP": "03", "AE_LANG": "en", "PYTHONIOENCODING": "utf-8"})

STEPS = [
    ("SO KHUNG CHUNK C", [sys.executable, str(W / "_count_frames_t03_en.py")]),
    ("SO ANH TINH vs VIDEO CHUNK C", [sys.executable, str(W / "_check_stills_vs_video.py"), "C"]),
    ("GHEP + MUX", [sys.executable, str(W / "_concat_mux_t03_en.py")]),
    ("QC CUOI (Tap03 EN)", [sys.executable, str(W / "_qc_en_t03_final.py")]),
    ("QC CUOI (generic A9.1/A9.3/A9.4)", [sys.executable, str(W / "_qc_final_generic.py")]),
    ("DO SO DO", [sys.executable, str(W / "_measure_t03_en.py")]),
    ("DO LECH A/V", [sys.executable, str(W / "_qc_sync_t03_en.py")]),
]

START = int(os.environ.get("AE_START", "1"))
for i, (name, cmd) in enumerate(STEPS, 1):
    if i < START:
        continue
    print(f"\n{'=' * 78}\n[{i}/{len(STEPS)}] {name}\n{'=' * 78}", flush=True)
    r = subprocess.run(cmd, env=ENV, cwd=str(ROOT), text=True, encoding="utf-8", errors="replace",
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = r.stdout or ""
    print(out[-6000:], flush=True)
    if r.returncode != 0:
        print(f"\n### BUOC [{i}] {name} THAT BAI (rc={r.returncode}) — dung lai.", flush=True)
        sys.exit(r.returncode)
    print(f"\n### BUOC [{i}] {name} OK", flush=True)

print("\nTAT CA CAC BUOC DA XONG.")
