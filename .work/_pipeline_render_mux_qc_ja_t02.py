#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pipeline toàn bộ: Dựng hình picture.mp4 -> Mux package -> QC đầu ra toàn diện (Tap02 JA)."""
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "02"
os.environ["PYTHONIOENCODING"] = "utf-8"

FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
LOG = W / "_pipeline_ja_t02.log"


def log(msg):
    ts = time.strftime("[%Y-%m-%d %H:%M:%S]")
    line = f"{ts} {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def run_step(desc, cmd):
    log(f"=== BẮT ĐẦU: {desc} ===")
    t0 = time.time()
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    dt = time.time() - t0
    log(f"Kết thúc: {desc} · rc={r.returncode} · thời gian={dt/60:.2f} phút ({dt:.1f} s)")
    if r.stdout:
        for l in r.stdout.strip().splitlines()[-15:]:
            log(f"  [out] {l}")
    if r.returncode != 0:
        if r.stderr:
            for l in r.stderr.strip().splitlines()[-15:]:
                log(f"  [err] {l}")
        raise SystemExit(f"LỖI TẠI BƯỚC: {desc} (rc={r.returncode})")
    return r.stdout


def main():
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(f"Pipeline Tap02 JA bat dau {time.ctime()}\n")

    # 1. Dựng hình picture.mp4
    run_step("1. Render picture.mp4", [sys.executable, str(W / "_render_picture_ja_t02.py"), "6"])

    # 2. Mux package
    run_step("2. package.py --mux", [sys.executable, str(W / "package.py"), "--mux"])

    # 3. QC final
    out_qc = run_step("3. QC Final", [sys.executable, str(W / "_qc_final_ja_t02.py")])

    # 4. QC Sync A/V
    out_sync = run_step("4. QC Sync A/V", [sys.executable, str(W / "_qc_sync_ja_t02.py")])

    log("=== TẤT CẢ CÁC BƯỚC HOÀN THÀNH THÀNH CÔNG ===")


if __name__ == "__main__":
    main()
