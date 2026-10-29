#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

os.environ["AE_EP"] = "05"
os.environ["PYTHONIOENCODING"] = "utf-8"
ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
OUT = ROOT / "02_SAN_XUAT" / "Tap05" / "xuat_ban" / "Tap05_master.mp4"

print("================================================================================")
print("BAT DAU DUNG HINH TAP 05 — AMBER EYES (6 WORKERS)")
print("================================================================================")
t_start = time.time()

# 1. Dựng video
cmd_render = [sys.executable, str(WORK / "build_video3.py"), "--workers", "6"]
print("Lệnh:", " ".join(cmd_render))
r = subprocess.run(cmd_render, cwd=str(ROOT))
if r.returncode != 0:
    print(f"LỖI: build_video3.py thất bại với mã lỗi {r.returncode}")
    sys.exit(r.returncode)

t_render = time.time() - t_start
print(f"-> Dựng hình thành công trong {t_render/60:.1f} phút!")

# 2. Đóng gói & mux audio
print("\nBAT DAU MUX VIDEO VA AUDIO...")
cmd_mux = [sys.executable, str(WORK / "package.py"), "--mux"]
r2 = subprocess.run(cmd_mux, cwd=str(ROOT))
if r2.returncode != 0:
    print(f"LỖI: package.py thất bại với mã lỗi {r2.returncode}")
    sys.exit(r2.returncode)

# 3. Kiểm định chất lượng thành phẩm (QC)
print("\nKIEM DINH CHAT LUONG THANH PHAM (QC)...")
if not OUT.exists():
    print("LỖI: Không tìm thấy file thành phẩm", OUT)
    sys.exit(1)

# Check decode errors
r_qc = subprocess.run([str(FF), "-v", "error", "-i", str(OUT), "-f", "null", "-"], capture_output=True, text=True)
decode_errors = len(r_qc.stderr.strip().splitlines()) if r_qc.stderr.strip() else 0

# Check duration
r_probe = subprocess.run([str(FF), "-v", "error", "-show_entries", "format=duration,size", "-of", "default=noprint_wrappers=1", str(OUT)], capture_output=True, text=True)

dur = None
size_mb = OUT.stat().st_size / (1024 * 1024)
for line in r_probe.stdout.splitlines():
    if line.startswith("duration="):
        dur = float(line.split("=")[1])

t_total = time.time() - t_start
summary = {
    "status": "SUCCESS",
    "episode": "Tap05",
    "master_mp4": str(OUT),
    "size_mb": round(size_mb, 1),
    "duration_s": round(dur, 2) if dur else None,
    "decode_errors": decode_errors,
    "render_time_min": round(t_render / 60, 1),
    "total_time_min": round(t_total / 60, 1)
}

(WORK / "render_tap05_done.json").write_text(str(summary), encoding="utf-8")

print(f"HOAN TAT TOAN BO!")
print(f"  File: {OUT} ({size_mb:.1f} MB)")
print(f"  Thời lượng: {dur:.2f} s")
print(f"  Lỗi giải mã: {decode_errors}")
print(f"  Thời gian render: {t_render/60:.1f} phút")
print(f"  Tổng thời gian: {t_total/60:.1f} phút")
