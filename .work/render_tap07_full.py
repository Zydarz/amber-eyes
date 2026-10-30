import os, sys, subprocess, time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
os.environ["AE_EP"] = "07"
os.environ["PYTHONIOENCODING"] = "utf-8"

ROOT = Path(__file__).resolve().parents[1]
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

print("=== BẮT ĐẦU DỰNG HÌNH TẬP 07 (build_video3.py --workers 6) ===")
t0 = time.time()
res1 = subprocess.run([sys.executable, ".work/build_video3.py", "--workers", "6"])
if res1.returncode != 0:
    print(f"LỖI: build_video3.py thoát với mã lỗi {res1.returncode}")
    sys.exit(res1.returncode)

t1 = time.time()
print(f"=== DỰNG HÌNH HOÀN TẤT TRONG {t1 - t0:.1f} GIÂY (~{(t1 - t0)/60:.1f} PHÚT) ===")

print("=== TIẾN HÀNH ĐÓNG GÓI THÀNH PHẨM (package.py --mux) ===")
res2 = subprocess.run([sys.executable, ".work/package.py", "--mux"])
if res2.returncode != 0:
    print(f"LỖI: package.py --mux thoát với mã lỗi {res2.returncode}")
    sys.exit(res2.returncode)

print("=== KIỂM TRA CHẤT LƯỢNG THÀNH PHẨM (QC A9.4) ===")
master_mp4 = ROOT / "02_SAN_XUAT" / "Tap07" / "xuat_ban" / "Tap07_master.mp4"
if not master_mp4.exists():
    print("LỖI: Không tìm thấy file thành phẩm:", master_mp4)
    sys.exit(1)

res3 = subprocess.run([str(FF), "-v", "error", "-i", str(master_mp4), "-f", "null", "-"], capture_output=True, text=True)
if res3.returncode == 0 and not res3.stderr.strip():
    print("QC A9.4 ĐẠT 100%: Giải mã video 0 lỗi, toàn vẹn stream!")
else:
    print("QC A9.4 Cảnh báo:", res3.stderr)

print(f"=== TOÀN BỘ QUÁ TRÌNH HOÀN TẤT TRONG {(time.time() - t0)/60:.1f} PHÚT ===")
print("Thành phẩm sẵn sàng tại:", master_mp4)
