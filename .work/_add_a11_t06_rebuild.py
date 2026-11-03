"""Them muc moi vao bang A11 (TIEU_CHUAN_DUNG_VIDEO.md) — BANG SCRIPT (A11 #95).

Quy tac: doc file -> quet cot '#' -> lay so lon nhat N -> cap so N+1, N+2...
-> KIEM LAI TOAN BANG (phai lien tiep 1..N, khong trung) -> ghi.
Validator chan ghi file neu trung so hoac so khong lien tiep.
"""
import os
import re
import sys
from pathlib import Path

os.environ.setdefault("PYTHONIOENCODING", "utf-8")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DOC = Path(r"D:/TEST/Gax/amber-eyes/00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md")
ROW = re.compile(r"^\|\s*(\d+)\s*\|")

NEW_ROWS = [
    # (bai, cach lam dung)
    (
        "**Pipe 4 KB mặc định của Windows khiến build video mất 34% throughput — đo được, không phải suy đoán** "
        "(Tập 06, 03/11/2026): 6 tiến trình chỉ render (không encode) = **12,6 fps**; cùng 6 tiến trình nhưng đẩy frame "
        "6,2 MB qua pipe cho ffmpeg = **8,3 fps**. Pipe ẩn danh của Windows mặc định chỉ **4 KB** ⇒ mỗi frame phải qua "
        "~1.550 vòng ghi/giác lịch. CPU lúc đó chỉ 330% python + 40% ffmpeg trên 12 luồng ⇒ **không phải kẹt CPU**",
        "Tăng buffer pipe bằng cách **patch `_winapi.CreatePipe`** để `subprocess` tự tạo cả hai đầu (giữ nguyên cơ chế "
        "handle/EOF) ⇒ **11,58 fps**, đạt 92% trần render thuần. **Không** tự tạo pipe rồi trả về: làm vậy "
        "`p2cwrite = -1` ⇒ ffmpeg **không** nhận handle làm stdin ⇒ lỗi `Bad file descriptor`; và phải truyền "
        "`stdin=subprocess.PIPE` cho lời gọi `Popen` nếu không thì `p.stdin` là `None`. Áp dụng ở "
        "`.work/_build_video3_split.py` (biến thể) chứ không sửa `build_video3.py` dùng chung",
    ),
    (
        "**Máy bão hoà ở ~13 fps dù CPU chỉ 42% ⇒ nút thắt là băng thông bộ nhớ, thêm worker KHÔNG giúp** "
        "(Tập 06, 03/11/2026): 6 tiến trình = 12,6 fps · **10 tiến trình = 13,27 fps (+5%)** trong khi mỗi tiến trình "
        "chỉ dùng ~55% CPU ⇒ tổng ~42% của 12 luồng. Kết luận sai kinh niên \"tăng `--workers` sẽ nhanh hơn\" làm "
        "lần build đầu vượt giới hạn 1 giờ của một lệnh bash và bị hủy",
        "Đo **aggregate** ở 2 mức worker (6 vs 10) trước khi quyết cấu hình; nếu tăng worker không tăng aggregate thì "
        "nút thắt là băng thông bộ nhớ ⇒ phải **giảm chi phí mỗi frame**, không phải thêm tiến trình. Đo trong lúc "
        "build bằng `Get-Process python,ffmpeg` (CPU s tích luỹ) để phân biệt kẹt CPU với kẹt băng thông",
    ),
    (
        "**Tối ưu `finishing()` phải BIT-IDENTICAL — và phải tự khởi tạo globals** (Tập 06, 03/11/2026): "
        "`finishing()` khởi tạo `VIGNETTE`/`GRAIN`/`ABUF` **lazy** ở lần gọi đầu; bản tối ưu gọi "
        "`np.repeat(B.VIGNETTE, …)` trước khi globals có giá trị ⇒ `AxisError: axis 2 is out of bounds` trong worker ⇒ "
        "**mọi part ra rỗng**, không ai báo vì lỗi chỉ hiện ở traceback của tiến trình con",
        "Gọi **bản gốc 1 lần** để khởi tạo globals rồi mới dùng giá trị đã khởi tạo (phải giữ tham chiếu tới bản gốc, "
        "tránh tự gọi lại chính bản đã patch ⇒ đệ quy). **Kiểm byte-for-byte** trên ≥ 120 frame × 2 nguồn (mảng ngẫu "
        "nhiên + frame thật) trước khi dùng (A11 #89). Đo được: **127,8 → 94,0 ms/frame (−26%)**, frame sau khi tối ưu "
        "giống hệt bản gọc ⇒ **ảnh tĩnh đã QC vẫn hợp lệ**, không phải render lại",
    ),
    (
        "**Giới hạn 1 giờ của một lệnh bash ⇒ phải chia build theo FRAME rồi ghép nhiều lần** (Tập 06, 03/11/2026): "
        "một lần build 37.751 frame ở 30 fps mất ~73 phút > trần 60 phút ⇒ task bị hủy giữa chừng, 6 part chỉ còn "
        "~3.000 frame mỗi part và **không có moov atom** (ffprobe: `moov atom not found`)",
        "`render(fi)` chỉ phụ thuộc `fi` ⇒ chia theo khoảng frame cho kết quả **y hệt** một lần build liên tục. Dùng "
        "**bản sao** `.work/_build_video3_split.py` (đọc `AE_VID` từ env) để không sửa `build_video3.py` dùng chung ⇒ "
        "không phát sinh nghĩa vụ hồi quy Tập 01 (L9). Chia **theo frame, không theo giây** (`int(t × 30)`) để khớp "
        "tổng: A = [0, 18875) · B = [18875, 37751) ⇒ tổng 37.751. Ghép **một** lần `ffmpeg -f concat -safe 0 -c copy` "
        "(không ghép 2 vòng) và kiểm: tổng frame == `int(timeline.total × 30)`, đủ 1920×1080@30, DTS không N/A",
    ),
]


