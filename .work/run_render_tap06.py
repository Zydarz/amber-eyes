# -*- coding: utf-8 -*-
"""Script xâu chuỗi dựng hình Tập 06 (Step 9 & Step 10)."""
import os
import subprocess
import sys
import time
from pathlib import Path

os.environ["PYTHONIOENCODING"] = "utf-8"
os.environ["AE_EP"] = "06"

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
LOG_FILE = WORK / "render_tap06.log"

def log(msg):
    t_str = time.strftime("[%Y-%m-%d %H:%M:%S]")
    line = f"{t_str} {msg}"
    print(line, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

log("=== BẮT ĐẦU DỰNG HÌNH TẬP 06 (STEP 9) ===")
start_time = time.time()

# 1. Chạy build_video3.py --workers 6
cmd_render = [sys.executable, str(WORK / "build_video3.py"), "--workers", "6"]
log(f"Chạy lệnh render: {' '.join(cmd_render)}")

r = subprocess.run(cmd_render, cwd=str(ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace")

if r.returncode != 0:
    log(f"LỖI RENDER (code {r.returncode}):\n{r.stderr[-2000:]}")
    sys.exit(r.returncode)

log("ĐÃ RENDER XONG picture.mp4!")
log(f"Thời gian render: {(time.time() - start_time) / 60:.1f} phút")

# 2. Chạy package.py --mux để ghép audio + video
log("=== BẮT ĐẦU ĐÓNG GÓI VIDEO (STEP 10) ===")
cmd_pkg = [sys.executable, str(WORK / "package.py"), "--mux"]
log(f"Chạy lệnh đóng gói: {' '.join(cmd_pkg)}")

r_pkg = subprocess.run(cmd_pkg, cwd=str(ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace")
if r_pkg.returncode != 0:
    log(f"LỖI ĐÓNG GÓI (code {r_pkg.returncode}):\n{r_pkg.stderr[-2000:]}")
    sys.exit(r_pkg.returncode)

log(f"ĐÃ HOÀN TẤT ĐÓNG GÓI! Kết quả:\n{r_pkg.stdout.strip()}")

# 3. Kiểm định chất lượng thành phẩm
master_mp4 = ROOT / "02_SAN_XUAT" / "Tap06" / "xuat_ban" / "Tap06_master.mp4"
if not master_mp4.exists():
    log(f"LỖI: Không tìm thấy file {master_mp4}")
    sys.exit(1)

log(f"Thành phẩm: {master_mp4} ({master_mp4.stat().st_size / (1024*1024):.1f} MB)")
log("=== HOÀN TẤT 100% TIẾN TRÌNH DỰNG VIDEO TẬP 06 ===")
