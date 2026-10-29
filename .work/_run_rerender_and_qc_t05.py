import subprocess
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

def log(msg):
    now = time.strftime("%H:%M:%S")
    print(f"[{now}] {msg}", flush=True)

log("BẮT ĐẦU QUY TRÌNH RE-RENDER VÀ ĐÓNG GÓI VIDEO TẬP 05")

# Step 1: Rerender part 0
log(">>> [1/5] Đang re-render part_00 (Chứa Shot 1-01 -> 1-04 đã sửa)...")
t0 = time.time()
res = subprocess.run([sys.executable, "-X", "utf8", ".work/rerender_part.py", "0"], env=dict(**dict(__import__('os').environ), AE_EP="05"))
if res.returncode != 0:
    log("LỖI khi re-render part 0!")
    sys.exit(1)
log(f"Hoàn thành part_00 trong {time.time()-t0:.1f} s")

# Step 2: Rerender part 1
log(">>> [2/5] Đang re-render part_01 (Chứa Shot 2-03 -> 2-09 đã sửa)...")
t1 = time.time()
res = subprocess.run([sys.executable, "-X", "utf8", ".work/rerender_part.py", "1"], env=dict(**dict(__import__('os').environ), AE_EP="05"))
if res.returncode != 0:
    log("LỖI khi re-render part 1!")
    sys.exit(1)
log(f"Hoàn thành part_01 trong {time.time()-t1:.1f} s")

# Step 3: Rerender part 2
log(">>> [3/5] Đang re-render part_02 (Chứa Shot 2-10 -> 2-13 đã sửa)...")
t2 = time.time()
res = subprocess.run([sys.executable, "-X", "utf8", ".work/rerender_part.py", "2"], env=dict(**dict(__import__('os').environ), AE_EP="05"))
if res.returncode != 0:
    log("LỖI khi re-render part 2!")
    sys.exit(1)
log(f"Hoàn thành part_02 trong {time.time()-t2:.1f} s")

# Step 4: Package --mux
log(">>> [4/5] Đang mux ghép âm thanh, hình ảnh và tạo package xuất bản...")
t3 = time.time()
res = subprocess.run([sys.executable, "-X", "utf8", ".work/package.py", "--mux"], env=dict(**dict(__import__('os').environ), AE_EP="05"))
if res.returncode != 0:
    log("LỖI khi chạy package --mux!")
    sys.exit(1)
log(f"Mux hoàn tất trong {time.time()-t3:.1f} s")

# Step 5: Full QC verification
log(">>> [5/5] Đang kiểm tra chất lượng toàn bộ file video thành phẩm...")
t4 = time.time()
res = subprocess.run([sys.executable, "-X", "utf8", ".work/_qc_tap05_final.py"], env=dict(**dict(__import__('os').environ), AE_EP="05"))
if res.returncode != 0:
    log("LỖI khi kiểm tra QC!")
    sys.exit(1)

log(f"Toàn bộ quy trình re-render và QC đã thành công rực rỡ trong {(time.time()-t0)/60:.1f} phút!")
