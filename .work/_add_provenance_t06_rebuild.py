"""Them dong provenance cho vong DUNG LAI Tap06 (03/11/2026).

Quy tac L7: moi tai san phai co dong trong provenance.json.
- File da co dong -> CAP NHAT (them ghi_chu + sha256 moi), khong them trung.
- File chua co   -> THEM moi.
Validator: chan ghi neu trung 'file' hoac file goc bi thay doi.
"""
import hashlib
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("PYTHONIOENCODING", "utf-8")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
PROV = ROOT / "provenance.json"
BAK = ROOT / ".work" / "_cu" / "provenance_truoc_rebuild_t06.json"

DAY = "2026-11-03"

NEW = [
    {
        "file": ".work/_build_video3_split.py",
        "loai": "biến thể của build_video3.py — chia build theo frame, ghi part ra thư mục riêng (env AE_VID)",
        "cong_cu": "viết tay (không sửa build_video3.py dùng chung ⇒ không phát sinh nghĩa vụ hồi quy Tập 01)",
        "ngay": DAY, "prompt": None, "seed": None,
        "dieu_khoan": "mã nội bộ dự án",
        "kiem_tra_thuong_mai": "không áp dụng",
        "ghi_chu": "patch 3 điểm (đều bật/tắt bằng env, mặc định tắt): AE_VID (thư mục part) · AE_PIPE_BUF (buffer pipe 4 MB — A11 #100) · AE_FAST_FINISH (finishing tối ưu, bit-identical — A11 #102)",
    },
    {
        "file": ".work/_bench_render_t06.py",
        "loai": "bộ đo throughput build (4 chế độ: pure / pipe / fast / pipebig)",
        "cong_cu": "viết tay — chạy N tiến trình song song, đo aggregate fps",
        "ngay": DAY, "prompt": None, "seed": None,
        "dieu_khoan": "mã nội bộ dự án", "kiem_tra_thuong_mai": "không áp dụng",
        "ghi_chu": "Đo được: pure 6 tiến trình = 12,6 fps · pipe 4 KB = 8,3 fps · pipe 4 MB = 11,58 fps · pure 10 tiến trình = 13,27 fps (máy bão hoà ở ~13 fps, CPU chỉ 42%)",
    },
    {
        "file": ".work/_bench_fast_check.py",
        "loai": "kiểm chứng finishing() tối ưu BIT-IDENTICAL với bản gốc + đo tốc độ",
        "cong_cu": "viết tay", "ngay": DAY, "prompt": None, "seed": None,
        "dieu_khoan": "mã nội bộ dự án", "kiem_tra_thuong_mai": "không áp dụng",
        "ghi_chu": "Kết quả: 240/240 mẫu khớp byte (0 sai lệch) · 127,8 → 94,0 ms/frame (−26%)",
    },
    {
        "file": ".work/_verify_fast_path.py",
        "loai": "kiểm chứng đường khởi tạo lazy của finishing tối ưu trong chính _build_video3_split.py",
        "cong_cu": "viết tay", "ngay": DAY, "prompt": None, "seed": None,
        "dieu_khoan": "mã nội bộ dự án", "kiem_tra_thuong_mai": "không áp dụng",
        "ghi_chu": "6 frame đối chiếu byte-for-byte trước/sau patch ⇒ OK (bắt được lỗi VIGNETTE=None → AxisError)",
    },
    {
        "file": ".work/_concat_t06_parts.py",
        "loai": "ghép 12 part (A+B) thành picture.mp4 bằng concat -c copy + kiểm frame/DTS",
        "cong_cu": "viết tay", "ngay": DAY, "prompt": None, "seed": None,
        "dieu_khoan": "mã nội bộ dự án", "kiem_tra_thuong_mai": "không áp dụng",
        "ghi_chu": "Cổng chặn: tổng frame phải = int(timeline.total × 30) = 37.751; mỗi part phải có frame > 0 và đúng 1920×1080; DTS không N/A",
    },
    {
        "file": ".work/_qc_lag_t06.py",
        "loai": "đo lag âm thanh–hình của file master bằng tương quan chéo",
        "cong_cu": "viết tay (numpy + ffmpeg)", "ngay": DAY, "prompt": None, "seed": None,
        "dieu_khoan": "mã nội bộ dự án", "kiem_tra_thuong_mai": "không áp dụng",
        "ghi_chu": "Đạt khi |lag| ≤ 40 ms và hệ số tương quan > 0,5 trên đoạn 30 s giữa tập",
    },
    {
        "file": ".work/_add_a11_t06_rebuild.py",
        "loai": "generator thêm mục A11 (quét số, cấp max+1, validator liên tiếp 1..N & không trùng)",
        "cong_cu": "viết tay — theo yêu cầu A11 #95 (không gõ tay)", "ngay": DAY,
        "prompt": None, "seed": None,
        "dieu_khoan": "mã nội bộ dự án", "kiem_tra_thuong_mai": "không áp dụng",
        "ghi_chu": "Thêm 4 mục #100–#103 cho vòng dựng lại Tập 06",
    },
]


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main():
    raw = PROV.read_bytes()
    if raw[:3] == b"\xef\xbb\xbf":
        raise SystemExit("CHẶN - provenance.json có BOM")
    data = json.loads(raw.decode("utf-8"))
    if not isinstance(data, list):
        raise SystemExit("CHẶN - provenance.json không phải list")

    BAK.parent.mkdir(parents=True, exist_ok=True)
    if not BAK.exists():
        BAK.write_bytes(raw)
        print(f"sao luu -> {BAK}")

    have = {x.get("file"): x for x in data}
    added, updated = [], []

    for e in NEW:
        p = ROOT / e["file"]
        if not p.exists():
            raise SystemExit(f"CHẶN - thiếu file {e['file']}")
        e["sha256"] = sha256(p)
        if e["file"] in have:
            have[e["file"]].update(e)
            updated.append(e["file"])
        else:
            data.append(e)
            added.append(e["file"])

    # master mp4: cap nhat dong neu da co
    mp4 = "02_SAN_XUAT/Tap06/xuat_ban/Tap06_master.mp4"
    if mp4 in have:
        have[mp4]["sha256"] = sha256(ROOT / mp4)
        have[mp4]["ngay"] = DAY
        have[mp4]["ghi_chu"] = ("DỰNG LẠI 03/11/2026 sau khi sửa 6 câu kịch bản + 11 chữ trên hình: "
                                "37.751 frame 1920×1080@30, ghép từ 12 part (A+B) concat -c copy; "
                                "audio = Tap06_master.mp3 1258,37 s (bản Higgs v3 mới)")
        updated.append(mp4)

    # --- validator: khong trung 'file' ---
    files = [x.get("file") for x in data]
    dup = sorted({f for f in files if files.count(f) > 1})
    if dup:
        raise SystemExit(f"CHẶN - provenance trùng 'file': {dup}")

    # giu nguyen dang goc: json indent=1 + CRLF (khong BOM)
    body = json.dumps(data, ensure_ascii=False, indent=1)
    out = body.encode("utf-8").replace(b"\n", b"\r\n")
    if b"\x00" in out:
        raise SystemExit("CHẶN - byte NUL")
    PROV.write_bytes(out)
    print(f"provenance: {len(data)} mục (+{len(added)} mới, {len(updated)} cập nhật)")
    for f in added:
        print(f"  + {f}")
    for f in updated:
        print(f"  ~ {f}")


if __name__ == "__main__":
    main()
