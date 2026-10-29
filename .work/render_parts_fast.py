import os, sys, math, subprocess, time, json
from multiprocessing import Pool
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
os.environ["AE_EP"] = "07"
os.environ["PYTHONIOENCODING"] = "utf-8"

sys.path.insert(0, str(Path(__file__).parent))
import build_video3 as bv

ROOT = Path(r"D:\TEST\Gax\Audi")
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
PROBE = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"
VD = bv.ED.w("video3")
VD.mkdir(parents=True, exist_ok=True)

N_PARTS = 6
TOTAL_FRAMES = int(bv.TOTAL * bv.FPS)
STEP = math.ceil(TOTAL_FRAMES / N_PARTS)


def is_valid_mp4(path):
    if not path.exists() or path.stat().st_size < 1000000:
        return False
    res = subprocess.run([str(PROBE), "-v", "error", "-select_streams", "v:0",
                         "-show_entries", "stream=codec_name", "-of", "default=noprint_wrappers=1", str(path)],
                         capture_output=True, text=True)
    return res.returncode == 0 and "h264" in res.stdout.lower()


def render_part(k):
    f0 = k * STEP
    f1 = min(TOTAL_FRAMES, (k + 1) * STEP)
    target = VD / f"part_{k:02d}.mp4"

    if is_valid_mp4(target):
        print(f"=== Part {k:02d} ĐÃ CÓ VÀ HỢP LỆ, BỎ QUA ===")
        return True

    print(f"\n=== ĐANG DỰNG PART {k:02d} (khung {f0} -> {f1}, tổng {f1 - f0} khung) ===")
    t_start = time.time()

    # 6 sub-jobs for this part
    sub_step = math.ceil((f1 - f0) / 6)
    sub_jobs = []
    for i in range(6):
        sf0 = f0 + i * sub_step
        sf1 = min(f1, f0 + (i + 1) * sub_step)
        if sf0 < sf1:
            sub_jobs.append((sf0, sf1, VD / f"fix{k}_{i}.mp4"))

    with Pool(len(sub_jobs)) as pool:
        codes = pool.map(bv.work, sub_jobs)
    if any(codes):
        print(f"LỖI: Một sub-worker của part {k} bị lỗi: {codes}")
        return False

    # Concat sub-parts
    fix_lst = VD / f"fix{k}.txt"
    fix_lst.write_text("".join(f"file '{j[2].as_posix()}'\n" for j in sub_jobs), encoding="utf-8")
    subprocess.run([str(FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(fix_lst),
                    "-c", "copy", str(target)], check=True)

    # Clean up temp fix files
    for j in sub_jobs:
        try: j[2].unlink()
        except Exception: pass
    try: fix_lst.unlink()
    except Exception: pass

    t_end = time.time()
    print(f"=== PART {k:02d} HOÀN TẤT TRONG {t_end - t_start:.1f} GIÂY ({target.name}) ===")
    return is_valid_mp4(target)


def main():
    t0 = time.time()
    print(f"Bắt đầu quy trình dựng video Tập 07 ({TOTAL_FRAMES} khung hình ~ {bv.TOTAL:.1f} s)...")

    # Render all 6 parts
    for k in range(N_PARTS):
        success = render_part(k)
        if not success:
            print(f"DỪNG: Không thể dựng thành công part {k:02d}")
            sys.exit(1)

    # Concat all 6 parts into picture.mp4
    print("\n=== GHÉP 6 PARTS THÀNH picture.mp4 ===")
    parts_txt = VD / "parts.txt"
    parts_txt.write_text("".join(f"file '{(VD / f'part_{k:02d}.mp4').as_posix()}'\n" for k in range(N_PARTS)), encoding="utf-8")
    picture_mp4 = VD / "picture.mp4"
    subprocess.run([str(FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(parts_txt),
                    "-c", "copy", str(picture_mp4)], check=True)
    print("Ghép picture.mp4 thành công:", picture_mp4)

    # Mux with audio master
    print("\n=== ĐÓNG GÓI THÀNH PHẨM (package.py --mux) ===")
    res_mux = subprocess.run([sys.executable, ".work/package.py", "--mux"])
    if res_mux.returncode != 0:
        print("LỖI: package.py --mux thất bại!")
        sys.exit(res_mux.returncode)

    # QC A9.4
    print("\n=== KIỂM DUYỆT CUỐI CÙNG QC A9.4 ===")
    master_file = ROOT / "02_SAN_XUAT" / "Tap07" / "xuat_ban" / "Tap07_master.mp4"
    res_qc = subprocess.run([str(FF), "-v", "error", "-i", str(master_file), "-f", "null", "-"],
                            capture_output=True, text=True)
    if res_qc.returncode == 0 and not res_qc.stderr.strip():
        print("QC A9.4: HOÀN HẢO! 0 lỗi giải mã, toàn vẹn stream video và audio.")
    else:
        print("QC A9.4:", res_qc.stderr)

    total_time = (time.time() - t0) / 60
    print(f"\n🎉 TOÀN BỘ VIDEO TẬP 07 ĐÃ ĐƯỢC XUẤT BẢN THÀNH CÔNG TRONG {total_time:.1f} PHÚT!")
    print("Đường dẫn:", master_file)


if __name__ == "__main__":
    main()