def main():
    raw = DOC.read_bytes()
    if raw[:3] == b"\xef\xbb\xbf":
        raise SystemExit("CHẶN - file có BOM")
    crlf = b"\r\n" in raw
    text = raw.decode("utf-8")
    lines = text.split("\r\n") if crlf else text.split("\n")

    # --- quet so da dung ---
    nums = []
    for i, L in enumerate(lines):
        m = ROW.match(L)
        if m:
            nums.append((i, int(m.group(1))))
    if not nums:
        raise SystemExit("CHẶN - không tìm thấy dòng bảng A11")
    seq = [n for _, n in nums]
    if len(set(seq)) != len(seq):
        dup = sorted({n for n in seq if seq.count(n) > 1})
        raise SystemExit(f"CHẶN - bảng A11 đang TRÙNG số: {dup}")
    if seq != list(range(1, len(seq) + 1)):
        raise SystemExit(f"CHẶN - số A11 không liên tiếp 1..{len(seq)}: {seq}")
    last_line_idx = nums[-1][0]
    nxt = len(seq) + 1
    print(f"[a11] hiện có {len(seq)} mục (1..{len(seq)}), số mới bắt đầu từ {nxt}")

    new_lines = []
    for k, (b, c) in enumerate(NEW_ROWS):
        num = nxt + k
        cell = lambda s: s.replace("|", "\\|")
        new_lines.append(f"| {num} | {cell(b)} | {cell(c)} |")

    out = lines[:last_line_idx + 1] + new_lines + lines[last_line_idx + 1:]
    body = "\r\n".join(out) if crlf else "\n".join(out)

    # --- kiem lai TOAN BANG sau khi them ---
    chk = [int(ROW.match(L).group(1)) for L in out if ROW.match(L)]
    if len(set(chk)) != len(chk):
        raise SystemExit("CHẶN - sau khi thêm có số trùng")
    if chk != list(range(1, len(chk) + 1)):
        raise SystemExit("CHẶN - sau khi thêm số không liên tiếp")

    data = body.encode("utf-8")
    if b"\x00" in data:
        raise SystemExit("CHẶN - file có byte NUL")
    DOC.write_bytes(data)
    print(f"[a11] đã thêm {len(new_lines)} mục (#{nxt}–#{nxt + len(new_lines) - 1}), tổng {len(chk)} mục, "
          f"liên tiếp 1..{len(chk)}, không trùng")
    for L in new_lines:
        print("  " + L[:150] + " …")


if __name__ == "__main__":
    main()
